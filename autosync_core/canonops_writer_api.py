from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
import os
from datetime import datetime
from autosync_core.memory_to_file import save_memory_snapshot

router = APIRouter()

WEBHOOK_SECRET = os.getenv("CANON_WEBHOOK_SECRET", "canon_webhook_secret")
SAVE_DIR = "canoncodex_inbox"
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

    log_sync(filename)
    save_memory_snapshot({
        "event": "file_written",
        "filename": filename,
        "timestamp": datetime.utcnow().isoformat()
    })

    return {"status": "success", "message": f"File '{filename}' saved."}

@router.get("/status/files")
def list_synced_files():
    inbox_files = [f.name for f in Path("canoncodex_inbox").glob("*")]
    memory_logs = [f.name for f in Path("memory_logs").glob("*")] if Path("memory_logs").exists() else []
    queue_log = Path("queue_log.txt").read_text().splitlines() if Path("queue_log.txt").exists() else []

    return {
        "inbox_files": inbox_files,
        "memory_logs": memory_logs,
        "queue_log": queue_log
    }

@router.get("/download/{filename}")
def download_file(filename: str):
    filepath = Path("canoncodex_inbox") / filename
    if not filepath.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(str(filepath))
