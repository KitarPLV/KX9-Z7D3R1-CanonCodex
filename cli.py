import sys
from ops import TASK_REGISTRY

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <task_name>")
        print("Available tasks:")
        for task in TASK_REGISTRY:
            print(f"  - {task}")
        sys.exit(1)

    task_name = sys.argv[1]
    task = TASK_REGISTRY.get(task_name)

    if task:
        print(f"Running task: {task_name}")
        task()
    else:
        print(f"Task '{task_name}' not found in registry.")

if __name__ == "__main__":
    main()