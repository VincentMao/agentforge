---
name: refactoring
description: Use this when asked to refactor, clean up, or restructure existing code. Enforces the refactoring contract: tests first, seams second, incremental changes only.
---

# Refactoring

Refactoring changes structure without changing behavior. If you change behavior while refactoring, that is a bug.

## The Refactoring Contract

**You MUST have tests before you start.** No exceptions.

1. Run existing tests → must be green
2. Refactor one seam → run tests → must still be green
3. Repeat

If there are no tests, stop and use the `unit-testing` skill first to write characterization tests.

```bash
pytest tests/ -v --tb=short -q
# Must show: N passed, 0 failed
```

## Process

### Step 1: Characterize the Code
Identify the problems — state them explicitly:
- Global state? Which variables?
- God function/class? What are its responsibilities?
- Missing types? Which parameters?
- No tests? Which behaviors need characterization tests?

### Step 2: Identify Seams
A seam is a place where you can change behavior without editing that code (function boundary, module boundary, interface point). List the seams before touching anything.

### Step 3: Strangler Fig for Large Refactors
Never rewrite large units at once. Build new alongside old:

```python
# Step A: Create new structure
class DataLoader:  # new clean class
    def load(self, path: Path) -> pd.DataFrame: ...

# Step B: Add thin adapter so old code still works
def load_data(path: str) -> pd.DataFrame:  # old function signature kept
    return DataLoader().load(Path(path))   # delegates to new class

# Step C: Migrate callers one by one
# Step D: Delete old function when no callers remain
```

### Step 4: Run Tests After Every Change
Every single step, no matter how small:
```bash
pytest tests/ -v --tb=short -q
```
If tests break → **STOP. Revert. Understand what changed.**

## Commit Strategy

Each refactoring step is its own commit:
```bash
git add -p  # stage only the seam you just changed
git commit -m "refactor: extract DataLoader class from process() function"
```

## Anti-Patterns

| ❌ Don't | ✅ Do |
|---|---|
| Refactor without tests | Write characterization tests first |
| Rename AND restructure in one commit | One type of change per commit |
| Big-bang rewrite | Strangler fig, one seam at a time |
| "I'll fix the tests later" | Tests stay green at every step |
| Change behavior while refactoring | That's a feature — separate commit |
