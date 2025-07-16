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

import os
import json
from pathlib import Path
from autosync_core.logger import save_memory_snapshot

def run_workflow_tasks(task_dir="canoncodex_inbox/tasks"):
    task_path = Path(task_dir)
    for task_file in task_path.glob("*.json"):
        with open(task_file, "r", encoding="utf-8") as f:
            task_data = json.load(f)
            print(f"[TASK] Executing task: {task_file.name}")
            print(json.dumps(task_data, indent=2))

        # Simulate result handling and logging
        save_memory_snapshot(tag=f"task_{task_file.stem}")
        os.rename(task_file, task_file.with_suffix(".done.json"))