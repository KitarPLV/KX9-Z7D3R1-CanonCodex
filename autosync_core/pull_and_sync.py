import os
import requests
import json
from datetime import datetime
from autosync_core.logger import save_memory_snapshot  # ✅ Correct import

def pull_and_sync():
    gist_url = os.getenv("GIST_PAYLOAD_URL")
    if not gist_url:
        raise ValueError("GIST_PAYLOAD_URL environment variable not set")

    response = requests.get(gist_url)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch payload: {response.status_code}")

    try:
        payload = response.json()
    except ValueError as e:
        raise RuntimeError("Payload is not valid JSON") from e

    # Save snapshot
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    save_memory_snapshot(payload, timestamp)
