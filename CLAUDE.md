# agentforge

A tool-agnostic productivity toolkit for AI-assisted large codebase management.

## What's Here

| Folder | Purpose | Start here when... |
|---|---|---|
| `examples/` | Working demos | You want to see it work first |
| `.claude/skills/` | Behavioral skill contracts | You want to activate a specific skill |
| `.claude/rules/` | Python quality guardrails | You're setting up a new project |
| `.claude/agents/` | Subagent team configs | You need a team for a complex task |
| `prompt-templates/` | Reusable prompt patterns | You're designing a new workflow |
| `docs/reference/` | Deep-dive book chapters | You want to understand the theory |

## Quick Navigation

- **New to this repo?** → Read `QUICKSTART.md`
- **Want to refactor messy code?** → Open `examples/legacy-refactor/`, run `/refactoring`
- **Setting up an ML pipeline?** → Open `examples/data-pipeline/`, run `/10x-data-scientist`
- **Adding a new skill?** → Read `.claude/skills/CLAUDE.md`
- **Reviewing a PR?** → Invoke the `code-reviewer` agent

## Skill Triggers (after installing plugin)

```
/10x-engineer         Before any significant coding task
/planner              When a task needs decomposition
/code-reviewer        After implementation, before committing
/refactoring          When restructuring existing code
/unit-testing         When generating test suites
/10x-data-scientist   For ML/data science work
/architecture-review  For system design decisions
/debugging            When you have a bug to track down
/documentation        When writing docs or docstrings
```
