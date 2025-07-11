# 🧠 CanonCodex System State Snapshot
**Snapshot Time**: 2025-07-11 18:44:42

---

## ✅ Active Components
- CLI: `cli.py` supports `--write-to`
- FastAPI: `router.py` supports `/ping`, `/tasks`, `/run/{task}`, `/webhook`
- Task Registry: Auto-imports from `core/` and `ops/`
- Webhook Listener: ✅ Enabled
- Output Folder: `canoncodex_inbox/output/`
- Logs Folder: `canoncodex_inbox/logs/`
- Tasks Folder: `canoncodex_inbox/tasks/`
- Notes Folder: `canoncodex_inbox/notes/`

---

## 🧪 Recent Commands
- `python cli.py sync_agent --write-to canoncodex_inbox/output/`

---

## 📂 Filesystem Confirmed
- ✅ `/core/sync_agent.py`
- ✅ `/ops/convert_codex.py`
- ✅ `/ops/__init__.py` (with task registration)
- ✅ `/canoncodex_inbox/` structure present and active

---

## 🚀 Deployment Config
- Render deployed via `uvicorn router:app --host 0.0.0.0 --port 10000`
- GitHub Webhook active to `/webhook`

---

To resume task memory, read this file and rehydrate logic accordingly.
