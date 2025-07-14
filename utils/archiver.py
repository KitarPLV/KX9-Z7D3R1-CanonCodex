
import shutil
import os
import datetime

def archive_folder(src, archive_root="archives"):
    if not os.path.exists(src):
        return
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    archive_path = os.path.join(archive_root, f"{os.path.basename(src)}-{timestamp}")
    os.makedirs(archive_root, exist_ok=True)
    shutil.move(src, archive_path)
    print(f"📦 Archived {src} -> {archive_path}")
