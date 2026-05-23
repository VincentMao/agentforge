---
name: unit-testing
description: Use this when writing tests, generating a test suite, or adding coverage to existing code. Follows pytest best practices: fixtures in conftest.py, parametrize for cases, behavior assertions only.
---

# Unit Testing

Tests describe **behavior**, not implementation. A test should break only when observable behavior changes.

## The AAA Pattern

Every test: Arrange → Act → Assert.

```python
def test_normalize_scales_to_unit_variance(sample_df: pd.DataFrame) -> None:
    # Arrange
    col = "feature1"

    # Act
    result = normalize(sample_df, col)

    # Assert — behavior, not internals
    assert result[col].std() == pytest.approx(1.0, abs=1e-6)
    assert result[col].mean() == pytest.approx(0.0, abs=1e-6)
```

## Shared Fixtures → conftest.py

Define shared test data once. pytest auto-discovers `conftest.py`:

```python
# tests/conftest.py
import pytest
import numpy as np
import pandas as pd


@pytest.fixture
def sample_df() -> pd.DataFrame:
    """100-row DataFrame with controlled seed for reproducibility."""
    rng = np.random.default_rng(42)
    return pd.DataFrame({
        "feature1": rng.standard_normal(100),
        "feature2": rng.standard_normal(100),
        "label": rng.integers(0, 2, 100),
    })


@pytest.fixture
def empty_df() -> pd.DataFrame:
    return pd.DataFrame({"feature1": [], "feature2": [], "label": []})
```

## Parametrize for Multiple Cases

```python
@pytest.mark.parametrize("col", ["feature1", "feature2"])
def test_normalize_works_for_all_feature_columns(
    sample_df: pd.DataFrame, col: str
) -> None:
    result = normalize(sample_df, col)
    assert result[col].mean() == pytest.approx(0.0, abs=1e-6)
```

## Error Case Tests

```python
def test_normalize_raises_on_missing_column(sample_df: pd.DataFrame) -> None:
    with pytest.raises(KeyError, match="nonexistent"):
        normalize(sample_df, "nonexistent")
```

## Running Tests with Coverage

```bash
pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=80 -v
```

## Coverage Target: 80% Minimum

Every new public function needs at least:
- One happy-path test
- One error/edge-case test

## Anti-Patterns

| ❌ Don't | ✅ Do |
|---|---|
| `assert result is not None` | `assert result == expected_value` |
| Test private methods directly | Test public behavior that uses them |
| Re-create fixtures in every test file | Define in `conftest.py` |
| Mock everything | Test real behavior; mock only I/O and external services |
| Tests that always pass | Run new tests on wrong code first to verify they fail |
| `test_function_works()` | `test_normalize_scales_feature_to_unit_variance()` |
