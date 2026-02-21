# User Assignment Workflow Report

- Generated at: 2026-02-18T08:08:51.952467+00:00
- Base URL: http://127.0.0.1:8787
- Workflow goal: register users, assign stores/planograms, login, and verify assigned data in response.
- Persistence: created records intentionally kept in DB (no deletion).

## Run Summary
```json
{
  "run_id": 1771402131,
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "store_ids": [
    "6d90d362-b97d-4125-ac5e-1c784c45a08f",
    "0cea5ad7-6931-4c36-bf29-bdb855b42693"
  ],
  "shelf_ids": [
    "b48392cc-c85c-4d5f-beef-c6813567ee8d",
    "43c4612a-a1bd-4906-b6d2-7f08d9ed138d"
  ],
  "planogram_ids": [
    "0f6378b6-3002-4e8d-82ca-406dc91fea65",
    "85954bfa-967a-49df-ac9b-e9c20d93440f"
  ],
  "user_ids": [
    "fe14b554-0e7e-44dd-9701-6fc8b7b9cb62",
    "1a687fd0-3989-48a4-800f-21986c0cb63a"
  ],
  "user_credentials": [
    {
      "identifier": "workflow_u1_1771402131",
      "email": "workflow_user1_1771402131@example.com",
      "password": "secret123"
    },
    {
      "identifier": "workflow_user2_1771402131@example.com",
      "email": "workflow_user2_1771402131@example.com",
      "password": "secret123"
    }
  ],
  "login_user1_stores": 1,
  "login_user1_planograms": 1,
  "login_user2_stores": 1,
  "login_user2_planograms": 1,
  "data_persistence_note": "No cleanup/delete was executed. All created records remain in the database."
}
```

## 1. Health Check
- Timestamp: `2026-02-18T08:08:51.878265+00:00`
- Method: `GET`
- Path: `/health`
- Status: `200`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me"
}
```
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

## 2. Create Tenant
- Timestamp: `2026-02-18T08:08:51.893994+00:00`
- Method: `POST`
- Path: `/rest/v1/tenants`
- Status: `201`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "name": "Workflow Tenant 1771402131",
  "status": "active",
  "is_active": true
}
```
- Response:
```json
{
  "id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "name": "Workflow Tenant 1771402131",
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
  "created_at": "2026-02-18T08:08:51.888680+00:00",
  "updated_at": "2026-02-18T08:08:51.888682+00:00"
}
```

## 3. Create Store 1
- Timestamp: `2026-02-18T08:08:51.897499+00:00`
- Method: `POST`
- Path: `/rest/v1/stores`
- Status: `201`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "name": "Workflow Store 1 1771402131",
  "city": "Cairo",
  "country": "EG"
}
```
- Response:
```json
{
  "id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "name": "Workflow Store 1 1771402131",
  "address": null,
  "city": "Cairo",
  "country": "EG",
  "created_at": "2026-02-18T08:08:51.895021+00:00",
  "updated_at": "2026-02-18T08:08:51.895023+00:00"
}
```

## 4. Create Store 2
- Timestamp: `2026-02-18T08:08:51.899799+00:00`
- Method: `POST`
- Path: `/rest/v1/stores`
- Status: `201`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "name": "Workflow Store 2 1771402131",
  "city": "Alexandria",
  "country": "EG"
}
```
- Response:
```json
{
  "id": "0cea5ad7-6931-4c36-bf29-bdb855b42693",
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "name": "Workflow Store 2 1771402131",
  "address": null,
  "city": "Alexandria",
  "country": "EG",
  "created_at": "2026-02-18T08:08:51.898156+00:00",
  "updated_at": "2026-02-18T08:08:51.898157+00:00"
}
```

## 5. Create Shelf 1
- Timestamp: `2026-02-18T08:08:51.902959+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "store_id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
  "name": "Workflow Shelf 1 1771402131",
  "location_in_store": "A1"
}
```
- Response:
```json
{
  "id": "b48392cc-c85c-4d5f-beef-c6813567ee8d",
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "store_id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
  "name": "Workflow Shelf 1 1771402131",
  "description": null,
  "location_in_store": "A1",
  "width_cm": null,
  "created_at": "2026-02-18T08:08:51.900623+00:00",
  "updated_at": "2026-02-18T08:08:51.900625+00:00"
}
```

## 6. Create Shelf 2
- Timestamp: `2026-02-18T08:08:51.904633+00:00`
- Method: `POST`
- Path: `/rest/v1/shelves`
- Status: `201`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "store_id": "0cea5ad7-6931-4c36-bf29-bdb855b42693",
  "name": "Workflow Shelf 2 1771402131",
  "location_in_store": "B1"
}
```
- Response:
```json
{
  "id": "43c4612a-a1bd-4906-b6d2-7f08d9ed138d",
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "store_id": "0cea5ad7-6931-4c36-bf29-bdb855b42693",
  "name": "Workflow Shelf 2 1771402131",
  "description": null,
  "location_in_store": "B1",
  "width_cm": null,
  "created_at": "2026-02-18T08:08:51.903449+00:00",
  "updated_at": "2026-02-18T08:08:51.903450+00:00"
}
```

## 7. Create Planogram 1
- Timestamp: `2026-02-18T08:08:51.907401+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "store_id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
  "shelf_id": "b48392cc-c85c-4d5f-beef-c6813567ee8d",
  "name": "Workflow Planogram 1 1771402131",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "label": "SKU-A"
    }
  ]
}
```
- Response:
```json
{
  "id": "0f6378b6-3002-4e8d-82ca-406dc91fea65",
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "store_id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
  "shelf_id": "b48392cc-c85c-4d5f-beef-c6813567ee8d",
  "name": "Workflow Planogram 1 1771402131",
  "description": null,
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "label": "SKU-A"
    }
  ],
  "created_by": null,
  "created_at": "2026-02-18T08:08:51.905446+00:00",
  "updated_at": "2026-02-18T08:08:51.905447+00:00"
}
```

## 8. Create Planogram 2
- Timestamp: `2026-02-18T08:08:51.909116+00:00`
- Method: `POST`
- Path: `/rest/v1/planogram_templates`
- Status: `201`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "store_id": "0cea5ad7-6931-4c36-bf29-bdb855b42693",
  "shelf_id": "43c4612a-a1bd-4906-b6d2-7f08d9ed138d",
  "name": "Workflow Planogram 2 1771402131",
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "label": "SKU-B"
    }
  ]
}
```
- Response:
```json
{
  "id": "85954bfa-967a-49df-ac9b-e9c20d93440f",
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "store_id": "0cea5ad7-6931-4c36-bf29-bdb855b42693",
  "shelf_id": "43c4612a-a1bd-4906-b6d2-7f08d9ed138d",
  "name": "Workflow Planogram 2 1771402131",
  "description": null,
  "status": "active",
  "layout": [
    {
      "slot": 1,
      "label": "SKU-B"
    }
  ],
  "created_by": null,
  "created_at": "2026-02-18T08:08:51.907921+00:00",
  "updated_at": "2026-02-18T08:08:51.907922+00:00"
}
```

## 9. Signup User 1
- Timestamp: `2026-02-18T08:08:51.920787+00:00`
- Method: `POST`
- Path: `/auth/v1/signup`
- Status: `200`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "email": "workflow_user1_1771402131@example.com",
  "password": "secret123",
  "data": {
    "full_name": "Workflow User One"
  }
}
```
- Response:
```json
{
  "user": {
    "id": "fe14b554-0e7e-44dd-9701-6fc8b7b9cb62",
    "email": "workflow_user1_1771402131@example.com"
  },
  "session": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmZTE0YjU1NC0wZTdlLTQ0ZGQtOTcwMS02ZmM4YjdiOWNiNjIiLCJleHAiOjE3NzE0ODg1MzF9.rl20HX_EvUb-4YzSp3L7fQknYZyQFEJt55mlzze-fNo",
    "token_type": "bearer",
    "expires_in": 86400
  }
}
```

## 10. Signup User 2
- Timestamp: `2026-02-18T08:08:51.926656+00:00`
- Method: `POST`
- Path: `/auth/v1/signup`
- Status: `200`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "email": "workflow_user2_1771402131@example.com",
  "password": "secret123",
  "data": {
    "full_name": "Workflow User Two"
  }
}
```
- Response:
```json
{
  "user": {
    "id": "1a687fd0-3989-48a4-800f-21986c0cb63a",
    "email": "workflow_user2_1771402131@example.com"
  },
  "session": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxYTY4N2ZkMC0zOTg5LTQ4YTQtODAwZi0yMTk4NmMwY2I2M2EiLCJleHAiOjE3NzE0ODg1MzF9.k1I5HIGL0S-uB6l2hi8qT-cfvcYXO_WJbhlzvawvlR4",
    "token_type": "bearer",
    "expires_in": 86400
  }
}
```

## 11. Update Profile User 1
- Timestamp: `2026-02-18T08:08:51.930327+00:00`
- Method: `PATCH`
- Path: `/rest/v1/profiles?user_id=eq.fe14b554-0e7e-44dd-9701-6fc8b7b9cb62`
- Status: `200`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "username": "workflow_u1_1771402131",
  "full_name": "Workflow User One"
}
```
- Response:
```json
{
  "id": "8648e1e4-da8f-405c-a474-3ad3f6e933d3",
  "user_id": "fe14b554-0e7e-44dd-9701-6fc8b7b9cb62",
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "full_name": "Workflow User One",
  "username": "workflow_u1_1771402131",
  "avatar_url": null,
  "last_login": null,
  "created_at": "2026-02-18T08:08:51.918080+00:00",
  "updated_at": "2026-02-18T08:08:51.928441+00:00"
}
```

## 12. Update Profile User 2
- Timestamp: `2026-02-18T08:08:51.932735+00:00`
- Method: `PATCH`
- Path: `/rest/v1/profiles?user_id=eq.1a687fd0-3989-48a4-800f-21986c0cb63a`
- Status: `200`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "username": "workflow_u2_1771402131",
  "full_name": "Workflow User Two"
}
```
- Response:
```json
{
  "id": "e145f5e6-7352-4a02-b326-690951547537",
  "user_id": "1a687fd0-3989-48a4-800f-21986c0cb63a",
  "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
  "full_name": "Workflow User Two",
  "username": "workflow_u2_1771402131",
  "avatar_url": null,
  "last_login": null,
  "created_at": "2026-02-18T08:08:51.925009+00:00",
  "updated_at": "2026-02-18T08:08:51.931213+00:00"
}
```

## 13. Assign Store 1 to User 1
- Timestamp: `2026-02-18T08:08:51.935570+00:00`
- Method: `POST`
- Path: `/rest/v1/user_store_access`
- Status: `201`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "user_id": "fe14b554-0e7e-44dd-9701-6fc8b7b9cb62",
  "store_id": "6d90d362-b97d-4125-ac5e-1c784c45a08f"
}
```
- Response:
```json
{
  "id": "acf52b34-4b1c-4f2c-b73a-4f52cea500f1",
  "user_id": "fe14b554-0e7e-44dd-9701-6fc8b7b9cb62",
  "store_id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
  "created_at": "2026-02-18T08:08:51.933517+00:00"
}
```

## 14. Assign Store 2 to User 2
- Timestamp: `2026-02-18T08:08:51.937279+00:00`
- Method: `POST`
- Path: `/rest/v1/user_store_access`
- Status: `201`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "user_id": "1a687fd0-3989-48a4-800f-21986c0cb63a",
  "store_id": "0cea5ad7-6931-4c36-bf29-bdb855b42693"
}
```
- Response:
```json
{
  "id": "cfb3129c-6022-4e28-8102-6b4ef4e55eca",
  "user_id": "1a687fd0-3989-48a4-800f-21986c0cb63a",
  "store_id": "0cea5ad7-6931-4c36-bf29-bdb855b42693",
  "created_at": "2026-02-18T08:08:51.936095+00:00"
}
```

## 15. Login User 1 via Username
- Timestamp: `2026-02-18T08:08:51.946102+00:00`
- Method: `POST`
- Path: `/auth/v1/login`
- Status: `200`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "identifier": "workflow_u1_1771402131",
  "password": "secret123"
}
```
- Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmZTE0YjU1NC0wZTdlLTQ0ZGQtOTcwMS02ZmM4YjdiOWNiNjIiLCJleHAiOjE3NzE0ODg1MzF9.rl20HX_EvUb-4YzSp3L7fQknYZyQFEJt55mlzze-fNo",
  "refresh_token": "db2731ce-b7a4-4f23-89dd-e9da898a08d3",
  "expires_in": 86400,
  "token_type": "bearer",
  "user": {
    "id": "fe14b554-0e7e-44dd-9701-6fc8b7b9cb62",
    "email": "workflow_user1_1771402131@example.com",
    "username": "workflow_u1_1771402131"
  },
  "stores": [
    {
      "id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
      "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
      "name": "Workflow Store 1 1771402131",
      "address": null,
      "city": "Cairo",
      "country": "EG",
      "created_at": "2026-02-18T08:08:51.895021+00:00",
      "updated_at": "2026-02-18T08:08:51.895023+00:00"
    }
  ],
  "planograms": [
    {
      "id": "0f6378b6-3002-4e8d-82ca-406dc91fea65",
      "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
      "store_id": "6d90d362-b97d-4125-ac5e-1c784c45a08f",
      "shelf_id": "b48392cc-c85c-4d5f-beef-c6813567ee8d",
      "name": "Workflow Planogram 1 1771402131",
      "description": null,
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "label": "SKU-A"
        }
      ],
      "created_by": null,
      "created_at": "2026-02-18T08:08:51.905446+00:00",
      "updated_at": "2026-02-18T08:08:51.905447+00:00"
    }
  ]
}
```

## 16. Login User 2 via Email
- Timestamp: `2026-02-18T08:08:51.952458+00:00`
- Method: `POST`
- Path: `/auth/v1/login`
- Status: `200`
- Request headers:
```json
{
  "apikey": "super-api-key-change-me",
  "Content-Type": "application/json"
}
```
- Request payload:
```json
{
  "identifier": "workflow_user2_1771402131@example.com",
  "password": "secret123"
}
```
- Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxYTY4N2ZkMC0zOTg5LTQ4YTQtODAwZi0yMTk4NmMwY2I2M2EiLCJleHAiOjE3NzE0ODg1MzF9.k1I5HIGL0S-uB6l2hi8qT-cfvcYXO_WJbhlzvawvlR4",
  "refresh_token": "2116e5b1-a882-4a82-b21e-d97e6be359ad",
  "expires_in": 86400,
  "token_type": "bearer",
  "user": {
    "id": "1a687fd0-3989-48a4-800f-21986c0cb63a",
    "email": "workflow_user2_1771402131@example.com",
    "username": "workflow_u2_1771402131"
  },
  "stores": [
    {
      "id": "0cea5ad7-6931-4c36-bf29-bdb855b42693",
      "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
      "name": "Workflow Store 2 1771402131",
      "address": null,
      "city": "Alexandria",
      "country": "EG",
      "created_at": "2026-02-18T08:08:51.898156+00:00",
      "updated_at": "2026-02-18T08:08:51.898157+00:00"
    }
  ],
  "planograms": [
    {
      "id": "85954bfa-967a-49df-ac9b-e9c20d93440f",
      "tenant_id": "e651123f-8d2e-46b8-8d59-b60e852a0aa0",
      "store_id": "0cea5ad7-6931-4c36-bf29-bdb855b42693",
      "shelf_id": "43c4612a-a1bd-4906-b6d2-7f08d9ed138d",
      "name": "Workflow Planogram 2 1771402131",
      "description": null,
      "status": "active",
      "layout": [
        {
          "slot": 1,
          "label": "SKU-B"
        }
      ],
      "created_by": null,
      "created_at": "2026-02-18T08:08:51.907921+00:00",
      "updated_at": "2026-02-18T08:08:51.907922+00:00"
    }
  ]
}
```

