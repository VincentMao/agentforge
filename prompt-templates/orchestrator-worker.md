# Orchestrator-Worker Pattern

## When to Use

Use when a task can be broken into **N independent subtasks** that can run in parallel, then need their results merged. The key condition: workers don't need each other's outputs.

Best for: multi-file code review, parallel test generation, translating the same content into multiple formats.

## The Pattern

```
ORCHESTRATOR PROMPT:
You are coordinating a team. Decompose [TASK] into parallel subtasks.
For each subtask, delegate to a worker with the exact context it needs.
After all workers complete, synthesize results into a unified output.

WORKER PROMPT (one per subtask):
You are a specialist worker. Your ONLY task is: [SPECIFIC_SUBTASK].
You have access to: [RELEVANT_FILES_OR_CONTEXT].
Output exactly: [EXPECTED_OUTPUT_FORMAT].
Do not address anything outside your specific task.
```

## Worked Example: Multi-file Code Review

```
ORCHESTRATOR:
"Review PR #42. Dispatch parallel workers:
- Worker 1: src/data/ changes (data pipeline)
- Worker 2: src/models/ changes (architecture)
- Worker 3: tests/ changes (coverage and quality)
Each worker reports using the format: [🔴 Must fix | 🟡 Should fix | summary]
After all complete, I'll merge and de-duplicate findings."

WORKER 1:
"Review ONLY the files changed in src/data/ from this diff.
Focus on: data loading correctness, type annotations, error handling.
Output: 🔴 must-fix items only. Under 200 words. No opinions on style."

WORKER 2: [analogous, focused on src/models/]
WORKER 3: [analogous, focused on tests/]
```

## Implementation with Claude Code Subagents

```python
# Pseudo-code for programmatic orchestration
tasks = [
    {"scope": "src/data/", "focus": "data correctness"},
    {"scope": "src/models/", "focus": "architecture"},
    {"scope": "tests/", "focus": "coverage"},
]

# Dispatch in parallel (Claude Code subagents run concurrently)
results = [dispatch_worker(t) for t in tasks]

# Merge: de-duplicate, rank by severity, summarize
merged = merge_findings(results)
```

## Output Format Contract

**Define the output format before dispatching.** Workers that output free-form prose produce outputs that are hard to merge. Workers that output structured reports (severity tags, file:line citations) produce outputs that merge mechanically.

## When NOT to Use

- Sequential tasks where step N needs step N-1's output (use plan-and-execute instead)
- Tasks too small to justify the coordination overhead (a single file review doesn't need orchestration)
- Tasks where workers would need shared mutable state

## Anti-Patterns

| ❌ | ✅ |
|---|---|
| Overlapping scopes between workers | Disjoint scopes — each file owned by exactly one worker |
| Free-form prose output | Structured output with predefined schema |
| Workers that report on everything | Workers with one specific focus |
| Merging without a format | Define merge format before dispatch |
