# ShelfVision API Endpoints: Request/Response Examples

## Base URLs
- Local: `http://localhost:8010`
- Public (Cloudflare quick tunnel): `https://establishment-single-monitors-wave.trycloudflare.com`

## Required Headers
Most endpoints require one of:
- `apikey: super-api-key-change-me`
- `Authorization: Bearer <access_token>`

For JSON bodies:
- `Content-Type: application/json`

---

## 1) Health
### GET `/health`
Request:
```bash
curl -X GET "http://localhost:8010/health"
```
Response `200`:
```json
{
  "status": "ok"
}
```

---

## 2) Authentication

### POST `/auth/v1/signup`
Request:
```bash
curl -X POST "http://localhost:8010/auth/v1/signup" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "a.salameh@cortanexai.com",
    "password": "123456",
    "data": {"full_name": "Ahmad Salameh"}
  }'
```
Response `200`:
```json
{
  "user": {
    "id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
    "email": "a.salameh@cortanexai.com"
  },
  "session": {
    "access_token": "<jwt>",
    "token_type": "bearer",
    "expires_in": 86400
  }
}
```

### POST `/auth/v1/token?grant_type=password`
Request:
```bash
curl -X POST "http://localhost:8010/auth/v1/token?grant_type=password" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "a.salameh@cortanexai.com",
    "password": "123456"
  }'
```
Response `200`:
```json
{
  "access_token": "<jwt>",
  "refresh_token": "<uuid>",
  "expires_in": 86400,
  "token_type": "bearer",
  "user": {
    "id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
    "email": "a.salameh@cortanexai.com"
  }
}
```

### POST `/auth/v1/login`
Login using username **or** email + password.

Request:
```bash
curl -X POST "http://localhost:8010/auth/v1/login" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{
    "identifier": "a.salameh@cortanexai.com",
    "password": "123456"
  }'
```
Response `200`:
```json
{
  "access_token": "<jwt>",
  "refresh_token": "<uuid>",
  "expires_in": 86400,
  "token_type": "bearer",
  "user": {
    "id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
    "email": "a.salameh@cortanexai.com",
    "username": "a.salameh"
  },
  "stores": [
    {
      "id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "name": "Cortanex Hypermarket - Amman West",
      "address": "Wasfi Al Tal Street, Building 221",
      "city": "Amman",
      "country": "Jordan",
      "created_at": "2026-02-18T10:26:26.0+00:00",
      "updated_at": "2026-02-18T10:26:26.0+00:00"
    }
  ],
  "planograms": [
    {
      "id": "0f6378b6-3002-4e8d-82ca-406dc91fea65",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
      "shelf_id": "b48392cc-c85c-4d5f-beef-c6813567ee8d",
      "name": "Amman Weekly Planogram 01",
      "description": "Planogram for shelf 1",
      "status": "active",
      "layout": [{"slot": 1, "category": "Beverages"}],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.0+00:00",
      "updated_at": "2026-02-18T10:26:26.0+00:00"
    }
  ]
}
```

### POST `/auth/v1/logout`
Request:
```bash
curl -X POST "http://localhost:8010/auth/v1/logout" \
  -H "Authorization: Bearer <jwt>"
```
Response `204` (no body)

---

## 3) Generic REST Resources

These endpoints are generic and work for all resources under `/rest/v1/{resource}`.

### Supported resources
- `tenants`
- `stores`
- `skus`
- `sku_images`
- `product_categories`
- `planogram_templates`
- `planogram_versions`
- `shelves`
- `shelf_products`
- `shelf_images`
- `detections`
- `compliance_scans`
- `profiles`
- `user_roles`
- `user_store_access`
- `user_shelf_access`
- `notifications`
- `usage_metrics`
- `models`
- `processing_jobs`
- `detection_results`

### GET `/rest/v1/{resource}`
Request:
```bash
curl -X GET "http://localhost:8010/rest/v1/stores?tenant_id=eq.d94b7aa1-fd11-4915-85f6-1bf6cc5f6254&select=*" \
  -H "apikey: super-api-key-change-me"
```
Response `200`:
```json
[
  {
    "id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
    "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
    "name": "Cortanex Hypermarket - Amman West",
    "address": "Wasfi Al Tal Street, Building 221",
    "city": "Amman",
    "country": "Jordan",
    "created_at": "2026-02-18T10:26:26.0+00:00",
    "updated_at": "2026-02-18T10:26:26.0+00:00"
  }
]
```

### POST `/rest/v1/{resource}`
Request:
```bash
curl -X POST "http://localhost:8010/rest/v1/tenants" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Cortanex Retail Group 1771410386",
    "status": "active",
    "is_active": true,
    "max_skus": 1000
  }'
```
Response `201`:
```json
{
  "id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Retail Group 1771410386",
  "status": "active",
  "is_active": true,
  "logo_url": null,
  "username": null,
  "password": null,
  "max_skus": 1000,
  "max_images_per_month": 1000,
  "max_images_per_week": 300,
  "max_images_per_year": 10000,
  "processed_images_this_month": 0,
  "processed_images_this_week": 0,
  "processed_images_this_year": 0,
  "created_at": "2026-02-18T10:26:26.0+00:00",
  "updated_at": "2026-02-18T10:26:26.0+00:00"
}
```

### PATCH `/rest/v1/{resource}`
Request:
```bash
curl -X PATCH "http://localhost:8010/rest/v1/profiles?user_id=eq.e26f368d-c9a3-4acc-a9ff-0a402ab77364" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "a.salameh",
    "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254"
  }'
```
Response `200`:
```json
{
  "id": "<profile-id>",
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "full_name": "Ahmad Salameh",
  "username": "a.salameh",
  "avatar_url": "https://cdn.cortanex.ai/avatars/a.salameh.png",
  "last_login": null,
  "created_at": "2026-02-18T10:26:26.0+00:00",
  "updated_at": "2026-02-18T10:26:26.0+00:00"
}
```

### DELETE `/rest/v1/{resource}`
Request:
```bash
curl -X DELETE "http://localhost:8010/rest/v1/sku_images?id=eq.<sku-image-id>" \
  -H "apikey: super-api-key-change-me"
```
Response `204` (no body)

---

## 4) RPC Endpoints

### POST `/rest/v1/rpc/check_tenant_quota`
Request:
```bash
curl -X POST "http://localhost:8010/rest/v1/rpc/check_tenant_quota" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{"_tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254"}'
```
Response `200`:
```json
{
  "tenantId": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "canProcess": true,
  "monthlyUsage": 0,
  "monthlyLimit": 150000,
  "weeklyUsage": 0,
  "weeklyLimit": 35000,
  "yearlyUsage": 0,
  "yearlyLimit": 1800000
}
```

### POST `/rest/v1/rpc/increment_usage_metric`
Request:
```bash
curl -X POST "http://localhost:8010/rest/v1/rpc/increment_usage_metric" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{
    "_tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
    "_period_type": "monthly",
    "_images_count": 2
  }'
```
Response `200`:
```json
{
  "success": true
}
```

### POST `/rest/v1/rpc/get_user_tenant_id`
Request:
```bash
curl -X POST "http://localhost:8010/rest/v1/rpc/get_user_tenant_id" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{"_user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"}'
```
Response `200`:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254"
}
```

### POST `/rest/v1/rpc/has_role`
Request:
```bash
curl -X POST "http://localhost:8010/rest/v1/rpc/has_role" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{
    "_user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
    "_role": "tenant_admin"
  }'
```
Response `200`:
```json
{
  "has_role": false
}
```

---

## 5) AI/Function Endpoints

### POST `/functions/v1/detect-skus`
Request:
```bash
curl -X POST "http://localhost:8010/functions/v1/detect-skus" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{
    "imageBase64": "ZmFrZS1pbWFnZS1ieXRlcw==",
    "tenantId": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
    "storeId": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
    "skusToDetect": [
      {
        "id": "sku-1",
        "name": "Cola 330ml",
        "imageUrls": ["https://example.com/cola.jpg"]
      }
    ]
  }'
```
Response `200`:
```json
{
  "success": true,
  "detectionId": "<uuid>",
  "result": {
    "detections": [
      {
        "skuId": "sku-1",
        "skuName": "Cola 330ml",
        "isAvailable": true,
        "facings": 1,
        "confidence": 0.9,
        "boundingBox": {
          "x": 0.1,
          "y": 0.1,
          "width": 0.2,
          "height": 0.2
        }
      }
    ],
    "missingSkus": [],
    "shareOfShelf": {
      "totalShelfArea": 1.0,
      "trainedProductsArea": 0.5,
      "percentage": 50.0
    },
    "totalFacings": 1,
    "summary": "Detection completed"
  }
}
```

### POST `/functions/v1/roboflow-detect`
Request:
```bash
curl -X POST "http://localhost:8010/functions/v1/roboflow-detect" \
  -H "apikey: super-api-key-change-me" \
  -H "Content-Type: application/json" \
  -d '{
    "imageUrl": "https://example.com/shelf.jpg",
    "shelfId": "b48392cc-c85c-4d5f-beef-c6813567ee8d",
    "tenantId": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254"
  }'
```
Response `200`:
```json
{
  "success": true,
  "result": {
    "workflow": "roboflow",
    "imageUrl": "https://example.com/shelf.jpg",
    "predictions": [],
    "status": "ok"
  }
}
```

---

## 6) Storage Endpoints

### POST `/storage/v1/object/shelf-images/{path}`
Request:
```bash
curl -X POST "http://localhost:8010/storage/v1/object/shelf-images/d94b7aa1-fd11-4915-85f6-1bf6cc5f6254/2026-02-18/shelf.jpg" \
  -H "apikey: super-api-key-change-me" \
  -F "file=@./shelf.jpg"
```
Response `200`:
```json
{
  "Key": "shelf-images/d94b7aa1-fd11-4915-85f6-1bf6cc5f6254/2026-02-18/shelf.jpg"
}
```

### GET `/storage/v1/object/shelf-images/{path}`
Request:
```bash
curl -X GET "http://localhost:8010/storage/v1/object/shelf-images/d94b7aa1-fd11-4915-85f6-1bf6cc5f6254/2026-02-18/shelf.jpg" \
  -H "apikey: super-api-key-change-me" --output shelf-downloaded.jpg
```
Response `200`: binary image file

### POST `/storage/v1/object/sku-training-images/{path}`
Request:
```bash
curl -X POST "http://localhost:8010/storage/v1/object/sku-training-images/d94b7aa1-fd11-4915-85f6-1bf6cc5f6254/sku-1/sku.jpg" \
  -H "apikey: super-api-key-change-me" \
  -F "file=@./sku.jpg"
```
Response `200`:
```json
{
  "Key": "sku-training-images/d94b7aa1-fd11-4915-85f6-1bf6cc5f6254/sku-1/sku.jpg"
}
```

### GET `/storage/v1/object/sku-training-images/{path}`
Request:
```bash
curl -X GET "http://localhost:8010/storage/v1/object/sku-training-images/d94b7aa1-fd11-4915-85f6-1bf6cc5f6254/sku-1/sku.jpg" \
  -H "apikey: super-api-key-change-me" --output sku-downloaded.jpg
```
Response `200`: binary image file

---

## 7) Common Error Responses

### Unauthorized `401`
```json
{
  "detail": "Missing or invalid auth"
}
```

### Bad request `400`
```json
{
  "detail": "Invalid credentials"
}
```

### Not found `404`
```json
{
  "detail": "Unknown resource"
}
```

### Method not allowed `405`
```json
{
  "detail": "Delete not supported"
}
```

