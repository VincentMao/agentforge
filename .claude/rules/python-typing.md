# Python Typing Rules

Tools: `mypy` (strict mode, replaces `pyre-type-error`)

## Why This Exists
Strict type annotations prevent entire categories of bugs and make refactoring safe. Replaces Meta's `pyre` type checker.

## Required Configuration (pyproject.toml)
```toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_any_generics = true
```

## Commands
```bash
# Type-check all source code
mypy src/

# Type-check with verbose output
mypy src/ --show-error-codes --pretty

# Check a specific file
mypy src/pipeline/loader.py
```

## Rules Claude Must Follow
- Every function parameter and return type must be annotated
- No bare `Any` — use `object` or a proper generic
- Use `X | None` (not `Optional[X]`) for nullable types in Python 3.11+
- Use `TypedDict` for structured dicts, `dataclass` for mutable objects
- Collection types: `list[str]` not `List[str]` (Python 3.9+ style)
- Never `# type: ignore` without a comment explaining why

## Common Patterns
```python
from typing import TypedDict
from pathlib import Path

class ModelConfig(TypedDict):
    lr: float
    epochs: int
    batch_size: int

def load_data(path: Path) -> pd.DataFrame: ...
def train(config: ModelConfig) -> tuple[float, float]: ...
```
