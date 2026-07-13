
# Enterprise Python Development Standards & Best Practices


# 1. Development Environment

## 1.1 Use Visual Studio Code as the Standard IDE

### Recommended Extensions

- Python
- Pylance
- Black Formatter
- GitLens
- Docker
- Kubernetes
- YAML
- GitHub Copilot


---

## 1.2 Create Projects Using PASFolds

Use **PASFolds** to generate a standard project structure.

### Benefits

- Standardized directory structure
- Faster onboarding
- Easier maintenance
- Consistent project layout

### Standard Moduler Project Structure

- [CREATE-PROJECT](https://github.com/python-ops-org/python-ops/blob/master/create_python_project.sh)

```text
grafana-backup-api/
├── src/
│   ├── __init__.py
│   ├── run.py
│   ├── config.py
│   ├── service/
│   │   └── __init__.py
│   ├── utils/
│   │   └── __init__.py
│   └── common/
│       └── __init__.py
│
├── tests/
│   └── .gitkeep
│
├── templates/
│   ├── prod/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── configmap.yaml
│   │   └── pvc.yaml
│   └── syst/
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── configmap.yaml
│       └── pvc.yaml
│
├── scripts/
│   └── test.sh
│
├── docs/
│   └── architecture.md
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .env.example
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 1.3 Create a Virtual Environment

### Create

```bash
python3 -m venv .venv

source .venv/bin/activate

.venv\Scripts\activate

pip install -r requirements.txt

pip freeze > requirements.txt
```

---

## 1.4 Manage Dependencies

- Maintain `requirements.txt`
- Pin package versions
- Remove unused packages regularly

---

# 2. Coding Standards

## 2.1 Follow PEP 8

Recommended tools:

- Black
- Flake8

---



---

## 2.3 Use Meaningful Naming

Use descriptive names for:

- Classes
- Functions
- Variables
- Packages
- Files

---

## 2.4 Use Type Hints

Example:

```python
def create_user(name: str) -> bool:
    ...
```

Recommended tool:

- mypy

---

## 2.5 Write Documentation

Maintain:

- README.md
- Docstrings
- Architecture diagrams
- Confluence documentation

---

# 3. Code Quality

## 3.1 Format Python Code

Format the entire project:

```bash
black .
black app.py
```

VS Code shortcut:

```
Shift + Alt + F

Shift + Alt + F

Ctrl + Shift + P

```

---

## 3.3 Format YAML

```bash
yamllint values.yaml
Shift + Alt + F
```

---

## 3.4 Validate Helm Charts

Lint:

```bash
helm lint charts/my-chart

helm template charts/my-chart

helm template charts/my-chart | yamllint -
```

---

## 3.5 Sort Imports

Recommended tools:

- Ruff
- isort

---

## 3.6 Static Code Analysis

```bash

flake8 .
mypy .
bandit -r .
pip-audit
```

---

# 4. Testing

## 4.1 Write Unit Tests

Recommended framework:

- pytest

Run all tests:

```bash
pytest

pytest tests/test_app.py

pytest -v

pytest --cov=app tests/
```

---

## 4.2 Maintain High Test Coverage

Cover:

- Business logic
- Negative scenarios
- Edge cases
- Exception handling

---

# 5. Logging & Error Handling

## 5.1 Implement Logging

Use:

```python
import logging
```

Never use:

```python
print()
```

---

## 5.2 Handle Exceptions Properly

- Catch expected exceptions
- Log errors
- Never use `except:` without specifying an exception

---

# 6. Security

## 6.1 Never Hardcode Secrets

Use:

- AWS Secrets Manager
- Kubernetes Secrets
- Environment Variables

---

## 6.2 Scan Dependencies

```bash
pip-audit

safety check
```

---

# 7. Docker Best Practices

## 7.1 Use Lean Base Images



## 7.2 Use Multi-Stage Docker Builds

Benefits:

- Smaller image size
- Faster deployment
- Reduced attack surface

- [multi-stage-dockerfile](https://github.com/nik786/kube-learn/blob/master/KUBERNETES/multi-stage-nodejs-dockerfile)



---

## 7.3 Run Containers as Non-Root

```dockerfile
RUN addgroup --system app

RUN adduser --system --ingroup app app

USER app
```

---

## 7.4 Optimize Docker Images

- Use `.dockerignore`
- Use `--no-cache-dir`
- Remove temporary files
- Copy only required files
- Minimize image layers
- DOCKER_BUILDKIT=1 docker build
   DOCKER_BUILDKIT=1 docker build -t grafana-backup .
- Use Dive
- --squash
   docker build --squash -t grafana-backup .
- docker builder prune -a
- docker image prune -a
- docker system prune -a --volumes
 

---

## 7.5 Scan Docker Images

```bash
trivy image my-app:latest

```

---

# 8. Git & Pull Requests

## 8.1 Follow Git Best Practices

- Use feature branches
- Make small commits
- Write meaningful commit messages
- Protect the `main` branch

---

## 8.2 Follow Pull Request Best Practices

Every Pull Request should:

- Be small
- Contain one feature
- Link the Jira ticket
- Include testing evidence
- Be reviewed before merging

---

## 8.3 Conduct Peer Reviews

Review for:

- Code quality
- Security
- Performance
- Testing
- Documentation

---

# 9. AI-Assisted Development

## 9.1 Use AI Coding Assistants

Recommended tools:

- GitHub Copilot


---

## 9.2 Use AI for Pull Request Reviews

Recommended tools:

- Qodo
- CodeQL
- GitHub Copilot Chat

Use AI to identify:

- Bugs
- Missing tests
- Code smells
- Security vulnerabilities
- Performance issues

---

## 9.3 Use AI for Documentation

Generate:

- README files
- API documentation
- Release notes
- Unit test templates

> **Always verify AI-generated content before committing it to the repository.**

---

# 10. Kubernetes Best Practices

## 10.1 Validate Kubernetes Manifests

```bash
kubectl apply --dry-run=client -f deployment.yaml
```

## 10.2 Validate Helm Charts Before Deployment

```bash
helm lint charts/my-chart

helm template charts/my-chart | yamllint -
```

---

## 10.3 Define Resource Requests and Limits

Always specify CPU and memory requests and limits.

```yaml
resources:
  requests:
    cpu: "200m"
    memory: "256Mi"
  limits:
    cpu: "500m"
    memory: "512Mi"
```

---

# Quick Reference Commands

| Activity | Command |
|-----------|---------|
| Create Virtual Environment | `python3 -m venv .venv` |
| Activate Virtual Environment | `source .venv/bin/activate` |
| Install Packages | `pip install -r requirements.txt` |
| Freeze Packages | `pip freeze > requirements.txt` |
| Format Python | `black .` |
| Ruff Check | `ruff check .` |
| Flake8 | `flake8 .` |
| Type Check | `mypy .` |
| Security Scan | `bandit -r .` |
| Dependency Scan | `pip-audit` |
| Validate YAML | `yamllint values.yaml` |
| Helm Lint | `helm lint charts/my-chart` |
| Validate Helm | `helm template charts/my-chart \| yamllint -` |
| Run Tests | `pytest` |
| Test Coverage | `pytest --cov=app tests/` |
| Build Docker Image | `docker build -t my-app .` |
| Run Docker | `docker run -p 8000:8000 my-app` |
| Scan Docker Image | `trivy image my-app:latest` |
| Kubernetes Dry Run | `kubectl apply --dry-run=client -f deployment.yaml` |

---

# Overall Assessment

This document provides a comprehensive set of enterprise Python development standards covering:

- Development environment
- Coding standards
- Code quality
- Testing
- Logging
- Security
- Docker
- Git workflows
- AI-assisted development
- Kubernetes best practices

Following these standards promotes consistency, maintainability, security, and scalable software development across engineering teams.
