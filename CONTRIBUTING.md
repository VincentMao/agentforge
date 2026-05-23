# Contributing to agentforge

## What We Accept

- New skills in `.claude/skills/`
- New agent configs in `.claude/agents/`
- Rule additions in `.claude/rules/`
- Prompt template additions in `prompt-templates/`
- Book chapter sections in `docs/reference/`
- Bug fixes or improvements in `examples/`

## How to Add a Skill

1. Fork the repo
2. Create `.claude/skills/your-skill-name/SKILL.md`
3. Required frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: Use this when... [trigger conditions]
   ---
   ```
4. Required sections: trigger conditions, behavioral contract, **anti-patterns table**
5. Add the path to `plugin.json` under `"skills"`
6. Open a PR with: what the skill does, when it activates, an example output

## How to Add an Agent

1. Create `.claude/agents/your-agent.md`
2. Required frontmatter:
   ```yaml
   ---
   name: your-agent
   description: ...
   tools: Read, Bash   # list only what the agent needs
   ---
   ```
3. Required sections: role (one sentence), process steps, hard rules, report format
4. Add to `.claude/agents/CLAUDE.md` table
5. Open a PR explaining the use case

## How to Contribute a Book Chapter Section

1. Find the relevant chapter in `docs/reference/`
2. Add your section to the `README.md`
3. Practical case studies > theory — show it working, explain why
4. Failures are valuable: include what didn't work and why
5. Keep sections under 500 words; link to external resources for depth

## Quality Bar for Code Contributions

All code changes must pass CI:
```bash
# legacy-refactor/after
cd examples/legacy-refactor/after
pytest tests/ --cov=src --cov-fail-under=80

# data-pipeline
cd examples/data-pipeline
make check   # lint + typecheck + test
```

## Skill and Agent Review Criteria

Reviewers check for:
- Clear trigger conditions (description starts with "Use this when...")
- No contradictions with existing rules in `.claude/rules/`
- Practical anti-patterns section (not just "don't do bad things")
- Hard rules that are actually hard (not "try to...")

## Questions?

Open an issue with the `question` label.

## Code of Conduct

Be constructive. Review code, not people.
