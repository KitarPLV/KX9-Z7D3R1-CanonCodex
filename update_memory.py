
import os
import datetime

CANON_ROOT = "."
SUBPROJECTS = [d for d in os.listdir(CANON_ROOT) if d.startswith("pj.")]
CORE_MEMORY_PATH = "CoreMemory.md"

def get_last_modified(path):
    if not os.path.exists(path):
        return "N/A"
    timestamp = os.path.getmtime(path)
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def gather_subproject_status():
    rows = []
    for proj in SUBPROJECTS:
        task_path = os.path.join(proj, "canoncodex_inbox", "tasks")
        output_path = os.path.join(proj, "canoncodex_inbox", "output")
        status = "Unknown"
        if os.path.isdir(task_path):
            task_files = [f for f in os.listdir(task_path) if f.endswith(".json")]
            status = "In Progress" if task_files else "Idle"
        last_mod = get_last_modified(output_path)
        rows.append((proj, "TBD", status, last_mod))
    return rows

def update_core_memory():
    rows = gather_subproject_status()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    header = f"""# 🧠 CanonCodex — Core Memory

## 🧾 Project ID: KX9-Z7D3R1
**Mode**: Sealed ID-Only  
**Updated**: {now}

---

## 📚 Project Overview
CanonCodex is the cognitive brain of Project KX9-Z7D3R1. It manages state, memory, and operational logic across all sub-projects.

---

## 🧩 Sub-Project Registry

| ID        | Name / Purpose         | Status     | Last Update |
|-----------|------------------------|------------|-------------|
"""
    subproject_lines = [f"| {proj} | TBD | {status} | {last_mod} |" for proj, _, status, last_mod in rows]
    footer = """

---

## 🔁 Task Snapshot

(Automated snapshot logic can be extended here.)

---

## 🧠 Notes
- Auto-updated via update_memory.py
- Upload to GPT for context rehydration
"""
    content = header + "\n".join(subproject_lines) + footer

    with open(CORE_MEMORY_PATH, "w") as f:
        f.write(content)
    print(f"✅ CoreMemory.md updated with {len(rows)} sub-projects.")

if __name__ == "__main__":
    update_core_memory()
