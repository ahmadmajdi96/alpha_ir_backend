import base64
import importlib
import uuid

import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def app_ctx(tmp_path, monkeypatch):
    db_path = tmp_path / "test.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite+pysqlite:///{db_path}")
    monkeypatch.setenv("API_KEY", "test-api-key")
    monkeypatch.setenv("JWT_SECRET", "test-secret")
    monkeypatch.setenv("MINIO_ENDPOINT", "127.0.0.1:1")
    monkeypatch.setenv("MINIO_PUBLIC_ENDPOINT", "http://localhost:9000")
    monkeypatch.setenv("MINIO_DEFAULT_BUCKETS", "shelf-images,sku-training-images,dataset-images")
    monkeypatch.setenv("PUBLIC_BUCKETS", "dataset-images")
    monkeypatch.setenv("UPLOAD_DIR", str(tmp_path / "storage"))

    import app.main as app_main

    importlib.reload(app_main)
    with TestClient(app_main.app) as client:
        yield client, app_main


def _auth_headers():
    return {"apikey": "test-api-key"}


def _create_tenant(client):
    payload = {"name": f"Tenant-{uuid.uuid4()}", "status": "active", "is_active": True}
    response = client.post("/rest/v1/tenants", json=payload, headers=_auth_headers())
    assert response.status_code == 201
    return response.json()


def _create_user_token(client):
    email = f"user-{uuid.uuid4()}@example.com"
    password = "secret123"
    signup_response = client.post(
        "/auth/v1/signup",
        json={"email": email, "password": password, "data": {"full_name": "Test User"}},
    )
    assert signup_response.status_code == 200
    token_response = client.post(
        "/auth/v1/token?grant_type=password",
        json={"email": email, "password": password},
    )
    assert token_response.status_code == 200
    return token_response.json()["access_token"]


def test_list_resources_enforce_default_limit_and_offset(app_ctx):
    client, _ = app_ctx

    for _ in range(130):
        _create_tenant(client)

    list_response = client.get("/rest/v1/tenants", headers=_auth_headers())
    assert list_response.status_code == 200
    assert len(list_response.json()) == 100

    paged_response = client.get(
        "/rest/v1/tenants?limit=20&offset=100&order=created_at.asc",
        headers=_auth_headers(),
    )
    assert paged_response.status_code == 200
    assert len(paged_response.json()) == 20

    invalid_limit_response = client.get("/rest/v1/tenants?limit=0", headers=_auth_headers())
    assert invalid_limit_response.status_code == 400


def test_admins_crud(app_ctx):
    client, _ = app_ctx

    create_response = client.post(
        "/rest/v1/admins",
        json={
            "email": f"admin-{uuid.uuid4()}@example.com",
            "password": "hashed-password",
            "full_name": "Admin User",
            "is_active": True,
        },
        headers=_auth_headers(),
    )
    assert create_response.status_code == 201
    admin_id = create_response.json()["id"]

    list_response = client.get("/rest/v1/admins", headers=_auth_headers())
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    patch_response = client.patch(
        f"/rest/v1/admins?id=eq.{admin_id}",
        json={"phone": "+15551234567"},
        headers=_auth_headers(),
    )
    assert patch_response.status_code == 200
    assert patch_response.json()["phone"] == "+15551234567"

    delete_response = client.delete(f"/rest/v1/admins?id=eq.{admin_id}", headers=_auth_headers())
    assert delete_response.status_code == 204


def test_create_tenant_with_admin_id(app_ctx):
    client, _ = app_ctx

    admin_response = client.post(
        "/rest/v1/admins",
        json={
            "email": f"admin-{uuid.uuid4()}@example.com",
            "password": "hashed-password",
            "full_name": "Admin Owner",
            "is_active": True,
        },
        headers=_auth_headers(),
    )
    assert admin_response.status_code == 201
    admin_id = admin_response.json()["id"]

    tenant_response = client.post(
        "/rest/v1/tenants",
        json={
            "name": f"Tenant-{uuid.uuid4()}",
            "status": "active",
            "is_active": True,
            "admin_id": admin_id,
        },
        headers=_auth_headers(),
    )
    assert tenant_response.status_code == 201
    assert tenant_response.json()["admin_id"] == admin_id


def test_unknown_field_returns_400_not_500(app_ctx):
    client, _ = app_ctx

    response = client.post(
        "/rest/v1/tenants",
        json={
            "name": f"Tenant-{uuid.uuid4()}",
            "status": "active",
            "is_active": True,
            "not_a_real_field": "value",
        },
        headers=_auth_headers(),
    )
    assert response.status_code == 400
    assert "Unknown fields" in response.json()["detail"]


def test_detect_skus_starts_processing_job_and_returns_status(app_ctx, monkeypatch):
    client, app_main = app_ctx
    tenant = _create_tenant(client)

    store_response = client.post(
        "/rest/v1/stores",
        json={"tenant_id": tenant["id"], "name": "Store A"},
        headers=_auth_headers(),
    )
    assert store_response.status_code == 201
    store_id = store_response.json()["id"]

    monkeypatch.setattr(
        app_main,
        "_start_external_job",
        lambda *_args, **_kwargs: {"job_id": "ext-inference-1", "status": "processing", "message": "queued"},
    )

    image_payload = base64.b64encode(b"image-data").decode("ascii")
    detect_response = client.post(
        "/functions/v1/detect-skus",
        json={"imageBase64": image_payload, "tenantId": tenant["id"], "storeId": store_id, "skusToDetect": []},
        headers=_auth_headers(),
    )
    assert detect_response.status_code == 200
    body = detect_response.json()
    assert body["success"] is True
    assert body["status"] == "processing"
    assert body["upstream_job_id"] == "ext-inference-1"

    jobs_response = client.get(
        f"/rest/v1/processing_jobs?tenant_id=eq.{tenant['id']}",
        headers=_auth_headers(),
    )
    assert jobs_response.status_code == 200
    assert len(jobs_response.json()) == 1
    assert jobs_response.json()[0]["status"] == "processing"


def test_training_start_creates_job_and_returns_status(app_ctx, monkeypatch):
    client, app_main = app_ctx
    token = _create_user_token(client)

    dataset_response = client.post(
        "/rest/v1/datasets",
        json={"name": "Dataset A", "status": "draft"},
        headers=_auth_headers(),
    )
    assert dataset_response.status_code == 201
    dataset_id = dataset_response.json()["id"]

    monkeypatch.setattr(
        app_main,
        "_start_external_job",
        lambda *_args, **_kwargs: {"job_id": "ext-train-1", "status": "training", "message": "training started"},
    )

    start_response = client.post(
        "/functions/v1/start-training",
        json={"dataset_id": dataset_id, "epochs": 10, "batch_size": 4},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert start_response.status_code == 200
    body = start_response.json()
    assert body["success"] is True
    assert body["status"] == "training"
    assert body["upstream_job_id"] == "ext-train-1"

    jobs_response = client.get(
        f"/rest/v1/training_jobs?dataset_id=eq.{dataset_id}",
        headers=_auth_headers(),
    )
    assert jobs_response.status_code == 200
    assert len(jobs_response.json()) == 1
    assert jobs_response.json()[0]["status"] == "training"


def test_export_dataset_returns_counts(app_ctx):
    client, _ = app_ctx
    dataset_response = client.post(
        "/rest/v1/datasets",
        json={"name": "Dataset B", "status": "draft"},
        headers=_auth_headers(),
    )
    assert dataset_response.status_code == 201
    dataset_id = dataset_response.json()["id"]

    class_response = client.post(
        "/rest/v1/dataset_classes",
        json={"dataset_id": dataset_id, "name": "cola", "color": "#ff0000"},
        headers=_auth_headers(),
    )
    assert class_response.status_code == 201

    for idx in range(2):
        image_response = client.post(
            "/rest/v1/dataset_images",
            json={"dataset_id": dataset_id, "image_url": f"https://example.com/{idx}.jpg", "is_annotated": False},
            headers=_auth_headers(),
        )
        assert image_response.status_code == 201

    export_response = client.post(
        "/functions/v1/export-dataset",
        json={"dataset_id": dataset_id, "format": "yolov8"},
        headers=_auth_headers(),
    )
    assert export_response.status_code == 200
    body = export_response.json()
    assert body["success"] is True
    assert body["image_count"] == 2
    assert body["class_count"] == 1


def test_public_storage_link_without_auth(app_ctx, monkeypatch):
    client, app_main = app_ctx

    class _FakeObject:
        headers = {"Content-Type": "image/jpeg"}

        def read(self):
            return b"jpeg-bytes"

    class _FakeMinio:
        def get_object(self, bucket, object_key):
            assert bucket == "dataset-images"
            assert object_key.endswith(".jpg")
            return _FakeObject()

    monkeypatch.setattr(app_main, "get_minio_client", lambda: _FakeMinio())

    response = client.get(
        "/storage/v1/object/public/dataset-images/471957d4-0563-4ea7-916d-3286b7dd47f8/file.jpg"
    )
    assert response.status_code == 200
    assert response.content == b"jpeg-bytes"
    assert response.headers["content-type"].startswith("image/jpeg")


def test_private_storage_link_requires_auth(app_ctx):
    client, _ = app_ctx
    response = client.get("/storage/v1/object/dataset-images/some/path.jpg")
    assert response.status_code == 401


def test_model_trainings_crud(app_ctx):
    client, _ = app_ctx

    tenant_response = client.post(
        "/rest/v1/tenants",
        json={"name": f"Tenant-{uuid.uuid4()}", "status": "active", "is_active": True},
        headers=_auth_headers(),
    )
    assert tenant_response.status_code == 201
    tenant_id = tenant_response.json()["id"]

    dataset_response = client.post(
        "/rest/v1/datasets",
        json={"name": "Training Dataset", "status": "draft", "tenant_id": tenant_id},
        headers=_auth_headers(),
    )
    assert dataset_response.status_code == 201
    dataset_id = dataset_response.json()["id"]

    create_response = client.post(
        "/rest/v1/model_trainings",
        json={
            "model_name": "yolov8-retail",
            "model_location": "https://models.example.com/yolov8-retail/v1.pt",
            "tenant_id": tenant_id,
            "dataset_id": dataset_id,
            "status": "training",
        },
        headers=_auth_headers(),
    )
    assert create_response.status_code == 201
    model_training_id = create_response.json()["id"]
    assert create_response.json()["model_name"] == "yolov8-retail"
    assert create_response.json()["model_location"] == "https://models.example.com/yolov8-retail/v1.pt"
    assert create_response.json()["tenant_id"] == tenant_id
    assert create_response.json()["dataset_id"] == dataset_id
    assert create_response.json()["status"] == "training"
    assert create_response.json()["created_at"]

    list_response = client.get("/rest/v1/model_trainings?order=created_at.desc", headers=_auth_headers())
    assert list_response.status_code == 200
    assert len(list_response.json()) >= 1

    patch_response = client.patch(
        f"/rest/v1/model_trainings?id=eq.{model_training_id}",
        json={"status": "completed"},
        headers=_auth_headers(),
    )
    assert patch_response.status_code == 200
    assert patch_response.json()["status"] == "completed"

    delete_response = client.delete(
        f"/rest/v1/model_trainings?id=eq.{model_training_id}",
        headers=_auth_headers(),
    )
    assert delete_response.status_code == 204
