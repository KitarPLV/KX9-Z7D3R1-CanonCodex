from dotenv import load_dotenv
load_dotenv()

import os, requests
from datetime import datetime
from autosync_core.logger import save_memory_snapshot

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

    if not isinstance(payload, list):
        raise ValueError("Expected payload to be a list of file descriptors")

    os.makedirs("canoncodex_inbox", exist_ok=True)

    for item in payload:
        filename = item.get("filename")
        content = item.get("content")
        if filename and content:
            with open(os.path.join("canoncodex_inbox", filename), "w", encoding="utf-8") as f:
                f.write(content)

    save_memory_snapshot(tag="pull")
