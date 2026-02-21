# Realistic User Workflow Test Report

- Generated at: 2026-02-18T10:26:26.604751+00:00
- Base URL: http://127.0.0.1:8010
- Scenario: Create realistic tenant/stores/shelves/planograms, assign to user, login with provided credentials, verify assigned data.
- Persistence: All created data kept in database (no cleanup).

## Summary
```json
{
  "run_id": 1771410386,
  "email_used": "a.salameh@cortanexai.com",
  "password_used": "123456",
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "stores_created_count": 5,
  "planograms_created_count": 50,
  "expected_stores": 5,
  "expected_planograms": 50,
  "login_response_stores_count": 5,
  "login_response_planograms_count": 50,
  "missing_created_stores_in_login_response": [],
  "missing_created_planograms_in_login_response": [],
  "data_persistence": "No delete/cleanup operations executed; data intentionally persisted."
}
```

## 1. Health Check
- Timestamp: `2026-02-18T10:26:26.123762+00:00`
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

## 2. Signup User
- Timestamp: `2026-02-18T10:26:26.270314+00:00`
- Method: `POST`
- Path: `/auth/v1/signup`
- Status: `200`
- Request payload:
```json
{
  "email": "a.salameh@cortanexai.com",
  "password": "123456",
  "data": {
    "full_name": "Ahmad Salameh"
  }
}
```
- Response:
```json
{
  "user": {
    "id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
    "email": "a.salameh@cortanexai.com"
  },
  "session": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlMjZmMzY4ZC1jOWEzLTRhY2MtYTlmZi0wYTQwMmFiNzczNjQiLCJleHAiOjE3NzE0OTY3ODZ9.0f937YZRQl9Wj0CtfKGzcntw-ZnI1sTfR8eFbnuIPAM",
    "token_type": "bearer",
    "expires_in": 86400
  }
}
```

## 3. Create Tenant
- Timestamp: `2026-02-18T10:26:26.290447+00:00`
- Method: `POST`
- Path: `/rest/v1/tenants`
- Status: `201`
- Request payload:
```json
{
  "name": "Cortanex Retail Group 1771410386",
  "status": "active",
  "is_active": true,
  "logo_url": "https://cdn.cortanex.ai/brand/cortanex-retail-logo.png",
  "username": "ops_admin",
  "password": "masked",
  "max_skus": 1000,
  "max_images_per_month": 150000,
  "max_images_per_week": 35000,
  "max_images_per_year": 1878700
}
```
- Response:
```json
{
  "id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Retail Group 1771410386",
  "status": "active",
  "is_active": true,
  "logo_url": "https://cdn.cortanex.ai/brand/cortanex-retail-logo.png",
  "username": "ops_admin",
  "password": "masked",
  "max_skus": 1000,
  "max_images_per_month": 150000,
  "max_images_per_week": 35000,
  "max_images_per_year": 1878700,
  "processed_images_this_month": 0,
  "processed_images_this_week": 0,
  "processed_images_this_year": 0,
  "created_at": "2026-02-18T10:26:26.285610+00:00",
  "updated_at": "2026-02-18T10:26:26.285613+00:00"
}
```

## 4. Update User Profile
- Timestamp: `2026-02-18T10:26:26.300408+00:00`
- Method: `PATCH`
- Path: `/rest/v1/profiles?user_id=eq.e26f368d-c9a3-4acc-a9ff-0a402ab77364`
- Status: `200`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "username": "a.salameh",
  "full_name": "Ahmad Salameh",
  "avatar_url": "https://cdn.cortanex.ai/avatars/a.salameh.png"
}
```
- Response:
```json
{
  "id": "06c5e78a-a0f1-4ce8-b2a2-0fcdb58c6e92",
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "full_name": "Ahmad Salameh",
  "username": "a.salameh",
  "avatar_url": "https://cdn.cortanex.ai/avatars/a.salameh.png",
  "last_login": null,
  "created_at": "2026-02-18T10:26:26.246986+00:00",
  "updated_at": "2026-02-18T10:26:26.297838+00:00"
}
```

## 5. Create Category 1
- Timestamp: `2026-02-18T10:26:26.318628+00:00`
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Beverages",
  "description": "Beverages products category for regional assortment planning"
}
```
- Response:
```json
{
  "id": "b19ccf60-feb8-41a5-8957-7162b205c046",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Beverages",
  "description": "Beverages products category for regional assortment planning",
  "created_at": "2026-02-18T10:26:26.307365+00:00",
  "updated_at": "2026-02-18T10:26:26.307369+00:00"
}
```

## 6. Create Category 2
- Timestamp: `2026-02-18T10:26:26.321689+00:00`
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Dairy",
  "description": "Dairy products category for regional assortment planning"
}
```
- Response:
```json
{
  "id": "1b099334-1704-46ab-9d3b-ffe7a7e323bb",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Dairy",
  "description": "Dairy products category for regional assortment planning",
  "created_at": "2026-02-18T10:26:26.319479+00:00",
  "updated_at": "2026-02-18T10:26:26.319482+00:00"
}
```

## 7. Create Category 3
- Timestamp: `2026-02-18T10:26:26.324448+00:00`
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Snacks",
  "description": "Snacks products category for regional assortment planning"
}
```
- Response:
```json
{
  "id": "36d15e4c-6091-42a5-811f-b4960c39c405",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Snacks",
  "description": "Snacks products category for regional assortment planning",
  "created_at": "2026-02-18T10:26:26.322494+00:00",
  "updated_at": "2026-02-18T10:26:26.322497+00:00"
}
```

## 8. Create Category 4
- Timestamp: `2026-02-18T10:26:26.327007+00:00`
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Breakfast",
  "description": "Breakfast products category for regional assortment planning"
}
```
- Response:
```json
{
  "id": "7cfa8aa2-5783-402e-9f2e-ca8342392da9",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Breakfast",
  "description": "Breakfast products category for regional assortment planning",
  "created_at": "2026-02-18T10:26:26.325224+00:00",
  "updated_at": "2026-02-18T10:26:26.325227+00:00"
}
```

## 9. Create Category 5
- Timestamp: `2026-02-18T10:26:26.329189+00:00`
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cleaning",
  "description": "Cleaning products category for regional assortment planning"
}
```
- Response:
```json
{
  "id": "9fe9611b-4a18-4e04-b576-01c4016cddd6",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cleaning",
  "description": "Cleaning products category for regional assortment planning",
  "created_at": "2026-02-18T10:26:26.327676+00:00",
  "updated_at": "2026-02-18T10:26:26.327678+00:00"
}
```

## 10. Create Category 6
- Timestamp: `2026-02-18T10:26:26.331163+00:00`
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Personal Care",
  "description": "Personal Care products category for regional assortment planning"
}
```
- Response:
```json
{
  "id": "3c9e3d98-14bc-4325-94c4-3399da184435",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Personal Care",
  "description": "Personal Care products category for regional assortment planning",
  "created_at": "2026-02-18T10:26:26.329841+00:00",
  "updated_at": "2026-02-18T10:26:26.329843+00:00"
}
```

## 11. Create Category 7
- Timestamp: `2026-02-18T10:26:26.333390+00:00`
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Canned Food",
  "description": "Canned Food products category for regional assortment planning"
}
```
- Response:
```json
{
  "id": "54e99137-f32e-4a96-8230-f744f31ed230",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Canned Food",
  "description": "Canned Food products category for regional assortment planning",
  "created_at": "2026-02-18T10:26:26.331756+00:00",
  "updated_at": "2026-02-18T10:26:26.331757+00:00"
}
```

## 12. Create Category 8
- Timestamp: `2026-02-18T10:26:26.335631+00:00`
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Frozen",
  "description": "Frozen products category for regional assortment planning"
}
```
- Response:
```json
{
  "id": "dbdb93eb-a894-4b45-892b-154f79a723fa",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Frozen",
  "description": "Frozen products category for regional assortment planning",
  "created_at": "2026-02-18T10:26:26.334079+00:00",
  "updated_at": "2026-02-18T10:26:26.334081+00:00"
}
```

## 13. Create Category 9
- Timestamp: `2026-02-18T10:26:26.337830+00:00`
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Bakery",
  "description": "Bakery products category for regional assortment planning"
}
```
- Response:
```json
{
  "id": "43b147c0-8bb8-43ce-9cb9-3fdaf3141d2c",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Bakery",
  "description": "Bakery products category for regional assortment planning",
  "created_at": "2026-02-18T10:26:26.336178+00:00",
  "updated_at": "2026-02-18T10:26:26.336179+00:00"
}
```

## 14. Create Category 10
- Timestamp: `2026-02-18T10:26:26.340116+00:00`
- Method: `POST`
- Path: `/rest/v1/product_categories`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Pet Care",
  "description": "Pet Care products category for regional assortment planning"
}
```
- Response:
```json
{
  "id": "98a65e26-688d-4644-8002-e5966a4d79bb",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Pet Care",
  "description": "Pet Care products category for regional assortment planning",
  "created_at": "2026-02-18T10:26:26.338619+00:00",
  "updated_at": "2026-02-18T10:26:26.338620+00:00"
}
```

## 15. Create Store 1
- Timestamp: `2026-02-18T10:26:26.342610+00:00`
- Method: `POST`
- Path: `/rest/v1/stores`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Hypermarket - Amman West",
  "address": "Wasfi Al Tal Street, Building 221",
  "city": "Amman",
  "country": "Jordan"
}
```
- Response:
```json
{
  "id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Hypermarket - Amman West",
  "address": "Wasfi Al Tal Street, Building 221",
  "city": "Amman",
  "country": "Jordan",
  "created_at": "2026-02-18T10:26:26.341126+00:00",
  "updated_at": "2026-02-18T10:26:26.341127+00:00"
}
```

## 16. Assign Store 1 To User
- Timestamp: `2026-02-18T10:26:26.345858+00:00`
- Method: `POST`
- Path: `/rest/v1/user_store_access`
- Status: `201`
- Request payload:
```json
{
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65"
}
```
- Response:
```json
{
  "id": "43f3f590-f2d3-4cd1-8efa-f794ad843576",
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "created_at": "2026-02-18T10:26:26.344334+00:00"
}
```

## 17. Create Shelf S1-P1
- Timestamp: `2026-02-18T10:26:26.350262+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 01",
  "description": "Main gondola shelf for aisle 1",
  "location_in_store": "Zone-2",
  "width_cm": 125
}
```
- Response:
```json
{
  "id": "49b2c14f-52ea-4f44-977c-f21ae530f135",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 01",
  "description": "Main gondola shelf for aisle 1",
  "location_in_store": "Zone-2",
  "width_cm": 125.0,
  "created_at": "2026-02-18T10:26:26.347656+00:00",
  "updated_at": "2026-02-18T10:26:26.347659+00:00"
}
```

## 18. Create Planogram S1-P1
- Timestamp: `2026-02-18T10:26:26.354484+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "49b2c14f-52ea-4f44-977c-f21ae530f135",
  "name": "Amman Weekly Planogram 01",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 1, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Beverages",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Dairy",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Snacks",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "ec99684a-fb14-48e5-9be1-65f81758c375",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "49b2c14f-52ea-4f44-977c-f21ae530f135",
  "name": "Amman Weekly Planogram 01",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 1, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Beverages",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Dairy",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Snacks",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.352135+00:00",
  "updated_at": "2026-02-18T10:26:26.352138+00:00"
}
```

## 19. Create Shelf S1-P2
- Timestamp: `2026-02-18T10:26:26.356707+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 02",
  "description": "Main gondola shelf for aisle 2",
  "location_in_store": "Zone-3",
  "width_cm": 130
}
```
- Response:
```json
{
  "id": "4db4f75c-a725-4e92-9484-dcc786022224",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 02",
  "description": "Main gondola shelf for aisle 2",
  "location_in_store": "Zone-3",
  "width_cm": 130.0,
  "created_at": "2026-02-18T10:26:26.355087+00:00",
  "updated_at": "2026-02-18T10:26:26.355089+00:00"
}
```

## 20. Create Planogram S1-P2
- Timestamp: `2026-02-18T10:26:26.359113+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "4db4f75c-a725-4e92-9484-dcc786022224",
  "name": "Amman Weekly Planogram 02",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 2, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Dairy",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Snacks",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Breakfast",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "686b166e-8a0f-4cb1-a873-70a1a34fa3eb",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "4db4f75c-a725-4e92-9484-dcc786022224",
  "name": "Amman Weekly Planogram 02",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 2, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Dairy",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Snacks",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Breakfast",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.357229+00:00",
  "updated_at": "2026-02-18T10:26:26.357230+00:00"
}
```

## 21. Create Shelf S1-P3
- Timestamp: `2026-02-18T10:26:26.362017+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 03",
  "description": "Main gondola shelf for aisle 3",
  "location_in_store": "Zone-4",
  "width_cm": 135
}
```
- Response:
```json
{
  "id": "cb28b3cf-9e96-4de6-926b-a64d924da37b",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 03",
  "description": "Main gondola shelf for aisle 3",
  "location_in_store": "Zone-4",
  "width_cm": 135.0,
  "created_at": "2026-02-18T10:26:26.360096+00:00",
  "updated_at": "2026-02-18T10:26:26.360098+00:00"
}
```

## 22. Create Planogram S1-P3
- Timestamp: `2026-02-18T10:26:26.364425+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "cb28b3cf-9e96-4de6-926b-a64d924da37b",
  "name": "Amman Weekly Planogram 03",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 3, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Snacks",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Breakfast",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Cleaning",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "6404c8ab-68cc-4879-9c19-8966feb927c7",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "cb28b3cf-9e96-4de6-926b-a64d924da37b",
  "name": "Amman Weekly Planogram 03",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 3, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Snacks",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Breakfast",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Cleaning",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.362722+00:00",
  "updated_at": "2026-02-18T10:26:26.362724+00:00"
}
```

## 23. Create Shelf S1-P4
- Timestamp: `2026-02-18T10:26:26.366423+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 04",
  "description": "Main gondola shelf for aisle 4",
  "location_in_store": "Zone-5",
  "width_cm": 140
}
```
- Response:
```json
{
  "id": "13ebaccb-1de8-48ec-b4ec-3f2cff01012f",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 04",
  "description": "Main gondola shelf for aisle 4",
  "location_in_store": "Zone-5",
  "width_cm": 140.0,
  "created_at": "2026-02-18T10:26:26.365025+00:00",
  "updated_at": "2026-02-18T10:26:26.365027+00:00"
}
```

## 24. Create Planogram S1-P4
- Timestamp: `2026-02-18T10:26:26.368321+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "13ebaccb-1de8-48ec-b4ec-3f2cff01012f",
  "name": "Amman Weekly Planogram 04",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 4, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Breakfast",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Cleaning",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Personal Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "b16bcf6c-ea01-4c5b-ac98-bb0ba1e146d7",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "13ebaccb-1de8-48ec-b4ec-3f2cff01012f",
  "name": "Amman Weekly Planogram 04",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 4, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Breakfast",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Cleaning",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Personal Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.366978+00:00",
  "updated_at": "2026-02-18T10:26:26.366980+00:00"
}
```

## 25. Create Shelf S1-P5
- Timestamp: `2026-02-18T10:26:26.370114+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 05",
  "description": "Main gondola shelf for aisle 5",
  "location_in_store": "Zone-1",
  "width_cm": 145
}
```
- Response:
```json
{
  "id": "08fda374-978a-4868-9812-c68de5f5cdaf",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 05",
  "description": "Main gondola shelf for aisle 5",
  "location_in_store": "Zone-1",
  "width_cm": 145.0,
  "created_at": "2026-02-18T10:26:26.368922+00:00",
  "updated_at": "2026-02-18T10:26:26.368923+00:00"
}
```

## 26. Create Planogram S1-P5
- Timestamp: `2026-02-18T10:26:26.371966+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "08fda374-978a-4868-9812-c68de5f5cdaf",
  "name": "Amman Weekly Planogram 05",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 5, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Cleaning",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Personal Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Canned Food",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "ac97683f-e6eb-4c0e-9bac-a895dbd3a8b8",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "08fda374-978a-4868-9812-c68de5f5cdaf",
  "name": "Amman Weekly Planogram 05",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 5, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Cleaning",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Personal Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Canned Food",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.370704+00:00",
  "updated_at": "2026-02-18T10:26:26.370705+00:00"
}
```

## 27. Create Shelf S1-P6
- Timestamp: `2026-02-18T10:26:26.373900+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 06",
  "description": "Main gondola shelf for aisle 6",
  "location_in_store": "Zone-2",
  "width_cm": 150
}
```
- Response:
```json
{
  "id": "bb07434a-f72a-42f7-9f38-08c4c5d4c381",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 06",
  "description": "Main gondola shelf for aisle 6",
  "location_in_store": "Zone-2",
  "width_cm": 150.0,
  "created_at": "2026-02-18T10:26:26.372440+00:00",
  "updated_at": "2026-02-18T10:26:26.372442+00:00"
}
```

## 28. Create Planogram S1-P6
- Timestamp: `2026-02-18T10:26:26.375909+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "bb07434a-f72a-42f7-9f38-08c4c5d4c381",
  "name": "Amman Weekly Planogram 06",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 6, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Personal Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Canned Food",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Frozen",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "ac7e7dbe-51a4-45e2-b12d-a017a60d21c0",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "bb07434a-f72a-42f7-9f38-08c4c5d4c381",
  "name": "Amman Weekly Planogram 06",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 6, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Personal Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Canned Food",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Frozen",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.374389+00:00",
  "updated_at": "2026-02-18T10:26:26.374391+00:00"
}
```

## 29. Create Shelf S1-P7
- Timestamp: `2026-02-18T10:26:26.377962+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 07",
  "description": "Main gondola shelf for aisle 7",
  "location_in_store": "Zone-3",
  "width_cm": 155
}
```
- Response:
```json
{
  "id": "b9748be7-65b1-4f96-b67f-a152341cedc7",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 07",
  "description": "Main gondola shelf for aisle 7",
  "location_in_store": "Zone-3",
  "width_cm": 155.0,
  "created_at": "2026-02-18T10:26:26.376487+00:00",
  "updated_at": "2026-02-18T10:26:26.376489+00:00"
}
```

## 30. Create Planogram S1-P7
- Timestamp: `2026-02-18T10:26:26.380068+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "b9748be7-65b1-4f96-b67f-a152341cedc7",
  "name": "Amman Weekly Planogram 07",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 7, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Canned Food",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Frozen",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Bakery",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "215e150d-6639-4102-83a9-76d3d2d5f9e7",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "b9748be7-65b1-4f96-b67f-a152341cedc7",
  "name": "Amman Weekly Planogram 07",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 7, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Canned Food",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Frozen",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Bakery",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.378508+00:00",
  "updated_at": "2026-02-18T10:26:26.378509+00:00"
}
```

## 31. Create Shelf S1-P8
- Timestamp: `2026-02-18T10:26:26.381891+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 08",
  "description": "Main gondola shelf for aisle 8",
  "location_in_store": "Zone-4",
  "width_cm": 160
}
```
- Response:
```json
{
  "id": "64a6d85b-0e4c-46c6-ba86-45fbb2e3b35f",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 08",
  "description": "Main gondola shelf for aisle 8",
  "location_in_store": "Zone-4",
  "width_cm": 160.0,
  "created_at": "2026-02-18T10:26:26.380657+00:00",
  "updated_at": "2026-02-18T10:26:26.380659+00:00"
}
```

## 32. Create Planogram S1-P8
- Timestamp: `2026-02-18T10:26:26.383612+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "64a6d85b-0e4c-46c6-ba86-45fbb2e3b35f",
  "name": "Amman Weekly Planogram 08",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 8, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Frozen",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Bakery",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Pet Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "9f878ae7-56c3-431d-a569-7aea61898783",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "64a6d85b-0e4c-46c6-ba86-45fbb2e3b35f",
  "name": "Amman Weekly Planogram 08",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 8, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Frozen",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Bakery",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Pet Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.382420+00:00",
  "updated_at": "2026-02-18T10:26:26.382421+00:00"
}
```

## 33. Create Shelf S1-P9
- Timestamp: `2026-02-18T10:26:26.385326+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 09",
  "description": "Main gondola shelf for aisle 9",
  "location_in_store": "Zone-5",
  "width_cm": 165
}
```
- Response:
```json
{
  "id": "eb28dad9-67e3-495c-abbf-bcc8a6f80680",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 09",
  "description": "Main gondola shelf for aisle 9",
  "location_in_store": "Zone-5",
  "width_cm": 165.0,
  "created_at": "2026-02-18T10:26:26.384186+00:00",
  "updated_at": "2026-02-18T10:26:26.384188+00:00"
}
```

## 34. Create Planogram S1-P9
- Timestamp: `2026-02-18T10:26:26.387021+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "eb28dad9-67e3-495c-abbf-bcc8a6f80680",
  "name": "Amman Weekly Planogram 09",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 9, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Bakery",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Pet Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Beverages",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "f0e73a0d-a7be-40ca-b863-fc7fece862ba",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "eb28dad9-67e3-495c-abbf-bcc8a6f80680",
  "name": "Amman Weekly Planogram 09",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 9, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Bakery",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Pet Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Beverages",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.385807+00:00",
  "updated_at": "2026-02-18T10:26:26.385809+00:00"
}
```

## 35. Create Shelf S1-P10
- Timestamp: `2026-02-18T10:26:26.389455+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 10",
  "description": "Main gondola shelf for aisle 10",
  "location_in_store": "Zone-1",
  "width_cm": 170
}
```
- Response:
```json
{
  "id": "e7db90eb-7dd4-48b6-911e-9d6cd3da9862",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "name": "Amman - Aisle 10",
  "description": "Main gondola shelf for aisle 10",
  "location_in_store": "Zone-1",
  "width_cm": 170.0,
  "created_at": "2026-02-18T10:26:26.387495+00:00",
  "updated_at": "2026-02-18T10:26:26.387496+00:00"
}
```

## 36. Create Planogram S1-P10
- Timestamp: `2026-02-18T10:26:26.391877+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "e7db90eb-7dd4-48b6-911e-9d6cd3da9862",
  "name": "Amman Weekly Planogram 10",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 10, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Pet Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Beverages",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Dairy",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "4e886854-e96e-484e-a27b-a0ad319c6790",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
  "shelf_id": "e7db90eb-7dd4-48b6-911e-9d6cd3da9862",
  "name": "Amman Weekly Planogram 10",
  "description": "Planogram for Cortanex Hypermarket - Amman West shelf 10, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Pet Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Beverages",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Dairy",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.390170+00:00",
  "updated_at": "2026-02-18T10:26:26.390171+00:00"
}
```

## 37. Create Store 2
- Timestamp: `2026-02-18T10:26:26.394158+00:00`
- Method: `POST`
- Path: `/rest/v1/stores`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Hypermarket - Amman Downtown",
  "address": "King Hussein Street, Block 14",
  "city": "Amman",
  "country": "Jordan"
}
```
- Response:
```json
{
  "id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Hypermarket - Amman Downtown",
  "address": "King Hussein Street, Block 14",
  "city": "Amman",
  "country": "Jordan",
  "created_at": "2026-02-18T10:26:26.392564+00:00",
  "updated_at": "2026-02-18T10:26:26.392566+00:00"
}
```

## 38. Assign Store 2 To User
- Timestamp: `2026-02-18T10:26:26.396421+00:00`
- Method: `POST`
- Path: `/rest/v1/user_store_access`
- Status: `201`
- Request payload:
```json
{
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c"
}
```
- Response:
```json
{
  "id": "0c9493f3-f82c-47c3-aff7-44f58b6fc1ed",
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "created_at": "2026-02-18T10:26:26.394716+00:00"
}
```

## 39. Create Shelf S2-P1
- Timestamp: `2026-02-18T10:26:26.398415+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 01",
  "description": "Main gondola shelf for aisle 1",
  "location_in_store": "Zone-2",
  "width_cm": 125
}
```
- Response:
```json
{
  "id": "a1878a9f-06c7-45b1-8b5e-af356a03112c",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 01",
  "description": "Main gondola shelf for aisle 1",
  "location_in_store": "Zone-2",
  "width_cm": 125.0,
  "created_at": "2026-02-18T10:26:26.397090+00:00",
  "updated_at": "2026-02-18T10:26:26.397092+00:00"
}
```

## 40. Create Planogram S2-P1
- Timestamp: `2026-02-18T10:26:26.401272+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "a1878a9f-06c7-45b1-8b5e-af356a03112c",
  "name": "Amman Weekly Planogram 01",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 1, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Beverages",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Dairy",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Snacks",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "7e510172-55ad-43c5-814f-e8d7af1023da",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "a1878a9f-06c7-45b1-8b5e-af356a03112c",
  "name": "Amman Weekly Planogram 01",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 1, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Beverages",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Dairy",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Snacks",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.398968+00:00",
  "updated_at": "2026-02-18T10:26:26.398969+00:00"
}
```

## 41. Create Shelf S2-P2
- Timestamp: `2026-02-18T10:26:26.403255+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 02",
  "description": "Main gondola shelf for aisle 2",
  "location_in_store": "Zone-3",
  "width_cm": 130
}
```
- Response:
```json
{
  "id": "223bf5ed-c2aa-4c96-a302-d199b15844d0",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 02",
  "description": "Main gondola shelf for aisle 2",
  "location_in_store": "Zone-3",
  "width_cm": 130.0,
  "created_at": "2026-02-18T10:26:26.401969+00:00",
  "updated_at": "2026-02-18T10:26:26.401970+00:00"
}
```

## 42. Create Planogram S2-P2
- Timestamp: `2026-02-18T10:26:26.405422+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "223bf5ed-c2aa-4c96-a302-d199b15844d0",
  "name": "Amman Weekly Planogram 02",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 2, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Dairy",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Snacks",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Breakfast",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "f70b90d5-bb65-4150-92c6-487c5be53cd2",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "223bf5ed-c2aa-4c96-a302-d199b15844d0",
  "name": "Amman Weekly Planogram 02",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 2, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Dairy",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Snacks",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Breakfast",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.403831+00:00",
  "updated_at": "2026-02-18T10:26:26.403832+00:00"
}
```

## 43. Create Shelf S2-P3
- Timestamp: `2026-02-18T10:26:26.407672+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 03",
  "description": "Main gondola shelf for aisle 3",
  "location_in_store": "Zone-4",
  "width_cm": 135
}
```
- Response:
```json
{
  "id": "b44b077c-6d1c-451f-8857-ab838b41bc15",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 03",
  "description": "Main gondola shelf for aisle 3",
  "location_in_store": "Zone-4",
  "width_cm": 135.0,
  "created_at": "2026-02-18T10:26:26.406013+00:00",
  "updated_at": "2026-02-18T10:26:26.406014+00:00"
}
```

## 44. Create Planogram S2-P3
- Timestamp: `2026-02-18T10:26:26.409918+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "b44b077c-6d1c-451f-8857-ab838b41bc15",
  "name": "Amman Weekly Planogram 03",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 3, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Snacks",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Breakfast",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Cleaning",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "1160013a-3327-452b-8834-3aa834169241",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "b44b077c-6d1c-451f-8857-ab838b41bc15",
  "name": "Amman Weekly Planogram 03",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 3, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Snacks",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Breakfast",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Cleaning",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.408294+00:00",
  "updated_at": "2026-02-18T10:26:26.408295+00:00"
}
```

## 45. Create Shelf S2-P4
- Timestamp: `2026-02-18T10:26:26.411996+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 04",
  "description": "Main gondola shelf for aisle 4",
  "location_in_store": "Zone-5",
  "width_cm": 140
}
```
- Response:
```json
{
  "id": "2a043367-4b48-45e0-84dd-901782f3d668",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 04",
  "description": "Main gondola shelf for aisle 4",
  "location_in_store": "Zone-5",
  "width_cm": 140.0,
  "created_at": "2026-02-18T10:26:26.410456+00:00",
  "updated_at": "2026-02-18T10:26:26.410457+00:00"
}
```

## 46. Create Planogram S2-P4
- Timestamp: `2026-02-18T10:26:26.414136+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "2a043367-4b48-45e0-84dd-901782f3d668",
  "name": "Amman Weekly Planogram 04",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 4, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Breakfast",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Cleaning",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Personal Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "964612b5-e787-44f2-a4bf-3e9aef3c429a",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "2a043367-4b48-45e0-84dd-901782f3d668",
  "name": "Amman Weekly Planogram 04",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 4, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Breakfast",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Cleaning",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Personal Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.412504+00:00",
  "updated_at": "2026-02-18T10:26:26.412505+00:00"
}
```

## 47. Create Shelf S2-P5
- Timestamp: `2026-02-18T10:26:26.416379+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 05",
  "description": "Main gondola shelf for aisle 5",
  "location_in_store": "Zone-1",
  "width_cm": 145
}
```
- Response:
```json
{
  "id": "17d14d4c-ac70-461f-b46d-11eeead71d17",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 05",
  "description": "Main gondola shelf for aisle 5",
  "location_in_store": "Zone-1",
  "width_cm": 145.0,
  "created_at": "2026-02-18T10:26:26.415032+00:00",
  "updated_at": "2026-02-18T10:26:26.415033+00:00"
}
```

## 48. Create Planogram S2-P5
- Timestamp: `2026-02-18T10:26:26.419081+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "17d14d4c-ac70-461f-b46d-11eeead71d17",
  "name": "Amman Weekly Planogram 05",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 5, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Cleaning",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Personal Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Canned Food",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "80703e68-fd0e-4492-9e3a-d0ff68d8e89a",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "17d14d4c-ac70-461f-b46d-11eeead71d17",
  "name": "Amman Weekly Planogram 05",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 5, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Cleaning",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Personal Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Canned Food",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.417217+00:00",
  "updated_at": "2026-02-18T10:26:26.417218+00:00"
}
```

## 49. Create Shelf S2-P6
- Timestamp: `2026-02-18T10:26:26.421839+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 06",
  "description": "Main gondola shelf for aisle 6",
  "location_in_store": "Zone-2",
  "width_cm": 150
}
```
- Response:
```json
{
  "id": "0d35ef88-b002-432c-9b8c-fcdf0deb0d56",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 06",
  "description": "Main gondola shelf for aisle 6",
  "location_in_store": "Zone-2",
  "width_cm": 150.0,
  "created_at": "2026-02-18T10:26:26.420160+00:00",
  "updated_at": "2026-02-18T10:26:26.420163+00:00"
}
```

## 50. Create Planogram S2-P6
- Timestamp: `2026-02-18T10:26:26.424429+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "0d35ef88-b002-432c-9b8c-fcdf0deb0d56",
  "name": "Amman Weekly Planogram 06",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 6, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Personal Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Canned Food",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Frozen",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "c81d05bc-881b-4ba5-9b92-71e1ae4b1bc2",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "0d35ef88-b002-432c-9b8c-fcdf0deb0d56",
  "name": "Amman Weekly Planogram 06",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 6, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Personal Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Canned Food",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Frozen",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.422617+00:00",
  "updated_at": "2026-02-18T10:26:26.422619+00:00"
}
```

## 51. Create Shelf S2-P7
- Timestamp: `2026-02-18T10:26:26.427235+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 07",
  "description": "Main gondola shelf for aisle 7",
  "location_in_store": "Zone-3",
  "width_cm": 155
}
```
- Response:
```json
{
  "id": "306172ce-147f-47cb-9466-ae604c39ef62",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 07",
  "description": "Main gondola shelf for aisle 7",
  "location_in_store": "Zone-3",
  "width_cm": 155.0,
  "created_at": "2026-02-18T10:26:26.425226+00:00",
  "updated_at": "2026-02-18T10:26:26.425228+00:00"
}
```

## 52. Create Planogram S2-P7
- Timestamp: `2026-02-18T10:26:26.429974+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "306172ce-147f-47cb-9466-ae604c39ef62",
  "name": "Amman Weekly Planogram 07",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 7, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Canned Food",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Frozen",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Bakery",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "22ce6282-c478-4586-b8c1-8388da4d0eed",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "306172ce-147f-47cb-9466-ae604c39ef62",
  "name": "Amman Weekly Planogram 07",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 7, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Canned Food",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Frozen",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Bakery",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.428215+00:00",
  "updated_at": "2026-02-18T10:26:26.428217+00:00"
}
```

## 53. Create Shelf S2-P8
- Timestamp: `2026-02-18T10:26:26.432248+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 08",
  "description": "Main gondola shelf for aisle 8",
  "location_in_store": "Zone-4",
  "width_cm": 160
}
```
- Response:
```json
{
  "id": "e06bcbed-61c0-4b86-b64f-d27250861781",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 08",
  "description": "Main gondola shelf for aisle 8",
  "location_in_store": "Zone-4",
  "width_cm": 160.0,
  "created_at": "2026-02-18T10:26:26.430605+00:00",
  "updated_at": "2026-02-18T10:26:26.430606+00:00"
}
```

## 54. Create Planogram S2-P8
- Timestamp: `2026-02-18T10:26:26.434134+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "e06bcbed-61c0-4b86-b64f-d27250861781",
  "name": "Amman Weekly Planogram 08",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 8, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Frozen",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Bakery",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Pet Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "b137bd24-c683-43c4-9871-306bbad5c4a8",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "e06bcbed-61c0-4b86-b64f-d27250861781",
  "name": "Amman Weekly Planogram 08",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 8, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Frozen",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Bakery",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Pet Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.432852+00:00",
  "updated_at": "2026-02-18T10:26:26.432854+00:00"
}
```

## 55. Create Shelf S2-P9
- Timestamp: `2026-02-18T10:26:26.435902+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 09",
  "description": "Main gondola shelf for aisle 9",
  "location_in_store": "Zone-5",
  "width_cm": 165
}
```
- Response:
```json
{
  "id": "0eac5eb7-aab4-471c-bc56-f2fa30304a8c",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 09",
  "description": "Main gondola shelf for aisle 9",
  "location_in_store": "Zone-5",
  "width_cm": 165.0,
  "created_at": "2026-02-18T10:26:26.434655+00:00",
  "updated_at": "2026-02-18T10:26:26.434656+00:00"
}
```

## 56. Create Planogram S2-P9
- Timestamp: `2026-02-18T10:26:26.437702+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "0eac5eb7-aab4-471c-bc56-f2fa30304a8c",
  "name": "Amman Weekly Planogram 09",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 9, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Bakery",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Pet Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Beverages",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "3b407f2a-ca4d-4748-a94a-cae3f240c4c9",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "0eac5eb7-aab4-471c-bc56-f2fa30304a8c",
  "name": "Amman Weekly Planogram 09",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 9, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Bakery",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Pet Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Beverages",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.436440+00:00",
  "updated_at": "2026-02-18T10:26:26.436441+00:00"
}
```

## 57. Create Shelf S2-P10
- Timestamp: `2026-02-18T10:26:26.439496+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 10",
  "description": "Main gondola shelf for aisle 10",
  "location_in_store": "Zone-1",
  "width_cm": 170
}
```
- Response:
```json
{
  "id": "e4ba9019-2a9f-473c-a586-15e8dd14f20b",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "name": "Amman - Aisle 10",
  "description": "Main gondola shelf for aisle 10",
  "location_in_store": "Zone-1",
  "width_cm": 170.0,
  "created_at": "2026-02-18T10:26:26.438226+00:00",
  "updated_at": "2026-02-18T10:26:26.438228+00:00"
}
```

## 58. Create Planogram S2-P10
- Timestamp: `2026-02-18T10:26:26.441500+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "e4ba9019-2a9f-473c-a586-15e8dd14f20b",
  "name": "Amman Weekly Planogram 10",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 10, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Pet Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Beverages",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Dairy",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "2c8fd361-15de-48f3-b62b-ee7615335776",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
  "shelf_id": "e4ba9019-2a9f-473c-a586-15e8dd14f20b",
  "name": "Amman Weekly Planogram 10",
  "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 10, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Pet Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Beverages",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Dairy",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.440008+00:00",
  "updated_at": "2026-02-18T10:26:26.440009+00:00"
}
```

## 59. Create Store 3
- Timestamp: `2026-02-18T10:26:26.443509+00:00`
- Method: `POST`
- Path: `/rest/v1/stores`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Market - Irbid Center",
  "address": "University Street, Gate 3",
  "city": "Irbid",
  "country": "Jordan"
}
```
- Response:
```json
{
  "id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Market - Irbid Center",
  "address": "University Street, Gate 3",
  "city": "Irbid",
  "country": "Jordan",
  "created_at": "2026-02-18T10:26:26.442011+00:00",
  "updated_at": "2026-02-18T10:26:26.442012+00:00"
}
```

## 60. Assign Store 3 To User
- Timestamp: `2026-02-18T10:26:26.445572+00:00`
- Method: `POST`
- Path: `/rest/v1/user_store_access`
- Status: `201`
- Request payload:
```json
{
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a"
}
```
- Response:
```json
{
  "id": "753d961d-a753-463f-9fdd-f367e6e52ed9",
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "created_at": "2026-02-18T10:26:26.444030+00:00"
}
```

## 61. Create Shelf S3-P1
- Timestamp: `2026-02-18T10:26:26.447585+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 01",
  "description": "Main gondola shelf for aisle 1",
  "location_in_store": "Zone-2",
  "width_cm": 125
}
```
- Response:
```json
{
  "id": "61150307-1617-48fc-bb5a-17189361789d",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 01",
  "description": "Main gondola shelf for aisle 1",
  "location_in_store": "Zone-2",
  "width_cm": 125.0,
  "created_at": "2026-02-18T10:26:26.446092+00:00",
  "updated_at": "2026-02-18T10:26:26.446093+00:00"
}
```

## 62. Create Planogram S3-P1
- Timestamp: `2026-02-18T10:26:26.449337+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "61150307-1617-48fc-bb5a-17189361789d",
  "name": "Irbid Weekly Planogram 01",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 1, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Beverages",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Dairy",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Snacks",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "29e7a59b-2ca4-4088-8685-02d3550b23d7",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "61150307-1617-48fc-bb5a-17189361789d",
  "name": "Irbid Weekly Planogram 01",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 1, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Beverages",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Dairy",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Snacks",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.448091+00:00",
  "updated_at": "2026-02-18T10:26:26.448092+00:00"
}
```

## 63. Create Shelf S3-P2
- Timestamp: `2026-02-18T10:26:26.451451+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 02",
  "description": "Main gondola shelf for aisle 2",
  "location_in_store": "Zone-3",
  "width_cm": 130
}
```
- Response:
```json
{
  "id": "e09f9991-d187-4d0c-a449-aa1962e8b024",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 02",
  "description": "Main gondola shelf for aisle 2",
  "location_in_store": "Zone-3",
  "width_cm": 130.0,
  "created_at": "2026-02-18T10:26:26.450083+00:00",
  "updated_at": "2026-02-18T10:26:26.450084+00:00"
}
```

## 64. Create Planogram S3-P2
- Timestamp: `2026-02-18T10:26:26.453612+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "e09f9991-d187-4d0c-a449-aa1962e8b024",
  "name": "Irbid Weekly Planogram 02",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 2, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Dairy",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Snacks",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Breakfast",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "be1a3cd3-d844-402f-aeac-d6ba6bb24980",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "e09f9991-d187-4d0c-a449-aa1962e8b024",
  "name": "Irbid Weekly Planogram 02",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 2, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Dairy",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Snacks",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Breakfast",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.452277+00:00",
  "updated_at": "2026-02-18T10:26:26.452278+00:00"
}
```

## 65. Create Shelf S3-P3
- Timestamp: `2026-02-18T10:26:26.455716+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 03",
  "description": "Main gondola shelf for aisle 3",
  "location_in_store": "Zone-4",
  "width_cm": 135
}
```
- Response:
```json
{
  "id": "d416e787-de88-4d22-95f6-e7057218353e",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 03",
  "description": "Main gondola shelf for aisle 3",
  "location_in_store": "Zone-4",
  "width_cm": 135.0,
  "created_at": "2026-02-18T10:26:26.454347+00:00",
  "updated_at": "2026-02-18T10:26:26.454348+00:00"
}
```

## 66. Create Planogram S3-P3
- Timestamp: `2026-02-18T10:26:26.458180+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "d416e787-de88-4d22-95f6-e7057218353e",
  "name": "Irbid Weekly Planogram 03",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 3, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Snacks",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Breakfast",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Cleaning",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "b2ede40c-fbbe-4996-b690-5852eca0ded1",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "d416e787-de88-4d22-95f6-e7057218353e",
  "name": "Irbid Weekly Planogram 03",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 3, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Snacks",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Breakfast",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Cleaning",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.456545+00:00",
  "updated_at": "2026-02-18T10:26:26.456547+00:00"
}
```

## 67. Create Shelf S3-P4
- Timestamp: `2026-02-18T10:26:26.460301+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 04",
  "description": "Main gondola shelf for aisle 4",
  "location_in_store": "Zone-5",
  "width_cm": 140
}
```
- Response:
```json
{
  "id": "27ca3f2b-44ba-4e77-94f9-5e63f67d17fe",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 04",
  "description": "Main gondola shelf for aisle 4",
  "location_in_store": "Zone-5",
  "width_cm": 140.0,
  "created_at": "2026-02-18T10:26:26.458878+00:00",
  "updated_at": "2026-02-18T10:26:26.458879+00:00"
}
```

## 68. Create Planogram S3-P4
- Timestamp: `2026-02-18T10:26:26.462669+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "27ca3f2b-44ba-4e77-94f9-5e63f67d17fe",
  "name": "Irbid Weekly Planogram 04",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 4, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Breakfast",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Cleaning",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Personal Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "a663558b-ceed-41c1-a0f7-e1bb6c76d3c3",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "27ca3f2b-44ba-4e77-94f9-5e63f67d17fe",
  "name": "Irbid Weekly Planogram 04",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 4, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Breakfast",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Cleaning",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Personal Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.460901+00:00",
  "updated_at": "2026-02-18T10:26:26.460902+00:00"
}
```

## 69. Create Shelf S3-P5
- Timestamp: `2026-02-18T10:26:26.464768+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 05",
  "description": "Main gondola shelf for aisle 5",
  "location_in_store": "Zone-1",
  "width_cm": 145
}
```
- Response:
```json
{
  "id": "994e3a3f-daac-443d-8897-65c91c63e0e5",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 05",
  "description": "Main gondola shelf for aisle 5",
  "location_in_store": "Zone-1",
  "width_cm": 145.0,
  "created_at": "2026-02-18T10:26:26.463263+00:00",
  "updated_at": "2026-02-18T10:26:26.463264+00:00"
}
```

## 70. Create Planogram S3-P5
- Timestamp: `2026-02-18T10:26:26.466653+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "994e3a3f-daac-443d-8897-65c91c63e0e5",
  "name": "Irbid Weekly Planogram 05",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 5, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Cleaning",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Personal Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Canned Food",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "576cedc4-c1d9-4b6e-bd6b-23f4d025c8f9",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "994e3a3f-daac-443d-8897-65c91c63e0e5",
  "name": "Irbid Weekly Planogram 05",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 5, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Cleaning",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Personal Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Canned Food",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.465304+00:00",
  "updated_at": "2026-02-18T10:26:26.465305+00:00"
}
```

## 71. Create Shelf S3-P6
- Timestamp: `2026-02-18T10:26:26.468619+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 06",
  "description": "Main gondola shelf for aisle 6",
  "location_in_store": "Zone-2",
  "width_cm": 150
}
```
- Response:
```json
{
  "id": "b0609e8a-dcd4-49ff-b49a-67d8e85a7cd2",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 06",
  "description": "Main gondola shelf for aisle 6",
  "location_in_store": "Zone-2",
  "width_cm": 150.0,
  "created_at": "2026-02-18T10:26:26.467357+00:00",
  "updated_at": "2026-02-18T10:26:26.467358+00:00"
}
```

## 72. Create Planogram S3-P6
- Timestamp: `2026-02-18T10:26:26.470425+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "b0609e8a-dcd4-49ff-b49a-67d8e85a7cd2",
  "name": "Irbid Weekly Planogram 06",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 6, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Personal Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Canned Food",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Frozen",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "367eea6c-ad72-4526-b6de-dd307d869a5d",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "b0609e8a-dcd4-49ff-b49a-67d8e85a7cd2",
  "name": "Irbid Weekly Planogram 06",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 6, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Personal Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Canned Food",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Frozen",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.469180+00:00",
  "updated_at": "2026-02-18T10:26:26.469181+00:00"
}
```

## 73. Create Shelf S3-P7
- Timestamp: `2026-02-18T10:26:26.472243+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 07",
  "description": "Main gondola shelf for aisle 7",
  "location_in_store": "Zone-3",
  "width_cm": 155
}
```
- Response:
```json
{
  "id": "3bd8a0f0-770e-4c19-a491-b4a351d1f060",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 07",
  "description": "Main gondola shelf for aisle 7",
  "location_in_store": "Zone-3",
  "width_cm": 155.0,
  "created_at": "2026-02-18T10:26:26.470952+00:00",
  "updated_at": "2026-02-18T10:26:26.470953+00:00"
}
```

## 74. Create Planogram S3-P7
- Timestamp: `2026-02-18T10:26:26.474290+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "3bd8a0f0-770e-4c19-a491-b4a351d1f060",
  "name": "Irbid Weekly Planogram 07",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 7, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Canned Food",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Frozen",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Bakery",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "2054add1-6abb-463c-bed7-8bfc2c50971b",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "3bd8a0f0-770e-4c19-a491-b4a351d1f060",
  "name": "Irbid Weekly Planogram 07",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 7, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Canned Food",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Frozen",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Bakery",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.472752+00:00",
  "updated_at": "2026-02-18T10:26:26.472753+00:00"
}
```

## 75. Create Shelf S3-P8
- Timestamp: `2026-02-18T10:26:26.476336+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 08",
  "description": "Main gondola shelf for aisle 8",
  "location_in_store": "Zone-4",
  "width_cm": 160
}
```
- Response:
```json
{
  "id": "012d3e6a-df9e-42f6-bb54-8601e3e66aea",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 08",
  "description": "Main gondola shelf for aisle 8",
  "location_in_store": "Zone-4",
  "width_cm": 160.0,
  "created_at": "2026-02-18T10:26:26.474843+00:00",
  "updated_at": "2026-02-18T10:26:26.474844+00:00"
}
```

## 76. Create Planogram S3-P8
- Timestamp: `2026-02-18T10:26:26.478420+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "012d3e6a-df9e-42f6-bb54-8601e3e66aea",
  "name": "Irbid Weekly Planogram 08",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 8, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Frozen",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Bakery",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Pet Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "69a527ea-4c6b-466d-a731-791eb7a5de48",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "012d3e6a-df9e-42f6-bb54-8601e3e66aea",
  "name": "Irbid Weekly Planogram 08",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 8, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Frozen",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Bakery",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Pet Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.476870+00:00",
  "updated_at": "2026-02-18T10:26:26.476871+00:00"
}
```

## 77. Create Shelf S3-P9
- Timestamp: `2026-02-18T10:26:26.480502+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 09",
  "description": "Main gondola shelf for aisle 9",
  "location_in_store": "Zone-5",
  "width_cm": 165
}
```
- Response:
```json
{
  "id": "075e101a-20a8-43d7-a259-f991a084f8b4",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 09",
  "description": "Main gondola shelf for aisle 9",
  "location_in_store": "Zone-5",
  "width_cm": 165.0,
  "created_at": "2026-02-18T10:26:26.478947+00:00",
  "updated_at": "2026-02-18T10:26:26.478948+00:00"
}
```

## 78. Create Planogram S3-P9
- Timestamp: `2026-02-18T10:26:26.482298+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "075e101a-20a8-43d7-a259-f991a084f8b4",
  "name": "Irbid Weekly Planogram 09",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 9, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Bakery",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Pet Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Beverages",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "e441c77b-5843-4ea3-95cf-3e841f0a9399",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "075e101a-20a8-43d7-a259-f991a084f8b4",
  "name": "Irbid Weekly Planogram 09",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 9, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Bakery",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Pet Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Beverages",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.481035+00:00",
  "updated_at": "2026-02-18T10:26:26.481036+00:00"
}
```

## 79. Create Shelf S3-P10
- Timestamp: `2026-02-18T10:26:26.484069+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 10",
  "description": "Main gondola shelf for aisle 10",
  "location_in_store": "Zone-1",
  "width_cm": 170
}
```
- Response:
```json
{
  "id": "52651533-ca54-4a88-810e-83764f294a2c",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "name": "Irbid - Aisle 10",
  "description": "Main gondola shelf for aisle 10",
  "location_in_store": "Zone-1",
  "width_cm": 170.0,
  "created_at": "2026-02-18T10:26:26.482893+00:00",
  "updated_at": "2026-02-18T10:26:26.482895+00:00"
}
```

## 80. Create Planogram S3-P10
- Timestamp: `2026-02-18T10:26:26.485971+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "52651533-ca54-4a88-810e-83764f294a2c",
  "name": "Irbid Weekly Planogram 10",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 10, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Pet Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Beverages",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Dairy",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "63f6545d-9bea-455d-90d7-cc9c6b82e487",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
  "shelf_id": "52651533-ca54-4a88-810e-83764f294a2c",
  "name": "Irbid Weekly Planogram 10",
  "description": "Planogram for Cortanex Market - Irbid Center shelf 10, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Pet Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Beverages",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Dairy",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.484711+00:00",
  "updated_at": "2026-02-18T10:26:26.484712+00:00"
}
```

## 81. Create Store 4
- Timestamp: `2026-02-18T10:26:26.487813+00:00`
- Method: `POST`
- Path: `/rest/v1/stores`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Market - Zarqa Avenue",
  "address": "36th Zarqa Main Road",
  "city": "Zarqa",
  "country": "Jordan"
}
```
- Response:
```json
{
  "id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Market - Zarqa Avenue",
  "address": "36th Zarqa Main Road",
  "city": "Zarqa",
  "country": "Jordan",
  "created_at": "2026-02-18T10:26:26.486502+00:00",
  "updated_at": "2026-02-18T10:26:26.486503+00:00"
}
```

## 82. Assign Store 4 To User
- Timestamp: `2026-02-18T10:26:26.489880+00:00`
- Method: `POST`
- Path: `/rest/v1/user_store_access`
- Status: `201`
- Request payload:
```json
{
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2"
}
```
- Response:
```json
{
  "id": "66584d34-d86e-4769-8f48-8067d054be75",
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "created_at": "2026-02-18T10:26:26.488373+00:00"
}
```

## 83. Create Shelf S4-P1
- Timestamp: `2026-02-18T10:26:26.492092+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 01",
  "description": "Main gondola shelf for aisle 1",
  "location_in_store": "Zone-2",
  "width_cm": 125
}
```
- Response:
```json
{
  "id": "e31dad17-1b26-4fdc-bce5-e84704577899",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 01",
  "description": "Main gondola shelf for aisle 1",
  "location_in_store": "Zone-2",
  "width_cm": 125.0,
  "created_at": "2026-02-18T10:26:26.490398+00:00",
  "updated_at": "2026-02-18T10:26:26.490399+00:00"
}
```

## 84. Create Planogram S4-P1
- Timestamp: `2026-02-18T10:26:26.494237+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "e31dad17-1b26-4fdc-bce5-e84704577899",
  "name": "Zarqa Weekly Planogram 01",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 1, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Beverages",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Dairy",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Snacks",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "6de87742-0103-4062-9b9f-32115cec4486",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "e31dad17-1b26-4fdc-bce5-e84704577899",
  "name": "Zarqa Weekly Planogram 01",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 1, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Beverages",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Dairy",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Snacks",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.492669+00:00",
  "updated_at": "2026-02-18T10:26:26.492670+00:00"
}
```

## 85. Create Shelf S4-P2
- Timestamp: `2026-02-18T10:26:26.496269+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 02",
  "description": "Main gondola shelf for aisle 2",
  "location_in_store": "Zone-3",
  "width_cm": 130
}
```
- Response:
```json
{
  "id": "93a6f2ce-ae7a-46bd-9426-711547e5328f",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 02",
  "description": "Main gondola shelf for aisle 2",
  "location_in_store": "Zone-3",
  "width_cm": 130.0,
  "created_at": "2026-02-18T10:26:26.494771+00:00",
  "updated_at": "2026-02-18T10:26:26.494772+00:00"
}
```

## 86. Create Planogram S4-P2
- Timestamp: `2026-02-18T10:26:26.498105+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "93a6f2ce-ae7a-46bd-9426-711547e5328f",
  "name": "Zarqa Weekly Planogram 02",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 2, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Dairy",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Snacks",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Breakfast",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "e4471aeb-7c31-43a6-aa9c-b0cf2bd7d62c",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "93a6f2ce-ae7a-46bd-9426-711547e5328f",
  "name": "Zarqa Weekly Planogram 02",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 2, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Dairy",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Snacks",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Breakfast",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.496824+00:00",
  "updated_at": "2026-02-18T10:26:26.496825+00:00"
}
```

## 87. Create Shelf S4-P3
- Timestamp: `2026-02-18T10:26:26.499974+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 03",
  "description": "Main gondola shelf for aisle 3",
  "location_in_store": "Zone-4",
  "width_cm": 135
}
```
- Response:
```json
{
  "id": "766a4f6c-10a0-4c56-a724-0f65641448f4",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 03",
  "description": "Main gondola shelf for aisle 3",
  "location_in_store": "Zone-4",
  "width_cm": 135.0,
  "created_at": "2026-02-18T10:26:26.498730+00:00",
  "updated_at": "2026-02-18T10:26:26.498732+00:00"
}
```

## 88. Create Planogram S4-P3
- Timestamp: `2026-02-18T10:26:26.501828+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "766a4f6c-10a0-4c56-a724-0f65641448f4",
  "name": "Zarqa Weekly Planogram 03",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 3, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Snacks",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Breakfast",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Cleaning",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "3ac44c5a-affc-40ca-bd08-edf5b75f3db4",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "766a4f6c-10a0-4c56-a724-0f65641448f4",
  "name": "Zarqa Weekly Planogram 03",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 3, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Snacks",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Breakfast",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Cleaning",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.500562+00:00",
  "updated_at": "2026-02-18T10:26:26.500563+00:00"
}
```

## 89. Create Shelf S4-P4
- Timestamp: `2026-02-18T10:26:26.503566+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 04",
  "description": "Main gondola shelf for aisle 4",
  "location_in_store": "Zone-5",
  "width_cm": 140
}
```
- Response:
```json
{
  "id": "5d33755b-eb94-4e8b-870e-bae6cf76f40a",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 04",
  "description": "Main gondola shelf for aisle 4",
  "location_in_store": "Zone-5",
  "width_cm": 140.0,
  "created_at": "2026-02-18T10:26:26.502373+00:00",
  "updated_at": "2026-02-18T10:26:26.502375+00:00"
}
```

## 90. Create Planogram S4-P4
- Timestamp: `2026-02-18T10:26:26.505594+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "5d33755b-eb94-4e8b-870e-bae6cf76f40a",
  "name": "Zarqa Weekly Planogram 04",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 4, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Breakfast",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Cleaning",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Personal Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "cece8b53-a996-4e6c-af6a-e57be18625d0",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "5d33755b-eb94-4e8b-870e-bae6cf76f40a",
  "name": "Zarqa Weekly Planogram 04",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 4, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Breakfast",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Cleaning",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Personal Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.504077+00:00",
  "updated_at": "2026-02-18T10:26:26.504078+00:00"
}
```

## 91. Create Shelf S4-P5
- Timestamp: `2026-02-18T10:26:26.507621+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 05",
  "description": "Main gondola shelf for aisle 5",
  "location_in_store": "Zone-1",
  "width_cm": 145
}
```
- Response:
```json
{
  "id": "64c34bcb-9935-4b06-9a0c-4866f7afe21e",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 05",
  "description": "Main gondola shelf for aisle 5",
  "location_in_store": "Zone-1",
  "width_cm": 145.0,
  "created_at": "2026-02-18T10:26:26.506118+00:00",
  "updated_at": "2026-02-18T10:26:26.506119+00:00"
}
```

## 92. Create Planogram S4-P5
- Timestamp: `2026-02-18T10:26:26.510541+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "64c34bcb-9935-4b06-9a0c-4866f7afe21e",
  "name": "Zarqa Weekly Planogram 05",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 5, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Cleaning",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Personal Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Canned Food",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "e48e8960-d32a-4d59-94b8-fc00a5b3c054",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "64c34bcb-9935-4b06-9a0c-4866f7afe21e",
  "name": "Zarqa Weekly Planogram 05",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 5, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Cleaning",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Personal Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Canned Food",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.508144+00:00",
  "updated_at": "2026-02-18T10:26:26.508145+00:00"
}
```

## 93. Create Shelf S4-P6
- Timestamp: `2026-02-18T10:26:26.514128+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 06",
  "description": "Main gondola shelf for aisle 6",
  "location_in_store": "Zone-2",
  "width_cm": 150
}
```
- Response:
```json
{
  "id": "f6bf952e-65fa-40c9-aada-2b07935d9d80",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 06",
  "description": "Main gondola shelf for aisle 6",
  "location_in_store": "Zone-2",
  "width_cm": 150.0,
  "created_at": "2026-02-18T10:26:26.511581+00:00",
  "updated_at": "2026-02-18T10:26:26.511584+00:00"
}
```

## 94. Create Planogram S4-P6
- Timestamp: `2026-02-18T10:26:26.517264+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "f6bf952e-65fa-40c9-aada-2b07935d9d80",
  "name": "Zarqa Weekly Planogram 06",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 6, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Personal Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Canned Food",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Frozen",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "3ee84eac-919a-4c13-a15b-25759fd5c5b2",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "f6bf952e-65fa-40c9-aada-2b07935d9d80",
  "name": "Zarqa Weekly Planogram 06",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 6, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Personal Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Canned Food",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Frozen",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.514899+00:00",
  "updated_at": "2026-02-18T10:26:26.514902+00:00"
}
```

## 95. Create Shelf S4-P7
- Timestamp: `2026-02-18T10:26:26.519852+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 07",
  "description": "Main gondola shelf for aisle 7",
  "location_in_store": "Zone-3",
  "width_cm": 155
}
```
- Response:
```json
{
  "id": "9fdcf997-9ae0-49f1-83d8-4853a02db060",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 07",
  "description": "Main gondola shelf for aisle 7",
  "location_in_store": "Zone-3",
  "width_cm": 155.0,
  "created_at": "2026-02-18T10:26:26.518094+00:00",
  "updated_at": "2026-02-18T10:26:26.518098+00:00"
}
```

## 96. Create Planogram S4-P7
- Timestamp: `2026-02-18T10:26:26.522052+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "9fdcf997-9ae0-49f1-83d8-4853a02db060",
  "name": "Zarqa Weekly Planogram 07",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 7, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Canned Food",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Frozen",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Bakery",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "45ca046f-23cf-4ad4-86e8-54ba865673b8",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "9fdcf997-9ae0-49f1-83d8-4853a02db060",
  "name": "Zarqa Weekly Planogram 07",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 7, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Canned Food",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Frozen",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Bakery",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.520561+00:00",
  "updated_at": "2026-02-18T10:26:26.520563+00:00"
}
```

## 97. Create Shelf S4-P8
- Timestamp: `2026-02-18T10:26:26.523884+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 08",
  "description": "Main gondola shelf for aisle 8",
  "location_in_store": "Zone-4",
  "width_cm": 160
}
```
- Response:
```json
{
  "id": "796b633b-c512-4d2c-b9e2-ce6cb2e1bdcf",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 08",
  "description": "Main gondola shelf for aisle 8",
  "location_in_store": "Zone-4",
  "width_cm": 160.0,
  "created_at": "2026-02-18T10:26:26.522657+00:00",
  "updated_at": "2026-02-18T10:26:26.522658+00:00"
}
```

## 98. Create Planogram S4-P8
- Timestamp: `2026-02-18T10:26:26.525957+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "796b633b-c512-4d2c-b9e2-ce6cb2e1bdcf",
  "name": "Zarqa Weekly Planogram 08",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 8, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Frozen",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Bakery",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Pet Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "159563ea-8501-4a20-8bee-95e8c46dd4b2",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "796b633b-c512-4d2c-b9e2-ce6cb2e1bdcf",
  "name": "Zarqa Weekly Planogram 08",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 8, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Frozen",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Bakery",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Pet Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.524442+00:00",
  "updated_at": "2026-02-18T10:26:26.524444+00:00"
}
```

## 99. Create Shelf S4-P9
- Timestamp: `2026-02-18T10:26:26.528108+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 09",
  "description": "Main gondola shelf for aisle 9",
  "location_in_store": "Zone-5",
  "width_cm": 165
}
```
- Response:
```json
{
  "id": "2e0f413f-db09-44c5-b5ed-0b831fbea43f",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 09",
  "description": "Main gondola shelf for aisle 9",
  "location_in_store": "Zone-5",
  "width_cm": 165.0,
  "created_at": "2026-02-18T10:26:26.526479+00:00",
  "updated_at": "2026-02-18T10:26:26.526481+00:00"
}
```

## 100. Create Planogram S4-P9
- Timestamp: `2026-02-18T10:26:26.531223+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "2e0f413f-db09-44c5-b5ed-0b831fbea43f",
  "name": "Zarqa Weekly Planogram 09",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 9, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Bakery",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Pet Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Beverages",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "9ed5d2ba-9b25-46f3-88b0-c49b1221a66b",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "2e0f413f-db09-44c5-b5ed-0b831fbea43f",
  "name": "Zarqa Weekly Planogram 09",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 9, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Bakery",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Pet Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Beverages",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.528989+00:00",
  "updated_at": "2026-02-18T10:26:26.528992+00:00"
}
```

## 101. Create Shelf S4-P10
- Timestamp: `2026-02-18T10:26:26.534042+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 10",
  "description": "Main gondola shelf for aisle 10",
  "location_in_store": "Zone-1",
  "width_cm": 170
}
```
- Response:
```json
{
  "id": "7df2c017-ca23-4d97-973c-75f834e86f2e",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "name": "Zarqa - Aisle 10",
  "description": "Main gondola shelf for aisle 10",
  "location_in_store": "Zone-1",
  "width_cm": 170.0,
  "created_at": "2026-02-18T10:26:26.531924+00:00",
  "updated_at": "2026-02-18T10:26:26.531926+00:00"
}
```

## 102. Create Planogram S4-P10
- Timestamp: `2026-02-18T10:26:26.537423+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "7df2c017-ca23-4d97-973c-75f834e86f2e",
  "name": "Zarqa Weekly Planogram 10",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 10, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Pet Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Beverages",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Dairy",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "8d9ac471-f7dc-4cdb-a10a-83e2dffba15a",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
  "shelf_id": "7df2c017-ca23-4d97-973c-75f834e86f2e",
  "name": "Zarqa Weekly Planogram 10",
  "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 10, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Pet Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Beverages",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Dairy",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.535133+00:00",
  "updated_at": "2026-02-18T10:26:26.535135+00:00"
}
```

## 103. Create Store 5
- Timestamp: `2026-02-18T10:26:26.540039+00:00`
- Method: `POST`
- Path: `/rest/v1/stores`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Express - Aqaba Marina",
  "address": "Marina Promenade, Unit 9",
  "city": "Aqaba",
  "country": "Jordan"
}
```
- Response:
```json
{
  "id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "name": "Cortanex Express - Aqaba Marina",
  "address": "Marina Promenade, Unit 9",
  "city": "Aqaba",
  "country": "Jordan",
  "created_at": "2026-02-18T10:26:26.538394+00:00",
  "updated_at": "2026-02-18T10:26:26.538397+00:00"
}
```

## 104. Assign Store 5 To User
- Timestamp: `2026-02-18T10:26:26.542296+00:00`
- Method: `POST`
- Path: `/rest/v1/user_store_access`
- Status: `201`
- Request payload:
```json
{
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009"
}
```
- Response:
```json
{
  "id": "99b22318-9e9c-403c-98b5-fd8009e88b1d",
  "user_id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "created_at": "2026-02-18T10:26:26.540863+00:00"
}
```

## 105. Create Shelf S5-P1
- Timestamp: `2026-02-18T10:26:26.544484+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 01",
  "description": "Main gondola shelf for aisle 1",
  "location_in_store": "Zone-2",
  "width_cm": 125
}
```
- Response:
```json
{
  "id": "e565bdaf-85ee-4e49-bdf7-f753bf93b06e",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 01",
  "description": "Main gondola shelf for aisle 1",
  "location_in_store": "Zone-2",
  "width_cm": 125.0,
  "created_at": "2026-02-18T10:26:26.543073+00:00",
  "updated_at": "2026-02-18T10:26:26.543074+00:00"
}
```

## 106. Create Planogram S5-P1
- Timestamp: `2026-02-18T10:26:26.547091+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "e565bdaf-85ee-4e49-bdf7-f753bf93b06e",
  "name": "Aqaba Weekly Planogram 01",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 1, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Beverages",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Dairy",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Snacks",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "1ee621fa-39ac-439f-9c23-952915308ae5",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "e565bdaf-85ee-4e49-bdf7-f753bf93b06e",
  "name": "Aqaba Weekly Planogram 01",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 1, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Beverages",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Dairy",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Snacks",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.545274+00:00",
  "updated_at": "2026-02-18T10:26:26.545275+00:00"
}
```

## 107. Create Shelf S5-P2
- Timestamp: `2026-02-18T10:26:26.549431+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 02",
  "description": "Main gondola shelf for aisle 2",
  "location_in_store": "Zone-3",
  "width_cm": 130
}
```
- Response:
```json
{
  "id": "e74bdeee-68b0-4f07-92a8-7616fc4cd066",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 02",
  "description": "Main gondola shelf for aisle 2",
  "location_in_store": "Zone-3",
  "width_cm": 130.0,
  "created_at": "2026-02-18T10:26:26.547866+00:00",
  "updated_at": "2026-02-18T10:26:26.547867+00:00"
}
```

## 108. Create Planogram S5-P2
- Timestamp: `2026-02-18T10:26:26.552134+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "e74bdeee-68b0-4f07-92a8-7616fc4cd066",
  "name": "Aqaba Weekly Planogram 02",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 2, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Dairy",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Snacks",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Breakfast",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "0d863601-f6d7-4332-a26f-80faddf4afd3",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "e74bdeee-68b0-4f07-92a8-7616fc4cd066",
  "name": "Aqaba Weekly Planogram 02",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 2, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Dairy",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Snacks",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Breakfast",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.550223+00:00",
  "updated_at": "2026-02-18T10:26:26.550224+00:00"
}
```

## 109. Create Shelf S5-P3
- Timestamp: `2026-02-18T10:26:26.554727+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 03",
  "description": "Main gondola shelf for aisle 3",
  "location_in_store": "Zone-4",
  "width_cm": 135
}
```
- Response:
```json
{
  "id": "a93baa02-4dbd-46c4-b642-cd658a968df5",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 03",
  "description": "Main gondola shelf for aisle 3",
  "location_in_store": "Zone-4",
  "width_cm": 135.0,
  "created_at": "2026-02-18T10:26:26.552982+00:00",
  "updated_at": "2026-02-18T10:26:26.552983+00:00"
}
```

## 110. Create Planogram S5-P3
- Timestamp: `2026-02-18T10:26:26.556957+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "a93baa02-4dbd-46c4-b642-cd658a968df5",
  "name": "Aqaba Weekly Planogram 03",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 3, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Snacks",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Breakfast",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Cleaning",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "e0513da3-85d5-4b7c-93f5-f1ef14b68464",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "a93baa02-4dbd-46c4-b642-cd658a968df5",
  "name": "Aqaba Weekly Planogram 03",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 3, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Snacks",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Breakfast",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Cleaning",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.555531+00:00",
  "updated_at": "2026-02-18T10:26:26.555532+00:00"
}
```

## 111. Create Shelf S5-P4
- Timestamp: `2026-02-18T10:26:26.559133+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 04",
  "description": "Main gondola shelf for aisle 4",
  "location_in_store": "Zone-5",
  "width_cm": 140
}
```
- Response:
```json
{
  "id": "bf6fa702-c0f5-4ea7-8f46-ed1b1327747c",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 04",
  "description": "Main gondola shelf for aisle 4",
  "location_in_store": "Zone-5",
  "width_cm": 140.0,
  "created_at": "2026-02-18T10:26:26.557694+00:00",
  "updated_at": "2026-02-18T10:26:26.557695+00:00"
}
```

## 112. Create Planogram S5-P4
- Timestamp: `2026-02-18T10:26:26.561264+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "bf6fa702-c0f5-4ea7-8f46-ed1b1327747c",
  "name": "Aqaba Weekly Planogram 04",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 4, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Breakfast",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Cleaning",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Personal Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "9bb2e133-ffff-40fb-bd64-33d49bf9290d",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "bf6fa702-c0f5-4ea7-8f46-ed1b1327747c",
  "name": "Aqaba Weekly Planogram 04",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 4, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Breakfast",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Cleaning",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Personal Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.559919+00:00",
  "updated_at": "2026-02-18T10:26:26.559921+00:00"
}
```

## 113. Create Shelf S5-P5
- Timestamp: `2026-02-18T10:26:26.563353+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 05",
  "description": "Main gondola shelf for aisle 5",
  "location_in_store": "Zone-1",
  "width_cm": 145
}
```
- Response:
```json
{
  "id": "c4d60a91-f752-42c7-9baf-dff09954a349",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 05",
  "description": "Main gondola shelf for aisle 5",
  "location_in_store": "Zone-1",
  "width_cm": 145.0,
  "created_at": "2026-02-18T10:26:26.562102+00:00",
  "updated_at": "2026-02-18T10:26:26.562103+00:00"
}
```

## 114. Create Planogram S5-P5
- Timestamp: `2026-02-18T10:26:26.565897+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "c4d60a91-f752-42c7-9baf-dff09954a349",
  "name": "Aqaba Weekly Planogram 05",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 5, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Cleaning",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Personal Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Canned Food",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "05b6da97-58f2-4f28-9654-f3b53ec2aed4",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "c4d60a91-f752-42c7-9baf-dff09954a349",
  "name": "Aqaba Weekly Planogram 05",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 5, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Cleaning",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Personal Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Canned Food",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.564099+00:00",
  "updated_at": "2026-02-18T10:26:26.564100+00:00"
}
```

## 115. Create Shelf S5-P6
- Timestamp: `2026-02-18T10:26:26.568282+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 06",
  "description": "Main gondola shelf for aisle 6",
  "location_in_store": "Zone-2",
  "width_cm": 150
}
```
- Response:
```json
{
  "id": "4ddd5de9-374d-4be8-aba6-430a9aac60fa",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 06",
  "description": "Main gondola shelf for aisle 6",
  "location_in_store": "Zone-2",
  "width_cm": 150.0,
  "created_at": "2026-02-18T10:26:26.566694+00:00",
  "updated_at": "2026-02-18T10:26:26.566695+00:00"
}
```

## 116. Create Planogram S5-P6
- Timestamp: `2026-02-18T10:26:26.571300+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "4ddd5de9-374d-4be8-aba6-430a9aac60fa",
  "name": "Aqaba Weekly Planogram 06",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 6, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Personal Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Canned Food",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Frozen",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "b3d98adf-d815-496b-bdda-9140aa1de2c8",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "4ddd5de9-374d-4be8-aba6-430a9aac60fa",
  "name": "Aqaba Weekly Planogram 06",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 6, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Personal Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Canned Food",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Frozen",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.569188+00:00",
  "updated_at": "2026-02-18T10:26:26.569189+00:00"
}
```

## 117. Create Shelf S5-P7
- Timestamp: `2026-02-18T10:26:26.574573+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 07",
  "description": "Main gondola shelf for aisle 7",
  "location_in_store": "Zone-3",
  "width_cm": 155
}
```
- Response:
```json
{
  "id": "e7b77017-9af9-4c22-bcf5-d8c52fd0d480",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 07",
  "description": "Main gondola shelf for aisle 7",
  "location_in_store": "Zone-3",
  "width_cm": 155.0,
  "created_at": "2026-02-18T10:26:26.572369+00:00",
  "updated_at": "2026-02-18T10:26:26.572371+00:00"
}
```

## 118. Create Planogram S5-P7
- Timestamp: `2026-02-18T10:26:26.577078+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "e7b77017-9af9-4c22-bcf5-d8c52fd0d480",
  "name": "Aqaba Weekly Planogram 07",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 7, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Canned Food",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Frozen",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Bakery",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "fc05b717-e9bf-458b-b3dd-d5bcd6493a9a",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "e7b77017-9af9-4c22-bcf5-d8c52fd0d480",
  "name": "Aqaba Weekly Planogram 07",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 7, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Canned Food",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Frozen",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Bakery",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.575331+00:00",
  "updated_at": "2026-02-18T10:26:26.575332+00:00"
}
```

## 119. Create Shelf S5-P8
- Timestamp: `2026-02-18T10:26:26.579532+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 08",
  "description": "Main gondola shelf for aisle 8",
  "location_in_store": "Zone-4",
  "width_cm": 160
}
```
- Response:
```json
{
  "id": "a8b07eea-a7ec-40c4-bc48-40c37a8fafee",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 08",
  "description": "Main gondola shelf for aisle 8",
  "location_in_store": "Zone-4",
  "width_cm": 160.0,
  "created_at": "2026-02-18T10:26:26.577802+00:00",
  "updated_at": "2026-02-18T10:26:26.577804+00:00"
}
```

## 120. Create Planogram S5-P8
- Timestamp: `2026-02-18T10:26:26.581902+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "a8b07eea-a7ec-40c4-bc48-40c37a8fafee",
  "name": "Aqaba Weekly Planogram 08",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 8, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Frozen",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Bakery",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Pet Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "efc90b0e-b3ca-46bf-81e3-9a8880098868",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "a8b07eea-a7ec-40c4-bc48-40c37a8fafee",
  "name": "Aqaba Weekly Planogram 08",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 8, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Frozen",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Bakery",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Pet Care",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.580208+00:00",
  "updated_at": "2026-02-18T10:26:26.580210+00:00"
}
```

## 121. Create Shelf S5-P9
- Timestamp: `2026-02-18T10:26:26.584242+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 09",
  "description": "Main gondola shelf for aisle 9",
  "location_in_store": "Zone-5",
  "width_cm": 165
}
```
- Response:
```json
{
  "id": "18c2bf42-5535-4c45-b601-3033022fff08",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 09",
  "description": "Main gondola shelf for aisle 9",
  "location_in_store": "Zone-5",
  "width_cm": 165.0,
  "created_at": "2026-02-18T10:26:26.582560+00:00",
  "updated_at": "2026-02-18T10:26:26.582562+00:00"
}
```

## 122. Create Planogram S5-P9
- Timestamp: `2026-02-18T10:26:26.586906+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "18c2bf42-5535-4c45-b601-3033022fff08",
  "name": "Aqaba Weekly Planogram 09",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 9, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Bakery",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Pet Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Beverages",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "473004dd-072d-4e7a-81ad-f42b0ad4eea5",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "18c2bf42-5535-4c45-b601-3033022fff08",
  "name": "Aqaba Weekly Planogram 09",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 9, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Bakery",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Pet Care",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Beverages",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.585016+00:00",
  "updated_at": "2026-02-18T10:26:26.585018+00:00"
}
```

## 123. Create Shelf S5-P10
- Timestamp: `2026-02-18T10:26:26.589374+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 10",
  "description": "Main gondola shelf for aisle 10",
  "location_in_store": "Zone-1",
  "width_cm": 170
}
```
- Response:
```json
{
  "id": "10157a4a-37fe-4957-b22c-d7e9eb8219e8",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "name": "Aqaba - Aisle 10",
  "description": "Main gondola shelf for aisle 10",
  "location_in_store": "Zone-1",
  "width_cm": 170.0,
  "created_at": "2026-02-18T10:26:26.587504+00:00",
  "updated_at": "2026-02-18T10:26:26.587506+00:00"
}
```

## 124. Create Planogram S5-P10
- Timestamp: `2026-02-18T10:26:26.591798+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request payload:
```json
{
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "10157a4a-37fe-4957-b22c-d7e9eb8219e8",
  "name": "Aqaba Weekly Planogram 10",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 10, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Pet Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Beverages",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Dairy",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364"
}
```
- Response:
```json
{
  "id": "f2d6624b-6bd6-4209-8de3-51f710a18ee4",
  "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
  "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
  "shelf_id": "10157a4a-37fe-4957-b22c-d7e9eb8219e8",
  "name": "Aqaba Weekly Planogram 10",
  "description": "Planogram for Cortanex Express - Aqaba Marina shelf 10, weekly rotation",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "category": "Pet Care",
      "expected_facings": 4,
      "priority": "high"
    },
    {
      "slot": 2,
      "category": "Beverages",
      "expected_facings": 3,
      "priority": "medium"
    },
    {
      "slot": 3,
      "category": "Dairy",
      "expected_facings": 2,
      "priority": "medium"
    }
  ],
  "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
  "created_at": "2026-02-18T10:26:26.590904+00:00",
  "updated_at": "2026-02-18T10:26:26.590906+00:00"
}
```

## 125. Login Via Email
- Timestamp: `2026-02-18T10:26:26.604672+00:00`
- Method: `POST`
- Path: `/auth/v1/login`
- Status: `200`
- Request payload:
```json
{
  "identifier": "a.salameh@cortanexai.com",
  "password": "123456"
}
```
- Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlMjZmMzY4ZC1jOWEzLTRhY2MtYTlmZi0wYTQwMmFiNzczNjQiLCJleHAiOjE3NzE0OTY3ODZ9.0f937YZRQl9Wj0CtfKGzcntw-ZnI1sTfR8eFbnuIPAM",
  "refresh_token": "f95285a7-8793-4a9e-9296-ab965a4c0c49",
  "expires_in": 86400,
  "token_type": "bearer",
  "user": {
    "id": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
    "email": "a.salameh@cortanexai.com",
    "username": "a.salameh"
  },
  "stores": [
    {
      "id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "name": "Cortanex Hypermarket - Amman West",
      "address": "Wasfi Al Tal Street, Building 221",
      "city": "Amman",
      "country": "Jordan",
      "created_at": "2026-02-18T10:26:26.341126+00:00",
      "updated_at": "2026-02-18T10:26:26.341127+00:00"
    },
    {
      "id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "name": "Cortanex Hypermarket - Amman Downtown",
      "address": "King Hussein Street, Block 14",
      "city": "Amman",
      "country": "Jordan",
      "created_at": "2026-02-18T10:26:26.392564+00:00",
      "updated_at": "2026-02-18T10:26:26.392566+00:00"
    },
    {
      "id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "name": "Cortanex Market - Irbid Center",
      "address": "University Street, Gate 3",
      "city": "Irbid",
      "country": "Jordan",
      "created_at": "2026-02-18T10:26:26.442011+00:00",
      "updated_at": "2026-02-18T10:26:26.442012+00:00"
    },
    {
      "id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "name": "Cortanex Market - Zarqa Avenue",
      "address": "36th Zarqa Main Road",
      "city": "Zarqa",
      "country": "Jordan",
      "created_at": "2026-02-18T10:26:26.486502+00:00",
      "updated_at": "2026-02-18T10:26:26.486503+00:00"
    },
    {
      "id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "name": "Cortanex Express - Aqaba Marina",
      "address": "Marina Promenade, Unit 9",
      "city": "Aqaba",
      "country": "Jordan",
      "created_at": "2026-02-18T10:26:26.538394+00:00",
      "updated_at": "2026-02-18T10:26:26.538397+00:00"
    }
  ],
  "planograms": [
    {
      "id": "9f878ae7-56c3-431d-a569-7aea61898783",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "shelf_id": "64a6d85b-0e4c-46c6-ba86-45fbb2e3b35f",
      "name": "Amman Weekly Planogram 08",
      "description": "Planogram for Cortanex Hypermarket - Amman West shelf 8, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Frozen",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Bakery",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Pet Care",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.382420+00:00",
      "updated_at": "2026-02-18T10:26:26.382421+00:00"
    },
    {
      "id": "ec99684a-fb14-48e5-9be1-65f81758c375",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "shelf_id": "49b2c14f-52ea-4f44-977c-f21ae530f135",
      "name": "Amman Weekly Planogram 01",
      "description": "Planogram for Cortanex Hypermarket - Amman West shelf 1, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Beverages",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Dairy",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Snacks",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.352135+00:00",
      "updated_at": "2026-02-18T10:26:26.352138+00:00"
    },
    {
      "id": "686b166e-8a0f-4cb1-a873-70a1a34fa3eb",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "shelf_id": "4db4f75c-a725-4e92-9484-dcc786022224",
      "name": "Amman Weekly Planogram 02",
      "description": "Planogram for Cortanex Hypermarket - Amman West shelf 2, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Dairy",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Snacks",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Breakfast",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.357229+00:00",
      "updated_at": "2026-02-18T10:26:26.357230+00:00"
    },
    {
      "id": "6404c8ab-68cc-4879-9c19-8966feb927c7",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "shelf_id": "cb28b3cf-9e96-4de6-926b-a64d924da37b",
      "name": "Amman Weekly Planogram 03",
      "description": "Planogram for Cortanex Hypermarket - Amman West shelf 3, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Snacks",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Breakfast",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Cleaning",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.362722+00:00",
      "updated_at": "2026-02-18T10:26:26.362724+00:00"
    },
    {
      "id": "b16bcf6c-ea01-4c5b-ac98-bb0ba1e146d7",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "shelf_id": "13ebaccb-1de8-48ec-b4ec-3f2cff01012f",
      "name": "Amman Weekly Planogram 04",
      "description": "Planogram for Cortanex Hypermarket - Amman West shelf 4, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Breakfast",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Cleaning",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Personal Care",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.366978+00:00",
      "updated_at": "2026-02-18T10:26:26.366980+00:00"
    },
    {
      "id": "ac97683f-e6eb-4c0e-9bac-a895dbd3a8b8",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "shelf_id": "08fda374-978a-4868-9812-c68de5f5cdaf",
      "name": "Amman Weekly Planogram 05",
      "description": "Planogram for Cortanex Hypermarket - Amman West shelf 5, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Cleaning",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Personal Care",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Canned Food",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.370704+00:00",
      "updated_at": "2026-02-18T10:26:26.370705+00:00"
    },
    {
      "id": "ac7e7dbe-51a4-45e2-b12d-a017a60d21c0",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "shelf_id": "bb07434a-f72a-42f7-9f38-08c4c5d4c381",
      "name": "Amman Weekly Planogram 06",
      "description": "Planogram for Cortanex Hypermarket - Amman West shelf 6, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Personal Care",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Canned Food",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Frozen",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.374389+00:00",
      "updated_at": "2026-02-18T10:26:26.374391+00:00"
    },
    {
      "id": "215e150d-6639-4102-83a9-76d3d2d5f9e7",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "shelf_id": "b9748be7-65b1-4f96-b67f-a152341cedc7",
      "name": "Amman Weekly Planogram 07",
      "description": "Planogram for Cortanex Hypermarket - Amman West shelf 7, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Canned Food",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Frozen",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Bakery",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.378508+00:00",
      "updated_at": "2026-02-18T10:26:26.378509+00:00"
    },
    {
      "id": "f0e73a0d-a7be-40ca-b863-fc7fece862ba",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "shelf_id": "eb28dad9-67e3-495c-abbf-bcc8a6f80680",
      "name": "Amman Weekly Planogram 09",
      "description": "Planogram for Cortanex Hypermarket - Amman West shelf 9, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Bakery",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Pet Care",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Beverages",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.385807+00:00",
      "updated_at": "2026-02-18T10:26:26.385809+00:00"
    },
    {
      "id": "4e886854-e96e-484e-a27b-a0ad319c6790",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "ebfed5ef-d277-4173-9ee0-19a2ca254c65",
      "shelf_id": "e7db90eb-7dd4-48b6-911e-9d6cd3da9862",
      "name": "Amman Weekly Planogram 10",
      "description": "Planogram for Cortanex Hypermarket - Amman West shelf 10, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Pet Care",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Beverages",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Dairy",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.390170+00:00",
      "updated_at": "2026-02-18T10:26:26.390171+00:00"
    },
    {
      "id": "7e510172-55ad-43c5-814f-e8d7af1023da",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "shelf_id": "a1878a9f-06c7-45b1-8b5e-af356a03112c",
      "name": "Amman Weekly Planogram 01",
      "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 1, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Beverages",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Dairy",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Snacks",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.398968+00:00",
      "updated_at": "2026-02-18T10:26:26.398969+00:00"
    },
    {
      "id": "f70b90d5-bb65-4150-92c6-487c5be53cd2",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "shelf_id": "223bf5ed-c2aa-4c96-a302-d199b15844d0",
      "name": "Amman Weekly Planogram 02",
      "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 2, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Dairy",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Snacks",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Breakfast",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.403831+00:00",
      "updated_at": "2026-02-18T10:26:26.403832+00:00"
    },
    {
      "id": "1160013a-3327-452b-8834-3aa834169241",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "shelf_id": "b44b077c-6d1c-451f-8857-ab838b41bc15",
      "name": "Amman Weekly Planogram 03",
      "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 3, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Snacks",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Breakfast",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Cleaning",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.408294+00:00",
      "updated_at": "2026-02-18T10:26:26.408295+00:00"
    },
    {
      "id": "964612b5-e787-44f2-a4bf-3e9aef3c429a",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "shelf_id": "2a043367-4b48-45e0-84dd-901782f3d668",
      "name": "Amman Weekly Planogram 04",
      "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 4, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Breakfast",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Cleaning",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Personal Care",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.412504+00:00",
      "updated_at": "2026-02-18T10:26:26.412505+00:00"
    },
    {
      "id": "80703e68-fd0e-4492-9e3a-d0ff68d8e89a",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "shelf_id": "17d14d4c-ac70-461f-b46d-11eeead71d17",
      "name": "Amman Weekly Planogram 05",
      "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 5, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Cleaning",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Personal Care",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Canned Food",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.417217+00:00",
      "updated_at": "2026-02-18T10:26:26.417218+00:00"
    },
    {
      "id": "c81d05bc-881b-4ba5-9b92-71e1ae4b1bc2",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "shelf_id": "0d35ef88-b002-432c-9b8c-fcdf0deb0d56",
      "name": "Amman Weekly Planogram 06",
      "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 6, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Personal Care",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Canned Food",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Frozen",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.422617+00:00",
      "updated_at": "2026-02-18T10:26:26.422619+00:00"
    },
    {
      "id": "22ce6282-c478-4586-b8c1-8388da4d0eed",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "shelf_id": "306172ce-147f-47cb-9466-ae604c39ef62",
      "name": "Amman Weekly Planogram 07",
      "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 7, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Canned Food",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Frozen",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Bakery",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.428215+00:00",
      "updated_at": "2026-02-18T10:26:26.428217+00:00"
    },
    {
      "id": "b137bd24-c683-43c4-9871-306bbad5c4a8",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "shelf_id": "e06bcbed-61c0-4b86-b64f-d27250861781",
      "name": "Amman Weekly Planogram 08",
      "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 8, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Frozen",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Bakery",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Pet Care",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.432852+00:00",
      "updated_at": "2026-02-18T10:26:26.432854+00:00"
    },
    {
      "id": "3b407f2a-ca4d-4748-a94a-cae3f240c4c9",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "shelf_id": "0eac5eb7-aab4-471c-bc56-f2fa30304a8c",
      "name": "Amman Weekly Planogram 09",
      "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 9, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Bakery",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Pet Care",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Beverages",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.436440+00:00",
      "updated_at": "2026-02-18T10:26:26.436441+00:00"
    },
    {
      "id": "2c8fd361-15de-48f3-b62b-ee7615335776",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "3f117943-7701-4f5a-b48d-df62d34ff58c",
      "shelf_id": "e4ba9019-2a9f-473c-a586-15e8dd14f20b",
      "name": "Amman Weekly Planogram 10",
      "description": "Planogram for Cortanex Hypermarket - Amman Downtown shelf 10, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Pet Care",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Beverages",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Dairy",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.440008+00:00",
      "updated_at": "2026-02-18T10:26:26.440009+00:00"
    },
    {
      "id": "29e7a59b-2ca4-4088-8685-02d3550b23d7",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "shelf_id": "61150307-1617-48fc-bb5a-17189361789d",
      "name": "Irbid Weekly Planogram 01",
      "description": "Planogram for Cortanex Market - Irbid Center shelf 1, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Beverages",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Dairy",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Snacks",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.448091+00:00",
      "updated_at": "2026-02-18T10:26:26.448092+00:00"
    },
    {
      "id": "be1a3cd3-d844-402f-aeac-d6ba6bb24980",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "shelf_id": "e09f9991-d187-4d0c-a449-aa1962e8b024",
      "name": "Irbid Weekly Planogram 02",
      "description": "Planogram for Cortanex Market - Irbid Center shelf 2, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Dairy",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Snacks",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Breakfast",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.452277+00:00",
      "updated_at": "2026-02-18T10:26:26.452278+00:00"
    },
    {
      "id": "b2ede40c-fbbe-4996-b690-5852eca0ded1",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "shelf_id": "d416e787-de88-4d22-95f6-e7057218353e",
      "name": "Irbid Weekly Planogram 03",
      "description": "Planogram for Cortanex Market - Irbid Center shelf 3, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Snacks",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Breakfast",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Cleaning",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.456545+00:00",
      "updated_at": "2026-02-18T10:26:26.456547+00:00"
    },
    {
      "id": "a663558b-ceed-41c1-a0f7-e1bb6c76d3c3",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "shelf_id": "27ca3f2b-44ba-4e77-94f9-5e63f67d17fe",
      "name": "Irbid Weekly Planogram 04",
      "description": "Planogram for Cortanex Market - Irbid Center shelf 4, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Breakfast",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Cleaning",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Personal Care",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.460901+00:00",
      "updated_at": "2026-02-18T10:26:26.460902+00:00"
    },
    {
      "id": "576cedc4-c1d9-4b6e-bd6b-23f4d025c8f9",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "shelf_id": "994e3a3f-daac-443d-8897-65c91c63e0e5",
      "name": "Irbid Weekly Planogram 05",
      "description": "Planogram for Cortanex Market - Irbid Center shelf 5, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Cleaning",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Personal Care",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Canned Food",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.465304+00:00",
      "updated_at": "2026-02-18T10:26:26.465305+00:00"
    },
    {
      "id": "367eea6c-ad72-4526-b6de-dd307d869a5d",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "shelf_id": "b0609e8a-dcd4-49ff-b49a-67d8e85a7cd2",
      "name": "Irbid Weekly Planogram 06",
      "description": "Planogram for Cortanex Market - Irbid Center shelf 6, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Personal Care",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Canned Food",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Frozen",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.469180+00:00",
      "updated_at": "2026-02-18T10:26:26.469181+00:00"
    },
    {
      "id": "2054add1-6abb-463c-bed7-8bfc2c50971b",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "shelf_id": "3bd8a0f0-770e-4c19-a491-b4a351d1f060",
      "name": "Irbid Weekly Planogram 07",
      "description": "Planogram for Cortanex Market - Irbid Center shelf 7, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Canned Food",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Frozen",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Bakery",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.472752+00:00",
      "updated_at": "2026-02-18T10:26:26.472753+00:00"
    },
    {
      "id": "69a527ea-4c6b-466d-a731-791eb7a5de48",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "shelf_id": "012d3e6a-df9e-42f6-bb54-8601e3e66aea",
      "name": "Irbid Weekly Planogram 08",
      "description": "Planogram for Cortanex Market - Irbid Center shelf 8, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Frozen",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Bakery",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Pet Care",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.476870+00:00",
      "updated_at": "2026-02-18T10:26:26.476871+00:00"
    },
    {
      "id": "e441c77b-5843-4ea3-95cf-3e841f0a9399",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "shelf_id": "075e101a-20a8-43d7-a259-f991a084f8b4",
      "name": "Irbid Weekly Planogram 09",
      "description": "Planogram for Cortanex Market - Irbid Center shelf 9, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Bakery",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Pet Care",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Beverages",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.481035+00:00",
      "updated_at": "2026-02-18T10:26:26.481036+00:00"
    },
    {
      "id": "63f6545d-9bea-455d-90d7-cc9c6b82e487",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "0b4c05b9-8ca9-48dc-8a17-d0b218a7b72a",
      "shelf_id": "52651533-ca54-4a88-810e-83764f294a2c",
      "name": "Irbid Weekly Planogram 10",
      "description": "Planogram for Cortanex Market - Irbid Center shelf 10, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Pet Care",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Beverages",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Dairy",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.484711+00:00",
      "updated_at": "2026-02-18T10:26:26.484712+00:00"
    },
    {
      "id": "6de87742-0103-4062-9b9f-32115cec4486",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "shelf_id": "e31dad17-1b26-4fdc-bce5-e84704577899",
      "name": "Zarqa Weekly Planogram 01",
      "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 1, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Beverages",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Dairy",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Snacks",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.492669+00:00",
      "updated_at": "2026-02-18T10:26:26.492670+00:00"
    },
    {
      "id": "e4471aeb-7c31-43a6-aa9c-b0cf2bd7d62c",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "shelf_id": "93a6f2ce-ae7a-46bd-9426-711547e5328f",
      "name": "Zarqa Weekly Planogram 02",
      "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 2, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Dairy",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Snacks",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Breakfast",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.496824+00:00",
      "updated_at": "2026-02-18T10:26:26.496825+00:00"
    },
    {
      "id": "3ac44c5a-affc-40ca-bd08-edf5b75f3db4",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "shelf_id": "766a4f6c-10a0-4c56-a724-0f65641448f4",
      "name": "Zarqa Weekly Planogram 03",
      "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 3, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Snacks",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Breakfast",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Cleaning",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.500562+00:00",
      "updated_at": "2026-02-18T10:26:26.500563+00:00"
    },
    {
      "id": "cece8b53-a996-4e6c-af6a-e57be18625d0",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "shelf_id": "5d33755b-eb94-4e8b-870e-bae6cf76f40a",
      "name": "Zarqa Weekly Planogram 04",
      "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 4, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Breakfast",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Cleaning",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Personal Care",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.504077+00:00",
      "updated_at": "2026-02-18T10:26:26.504078+00:00"
    },
    {
      "id": "e48e8960-d32a-4d59-94b8-fc00a5b3c054",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "shelf_id": "64c34bcb-9935-4b06-9a0c-4866f7afe21e",
      "name": "Zarqa Weekly Planogram 05",
      "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 5, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Cleaning",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Personal Care",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Canned Food",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.508144+00:00",
      "updated_at": "2026-02-18T10:26:26.508145+00:00"
    },
    {
      "id": "3ee84eac-919a-4c13-a15b-25759fd5c5b2",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "shelf_id": "f6bf952e-65fa-40c9-aada-2b07935d9d80",
      "name": "Zarqa Weekly Planogram 06",
      "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 6, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Personal Care",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Canned Food",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Frozen",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.514899+00:00",
      "updated_at": "2026-02-18T10:26:26.514902+00:00"
    },
    {
      "id": "45ca046f-23cf-4ad4-86e8-54ba865673b8",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "shelf_id": "9fdcf997-9ae0-49f1-83d8-4853a02db060",
      "name": "Zarqa Weekly Planogram 07",
      "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 7, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Canned Food",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Frozen",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Bakery",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.520561+00:00",
      "updated_at": "2026-02-18T10:26:26.520563+00:00"
    },
    {
      "id": "159563ea-8501-4a20-8bee-95e8c46dd4b2",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "shelf_id": "796b633b-c512-4d2c-b9e2-ce6cb2e1bdcf",
      "name": "Zarqa Weekly Planogram 08",
      "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 8, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Frozen",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Bakery",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Pet Care",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.524442+00:00",
      "updated_at": "2026-02-18T10:26:26.524444+00:00"
    },
    {
      "id": "9ed5d2ba-9b25-46f3-88b0-c49b1221a66b",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "shelf_id": "2e0f413f-db09-44c5-b5ed-0b831fbea43f",
      "name": "Zarqa Weekly Planogram 09",
      "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 9, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Bakery",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Pet Care",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Beverages",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.528989+00:00",
      "updated_at": "2026-02-18T10:26:26.528992+00:00"
    },
    {
      "id": "8d9ac471-f7dc-4cdb-a10a-83e2dffba15a",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "d68618d2-0bfc-44b9-9534-caf53b80dff2",
      "shelf_id": "7df2c017-ca23-4d97-973c-75f834e86f2e",
      "name": "Zarqa Weekly Planogram 10",
      "description": "Planogram for Cortanex Market - Zarqa Avenue shelf 10, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Pet Care",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Beverages",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Dairy",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.535133+00:00",
      "updated_at": "2026-02-18T10:26:26.535135+00:00"
    },
    {
      "id": "1ee621fa-39ac-439f-9c23-952915308ae5",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "shelf_id": "e565bdaf-85ee-4e49-bdf7-f753bf93b06e",
      "name": "Aqaba Weekly Planogram 01",
      "description": "Planogram for Cortanex Express - Aqaba Marina shelf 1, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Beverages",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Dairy",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Snacks",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.545274+00:00",
      "updated_at": "2026-02-18T10:26:26.545275+00:00"
    },
    {
      "id": "0d863601-f6d7-4332-a26f-80faddf4afd3",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "shelf_id": "e74bdeee-68b0-4f07-92a8-7616fc4cd066",
      "name": "Aqaba Weekly Planogram 02",
      "description": "Planogram for Cortanex Express - Aqaba Marina shelf 2, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Dairy",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Snacks",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Breakfast",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.550223+00:00",
      "updated_at": "2026-02-18T10:26:26.550224+00:00"
    },
    {
      "id": "e0513da3-85d5-4b7c-93f5-f1ef14b68464",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "shelf_id": "a93baa02-4dbd-46c4-b642-cd658a968df5",
      "name": "Aqaba Weekly Planogram 03",
      "description": "Planogram for Cortanex Express - Aqaba Marina shelf 3, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Snacks",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Breakfast",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Cleaning",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.555531+00:00",
      "updated_at": "2026-02-18T10:26:26.555532+00:00"
    },
    {
      "id": "9bb2e133-ffff-40fb-bd64-33d49bf9290d",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "shelf_id": "bf6fa702-c0f5-4ea7-8f46-ed1b1327747c",
      "name": "Aqaba Weekly Planogram 04",
      "description": "Planogram for Cortanex Express - Aqaba Marina shelf 4, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Breakfast",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Cleaning",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Personal Care",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.559919+00:00",
      "updated_at": "2026-02-18T10:26:26.559921+00:00"
    },
    {
      "id": "05b6da97-58f2-4f28-9654-f3b53ec2aed4",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "shelf_id": "c4d60a91-f752-42c7-9baf-dff09954a349",
      "name": "Aqaba Weekly Planogram 05",
      "description": "Planogram for Cortanex Express - Aqaba Marina shelf 5, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Cleaning",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Personal Care",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Canned Food",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.564099+00:00",
      "updated_at": "2026-02-18T10:26:26.564100+00:00"
    },
    {
      "id": "b3d98adf-d815-496b-bdda-9140aa1de2c8",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "shelf_id": "4ddd5de9-374d-4be8-aba6-430a9aac60fa",
      "name": "Aqaba Weekly Planogram 06",
      "description": "Planogram for Cortanex Express - Aqaba Marina shelf 6, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Personal Care",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Canned Food",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Frozen",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.569188+00:00",
      "updated_at": "2026-02-18T10:26:26.569189+00:00"
    },
    {
      "id": "fc05b717-e9bf-458b-b3dd-d5bcd6493a9a",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "shelf_id": "e7b77017-9af9-4c22-bcf5-d8c52fd0d480",
      "name": "Aqaba Weekly Planogram 07",
      "description": "Planogram for Cortanex Express - Aqaba Marina shelf 7, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Canned Food",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Frozen",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Bakery",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.575331+00:00",
      "updated_at": "2026-02-18T10:26:26.575332+00:00"
    },
    {
      "id": "efc90b0e-b3ca-46bf-81e3-9a8880098868",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "shelf_id": "a8b07eea-a7ec-40c4-bc48-40c37a8fafee",
      "name": "Aqaba Weekly Planogram 08",
      "description": "Planogram for Cortanex Express - Aqaba Marina shelf 8, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Frozen",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Bakery",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Pet Care",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.580208+00:00",
      "updated_at": "2026-02-18T10:26:26.580210+00:00"
    },
    {
      "id": "473004dd-072d-4e7a-81ad-f42b0ad4eea5",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "shelf_id": "18c2bf42-5535-4c45-b601-3033022fff08",
      "name": "Aqaba Weekly Planogram 09",
      "description": "Planogram for Cortanex Express - Aqaba Marina shelf 9, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Bakery",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Pet Care",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Beverages",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.585016+00:00",
      "updated_at": "2026-02-18T10:26:26.585018+00:00"
    },
    {
      "id": "f2d6624b-6bd6-4209-8de3-51f710a18ee4",
      "tenant_id": "d94b7aa1-fd11-4915-85f6-1bf6cc5f6254",
      "store_id": "7e8439b0-ec6c-445d-a228-2ffb57163009",
      "shelf_id": "10157a4a-37fe-4957-b22c-d7e9eb8219e8",
      "name": "Aqaba Weekly Planogram 10",
      "description": "Planogram for Cortanex Express - Aqaba Marina shelf 10, weekly rotation",
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "category": "Pet Care",
          "expected_facings": 4,
          "priority": "high"
        },
        {
          "slot": 2,
          "category": "Beverages",
          "expected_facings": 3,
          "priority": "medium"
        },
        {
          "slot": 3,
          "category": "Dairy",
          "expected_facings": 2,
          "priority": "medium"
        }
      ],
      "created_by": "e26f368d-c9a3-4acc-a9ff-0a402ab77364",
      "created_at": "2026-02-18T10:26:26.590904+00:00",
      "updated_at": "2026-02-18T10:26:26.590906+00:00"
    }
  ]
}
```

