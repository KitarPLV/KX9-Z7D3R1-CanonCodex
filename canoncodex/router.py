def route_task(task_path):
    print(f"📦 Routed task from: {task_path}")
    with open(task_path, "r") as f:
        lines = f.readlines()
    task_type = ""
    for line in lines:
        if line.startswith("TASK_TYPE:"):
            task_type = line.split(":", 1)[1].strip().lower()
            break
    if task_type == "write":
        from canoncodex.handlers.write import dispatch
        dispatch(task_path)
    else:
        raise ValueError(f"Unsupported TASK_TYPE: {task_type}")
