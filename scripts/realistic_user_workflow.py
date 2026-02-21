import json
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

BASE_URL = "http://127.0.0.1:8010"
API_KEY = "super-api-key-change-me"
EMAIL = "a.salameh@cortanexai.com"
PASSWORD = "123456"
USERNAME = "a.salameh"


def call_api(logs, name, method, path, payload=None, extra_headers=None):
    url = f"{BASE_URL}{path}"
    headers = {"apikey": API_KEY}
    if extra_headers:
        headers.update(extra_headers)

    body = None
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=body, method=method, headers=headers)

    status = None
    text = ""
    parsed = None
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            status = resp.status
            text = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        status = e.code
        text = e.read().decode("utf-8", errors="replace")
    except Exception as e:
        status = 0
        text = str(e)

    try:
        parsed = json.loads(text) if text else None
    except json.JSONDecodeError:
        parsed = text

    logs.append(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "name": name,
            "method": method,
            "path": path,
            "status": status,
            "request_payload": payload,
            "response": parsed,
        }
    )
    return status, parsed


def ensure(status, expected, step):
    if status != expected:
        raise RuntimeError(f"{step}: expected {expected}, got {status}")


def main():
    logs = []
    run_id = int(time.time())

    # Realistic static dictionaries
    store_defs = [
        {
            "name": "Cortanex Hypermarket - Amman West",
            "address": "Wasfi Al Tal Street, Building 221",
            "city": "Amman",
            "country": "Jordan",
        },
        {
            "name": "Cortanex Hypermarket - Amman Downtown",
            "address": "King Hussein Street, Block 14",
            "city": "Amman",
            "country": "Jordan",
        },
        {
            "name": "Cortanex Market - Irbid Center",
            "address": "University Street, Gate 3",
            "city": "Irbid",
            "country": "Jordan",
        },
        {
            "name": "Cortanex Market - Zarqa Avenue",
            "address": "36th Zarqa Main Road",
            "city": "Zarqa",
            "country": "Jordan",
        },
        {
            "name": "Cortanex Express - Aqaba Marina",
            "address": "Marina Promenade, Unit 9",
            "city": "Aqaba",
            "country": "Jordan",
        },
    ]

    category_catalog = [
        "Beverages", "Dairy", "Snacks", "Breakfast", "Cleaning", "Personal Care", "Canned Food", "Frozen", "Bakery", "Pet Care"
    ]

    # 1) Health
    call_api(logs, "Health Check", "GET", "/health")

    # 2) Sign up user (or continue if already exists)
    signup_payload = {
        "email": EMAIL,
        "password": PASSWORD,
        "data": {"full_name": "Ahmad Salameh"},
    }
    status, signup_resp = call_api(logs, "Signup User", "POST", "/auth/v1/signup", signup_payload)

    user_id = None
    if status == 200:
        user_id = signup_resp["user"]["id"]
    elif status == 409:
        # Existing user, use password grant to fetch user id
        status, token_resp = call_api(
            logs,
            "Password Grant Login (Existing User)",
            "POST",
            "/auth/v1/token?grant_type=password",
            {"email": EMAIL, "password": PASSWORD},
        )
        ensure(status, 200, "Password Grant Login")
        user_id = token_resp["user"]["id"]
    else:
        raise RuntimeError(f"Unexpected signup response: {status}")

    # 3) Create tenant
    tenant_payload = {
        "name": f"Cortanex Retail Group {run_id}",
        "status": "active",
        "is_active": True,
        "logo_url": "https://cdn.cortanex.ai/brand/cortanex-retail-logo.png",
        "username": "ops_admin",
        "password": "masked",
        "max_skus": 1000,
        "max_images_per_month": 150000,
        "max_images_per_week": 35000,
        "max_images_per_year": 1878700,
    }
    status, tenant = call_api(logs, "Create Tenant", "POST", "/rest/v1/tenants", tenant_payload)
    ensure(status, 201, "Create Tenant")
    tenant_id = tenant["id"]

    # 4) Update user profile with username + tenant
    profile_payload = {
        "tenant_id": tenant_id,
        "username": USERNAME,
        "full_name": "Ahmad Salameh",
        "avatar_url": "https://cdn.cortanex.ai/avatars/a.salameh.png",
    }
    status, _ = call_api(
        logs,
        "Update User Profile",
        "PATCH",
        f"/rest/v1/profiles?user_id=eq.{user_id}",
        profile_payload,
    )
    ensure(status, 200, "Update User Profile")

    # 5) Create categories for realism
    category_ids = []
    for idx, cat in enumerate(category_catalog, start=1):
        status, resp = call_api(
            logs,
            f"Create Category {idx}",
            "POST",
            "/rest/v1/product_categories",
            {
                "tenant_id": tenant_id,
                "name": cat,
                "description": f"{cat} products category for regional assortment planning",
            },
        )
        ensure(status, 201, f"Create Category {idx}")
        category_ids.append(resp["id"])

    # 6) Create stores, shelves, planograms; assign stores to user
    created_store_ids = []
    created_planogram_ids = []

    for store_index, store in enumerate(store_defs, start=1):
        status, store_resp = call_api(
            logs,
            f"Create Store {store_index}",
            "POST",
            "/rest/v1/stores",
            {
                "tenant_id": tenant_id,
                "name": store["name"],
                "address": store["address"],
                "city": store["city"],
                "country": store["country"],
            },
        )
        ensure(status, 201, f"Create Store {store_index}")
        store_id = store_resp["id"]
        created_store_ids.append(store_id)

        status, _ = call_api(
            logs,
            f"Assign Store {store_index} To User",
            "POST",
            "/rest/v1/user_store_access",
            {"user_id": user_id, "store_id": store_id},
        )
        ensure(status, 201, f"Assign Store {store_index} To User")

        for p in range(1, 11):
            shelf_name = f"{store['city']} - Aisle {p:02d}"
            status, shelf_resp = call_api(
                logs,
                f"Create Shelf S{store_index}-P{p}",
                "POST",
                "/rest/v1/shelves",
                {
                    "tenant_id": tenant_id,
                    "store_id": store_id,
                    "name": shelf_name,
                    "description": f"Main gondola shelf for aisle {p}",
                    "location_in_store": f"Zone-{(p % 5) + 1}",
                    "width_cm": 120 + (p * 5),
                },
            )
            ensure(status, 201, f"Create Shelf S{store_index}-P{p}")
            shelf_id = shelf_resp["id"]

            layout = [
                {
                    "slot": 1,
                    "category": category_catalog[(p - 1) % len(category_catalog)],
                    "expected_facings": 4,
                    "priority": "high",
                },
                {
                    "slot": 2,
                    "category": category_catalog[(p) % len(category_catalog)],
                    "expected_facings": 3,
                    "priority": "medium",
                },
                {
                    "slot": 3,
                    "category": category_catalog[(p + 1) % len(category_catalog)],
                    "expected_facings": 2,
                    "priority": "medium",
                },
            ]

            status, planogram_resp = call_api(
                logs,
                f"Create Planogram S{store_index}-P{p}",
                "POST",
                "/rest/v1/planogram_templates",
                {
                    "tenant_id": tenant_id,
                    "store_id": store_id,
                    "shelf_id": shelf_id,
                    "name": f"{store['city']} Weekly Planogram {p:02d}",
                    "description": f"Planogram for {store['name']} shelf {p}, weekly rotation",
                    "status": "active",
                    "layout": layout,
                    "created_by": user_id,
                },
            )
            ensure(status, 201, f"Create Planogram S{store_index}-P{p}")
            created_planogram_ids.append(planogram_resp["id"])

    # 7) Login using the requested email/password and verify assigned data
    status, login_resp = call_api(
        logs,
        "Login Via Email",
        "POST",
        "/auth/v1/login",
        {"identifier": EMAIL, "password": PASSWORD},
    )
    ensure(status, 200, "Login Via Email")

    returned_store_ids = {s.get("id") for s in login_resp.get("stores", []) if isinstance(s, dict)}
    returned_planogram_ids = {p.get("id") for p in login_resp.get("planograms", []) if isinstance(p, dict)}

    missing_stores = [sid for sid in created_store_ids if sid not in returned_store_ids]
    missing_planograms = [pid for pid in created_planogram_ids if pid not in returned_planogram_ids]

    summary = {
        "run_id": run_id,
        "email_used": EMAIL,
        "password_used": PASSWORD,
        "user_id": user_id,
        "tenant_id": tenant_id,
        "stores_created_count": len(created_store_ids),
        "planograms_created_count": len(created_planogram_ids),
        "expected_stores": 5,
        "expected_planograms": 50,
        "login_response_stores_count": len(login_resp.get("stores", [])),
        "login_response_planograms_count": len(login_resp.get("planograms", [])),
        "missing_created_stores_in_login_response": missing_stores,
        "missing_created_planograms_in_login_response": missing_planograms,
        "data_persistence": "No delete/cleanup operations executed; data intentionally persisted.",
    }

    out_path = "realistic_user_workflow_report.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Realistic User Workflow Test Report\n\n")
        f.write(f"- Generated at: {datetime.now(timezone.utc).isoformat()}\n")
        f.write(f"- Base URL: {BASE_URL}\n")
        f.write("- Scenario: Create realistic tenant/stores/shelves/planograms, assign to user, login with provided credentials, verify assigned data.\n")
        f.write("- Persistence: All created data kept in database (no cleanup).\n\n")

        f.write("## Summary\n")
        f.write("```json\n")
        f.write(json.dumps(summary, indent=2))
        f.write("\n```\n\n")

        for i, entry in enumerate(logs, start=1):
            f.write(f"## {i}. {entry['name']}\n")
            f.write(f"- Timestamp: `{entry['timestamp']}`\n")
            f.write(f"- Method: `{entry['method']}`\n")
            f.write(f"- Path: `{entry['path']}`\n")
            f.write(f"- Status: `{entry['status']}`\n")
            f.write("- Request payload:\n")
            f.write("```json\n")
            f.write(json.dumps(entry["request_payload"], indent=2))
            f.write("\n```\n")
            f.write("- Response:\n")
            f.write("```json\n")
            f.write(json.dumps(entry["response"], indent=2))
            f.write("\n```\n\n")

    print(json.dumps(summary, indent=2))
    print(f"REPORT_PATH={out_path}")


if __name__ == "__main__":
    main()
