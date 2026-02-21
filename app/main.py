import base64
import io
import logging
import os
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

from fastapi import Depends, FastAPI, File, Form, Header, HTTPException, Query, Request, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from minio import Minio
from minio.error import S3Error
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from sqlalchemy import JSON, Boolean, DateTime, Float, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


# -----------------------------
# Configuration
# -----------------------------
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://shelfvision:shelfvision@db:5432/shelfvision",
)
JWT_SECRET = os.getenv("JWT_SECRET", "change-me")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
API_KEY = os.getenv("API_KEY", "change-me")
UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "/data/storage"))
CORS_ALLOW_ORIGINS = os.getenv(
    "CORS_ALLOW_ORIGINS",
    "*",
)
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "minio:9090")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin")
MINIO_SECURE = os.getenv("MINIO_SECURE", "false").lower() == "true"
MINIO_PUBLIC_ENDPOINT = os.getenv("MINIO_PUBLIC_ENDPOINT", "http://localhost:9090")
MINIO_DEFAULT_BUCKETS = os.getenv("MINIO_DEFAULT_BUCKETS", "shelf-images,sku-training-images")

logger = logging.getLogger("shelfvision")


# -----------------------------
# Database
# -----------------------------
class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


class Tenant(Base, TimestampMixin):
    __tablename__ = "tenants"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(255), unique=True)
    status: Mapped[str] = mapped_column(String(32), default="active")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    logo_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    username: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    password: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    max_skus: Mapped[int] = mapped_column(Integer, default=50)
    max_images_per_month: Mapped[int] = mapped_column(Integer, default=1000)
    max_images_per_week: Mapped[int] = mapped_column(Integer, default=300)
    max_images_per_year: Mapped[int] = mapped_column(Integer, default=10000)
    processed_images_this_month: Mapped[int] = mapped_column(Integer, default=0)
    processed_images_this_week: Mapped[int] = mapped_column(Integer, default=0)
    processed_images_this_year: Mapped[int] = mapped_column(Integer, default=0)


class Store(Base, TimestampMixin):
    __tablename__ = "stores"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"), index=True)
    name: Mapped[str] = mapped_column(String(255))
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    country: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)


class ProductCategory(Base, TimestampMixin):
    __tablename__ = "product_categories"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"), index=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


class SKU(Base, TimestampMixin):
    __tablename__ = "skus"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"), index=True)
    category_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("product_categories.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    barcode: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    training_status: Mapped[str] = mapped_column(String(32), default="pending")


class SKUImage(Base):
    __tablename__ = "sku_images"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    sku_id: Mapped[str] = mapped_column(String(36), ForeignKey("skus.id"), index=True)
    image_url: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class PlanogramTemplate(Base, TimestampMixin):
    __tablename__ = "planogram_templates"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"), index=True)
    store_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("stores.id"), nullable=True)
    shelf_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="draft")
    layout: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON, nullable=True)
    created_by: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)


class PlanogramVersion(Base):
    __tablename__ = "planogram_versions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    template_id: Mapped[str] = mapped_column(String(36), ForeignKey("planogram_templates.id"), index=True)
    version_number: Mapped[int] = mapped_column(Integer)
    layout: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON, nullable=True)
    change_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_by: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class Shelf(Base, TimestampMixin):
    __tablename__ = "shelves"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"), index=True)
    store_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("stores.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    location_in_store: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    width_cm: Mapped[Optional[float]] = mapped_column(Float, nullable=True)


class ShelfProduct(Base):
    __tablename__ = "shelf_products"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    shelf_id: Mapped[str] = mapped_column(String(36), ForeignKey("shelves.id"), index=True)
    sku_id: Mapped[str] = mapped_column(String(36), ForeignKey("skus.id"), index=True)
    expected_facings: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    position_order: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class ShelfImage(Base):
    __tablename__ = "shelf_images"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    shelf_id: Mapped[str] = mapped_column(String(36), ForeignKey("shelves.id"), index=True)
    image_url: Mapped[str] = mapped_column(Text)
    detection_result: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON, nullable=True)
    processed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class Detection(Base):
    __tablename__ = "detections"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"), index=True)
    store_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("stores.id"), nullable=True)
    original_image_url: Mapped[str] = mapped_column(Text)
    annotated_image_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    detection_result: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON, nullable=True)
    share_of_shelf_percentage: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    total_facings: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    detected_skus: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    missing_skus: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    processed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class ComplianceScan(Base):
    __tablename__ = "compliance_scans"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    template_id: Mapped[str] = mapped_column(String(36), ForeignKey("planogram_templates.id"), index=True)
    shelf_image_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("shelf_images.id"), nullable=True)
    image_url: Mapped[str] = mapped_column(Text)
    compliance_score: Mapped[float] = mapped_column(Float)
    total_expected: Mapped[int] = mapped_column(Integer)
    total_found: Mapped[int] = mapped_column(Integer)
    total_missing: Mapped[int] = mapped_column(Integer)
    total_extra: Mapped[int] = mapped_column(Integer)
    details: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON, nullable=True)
    scanned_by: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class Profile(Base, TimestampMixin):
    __tablename__ = "profiles"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), unique=True, index=True)
    tenant_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("tenants.id"), nullable=True)
    full_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    username: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    avatar_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)


class UserRole(Base):
    __tablename__ = "user_roles"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True)
    role: Mapped[str] = mapped_column(String(32), default="tenant_user")


class UserStoreAccess(Base):
    __tablename__ = "user_store_access"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True)
    store_id: Mapped[str] = mapped_column(String(36), ForeignKey("stores.id"), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class UserShelfAccess(Base):
    __tablename__ = "user_shelf_access"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True)
    shelf_id: Mapped[str] = mapped_column(String(36), ForeignKey("shelves.id"), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True)
    tenant_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("tenants.id"), nullable=True)
    title: Mapped[str] = mapped_column(String(255))
    message: Mapped[str] = mapped_column(Text)
    type: Mapped[str] = mapped_column(String(64))
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    metadata_: Mapped[Optional[dict[str, Any]]] = mapped_column("metadata", JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


class UsageMetric(Base, TimestampMixin):
    __tablename__ = "usage_metrics"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"), index=True)
    period_type: Mapped[str] = mapped_column(String(16))
    period_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    images_processed: Mapped[int] = mapped_column(Integer, default=0)
    training_jobs: Mapped[int] = mapped_column(Integer, default=0)


class Model(Base, TimestampMixin):
    __tablename__ = "models"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"), index=True)
    version: Mapped[str] = mapped_column(String(64))
    status: Mapped[str] = mapped_column(String(64))
    accuracy: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    model_path: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    trained_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)


class ProcessingJob(Base, TimestampMixin):
    __tablename__ = "processing_jobs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id: Mapped[str] = mapped_column(String(36), ForeignKey("tenants.id"), index=True)
    store_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("stores.id"), nullable=True)
    model_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("models.id"), nullable=True)
    original_image_url: Mapped[str] = mapped_column(Text)
    annotated_image_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="pending")
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


class DetectionResult(Base):
    __tablename__ = "detection_results"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    job_id: Mapped[str] = mapped_column(String(36), ForeignKey("processing_jobs.id"), index=True)
    sku_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("skus.id"), nullable=True)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    facings_count: Mapped[int] = mapped_column(Integer, default=0)
    confidence: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    share_of_shelf: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    bounding_boxes: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


# -----------------------------
# Security / Auth
# -----------------------------
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_minio_client() -> Minio:
    return Minio(
        MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=MINIO_SECURE,
    )


def ensure_minio_bucket(client: Minio, bucket: str) -> None:
    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)


def upload_to_minio(client: Minio, bucket: str, object_key: str, data: bytes, content_type: Optional[str]) -> None:
    ensure_minio_bucket(client, bucket)
    client.put_object(
        bucket_name=bucket,
        object_name=object_key,
        data=io.BytesIO(data),
        length=len(data),
        content_type=content_type or "application/octet-stream",
    )


def to_dict(row: Any) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for attr in row.__mapper__.column_attrs:
        attr_key = attr.key
        col_name = attr.columns[0].name
        val = getattr(row, attr_key)
        if isinstance(val, datetime):
            out[col_name] = val.isoformat()
        else:
            out[col_name] = val
    return out


def parse_eq(value: str) -> str:
    if value.startswith("eq."):
        return value[3:]
    return value


def cast_filter_value(raw: str) -> Any:
    value = parse_eq(raw)
    lower = value.lower()
    if lower == "true":
        return True
    if lower == "false":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


def apply_query_filters(query, model, params: dict[str, str]):
    ignored = {"select", "order", "limit", "offset"}
    for key, raw in params.items():
        if key in ignored:
            continue
        if hasattr(model, key):
            query = query.filter(getattr(model, key) == cast_filter_value(raw))
    if "order" in params:
        ord_value = params["order"]
        if "." in ord_value:
            field, direction = ord_value.split(".", 1)
            if hasattr(model, field):
                col = getattr(model, field)
                query = query.order_by(col.desc() if direction == "desc" else col.asc())
    return query


def require_security(
    authorization: Optional[str] = Header(default=None),
    apikey: Optional[str] = Header(default=None),
) -> Optional[str]:
    if apikey and apikey == API_KEY:
        return "apikey"

    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ", 1)[1]
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return str(payload.get("sub"))
        except JWTError as exc:
            raise HTTPException(status_code=401, detail="Invalid token") from exc

    raise HTTPException(status_code=401, detail="Missing or invalid auth")


def require_user(
    authorization: Optional[str] = Header(default=None),
) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")
    token = authorization.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        subject = payload.get("sub")
        if not subject:
            raise HTTPException(status_code=401, detail="Invalid token subject")
        return str(subject)
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc


# -----------------------------
# API models
# -----------------------------
class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    data: Optional[dict[str, Any]] = None


class TokenRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    identifier: str
    password: str


class DetectSKUsRequest(BaseModel):
    imageBase64: str
    tenantId: str
    storeId: Optional[str] = None
    skusToDetect: Optional[list[dict[str, Any]]] = None


class RoboflowDetectRequest(BaseModel):
    imageUrl: str
    shelfId: Optional[str] = None
    tenantId: Optional[str] = None


app = FastAPI(title="ShelfVision API", version="2.0.0")

cors_origins_raw = CORS_ALLOW_ORIGINS.strip()
if cors_origins_raw == "*":
    allow_origins = ["*"]
    allow_credentials = False
else:
    allow_origins = [o.strip() for o in cors_origins_raw.split(",") if o.strip()]
    allow_credentials = True

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup() -> None:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    (UPLOAD_DIR / "shelf-images").mkdir(parents=True, exist_ok=True)
    (UPLOAD_DIR / "sku-training-images").mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(bind=engine)
    try:
        client = get_minio_client()
        for bucket in [b.strip() for b in MINIO_DEFAULT_BUCKETS.split(",") if b.strip()]:
            ensure_minio_bucket(client, bucket)
    except S3Error as exc:
        logger.warning("MinIO startup bucket initialization failed: %s", exc)
    except Exception as exc:  # noqa: BLE001
        logger.warning("MinIO unavailable at startup: %s", exc)


# -----------------------------
# Generic REST CRUD
# -----------------------------
CRUD_RESOURCES: dict[str, Any] = {
    "tenants": Tenant,
    "stores": Store,
    "skus": SKU,
    "sku_images": SKUImage,
    "product_categories": ProductCategory,
    "planogram_templates": PlanogramTemplate,
    "planogram_versions": PlanogramVersion,
    "shelves": Shelf,
    "shelf_products": ShelfProduct,
    "shelf_images": ShelfImage,
    "detections": Detection,
    "compliance_scans": ComplianceScan,
    "profiles": Profile,
    "user_roles": UserRole,
    "user_store_access": UserStoreAccess,
    "user_shelf_access": UserShelfAccess,
    "notifications": Notification,
    "usage_metrics": UsageMetric,
    "models": Model,
    "processing_jobs": ProcessingJob,
    "detection_results": DetectionResult,
}

READ_ONLY = {"detections", "usage_metrics", "models", "processing_jobs", "detection_results"}
NO_PATCH = {"sku_images", "planogram_versions", "shelf_products", "user_roles", "user_store_access", "user_shelf_access", "usage_metrics", "models", "processing_jobs", "detection_results", "detections", "compliance_scans"}
NO_DELETE = {"compliance_scans", "planogram_versions", "usage_metrics", "models", "processing_jobs", "detection_results", "detections", "profiles"}
PATCH_KEY = {
    "profiles": "user_id",
}


def _delete_planogram_templates(db: Session, template_ids: list[str]) -> None:
    if not template_ids:
        return
    db.query(ComplianceScan).filter(ComplianceScan.template_id.in_(template_ids)).delete(synchronize_session=False)
    db.query(PlanogramVersion).filter(PlanogramVersion.template_id.in_(template_ids)).delete(synchronize_session=False)
    db.query(PlanogramTemplate).filter(PlanogramTemplate.id.in_(template_ids)).delete(synchronize_session=False)


def _delete_shelves(db: Session, shelf_ids: list[str]) -> None:
    if not shelf_ids:
        return
    db.query(UserShelfAccess).filter(UserShelfAccess.shelf_id.in_(shelf_ids)).delete(synchronize_session=False)
    db.query(ShelfProduct).filter(ShelfProduct.shelf_id.in_(shelf_ids)).delete(synchronize_session=False)

    shelf_image_ids = [sid for (sid,) in db.query(ShelfImage.id).filter(ShelfImage.shelf_id.in_(shelf_ids)).all()]
    if shelf_image_ids:
        db.query(ComplianceScan).filter(ComplianceScan.shelf_image_id.in_(shelf_image_ids)).delete(
            synchronize_session=False
        )
    db.query(ShelfImage).filter(ShelfImage.shelf_id.in_(shelf_ids)).delete(synchronize_session=False)

    template_ids = [tid for (tid,) in db.query(PlanogramTemplate.id).filter(PlanogramTemplate.shelf_id.in_(shelf_ids)).all()]
    _delete_planogram_templates(db, template_ids)
    db.query(Shelf).filter(Shelf.id.in_(shelf_ids)).delete(synchronize_session=False)


def _delete_stores(db: Session, store_ids: list[str]) -> None:
    if not store_ids:
        return
    db.query(UserStoreAccess).filter(UserStoreAccess.store_id.in_(store_ids)).delete(synchronize_session=False)
    db.query(Detection).filter(Detection.store_id.in_(store_ids)).delete(synchronize_session=False)

    job_ids = [jid for (jid,) in db.query(ProcessingJob.id).filter(ProcessingJob.store_id.in_(store_ids)).all()]
    if job_ids:
        db.query(DetectionResult).filter(DetectionResult.job_id.in_(job_ids)).delete(synchronize_session=False)
    db.query(ProcessingJob).filter(ProcessingJob.store_id.in_(store_ids)).delete(synchronize_session=False)

    shelf_ids = [sid for (sid,) in db.query(Shelf.id).filter(Shelf.store_id.in_(store_ids)).all()]
    _delete_shelves(db, shelf_ids)

    template_ids = [tid for (tid,) in db.query(PlanogramTemplate.id).filter(PlanogramTemplate.store_id.in_(store_ids)).all()]
    _delete_planogram_templates(db, template_ids)

    db.query(Store).filter(Store.id.in_(store_ids)).delete(synchronize_session=False)


def _delete_tenant(db: Session, tenant_id: str) -> None:
    store_ids = [sid for (sid,) in db.query(Store.id).filter(Store.tenant_id == tenant_id).all()]
    _delete_stores(db, store_ids)

    orphan_shelf_ids = [sid for (sid,) in db.query(Shelf.id).filter(Shelf.tenant_id == tenant_id).all()]
    _delete_shelves(db, orphan_shelf_ids)

    template_ids = [tid for (tid,) in db.query(PlanogramTemplate.id).filter(PlanogramTemplate.tenant_id == tenant_id).all()]
    _delete_planogram_templates(db, template_ids)

    db.query(Detection).filter(Detection.tenant_id == tenant_id).delete(synchronize_session=False)
    db.query(Notification).filter(Notification.tenant_id == tenant_id).delete(synchronize_session=False)
    db.query(UsageMetric).filter(UsageMetric.tenant_id == tenant_id).delete(synchronize_session=False)

    model_ids = [mid for (mid,) in db.query(Model.id).filter(Model.tenant_id == tenant_id).all()]
    if model_ids:
        db.query(ProcessingJob).filter(ProcessingJob.model_id.in_(model_ids)).update(
            {ProcessingJob.model_id: None}, synchronize_session=False
        )
    db.query(Model).filter(Model.tenant_id == tenant_id).delete(synchronize_session=False)

    job_ids = [jid for (jid,) in db.query(ProcessingJob.id).filter(ProcessingJob.tenant_id == tenant_id).all()]
    if job_ids:
        db.query(DetectionResult).filter(DetectionResult.job_id.in_(job_ids)).delete(synchronize_session=False)
    db.query(ProcessingJob).filter(ProcessingJob.tenant_id == tenant_id).delete(synchronize_session=False)

    sku_ids = [sid for (sid,) in db.query(SKU.id).filter(SKU.tenant_id == tenant_id).all()]
    if sku_ids:
        db.query(SKUImage).filter(SKUImage.sku_id.in_(sku_ids)).delete(synchronize_session=False)
        db.query(ShelfProduct).filter(ShelfProduct.sku_id.in_(sku_ids)).delete(synchronize_session=False)
        db.query(DetectionResult).filter(DetectionResult.sku_id.in_(sku_ids)).delete(synchronize_session=False)
    db.query(SKU).filter(SKU.tenant_id == tenant_id).delete(synchronize_session=False)

    db.query(ProductCategory).filter(ProductCategory.tenant_id == tenant_id).delete(synchronize_session=False)
    db.query(Profile).filter(Profile.tenant_id == tenant_id).update({Profile.tenant_id: None}, synchronize_session=False)

    db.query(Tenant).filter(Tenant.id == tenant_id).delete(synchronize_session=False)


@app.get("/rest/v1/{resource}")
def list_resource(
    resource: str,
    request: Request,
    _: str = Depends(require_security),
    db: Session = Depends(get_db),
):
    model = CRUD_RESOURCES.get(resource)
    if not model:
        raise HTTPException(status_code=404, detail="Unknown resource")

    query = db.query(model)
    query = apply_query_filters(query, model, dict(request.query_params))
    rows = query.all()
    return [to_dict(row) for row in rows]


@app.post("/rest/v1/{resource}", status_code=201)
def create_resource(
    resource: str,
    payload: dict[str, Any],
    _: str = Depends(require_security),
    db: Session = Depends(get_db),
):
    model = CRUD_RESOURCES.get(resource)
    if not model:
        raise HTTPException(status_code=404, detail="Unknown resource")
    if resource in READ_ONLY:
        raise HTTPException(status_code=405, detail="Read-only resource")

    row = model(**payload)
    db.add(row)
    db.commit()
    db.refresh(row)
    return to_dict(row)


@app.patch("/rest/v1/{resource}")
def update_resource(
    resource: str,
    payload: dict[str, Any],
    id: Optional[str] = Query(default=None),
    user_id: Optional[str] = Query(default=None),
    _: str = Depends(require_security),
    db: Session = Depends(get_db),
):
    model = CRUD_RESOURCES.get(resource)
    if not model:
        raise HTTPException(status_code=404, detail="Unknown resource")
    if resource in NO_PATCH:
        raise HTTPException(status_code=405, detail="Patch not supported")

    key = PATCH_KEY.get(resource, "id")
    lookup_val = user_id if key == "user_id" else id
    if not lookup_val:
        raise HTTPException(status_code=400, detail=f"Missing query parameter: {key}")

    lookup = parse_eq(lookup_val)
    row = db.query(model).filter(getattr(model, key) == lookup).first()
    if not row:
        raise HTTPException(status_code=404, detail="Not found")

    for k, v in payload.items():
        if hasattr(row, k):
            setattr(row, k, v)

    db.commit()
    db.refresh(row)
    return to_dict(row)


@app.delete("/rest/v1/{resource}", status_code=204)
def delete_resource(
    resource: str,
    id: str = Query(...),
    _: str = Depends(require_security),
    db: Session = Depends(get_db),
):
    model = CRUD_RESOURCES.get(resource)
    if not model:
        raise HTTPException(status_code=404, detail="Unknown resource")
    if resource in NO_DELETE:
        raise HTTPException(status_code=405, detail="Delete not supported")

    target_id = parse_eq(id)
    row = db.query(model).filter(model.id == target_id).first()
    if not row:
        return None

    if resource == "shelves":
        _delete_shelves(db, [target_id])
    elif resource == "stores":
        _delete_stores(db, [target_id])
    elif resource == "tenants":
        _delete_tenant(db, target_id)
    else:
        db.delete(row)

    db.commit()
    return None


# -----------------------------
# RPC
# -----------------------------
@app.post("/rest/v1/rpc/check_tenant_quota")
def check_tenant_quota(payload: dict[str, Any], _: str = Depends(require_security), db: Session = Depends(get_db)):
    tenant_id = payload.get("_tenant_id")
    if not tenant_id:
        raise HTTPException(status_code=400, detail="_tenant_id is required")

    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")

    monthly = tenant.processed_images_this_month or 0
    weekly = tenant.processed_images_this_week or 0
    yearly = tenant.processed_images_this_year or 0

    can_process = (
        monthly < (tenant.max_images_per_month or 0)
        and weekly < (tenant.max_images_per_week or 0)
        and yearly < (tenant.max_images_per_year or 0)
    )

    return {
        "tenantId": tenant.id,
        "canProcess": can_process,
        "monthlyUsage": monthly,
        "monthlyLimit": tenant.max_images_per_month,
        "weeklyUsage": weekly,
        "weeklyLimit": tenant.max_images_per_week,
        "yearlyUsage": yearly,
        "yearlyLimit": tenant.max_images_per_year,
    }


@app.post("/rest/v1/rpc/increment_usage_metric")
def increment_usage_metric(payload: dict[str, Any], _: str = Depends(require_security), db: Session = Depends(get_db)):
    tenant_id = payload.get("_tenant_id")
    period_type = payload.get("_period_type")
    images_count = int(payload.get("_images_count", 1))

    if not tenant_id or not period_type:
        raise HTTPException(status_code=400, detail="_tenant_id and _period_type are required")

    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")

    if period_type == "monthly":
        tenant.processed_images_this_month = (tenant.processed_images_this_month or 0) + images_count
    elif period_type == "weekly":
        tenant.processed_images_this_week = (tenant.processed_images_this_week or 0) + images_count
    elif period_type == "yearly":
        tenant.processed_images_this_year = (tenant.processed_images_this_year or 0) + images_count

    period_start = datetime.now(timezone.utc)
    metric = (
        db.query(UsageMetric)
        .filter(
            UsageMetric.tenant_id == tenant_id,
            UsageMetric.period_type == period_type,
        )
        .order_by(UsageMetric.created_at.desc())
        .first()
    )
    if metric is None:
        metric = UsageMetric(
            tenant_id=tenant_id,
            period_type=period_type,
            period_start=period_start,
            images_processed=images_count,
        )
        db.add(metric)
    else:
        metric.images_processed = (metric.images_processed or 0) + images_count

    db.commit()
    return {"success": True}


@app.post("/rest/v1/rpc/get_user_tenant_id")
def get_user_tenant_id(payload: dict[str, Any], _: str = Depends(require_security), db: Session = Depends(get_db)):
    user_id = payload.get("_user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="_user_id is required")

    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    return {"tenant_id": profile.tenant_id if profile else None}


@app.post("/rest/v1/rpc/has_role")
def has_role(payload: dict[str, Any], _: str = Depends(require_security), db: Session = Depends(get_db)):
    user_id = payload.get("_user_id")
    role = payload.get("_role")
    if not user_id or not role:
        raise HTTPException(status_code=400, detail="_user_id and _role are required")

    exists = db.query(UserRole).filter(UserRole.user_id == user_id, UserRole.role == role).first() is not None
    return {"has_role": exists}


# -----------------------------
# Edge-like functions
# -----------------------------
@app.post("/functions/v1/detect-skus")
def detect_skus(payload: DetectSKUsRequest, _: str = Depends(require_security), db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.id == payload.tenantId).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")

    if (tenant.processed_images_this_month or 0) >= (tenant.max_images_per_month or 0):
        raise HTTPException(status_code=429, detail="Quota exceeded")

    try:
        if "," in payload.imageBase64:
            raw = payload.imageBase64.split(",", 1)[1]
        else:
            raw = payload.imageBase64
        image_bytes = base64.b64decode(raw)
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Invalid imageBase64") from exc

    image_id = str(uuid.uuid4())
    image_path = UPLOAD_DIR / "shelf-images" / f"{image_id}.jpg"
    image_path.write_bytes(image_bytes)

    skus = payload.skusToDetect or []
    detections = []
    for sku in skus:
        detections.append(
            {
                "skuId": sku.get("id"),
                "skuName": sku.get("name", "Unknown"),
                "isAvailable": True,
                "facings": 1,
                "confidence": 0.9,
                "boundingBox": {"x": 0.1, "y": 0.1, "width": 0.2, "height": 0.2},
            }
        )

    missing = []
    detection_record = Detection(
        tenant_id=payload.tenantId,
        store_id=payload.storeId,
        original_image_url=f"/storage/v1/object/shelf-images/{image_id}.jpg",
        annotated_image_url=None,
        detection_result={"detections": detections, "missingSkus": missing},
        share_of_shelf_percentage=50.0,
        total_facings=sum(d["facings"] for d in detections),
        detected_skus=len(detections),
        missing_skus=len(missing),
    )
    db.add(detection_record)

    tenant.processed_images_this_month = (tenant.processed_images_this_month or 0) + 1
    tenant.processed_images_this_week = (tenant.processed_images_this_week or 0) + 1
    tenant.processed_images_this_year = (tenant.processed_images_this_year or 0) + 1

    for period in ("daily", "weekly", "monthly", "yearly"):
        metric = UsageMetric(
            tenant_id=tenant.id,
            period_type=period,
            period_start=datetime.now(timezone.utc),
            images_processed=1,
        )
        db.add(metric)

    db.commit()
    db.refresh(detection_record)

    return {
        "success": True,
        "detectionId": detection_record.id,
        "result": {
            "detections": detections,
            "missingSkus": missing,
            "shareOfShelf": {
                "totalShelfArea": 1.0,
                "trainedProductsArea": 0.5,
                "percentage": 50.0,
            },
            "totalFacings": sum(d["facings"] for d in detections),
            "summary": "Detection completed",
        },
    }


@app.post("/functions/v1/roboflow-detect")
def roboflow_detect(payload: RoboflowDetectRequest, _: str = Depends(require_security), db: Session = Depends(get_db)):
    result = {
        "workflow": "roboflow",
        "imageUrl": payload.imageUrl,
        "predictions": [],
        "status": "ok",
    }

    if payload.shelfId:
        row = ShelfImage(
            shelf_id=payload.shelfId,
            image_url=payload.imageUrl,
            detection_result=result,
            processed_at=datetime.now(timezone.utc),
        )
        db.add(row)

    if payload.tenantId:
        tenant = db.query(Tenant).filter(Tenant.id == payload.tenantId).first()
        if tenant:
            tenant.processed_images_this_month = (tenant.processed_images_this_month or 0) + 1
            tenant.processed_images_this_week = (tenant.processed_images_this_week or 0) + 1
            tenant.processed_images_this_year = (tenant.processed_images_this_year or 0) + 1

    db.commit()
    return {"success": True, "result": result}


# -----------------------------
# Authentication
# -----------------------------
@app.post("/auth/v1/signup")
def signup(payload: SignupRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")

    user = User(email=payload.email, password_hash=hash_password(payload.password))
    db.add(user)
    db.flush()

    profile = Profile(
        user_id=user.id,
        full_name=(payload.data or {}).get("full_name"),
    )
    db.add(profile)
    db.commit()
    db.refresh(user)

    token = create_access_token(user.id)
    return {
        "user": {"id": user.id, "email": user.email},
        "session": {
            "access_token": token,
            "token_type": "bearer",
            "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        },
    }


@app.post("/auth/v1/token")
def token(
    payload: TokenRequest,
    grant_type: str = Query(...),
    db: Session = Depends(get_db),
):
    if grant_type != "password":
        raise HTTPException(status_code=400, detail="Unsupported grant_type")

    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    profile = db.query(Profile).filter(Profile.user_id == user.id).first()
    if profile:
        profile.last_login = datetime.now(timezone.utc)
        db.commit()

    access_token = create_access_token(user.id)
    return {
        "access_token": access_token,
        "refresh_token": str(uuid.uuid4()),
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        "token_type": "bearer",
        "user": {"id": user.id, "email": user.email},
    }


def _get_user_assignments(db: Session, user_id: str) -> dict[str, Any]:
    store_ids = {sid for (sid,) in db.query(UserStoreAccess.store_id).filter(UserStoreAccess.user_id == user_id).all()}
    shelf_ids = {sid for (sid,) in db.query(UserShelfAccess.shelf_id).filter(UserShelfAccess.user_id == user_id).all()}

    if shelf_ids:
        shelf_store_ids = {
            sid for (sid,) in db.query(Shelf.store_id).filter(Shelf.id.in_(list(shelf_ids))).all() if sid is not None
        }
        store_ids.update(shelf_store_ids)

    stores: list[dict[str, Any]] = []
    if store_ids:
        stores = [to_dict(row) for row in db.query(Store).filter(Store.id.in_(list(store_ids))).all()]

    planogram_query = db.query(PlanogramTemplate)
    if store_ids or shelf_ids:
        if store_ids and shelf_ids:
            planogram_query = planogram_query.filter(
                (PlanogramTemplate.store_id.in_(list(store_ids))) | (PlanogramTemplate.shelf_id.in_(list(shelf_ids)))
            )
        elif store_ids:
            planogram_query = planogram_query.filter(PlanogramTemplate.store_id.in_(list(store_ids)))
        else:
            planogram_query = planogram_query.filter(PlanogramTemplate.shelf_id.in_(list(shelf_ids)))
        planograms = [to_dict(row) for row in planogram_query.all()]
    else:
        planograms = []

    return {"stores": stores, "planograms": planograms}


@app.post("/auth/v1/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    identifier = payload.identifier.strip()
    if not identifier:
        raise HTTPException(status_code=400, detail="identifier is required")

    user = db.query(User).filter(User.email == identifier).first()
    if not user:
        profile = db.query(Profile).filter(Profile.username == identifier).first()
        if profile:
            user = db.query(User).filter(User.id == profile.user_id).first()

    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    profile = db.query(Profile).filter(Profile.user_id == user.id).first()
    if profile:
        profile.last_login = datetime.now(timezone.utc)
        db.commit()

    assignments = _get_user_assignments(db, user.id)
    access_token = create_access_token(user.id)
    return {
        "access_token": access_token,
        "refresh_token": str(uuid.uuid4()),
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "username": profile.username if profile else None,
        },
        "stores": assignments["stores"],
        "planograms": assignments["planograms"],
    }


@app.post("/auth/v1/logout", status_code=204)
def logout(_: str = Depends(require_user)):
    return None


# -----------------------------
# Storage
# -----------------------------
def _sanitize_object_path(object_path: str) -> str:
    cleaned = object_path.strip().lstrip("/")
    if not cleaned or ".." in cleaned:
        raise HTTPException(status_code=400, detail="Invalid path")
    return cleaned


@app.post("/storage/v1/object/shelf-images/{path:path}")
async def upload_shelf_image(
    path: str,
    file: UploadFile | None = File(default=None),
    files: list[UploadFile] | None = File(default=None),
    tenant_id: str | None = Form(default=None),
    category_id: str | None = Form(default=None),
    _: str = Depends(require_security),
):
    base_path = _sanitize_object_path(path).rstrip("/")
    client = get_minio_client()

    if files:
        if not tenant_id or not category_id:
            raise HTTPException(status_code=400, detail="tenant_id and category_id are required for multi-file upload")
        uploaded: list[dict[str, Any]] = []
        for item in files:
            data = await item.read()
            object_key = f"{base_path}/{tenant_id}/{category_id}/{uuid.uuid4()}-{item.filename}"
            try:
                upload_to_minio(client, "shelf-images", object_key, data, item.content_type)
            except S3Error as exc:
                raise HTTPException(status_code=500, detail=f"MinIO upload failed: {exc}") from exc
            uploaded.append(
                {
                    "filename": item.filename,
                    "object_key": object_key,
                    "url": f"{MINIO_PUBLIC_ENDPOINT}/shelf-images/{object_key}",
                }
            )
        return {"bucket": "shelf-images", "tenant_id": tenant_id, "category_id": category_id, "count": len(uploaded), "items": uploaded}

    if file is None:
        raise HTTPException(status_code=400, detail="file or files is required")

    object_key = base_path
    data = await file.read()
    try:
        upload_to_minio(client, "shelf-images", object_key, data, file.content_type)
    except S3Error as exc:
        raise HTTPException(status_code=500, detail=f"MinIO upload failed: {exc}") from exc
    return {"Key": f"shelf-images/{object_key}", "url": f"{MINIO_PUBLIC_ENDPOINT}/shelf-images/{object_key}"}


@app.get("/storage/v1/object/shelf-images/{path:path}")
def download_shelf_image(path: str, _: str = Depends(require_security)):
    object_key = _sanitize_object_path(path)
    client = get_minio_client()
    try:
        response = client.get_object("shelf-images", object_key)
        data = response.read()
        content_type = response.headers.get("Content-Type", "application/octet-stream")
    except S3Error:
        raise HTTPException(status_code=404, detail="Not found")
    return Response(content=data, media_type=content_type)


@app.post("/storage/v1/object/sku-training-images/{path:path}")
async def upload_sku_training_image(
    path: str,
    file: UploadFile | None = File(default=None),
    files: list[UploadFile] | None = File(default=None),
    tenant_id: str | None = Form(default=None),
    category_id: str | None = Form(default=None),
    _: str = Depends(require_security),
):
    base_path = _sanitize_object_path(path).rstrip("/")
    client = get_minio_client()

    if files:
        if not tenant_id or not category_id:
            raise HTTPException(status_code=400, detail="tenant_id and category_id are required for multi-file upload")
        uploaded: list[dict[str, Any]] = []
        for item in files:
            data = await item.read()
            object_key = f"{base_path}/{tenant_id}/{category_id}/{uuid.uuid4()}-{item.filename}"
            try:
                upload_to_minio(client, "sku-training-images", object_key, data, item.content_type)
            except S3Error as exc:
                raise HTTPException(status_code=500, detail=f"MinIO upload failed: {exc}") from exc
            uploaded.append(
                {
                    "filename": item.filename,
                    "object_key": object_key,
                    "url": f"{MINIO_PUBLIC_ENDPOINT}/sku-training-images/{object_key}",
                }
            )
        return {
            "bucket": "sku-training-images",
            "tenant_id": tenant_id,
            "category_id": category_id,
            "count": len(uploaded),
            "items": uploaded,
        }

    if file is None:
        raise HTTPException(status_code=400, detail="file or files is required")

    object_key = base_path
    data = await file.read()
    try:
        upload_to_minio(client, "sku-training-images", object_key, data, file.content_type)
    except S3Error as exc:
        raise HTTPException(status_code=500, detail=f"MinIO upload failed: {exc}") from exc
    return {"Key": f"sku-training-images/{object_key}", "url": f"{MINIO_PUBLIC_ENDPOINT}/sku-training-images/{object_key}"}


@app.get("/storage/v1/object/sku-training-images/{path:path}")
def download_sku_training_image(path: str, _: str = Depends(require_security)):
    object_key = _sanitize_object_path(path)
    client = get_minio_client()
    try:
        response = client.get_object("sku-training-images", object_key)
        data = response.read()
        content_type = response.headers.get("Content-Type", "application/octet-stream")
    except S3Error:
        raise HTTPException(status_code=404, detail="Not found")
    return Response(content=data, media_type=content_type)


@app.post("/storage/v1/object/{bucket}/{path:path}")
async def upload_multiple_sku_images(
    bucket: str,
    path: str,
    tenant_id: str = Form(...),
    category_id: str = Form(...),
    files: list[UploadFile] = File(...),
    _: str = Depends(require_security),
):
    if not files:
        raise HTTPException(status_code=400, detail="At least one file is required")

    base_path = _sanitize_object_path(path).rstrip("/")
    client = get_minio_client()
    uploaded: list[dict[str, Any]] = []

    for file in files:
        data = await file.read()
        if not data:
            continue
        object_name = f"{base_path}/{tenant_id}/{category_id}/{uuid.uuid4()}-{file.filename}"
        try:
            upload_to_minio(client, bucket, object_name, data, file.content_type)
        except S3Error as exc:
            raise HTTPException(status_code=500, detail=f"MinIO upload failed for {file.filename}: {exc}") from exc

        uploaded.append(
            {
                "filename": file.filename,
                "content_type": file.content_type or "application/octet-stream",
                "size_bytes": len(data),
                "object_key": object_name,
                "url": f"{MINIO_PUBLIC_ENDPOINT}/{bucket}/{object_name}",
            }
        )

    return {
        "bucket": bucket,
        "tenant_id": tenant_id,
        "category_id": category_id,
        "count": len(uploaded),
        "items": uploaded,
    }


@app.get("/storage/v1/object/{bucket}/{path:path}")
def download_storage_object(bucket: str, path: str, _: str = Depends(require_security)):
    object_key = _sanitize_object_path(path)
    client = get_minio_client()
    try:
        response = client.get_object(bucket, object_key)
        data = response.read()
        content_type = response.headers.get("Content-Type", "application/octet-stream")
    except S3Error:
        raise HTTPException(status_code=404, detail="Not found")
    return Response(content=data, media_type=content_type)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
