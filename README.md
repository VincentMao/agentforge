<div align="center">
  <img src="assets/banner.png" alt="agentforge banner" width="100%">

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
  [![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-purple.svg)](https://claude.ai/code)
  [![CI](https://github.com/VincentMao/agentforge/actions/workflows/ci.yml/badge.svg)](https://github.com/VincentMao/agentforge/actions)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
</div>

---

> **Skills, agents, rules, and prompt patterns that make AI-assisted development actually work at scale.**

Without structure, Claude on a large codebase produces code that works once, degrades fast, and has no tests.  
agentforge fixes this with 9 behavioral skills, a 7-agent team, and 5 quality rules — installable in one command.

```bash
claude plugin install github:VincentMao/agentforge
```

→ **[5-minute walkthrough](QUICKSTART.md)** · [Refactor demo](examples/legacy-refactor/) · [ML pipeline](examples/data-pipeline/)

---

## What's Inside

| | Count | What |
|---|---|---|
| 🧠 **Skills** | 9 | Behavioral contracts: `10x-engineer`, `refactoring`, `unit-testing`, `debugging`, and more |
| 🤖 **Agents** | 7 | Team roles: `orchestrator`, `architect`, `planner`, `code-reviewer`, `evaluator`, `doc-drafter` |
| 📐 **Rules** | 5 | Python quality: ruff, mypy strict, pytest 80%+ coverage, git workflow |
| 🔀 **Prompt templates** | 7 | Orchestrator-worker, ReAct, evaluator-optimizer, reflection, and more |
| 💡 **Examples** | 2 | Legacy refactor (before/after Python) · ML pipeline (PyTorch + Hydra) |
| 📖 **Reference docs** | 4 chapters | Prompt engineering · LLM engineering · Multi-agent design · Research engineering |

---

## The Agent Team

```mermaid
flowchart LR
    U(["👤 You\nUser Request"]) --> O

    subgraph Team["agentforge Agent Team"]
        O["🎯 orchestrator\nRoutes & Assigns"]
        P["📋 planner\nBreaks Down"]
        CR["👀 code-reviewer\nValidates"]
        EV["✅ evaluator\nVerifies"]
        DD["📚 doc-drafter\nDocuments"]
    end

    O --> P
    P -->|"task list"| CR
    CR -->|"❌ issues"| P
    CR -->|"✅ passes"| EV
    EV -->|"❌ rework"| P
    EV -->|"✅ verified"| DD
    DD --> Done(["🚀 Done"])

    style O  fill:#ec4899,stroke:#be185d,color:#fff
    style P  fill:#f59e0b,stroke:#d97706,color:#fff
    style CR fill:#8b5cf6,stroke:#6d28d9,color:#fff
    style EV fill:#10b981,stroke:#047857,color:#fff
    style DD fill:#06b6d4,stroke:#0891b2,color:#fff
    style U  fill:#6b7280,stroke:#374151,color:#fff
    style Done fill:#22c55e,stroke:#15803d,color:#fff
```

---

## How Skills Work

Type `/refactoring` in Claude Code → the behavioral contract loads → Claude changes how it thinks and acts.

```mermaid
flowchart LR
    A(["/refactoring\nUser types"]) --> B["Claude Code\nloads SKILL.md"]
    B --> C["Behavioral contract\napplied to session"]
    C --> D["Tests must exist first\nOne seam per commit\nStrangler fig for big refactors"]
    D --> E(["Claude produces\nrefactored code ✅"])

    style A fill:#6366f1,stroke:#4f46e5,color:#fff
    style B fill:#8b5cf6,stroke:#6d28d9,color:#fff
    style C fill:#06b6d4,stroke:#0891b2,color:#fff
    style D fill:#f59e0b,stroke:#d97706,color:#fff
    style E fill:#10b981,stroke:#047857,color:#fff
```

**All 9 skills:** `10x-engineer` · `planner` · `code-reviewer` · `refactoring` · `unit-testing` · `10x-data-scientist` · `architecture-review` · `debugging` · `documentation`

---

## The Quality Gate

Every commit passes through four automated gates — enforced by pre-commit hooks:

```mermaid
flowchart TD
    G(["git commit"]) --> R

    R["🔧 ruff\nlinting + formatting"]
    R -->|"✅"| M["🏷️ mypy\nstrict type checking"]
    R -->|"❌"| Fix1(["fix & retry"])

    M -->|"✅"| T["🧪 pytest\nunit + integration tests"]
    M -->|"❌"| Fix2(["add types"])

    T -->|"✅"| C["📊 coverage\nminimum 80%"]
    T -->|"❌"| Fix3(["fix tests"])

    C -->|"✅"| Done(["✨ commit accepted"])
    C -->|"❌"| Fix4(["add tests"])

    style G    fill:#3b82f6,stroke:#1d4ed8,color:#fff
    style R    fill:#f59e0b,stroke:#d97706,color:#fff
    style M    fill:#8b5cf6,stroke:#6d28d9,color:#fff
    style T    fill:#ef4444,stroke:#991b1b,color:#fff
    style C    fill:#06b6d4,stroke:#0891b2,color:#fff
    style Done fill:#22c55e,stroke:#15803d,color:#fff
```

---

## The Refactor Demo

Open the messy `before/` code in Claude Code, type `/refactoring`. Watch it:

| | `before/` | `after/` |
|---|---|---|
| Functions | 1 god function, 300+ lines | 4 pure functions, each < 40 lines |
| Global state | `data = None`, `model = None` | None — pure functions only |
| Type annotations | Zero | 100%, `mypy --strict` clean |
| Tests | Zero | 18 tests, 100% coverage |
| Imports | Circular, unstructured | Explicit, typed |

```bash
cd examples/legacy-refactor/before
claude   # then type: /refactoring
```

---

## The ML Pipeline

A production-ready PyTorch + Hydra training pipeline. Mirrors the vizard_project pattern.

```bash
cd examples/data-pipeline
pip install -e ".[dev]"
make train   # synthetic data auto-generated
```

Override any hyperparameter from the CLI:
```bash
python src/train.py experiment=baseline
python src/train.py model.optimizer.lr=0.0001 trainer.max_epochs=50
python src/train.py "model.optimizer.lr=0.001,0.0001" --multirun
```

---

## Prompt Templates

7 orchestration patterns — each with worked examples and anti-patterns:

| Pattern | When to use |
|---|---|
| [`orchestrator-worker`](prompt-templates/orchestrator-worker.md) | Break task into N independent parallel subtasks |
| [`evaluator-optimizer`](prompt-templates/evaluator-optimizer.md) | Iterate against a rubric until quality threshold is met |
| [`parallel-agents`](prompt-templates/parallel-agents.md) | Same task type across N independent contexts |
| [`reflection`](prompt-templates/reflection.md) | Adversarial self-critique before delivering high-stakes output |
| [`plan-and-execute`](prompt-templates/plan-and-execute.md) | Approval gate before touching code |
| [`react-pattern`](prompt-templates/react-pattern.md) | Exploratory tasks where next action depends on previous result |
| [`chain-of-thought`](prompt-templates/chain-of-thought.md) | Complex reasoning with intermediate steps |

---

## Quick Start

```bash
# Install as Claude Code plugin (one command, all 9 skills activated)
claude plugin install github:VincentMao/agentforge

# Or copy .claude/ into any existing project
cp -r /path/to/agentforge/.claude /your/project/
```

→ Full walkthrough: **[QUICKSTART.md](QUICKSTART.md)**

---

## Contributing

Contributions welcome — skills, agents, prompt templates, reference chapter sections, and bug fixes.

- 📖 Read **[CONTRIBUTING.md](CONTRIBUTING.md)** for how to add a skill or agent
- 💬 Open a **[GitHub Discussion](https://github.com/VincentMao/agentforge/discussions)** for questions, ideas, or showing what you built
- 🐛 File an **[Issue](https://github.com/VincentMao/agentforge/issues)** for bugs

---

## Contact

Built by [Vincent Xianglun Mao](https://github.com/VincentMao) — research scientist, large-scale ML systems.

For collaborations, research, or questions:  
📧 **maoxianglun@gmail.com**  
🔗 **[LinkedIn](https://www.linkedin.com/in/xianglun-mao-phd-7608a291/)**  
💬 **[GitHub Discussions](https://github.com/VincentMao/agentforge/discussions)**

---

## License

MIT — see [LICENSE](LICENSE).
