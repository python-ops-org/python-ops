

```

import subprocess
import sys

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

def run_cmd(cmd):
    print(f"🛠️ {cmd}")
    result = subprocess.run(cmd, shell=True, executable="/bin/bash", capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ {result.stderr.strip()}")
        sys.exit(1)
    if result.stdout.strip():
        print(result.stdout.strip())
    return result.stdout.strip()

def main():
    run_cmd(f"if [ -d {CLONE_DIR} ]; then rm -rf {CLONE_DIR}; fi")
    run_cmd(f"git clone {REPO_URL} {CLONE_DIR}")
    run_cmd(f"cd {CLONE_DIR} && git checkout -b {NEW_BRANCH}")
    run_cmd(f"cd {CLONE_DIR} && mvn clean package")
    run_cmd("mkdir -p artifacts")
    run_cmd(f"cd {CLONE_DIR}/target && mv *.jar ../../artifacts")

    # Sonar Scan
    run_cmd(f"""
        cd {CLONE_DIR} && \
        sonar-scanner \
        -Dsonar.projectKey={SONAR_PROJECT_KEY} \
        -Dsonar.sources=. \
        -Dsonar.host.url={SONAR_HOST_URL} \
        -Dsonar.login={SONAR_TOKEN}
    """)

    # Get Sonar Quality Gate result (mocked here)
    print("📊 Checking Sonar score...")
    score = 100  # In real case, use Web API to fetch actual quality score

    if score >= 99:
        print("✅ Sonar score OK. Uploading JAR to Nexus...")

        jar_file = run_cmd("ls artifacts/*.jar")
        run_cmd(f"""
            curl -u {NEXUS_USER}:{NEXUS_PASS} \
            --upload-file {jar_file} \
            {NEXUS_URL}$(basename {jar_file})
        """)

        print("📦 Building Docker image...")
        run_cmd(f"cd {CLONE_DIR} && docker build -t {IMAGE_NAME}:latest .")

        print("🔍 Scanning Docker image with Trivy...")
        trivy_result = run_cmd(f"trivy image --exit-code 1 --quiet {IMAGE_NAME}:latest || echo 'scan_fail'")

        if "scan_fail" in trivy_result:
            print("❌ Trivy scan failed. Aborting push to ECR.")
            sys.exit(1)

        print("✅ Scan clean. Pushing to ECR...")

        run_cmd("aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin {}".format(ECR_REPO))
        run_cmd(f"docker tag {IMAGE_NAME}:latest {ECR_REPO}:latest")
        run_cmd(f"docker push {ECR_REPO}:latest")

        print("🚀 Image pushed to ECR successfully.")
    else:
        print("❌ Sonar score too low. Skipping deployment.")

if __name__ == "__main__":
    main()


```
