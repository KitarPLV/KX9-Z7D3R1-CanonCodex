import os
import traceback

from canoncodex.router import route_task
from canoncodex.telemetry import log_event
from canoncodex.sync.github_ingest import fetch_task
from canoncodex.integrations.prune_outputs import prune_old_outputs
from canoncodex.integrations.discord_notify import send_discord_alert

TASK_DIR = "tasks"
DONE_DIR = os.path.join(TASK_DIR, "_done")
OUTPUT_DIR = "outputs"

def process_tasks():
    os.makedirs(DONE_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    send_discord_alert("🧠 CanonCodex loop activated.")
    prune_old_outputs(OUTPUT_DIR)

    try:
        fetch_task(DONE_DIR)
    except Exception as e:
        print(f"⚠️ Failed to fetch tasks/_done ({e})")

    print("🔍 Scanning for tasks...")
    task_files = [f for f in os.listdir(TASK_DIR) if f.endswith(".txt") and f != "_done"]

    if not task_files:
        print("📭 No tasks found. Exiting.")
        return

    for file in task_files:
        task_path = os.path.join(TASK_DIR, file)
        print(f"🛠️  Processing: {file}")

        try:
            route_task(task_path)
            log_event(f"✅ Task completed: {file}")
            os.rename(task_path, os.path.join(DONE_DIR, file))
        except Exception as e:
            print(f"❌ Error: {e}")
            traceback.print_exc()
            log_event(f"❌ Task failed: {file}")

    print("✅ CanonCodex loop complete.")

if __name__ == "__main__":
    process_tasks()
