
#!/bin/bash

set -e

# -----------------------------------------------------------------------------
# Validate input
# -----------------------------------------------------------------------------

if [ $# -ne 1 ]; then
    echo "Usage: $0 <project-name>"
    exit 1
fi

PROJECT="$1"

if [ -d "$PROJECT" ]; then
    echo "❌ Directory '$PROJECT' already exists."
    exit 1
fi

echo "Creating FastAPI project: $PROJECT"

# -----------------------------------------------------------------------------
# Create directory structure
# -----------------------------------------------------------------------------

mkdir -p "$PROJECT"/src/{service,utils}
mkdir -p "$PROJECT"/tests
mkdir -p "$PROJECT"/templates/{prod,syst}
mkdir -p "$PROJECT"/scripts

# -----------------------------------------------------------------------------
# Create source files
# -----------------------------------------------------------------------------

touch "$PROJECT"/src/__init__.py
touch "$PROJECT"/src/run.py
touch "$PROJECT"/src/config.py

touch "$PROJECT"/src/service/__init__.py
touch "$PROJECT"/src/utils/__init__.py

# -----------------------------------------------------------------------------
# Create Kubernetes template files
# -----------------------------------------------------------------------------

for ENV in prod syst; do
    touch "$PROJECT"/templates/$ENV/deployment.yaml
    touch "$PROJECT"/templates/$ENV/service.yaml
    touch "$PROJECT"/templates/$ENV/configmap.yaml
    touch "$PROJECT"/templates/$ENV/pvc.yaml
done

# -----------------------------------------------------------------------------
# Create test placeholder
# -----------------------------------------------------------------------------

touch "$PROJECT"/tests/.gitkeep

# -----------------------------------------------------------------------------
# Create script files
# -----------------------------------------------------------------------------

touch "$PROJECT"/scripts/test.sh
chmod +x "$PROJECT"/scripts/test.sh

# -----------------------------------------------------------------------------
# Create project root files
# -----------------------------------------------------------------------------

touch "$PROJECT"/Dockerfile
touch "$PROJECT"/.dockerignore
touch "$PROJECT"/requirements.txt
touch "$PROJECT"/README.md
touch "$PROJECT"/.gitignore
touch "$PROJECT"/.env.example

# -----------------------------------------------------------------------------
# Success message
# -----------------------------------------------------------------------------

echo
echo "=========================================================="
echo "✅ FastAPI project '$PROJECT' created successfully!"
echo "=========================================================="

if command -v tree >/dev/null 2>&1; then
    echo
    tree "$PROJECT"
else
    echo
    echo "Install 'tree' to view the generated project structure."
fi
