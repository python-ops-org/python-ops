
```

import os
import sys

REPO_URL = "git@github.com:infra-ops/kub-poc.git"
CLONE_DIR = "/tmp/01/kub-poc"
WORKING_BRANCH = "release/1.0"
TF_WORKING_DIRECTORY = os.path.join(CLONE_DIR, "cloud_k8s_platform/eks/infra_deployment/zero-click-eks-deployment/self-managed")

def run_cmd(cmd):
    print(f"Running: {cmd}")
    code = os.system(cmd)
    if code != 0:
        print(f"Command failed: {cmd}")
    return code

def main():
    # Clean up previous clone if it exists
    if os.path.exists(CLONE_DIR):
        run_cmd(f"rm -rf {CLONE_DIR}")
    
    # Clone the repo
    if run_cmd(f"git clone {REPO_URL} {CLONE_DIR}") != 0:
        sys.exit(1)

    # Checkout the desired branch
    os.chdir(CLONE_DIR)
    if run_cmd(f"git checkout {WORKING_BRANCH}") != 0:
        sys.exit(1)

    # List files using `ls -l`
    print("Listing files in cloned directory:")
    run_cmd("ls -l")

    os.chdir("..")

    # Run terraform plan
    print("Executing terraform plan")
    if not os.path.exists(TF_WORKING_DIRECTORY):
        print(f"Terraform directory not found: {TF_WORKING_DIRECTORY}")
        sys.exit(1)

    os.chdir(TF_WORKING_DIRECTORY)
    tf_plan = run_cmd("terraform init && terraform plan --var-file=dev.tfvars")

    if tf_plan != 0:
        print("Terraform plan failed.")
        sys.exit(1)
    else:
        print("Terraform plan is successful.")

if __name__ == '__main__':
    main()

```
