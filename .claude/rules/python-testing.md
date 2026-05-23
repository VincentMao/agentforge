# Python Testing Rules

Tools: `pytest`, `pytest-cov`, `pytest-xdist` (replaces `buck test`)

## Why This Exists
Consistent test conventions make tests discoverable, fast, and meaningful across the entire codebase.

## Required Configuration (pyproject.toml)
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = ["--strict-markers", "--tb=short", "-q"]

[tool.coverage.run]
source = ["src"]
omit = ["tests/*", "src/__init__.py"]

[tool.coverage.report]
fail_under = 80
show_missing = true
```

## Commands
```bash
# Run all tests
pytest

# Run with coverage (required before commit)
pytest --cov=src --cov-report=term-missing

# Run specific test file
pytest tests/unit/test_loader.py -v

# Run in parallel
pytest -n auto

# Run tests matching name
pytest -k "normalize or transform" -v
```

## Rules Claude Must Follow
- Coverage must be ≥ 80% before any commit touching `src/`
- Test file mirrors source file: `src/pipeline/loader.py` → `tests/unit/test_loader.py`
- Fixtures for shared data go in `tests/conftest.py`
- Use `pytest.approx()` for float comparisons
- Integration tests go in `tests/integration/`, unit tests in `tests/unit/`
