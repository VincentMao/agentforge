# Legacy Refactor Demo

**Before:** 40 lines. Global state. No types. No tests. One function does everything.

**After:** Typed, pure functions. 7 tests. 85%+ coverage. Each file has one responsibility.

## Run the Before Code

```bash
cd before
python data_processor.py  # requires data.csv — will fail gracefully
```

## Run the After Tests

```bash
cd after
pip install -e ".[dev]"
pytest tests/ --cov=src -v
```

## See the Transformation

Read `WALKTHROUGH.md` to see the exact `/refactoring` and `/unit-testing` skill invocations that produced the `after/` code.
