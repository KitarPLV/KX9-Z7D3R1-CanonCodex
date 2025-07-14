
import os
import shutil
import sys

TEMPLATE_FILES = [
    "task_daemon.py",
    "update_memory.py",
    "git_push.sh",
    "github_push.py"
]

def create_subproject(project_id):
    if not project_id.startswith("pj."):
        print("❌ Project ID must start with 'pj.'")
        return

    if os.path.exists(project_id):
        print(f"❌ Sub-project {project_id} already exists.")
        return

    # Create base folders
    os.makedirs(os.path.join(project_id, "canoncodex_inbox", "tasks"), exist_ok=True)
    os.makedirs(os.path.join(project_id, "canoncodex_inbox", "output"), exist_ok=True)

    # Copy template files if available in current dir
    for fname in TEMPLATE_FILES:
        if os.path.exists(fname):
            shutil.copy(fname, os.path.join(project_id, fname))
        else:
            print(f"⚠️  Template file not found: {fname}")

    # Create blank CoreMemory.md
    core_memory_path = os.path.join(project_id, "CoreMemory.md")
    with open(core_memory_path, "w") as f:
        f.write(f"# 🧠 {project_id} — Local Core Memory\n\nStatus: Initialized\n")

    print(f"✅ Sub-project {project_id} created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_subproject.py pj.xxxID")
    else:
        create_subproject(sys.argv[1])
