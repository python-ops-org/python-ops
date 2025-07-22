import os
import sys
import glob

REPO_URL = "git@github.com:python-ops-org/python-ops.git"
CLONE_DIR = "/tmp/01"
NEW_BRANCH = "release/1.0"
IMAGE = "nginx:latest"

def run_cmd(cmd):
    print(f"Running: {cmd}")
    code = os.system(cmd)
    if code != 0:
        print(f"Command failed: {cmd}")
    return code

def main():
    if os.path.exists(CLONE_DIR):
        run_cmd(f"rm -rf {CLONE_DIR}")
    
    if run_cmd(f"git clone {REPO_URL} {CLONE_DIR}") != 0:
        sys.exit(1)

    os.chdir(CLONE_DIR)
    run_cmd("ls -l")
    os.chdir("..")
    
    print("Scanning Docker image...")
    scan_result = run_cmd(f"trivy image --exit-code 1 --quiet {IMAGE}")
    
    if scan_result != 0:
        print("Image scan failed.")
        sys.exit(1)
    else:
        print("Image is clean. Pushing to ECR...")

if __name__ == '__main__':
    main()
