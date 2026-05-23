# Chapter 3: Multi-Agent System Design

> This chapter is actively evolving. PRs welcome.

## What This Chapter Covers

Designing agent teams that work reliably: role definition, communication patterns, failure handling, and the traps that make agent systems brittle.

## Sections

### 1. The Agent Team in This Repo

The 7 agents in `.claude/agents/` form a complete engineering team:

```
orchestrator          ← coordinates; never writes code
    ├── architect     ← designs; produces ADRs
    ├── planner       ← decomposes; produces task lists
    ├── (engineer)    ← you; writes the code
    ├── code-reviewer ← checks quality post-implementation
    ├── evaluator     ← verifies requirements were met
    └── doc-drafter   ← documents what was built
```

`commit-reviewer` is a pre-push gate, not part of the implementation pipeline.

### 2. Role Definition Principles

Each agent in this repo has:
- **One role** — stated in one sentence in the description
- **Explicit tool restrictions** — agents only have tools they need
- **Hard rules** — non-negotiable gates that prevent shortcuts
- **A report format** — structured output enables programmatic processing

Why tool restrictions matter: an agent that can `Edit` and `Bash` can do anything. Restricting to `Read` and `Grep` makes the agent's behavior auditable.

### 3. Communication Patterns (in progress)

How agents pass outputs to each other:
- Sequential hand-off (one completes, next begins)
- Parallel dispatch with merge
- Feedback loops (evaluator back to implementer)

*[Case studies needed]*

### 4. Failure Handling (in progress)

What happens when an agent can't complete its task:
- Hard fail vs. partial result
- Escalation to orchestrator
- Human-in-the-loop gates

*[Community contributions welcome]*

### 5. The "Never Write Code" Principle

The orchestrator and architect agents have a hard rule: never write implementation code. This sounds restrictive — it's actually liberating. It forces clear separation between "what to build" and "how to build it," which is the boundary most often violated in single-agent systems.

## Contributing

Add sections with: real multi-agent system designs you've built, failure modes you've encountered, and architectural decisions you'd make differently.
