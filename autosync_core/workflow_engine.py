import os
import json
from datetime import datetime

LOG_FILE = "logs/workflow_state.jsonl"

def log_state(task_id, state, next_action, source="system"):
    os.makedirs("logs", exist_ok=True)

    entry = {
        "task_id": task_id,
        "timestamp": datetime.utcnow().isoformat(),
        "state": state,
        "next_action": next_action,
        "source": source
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return entry

def get_all_states():
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as f:
        return [json.loads(line) for line in f]
