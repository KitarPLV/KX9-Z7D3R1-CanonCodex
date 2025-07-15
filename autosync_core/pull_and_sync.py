import requests
import os
from pathlib import Path
from datetime import datetime
from autosync_core.memory_to_file import save_memory_snapshot

# CONFIG: Replace this with your actual Gist raw URL or remote JSON endpoint
REMOTE_URL = "https://gist.githubusercontent.com/your-username/raw/ai_sync_payload.json"
INBOX_DIR = "canoncodex_inbox"

def log_sync(filename):
    with open("queue_log.txt", "a") as log:
        log.write(f"[PULL_SYNC] {filename} at {datetime.utcnow().isoformat()}\n")

def pull_and_sync():
    try:
        res = requests.get(REMOTE_URL)
        res.raise_for_status()
        payload = res.json()

        filename = payload.get("filename")
        content = payload.get("content")

        if not filename or not content:
            print("Invalid payload structure.")
            return

        Path(INBOX_DIR).mkdir(parents=True, exist_ok=True)
        filepath = Path(INBOX_DIR) / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        log_sync(filename)
        save_memory_snapshot({
            "event": "file_pulled",
            "filename": filename,
            "timestamp": datetime.utcnow().isoformat()
        })

        print(f"✅ Pulled and synced: {filename}")

    except Exception as e:
        print(f"❌ Pull failed: {e}")

if __name__ == "__main__":
    pull_and_sync()
