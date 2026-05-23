# Refactor Walkthrough — Exact Skill Invocations

This documents the Claude Code session that transformed `before/` into `after/`.

## Session 1: Diagnosis with /refactoring

**User:** `/refactoring`

**Claude activated:** `.claude/skills/refactoring/SKILL.md`

**Claude's output:**
> "Before I start, I need to confirm tests exist. Running `pytest tests/` — no tests found.
> I'll stop and use `/unit-testing` first to write characterization tests for the existing behavior."

**Lesson:** The refactoring skill correctly blocked the refactor because no tests existed.

## Session 2: Characterization Tests with /unit-testing

**User:** `/unit-testing`

**Claude identified these behaviors to characterize:**
1. `process()` reads a CSV, drops NaN rows, scales feat1 by 2, normalizes feat2, trains RandomForest, pickles model
2. `predict()` returns model prediction — but crashes if `process()` not called first (global state bug)

**Claude generated minimal tests** that lock in current behavior before restructuring.

## Session 3: Refactor Execution

**User:** `/refactoring` (now with characterization tests in place)

**Claude's seam identification:**
1. **Seam 1:** Extract `load_csv()` from `process()` — pure function, no side effects
2. **Seam 2:** Extract `scale_linear()` and `normalize()` as pure functions (from helpers.py)
3. **Seam 3:** Extract `Trainer` class — encapsulate model + predict, eliminate globals
4. **Seam 4:** Type annotate all public functions
5. **Final:** Delete helpers.py (all functions migrated)

**Each seam was a separate commit. Tests stayed green after every step.**

## Key Skill Behaviors Observed

| Skill | What it enforced |
|---|---|
| `/refactoring` | Blocked until tests existed; strangler fig pattern; one commit per seam |
| `/unit-testing` | AAA format; fixtures in conftest.py; behavior not implementation |
| `/code-reviewer` | Ran mypy + ruff after each seam; flagged missing error handling in loader |

## The Numbers

| Metric | Before | After |
|---|---|---|
| Lines of code | 40 | 120 (split across 5 focused files) |
| Type annotations | 0 | 100% |
| Test coverage | 0% | 85% |
| Global variables | 2 | 0 |
| Functions doing > 1 thing | 1 (process()) | 0 |
