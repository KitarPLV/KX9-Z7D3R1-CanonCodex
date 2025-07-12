import os
import shutil
import time

ROOT_DIR = "canoncodex_inbox"
ARCHIVE_SUBDIR = "archive"
EXPIRATION_SECONDS = 60 * 60 * 24  # 1 day

def is_expired(file_path):
    return time.time() - os.path.getmtime(file_path) > EXPIRATION_SECONDS

def cleanup_folder(folder):
    print(f"🧹 Scanning: {folder}")
    archive_dir = os.path.join(folder, ARCHIVE_SUBDIR)
    os.makedirs(archive_dir, exist_ok=True)

    for fname in os.listdir(folder):
        fpath = os.path.join(folder, fname)
        if not os.path.isfile(fpath) or fname.endswith(".done") or fname.endswith(".keep"):
            continue
        if is_expired(fpath):
            print(f"📦 Archiving expired file: {fname}")
            shutil.move(fpath, os.path.join(archive_dir, fname))

def main():
    for subdir in ["tasks", "output", "logs"]:
        cleanup_folder(os.path.join(ROOT_DIR, subdir))

if __name__ == "__main__":
    main()
