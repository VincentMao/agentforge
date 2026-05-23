# Chapter 4: Research Engineering with LLMs

> This chapter is actively evolving. PRs welcome — especially from practitioners.

## What This Chapter Covers

Applying LLM-assisted development to research codebases: the unique challenges of research code, how to introduce engineering rigor without killing research velocity, and the vizard-pattern ML pipeline.

## Sections

### 1. The Research Code Problem

Research code has a lifecycle:
1. **Notebook prototype**: works, disposable, no tests
2. **Script**: works on the author's machine, not reproducible
3. **"Production" research code**: intended to be reused, actually a script with more flags

The gap between 2 and "actually production-quality" is where most research teams live. This gap causes: "it worked six months ago," "I can't reproduce figure 3," "we need to retrain but no one knows the hyperparameters."

### 2. The Reproducibility Contract

The `10x-data-scientist` skill enforces the minimum reproducibility contract:
- Seed everything: `L.seed_everything(cfg.seed, workers=True)`
- Config-driven: no hardcoded hyperparameters
- Deterministic splits: same seed → same train/val/test
- Checkpoint includes config: load checkpoint → know exact hyperparameters

### 3. The vizard Pattern

The `examples/data-pipeline/` in this repo mirrors Meta's vizard_project pattern (now `ashleve/lightning-hydra-template` in open-source):

```
configs/           Hydra YAML hierarchy
  experiment/      One file per experiment — overrides root config
  data/            Dataset configuration
  model/           Architecture + optimizer + scheduler
  callbacks/       Training callbacks
  trainer/         Lightning Trainer settings

src/
  train.py         Entry point: compose configs → train
  data/            DataModule (data loading, splitting, transforms)
  models/          LightningModule (training logic) + components (architecture)
```

Why this works: **the experiment config is the experiment record**. If you save `configs/experiment/my_experiment.yaml` alongside your results, you have everything needed to reproduce the run.

### 4. Strangler Fig for Research Code

The `examples/legacy-refactor/` shows how to apply the strangler fig pattern to a typical research script (`data_processor.py`) to produce typed, tested, reproducible code without a big-bang rewrite.

Key insight: characterization tests first. Write tests that lock in the current (possibly wrong) behavior before restructuring. This gives you a safety net during the refactor.

### 5. When to Introduce Rigor (and When Not To)

Not every research project benefits from the full engineering stack. Heuristics:
- **Notebook/exploration**: no tests needed; reproducibility via fixed seed
- **Recurring pipeline (weekly retraining)**: DataModule + tests worth the investment
- **Shared infrastructure (used by 3+ people)**: full stack: types, tests, CI

The cost of over-engineering early-stage research is lost velocity. The cost of under-engineering stable pipelines is accumulated technical debt. Match the rigor to the stage.

## Contributing

Add sections with: case studies of research code that became production infrastructure, lessons from failed reproducibility attempts, or LLM-assisted research tooling patterns.
