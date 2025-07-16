from fastapi import FastAPI, Request, HTTPException
from autosync_core import canonops_writer_api
from pathlib import Path
import json

app = FastAPI()
app.include_router(canonops_writer_api.router)

@app.get("/status/files")
def status():
    return {
        "inbox_files": [f.name for f in Path("canoncodex_inbox/tasks").glob("*")],
        "memory_logs": [f.name for f in Path("memory_logs").glob("*.json")],
        "queue_log": Path("queue_log.txt").read_text().splitlines()[-10:] if Path("queue_log.txt").exists() else []
    }
