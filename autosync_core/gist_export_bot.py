import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def export_to_gist(content: str, filename: str, description: str = "CanonCodex export", gist_id=None):
    token = os.getenv("GH_TOKEN")
    if not token:
        raise EnvironmentError("Missing GH_TOKEN")

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    payload = {
        "description": description,
        "public": False,
        "files": {
            filename: {
                "content": content
            }
        }
    }

    url = f"https://api.github.com/gists/{gist_id}" if gist_id else "https://api.github.com/gists"
    method = requests.patch if gist_id else requests.post

    response = method(url, headers=headers, json=payload)
    if response.status_code in [200, 201]:
        print("[EXPORT] Gist updated:", response.json()["html_url"])
        return response.json()["html_url"]
    else:
        raise RuntimeError(f"Failed to export to Gist: {response.status_code} - {response.text}")
