
def demo_task(**kwargs):
    return f"✅ Demo task executed with: {kwargs}"

TASK_REGISTRY = {
    "DEMO": demo_task
}
