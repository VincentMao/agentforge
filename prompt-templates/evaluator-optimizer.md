# Evaluator-Optimizer Pattern

## When to Use

Use when you need generated output to meet a quality bar — run **generate → score against rubric → improve → repeat** until passing. The key: you have an explicit, scoreable rubric.

Best for: docstring quality, code review feedback, writing clarity, API design review.

## The Pattern

```
GENERATOR PROMPT:
Generate [OUTPUT] for [TASK].

EVALUATOR PROMPT:
Score this [OUTPUT] against each criterion (0–10 each):
- [Criterion 1]: [score]/10 — [one sentence reason]
- [Criterion 2]: [score]/10 — [one sentence reason]
- [Criterion 3]: [score]/10 — [one sentence reason]
Overall: [score]/10
Minimum passing score: 8/10.
If below 8, list the top 2 specific improvements needed.

OPTIMIZER PROMPT:
The previous output scored [X]/10.
The evaluator flagged these specific weaknesses: [feedback].
Rewrite the output addressing ONLY those weaknesses.
Do not change what already scored well.
```

## Worked Example: Docstring Quality

```
GENERATE:
"Write a Google-style docstring for this function:
def load_csv(path: Path, required_cols: list[str]) -> pd.DataFrame: ..."

EVALUATE:
Score against:
1. Behavior-first (not implementation): describes what, not how
2. All parameters documented with types
3. All exceptions documented
4. Has copy-pasteable example
5. First line is one sentence, ≤ 72 chars
Minimum 8/10 overall to pass.

OPTIMIZE (if score < 8):
"The docstring scored 6/10. Weaknesses:
- Raises: section missing (FileNotFoundError, KeyError)
- Example: section missing
Rewrite the docstring adding only these two sections. Keep the rest."
```

## Rubric Design Rules

A good rubric criterion is:
- **Binary or clearly gradable** — "has an example" (yes/no) beats "is clear" (subjective)
- **Independent** — each criterion tests one thing
- **Actionable on failure** — "missing Raises section" is actionable; "could be better" is not

## Stopping Criteria

Stop when score ≥ 8/10 **or** after 3 iterations (diminishing returns; if 3 passes haven't reached 8/10, the rubric or the generator prompt needs revision, not another iteration).

## When NOT to Use

- Tasks with no scoreable rubric (use reflection instead)
- Tasks where the first attempt is clearly correct
- Creative tasks where "correctness" is subjective

## Anti-Patterns

| ❌ | ✅ |
|---|---|
| Vague rubric ("is it good?") | Explicit criteria with numeric scores |
| Optimizer changes everything | Optimizer targets only the flagged weaknesses |
| Iterate indefinitely | Hard stop at 3 iterations |
| Evaluator and generator in same prompt | Separate prompts — evaluator needs to be skeptical |
