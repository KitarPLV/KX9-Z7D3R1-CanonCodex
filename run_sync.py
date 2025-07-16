import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from autosync_core.pull_and_sync import pull_and_sync
if __name__ == "__main__":
    pull_and_sync()
