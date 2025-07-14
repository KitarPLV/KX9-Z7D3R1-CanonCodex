
import os
import datetime
from utils.logger import log_sync_event
from utils.tagger import create_git_tag
from utils.archiver import archive_folder

CANON_ROOT = "."
MASTER_MEMORY_PATH = "MasterMemory.md"
SUBPROJECTS = [d for d in os.listdir(CANON_ROOT) if d.startswith("pj.") and os.path.isdir(d)]

def extract_core_info(core_path):
    if not os.path.exists(core_path):
        return "Missing", "N/A"

    try:
        with open(core_path, "r") as f:
            lines = f.readlines()
            status = "Unknown"
            for line in lines:
                if "Status" in line and not line.startswith("#"):
                    status = line.split(":", 1)[1].strip()
                    break
            last_modified = os.path.getmtime(core_path)
            last_updated = datetime.datetime.fromtimestamp(last_modified).strftime('%Y-%m-%d %H:%M:%S')
            return status, last_updated
    except:
        return "Corrupt", "N/A"

def update_master_memory():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = []

    for proj in SUBPROJECTS:
        core_path = os.path.join(proj, "CoreMemory.md")
        status, last_updated = extract_core_info(core_path)
        rows.append((proj, "TBD", status, last_updated))

    header = f"""# 🧠 CanonCodex — Master Memory

## 📂 Project: KX9-Z7D3R1-CanonCodex
**Mode**: Sealed | Multi-Subproject  
**Updated**: {now}

---

## 📚 Summary
This master memory tracks the status and scope of all sub-projects (`pj.xxx01`, `pj.xxx02`, etc.) under Project KX9-Z7D3R1. It should be referenced during global syncs, project transitions, and GPT context rehydration.

---

## 🧩 Sub-Project Registry

| ID        | Purpose / Notes          | Status     | Last Updated        |
|-----------|--------------------------|------------|---------------------|"""

    body = "\n".join([f"| {proj} | TBD | {status} | {last_updated} |" for proj, _, status, last_updated in rows])

    footer = f"""

---

## 🔁 Last Aggregated Sync

- **Updated**: {now}
- **Files Read**: pj.xxx*/CoreMemory.md
- **System Trigger**: update_master_memory.py

---

## 🧠 Notes

- This file is auto-updated by scanning all sub-projects.
- It acts as a project-wide snapshot for external memory systems or operators.
- Uploading this to GPT rehydrates global state.
"""

    full_content = f"{header}\n{body}{footer}"

    with open(MASTER_MEMORY_PATH, "w") as f:
        f.write(full_content)

    print(f"✅ MasterMemory.md updated with {len(rows)} sub-project(s).")

    # 🔁 Log the sync
    log_sync_event("success", notes=f"{len(rows)} sub-project(s) scanned.")

    # 🏷️ Tag the sync
    create_git_tag()

    # 📦 Archive output folders (optional)
    for proj in SUBPROJECTS:
        archive_folder(os.path.join(proj, "canoncodex_inbox", "output"))

if __name__ == "__main__":
    update_master_memory()
