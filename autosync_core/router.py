from fastapi import FastAPI
from autosync_core import canonops_writer_api

app = FastAPI()

# Mount CanonCodex writer and status routes
app.include_router(canonops_writer_api.router)

# Trigger sync from remote source on startup
try:
    from autosync_core import pull_and_sync
    pull_and_sync.pull_and_sync()
except Exception as e:
    print(f"[ROUTER] Startup sync failed: {e}")
