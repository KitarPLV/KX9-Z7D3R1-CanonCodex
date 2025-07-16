from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from autosync_core.pull_and_sync import pull_and_sync

if __name__ == "__main__":
    print("Loaded GIST URL:", os.getenv("GIST_PAYLOAD_URL"))
    pull_and_sync()
