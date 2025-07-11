import os
import time
from canoncodex.handlers import write

TASK_DIR = "tasks"
PROCESSED_DIR = os.path.join(TASK_DIR, "_done")
os.makedirs(PROCESSED_DIR, exist_ok=True)

def dispatch(task_path):
    with open(task_path, "r") as f:
        content = f.read()
    if "TASK_TYPE: write" in content:
        write.handle(content)
    else:
        print(f"No handler for: {task_path}")

def watch():
    print("🔁 Watching for tasks...")
    while True:
        tasks = [f for f in os.listdir(TASK_DIR) if f.endswith(".txt") and f != "_done"]
        for task in tasks:
            full_path = os.path.join(TASK_DIR, task)
            try:
                dispatch(full_path)
                os.rename(full_path, os.path.join(PROCESSED_DIR, task))
            except Exception as e:
                print(f"❌ Error processing {task}: {e}")
        time.sleep(2)

if __name__ == "__main__":
    watch()
