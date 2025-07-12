import os
import json
import time
import argparse
from datetime import datetime

def load_tasks(task_dir):
    if not os.path.isdir(task_dir):
        return []

    tasks = []
    for file in os.listdir(task_dir):
        if file.endswith(".json"):
            path = os.path.join(task_dir, file)
            with open(path, "r") as f:
                try:
                    data = json.load(f)
                    tasks.append((file, data.get("name"), data.get("status", "pending")))
                except:
                    tasks.append((file, "Invalid JSON", "error"))
    return tasks

def show_dashboard():
    print("\n📊 CanonCodex System Dashboard")
    print("-" * 40)

    print("\n📥 Task Inbox:")
    tasks = load_tasks("canoncodex_inbox/tasks")
    if tasks:
        for file, name, status in tasks:
            print(f" - {file}: {name} ({status})")
    else:
        print(" - No tasks found.")

    print("\n📤 Output:")
    for file in os.listdir("canoncodex_inbox/output"):
        print(f" - {file}")

    print("\n📝 Notes:")
    for file in os.listdir("canoncodex_inbox/notes"):
        print(f" - {file}")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n🕒 Last Updated: {now}")
    print("-" * 40)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", type=int, help="Refresh every N seconds")
    args = parser.parse_args()

    if args.watch:
        try:
            while True:
                os.system("clear" if os.name == "posix" else "cls")
                show_dashboard()
                time.sleep(args.watch)
        except KeyboardInterrupt:
            print("\n🛑 Stopped watching dashboard.")
    else:
        show_dashboard()
