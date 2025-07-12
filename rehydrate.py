import os

SNAPSHOT_PATH = "canoncodex_inbox/notes/system_state_snapshot.md"

def rehydrate_state():
    if not os.path.exists(SNAPSHOT_PATH):
        print("❌ Snapshot not found.")
        return

    print("🔁 Rehydrating CanonCodex State from Snapshot...")
    with open(SNAPSHOT_PATH, "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.strip().startswith("- "):
            print("🧠", line.strip())

if __name__ == "__main__":
    rehydrate_state()