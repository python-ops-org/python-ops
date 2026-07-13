# Enterprise Python Development Standards & Best Practices

> **Version:** 2.0  
> **Audience:** Python Developers, DevOps Engineers, SREs, Platform Engineers

## Table of Contents

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
11. Git & Pull Requests
12. CI/CD
13. AI-Assisted Development
14. Quick Reference

---

# 1. Development Environment

## Recommended IDE

- Visual Studio Code

### Recommended Extensions

| Extension | Purpose |
|-----------|---------|
| Python | Python support |
| Pylance | IntelliSense |
| Ruff | Linting |
| Black Formatter | Formatting |
| GitLens | Git insights |
| Docker | Docker integration |
| Kubernetes | Kubernetes manifests |
| YAML | YAML editing |
| Error Lens | Inline diagnostics |
| GitHub Copilot | AI coding |
| AWS Toolkit | AWS integration |
| Terraform | IaC support |
| SonarLint | Static analysis |

## Virtual Environment

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
| Tool Configuration | pyproject.toml |
| Lock Versions | Yes |
| Remove Unused Packages | Regularly |

---

# 4. Coding Standards

- Follow **PEP 8**
- Use **meaningful names**
- Add **type hints**
- Write **docstrings**
- Prefer **f-strings**
- Keep functions small and focused

Example:

```python
def create_user(name: str) -> bool:
    return True
```

---

# 5. Code Quality

| Tool | Purpose |
|------|---------|
| Ruff | Linting + import sorting |
| Black | Formatting |
| mypy | Type checking |
| Bandit | Security scanning |
| pip-audit | Dependency scanning |

Commands:

```bash
ruff check .
black .
mypy .
bandit -r .
pip-audit
```

### Pre-commit

```bash
pip install pre-commit
pre-commit install
```

---

# 6. Testing

Use **pytest**.

```bash
pytest
pytest -v
pytest --cov=src tests/
```

Target **80%+** code coverage.

---

# 7. Logging & Error Handling

Use:

```python
import logging
logger = logging.getLogger(__name__)
```

Never use `print()` for production logging.

---

# 8. Security

- Never hardcode secrets
- Use Kubernetes Secrets
- Use AWS Secrets Manager
- Scan dependencies
- Scan container images

Commands:

```bash
pip-audit
bandit -r .
trivy image my-app:latest
```

---

# 9. Docker Best Practices

| Best Practice | Description |
|--------------|-------------|
| Slim Images | `python:3.12-slim` |
| Multi-stage Builds | Reduce image size |
| Non-root User | Improve security |
| `.dockerignore` | Reduce build context |
| BuildKit | Faster builds |
| Docker Scout | Recommendations |
| Dive | Layer analysis |

Example:

```bash
DOCKER_BUILDKIT=1 docker build -t my-app .
```

Cleanup:

```bash
docker builder prune -a
docker image prune -a
docker system prune -a --volumes
```

---

# 10. Kubernetes Best Practices

- Define CPU/Memory requests and limits
- Configure liveness/readiness probes
- Use ConfigMaps and Secrets
- Validate manifests

```bash
kubectl apply --dry-run=client -f deployment.yaml
helm lint charts/my-chart
```

---

# 11. Git & Pull Requests

| Practice | Recommendation |
|----------|----------------|
| Branch Strategy | Feature branches |
| Commits | Small & meaningful |
| PR Size | One feature per PR |
| Reviews | Mandatory |

---

# 12. CI/CD Pipeline

```text
Developer
    │
    ▼
Pre-commit
    ▼
Ruff
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

Recommended:

- GitHub Copilot
- Amazon Q
- Qodo
- Cursor

Use AI for:

- Unit tests
- Documentation
- Code review
- Refactoring

Always review AI-generated code before committing.

---

# 14. Quick Reference

| Activity | Command |
|----------|---------|
| Create venv | `python3 -m venv .venv` |
| Activate | `source .venv/bin/activate` |
| Install | `pip install -r requirements.txt` |
| Format | `black .` |
| Lint | `ruff check .` |
| Type Check | `mypy .` |
| Test | `pytest` |
| Docker Build | `docker build -t my-app .` |
| Docker Scan | `trivy image my-app` |
| Helm Lint | `helm lint chart/` |
| K8s Dry Run | `kubectl apply --dry-run=client -f deployment.yaml` |

---

# Overall Assessment

Following these standards promotes:

- Consistency
- Maintainability
- Security
- Performance
- Scalability
- Production readiness
- Enterprise-grade engineering practices
