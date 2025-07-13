# CanonCodex

This repository is managed by an AI Codex system. It uses automated workflows, GitHub Actions, and Render Web Services.

## AI-Aware Instructions

- `.canonrc` defines the sealed Codex configuration
- CanonOps tasks are located in `canoncodex_inbox/tasks/`
- SubCodex routes are registered in `.canonrc`
- System is auto-synced every hour with GitHub Actions
- Render deploys are triggered by push or webhook

## Manual Intervention

If something fails:
1. Pull the latest changes: `git pull --rebase`
2. Retry pushing: `git push origin main`
3. Trigger webhook manually (optional)

## Status

All tasks and changes are recorded in `canoncodex_inbox/logs/`
