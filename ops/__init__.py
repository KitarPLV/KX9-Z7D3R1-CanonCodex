TASK_REGISTRY = {}

def register(name):
    def wrapper(func):
        TASK_REGISTRY[name] = func
        return func
    return wrapper

# Auto-import task modules to register them
from core.sync_agent import sync_agent
from ops.convert_codex import convert_codex
