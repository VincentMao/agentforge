# Chapter 2: LLM-Assisted Software Engineering

> This chapter is actively evolving. PRs welcome.

## What This Chapter Covers

How to use LLMs effectively as a software engineering tool — not as a replacement for engineering judgment, but as an accelerant that amplifies it.

## Sections

### 1. The Core Tension

LLMs are excellent at generating plausible-looking code. "Plausible-looking" is not the same as "correct." The engineering discipline required to work with LLMs is: **always verify, never trust by default**.

The verification hierarchy:
1. Tests pass (pytest)
2. Types check (mypy --strict)
3. Lint passes (ruff)
4. You can read and understand the diff

### 2. Skill-Based Workflows

The `.claude/skills/` directory encodes the engineering workflows that make LLM-assisted development reliable:

| Skill | What it enforces |
|---|---|
| `10x-engineer` | State assumptions before coding; surgical changes only |
| `refactoring` | Tests first; one seam per commit |
| `unit-testing` | AAA pattern; behavior not implementation |
| `code-reviewer` | Run tools before approving |
| `debugging` | Hypothesis first; reproduce before fixing |

### 3. The Surgical Change Principle

The most common failure mode of LLM-assisted coding is **scope creep** — the model "cleans up" adjacent code while implementing the requested change, creating untestable diffs.

Counter-strategy: The `10x-engineer` skill enforces that every diff must be reviewable. If you can't read the diff in 60 seconds, it's too large.

### 4. Meta Tool Mapping (in progress)

For engineers coming from Meta's internal tooling:

| Meta tool | Open source equivalent | Key difference |
|---|---|---|
| `buck test` | `pytest --cov=src --cov-fail-under=80` | Coverage enforcement is explicit |
| `arc lint` | `ruff check --fix` | Single tool replaces multiple linters |
| `pyre-type-error` | `mypy --strict` | Strict mode is opt-in per project |
| `arc diff` | `git diff --staged` + PR | No automatic review assignment |

*[More sections in progress — PRs welcome]*

## Contributing

Add sections with: what you learned from production use of LLM-assisted engineering. Failures are more valuable than successes.
