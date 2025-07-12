import os
import subprocess

def check_structure():
    print("🔍 Checking CanonCodex directory structure...")
    required_dirs = [
        "canoncodex_inbox/output",
        "canoncodex_inbox/logs",
        "canoncodex_inbox/tasks",
        "canoncodex_inbox/notes",
        "core",
        "ops"
    ]
    for d in required_dirs:
        if not os.path.exists(d):
            os.makedirs(d, exist_ok=True)
            print(f"✅ Created missing directory: {d}")
        else:
            print(f"✅ Found: {d}")

def check_files():
    print("\n📄 Checking key system files...")
    required_files = [
        "cli.py",
        "rehydrate.py",
        "router.py",
        "canoncodex_inbox/notes/system_state_snapshot.md"
    ]
    for f in required_files:
        if os.path.exists(f):
            print(f"✅ {f}")
        else:
            print(f"❌ MISSING: {f}")

def git_status():
    print("\n🔁 Checking Git sync status...")
    try:
        subprocess.run(["git", "status"], check=True)
    except subprocess.CalledProcessError as e:
        print("❌ Git status failed:", e)

def run():
    print("🚀 Bootstrapping CanonCodex environment...")
    check_structure()
    check_files()
    git_status()
    print("\n✅ Bootstrap complete. System is ready.")

if __name__ == "__main__":
    run()