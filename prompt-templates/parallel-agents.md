# Parallel Agents Pattern

## When to Use

Use when you need the **same type of work** done across multiple independent contexts simultaneously. Fan out, then merge.

Difference from orchestrator-worker: parallel agents are peers doing the same task type; orchestrator-worker has a coordinator delegating different task types.

Best for: generating tests for multiple files, translating code comments to multiple languages, running the same analysis on multiple datasets.

## The Pattern

```
Dispatch N agents simultaneously. Each agent receives:
1. Its specific scope (exactly which files or context — disjoint from other agents)
2. Its exact output format (so merging is mechanical)
3. A reminder not to address anything outside its scope

After all agents complete, merge using the stated output format.
```

## Worked Example: Parallel Test Generation

```
Agent 1:
"Generate pytest tests for src/data/cleaners.py ONLY.
Output: a complete, runnable test file with no external dependencies beyond cleaners.py.
Include: one happy-path test and one error case per public function.
Do not import from any other src/ module."

Agent 2:
"Generate pytest tests for src/data/transformers.py ONLY.
[same format instructions]"

Agent 3:
"Generate pytest tests for src/pipeline/loader.py ONLY.
[same format instructions]"

Merge step:
"Combine the three test files. Extract shared fixtures (sample_df, tmp_path usage)
into tests/conftest.py. Ensure no import conflicts between the three files."
```

## The Merge Contract

Define the merge format **before** dispatching. Agents that don't know how their output will be merged produce outputs that conflict on import names, fixture names, or coverage claims.

```
Merge format for test files:
- Each file is complete and runnable independently
- Fixtures needed by multiple files go in conftest.py
- No two files can import the same fixture with different definitions
```

## Scaling

| N agents | Speedup | Risk |
|---|---|---|
| 2–3 | 2–3x | Low — easy to merge |
| 4–6 | 4–6x | Medium — define merge format carefully |
| 7+ | Diminishing | High — merge complexity grows faster than speedup |

## When NOT to Use

- Agents need each other's outputs (use sequential pipeline instead)
- N=1 (just do it directly)
- The merge step is harder than the task itself

## Anti-Patterns

| ❌ | ✅ |
|---|---|
| Overlapping scopes | Disjoint scopes — each item owned by one agent |
| Agents output prose | Agents output structured format defined upfront |
| Skip the merge step | Explicit merge agent that de-duplicates and resolves conflicts |
| Fan out without knowing how to fan in | Define the fan-in before dispatching |
