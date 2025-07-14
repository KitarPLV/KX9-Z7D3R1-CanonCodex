
import sys
import os
import json
import time
import subprocess

# ✅ Allow importing from parent folder (where /ops/ lives)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ops.registry import TASK_REGISTRY

TASK_DIR = "canoncodex_inbox/tasks"
OUTPUT_DIR = "canoncodex_inbox/output"
PROCESSED_DIR = "canoncodex_inbox/processed"

def load_task(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def run_task(task):
    task_type = task.get("type")
    payload = task.get("payload", {})
    if task_type not in TASK_REGISTRY:
        print(f"❌ Unknown task type: {task_type}")
        return None

    print(f"▶️ Running task: {task_type}")
    result = TASK_REGISTRY[task_type](**payload)

    output_path = os.path.join(OUTPUT_DIR, f"{task_type}_result.txt")
    with open(output_path, "w") as f:
        f.write(str(result))
    print(f"✅ Task result written to {output_path}")
    return output_path

def daemon_loop():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    os.makedirs(TASK_DIR, exist_ok=True)

    print("🔁 CanonCodex Task Daemon Started.")
    while True:
        for file in os.listdir(TASK_DIR):
            if file.endswith(".task.json"):
                file_path = os.path.join(TASK_DIR, file)
                try:
                    task = load_task(file_path)
                    output_file = run_task(task)
                    if output_file:
                        subprocess.run(["python", "commit_snapshot.py"])
                        os.rename(file_path, os.path.join(PROCESSED_DIR, file))
                except Exception as e:
                    print(f"❌ Error processing {file}: {e}")
        time.sleep(10)

if __name__ == "__main__":
    daemon_loop()
