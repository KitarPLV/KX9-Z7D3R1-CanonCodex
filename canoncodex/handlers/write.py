import os

def handle(task_text):
    print("✍️  Handling WRITE task")
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    result = f"# Documentation\n\nThis is a placeholder documentation for the task:\n\n{task_text.strip()}"
    output_file = os.path.join(output_dir, "write_output_test.md")
    with open(output_file, "w") as f:
        f.write(result)
    print(f"✅ Output written to {output_file}")
