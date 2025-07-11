from fastapi import FastAPI
from ops import TASK_REGISTRY

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "OK"}

@app.get("/tasks")
def list_tasks():
    return {"available_tasks": list(TASK_REGISTRY.keys())}

@app.get("/run/{task_name}")
def run_task(task_name: str):
    task = TASK_REGISTRY.get(task_name)
    if task:
        task()
        return {"status": "success", "task": task_name}
    return {"status": "error", "reason": "task not found"}
