# Enterprise Python Development Standards & Best Practices

This is the updated GitHub Markdown version with **Flake8** replacing Ruff and includes **yq** and **jq** utilities.

## Code Quality

| Tool | Purpose |
|------|---------|
| Flake8 | PEP 8 Linting |
| Black | Code Formatting |
| mypy | Static Type Checking |
| Bandit | Security Scanning |
| pip-audit | Dependency Scanning |

```bash
flake8 .
black .
mypy .
bandit -r .
pip-audit
```

## YAML Utilities

```bash
yamllint values.yaml
yq '.image.tag' values.yaml
yq '.replicaCount = 3' values.yaml
```

## JSON Utilities

```bash
jq '.' data.json
jq '.name' data.json
jq empty data.json
```

## CI/CD

```text
Developer
  ↓
Pre-commit
  ↓
Flake8
  ↓
Black
  ↓
mypy
  ↓
pytest
  ↓
Bandit
  ↓
pip-audit
  ↓
Docker Build
  ↓
Trivy
  ↓
Helm Lint
  ↓
Deploy
```
