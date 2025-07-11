# 🧠 CanonCodex Setup & Usage Guide

Welcome to the KX9-Z7D3R1 CanonCodex sealed task system. This document outlines everything needed to run, extend, and automate your persistent codex operations.

---

## 📦 Project Structure

```
/core/                      ← Core task implementations
/ops/                       ← Auxiliary tasks and registries
/canoncodex_inbox/
├── logs/                   ← Optional runtime logs
├── output/                 ← Task result files
├── tasks/                  ← Task blueprints or queued dispatches
├── notes/                  ← Canon metadata + state snapshots
cli.py                      ← Main task runner
rehydrate.py                ← Memory rehydration script
router.py                   ← FastAPI routes for API + Webhook
```

---

## 🚀 Running Tasks

Use the `cli.py` interface:

```bash
python cli.py <task_name> [--write-to <output_path>]
```

✅ Example:
```bash
python cli.py sync_agent --write-to canoncodex_inbox/output/
```

This will:
- Run the task
- Save a log in `/output/`
- Auto-update the memory snapshot
- Auto-commit + push the snapshot to Git

---

## 🔁 Memory Rehydration

After session or Codespace resets, restore system context by running:

```bash
python rehydrate.py
```

This will read from:

```
canoncodex_inbox/notes/system_state_snapshot.md
```

And print all remembered task states and runtime context.

---

## 🌐 API Usage (FastAPI)

Start your app with:
```bash
uvicorn router:app --host 0.0.0.0 --port 10000
```

### Endpoints:
| Method | Path          | Description               |
|--------|---------------|---------------------------|
| GET    | /ping         | Health check              |
| GET    | /tasks        | List all tasks            |
| GET    | /run/{task}   | Run a task via API        |
| POST   | /webhook      | GitHub webhook receiver   |

---

## 🔒 Persistence Notes

All system files are stored under `/workspaces/KX9-Z7D3R1-CanonCodex/` and committed to Git.

Avoid `/mnt/data/` — this is a temporary memory.

---

## 📥 GitHub Snapshot Auto-Sync

Every CLI task automatically:
1. Updates the system memory file
2. Commits and pushes to your repository

---

## ✅ Tips
- New tasks go in `/core/` or `/ops/`, and auto-register
- All metadata/notes should be stored in `/canoncodex_inbox/notes/`
- Outputs should use the `--write-to` flag to go to `/output/`
- You can extend snapshot logging to track user input or timeline

---

🔐 You are operating in sealed persistent mode. Task history is preserved. Logs are live. Codex is online.