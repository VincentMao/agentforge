# Chapter 1: Prompt Engineering Patterns

> This chapter is actively evolving. PRs welcome — especially case studies from production use.

## What This Chapter Covers

The 7 patterns in `prompt-templates/` explained in depth: when they work, when they fail, how to compose them, and how to calibrate them for your use case.

## Sections

### 1. Why Patterns Matter

Unstructured prompting at scale produces inconsistent output. A prompt that works once may fail on similar inputs because it relies on the model's internal heuristics rather than explicit structure.

Patterns solve this by:
- **Constraining the output space** — structured outputs are easier to merge, evaluate, and build on
- **Making failure modes explicit** — each pattern has known failure modes; unstructured prompts have unpredictable ones
- **Enabling composition** — patterns designed to compose produce more powerful workflows than monolithic prompts

### 2. The Seven Patterns (brief)

| Pattern | Key insight | When it breaks |
|---|---|---|
| Orchestrator-Worker | Parallel execution with disjoint scopes | When scopes overlap |
| Parallel Agents | N copies of same task | When outputs need to be consistent with each other |
| Evaluator-Optimizer | Explicit rubric enables iteration | When the rubric is vague |
| Reflection | Adversarial self-critique | When the model can't be skeptical about its own work |
| Plan and Execute | Approval gate prevents wasted work | When requirements will change during execution |
| ReAct | Observation-driven exploration | When you already know the path |
| Chain of Thought | Intermediate steps prevent shortcut errors | When the reasoning path is obvious |

### 3. Composition (in progress)

Common compositions and when to use them:

- **Orchestrator + ReAct workers**: coordinator knows what to explore; workers discover how
- **CoT + Reflection**: reason through, then critique the reasoning
- **Plan-and-Execute + Parallel Agents**: plan identifies parallelizable subtasks

*[Case studies needed — open a PR with your production experience]*

### 4. Calibration (in progress)

How to adjust pattern parameters for your use case:
- When to increase reflection depth
- How to design rubric criteria that are actually scoreable
- Orchestrator strategies for N > 5 workers

*[Community contributions welcome]*

### 5. Anti-Pattern Catalog (in progress)

The most common ways each pattern breaks in practice.

*[Add yours with a PR — include: what you tried, what went wrong, what fixed it]*

## Contributing

If you have production experience with any of these patterns, open a PR with a case study. Format:
1. Task description (1 sentence)
2. Pattern used
3. What worked
4. What didn't
5. What you'd do differently

The best contributions show failure modes, not just successes.
