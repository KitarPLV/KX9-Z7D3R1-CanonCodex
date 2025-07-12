import json
import os
import sys
from datetime import datetime

TASKS_DIR = "canoncodex_inbox/tasks"

def queue_task(task_name, args=None):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    task_filename = f"{task_name}_{timestamp}.task.json"
    task_path = os.path.join(TASKS_DIR, task_filename)

    task_data = {
        "name": task_name,
        "args": args or []
    }

    os.makedirs(TASKS_DIR, exist_ok=True)
    with open(task_path, "w") as f:
        json.dump(task_data, f, indent=2)

    print(f"✅ Queued task: {task_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python queue_task.py <task_name> [arg1 arg2 ...]")
        sys.exit(1)

    name = sys.argv[1]
    arguments = sys.argv[2:] if len(sys.argv) > 2 else []
    queue_task(name, arguments)