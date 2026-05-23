# .claude/

The engine room. Contains skills, rules, and agents for agentforge.

## Contents

- `skills/` — 9 behavioral skill contracts (SKILL.md files). Activated by typing `/skill-name` in Claude Code.
- `rules/` — 5 Python quality guardrail files (added in Phase 3).
- `agents/` — 7 Claude Code subagent configs (added in Phase 4).

## How Skills Work

Skills are loaded by the plugin system when Claude Code reads `plugin.json` at the repo root. Each skill is a `SKILL.md` with YAML frontmatter + Markdown behavioral instructions. When a user types `/10x-engineer`, Claude Code loads and applies the corresponding SKILL.md.
