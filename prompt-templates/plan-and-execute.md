# Plan and Execute Pattern

## When to Use

Use for **any task where wrong assumptions lead to wasted work**. Get explicit plan approval before touching code. The plan surfaces assumptions before they cost hours of implementation.

Best for: multi-file features, refactoring, new subsystem design, any task where "I'll figure it out as I go" has burned you before.

## The Pattern

```
PLANNING PROMPT:
Before writing any code, produce a plan:

1. State your understanding of the task (2–3 sentences)
2. List your assumptions explicitly
3. List the files you will create or modify (exact paths)
4. For each file, describe what changes and why
5. Describe how you will verify each step (test command or observable outcome)

Do NOT write code. Wait for approval.

---
[User reviews, adjusts, approves]
---

EXECUTION PROMPT:
Execute the approved plan exactly. Follow it step by step.
State which step you're on before each action.
If you encounter a blocker not in the plan, STOP and report — do not improvise.
```

## Worked Example: Adding a New Data Loader

```
PLAN:
"My understanding: add a Parquet loader alongside the existing CSV loader,
with the same validation interface.

Assumptions:
- Parquet files will have the same column schema as CSV
- pyarrow is available (I see it in pyproject.toml)
- Tests follow the same pattern as test_loader.py

Files to create/modify:
- CREATE src/pipeline/parquet_loader.py — load_parquet() with same signature as load_csv()
- MODIFY src/pipeline/__init__.py — export load_parquet
- CREATE tests/unit/test_parquet_loader.py — mirror test_loader.py test structure

Verification:
- Step 1: pytest tests/unit/test_parquet_loader.py -v (must fail before implementation)
- Step 2: implement, run same test (must pass)
- Step 3: pytest tests/ --cov=src --cov-fail-under=80 (must still pass)

Do NOT write code yet. Does this plan look right?"

[User: "Yes, but also add a test for malformed Parquet files"]

EXECUTE:
"Step 1 of 3: Creating test file (including malformed Parquet test)..."
```

## The Stop-on-Blocker Rule

The execution phase must stop when encountering something not in the plan — not improvise. This is the most important rule.

**Why:** Improvisation during execution is how plans silently diverge. A 30-second check-in saves a rework.

```
❌ "The API changed, so I'll adapt the plan and keep going"
✅ "Step 2 blocker: the pyarrow API differs from what I planned.
    Proposed adaptation: [describe]. Proceed?"
```

## When NOT to Use

- Trivial single-file changes (overhead exceeds benefit)
- Tasks where requirements will definitely change during execution (use shorter iterations)
- Exploratory work where the destination is unknown

## Anti-Patterns

| ❌ | ✅ |
|---|---|
| Vague plan ("implement X") | Exact file paths and verification commands |
| Code first, plan later | Plan → approve → execute |
| Continue past blockers | Stop, report, get approval before continuing |
| Plan and execute in one prompt | Separate prompts with explicit approval gate |
