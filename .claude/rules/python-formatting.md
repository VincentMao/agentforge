# Python Formatting Rules

Tools: `ruff` (formatter + linter, replaces `black` + `arc lint`)

## Why This Exists
Consistent formatting eliminates style debates in code review. Automated tools enforce it; humans don't.

## Required Configuration (pyproject.toml)
```toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "W", "F", "I", "B", "C4", "UP"]
ignore = ["E501"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

## Commands
```bash
# Check for violations (CI)
ruff check src/ tests/

# Auto-fix violations
ruff check src/ tests/ --fix

# Format code (replaces black)
ruff format src/ tests/

# Check + format in one pass
ruff check --fix && ruff format
```

## Rules Claude Must Follow
- Always run `ruff format` before committing
- Never commit code with `ruff check` violations
- Import order: stdlib → third-party → local (ruff enforces automatically)
- Strings: double-quotes always
- Line length: 88 characters max
