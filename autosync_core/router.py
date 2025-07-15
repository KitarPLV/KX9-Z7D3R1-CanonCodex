from fastapi import FastAPI
from autosync_core.canonops_writer_api import router as writer_router

app = FastAPI()
app.include_router(writer_router)

@app.get("/healthz")
def health_check():
    return {"status": "ok"}
