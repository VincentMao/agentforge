# Prompt Templates

7 reusable prompt engineering patterns. Each file has: when to use, the full pattern, a worked example, and anti-patterns.

## Choosing a Pattern

| Situation | Pattern | File |
|---|---|---|
| Break task into parallel subtasks with a coordinator | Orchestrator-Worker | `orchestrator-worker.md` |
| Same task type across N independent contexts | Parallel Agents | `parallel-agents.md` |
| Improve output quality against a rubric | Evaluator-Optimizer | `evaluator-optimizer.md` |
| Self-critique before delivering high-stakes output | Reflection | `reflection.md` |
| Get plan approval before touching code | Plan and Execute | `plan-and-execute.md` |
| Next action depends on previous result (debugging, exploration) | ReAct | `react-pattern.md` |
| Complex reasoning with intermediate steps | Chain of Thought | `chain-of-thought.md` |

## Pattern Selection Quick Guide

**"I have N files to process independently"** → Parallel Agents or Orchestrator-Worker

**"I want to iteratively improve generated output"** → Evaluator-Optimizer

**"I'm debugging a bug I don't fully understand"** → ReAct

**"I need to make a non-trivial decision"** → Chain of Thought + Reflection

**"I'm about to write a lot of code"** → Plan and Execute first

**"My output might have blind spots"** → Reflection

## Composition

Patterns compose. Common combinations:

- **ReAct inside Orchestrator**: workers use ReAct for exploration while orchestrator coordinates
- **Reflection inside Evaluator-Optimizer**: evaluator uses reflection to be more adversarial
- **Plan-and-Execute with CoT planning**: use CoT to reason through the plan before writing it
- **Parallel Agents with Evaluator-Optimizer**: fan out, then use eval-optimize to merge and improve

## Relationship to the Agent Team

These patterns map to the agent configs in `.claude/agents/`:

| Pattern | Agent |
|---|---|
| Orchestrator-Worker | `orchestrator.md` |
| Plan and Execute | `planner.md` |
| Evaluation | `evaluator.md` |
| Reflection (pre-commit) | `commit-reviewer.md` |
