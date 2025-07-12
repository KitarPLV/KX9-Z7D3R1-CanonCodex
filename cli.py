import sys
import os
import subprocess
from datetime import datetime
from ops import TASK_REGISTRY

SNAPSHOT_PATH = "canoncodex_inbox/notes/system_state_snapshot.md"

def update_snapshot(task_name, output_path):
    os.makedirs(os.path.dirname(SNAPSHOT_PATH), exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    snapshot_content = f"""# 🧠 CanonCodex System State Snapshot
**Last Updated**: {now}

## ✅ Last Task Run
- Name: {task_name}
- Output: {output_path}/{task_name}_result.txt

## 🔁 Active Tasks
""" + "\n".join([f"- {name}" for name in TASK_REGISTRY])

    with open(SNAPSHOT_PATH, "w") as f:
        f.write(snapshot_content)

def auto_commit_snapshot():
    try:
        subprocess.run(["git", "add", SNAPSHOT_PATH], check=True)
        subprocess.run(["git", "commit", "-m", "chore: update system snapshot"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Snapshot committed and pushed.")
    except subprocess.CalledProcessError as e:
        print("❌ Git commit failed:", e)

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <task_name> [--write-to <output_path>]")
        print("Available tasks:")
        for task in TASK_REGISTRY:
            print(f"  - {task}")
        sys.exit(1)

    task_name = sys.argv[1]
    output_path = "canoncodex_inbox/output"  # default

    if "--write-to" in sys.argv:
        try:
            output_path = sys.argv[sys.argv.index("--write-to") + 1]
        except IndexError:
            print("⚠️ Missing value for --write-to flag. Using default.")

    os.makedirs(output_path, exist_ok=True)
    log_file = os.path.join(output_path, f"{task_name}_result.txt")
    task = TASK_REGISTRY.get(task_name)

    if task:
        print(f"Running task: {task_name}")
        try:
            result = task()
            with open(log_file, "w") as f:
                f.write(f"✅ Task '{task_name}' completed successfully.\n")
                if result:
                    f.write(str(result) + "\n")
            update_snapshot(task_name, output_path)
            auto_commit_snapshot()
        except Exception as e:
            with open(log_file, "w") as f:
                f.write(f"❌ Task '{task_name}' failed with error:\n{e}\n")
            print(f"Task failed: {e}")
    else:
        print(f"Task '{task_name}' not found in registry.")
        with open(log_file, "w") as f:
            f.write(f"❌ Task '{task_name}' not found in registry.\n")

if __name__ == "__main__":
    main()