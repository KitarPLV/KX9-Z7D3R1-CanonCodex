import json
from datetime import datetime
from pathlib import Path

def save_memory_snapshot(task_data: dict, memory_dir: str = "memory_logs"):
    Path(memory_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = f"{memory_dir}/memory_snapshot_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(task_data, f, indent=2)
    return filename
