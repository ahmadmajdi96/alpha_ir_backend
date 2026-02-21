import base64
import json
import os
import time
import uuid
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

BASE_URL = os.getenv("TEST_BASE_URL", "http://127.0.0.1:8787")
API_KEY = os.getenv("API_KEY", "super-api-key-change-me")

report = []
expectation_failures = []


def encode_multipart_formdata(field_name: str, filename: str, content: bytes, content_type: str):
    boundary = f"----ShelfVisionBoundary{uuid.uuid4().hex}"
    lines = []
    lines.append(f"--{boundary}".encode())
    lines.append(
        (
            f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"'
        ).encode()
    )
    lines.append(f"Content-Type: {content_type}".encode())
    lines.append(b"")
    lines.append(content)
    lines.append(f"--{boundary}--".encode())
    lines.append(b"")
    body = b"\r\n".join(lines)
    return body, f"multipart/form-data; boundary={boundary}"


def call_api(name, method, path, payload=None, headers=None, raw_body=None, content_type=None):
    url = f"{BASE_URL}{path}"
    req_headers = {"apikey": API_KEY}
    if headers:
        req_headers.update(headers)

    body = None
    payload_repr = payload

    if raw_body is not None:
        body = raw_body
        if content_type:
            req_headers["Content-Type"] = content_type
        if payload is None:
            payload_repr = f"<raw-bytes:{len(raw_body)}>"
    elif payload is not None:
        body = json.dumps(payload).encode("utf-8")
        req_headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=body, method=method, headers=req_headers)

    status = None
    response_text = ""
    response_json = None

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            response_text = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        status = e.code
        response_text = e.read().decode("utf-8", errors="replace")
    except Exception as e:
        status = 0
        response_text = str(e)

    try:
        response_json = json.loads(response_text) if response_text else None
    except json.JSONDecodeError:
        response_json = response_text

    entry = {
        "name": name,
        "method": method,
        "path": path,
        "request_payload": payload_repr,
        "status_code": status,
        "response": response_json,
    }
    report.append(entry)
    return status, response_json


def ensure(status, expected, name):
    if status != expected:
        expectation_failures.append(
            {"name": name, "expected_status": expected, "actual_status": status}
        )


def main():
    run_id = int(time.time())
    email = f"qa_{run_id}@example.com"
    password = "secret123"

    # Health
    call_api("Health", "GET", "/health", payload=None, headers={"apikey": API_KEY})

    # Auth
    status, signup = call_api(
        "Auth Signup",
        "POST",
        "/auth/v1/signup",
        payload={"email": email, "password": password, "data": {"full_name": "QA User"}},
        headers={"apikey": API_KEY},
    )
    ensure(status, 200, "Auth Signup")
    user_id = signup["user"]["id"]

    status, token_data = call_api(
        "Auth Token Password",
        "POST",
        "/auth/v1/token?grant_type=password",
        payload={"email": email, "password": password},
        headers={"apikey": API_KEY},
    )
    ensure(status, 200, "Auth Token Password")
    access_token = token_data["access_token"]

    status, _ = call_api(
        "Auth Logout",
        "POST",
        "/auth/v1/logout",
        payload=None,
        headers={"Authorization": f"Bearer {access_token}", "apikey": API_KEY},
    )
    ensure(status, 204, "Auth Logout")

    # Core resources
    status, tenant = call_api(
        "Create Tenant",
        "POST",
        "/rest/v1/tenants",
        payload={"name": f"Tenant-{run_id}", "status": "active", "is_active": True},
    )
    ensure(status, 201, "Create Tenant")
    tenant_id = tenant["id"]

    call_api("List Tenants", "GET", "/rest/v1/tenants?select=*&status=eq.active")

    status, _ = call_api(
        "Update Tenant",
        "PATCH",
        f"/rest/v1/tenants?id=eq.{tenant_id}",
        payload={"logo_url": "https://example.com/logo.png"},
    )
    ensure(status, 200, "Update Tenant")

    status, store = call_api(
        "Create Store",
        "POST",
        "/rest/v1/stores",
        payload={"tenant_id": tenant_id, "name": "Main Store", "city": "Cairo", "country": "EG"},
    )
    ensure(status, 201, "Create Store")
    store_id = store["id"]

    call_api("List Stores", "GET", f"/rest/v1/stores?tenant_id=eq.{tenant_id}&select=*")

    status, _ = call_api(
        "Update Store",
        "PATCH",
        f"/rest/v1/stores?id=eq.{store_id}",
        payload={"address": "Street 123"},
    )
    ensure(status, 200, "Update Store")

    status, category = call_api(
        "Create Category",
        "POST",
        "/rest/v1/product_categories",
        payload={"tenant_id": tenant_id, "name": "Beverages", "description": "Drinks"},
    )
    ensure(status, 201, "Create Category")
    category_id = category["id"]

    call_api("List Categories", "GET", f"/rest/v1/product_categories?tenant_id=eq.{tenant_id}")

    status, sku = call_api(
        "Create SKU",
        "POST",
        "/rest/v1/skus",
        payload={
            "tenant_id": tenant_id,
            "category_id": category_id,
            "name": "Cola 330ml",
            "description": "Soda",
            "barcode": "1234567890",
            "is_active": True,
            "training_status": "completed",
        },
    )
    ensure(status, 201, "Create SKU")
    sku_id = sku["id"]

    call_api(
        "List SKUs",
        "GET",
        f"/rest/v1/skus?tenant_id=eq.{tenant_id}&category_id=eq.{category_id}&is_active=eq.true&training_status=eq.completed&select=*",
    )

    status, sku_image = call_api(
        "Create SKU Image",
        "POST",
        "/rest/v1/sku_images",
        payload={"sku_id": sku_id, "image_url": "https://example.com/sku.jpg"},
    )
    ensure(status, 201, "Create SKU Image")
    sku_image_id = sku_image["id"]

    call_api("List SKU Images", "GET", f"/rest/v1/sku_images?sku_id=eq.{sku_id}")

    status, shelf = call_api(
        "Create Shelf",
        "POST",
        "/rest/v1/shelves",
        payload={"tenant_id": tenant_id, "store_id": store_id, "name": "Aisle A Shelf 1", "width_cm": 120},
    )
    ensure(status, 201, "Create Shelf")
    shelf_id = shelf["id"]

    call_api("List Shelves", "GET", f"/rest/v1/shelves?tenant_id=eq.{tenant_id}&store_id=eq.{store_id}&select=*")

    status, _ = call_api(
        "Update Shelf",
        "PATCH",
        f"/rest/v1/shelves?id=eq.{shelf_id}",
        payload={"location_in_store": "Near cashier"},
    )
    ensure(status, 200, "Update Shelf")

    status, shelf_product = call_api(
        "Create Shelf Product",
        "POST",
        "/rest/v1/shelf_products",
        payload={"shelf_id": shelf_id, "sku_id": sku_id, "expected_facings": 5, "position_order": 1},
    )
    ensure(status, 201, "Create Shelf Product")
    shelf_product_id = shelf_product["id"]

    call_api("List Shelf Products", "GET", f"/rest/v1/shelf_products?shelf_id=eq.{shelf_id}")

    status, shelf_image = call_api(
        "Create Shelf Image Record",
        "POST",
        "/rest/v1/shelf_images",
        payload={"shelf_id": shelf_id, "image_url": "https://example.com/shelf.jpg"},
    )
    ensure(status, 201, "Create Shelf Image Record")

    call_api("List Shelf Images", "GET", f"/rest/v1/shelf_images?shelf_id=eq.{shelf_id}")

    status, template = call_api(
        "Create Planogram Template",
        "POST",
        "/rest/v1/planogram_templates",
        payload={
            "tenant_id": tenant_id,
            "store_id": store_id,
            "shelf_id": shelf_id,
            "name": "Template 1",
            "status": "active",
            "layout": [{"sku_id": sku_id, "facings": 5}],
        },
    )
    ensure(status, 201, "Create Planogram Template")
    template_id = template["id"]

    call_api("List Planogram Templates", "GET", f"/rest/v1/planogram_templates?tenant_id=eq.{tenant_id}&status=eq.active&select=*")

    status, _ = call_api(
        "Update Planogram Template",
        "PATCH",
        f"/rest/v1/planogram_templates?id=eq.{template_id}",
        payload={"description": "Updated template"},
    )
    ensure(status, 200, "Update Planogram Template")

    status, _ = call_api(
        "Create Planogram Version",
        "POST",
        "/rest/v1/planogram_versions",
        payload={"template_id": template_id, "version_number": 1, "layout": [{"sku_id": sku_id}]},
    )
    ensure(status, 201, "Create Planogram Version")

    call_api("List Planogram Versions", "GET", f"/rest/v1/planogram_versions?template_id=eq.{template_id}&order=version_number.desc")

    status, _ = call_api(
        "Create Compliance Scan",
        "POST",
        "/rest/v1/compliance_scans",
        payload={
            "template_id": template_id,
            "shelf_image_id": shelf_image["id"],
            "image_url": "https://example.com/scan.jpg",
            "compliance_score": 92.5,
            "total_expected": 10,
            "total_found": 9,
            "total_missing": 1,
            "total_extra": 0,
        },
    )
    ensure(status, 201, "Create Compliance Scan")

    call_api("List Compliance Scans", "GET", f"/rest/v1/compliance_scans?template_id=eq.{template_id}&order=created_at.desc")

    # User access and notifications
    call_api("List Profiles", "GET", "/rest/v1/profiles")

    status, _ = call_api(
        "Update Profile",
        "PATCH",
        f"/rest/v1/profiles?user_id=eq.{user_id}",
        payload={"username": "qa_user", "full_name": "QA Updated"},
    )
    ensure(status, 200, "Update Profile")

    status, _ = call_api(
        "Create User Role",
        "POST",
        "/rest/v1/user_roles",
        payload={"user_id": user_id, "role": "tenant_admin"},
    )
    ensure(status, 201, "Create User Role")

    call_api("List User Roles", "GET", f"/rest/v1/user_roles?user_id=eq.{user_id}")

    status, user_store_access = call_api(
        "Create User Store Access",
        "POST",
        "/rest/v1/user_store_access",
        payload={"user_id": user_id, "store_id": store_id},
    )
    ensure(status, 201, "Create User Store Access")

    call_api("List User Store Access", "GET", f"/rest/v1/user_store_access?user_id=eq.{user_id}&store_id=eq.{store_id}")

    status, user_shelf_access = call_api(
        "Create User Shelf Access",
        "POST",
        "/rest/v1/user_shelf_access",
        payload={"user_id": user_id, "shelf_id": shelf_id},
    )
    ensure(status, 201, "Create User Shelf Access")

    call_api("List User Shelf Access", "GET", f"/rest/v1/user_shelf_access?user_id=eq.{user_id}&shelf_id=eq.{shelf_id}")

    status, notification = call_api(
        "Create Notification",
        "POST",
        "/rest/v1/notifications",
        payload={
            "user_id": user_id,
            "tenant_id": tenant_id,
            "title": "Low Stock",
            "message": "SKU below threshold",
            "type": "alert",
            "is_read": False,
            "metadata": {"sku_id": sku_id},
        },
    )
    ensure(status, 201, "Create Notification")
    notification_id = notification["id"]

    call_api("List Notifications", "GET", f"/rest/v1/notifications?user_id=eq.{user_id}&is_read=eq.false")

    status, _ = call_api(
        "Patch Notification",
        "PATCH",
        f"/rest/v1/notifications?id=eq.{notification_id}",
        payload={"is_read": True},
    )
    ensure(status, 200, "Patch Notification")

    # RPC
    status, _ = call_api(
        "RPC Check Tenant Quota",
        "POST",
        "/rest/v1/rpc/check_tenant_quota",
        payload={"_tenant_id": tenant_id},
    )
    ensure(status, 200, "RPC Check Tenant Quota")

    status, _ = call_api(
        "RPC Increment Usage Metric",
        "POST",
        "/rest/v1/rpc/increment_usage_metric",
        payload={"_tenant_id": tenant_id, "_period_type": "monthly", "_images_count": 2},
    )
    ensure(status, 200, "RPC Increment Usage Metric")

    status, _ = call_api(
        "RPC Get User Tenant ID",
        "POST",
        "/rest/v1/rpc/get_user_tenant_id",
        payload={"_user_id": user_id},
    )
    ensure(status, 200, "RPC Get User Tenant ID")

    status, _ = call_api(
        "RPC Has Role",
        "POST",
        "/rest/v1/rpc/has_role",
        payload={"_user_id": user_id, "_role": "tenant_admin"},
    )
    ensure(status, 200, "RPC Has Role")

    # Functions
    fake_image = base64.b64encode(b"fake-image-bytes").decode()
    status, detect_result = call_api(
        "Function Detect SKUs",
        "POST",
        "/functions/v1/detect-skus",
        payload={
            "imageBase64": fake_image,
            "tenantId": tenant_id,
            "storeId": store_id,
            "skusToDetect": [{"id": sku_id, "name": "Cola 330ml", "imageUrls": ["https://example.com/sku.jpg"]}],
        },
    )
    ensure(status, 200, "Function Detect SKUs")

    status, _ = call_api(
        "Function Roboflow Detect",
        "POST",
        "/functions/v1/roboflow-detect",
        payload={"imageUrl": "https://example.com/shelf.jpg", "shelfId": shelf_id, "tenantId": tenant_id},
    )
    ensure(status, 200, "Function Roboflow Detect")

    # Storage
    shelf_file = b"fake-jpeg-shelf-data"
    shelf_body, shelf_ct = encode_multipart_formdata("file", "shelf.jpg", shelf_file, "image/jpeg")
    status, _ = call_api(
        "Storage Upload Shelf Image",
        "POST",
        f"/storage/v1/object/shelf-images/{tenant_id}/2026-02-18/shelf.jpg",
        payload={"file": "<binary image/jpeg 20 bytes>"},
        raw_body=shelf_body,
        content_type=shelf_ct,
    )
    ensure(status, 200, "Storage Upload Shelf Image")

    call_api(
        "Storage Download Shelf Image",
        "GET",
        f"/storage/v1/object/shelf-images/{tenant_id}/2026-02-18/shelf.jpg",
    )

    sku_file = b"fake-jpeg-sku-training-data"
    sku_body, sku_ct = encode_multipart_formdata("file", "sku.jpg", sku_file, "image/jpeg")
    status, _ = call_api(
        "Storage Upload SKU Training Image",
        "POST",
        f"/storage/v1/object/sku-training-images/{tenant_id}/{sku_id}/sku.jpg",
        payload={"file": "<binary image/jpeg 27 bytes>"},
        raw_body=sku_body,
        content_type=sku_ct,
    )
    ensure(status, 200, "Storage Upload SKU Training Image")

    call_api(
        "Storage Download SKU Training Image",
        "GET",
        f"/storage/v1/object/sku-training-images/{tenant_id}/{sku_id}/sku.jpg",
    )

    # Read-only analytics resources
    call_api("List Detections", "GET", f"/rest/v1/detections?tenant_id=eq.{tenant_id}&store_id=eq.{store_id}&order=processed_at.desc")
    call_api("List Usage Metrics", "GET", f"/rest/v1/usage_metrics?tenant_id=eq.{tenant_id}&period_type=eq.monthly")
    call_api("List Models", "GET", f"/rest/v1/models?tenant_id=eq.{tenant_id}")
    call_api("List Processing Jobs", "GET", f"/rest/v1/processing_jobs?tenant_id=eq.{tenant_id}&status=eq.pending")
    call_api("List Detection Results", "GET", "/rest/v1/detection_results?job_id=eq.non-existent")

    # Cleanup checks for deletes
    status, _ = call_api("Delete SKU Image", "DELETE", f"/rest/v1/sku_images?id=eq.{sku_image_id}")
    ensure(status, 204, "Delete SKU Image")

    status, _ = call_api("Delete User Store Access", "DELETE", f"/rest/v1/user_store_access?id=eq.{user_store_access['id']}")
    ensure(status, 204, "Delete User Store Access")

    status, _ = call_api("Delete User Shelf Access", "DELETE", f"/rest/v1/user_shelf_access?id=eq.{user_shelf_access['id']}")
    ensure(status, 204, "Delete User Shelf Access")

    status, _ = call_api("Delete Shelf Product", "DELETE", f"/rest/v1/shelf_products?id=eq.{shelf_product_id}")
    ensure(status, 204, "Delete Shelf Product")

    status, _ = call_api("Delete SKU", "DELETE", f"/rest/v1/skus?id=eq.{sku_id}")
    ensure(status, 204, "Delete SKU")

    status, _ = call_api("Delete Category", "DELETE", f"/rest/v1/product_categories?id=eq.{category_id}")
    ensure(status, 204, "Delete Category")

    status, _ = call_api("Delete Shelf", "DELETE", f"/rest/v1/shelves?id=eq.{shelf_id}")
    ensure(status, 204, "Delete Shelf")

    status, _ = call_api("Delete Store", "DELETE", f"/rest/v1/stores?id=eq.{store_id}")
    ensure(status, 204, "Delete Store")

    status, _ = call_api("Delete Tenant", "DELETE", f"/rest/v1/tenants?id=eq.{tenant_id}")
    ensure(status, 204, "Delete Tenant")

    timestamp = datetime.now(timezone.utc).isoformat()
    report_dir = "/app/test_reports"
    os.makedirs(report_dir, exist_ok=True)

    json_path = os.path.join(report_dir, "api_test_report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "generated_at": timestamp,
                "base_url": BASE_URL,
                "total_tests": len(report),
                "passed": sum(1 for r in report if 200 <= r["status_code"] < 300),
                "failed": sum(1 for r in report if not (200 <= r["status_code"] < 300)),
                "expectation_failures_count": len(expectation_failures),
                "expectation_failures": expectation_failures,
                "results": report,
            },
            f,
            indent=2,
        )

    md_path = os.path.join(report_dir, "api_test_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# ShelfVision API Test Report\n\n")
        f.write(f"- Generated at: {timestamp}\n")
        f.write(f"- Base URL: {BASE_URL}\n")
        f.write(f"- Total tests: {len(report)}\n")
        f.write(f"- Passed (2xx): {sum(1 for r in report if 200 <= r['status_code'] < 300)}\n")
        f.write(f"- Failed (non-2xx): {sum(1 for r in report if not (200 <= r['status_code'] < 300))}\n")
        f.write(f"- Expectation failures: {len(expectation_failures)}\n\n")

        if expectation_failures:
            f.write("## Expectation Failures\n")
            for ef in expectation_failures:
                f.write(
                    f"- {ef['name']}: expected `{ef['expected_status']}`, got `{ef['actual_status']}`\n"
                )
            f.write("\n")

        for i, r in enumerate(report, start=1):
            f.write(f"## {i}. {r['name']}\n")
            f.write(f"- Method: `{r['method']}`\n")
            f.write(f"- Path: `{r['path']}`\n")
            f.write(f"- Status: `{r['status_code']}`\n")
            f.write("- Request payload:\n")
            f.write("```json\n")
            f.write(json.dumps(r["request_payload"], indent=2))
            f.write("\n```\n")
            f.write("- Response:\n")
            f.write("```json\n")
            f.write(json.dumps(r["response"], indent=2))
            f.write("\n```\n\n")

    print(
        json.dumps(
            {
                "ok": len(expectation_failures) == 0,
                "json_report": json_path,
                "md_report": md_path,
                "total": len(report),
                "expectation_failures": len(expectation_failures),
            }
        )
    )


if __name__ == "__main__":
    main()
