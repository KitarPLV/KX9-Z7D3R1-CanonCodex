# Changelog

## [v1.0.0] - 2025-07-14

### ✨ Features
- CanonCodex automation for memory system integration
- Sub-project task daemon execution pipeline
- `create_subproject.py` bootstrapping tool
- Auto-update `MasterMemory.md` from subprojects
- GitHub Action: `auto_update_master_memory.yml`

### 🛠 Fixes
- Resolved Python module import paths (`ops`, `utils`)
- Fixed `.gitignore` to allow versioning `dashboard.html`
- Git push conflict resolution and rebase handling
- Corrected file generation paths (e.g., `docs/dashboard.html`)

### 🧰 Utilities
- `logger.py`, `tagger.py`, `archiver.py` (modular sync tools)
- `view_sync_log.py`: CLI viewer for sync logs
- `generate_dashboard.py`: creates `dashboard.html` for subproject status

### 🔄 GitHub Workflow Improvements
- Auto-tagging and archiving of snapshots
- GitHub Pages-compatible `docs/dashboard.html` generation
- Safe push policies with commit validation

---
