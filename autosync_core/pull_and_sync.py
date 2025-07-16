import os
import requests
from datetime import datetime
from autosync_core.logger import save_memory_snapshot  # ✅ Updated import

def pull_and_sync():
    gist_url = os.getenv("GIST_PAYLOAD_URL")
    if not gist_url:
        raise ValueError("GIST_PAYLOAD_URL environment variable not set")

    response = requests.get(gist_url)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch payload: {response.status_code}")

    try:
        payload = response.json()
    except ValueError as e:
        raise RuntimeError("Payload is not valid JSON") from e

    # Ensure payload is a list of objects
    if not isinstance(payload, list):
        raise ValueError("Expected payload to be a list of file descriptors")

    synced_files = []

    for item in payload:
        filename = item.get("filename")
        content = item.get("content")

        if not filename or not content:
            print(f"Skipping invalid item: {item}")
            continue

        os.makedirs("canoncodex_inbox/tasks", exist_ok=True)
        filepath = os.path.join("canoncodex_inbox/tasks", filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"[PULL_SYNC] Synced: {filename}")
        synced_files.append(filename)

    # Log snapshot with timestamp
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    save_memory_snapshot(tag=f"sync_{timestamp}")

    return synced_files


# Optional helper for running independently
if __name__ == "__main__":
    try:
        results = pull_and_sync()
        print(f"\n✅ Synced {len(results)} files:", results)
    except Exception as e:
        print(f"\n❌ Sync failed: {e}")
