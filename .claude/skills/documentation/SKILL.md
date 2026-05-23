---
name: documentation
description: Use this when writing docstrings, README files, or changelogs. Enforces Google-style docstrings, behavior-first descriptions, and the standard README structure.
---

# Documentation

Documentation describes what code does, not how it does it.

## Docstring Format (Google Style)

```python
def normalize(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Z-score normalize a column (mean=0, std=1).

    Args:
        df: Input DataFrame. Not modified in place.
        col: Column name to normalize. Must exist in df.

    Returns:
        New DataFrame with the specified column normalized.
        All other columns are unchanged.

    Raises:
        KeyError: If col is not in df.columns.
        ValueError: If the column has zero standard deviation.

    Example:
        >>> result = normalize(df, "feature1")
        >>> result["feature1"].mean()
        0.0
    """
```

## README Structure (Required Sections)

Every README must have in this order:
1. **One-line description** (what it does, not what it is)
2. **Install** (exact commands, no "see docs")
3. **Quickstart** (working code in < 10 lines)
4. **Examples** (2–3 realistic use cases)
5. **API reference** (or link to one)

## Changelog Format

```markdown
## [0.2.0] - 2026-05-23
### Added
- `normalize()` function in `src/pipeline/transformer.py`
### Fixed
- `load_csv()` now raises `FileNotFoundError` instead of silent `None` return
```

## Anti-Patterns

| ❌ | ✅ |
|---|---|
| "This function processes the data" | "Returns normalized DataFrame with mean=0, std=1" |
| Docstring copies the function signature | Explains the contract — what's guaranteed |
| README with no working example | Quickstart with exact copy-pasteable commands |
| "See source code for details" | Inline Example section |
