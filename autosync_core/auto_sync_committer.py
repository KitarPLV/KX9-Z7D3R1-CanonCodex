import subprocess

def commit_changes(message="Auto commit from Codex"):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push"], check=True)
        return "✅ Commit and push successful"
    except subprocess.CalledProcessError as e:
        return f"❌ Commit failed: {str(e)}"
