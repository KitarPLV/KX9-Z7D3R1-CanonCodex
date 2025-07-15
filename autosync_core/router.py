from fastapi import FastAPI
from autosync_core import canonops_writer_api

app = FastAPI()

# Mount CanonCodex writer and status routes
app.include_router(canonops_writer_api.router)
