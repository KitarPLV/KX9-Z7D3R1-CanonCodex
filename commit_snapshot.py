import os
import subprocess

SNAPSHOT_FILE = "canoncodex_inbox/notes/system_state_snapshot.md"

def git_commit_snapshot():
    if not os.path.exists(SNAPSHOT_FILE):
        print("❌ Snapshot file not found.")
        return

    try:
        subprocess.run(["git", "add", "-u"], check=True)
        result = subprocess.run(
            ["git", "commit", "-m", "chore: update system snapshot"],
            check=False  # allow graceful exit
        )
        if result.returncode == 0:
            subprocess.run(["git", "push"], check=True)
            print("✅ Snapshot committed and pushed.")
        else:
            print("🟡 No changes to commit.")
    except subprocess.CalledProcessError as e:
        print("❌ Git operation failed:", e)

if __name__ == "__main__":
    git_commit_snapshot()
