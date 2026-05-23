# Reflection Pattern

## When to Use

Use for **high-stakes outputs** where self-critique before delivery materially improves quality. The model generates output, then critiques it as if seeing it for the first time, then revises.

Best for: security analysis, architectural decisions, code review, anything where a missed flaw is costly.

**Do not use for routine tasks** — reflection adds latency and token cost. The improvement is only meaningful when the initial output has a non-trivial probability of being wrong in important ways.

## The Pattern

```
GENERATION PROMPT:
[Generate the output normally]

REFLECTION PROMPT (same agent, same context):
Review your output above as if you were a skeptical senior engineer seeing it for the first time.

Answer these three questions:
1. What assumption did I make that could be wrong?
2. What edge case did I not handle?
3. What would a 3am production incident reveal about this output?

Then revise your output to address these critiques.
```

## Worked Example: Security Analysis

```
GENERATE:
"Analyze this authentication code for security vulnerabilities."
[Claude produces analysis]

REFLECT:
"Review your analysis as a hostile security researcher who gets paid per finding.

1. What vulnerability did you miss because you assumed the caller would validate input?
2. What timing attack or race condition did you not consider?
3. What would a pentester find in 10 minutes that you didn't flag?

Revise your analysis to address these three questions."
```

## Worked Example: Architectural Decision

```
GENERATE:
"Design the caching layer for this service."
[Claude produces architecture]

REFLECT:
"Review your proposed architecture as a skeptical staff engineer.

1. What assumption about usage patterns might be wrong?
2. What happens when the cache is cold (first request after deploy)?
3. What operational problem will appear at 10x current load?

Revise the architecture addressing these concerns."
```

## Calibrating Depth

One reflection loop is usually sufficient. More loops have diminishing returns and can produce "analysis paralysis" outputs that hedge every statement.

Use a second loop only if:
- The first reflection revealed a fundamental flaw (not just a gap)
- The stakes are extremely high (public security advisory, irreversible infrastructure change)

## When NOT to Use

- Routine code generation with a clear spec
- Tasks where the first output is clearly correct
- Time-sensitive situations where latency matters more than perfection
- More than one reflection loop (converges fast; second loop rarely adds signal)

## Anti-Patterns

| ❌ | ✅ |
|---|---|
| "Is this good?" (vague) | Three specific adversarial questions |
| Reflect on every output | Reserve for high-stakes decisions |
| Multiple reflection loops | One loop; if still wrong, reframe the problem |
| Reflection as validation | Reflection as adversarial critique |
