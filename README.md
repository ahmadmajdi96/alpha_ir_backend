# ShelfVision Backend (Dockerized)

Production-ready backend scaffold for ShelfVision with:

- FastAPI app
- PostgreSQL persistence (SQLAlchemy)
- JWT auth + API key auth
- REST resources under `/rest/v1/*`
- RPC endpoints under `/rest/v1/rpc/*`
- Edge-style functions under `/functions/v1/*`
- Storage upload/download endpoints under `/storage/v1/object/*`
- Docker + Docker Compose

## Run

```bash
docker compose up -d --build
```

API: `http://localhost:8787`

Health check:

```bash
curl http://localhost:8787/health
```

## Auth

You can authenticate with either:

- `Authorization: Bearer <jwt>`
- `apikey: <API_KEY>`

Default API key is in `.env`.

## Quick flow

1. Sign up:

```bash
curl -X POST http://localhost:8787/auth/v1/signup \
  -H 'Content-Type: application/json' \
  -d '{"email":"admin@example.com","password":"secret123","data":{"full_name":"Admin"}}'
```

2. Sign in:

```bash
curl -X POST 'http://localhost:8787/auth/v1/token?grant_type=password' \
  -H 'Content-Type: application/json' \
  -d '{"email":"admin@example.com","password":"secret123"}'
```

3. Create tenant (with API key):

```bash
curl -X POST http://localhost:8787/rest/v1/tenants \
  -H 'Content-Type: application/json' \
  -H 'apikey: super-api-key-change-me' \
  -d '{"name":"Tenant A","status":"active","is_active":true}'
```

4. List tenants:

```bash
curl -X GET 'http://localhost:8787/rest/v1/tenants?select=*' \
  -H 'apikey: super-api-key-change-me'
```

## Notes

- Query filters support `eq.` syntax, for example `?tenant_id=eq.<uuid>`.
- Sorting supports `order=field.desc` or `order=field.asc`.
- `select` is accepted for compatibility, but full SQL projection/join emulation is intentionally not implemented in this scaffold.
- AI detection endpoints are implemented with deterministic placeholders suitable for integration and further replacement with real model services.
