
# CanonCodex GitHub Webhook Event Handler
# Connects GitHub push/PR/issue events to CanonCodex task modules

import os
import json
from scripts.dispatcher import dispatch

TASKS_DIR = os.path.join(os.path.dirname(__file__), "..", "tasks")
WEBHOOK_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs", "webhooks")
os.makedirs(TASKS_DIR, exist_ok=True)

def handle_push_event(data):
    commit_msgs = [c["message"] for c in data.get("commits", [])]
    for msg in commit_msgs:
        create_task_file(f"push_{hash(msg)}.txt", msg)

def handle_pr_event(data):
    title = data.get("pull_request", {}).get("title", "PR Task")
    body = data.get("pull_request", {}).get("body", "")
    create_task_file(f"pr_{data.get('number')}.txt", f"{title}\n{body}")

def handle_issue_event(data):
    action = data.get("action", "")
    if action in ["opened", "reopened"]:
        issue = data.get("issue", {})
        title = issue.get("title", "")
        body = issue.get("body", "")
        create_task_file(f"issue_{issue.get('number')}.txt", f"{title}\n{body}")

def create_task_file(filename, content):
    task_path = os.path.join(TASKS_DIR, filename)
    with open(task_path, "w") as f:
        f.write(content)

def route_event(event_type, data):
    if event_type == "push":
        handle_push_event(data)
    elif event_type == "pull_request":
        handle_pr_event(data)
    elif event_type == "issues":
        handle_issue_event(data)
