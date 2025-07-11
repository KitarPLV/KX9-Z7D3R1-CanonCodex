#!/usr/bin/env python3
import subprocess
import os
from datetime import datetime

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
    else:
        print(f"✅ Success: {result.stdout.strip()}")
    return result

def git_commit_push(message="Automated update from CanonCodex agent"):
    print("\n📦 Staging all changes...")
    run("git add .")

    print("📝 Committing changes...")
    commit_message = f"{message} @ {datetime.utcnow().isoformat()} UTC"
    run(f"git commit -m \"{commit_message}\"")

    print("🚀 Pushing to GitHub...")
    run("git push origin main")

if __name__ == "__main__":
    git_commit_push()
