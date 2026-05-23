# legacy-refactor/after/

The clean version: typed, pure functions, 100% test coverage.

## Run Tests

```bash
pip install -e ".[dev]"
pytest tests/ --cov=src --cov-report=term-missing -v
```

## Structure

- `src/pipeline/loader.py` — typed CSV loader with column validation
- `src/pipeline/transformer.py` — pure functions: normalize(), scale_linear()
- `src/pipeline/trainer.py` — orchestrates load → transform → train → save
- `src/utils/types.py` — PipelineConfig dataclass
- `tests/` — 18 tests, 100% coverage

## Comparing to before/

| before/ | after/ |
|---|---|
| Global state (`data = None`) | Pure functions, no side effects |
| No type annotations | Full mypy --strict compliance |
| Zero tests | 18 tests, 100% coverage |
| God function (`process()`) | Separated: loader + transformer + trainer |
| `helpers.py` dump | Specific modules with clear ownership |
