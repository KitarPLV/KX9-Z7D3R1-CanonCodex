from autosync_core.router import app

# Ensure sync on startup (only once per boot)
try:
    from autosync_core import pull_and_sync
    pull_and_sync.pull_and_sync()
except Exception as e:
    print(f"[WARN] Startup sync failed: {e}")
