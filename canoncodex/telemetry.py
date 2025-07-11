def log_event(message):
    with open("outputs/logs/events.log", "a") as f:
        f.write(message + "\n")
    print(f"📜 Logged: {message}")
