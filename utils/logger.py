
import json
import datetime

LOG_FILE = "sync_log.jsonl"

def log_sync_event(status, source="update_master_memory.py", notes=""):
    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "status": status,
        "source": source,
        "notes": notes
    }
    with open(LOG_FILE, "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")
