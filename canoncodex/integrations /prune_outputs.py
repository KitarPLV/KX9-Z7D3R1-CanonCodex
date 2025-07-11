import os
import shutil


def prune_old_outputs(output_dir, keep_latest=5):
    print("🧹 Pruning old outputs...")
    files = sorted(
        [f for f in os.listdir(output_dir) if f.endswith(".md")],
        key=lambda f: os.path.getmtime(os.path.join(output_dir, f)),
        reverse=True,
    )
    for old_file in files[keep_latest:]:
        path = os.path.join(output_dir, old_file)
        os.remove(path)
        print(f"🗑️ Removed old output: {old_file}")
