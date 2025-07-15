from fastapi import FastAPI
from autosync_core.canonops_writer_api import router as writer_router

app = FastAPI()
app.include_router(writer_router)

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("autosync_core.router:app", host="0.0.0.0", port=10000, reload=True)
