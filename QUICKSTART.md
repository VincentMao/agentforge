# Quickstart — 5 Minutes to First Win

## Step 1: Install (30 seconds)

```bash
claude plugin install github:YOUR_USERNAME/agentforge
```

Restart Claude Code. All 9 skills are now available as `/skill-name` commands.

## Step 2: Clone the Examples

```bash
git clone https://github.com/YOUR_USERNAME/agentforge
cd agentforge
```

## Step 3: The Refactor Demo (3 minutes)

Open the `before/` folder — this is intentionally messy Python, the kind that accumulates in research codebases:

```bash
cd examples/legacy-refactor/before
claude
```

Inside Claude Code, type:
```
/refactoring
```

Claude will:
1. **Identify the problems** — global state, no type annotations, god function, zero tests
2. **Propose a plan** — strangler fig approach, one seam at a time
3. **Ask for approval** — you control what happens
4. **Execute** — produce the clean version and generate pytest tests

Compare the result with `../after/` which shows the gold standard output.

Read `WALKTHROUGH.md` to see the exact skill invocations used.

## Step 4: Try the ML Pipeline

```bash
cd ../data-pipeline
pip install -e ".[dev]"
make train
```

This runs a full PyTorch + Hydra training pipeline. To extend it with Claude:

```bash
claude
/10x-data-scientist
```

## Step 5: Use in Your Own Project

Copy the `.claude/` folder into any Python project:

```bash
cp -r /path/to/agentforge/.claude /your/project/
```

Then open Claude Code in your project and run any skill.

## Next Steps

- Read `.claude/skills/CLAUDE.md` to understand how skills work
- Read `.claude/agents/CLAUDE.md` to learn how to use the agent team
- Read `prompt-templates/README.md` for orchestration patterns
- Browse `docs/reference/` when you want the theory
