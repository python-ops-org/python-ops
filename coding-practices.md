# Enterprise Python Development Standards & Best Practices

> **Version:** 3.0\
> **Audience:** Python Developers, DevOps Engineers, SREs, and Platform
> Engineers

------------------------------------------------------------------------

# Table of Contents

1.  Development Environment
2.  Project Structure
3.  Dependency Management
4.  Coding Standards
5.  Code Quality
6.  Testing
7.  Logging & Observability
8.  Security
9.  Docker Best Practices
10. Kubernetes Best Practices
11. Git & Pull Request Best Practices
12. CI/CD Pipeline
13. AI-Assisted Development
14. Documentation Standards
15. YAML & JSON Utilities
16. Quick Reference

------------------------------------------------------------------------

# 1. Development Environment

## Standards

-   Standardize on **Python 3.12+**
-   Use **Visual Studio Code**
-   Configure projects using **pyproject.toml**
-   Use isolated virtual environments

## Recommended Extensions

  Extension         Purpose
  ----------------- -------------------------------
  Python            Python support
  Pylance           IntelliSense & Type Checking
  Ruff              Fast linting & import sorting
  Black Formatter   Code formatting
  GitLens           Git history
  Docker            Docker integration
  Kubernetes        Manifest support
  YAML              YAML editing
  SonarLint         Static analysis
  AWS Toolkit       AWS integration
  Terraform         IaC support

------------------------------------------------------------------------

# 2. Project Structure

``` text
project/
├── src/
├── tests/
├── docs/
├── scripts/
├── configs/
├── templates/
├── .github/
├── Dockerfile
├── pyproject.toml
├── Makefile
├── README.md
└── requirements.txt
```

------------------------------------------------------------------------

# 3. Dependency Management

-   Pin dependency versions
-   Maintain `requirements.txt`
-   Configure tools in `pyproject.toml`
-   Consider **uv** or **pip-tools**
-   Review dependencies regularly

------------------------------------------------------------------------

# 4. Coding Standards

-   Follow PEP 8
-   Use type hints
-   Prefer f-strings
-   Write docstrings
-   Keep functions small
-   Avoid duplicate code

------------------------------------------------------------------------

# 5. Code Quality

Recommended tools:

-   Ruff
-   Black
-   mypy
-   Bandit
-   pip-audit
-   pre-commit

``` bash
ruff check .
black .
mypy .
bandit -r .
pip-audit
```

------------------------------------------------------------------------

# 6. Testing

-   pytest
-   Fixtures
-   Parameterized tests
-   unittest.mock / pytest-mock
-   Integration tests
-   End-to-End tests
-   ≥80% code coverage

------------------------------------------------------------------------

# 7. Logging & Observability

-   Structured JSON logging
-   Correlation IDs
-   Request IDs
-   Appropriate log levels
-   Never log secrets
-   OpenTelemetry integration

------------------------------------------------------------------------

# 8. Security

-   AWS Secrets Manager
-   Kubernetes Secrets
-   Least-Privilege IAM
-   RBAC
-   Bandit
-   pip-audit
-   Trivy
-   SBOM generation
-   Cosign image signing
-   Gitleaks secret scanning

------------------------------------------------------------------------

# 9. Docker Best Practices

-   Multi-stage builds
-   Pin image versions
-   Run as non-root
-   Use `.dockerignore`
-   Enable BuildKit
-   Add HEALTHCHECK
-   Docker Scout
-   Dive

------------------------------------------------------------------------

# 10. Kubernetes Best Practices

-   CPU & memory requests/limits
-   Readiness & liveness probes
-   ConfigMaps & Secrets
-   RBAC
-   NetworkPolicy
-   SecurityContext
-   PodDisruptionBudget
-   HPA/VPA
-   ResourceQuota
-   LimitRange
-   `helm lint`
-   `kubectl apply --dry-run=client`

------------------------------------------------------------------------

# 11. Git & Pull Request Best Practices

## Branch Strategy

Use feature branches.

  Branch    Example
  --------- ------------------------------
  Feature   `feature/OBS-245-backup-api`
  Bugfix    `bugfix/OBS-301-auth-fix`
  Hotfix    `hotfix/OBS-410-prod-fix`
  Release   `release/v3.0.0`

### Rules

-   Never push directly to `main`.
-   One feature or bug per branch.
-   Link every branch to a Jira ticket.
-   Delete merged feature branches.

## Commit Messages

Format:

``` text
<JIRA-ID>: <Description>
```

Example:

``` text
OBS-245: Add Grafana backup scheduler
```

## Pull Requests

-   One feature per PR
-   Mandatory Code Review (CR)
-   Four-Eye Principle (minimum one independent approval)
-   Link Jira ticket
-   Include testing evidence
-   Update documentation when required

## GitHub CodeQL

Enable CodeQL on every Pull Request.

Detects:

-   SQL Injection
-   Command Injection
-   Credential leaks
-   Unsafe API usage
-   Security vulnerabilities

Treat High and Critical findings as merge blockers.

## Branch Protection Rules

Protect `main` and `release/*`.

-   Prevent direct pushes
-   Require Pull Requests
-   Require 1--2 approvals
-   Enforce Four-Eye review
-   Require CI/CD success
-   Require CodeQL success
-   Require Bandit, Trivy and pip-audit
-   Require unit tests
-   Require coverage threshold
-   Dismiss stale approvals
-   Restrict force pushes
-   Restrict branch deletion
-   Require signed commits (recommended)

## CODEOWNERS

Use a `CODEOWNERS` file to automatically assign reviewers.

## Pull Request Template

Include:

-   Jira Ticket
-   Problem Statement
-   Solution
-   Testing
-   Deployment Impact
-   Rollback Plan
-   Reviewer Checklist

------------------------------------------------------------------------

# 12. CI/CD Pipeline

``` text
Checkout
 ↓
Dependency Restore
 ↓
Pre-commit
 ↓
Ruff
 ↓
Black
 ↓
mypy
 ↓
pytest
 ↓
Coverage
 ↓
Bandit
 ↓
pip-audit
 ↓
Gitleaks
 ↓
CodeQL
 ↓
Docker Build
 ↓
Trivy
 ↓
Helm Lint
 ↓
Kubernetes Validation
 ↓
Deploy
```

Also consider Dependabot or Renovate.

------------------------------------------------------------------------

# 13. AI-Assisted Development

Recommended:

-   GitHub Copilot
-   Amazon Q
-   Cursor
-   Qodo

Always review AI-generated code before merging.

------------------------------------------------------------------------

# 14. Documentation Standards

Maintain:

-   README
-   Google-style docstrings
-   ADRs
-   API documentation
-   Architecture diagrams
-   CHANGELOG

------------------------------------------------------------------------

# 15. YAML & JSON Utilities

## YAML

-   yamllint
-   yq

## JSON

-   jq

------------------------------------------------------------------------

# 16. Quick Reference

  Activity          Tool
  ----------------- -------------------------
  Lint              Ruff
  Format            Black
  Type Check        mypy
  Tests             pytest
  Security          Bandit, Trivy, Gitleaks
  Dependency Scan   pip-audit
  PR Analysis       CodeQL
  YAML              yamllint, yq
  JSON              jq

------------------------------------------------------------------------



This guide aligns with modern enterprise engineering practices by
combining Python development standards with DevSecOps, cloud-native
architecture, Git governance, CI/CD quality gates, supply-chain
security, and AI-assisted development. It is suitable as a baseline
engineering standard for enterprise software teams.
