import os
import json
from datetime import datetime

def save_memory_snapshot(data: dict, timestamp: str, directory: str = "memory_logs") -> str:
    os.makedirs(directory, exist_ok=True)
    filename = f"memory_snapshot_{timestamp}_pull.json"
    filepath = os.path.join(directory, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"[LOG] Saved memory snapshot: {filepath}")
    return filepath
