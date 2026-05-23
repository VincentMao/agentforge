---
name: architecture-review
description: Use this for system design decisions or when a codebase feels hard to change. Produces an Architecture Decision Record (ADR). Activate before adding a major new subsystem.
---

# Architecture Review

Every significant design decision deserves an ADR. A decision undocumented is a decision that will be re-litigated in six months.

## Always Produce an ADR

Format:
```markdown
# ADR-NNN: [Decision title]

**Status:** Proposed / Accepted / Deprecated
**Date:** YYYY-MM-DD

## Context
[What problem are we solving? What constraints exist?]

## Decision
[What we decided to do]

## Consequences
**Positive:** [What gets better]
**Negative:** [What gets harder]
**Risks:** [What could go wrong]
```

## Dependency Analysis

Before proposing any architecture change:
```bash
# Find all imports of a module
grep -r "from src.models" src/ --include="*.py"

# Check for circular imports
python -c "import src.models.module"

# List module dependencies
grep -rn "^import\|^from" src/ --include="*.py" | sort | uniq
```

## Coupling/Cohesion Check

Ask for each module:
- **Single responsibility?** Can you describe it in one sentence?
- **High cohesion?** Do all its parts work toward that one purpose?
- **Low coupling?** How many other modules does it import?

Flag any module importing > 5 other internal modules as a coupling smell.

## Anti-Patterns

| ❌ Don't | ✅ Do instead |
|---|---|
| Design for requirements that don't exist yet | YAGNI — build for what's needed now |
| Skip the ADR ("we all know why") | Document every significant decision |
| God modules (one file doing 5 things) | One clear responsibility per module |
| Propose a rewrite to "clean things up" | Targeted improvements serving the current goal |
| Design in isolation without reading existing code | Explore patterns before proposing changes |
