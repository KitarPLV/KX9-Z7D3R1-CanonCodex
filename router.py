from fastapi import FastAPI, Request
import os
import json
from datetime import datetime
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
        try:
            print(f"🧠 Running task manually: {task_name}")
            task()
        except Exception as e:
            print(f"🔥 Manual task '{task_name}' failed:", str(e))
            return {"status": "error", "reason": str(e)}
        return {"status": "success", "task": task_name}
    return {"status": "error", "reason": "task not found"}

@app.post("/webhook")
async def github_webhook(req: Request):
    try:
        payload = await req.json()
    except:
        payload = {"note": "No payload sent or could not parse JSON."}

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = "canoncodex_inbox/logs"
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, f"github_webhook_{timestamp}.json")
    with open(log_path, "w") as f:
        json.dump(payload, f, indent=2)

    print("📡 Webhook triggered.")
    print("📦 Scanning tasks in: canoncodex_inbox/tasks")

    task_folder = "canoncodex_inbox/tasks"
    executed = []

    for fname in os.listdir(task_folder):
        if fname.endswith(".task.json"):
            full_path = os.path.join(task_folder, fname)
            print(f"🔍 Found task file: {fname}")

            try:
                with open(full_path, "r") as tf:
                    task_json = json.load(tf)
                    task_type = task_json.get("task")
                    print(f"🧩 Task type detected: {task_type}")

                    task_fn = TASK_REGISTRY.get(task_type)
                    if task_fn:
                        print(f"🚀 Executing task: {task_type}")
                        try:
                            task_fn(task_json)
                        except TypeError:
                            print("⚙️ Retrying task with no arguments")
                            task_fn()
                        print(f"✅ Task completed: {fname}")
                        executed.append(fname)
                    else:
                        print(f"❌ Task type '{task_type}' not registered.")
            except Exception as e:
                print(f"🔥 Error while processing task {fname}: {e}")

    return {
        "status": "received",
        "logged": log_path,
        "executed_tasks": executed
    }
