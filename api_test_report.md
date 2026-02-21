# ShelfVision API Test Report

- Generated at: 2026-02-18T07:01:39.732985+00:00
- Base URL: http://127.0.0.1:8787
- Total tests: 65
- Passed (2xx): 65
- Failed (non-2xx): 0
- Expectation failures: 0

## 1. Health
- Method: `GET`
- Path: `/health`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
{
  "status": "ok"
}
```

## 2. Auth Signup
- Method: `POST`
- Path: `/auth/v1/signup`
- Status: `200`
- Request payload:
```json
{
  "email": "qa_1771398099@example.com",
  "password": "secret123",
  "data": {
    "full_name": "QA User"
  }
}
```
- Response:
```json
{
  "user": {
    "id": "fef61235-935c-4321-8fed-7b3f09d953f1",
    "email": "qa_1771398099@example.com"
  },
  "session": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmZWY2MTIzNS05MzVjLTQzMjEtOGZlZC03YjNmMDlkOTUzZjEiLCJleHAiOjE3NzE0ODQ0OTl9.nnlyjUyn5QUXQ5jOGMZxWOJ9yC1hxLDGrds376UQ0aE",
    "token_type": "bearer",
    "expires_in": 86400
  }
}
```

## 3. Auth Token Password
- Method: `POST`
- Path: `/auth/v1/token?grant_type=password`
- Status: `200`
- Request payload:
```json
{
  "email": "qa_1771398099@example.com",
  "password": "secret123"
}
```
- Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmZWY2MTIzNS05MzVjLTQzMjEtOGZlZC03YjNmMDlkOTUzZjEiLCJleHAiOjE3NzE0ODQ0OTl9.nnlyjUyn5QUXQ5jOGMZxWOJ9yC1hxLDGrds376UQ0aE",
  "refresh_token": "4339a650-3b83-4915-b078-e4653a244588",
  "expires_in": 86400,
  "token_type": "bearer",
  "user": {
    "id": "fef61235-935c-4321-8fed-7b3f09d953f1",
    "email": "qa_1771398099@example.com"
  }
}
```

## 4. Auth Logout
- Method: `POST`
- Path: `/auth/v1/logout`
- Status: `204`
- Request payload:
```json
null
```
- Response:
```json
null
```

## 5. Create Tenant
- Method: `POST`
- Path: `/rest/v1/tenants`
- Status: `201`
- Request payload:
```json
{
  "name": "Tenant-1771398099",
  "status": "active",
  "is_active": true
}
```
- Response:
```json
{
  "id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "name": "Tenant-1771398099",
  "status": "active",
  "is_active": true,
  "logo_url": null,
  "username": null,
  "password": null,
  "max_skus": 50,
  "max_images_per_month": 1000,
  "max_images_per_week": 300,
  "max_images_per_year": 10000,
  "processed_images_this_month": 0,
  "processed_images_this_week": 0,
  "processed_images_this_year": 0,
  "created_at": "2026-02-18T07:01:39.602248+00:00",
  "updated_at": "2026-02-18T07:01:39.602249+00:00"
}
```

## 6. List Tenants
- Method: `GET`
- Path: `/rest/v1/tenants?select=*&status=eq.active`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "88a46ea0-7868-47f8-87cb-9ba8c0bb0275",
    "name": "Tenant-1771397879",
    "status": "active",
    "is_active": true,
    "logo_url": "https://example.com/logo.png",
    "username": null,
    "password": null,
    "max_skus": 50,
    "max_images_per_month": 1000,
    "max_images_per_week": 300,
    "max_images_per_year": 10000,
    "processed_images_this_month": 0,
    "processed_images_this_week": 0,
    "processed_images_this_year": 0,
    "created_at": "2026-02-18T06:57:59.123040+00:00",
    "updated_at": "2026-02-18T06:57:59.128286+00:00"
  },
  {
    "id": "302aef13-456d-405e-bb0b-bb592065eb36",
    "name": "Tenant-1771397902",
    "status": "active",
    "is_active": true,
    "logo_url": "https://example.com/logo.png",
    "username": null,
    "password": null,
    "max_skus": 50,
    "max_images_per_month": 1000,
    "max_images_per_week": 300,
    "max_images_per_year": 10000,
    "processed_images_this_month": 4,
    "processed_images_this_week": 2,
    "processed_images_this_year": 2,
    "created_at": "2026-02-18T06:58:22.404901+00:00",
    "updated_at": "2026-02-18T06:58:22.493546+00:00"
  },
  {
    "id": "dd945445-1ea1-4d2f-b06c-2c86edfb0298",
    "name": "Tenant-1771397943",
    "status": "active",
    "is_active": true,
    "logo_url": "https://example.com/logo.png",
    "username": null,
    "password": null,
    "max_skus": 50,
    "max_images_per_month": 1000,
    "max_images_per_week": 300,
    "max_images_per_year": 10000,
    "processed_images_this_month": 4,
    "processed_images_this_week": 2,
    "processed_images_this_year": 2,
    "created_at": "2026-02-18T06:59:03.246350+00:00",
    "updated_at": "2026-02-18T06:59:03.315726+00:00"
  },
  {
    "id": "eb7f901b-aa61-4f87-b421-b98862754237",
    "name": "Tenant-1771397954",
    "status": "active",
    "is_active": true,
    "logo_url": "https://example.com/logo.png",
    "username": null,
    "password": null,
    "max_skus": 50,
    "max_images_per_month": 1000,
    "max_images_per_week": 300,
    "max_images_per_year": 10000,
    "processed_images_this_month": 4,
    "processed_images_this_week": 2,
    "processed_images_this_year": 2,
    "created_at": "2026-02-18T06:59:14.173299+00:00",
    "updated_at": "2026-02-18T06:59:14.262128+00:00"
  },
  {
    "id": "111608a9-b560-42a1-b72b-baa90c433b88",
    "name": "Tenant-1771398099",
    "status": "active",
    "is_active": true,
    "logo_url": null,
    "username": null,
    "password": null,
    "max_skus": 50,
    "max_images_per_month": 1000,
    "max_images_per_week": 300,
    "max_images_per_year": 10000,
    "processed_images_this_month": 0,
    "processed_images_this_week": 0,
    "processed_images_this_year": 0,
    "created_at": "2026-02-18T07:01:39.602248+00:00",
    "updated_at": "2026-02-18T07:01:39.602249+00:00"
  }
]
```

## 7. Update Tenant
- Method: `PATCH`
- Path: `/rest/v1/tenants?id=eq.111608a9-b560-42a1-b72b-baa90c433b88`
- Status: `200`
- Request payload:
```json
{
  "logo_url": "https://example.com/logo.png"
}
```
- Response:
```json
{
  "id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "name": "Tenant-1771398099",
  "status": "active",
  "is_active": true,
  "logo_url": "https://example.com/logo.png",
  "username": null,
  "password": null,
  "max_skus": 50,
  "max_images_per_month": 1000,
  "max_images_per_week": 300,
  "max_images_per_year": 10000,
  "processed_images_this_month": 0,
  "processed_images_this_week": 0,
  "processed_images_this_year": 0,
  "created_at": "2026-02-18T07:01:39.602248+00:00",
  "updated_at": "2026-02-18T07:01:39.607678+00:00"
}
```

## 8. Create Store
- Method: `POST`
- Path: `/rest/v1/stores`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "name": "Main Store",
  "city": "Cairo",
  "country": "EG"
}
```
- Response:
```json
{
  "id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "name": "Main Store",
  "address": null,
  "city": "Cairo",
  "country": "EG",
  "created_at": "2026-02-18T07:01:39.609965+00:00",
  "updated_at": "2026-02-18T07:01:39.609967+00:00"
}
```

## 9. List Stores
- Method: `GET`
- Path: `/rest/v1/stores?tenant_id=eq.111608a9-b560-42a1-b72b-baa90c433b88&select=*`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
    "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
    "name": "Main Store",
    "address": null,
    "city": "Cairo",
    "country": "EG",
    "created_at": "2026-02-18T07:01:39.609965+00:00",
    "updated_at": "2026-02-18T07:01:39.609967+00:00"
  }
]
```

## 10. Update Store
- Method: `PATCH`
- Path: `/rest/v1/stores?id=eq.7808be17-3cb7-48a1-a98b-9391b8d1f2ee`
- Status: `200`
- Request payload:
```json
{
  "address": "Street 123"
}
```
- Response:
```json
{
  "id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "name": "Main Store",
  "address": "Street 123",
  "city": "Cairo",
  "country": "EG",
  "created_at": "2026-02-18T07:01:39.609965+00:00",
  "updated_at": "2026-02-18T07:01:39.615026+00:00"
}
```

## 11. Create Category
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "name": "Beverages",
  "description": "Drinks"
}
```
- Response:
```json
{
  "id": "5e97e62e-d355-456a-ae1e-4e3c7f5bf2a0",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "name": "Beverages",
  "description": "Drinks",
  "created_at": "2026-02-18T07:01:39.617181+00:00",
  "updated_at": "2026-02-18T07:01:39.617182+00:00"
}
```

## 12. List Categories
- Method: `GET`
- Path: `/rest/v1/product_categories?tenant_id=eq.111608a9-b560-42a1-b72b-baa90c433b88`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "5e97e62e-d355-456a-ae1e-4e3c7f5bf2a0",
    "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
    "name": "Beverages",
    "description": "Drinks",
    "created_at": "2026-02-18T07:01:39.617181+00:00",
    "updated_at": "2026-02-18T07:01:39.617182+00:00"
  }
]
```

## 13. Create SKU
- Method: `POST`
- Path: `/rest/v1/skus`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "category_id": "5e97e62e-d355-456a-ae1e-4e3c7f5bf2a0",
  "name": "Cola 330ml",
  "description": "Soda",
  "barcode": "1234567890",
  "is_active": true,
  "training_status": "completed"
}
```
- Response:
```json
{
  "id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "category_id": "5e97e62e-d355-456a-ae1e-4e3c7f5bf2a0",
  "name": "Cola 330ml",
  "description": "Soda",
  "barcode": "1234567890",
  "is_active": true,
  "training_status": "completed",
  "created_at": "2026-02-18T07:01:39.620925+00:00",
  "updated_at": "2026-02-18T07:01:39.620927+00:00"
}
```

## 14. List SKUs
- Method: `GET`
- Path: `/rest/v1/skus?tenant_id=eq.111608a9-b560-42a1-b72b-baa90c433b88&category_id=eq.5e97e62e-d355-456a-ae1e-4e3c7f5bf2a0&is_active=eq.true&training_status=eq.completed&select=*`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
    "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
    "category_id": "5e97e62e-d355-456a-ae1e-4e3c7f5bf2a0",
    "name": "Cola 330ml",
    "description": "Soda",
    "barcode": "1234567890",
    "is_active": true,
    "training_status": "completed",
    "created_at": "2026-02-18T07:01:39.620925+00:00",
    "updated_at": "2026-02-18T07:01:39.620927+00:00"
  }
]
```

## 15. Create SKU Image
- Method: `POST`
- Path: `/rest/v1/sku_images`
- Status: `201`
- Request payload:
```json
{
  "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
  "image_url": "https://example.com/sku.jpg"
}
```
- Response:
```json
{
  "id": "8548102d-c51f-45e9-8364-fd51865f2399",
  "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
  "image_url": "https://example.com/sku.jpg",
  "created_at": "2026-02-18T07:01:39.625170+00:00"
}
```

## 16. List SKU Images
- Method: `GET`
- Path: `/rest/v1/sku_images?sku_id=eq.815724a9-fa4d-49f1-81a4-4e08f5c5a29b`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "8548102d-c51f-45e9-8364-fd51865f2399",
    "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
    "image_url": "https://example.com/sku.jpg",
    "created_at": "2026-02-18T07:01:39.625170+00:00"
  }
]
```

## 17. Create Shelf
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
  "name": "Aisle A Shelf 1",
  "width_cm": 120
}
```
- Response:
```json
{
  "id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
  "name": "Aisle A Shelf 1",
  "description": null,
  "location_in_store": null,
  "width_cm": 120.0,
  "created_at": "2026-02-18T07:01:39.629021+00:00",
  "updated_at": "2026-02-18T07:01:39.629022+00:00"
}
```

## 18. List Shelves
- Method: `GET`
- Path: `/rest/v1/shelves?tenant_id=eq.111608a9-b560-42a1-b72b-baa90c433b88&store_id=eq.7808be17-3cb7-48a1-a98b-9391b8d1f2ee&select=*`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
    "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
    "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
    "name": "Aisle A Shelf 1",
    "description": null,
    "location_in_store": null,
    "width_cm": 120.0,
    "created_at": "2026-02-18T07:01:39.629021+00:00",
    "updated_at": "2026-02-18T07:01:39.629022+00:00"
  }
]
```

## 19. Update Shelf
- Method: `PATCH`
- Path: `/rest/v1/shelves?id=eq.fecce0bb-b3e2-48cb-9ab4-d34a3917c670`
- Status: `200`
- Request payload:
```json
{
  "location_in_store": "Near cashier"
}
```
- Response:
```json
{
  "id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
  "name": "Aisle A Shelf 1",
  "description": null,
  "location_in_store": "Near cashier",
  "width_cm": 120.0,
  "created_at": "2026-02-18T07:01:39.629021+00:00",
  "updated_at": "2026-02-18T07:01:39.633469+00:00"
}
```

## 20. Create Shelf Product
- Method: `POST`
- Path: `/rest/v1/shelf_products`
- Status: `201`
- Request payload:
```json
{
  "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
  "expected_facings": 5,
  "position_order": 1
}
```
- Response:
```json
{
  "id": "970403c6-9f6b-4479-94ea-fde71ae7e60c",
  "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
  "expected_facings": 5,
  "position_order": 1,
  "created_at": "2026-02-18T07:01:39.635686+00:00"
}
```

## 21. List Shelf Products
- Method: `GET`
- Path: `/rest/v1/shelf_products?shelf_id=eq.fecce0bb-b3e2-48cb-9ab4-d34a3917c670`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "970403c6-9f6b-4479-94ea-fde71ae7e60c",
    "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
    "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
    "expected_facings": 5,
    "position_order": 1,
    "created_at": "2026-02-18T07:01:39.635686+00:00"
  }
]
```

## 22. Create Shelf Image Record
- Method: `POST`
- Path: `/rest/v1/shelf_images`
- Status: `201`
- Request payload:
```json
{
  "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "image_url": "https://example.com/shelf.jpg"
}
```
- Response:
```json
{
  "id": "147c584e-5ef5-469a-9ee0-fa0cad1baca4",
  "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "image_url": "https://example.com/shelf.jpg",
  "detection_result": null,
  "processed_at": null,
  "created_at": "2026-02-18T07:01:39.639193+00:00"
}
```

## 23. List Shelf Images
- Method: `GET`
- Path: `/rest/v1/shelf_images?shelf_id=eq.fecce0bb-b3e2-48cb-9ab4-d34a3917c670`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "147c584e-5ef5-469a-9ee0-fa0cad1baca4",
    "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
    "image_url": "https://example.com/shelf.jpg",
    "detection_result": null,
    "processed_at": null,
    "created_at": "2026-02-18T07:01:39.639193+00:00"
  }
]
```

## 24. Create Planogram Template
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
  "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "name": "Template 1",
  "status": "active",
  "layout": [
    {
      "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
      "facings": 5
    }
  ]
}
```
- Response:
```json
{
  "id": "4c357502-1ba6-4cb7-8240-d00dcf18701e",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
  "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "name": "Template 1",
  "description": null,
  "status": "active",
  "layout": [
    {
      "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
      "facings": 5
    }
  ],
  "created_by": null,
  "created_at": "2026-02-18T07:01:39.643018+00:00",
  "updated_at": "2026-02-18T07:01:39.643019+00:00"
}
```

## 25. List Planogram Templates
- Method: `GET`
- Path: `/rest/v1/planogram_templates?tenant_id=eq.111608a9-b560-42a1-b72b-baa90c433b88&status=eq.active&select=*`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "4c357502-1ba6-4cb7-8240-d00dcf18701e",
    "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
    "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
    "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
    "name": "Template 1",
    "description": null,
    "status": "active",
    "layout": [
      {
        "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
        "facings": 5
      }
    ],
    "created_by": null,
    "created_at": "2026-02-18T07:01:39.643018+00:00",
    "updated_at": "2026-02-18T07:01:39.643019+00:00"
  }
]
```

## 26. Update Planogram Template
- Method: `PATCH`
- Path: `/rest/v1/planogram_templates?id=eq.4c357502-1ba6-4cb7-8240-d00dcf18701e`
- Status: `200`
- Request payload:
```json
{
  "description": "Updated template"
}
```
- Response:
```json
{
  "id": "4c357502-1ba6-4cb7-8240-d00dcf18701e",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
  "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "name": "Template 1",
  "description": "Updated template",
  "status": "active",
  "layout": [
    {
      "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
      "facings": 5
    }
  ],
  "created_by": null,
  "created_at": "2026-02-18T07:01:39.643018+00:00",
  "updated_at": "2026-02-18T07:01:39.649918+00:00"
}
```

## 27. Create Planogram Version
- Method: `POST`
- Path: `/rest/v1/planogram_versions`
- Status: `201`
- Request payload:
```json
{
  "template_id": "4c357502-1ba6-4cb7-8240-d00dcf18701e",
  "version_number": 1,
  "layout": [
    {
      "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b"
    }
  ]
}
```
- Response:
```json
{
  "id": "ce570084-8f83-4dd1-bf38-f7dc08a0f241",
  "template_id": "4c357502-1ba6-4cb7-8240-d00dcf18701e",
  "version_number": 1,
  "layout": [
    {
      "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b"
    }
  ],
  "change_notes": null,
  "created_by": null,
  "created_at": "2026-02-18T07:01:39.652569+00:00"
}
```

## 28. List Planogram Versions
- Method: `GET`
- Path: `/rest/v1/planogram_versions?template_id=eq.4c357502-1ba6-4cb7-8240-d00dcf18701e&order=version_number.desc`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "ce570084-8f83-4dd1-bf38-f7dc08a0f241",
    "template_id": "4c357502-1ba6-4cb7-8240-d00dcf18701e",
    "version_number": 1,
    "layout": [
      {
        "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b"
      }
    ],
    "change_notes": null,
    "created_by": null,
    "created_at": "2026-02-18T07:01:39.652569+00:00"
  }
]
```

## 29. Create Compliance Scan
- Method: `POST`
- Path: `/rest/v1/compliance_scans`
- Status: `201`
- Request payload:
```json
{
  "template_id": "4c357502-1ba6-4cb7-8240-d00dcf18701e",
  "shelf_image_id": "147c584e-5ef5-469a-9ee0-fa0cad1baca4",
  "image_url": "https://example.com/scan.jpg",
  "compliance_score": 92.5,
  "total_expected": 10,
  "total_found": 9,
  "total_missing": 1,
  "total_extra": 0
}
```
- Response:
```json
{
  "id": "954e75ea-148e-48af-9442-fcd7eaffbe45",
  "template_id": "4c357502-1ba6-4cb7-8240-d00dcf18701e",
  "shelf_image_id": "147c584e-5ef5-469a-9ee0-fa0cad1baca4",
  "image_url": "https://example.com/scan.jpg",
  "compliance_score": 92.5,
  "total_expected": 10,
  "total_found": 9,
  "total_missing": 1,
  "total_extra": 0,
  "details": null,
  "scanned_by": null,
  "created_at": "2026-02-18T07:01:39.658086+00:00"
}
```

## 30. List Compliance Scans
- Method: `GET`
- Path: `/rest/v1/compliance_scans?template_id=eq.4c357502-1ba6-4cb7-8240-d00dcf18701e&order=created_at.desc`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "954e75ea-148e-48af-9442-fcd7eaffbe45",
    "template_id": "4c357502-1ba6-4cb7-8240-d00dcf18701e",
    "shelf_image_id": "147c584e-5ef5-469a-9ee0-fa0cad1baca4",
    "image_url": "https://example.com/scan.jpg",
    "compliance_score": 92.5,
    "total_expected": 10,
    "total_found": 9,
    "total_missing": 1,
    "total_extra": 0,
    "details": null,
    "scanned_by": null,
    "created_at": "2026-02-18T07:01:39.658086+00:00"
  }
]
```

## 31. List Profiles
- Method: `GET`
- Path: `/rest/v1/profiles`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "aef9b33c-3ab4-4033-9458-7d3353e177a6",
    "user_id": "d06f6968-0d7f-4178-9a11-d80567f30cbb",
    "tenant_id": null,
    "full_name": "QA Updated",
    "username": "qa_user",
    "avatar_url": null,
    "last_login": "2026-02-18T06:57:59.118978+00:00",
    "created_at": "2026-02-18T06:57:59.109509+00:00",
    "updated_at": "2026-02-18T06:57:59.181385+00:00"
  },
  {
    "id": "ad08f6c8-26d6-4a44-afab-03d8eda784e8",
    "user_id": "54b16a9b-e163-44d8-95df-ee52ee258755",
    "tenant_id": null,
    "full_name": "QA Updated",
    "username": "qa_user",
    "avatar_url": null,
    "last_login": "2026-02-18T06:58:22.401346+00:00",
    "created_at": "2026-02-18T06:58:22.392807+00:00",
    "updated_at": "2026-02-18T06:58:22.461758+00:00"
  },
  {
    "id": "1351151f-165e-4958-ada3-e89a1ad2095c",
    "user_id": "6527c20d-3eb6-4ceb-b6e5-652d309a2b71",
    "tenant_id": null,
    "full_name": "QA Updated",
    "username": "qa_user",
    "avatar_url": null,
    "last_login": "2026-02-18T06:59:03.243500+00:00",
    "created_at": "2026-02-18T06:59:03.237504+00:00",
    "updated_at": "2026-02-18T06:59:03.293107+00:00"
  },
  {
    "id": "2d7e0c2c-0b3c-441e-a7bd-e2012aeee4c4",
    "user_id": "2ea4ffed-7261-4cbc-87e0-a786b19fec5c",
    "tenant_id": null,
    "full_name": "QA Updated",
    "username": "qa_user",
    "avatar_url": null,
    "last_login": "2026-02-18T06:59:14.169757+00:00",
    "created_at": "2026-02-18T06:59:14.160652+00:00",
    "updated_at": "2026-02-18T06:59:14.230701+00:00"
  },
  {
    "id": "3da4e67c-3adb-476a-a921-96aab71d3699",
    "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
    "tenant_id": null,
    "full_name": "QA User",
    "username": null,
    "avatar_url": null,
    "last_login": "2026-02-18T07:01:39.598017+00:00",
    "created_at": "2026-02-18T07:01:39.588804+00:00",
    "updated_at": "2026-02-18T07:01:39.598437+00:00"
  }
]
```

## 32. Update Profile
- Method: `PATCH`
- Path: `/rest/v1/profiles?user_id=eq.fef61235-935c-4321-8fed-7b3f09d953f1`
- Status: `200`
- Request payload:
```json
{
  "username": "qa_user",
  "full_name": "QA Updated"
}
```
- Response:
```json
{
  "id": "3da4e67c-3adb-476a-a921-96aab71d3699",
  "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "tenant_id": null,
  "full_name": "QA Updated",
  "username": "qa_user",
  "avatar_url": null,
  "last_login": "2026-02-18T07:01:39.598017+00:00",
  "created_at": "2026-02-18T07:01:39.588804+00:00",
  "updated_at": "2026-02-18T07:01:39.664588+00:00"
}
```

## 33. Create User Role
- Method: `POST`
- Path: `/rest/v1/user_roles`
- Status: `201`
- Request payload:
```json
{
  "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "role": "tenant_admin"
}
```
- Response:
```json
{
  "id": "ff0f655f-e00e-42ab-97fb-717a13699f65",
  "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "role": "tenant_admin"
}
```

## 34. List User Roles
- Method: `GET`
- Path: `/rest/v1/user_roles?user_id=eq.fef61235-935c-4321-8fed-7b3f09d953f1`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "ff0f655f-e00e-42ab-97fb-717a13699f65",
    "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
    "role": "tenant_admin"
  }
]
```

## 35. Create User Store Access
- Method: `POST`
- Path: `/rest/v1/user_store_access`
- Status: `201`
- Request payload:
```json
{
  "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee"
}
```
- Response:
```json
{
  "id": "7cae5757-b3e7-45dc-b5f2-356db98539b2",
  "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
  "created_at": "2026-02-18T07:01:39.670842+00:00"
}
```

## 36. List User Store Access
- Method: `GET`
- Path: `/rest/v1/user_store_access?user_id=eq.fef61235-935c-4321-8fed-7b3f09d953f1&store_id=eq.7808be17-3cb7-48a1-a98b-9391b8d1f2ee`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "7cae5757-b3e7-45dc-b5f2-356db98539b2",
    "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
    "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
    "created_at": "2026-02-18T07:01:39.670842+00:00"
  }
]
```

## 37. Create User Shelf Access
- Method: `POST`
- Path: `/rest/v1/user_shelf_access`
- Status: `201`
- Request payload:
```json
{
  "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670"
}
```
- Response:
```json
{
  "id": "79f67bfb-a3b8-4514-8d95-c6894dda3978",
  "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "created_at": "2026-02-18T07:01:39.674487+00:00"
}
```

## 38. List User Shelf Access
- Method: `GET`
- Path: `/rest/v1/user_shelf_access?user_id=eq.fef61235-935c-4321-8fed-7b3f09d953f1&shelf_id=eq.fecce0bb-b3e2-48cb-9ab4-d34a3917c670`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "79f67bfb-a3b8-4514-8d95-c6894dda3978",
    "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
    "shelf_id": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
    "created_at": "2026-02-18T07:01:39.674487+00:00"
  }
]
```

## 39. Create Notification
- Method: `POST`
- Path: `/rest/v1/notifications`
- Status: `201`
- Request payload:
```json
{
  "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "title": "Low Stock",
  "message": "SKU below threshold",
  "type": "alert",
  "is_read": false,
  "metadata": {
    "sku_id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b"
  }
}
```
- Response:
```json
{
  "id": "38073916-8f34-4f51-947d-34af42169243",
  "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "title": "Low Stock",
  "message": "SKU below threshold",
  "type": "alert",
  "is_read": false,
  "metadata": null,
  "created_at": "2026-02-18T07:01:39.678083+00:00"
}
```

## 40. List Notifications
- Method: `GET`
- Path: `/rest/v1/notifications?user_id=eq.fef61235-935c-4321-8fed-7b3f09d953f1&is_read=eq.false`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "38073916-8f34-4f51-947d-34af42169243",
    "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
    "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
    "title": "Low Stock",
    "message": "SKU below threshold",
    "type": "alert",
    "is_read": false,
    "metadata": null,
    "created_at": "2026-02-18T07:01:39.678083+00:00"
  }
]
```

## 41. Patch Notification
- Method: `PATCH`
- Path: `/rest/v1/notifications?id=eq.38073916-8f34-4f51-947d-34af42169243`
- Status: `200`
- Request payload:
```json
{
  "is_read": true
}
```
- Response:
```json
{
  "id": "38073916-8f34-4f51-947d-34af42169243",
  "user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "title": "Low Stock",
  "message": "SKU below threshold",
  "type": "alert",
  "is_read": true,
  "metadata": null,
  "created_at": "2026-02-18T07:01:39.678083+00:00"
}
```

## 42. RPC Check Tenant Quota
- Method: `POST`
- Path: `/rest/v1/rpc/check_tenant_quota`
- Status: `200`
- Request payload:
```json
{
  "_tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88"
}
```
- Response:
```json
{
  "tenantId": "111608a9-b560-42a1-b72b-baa90c433b88",
  "canProcess": true,
  "monthlyUsage": 0,
  "monthlyLimit": 1000,
  "weeklyUsage": 0,
  "weeklyLimit": 300,
  "yearlyUsage": 0,
  "yearlyLimit": 10000
}
```

## 43. RPC Increment Usage Metric
- Method: `POST`
- Path: `/rest/v1/rpc/increment_usage_metric`
- Status: `200`
- Request payload:
```json
{
  "_tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
  "_period_type": "monthly",
  "_images_count": 2
}
```
- Response:
```json
{
  "success": true
}
```

## 44. RPC Get User Tenant ID
- Method: `POST`
- Path: `/rest/v1/rpc/get_user_tenant_id`
- Status: `200`
- Request payload:
```json
{
  "_user_id": "fef61235-935c-4321-8fed-7b3f09d953f1"
}
```
- Response:
```json
{
  "tenant_id": null
}
```

## 45. RPC Has Role
- Method: `POST`
- Path: `/rest/v1/rpc/has_role`
- Status: `200`
- Request payload:
```json
{
  "_user_id": "fef61235-935c-4321-8fed-7b3f09d953f1",
  "_role": "tenant_admin"
}
```
- Response:
```json
{
  "has_role": true
}
```

## 46. Function Detect SKUs
- Method: `POST`
- Path: `/functions/v1/detect-skus`
- Status: `200`
- Request payload:
```json
{
  "imageBase64": "ZmFrZS1pbWFnZS1ieXRlcw==",
  "tenantId": "111608a9-b560-42a1-b72b-baa90c433b88",
  "storeId": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
  "skusToDetect": [
    {
      "id": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
      "name": "Cola 330ml",
      "imageUrls": [
        "https://example.com/sku.jpg"
      ]
    }
  ]
}
```
- Response:
```json
{
  "success": true,
  "detectionId": "a245b504-e6cf-4772-8417-324f1d12fbce",
  "result": {
    "detections": [
      {
        "skuId": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
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

## 47. Function Roboflow Detect
- Method: `POST`
- Path: `/functions/v1/roboflow-detect`
- Status: `200`
- Request payload:
```json
{
  "imageUrl": "https://example.com/shelf.jpg",
  "shelfId": "fecce0bb-b3e2-48cb-9ab4-d34a3917c670",
  "tenantId": "111608a9-b560-42a1-b72b-baa90c433b88"
}
```
- Response:
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

## 48. Storage Upload Shelf Image
- Method: `POST`
- Path: `/storage/v1/object/shelf-images/111608a9-b560-42a1-b72b-baa90c433b88/2026-02-18/shelf.jpg`
- Status: `200`
- Request payload:
```json
{
  "file": "<binary image/jpeg 20 bytes>"
}
```
- Response:
```json
{
  "Key": "shelf-images/111608a9-b560-42a1-b72b-baa90c433b88/2026-02-18/shelf.jpg"
}
```

## 49. Storage Download Shelf Image
- Method: `GET`
- Path: `/storage/v1/object/shelf-images/111608a9-b560-42a1-b72b-baa90c433b88/2026-02-18/shelf.jpg`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
"fake-jpeg-shelf-data"
```

## 50. Storage Upload SKU Training Image
- Method: `POST`
- Path: `/storage/v1/object/sku-training-images/111608a9-b560-42a1-b72b-baa90c433b88/815724a9-fa4d-49f1-81a4-4e08f5c5a29b/sku.jpg`
- Status: `200`
- Request payload:
```json
{
  "file": "<binary image/jpeg 27 bytes>"
}
```
- Response:
```json
{
  "Key": "sku-training-images/111608a9-b560-42a1-b72b-baa90c433b88/815724a9-fa4d-49f1-81a4-4e08f5c5a29b/sku.jpg"
}
```

## 51. Storage Download SKU Training Image
- Method: `GET`
- Path: `/storage/v1/object/sku-training-images/111608a9-b560-42a1-b72b-baa90c433b88/815724a9-fa4d-49f1-81a4-4e08f5c5a29b/sku.jpg`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
"fake-jpeg-sku-training-data"
```

## 52. List Detections
- Method: `GET`
- Path: `/rest/v1/detections?tenant_id=eq.111608a9-b560-42a1-b72b-baa90c433b88&store_id=eq.7808be17-3cb7-48a1-a98b-9391b8d1f2ee&order=processed_at.desc`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "a245b504-e6cf-4772-8417-324f1d12fbce",
    "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
    "store_id": "7808be17-3cb7-48a1-a98b-9391b8d1f2ee",
    "original_image_url": "/storage/v1/object/shelf-images/1df42595-05ca-4217-aa84-58271e99c845.jpg",
    "annotated_image_url": null,
    "detection_result": {
      "detections": [
        {
          "skuId": "815724a9-fa4d-49f1-81a4-4e08f5c5a29b",
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
      "missingSkus": []
    },
    "share_of_shelf_percentage": 50.0,
    "total_facings": 1,
    "detected_skus": 1,
    "missing_skus": 0,
    "processed_at": "2026-02-18T07:01:39.691659+00:00"
  }
]
```

## 53. List Usage Metrics
- Method: `GET`
- Path: `/rest/v1/usage_metrics?tenant_id=eq.111608a9-b560-42a1-b72b-baa90c433b88&period_type=eq.monthly`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[
  {
    "id": "ede08ed0-61e9-472c-8095-1341ad0ee79e",
    "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
    "period_type": "monthly",
    "period_start": "2026-02-18T07:01:39.685088+00:00",
    "images_processed": 2,
    "training_jobs": 0,
    "created_at": "2026-02-18T07:01:39.686478+00:00",
    "updated_at": "2026-02-18T07:01:39.686479+00:00"
  },
  {
    "id": "022e2929-4eda-48e5-8ee6-3872a0337831",
    "tenant_id": "111608a9-b560-42a1-b72b-baa90c433b88",
    "period_type": "monthly",
    "period_start": "2026-02-18T07:01:39.691169+00:00",
    "images_processed": 1,
    "training_jobs": 0,
    "created_at": "2026-02-18T07:01:39.692387+00:00",
    "updated_at": "2026-02-18T07:01:39.692388+00:00"
  }
]
```

## 54. List Models
- Method: `GET`
- Path: `/rest/v1/models?tenant_id=eq.111608a9-b560-42a1-b72b-baa90c433b88`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[]
```

## 55. List Processing Jobs
- Method: `GET`
- Path: `/rest/v1/processing_jobs?tenant_id=eq.111608a9-b560-42a1-b72b-baa90c433b88&status=eq.pending`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[]
```

## 56. List Detection Results
- Method: `GET`
- Path: `/rest/v1/detection_results?job_id=eq.non-existent`
- Status: `200`
- Request payload:
```json
null
```
- Response:
```json
[]
```

## 57. Delete SKU Image
- Method: `DELETE`
- Path: `/rest/v1/sku_images?id=eq.8548102d-c51f-45e9-8364-fd51865f2399`
- Status: `204`
- Request payload:
```json
null
```
- Response:
```json
null
```

## 58. Delete User Store Access
- Method: `DELETE`
- Path: `/rest/v1/user_store_access?id=eq.7cae5757-b3e7-45dc-b5f2-356db98539b2`
- Status: `204`
- Request payload:
```json
null
```
- Response:
```json
null
```

## 59. Delete User Shelf Access
- Method: `DELETE`
- Path: `/rest/v1/user_shelf_access?id=eq.79f67bfb-a3b8-4514-8d95-c6894dda3978`
- Status: `204`
- Request payload:
```json
null
```
- Response:
```json
null
```

## 60. Delete Shelf Product
- Method: `DELETE`
- Path: `/rest/v1/shelf_products?id=eq.970403c6-9f6b-4479-94ea-fde71ae7e60c`
- Status: `204`
- Request payload:
```json
null
```
- Response:
```json
null
```

## 61. Delete SKU
- Method: `DELETE`
- Path: `/rest/v1/skus?id=eq.815724a9-fa4d-49f1-81a4-4e08f5c5a29b`
- Status: `204`
- Request payload:
```json
null
```
- Response:
```json
null
```

## 62. Delete Category
- Method: `DELETE`
- Path: `/rest/v1/product_categories?id=eq.5e97e62e-d355-456a-ae1e-4e3c7f5bf2a0`
- Status: `204`
- Request payload:
```json
null
```
- Response:
```json
null
```

## 63. Delete Shelf
- Method: `DELETE`
- Path: `/rest/v1/shelves?id=eq.fecce0bb-b3e2-48cb-9ab4-d34a3917c670`
- Status: `204`
- Request payload:
```json
null
```
- Response:
```json
null
```

## 64. Delete Store
- Method: `DELETE`
- Path: `/rest/v1/stores?id=eq.7808be17-3cb7-48a1-a98b-9391b8d1f2ee`
- Status: `204`
- Request payload:
```json
null
```
- Response:
```json
null
```

## 65. Delete Tenant
- Method: `DELETE`
- Path: `/rest/v1/tenants?id=eq.111608a9-b560-42a1-b72b-baa90c433b88`
- Status: `204`
- Request payload:
```json
null
```
- Response:
```json
null
```

