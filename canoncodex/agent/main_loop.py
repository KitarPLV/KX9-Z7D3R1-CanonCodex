import os
from canoncodex.handlers import write

TASK_DIR = "tasks"
DONE_DIR = os.path.join(TASK_DIR, "_done")
OUTPUT_DIR = "outputs"

def process_tasks():
    os.makedirs(DONE_DIR, exist_ok=True)
    task_files = [f for f in os.listdir(TASK_DIR) if f.endswith(".txt")]
    if not task_files:
        print("🕊️ No tasks found. Exiting.")
        return
    for file in task_files:
        task_path = os.path.join(TASK_DIR, file)
        print(f"🛠️  Processing: {file}")
        write.dispatch(task_path)
        os.rename(task_path, os.path.join(DONE_DIR, file))
    print("✅ Task processing complete.")

if __name__ == "__main__":
    process_tasks()
