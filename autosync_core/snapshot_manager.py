import os
import json
from datetime import datetime

INBOX_DIR = "canoncodex_inbox"
SNAPSHOT_DIR = "snapshots"

def create_snapshot():
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    snapshot = {}

    if os.path.exists(INBOX_DIR):
        for file in os.listdir(INBOX_DIR):
            if file.endswith(".json"):
                with open(os.path.join(INBOX_DIR, file)) as f:
                    snapshot[file] = json.load(f)

    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    snapshot_file = os.path.join(SNAPSHOT_DIR, f"memory_{timestamp}.json")

    with open(snapshot_file, "w") as f:
        json.dump(snapshot, f, indent=2)

    return snapshot_file
