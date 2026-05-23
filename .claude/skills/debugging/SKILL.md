---
name: debugging
description: Use this when you have a bug to track down. Enforces hypothesis-first debugging — never guess, always reproduce, always verify the fix doesn't break other tests.
---

# Debugging

A bug without a reproduction is a rumor. A fix without a test is a prayer.

## The Protocol

### Step 1: Write a Failing Reproduction First
Before touching any code:
```python
def test_reproduces_bug():
    # Minimal case that triggers the bug
    result = function_under_test(bad_input)
    assert result == expected  # This FAILS — that's the point
```
Run it: `pytest tests/test_bug.py::test_reproduces_bug -v`
It must fail. If it passes, you haven't reproduced the bug.

### Step 2: State Your Hypothesis Explicitly
Before changing code, write:
> "I believe the bug is in [specific location] because [reason]. My hypothesis: [if I change X, the test will pass]."

If you can't state a hypothesis, add logging — not guesses.

### Step 3: Make One Change
Change exactly what your hypothesis says. Run the reproduction test.
- If it passes → verify no other tests broke: `pytest tests/ -q`
- If it fails → your hypothesis was wrong. Form a new one from the evidence.

### Step 4: Never `print()` Debug in Production Code
Use logging:
```python
import logging
log = logging.getLogger(__name__)
log.debug("Processing batch: size=%d, dtype=%s", batch.shape[0], batch.dtype)
```
Remove all debug logging before committing.

## Anti-Patterns

| ❌ | ✅ |
|---|---|
| Change code and hope | Write failing test first |
| "It works now" without knowing why | State and verify the hypothesis |
| Stack of `print()` statements | `logging.debug()` with structured fields |
| Fix the symptom | Find the root cause |
