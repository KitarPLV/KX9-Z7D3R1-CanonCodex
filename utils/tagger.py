
import subprocess
import datetime

def create_git_tag(prefix="snapshot"):
    tag = f"{prefix}-{datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S')}"
    try:
        subprocess.run(["git", "tag", tag], check=True)
        subprocess.run(["git", "push", "origin", tag], check=True)
        print(f"✅ Git tag created and pushed: {tag}")
    except Exception as e:
        print(f"❌ Failed to tag: {e}")
