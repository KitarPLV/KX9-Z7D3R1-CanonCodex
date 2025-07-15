from fastapi import APIRouter, Request, HTTPException, status
from pydantic import BaseModel
from pathlib import Path
import os
from datetime import datetime
from autosync_core.memory_to_file import save_memory_snapshot

router = APIRouter()

# Secret key for simple token auth
WEBHOOK_SECRET = os.getenv("CANON_WEBHOOK_SECRET", "canon_webhook_secret")
SAVE_DIR = "canoncodex_inbox"

# Ensure inbox directory exists
Path(SAVE_DIR).mkdir(parents=True, exist_ok=True)

class FilePayload(BaseModel):
    filename: str
    content: str

def log_sync(filename: str):
    with open("queue_log.txt", "a") as log:
        log.write(f"[SYNC] {filename} at {datetime.utcnow().isoformat()}\n")

@router.post("/api/write")
async def write_file(request: Request, payload: FilePayload):
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != f"Bearer {WEBHOOK_SECRET}":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    filename = payload.filename
    filepath = Path(SAVE_DIR) / filename

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(payload.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to write file: {e}")

    # Log sync to queue
    log_sync(filename)

    # Save memory snapshot
    save_memory_snapshot({
        "event": "file_written",
        "filename": filename,
        "timestamp": datetime.utcnow().isoformat()
    })

    return {"status": "success", "message": f"File '{filename}' saved."}
