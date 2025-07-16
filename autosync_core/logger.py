import os, json
from datetime import datetime

def save_memory_snapshot(tag=None, directory="memory_logs") -> str:
    os.makedirs(directory, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    tag_suffix = f"_{tag}" if tag else ""
    filename = f"memory_snapshot_{timestamp}{tag_suffix}.json"

    memory = {
        "timestamp": timestamp,
        "status": "Synced successfully",
        "details": {}
    }

    filepath = os.path.join(directory, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

    print(f"[LOG] Saved memory snapshot: {filepath}")
    return filepath
