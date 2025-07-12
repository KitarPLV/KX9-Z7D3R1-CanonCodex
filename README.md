# KX9-Z7D3R1-CanonCodex

This repository contains a small Flask server that listens for webhook events and updates files in a GitHub repository. The server requires a few environment variables to run:

- `GITHUB_TOKEN` – personal access token with permission to commit to the target repository
- `GITHUB_REPO` – repository name in the form `owner/repo`
- `BRANCH` – branch to commit to (defaults to `main`)

To start the server:

```bash
pip install -r requirements.txt
python webhook_server.py
```

It exposes a `/codex` endpoint to create or update files and a simple `/` health check.
