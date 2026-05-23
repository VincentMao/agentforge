# agentforge ⚒️

> Skills, agents, rules, and prompt patterns that make AI-assisted development actually work at scale.

**One-command install:**
```bash
claude plugin install github:VincentMao/agentforge
```

## The Problem

Working with Claude on a large codebase without structure is like pair programming with someone who has no memory and no taste. You get code that works once, degrades fast, and has no tests.

agentforge fixes this with:
- **9 skills** that shape how Claude approaches code (think before coding, surgical changes, TDD)
- **7 agents** that work as a team: planner, architect, reviewer, evaluator, doc writer
- **5 rules files** that enforce ruff/mypy/pytest quality standards automatically
- **7 prompt templates** for orchestrator-worker, ReAct, evaluation loops, and more
- **Real examples** you can run in 5 minutes

## See It Work First

```bash
git clone https://github.com/VincentMao/agentforge
cd agentforge/examples/legacy-refactor/before
claude  # open Claude Code here
# then type: /refactoring
```

Watch Claude identify the god function, propose a refactoring plan using the strangler fig pattern, generate tests, and produce the clean version in `../after/`.

## → [QUICKSTART.md](QUICKSTART.md) — 5-minute walkthrough

## What's Inside

| | |
|---|---|
| `.claude/skills/` | 9 SKILL.md behavioral contracts |
| `.claude/rules/` | Python formatting, typing, testing, git, quality |
| `.claude/agents/` | 7 Claude Code subagent configs with roles + dos/don'ts |
| `examples/legacy-refactor/` | Before/after Python refactor with walkthrough |
| `examples/data-pipeline/` | Production ML pipeline (PyTorch + Hydra, vizard-style) |
| `prompt-templates/` | Orchestrator-worker, ReAct, evaluator-optimizer, and more |
| `docs/reference/` | Living book chapters on prompt engineering + ML engineering |

## Tool Compatibility

Built for Claude Code. Patterns apply to Codex, JetBrains AI Assistant, and any agent that reads Markdown skill files.

## License

MIT
