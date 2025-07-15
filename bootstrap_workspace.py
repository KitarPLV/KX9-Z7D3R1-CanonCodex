import os
import subprocess

def is_git_repo():
    return os.path.isdir(".git")

def bootstrap_workspace():
    if not is_git_repo():
        print("Workspace not initialized. Cloning...")
        repo_url = "https://github.com/KitarPLV/KX9-Z7D3R1-CanonCodex.git"
        subprocess.run(["git", "clone", repo_url])
        os.chdir("KX9-Z7D3R1-CanonCodex")
        print("Workspace bootstrapped.")
    else:
        print("Git repo already present.")

if __name__ == "__main__":
    bootstrap_workspace()
