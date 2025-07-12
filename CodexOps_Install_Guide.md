# 🧪 CanonCodex Installation & Ops Guide

Welcome to your sealed Codex system. This guide ensures that any future operator or clone can initialize, run, and maintain this project from scratch with full automation.

---

## ✅ 1. System Overview

| Component          | Description                                   |
|-------------------|-----------------------------------------------|
| `cli.py`          | Main task launcher                            |
| `task_daemon.py`  | Watches task inbox, runs `.task.json` files   |
| `commit_snapshot.py` | Saves system memory state                 |
| `dashboard.py`    | Displays system status (live view)            |
| `cleanup.py`      | Archives/removes expired output and logs      |
| `bootstrap.py`    | Recreates required folders + `.gitkeep`       |
| `rehydrate.py`    | Reloads snapshot and daemon state             |

---

## 🔁 2. GitHub Automation

| Workflow Name             | Trigger           | Description                              |
|---------------------------|-------------------|------------------------------------------|
| `sync_and_snapshot.yml`   | Manual Dispatch   | Sync + memory snapshot                   |
| `auto_sync_snapshot.yml`  | Every 30m         | Scheduled sync + Git commit              |
| `daily_cleanup.yml`       | Daily at 3am UTC  | Cleanup logs, output, tasks              |
| `auto_repair.yml`         | Manual            | Fix missing folders, structure           |
| `daemon_trigger.yml`      | Push to `canon/*` | Queue task via webhook                   |

---

## 🛠 3. Install Checklist (Single Operator)

1. Clone repo:
   ```bash
   git clone https://github.com/your-org/KX9-Z7D3R1-CanonCodex.git
   cd KX9-Z7D3R1-CanonCodex
   ```

2. Run the environment bootstrap:
   ```bash
   python bootstrap.py
   ```

3. Start the task daemon:
   ```bash
   python task_daemon.py
   ```

4. Launch dashboard:
   ```bash
   python dashboard.py --watch 10
   ```

5. Trigger workflows (or let GitHub run them)

---

## 📦 4. Filesystem Layout

```
canoncodex_inbox/
├─ tasks/
│  ├─ archive/
│  └─ *.task.json
├─ output/
├─ logs/
├─ notes/
│  └─ system_state_snapshot.md
```

---

## 🧠 5. Rehydration

If system is reloaded or reset:
```bash
python rehydrate.py
```

---

System is now sealed, self-healing, and AI-ready.