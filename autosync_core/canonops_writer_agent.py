import json
import requests
from pathlib import Path
from datetime import datetime

API_URL = "https://kx9-z7d3r1-canoncodex.onrender.com/api/write"
AUTH_TOKEN = "canon_webhook_secret"
INBOX_DIR = Path("canoncodex_inbox/tasks")

def send_to_api(filename, content):
    try:
        res = requests.post(API_URL,
            headers={
                "Authorization": f"Bearer {AUTH_TOKEN}",
                "Content-Type": "application/json"
            },
            json={"filename": filename, "content": content}
        )
        return res.status_code, res.text
    except Exception as e:
        return 500, str(e)

def run():
    for file in INBOX_DIR.glob("*.json"):
        content = file.read_text()
        code, result = send_to_api(file.name, content)
        print(f"{file.name}: {code} -> {result}")

if __name__ == "__main__":
    run()
