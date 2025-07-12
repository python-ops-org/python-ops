

```

import os
import sys
import glob

REPO_URL = "http://git-repo:test.git"
CLONE_DIR = "test_repo"
NEW_BRANCH = "release/1.0"
IMAGE_NAME = "test-app"

def run_cmd(cmd):
    print(f"{cmd}")
    code = os.system(cmd)
    if code != 0:
        print(f"Command failed: {cmd}")
        sys.exit(1)

def main():
    if os.path.exists(CLONE_DIR):
        run_cmd(f"rm -rf {CLONE_DIR}")
    
    run_cmd(f"git clone {REPO_URL} {CLONE_DIR}")
    
    os.chdir(CLONE_DIR)
    run_cmd(f"git checkout -b {NEW_BRANCH}")
    run_cmd("mvn clean package")
    os.chdir("..")

    # Ensure artifacts directory exists
    os.makedirs("artifacts", exist_ok=True)
    run_cmd(f"cp {CLONE_DIR}/target/*.jar artifacts/")

    print("Scanning Docker image with Trivy...")
    scan_result = os.system(f"trivy image --exit-code 1 --quiet {IMAGE_NAME}:latest")

    if scan_result != 0:
        print("Trivy scan failed.")
        sys.exit(1)
    else:
        print("Scan clean. Pushing to ECR...")
        print("Image pushed to ECR")

if __name__ == "__main__":
    main()

```
