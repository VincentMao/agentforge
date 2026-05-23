# Agent Team

7 Claude Code subagents. Each has a defined role, tool restrictions, and hard rules.

## Team Roles

| Agent | Best for |
|---|---|
| `orchestrator` | Multi-step tasks needing plan → implement → review |
| `architect` | System design decisions, dependency review |
| `planner` | Breaking a feature into phased implementation steps |
| `code-reviewer` | After implementation, before committing |
| `commit-reviewer` | Before pushing — checks staged changes |
| `evaluator` | After implementation — did we meet requirements? |
| `doc-drafter` | Writing/updating docstrings, README, changelog |

## Common Workflows

**New feature:** orchestrator → planner → (implement) → code-reviewer → evaluator → doc-drafter

**Bug fix:** commit-reviewer (before push) → code-reviewer (after fix)

**Architecture decision:** architect → planner → orchestrator
