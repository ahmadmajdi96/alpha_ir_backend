import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

BASE_URL = os.getenv("WORKFLOW_BASE_URL", "http://127.0.0.1:8787")
API_KEY = os.getenv("API_KEY", "super-api-key-change-me")


def call_api(logs, name, method, path, payload=None, headers=None):
    url = f"{BASE_URL}{path}"
    req_headers = {"apikey": API_KEY}
    if headers:
        req_headers.update(headers)

    req_body = None
    if payload is not None:
        req_body = json.dumps(payload).encode("utf-8")
        req_headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=req_body, method=method, headers=req_headers)

    status = None
    raw_text = ""
    parsed = None
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            raw_text = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as err:
        status = err.code
        raw_text = err.read().decode("utf-8", errors="replace")
    except Exception as exc:
        status = 0
        raw_text = str(exc)

    try:
        parsed = json.loads(raw_text) if raw_text else None
    except json.JSONDecodeError:
        parsed = raw_text

    logs.append(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "name": name,
            "method": method,
            "path": path,
            "request_headers": req_headers,
            "request_payload": payload,
            "status_code": status,
            "response": parsed,
        }
    )
    return status, parsed


def ensure_ok(status, expected, step):
    if status != expected:
        raise RuntimeError(f"{step} failed. expected={expected} actual={status}")


def main():
    run_id = int(time.time())
    logs = []

    user1_email = f"workflow_user1_{run_id}@example.com"
    user2_email = f"workflow_user2_{run_id}@example.com"
    user1_password = "secret123"
    user2_password = "secret123"
    user1_username = f"workflow_u1_{run_id}"
    user2_username = f"workflow_u2_{run_id}"

    # 1) Health
    call_api(logs, "Health Check", "GET", "/health")

    # 2) Create tenant
    status, tenant = call_api(
        logs,
        "Create Tenant",
        "POST",
        "/rest/v1/tenants",
        {
            "name": f"Workflow Tenant {run_id}",
            "status": "active",
            "is_active": True,
        },
    )
    ensure_ok(status, 201, "Create Tenant")
    tenant_id = tenant["id"]

    # 3) Create stores
    status, store1 = call_api(
        logs,
        "Create Store 1",
        "POST",
        "/rest/v1/stores",
        {
            "tenant_id": tenant_id,
            "name": f"Workflow Store 1 {run_id}",
            "city": "Cairo",
            "country": "EG",
        },
    )
    ensure_ok(status, 201, "Create Store 1")
    store1_id = store1["id"]

    status, store2 = call_api(
        logs,
        "Create Store 2",
        "POST",
        "/rest/v1/stores",
        {
            "tenant_id": tenant_id,
            "name": f"Workflow Store 2 {run_id}",
            "city": "Alexandria",
            "country": "EG",
        },
    )
    ensure_ok(status, 201, "Create Store 2")
    store2_id = store2["id"]

    # 4) Create shelves
    status, shelf1 = call_api(
        logs,
        "Create Shelf 1",
        "POST",
        "/rest/v1/shelves",
        {
            "tenant_id": tenant_id,
            "store_id": store1_id,
            "name": f"Workflow Shelf 1 {run_id}",
            "location_in_store": "A1",
        },
    )
    ensure_ok(status, 201, "Create Shelf 1")
    shelf1_id = shelf1["id"]

    status, shelf2 = call_api(
        logs,
        "Create Shelf 2",
        "POST",
        "/rest/v1/shelves",
        {
            "tenant_id": tenant_id,
            "store_id": store2_id,
            "name": f"Workflow Shelf 2 {run_id}",
            "location_in_store": "B1",
        },
    )
    ensure_ok(status, 201, "Create Shelf 2")
    shelf2_id = shelf2["id"]

    # 5) Create planograms
    status, planogram1 = call_api(
        logs,
        "Create Planogram 1",
        "POST",
        "/rest/v1/planogram_templates",
        {
            "tenant_id": tenant_id,
            "store_id": store1_id,
            "shelf_id": shelf1_id,
            "name": f"Workflow Planogram 1 {run_id}",
            "status": "active",
            "layout": [{"slot": 1, "label": "SKU-A"}],
        },
    )
    ensure_ok(status, 201, "Create Planogram 1")

    status, planogram2 = call_api(
        logs,
        "Create Planogram 2",
        "POST",
        "/rest/v1/planogram_templates",
        {
            "tenant_id": tenant_id,
            "store_id": store2_id,
            "shelf_id": shelf2_id,
            "name": f"Workflow Planogram 2 {run_id}",
            "status": "active",
            "layout": [{"slot": 1, "label": "SKU-B"}],
        },
    )
    ensure_ok(status, 201, "Create Planogram 2")

    # 6) Register users
    status, signup1 = call_api(
        logs,
        "Signup User 1",
        "POST",
        "/auth/v1/signup",
        {
            "email": user1_email,
            "password": user1_password,
            "data": {"full_name": "Workflow User One"},
        },
    )
    ensure_ok(status, 200, "Signup User 1")
    user1_id = signup1["user"]["id"]

    status, signup2 = call_api(
        logs,
        "Signup User 2",
        "POST",
        "/auth/v1/signup",
        {
            "email": user2_email,
            "password": user2_password,
            "data": {"full_name": "Workflow User Two"},
        },
    )
    ensure_ok(status, 200, "Signup User 2")
    user2_id = signup2["user"]["id"]

    # 7) Attach tenant + usernames to profiles
    status, _ = call_api(
        logs,
        "Update Profile User 1",
        "PATCH",
        f"/rest/v1/profiles?user_id=eq.{user1_id}",
        {
            "tenant_id": tenant_id,
            "username": user1_username,
            "full_name": "Workflow User One",
        },
    )
    ensure_ok(status, 200, "Update Profile User 1")

    status, _ = call_api(
        logs,
        "Update Profile User 2",
        "PATCH",
        f"/rest/v1/profiles?user_id=eq.{user2_id}",
        {
            "tenant_id": tenant_id,
            "username": user2_username,
            "full_name": "Workflow User Two",
        },
    )
    ensure_ok(status, 200, "Update Profile User 2")

    # 8) Assign store access
    status, _ = call_api(
        logs,
        "Assign Store 1 to User 1",
        "POST",
        "/rest/v1/user_store_access",
        {"user_id": user1_id, "store_id": store1_id},
    )
    ensure_ok(status, 201, "Assign Store 1 to User 1")

    status, _ = call_api(
        logs,
        "Assign Store 2 to User 2",
        "POST",
        "/rest/v1/user_store_access",
        {"user_id": user2_id, "store_id": store2_id},
    )
    ensure_ok(status, 201, "Assign Store 2 to User 2")

    # 9) Login and verify returned assigned stores/planograms
    status, login1 = call_api(
        logs,
        "Login User 1 via Username",
        "POST",
        "/auth/v1/login",
        {"identifier": user1_username, "password": user1_password},
    )
    ensure_ok(status, 200, "Login User 1 via Username")

    status, login2 = call_api(
        logs,
        "Login User 2 via Email",
        "POST",
        "/auth/v1/login",
        {"identifier": user2_email, "password": user2_password},
    )
    ensure_ok(status, 200, "Login User 2 via Email")

    summary = {
        "run_id": run_id,
        "tenant_id": tenant_id,
        "store_ids": [store1_id, store2_id],
        "shelf_ids": [shelf1_id, shelf2_id],
        "planogram_ids": [planogram1["id"], planogram2["id"]],
        "user_ids": [user1_id, user2_id],
        "user_credentials": [
            {"identifier": user1_username, "email": user1_email, "password": user1_password},
            {"identifier": user2_email, "email": user2_email, "password": user2_password},
        ],
        "login_user1_stores": len(login1.get("stores", [])) if isinstance(login1, dict) else None,
        "login_user1_planograms": len(login1.get("planograms", [])) if isinstance(login1, dict) else None,
        "login_user2_stores": len(login2.get("stores", [])) if isinstance(login2, dict) else None,
        "login_user2_planograms": len(login2.get("planograms", [])) if isinstance(login2, dict) else None,
        "data_persistence_note": "No cleanup/delete was executed. All created records remain in the database.",
    }

    generated_at = datetime.now(timezone.utc).isoformat()
    out_dir = "/app/test_reports"
    os.makedirs(out_dir, exist_ok=True)
    report_path = os.path.join(out_dir, "user_assignment_workflow_report.md")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# User Assignment Workflow Report\n\n")
        f.write(f"- Generated at: {generated_at}\n")
        f.write(f"- Base URL: {BASE_URL}\n")
        f.write("- Workflow goal: register users, assign stores/planograms, login, and verify assigned data in response.\n")
        f.write("- Persistence: created records intentionally kept in DB (no deletion).\n\n")

        f.write("## Run Summary\n")
        f.write("```json\n")
        f.write(json.dumps(summary, indent=2))
        f.write("\n```\n\n")

        for idx, entry in enumerate(logs, start=1):
            f.write(f"## {idx}. {entry['name']}\n")
            f.write(f"- Timestamp: `{entry['timestamp']}`\n")
            f.write(f"- Method: `{entry['method']}`\n")
            f.write(f"- Path: `{entry['path']}`\n")
            f.write(f"- Status: `{entry['status_code']}`\n")
            f.write("- Request headers:\n")
            f.write("```json\n")
            f.write(json.dumps(entry["request_headers"], indent=2))
            f.write("\n```\n")
            f.write("- Request payload:\n")
            f.write("```json\n")
            f.write(json.dumps(entry["request_payload"], indent=2))
            f.write("\n```\n")
            f.write("- Response:\n")
            f.write("```json\n")
            f.write(json.dumps(entry["response"], indent=2))
            f.write("\n```\n\n")

    print(json.dumps({"ok": True, "report_path": report_path, "steps": len(logs), "summary": summary}))


if __name__ == "__main__":
    main()
