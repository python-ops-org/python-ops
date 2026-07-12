
# Enterprise Python Development Standards & Best Practices

> **Objective**
>
> This document defines the engineering standards and best practices for developing Python applications across the organization. Following these guidelines ensures consistency, maintainability, security, scalability, and high-quality software delivery.

---

# 1. Development Environment

## 1.1 Use Visual Studio Code as the Standard IDE

### Recommended Extensions

- Python
- Pylance
- Black Formatter
- Ruff
- GitLens
- Docker
- Kubernetes
- YAML
- GitHub Copilot
- Amazon Q Developer
- Error Lens

---

## 1.2 Create Projects Using PASFolds

Use **PASFolds** to generate a standard project structure.

### Benefits

- Standardized directory structure
- Faster onboarding
- Easier maintenance
- Consistent project layout

### Standard Project Structure

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
```

### Activate (Linux/macOS)

```bash
source .venv/bin/activate
```

### Activate (Windows)

```powershell
.venv\Scripts\activate
```

### Install Packages

```bash
pip install -r requirements.txt
```

### Freeze Dependencies

```bash
pip freeze > requirements.txt
```

---

## 1.4 Manage Dependencies

- Maintain `requirements.txt`
- Maintain `pyproject.toml`
- Pin package versions
- Remove unused packages regularly

---

# 2. Coding Standards

## 2.1 Follow PEP 8

Recommended tools:

- Black
- Ruff
- Flake8

---

## 2.2 Follow a Modular Architecture

Separate application code into:

- `api`
- `services`
- `repositories`
- `models`
- `config`
- `utils`
- `common`
- `tests`

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
```

Format a single file:

```bash
black app.py
```

VS Code shortcut:

```
Shift + Alt + F
```

---

## 3.2 Format JSON

VS Code:

```
Shift + Alt + F
```

or

```
Ctrl + Shift + P
→ Format Document
```

---

## 3.3 Format YAML

```bash
yamllint values.yaml
```

VS Code:

```
Shift + Alt + F
```

---

## 3.4 Validate Helm Charts

Lint:

```bash
helm lint charts/my-chart
```

Render templates:

```bash
helm template charts/my-chart
```

Validate rendered YAML:

```bash
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
ruff check .
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
```

Run a single file:

```bash
pytest tests/test_app.py
```

Verbose output:

```bash
pytest -v
```

Coverage:

```bash
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

❌ Never use:

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
```

or

```bash
safety check
```

---

# 7. Docker Best Practices

## 7.1 Use Lean Base Images

✅ Preferred

```dockerfile
FROM python:3.12-slim
```

❌ Avoid

```dockerfile
FROM python:latest
```

---

## 7.2 Use Multi-Stage Docker Builds

Benefits:

- Smaller image size
- Faster deployment
- Reduced attack surface

Example:

```dockerfile
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /app /app

CMD ["python", "app.py"]
```

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

---

## 7.5 Scan Docker Images

```bash
trivy image my-app:latest
```

or

```bash
docker scout quickview my-app
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
- Amazon Q Developer
- Cursor
- ChatGPT

---

## 9.2 Use AI for Pull Request Reviews

Recommended tools:

- Qodo
- Amazon Q
- Cursor AI
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

---

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
