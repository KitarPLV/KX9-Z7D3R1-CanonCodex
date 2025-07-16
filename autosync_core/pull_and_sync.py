# pull_and_sync.py

import requests
import os
from pathlib import Path
from datetime import datetime
from autosync_core.memory_to_file import save_memory_snapshot

REMOTE_URL = "https://gist.githubusercontent.com/KitarPLV/243ae179beb4b10d21781dc17e5695a3/raw/ai_sync_payload.json"
INBOX_DIR = Path("canoncodex_inbox")

def log_sync(filename):
    with open("queue_log.txt", "a") as log:
        log.write(f"[PULL_SYNC] {filename} at {datetime.utcnow().isoformat()}\n")

def pull_and_sync():
    try:
        res = requests.get(REMOTE_URL)
        payload_list = res.json()

        if not isinstance(payload_list, list):
            print("❌ Invalid payload: expected a list.")
            return

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

        print("✅ Sync completed for all files.")

    except Exception as e:
        print(f"❌ Sync failed: {e}")

if __name__ == "__main__":
    pull_and_sync()
