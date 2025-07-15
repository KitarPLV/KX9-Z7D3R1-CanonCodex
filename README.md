# CanonCodex 2.0

This is the final, complete, Git- and Render-ready version of the autonomous CanonCodex system. It includes autosave, webhook support, autosync GitHub workflow, Render deploy config, and more.

## Structure

- `autosync_core/`: Core FastAPI server and Codex modules
- `.github/workflows/`: GitHub Action for autosync
- `render.yaml`: Render.com deploy configuration
- `.canonrc`: Codex metadata
- `requirements.txt`: Python dependencies

## Deployment

- Push to GitHub
- Connect to Render with `main` branch and auto-deploy enabled
- Service URL: `https://your-subdomain.onrender.com/healthz`
