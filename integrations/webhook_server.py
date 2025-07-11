from flask import Flask, request, jsonify
from github import Github
import os

app = Flask(__name__)

# Load environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")
BRANCH = os.getenv("BRANCH", "main")

# Initialize GitHub API client
g = Github(GITHUB_TOKEN)
repo = g.get_repo(GITHUB_REPO)

@app.route("/codex", methods=["POST"])
def create_or_update_file():
    data = request.json
    path = data.get("path")
    content = data.get("content")
    commit_message = data.get("message", "Automated codex update")

    if not path or not content:
        return jsonify({"error": "Missing path or content"}), 400

    try:
        # Check if file exists
        try:
            contents = repo.get_contents(path, ref=BRANCH)
            repo.update_file(contents.path, commit_message, content, contents.sha, branch=BRANCH)
            action = "updated"
        except:
            repo.create_file(path, commit_message, content, branch=BRANCH)
            action = "created"

        return jsonify({"status": "success", "action": action, "path": path}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def health_check():
    return "Webhook is active."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
