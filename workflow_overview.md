# 🧪 CanonCodex Workflow Overview

This document outlines the automated GitHub Actions workflows active in this sealed canon environment.

---

## ✅ Workflows Summary

### 1. 🔁 `sync_and_snapshot.yml`
**Trigger:** `push` to `main`  
**Purpose:**  
- Runs `sync_agent`  
- Updates the `system_state_snapshot.md`  
- Auto-commits and pushes result

---

### 2. 🧹 `daily_cleanup.yml`
**Trigger:** `cron: 0 3 * * *` (3:00 AM UTC daily)  
**Purpose:**  
- Runs `cleanup.py` to archive/remove expired:
  - Logs
  - `.task.json`
  - Old `.done` or stale files

---

### 3. 🛠️ `auto_repair.yml`
**Trigger:** Manual (from GitHub Actions UI)  
**Purpose:**  
- Runs `bootstrap.py`  
- Recreates missing folders, `.gitkeep` files, or system layout

---

### 4. 📡 `daemon_trigger.yml`
**Trigger:** `push` to `canon/auto` branch  
**Purpose:**  
- Calls webhook (`/webhook`) on Render instance  
- Intended for triggering `sync_agent` or task queue on auto-updates

---

## 📁 Workflow Location
All workflows are stored in:

```
.github/workflows/
```

These are installed automatically as part of system setup.

---

## 💡 Tips
- Use `workflow_dispatch` on GitHub to trigger repairs manually
- View logs and execution in the GitHub Actions tab
- Keep `.canonrc` updated with behavior flags

---

🧠 You are now running a fully autonomous, GitHub-driven sealed task network.