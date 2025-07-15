import sys
import os

# Add project root to system path for reliable imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from autosync_core.pull_and_sync import pull_and_sync

if __name__ == "__main__":
    try:
        print("▶ Starting pull and sync from remote Gist...")
        pull_and_sync()
        print("✅ Sync completed successfully.")
    except Exception as e:
        print(f"❌ Sync failed: {e}")
        sys.exit(1)
