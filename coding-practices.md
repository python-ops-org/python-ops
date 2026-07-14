# Enterprise Python Development Standards & Best Practices

> **Version:** 2.1  
> **Audience:** Python Developers, DevOps Engineers, SREs, and Platform Engineers

---

# Table of Contents

1. Development Environment
2. Project Structure
3. Dependency Management
4. Coding Standards
5. Code Quality
6. Testing
7. Logging & Error Handling
8. Security
9. Docker Best Practices
10. Kubernetes Best Practices
11. Git & Pull Request Best Practices
12. CI/CD Pipeline
13. AI-Assisted Development
14. YAML & JSON Utilities
15. Quick Reference

---

# 1. Development Environment

## Recommended IDE

- Visual Studio Code

### Recommended Extensions

| Extension | Purpose |
|-----------|---------|
| Python | Python language support |
| Pylance | IntelliSense and type checking |
| Flake8 | PEP 8 linting |
| Black Formatter | Code formatting |
| GitLens | Git history and blame |
| Docker | Docker integration |
| Kubernetes | Kubernetes manifest support |
| YAML | YAML editing |
| Error Lens | Display errors inline |
| GitHub Copilot | AI coding assistant |
| AWS Toolkit | AWS integration |
| Terraform | Infrastructure as Code |
| SonarLint | Static code analysis |

---

## Create a Virtual Environment

```bash
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

pip freeze > requirements.txt
```

---

# 2. Standard Project Structure

```text
project/
├── src/
├── tests/
├── docs/
├── scripts/
├── templates/
├── configs/
├── .github/
├── .vscode/
├── Dockerfile
├── .dockerignore
├── .gitignore
├── pyproject.toml
├── Makefile
├── README.md
└── requirements.txt
```

---

# 3. Dependency Management

| Recommendation | Best Practice |
|---------------|---------------|
| Dependency File | requirements.txt |
| Project Configuration | pyproject.toml |
| Pin Package Versions | Yes |
| Remove Unused Packages | Regularly |

---

# 4. Coding Standards

Follow these best practices:

- Follow **PEP 8**
- Use meaningful variable and function names
- Add type hints
- Write docstrings
- Prefer f-strings
- Keep functions small and focused

Example:

```python
def create_user(name: str) -> bool:
    return True
```

---

# 5. Code Quality

## Recommended Tools

| Tool | Purpose |
|------|---------|
| Flake8 | PEP 8 linting and code quality |
| Black | Code formatting |
| mypy | Static type checking |
| Bandit | Security scanning |
| pip-audit | Dependency vulnerability scanning |

### Run Code Quality Checks

```bash
flake8 .

black .

mypy .

bandit -r .

pip-audit
```

---

## Configure Flake8

Create a `.flake8` file:

```ini
[flake8]
max-line-length = 100
ignore = E203,W503
exclude =
    .git,
    __pycache__,
    .venv,
    build,
    dist
```

---

## Pre-commit Hooks

```bash
pip install pre-commit

pre-commit install
```

---

# 6. Testing

Use **pytest** for unit testing.

```bash
pytest

pytest -v

pytest --cov=src tests/
```

Target **80% or higher** code coverage.

---

# 7. Logging & Error Handling

Use the Python logging module.

```python
import logging

logger = logging.getLogger(__name__)
```

Best Practices:

- Never use `print()` in production code.
- Log meaningful messages.
- Handle expected exceptions gracefully.

---

# 8. Security

Best Practices

- Never hardcode secrets.
- Use AWS Secrets Manager.
- Use Kubernetes Secrets.
- Scan dependencies regularly.
- Scan Docker images before deployment.

Commands:

```bash
bandit -r .

pip-audit

trivy image my-app:latest
```

---

# 9. Docker Best Practices

| Best Practice | Description |
|--------------|-------------|
| Use `python:3.12-slim` | Reduce image size |
| Multi-stage Build | Smaller production images |
| Run as Non-root User | Improve security |
| `.dockerignore` | Reduce build context |
| BuildKit | Faster builds |
| Docker Scout | Image recommendations |
| Dive | Analyze image layers |

Build Example

```bash
DOCKER_BUILDKIT=1 docker build -t my-app .
```

Cleanup Commands

```bash
docker builder prune -a

docker image prune -a

docker system prune -a --volumes
```

---

# 10. Kubernetes Best Practices

Best Practices

- Define CPU and memory requests & limits.
- Configure readiness and liveness probes.
- Store configuration in ConfigMaps.
- Store secrets in Kubernetes Secrets.
- Validate manifests before deployment.

Commands

```bash
kubectl apply --dry-run=client -f deployment.yaml

helm lint charts/my-chart
```

---

# 11. Git & Pull Request Best Practices

| Practice | Recommendation |
|----------|----------------|
| Branch Strategy | Use feature branches |
| Commit Messages | Keep them meaningful |
| Pull Requests | One feature per PR |
| Code Reviews | Mandatory before merge |

---

# 12. CI/CD Pipeline

```text
Developer
      │
      ▼
Pre-commit
      ▼
Flake8
      ▼
Black
      ▼
mypy
      ▼
pytest
      ▼
Bandit
      ▼
pip-audit
      ▼
Docker Build
      ▼
Trivy
      ▼
Helm Lint
      ▼
Deploy
```

---

# 13. AI-Assisted Development

Recommended Tools

- GitHub Copilot
- Amazon Q
- Cursor
- Qodo

Use AI for:

- Unit test generation
- Documentation
- Code review
- Refactoring

> **Always review AI-generated code before committing it to the repository.**

---

# 14. YAML & JSON Utilities

## YAML

| Tool | Purpose |
|------|---------|
| yamllint | Validate YAML syntax |
| yq | Read, update, and process YAML |

Commands

```bash
yamllint values.yaml

yq '.image.tag' values.yaml

yq '.replicaCount = 3' values.yaml
```

---

## JSON

| Tool | Purpose |
|------|---------|
| jq | Beautify, validate, and query JSON |

Commands

```bash
jq '.' data.json

jq '.name' data.json

jq empty data.json
```

---

# 15. Quick Reference

| Activity | Command |
|-----------|---------|
| Create Virtual Environment | `python3 -m venv .venv` |
| Activate Virtual Environment | `source .venv/bin/activate` |
| Install Packages | `pip install -r requirements.txt` |
| Freeze Packages | `pip freeze > requirements.txt` |
| Format Code | `black .` |
| Lint Code | `flake8 .` |
| Type Check | `mypy .` |
| Run Tests | `pytest` |
| Test Coverage | `pytest --cov=src tests/` |
| Security Scan | `bandit -r .` |
| Dependency Scan | `pip-audit` |
| Docker Build | `docker build -t my-app .` |
| Docker Image Scan | `trivy image my-app` |
| Validate YAML | `yamllint values.yaml` |
| Process YAML | `yq '.image.tag' values.yaml` |
| Beautify JSON | `jq '.' data.json` |
| Validate JSON | `jq empty data.json` |
| Helm Lint | `helm lint charts/my-chart` |
| Kubernetes Dry Run | `kubectl apply --dry-run=client -f deployment.yaml` |

---

# Overall Assessment

Following these standards helps teams achieve:

- Consistent code quality
- Better maintainability
- Improved security
- Higher performance
- Better scalability
- Production-ready applications
- Enterprise-grade software development practices
