import shutil
import os
from datetime import datetime

SRC = "/mnt/data/"
DEST = "canoncodex_inbox/sandbox_backups/"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
ARCHIVE_PATH = os.path.join(DEST, f"backup_{timestamp}")

def sync_sandbox():
    if not os.path.exists(SRC):
        print("⚠️ No sandbox data to sync.")
        return
    os.makedirs(ARCHIVE_PATH, exist_ok=True)
    shutil.copytree(SRC, ARCHIVE_PATH, dirs_exist_ok=True)
    print(f"✅ Synced /mnt/data to {ARCHIVE_PATH}")

if __name__ == "__main__":
    sync_sandbox()
