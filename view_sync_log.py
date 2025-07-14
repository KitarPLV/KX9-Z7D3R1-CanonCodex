
import json
import os

LOG_FILE = "sync_log.jsonl"

def tail_log(n=5):
    if not os.path.exists(LOG_FILE):
        print("No sync_log.jsonl found.")
        return
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()[-n:]
        for line in lines:
            try:
                entry = json.loads(line.strip())
                print(f"[{entry['timestamp']}] {entry['status'].upper()} - {entry['notes']}")
            except:
                continue

if __name__ == "__main__":
    print("🧠 Latest Sync Log Entries:")
    tail_log(10)
