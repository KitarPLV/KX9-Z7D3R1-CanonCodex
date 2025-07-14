from github import Github
import os

# 🔐 Replace with your actual GitHub token or use environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "your_token_here")
REPO_NAME = "KitarPLV/KX9-Z7D3R1-CanonCodex"
BRANCH = "main"

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)
branch = repo.get_branch(BRANCH)

def push_file(file_path, repo_path, commit_message):
    with open(file_path, "r") as f:
        content = f.read()

    try:
        contents = repo.get_contents(repo_path, ref=branch.name)
        repo.update_file(contents.path, commit_message, content, contents.sha, branch=branch.name)
        print(f"✅ Updated {repo_path}")
    except:
        repo.create_file(repo_path, commit_message, content, branch=branch.name)
        print(f"✅ Created {repo_path}")

# 🧪 Example usage
if __name__ == "__main__":
    local_file = "task_daemon.py"
    remote_path = "canoncodex_inbox/tasks/task_daemon.py"
    push_file(local_file, remote_path, "feat: add task daemon")