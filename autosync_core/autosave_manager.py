import os
import json
from datetime import datetime

INBOX_DIR = "canoncodex_inbox"
LOG_FILE = "logs/queue_log.txt"

def autosave_task(task_id, content, metadata=None):
    os.makedirs(INBOX_DIR, exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    entry = {
        "task_id": task_id,
        "timestamp": datetime.utcnow().isoformat(),
        "content": content,
        "metadata": metadata or {}
    }

    filepath = os.path.join(INBOX_DIR, f"{task_id}.json")
    with open(filepath, "w") as f:
        json.dump(entry, f, indent=2)

    with open(LOG_FILE, "a") as log:
        log.write(f"[{entry['timestamp']}] Saved {filepath}\n")

    return filepath
