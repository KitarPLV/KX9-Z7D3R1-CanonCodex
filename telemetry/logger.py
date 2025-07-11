from datetime import datetime

def log_event(event_type: str, message: str):
    with open("outputs/telemetry.log", "a") as f:
        f.write(f"[{datetime.now()}] [{event_type}] {message}\n")

def heartbeat():
    return {"status": "online", "timestamp": str(datetime.now())}