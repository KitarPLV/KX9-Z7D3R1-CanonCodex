import requests
import os
from pathlib import Path
from datetime import datetime
from autosync_core.memory_to_file import save_memory_snapshot

# ✅ Remote Gist JSON payload (from your Gist)
REMOTE_URL = "https://gist.githubusercontent.com/KitarPLV/243ae179beb4b10d21781dc17e5695a3/raw/ai_sync_payload.json"
INBOX_DIR = "canoncodex_inbox"
INBOX_DIR = Path("canoncodex_inbox")

def log_sync(filename):
    with open("queue_log.txt", "a") as log:
        log.write(f"[PULL_SYNC] {filename} at {datetime.utcnow().isoformat()}\n")

def pull_and_sync():
    try:
        print(f"📡 Pulling from: {REMOTE_URL}")
        res = requests.get(REMOTE_URL)
        res.raise_for_status()
        payload = res.json()

        filename = payload.get("filename")
        content = payload.get("content")
        payload_list = res.json()

        if not filename or not content:
            print("❌ Invalid payload structure.")
        if not isinstance(payload_list, list):
            print("❌ Invalid payload: expected a list.")
            return

        Path(INBOX_DIR).mkdir(parents=True, exist_ok=True)
        filepath = Path(INBOX_DIR) / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        INBOX_DIR.mkdir(parents=True, exist_ok=True)

        for payload in payload_list:
            filename = payload.get("filename")
            content = payload.get("content")

            if not filename or not content:
                print("⚠️ Skipped invalid entry in payload.")
                continue

            filepath = INBOX_DIR / filename
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

        log_sync(filename)
        save_memory_snapshot({
            "event": "file_pulled",
            "filename": filename,
            "source": REMOTE_URL,
            "timestamp": datetime.utcnow().isoformat()
        })
            log_sync(filename)
            save_memory_snapshot({
                "event": "file_pulled",
                "filename": filename,
                "source": REMOTE_URL,
                "timestamp": datetime.utcnow().isoformat()
            })

        print(f"✅ Pulled and synced: {filename}")
        print("✅ Sync completed for all files.")

    except Exception as e:
        print(f"❌ Pull failed: {e}")
        print(f"❌ Sync failed: {e}")

if __name__ == "__main__":
    pull_and_sync()