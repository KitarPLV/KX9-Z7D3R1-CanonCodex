from datetime import datetime

def log_event(message, log_file="queue_log.txt"):
    timestamp = datetime.utcnow().isoformat()
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
