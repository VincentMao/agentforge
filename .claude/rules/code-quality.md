# Code Quality Rules

Tools: `ruff` (complexity checks)

## File Size Limits
- Source files: ≤ 300 lines (extract a module when growing beyond)
- Test files: ≤ 500 lines
- Functions: ≤ 40 lines (extract helpers when longer)

## Complexity Limits
```toml
[tool.ruff.lint]
select = ["C90"]

[tool.ruff.lint.mccabe]
max-complexity = 10
```

## Naming Conventions
- Functions/variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_single_leading_underscore`
- Type aliases: `PascalCase`

## Module Structure Pattern
Every Python module > 50 lines should have:
1. Module docstring explaining purpose
2. `__all__` list of public exports
3. Imports grouped: stdlib → third-party → local

```python
"""
Transformer module: feature engineering for tabular ML pipelines.
"""
__all__ = ["normalize", "encode_categoricals"]

import logging  # stdlib
import pandas as pd  # third-party
from .types import FeatureConfig  # local
```

## What Claude Must Never Do
- Create `utils.py` files that grow without bound — extract specific modules
- Put business logic in `__init__.py`
- Use global state (no module-level mutable variables)
- Catch `Exception` broadly without re-raising or specific handling
