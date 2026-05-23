# Rules

Rules are Markdown files defining Python code quality standards. Claude reads these when working in any Python project that includes this `.claude/` folder.

## How Rules Are Applied

These rules define what Claude should do and what commands to run. Use the `evaluator` agent to check compliance.

## Meta Tool → Open Source Mapping

| Meta tool (internal) | Open source equivalent |
|---|---|
| `buck test` | `pytest --cov=src --cov-fail-under=80` |
| `black` | `ruff format` |
| `arc lint` | `ruff check --fix` |
| `pyre-type-error` | `mypy --strict` |
| `arc diff` | `git diff --staged` + PR review |

## Adding a New Rule

1. Create a new `.md` file in this folder
2. Structure: **Why → Commands → What Claude must do → Anti-patterns**
3. Update this CLAUDE.md with a one-line summary
