# legacy-refactor/

Demonstrates the /refactoring + /unit-testing skill workflow.

## The Story

`before/` is a single-file research script: global state, no types, no tests.
`after/` is what the refactoring skill produces: typed, pure functions, 80%+ test coverage.

## How to Run the Demo

```bash
cd before && claude   # open Claude Code
# type: /refactoring
# Claude will: identify seams → propose plan → execute → generate tests
```

## WALKTHROUGH.md

Documents the exact skill invocations and Claude outputs from the demo run.
