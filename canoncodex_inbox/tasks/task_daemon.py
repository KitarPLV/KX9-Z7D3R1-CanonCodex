import datetime

def run_task():
    now = datetime.datetime.now().isoformat()
    print(f"[Task Daemon] Task executed at {now}")

if __name__ == "__main__":
    run_task()
