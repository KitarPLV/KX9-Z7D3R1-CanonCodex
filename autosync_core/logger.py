import os
import json
from datetime import datetime

def save_memory_snapshot(memory_data: dict, timestamp: str = None, directory: str = "memory_logs") -> str:
    os.makedirs(directory, exist_ok=True)

    if timestamp is None:
        timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    filename = f"memory_snapshot_{timestamp}.json"
    filepath = os.path.join(directory, filename)

    memory = {
        "timestamp": timestamp,
        "status": "Synced successfully",
        "details": memory_data.get("details", [])
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

    print(f"[LOG] Saved memory snapshot → {filepath}")
    return filepath
