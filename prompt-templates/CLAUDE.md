# prompt-templates/

7 reusable prompt engineering patterns. Each file: when to use, full pattern, worked example, anti-patterns.

## Choosing a Template

| Situation | Template |
|---|---|
| Break task into parallel subtasks | orchestrator-worker |
| Improve output quality iteratively | evaluator-optimizer |
| Same task, N independent contexts | parallel-agents |
| Self-critique before delivering | reflection |
| Get approval before executing | plan-and-execute |
| Next action depends on previous result | react-pattern |
| Complex reasoning with intermediate steps | chain-of-thought |

## How Templates Compose

These patterns combine: use ReAct inside an orchestrator, or reflection inside evaluator-optimizer.
The README.md has a composition guide.
