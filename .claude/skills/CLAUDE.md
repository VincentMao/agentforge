# Skills

Each subfolder is one skill. Claude Code loads skills from `plugin.json` and activates them when the user types `/skill-name`.

## Skill Format

```yaml
---
name: skill-name
description: Shown in skill picker. Start with "Use this when..." to make trigger conditions explicit.
---
```

Followed by Markdown content that shapes Claude's behavior when the skill is active.

## Adding a New Skill

1. Create `.claude/skills/your-skill-name/SKILL.md`
2. Add the path to `plugin.json` under `"skills"`
3. Test by restarting Claude Code and typing `/your-skill-name`

## Skill Design Principles

- **One behavior per skill** — don't create a mega-skill
- **Trigger conditions first** — the `description` must say when to use this
- **Anti-patterns section required**
- **Keep under 500 lines**
