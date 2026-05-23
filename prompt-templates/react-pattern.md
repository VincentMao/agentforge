# ReAct Pattern (Reasoning + Acting)

## When to Use

Use for **exploratory tasks** where the next action depends on the result of the previous one. You don't know the full path upfront — you discover it through action.

Best for: debugging, codebase exploration, iterative data analysis, research tasks with unknown structure.

## The Pattern

```
SYSTEM:
You solve problems by alternating Thought and Action.
Format strictly:

Thought: [what you know and what you need to find out next]
Action: [one tool call or one concrete step — never two at once]
Observation: [what the action returned]
[repeat until done]
Final Answer: [conclusion with evidence]
```

## Worked Example: Bug Tracking

```
Thought: The test says load_csv raises KeyError on line 45. I need to see that line.
Action: Read src/pipeline/loader.py, lines 40-55
Observation: Line 45 is `return df[col]` with no prior column existence check.
             The function signature takes `col: str` but never validates it.

Thought: The bug is unguarded column access. I need to verify the test reproduces it
         before fixing so I know my fix is actually needed.
Action: Run `pytest tests/test_loader.py::test_load_missing_column -v`
Observation: FAIL — KeyError raised at loader.py:45, not caught. Reproduces the bug.

Thought: The fix is to check `col in df.columns` before accessing. One line.
Action: Edit loader.py line 45 to add the guard clause.
Observation: Edit applied.

Thought: Verify the fix makes the test pass and nothing else broke.
Action: Run `pytest tests/ -q`
Observation: 24 passed, 0 failed.

Final Answer: Bug was unguarded column access on loader.py:45.
              Fixed with a KeyError raise before the access.
              24 tests pass, no regressions.
```

## The One-Action Rule

**Never combine two actions in one step.** Each action produces an observation that informs the next thought. Combining actions means you lose the observation signal — you can't know which action caused which outcome.

```
❌ Action: Read loader.py AND run the tests
✅ Action: Read loader.py
   [Observation]
   Thought: ...
   Action: Run the tests
```

## Worked Example: Codebase Exploration

```
Thought: I need to understand how the DataModule connects to the Trainer.
         Start at the entry point.
Action: Read src/train.py
Observation: Line 18: `trainer.fit(model=model, datamodule=datamodule)`
             The Trainer calls setup() and dataloader methods on the DataModule.

Thought: I need to see what setup() does in our DataModule.
Action: Read src/data/datamodule.py, focusing on setup()
Observation: setup() calls prepare_data() and then splits the DataFrame into
             _train, _val, _test TensorDatasets.

Thought: The connection is clear. The Trainer calls setup("fit"),
         which creates the three datasets. Then calls train/val/test_dataloader()
         to get DataLoader objects. No magic — just the Lightning protocol.

Final Answer: DataModule connects to Trainer via the LightningDataModule protocol:
              prepare_data() → setup(stage) → train/val/test_dataloader().
              See datamodule.py:setup() for the split logic.
```

## When NOT to Use

- Tasks with a known execution path (use plan-and-execute instead)
- Simple lookups with a single known action
- When you already know what you'll find (don't perform theater; just do the task)

## Anti-Patterns

| ❌ | ✅ |
|---|---|
| Combined actions | One action per step |
| Skip the Thought step | Always state what you know and what you need before acting |
| Long observation summaries | Quote the exact relevant output |
| "I'll check multiple things at once to save time" | Each action gives signal that changes the next thought |
