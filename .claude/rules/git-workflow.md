# Git Workflow Rules

## Commit Message Format
```
<type>(<scope>): <subject>

[optional body]

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `perf`

### Examples
```bash
git commit -m "feat(pipeline): add Parquet loader with schema validation"
git commit -m "fix(trainer): handle empty batch gracefully"
git commit -m "refactor(transformer): extract normalize() into pure function"
git commit -m "test(loader): add edge case for empty CSV file"
```

## Branch Naming
- Features: `feat/short-description`
- Fixes: `fix/what-was-broken`
- Refactors: `refactor/what-changed`

## Rules Claude Must Follow
- Never commit directly to `main` on team projects
- Every commit must pass `ruff check` and `mypy`
- Commit message subject ≤ 72 characters
- One logical change per commit
- Run `git diff --staged` before committing to verify what's included

## Pre-commit Setup
```bash
pip install pre-commit
pre-commit install
```

`.pre-commit-config.yaml` (create at repo root):
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.4
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.9.0
    hooks:
      - id: mypy
        args: [--strict]
        additional_dependencies:
          - pandas-stubs>=2.2.0
          - types-PyYAML
```
