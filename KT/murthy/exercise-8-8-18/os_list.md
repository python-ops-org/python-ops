

```

import os
import sys
import glob

REPO_URL = "http://git-repo:test.git"
CLONE_DIR = "test_repo"
NEW_BRANCH = "auto-artifact-branch"
SONAR_PROJECT_KEY = "test-app"
SONAR_HOST_URL = "http://localhost:9000"
SONAR_TOKEN = "your-sonar-token"
NEXUS_URL = "http://nexus-host:8081/repository/maven-releases/"
NEXUS_USER = "admin"
NEXUS_PASS = "admin123"
IMAGE_NAME = "test-app"
ECR_REPO = "123456789012.dkr.ecr.ap-south-1.amazonaws.com/test-app"

def run_cmd_os(cmd):
    print(f"{cmd}")
    code = os.system(cmd)
    if code != 0:
        print(f"Command failed: {cmd}")
        sys.exit(1)

def main():
    if os.path.exists(CLONE_DIR):
        run_cmd_os(f"rm -rf {CLONE_DIR}")

    run_cmd_os(f"git clone {REPO_URL} {CLONE_DIR}")
    os.chdir(CLONE_DIR)
    run_cmd_os(f"git checkout -b {NEW_BRANCH}")
    run_cmd_os("mvn clean package")
    os.chdir("..")

    os.makedirs("artifacts", exist_ok=True)
    run_cmd_os(f"cp {CLONE_DIR}/target/*.jar artifacts/")

    # Sonar Scan
    run_cmd_os(f"""
        cd {CLONE_DIR} && \
        sonar-scanner \
        -Dsonar.projectKey={SONAR_PROJECT_KEY} \
        -Dsonar.sources=. \
        -Dsonar.host.url={SONAR_HOST_URL} \
        -Dsonar.login={SONAR_TOKEN}
    """)

    # Mocked sonar score logic
    print("Checking Sonar score...")
    score = 100  # Replace with real API check

    if score >= 99:
        print("✅ Sonar score OK. Uploading JAR to Nexus...")

        jar_files = glob.glob("artifacts/*.jar")
        if not jar_files:
            print("No JAR file found.")
            sys.exit(1)
        jar_file = jar_files[0]

        run_cmd_os(f"""
            curl -u {NEXUS_USER}:{NEXUS_PASS} \
            --upload-file {jar_file} \
            {NEXUS_URL}{os.path.basename(jar_file)}
        """)

        print("Building Docker image...")
        os.chdir(CLONE_DIR)
        run_cmd_os(f"docker build -t {IMAGE_NAME}:latest .")
        os.chdir("..")

        print("🔍 Scanning Docker image with Trivy...")
        scan_result = os.system(f"trivy image --exit-code 1 --quiet {IMAGE_NAME}:latest")
        if scan_result != 0:
            print("Trivy scan failed. Aborting push to ECR.")
            sys.exit(1)

        print("✅ Scan clean. Pushing to ECR...")
        run_cmd_os(f"aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin {ECR_REPO}")
        run_cmd_os(f"docker tag {IMAGE_NAME}:latest {ECR_REPO}:latest")
        run_cmd_os(f"docker push {ECR_REPO}:latest")

        print("🚀 Image pushed to ECR successfully.")
    else:
        print("Sonar score too low. Skipping deployment.")

if __name__ == "__main__":
    main()


```


