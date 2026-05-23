# data-pipeline

> A production ML training pipeline: PyTorch Lightning + Hydra config system. Mirrors the vizard_project pattern used at Meta.

## Run in 30 Seconds

```bash
pip install -e ".[dev]"
make train   # synthetic data auto-generated
```

Output:
```
Epoch 29: train/loss=0.142 val/loss=0.149 val/acc=0.941
```

## The Pattern

| Layer | Tool | What it does |
|---|---|---|
| Config | Hydra | Compose YAML files, CLI overrides, multirun sweeps |
| Training loop | Lightning | Training/val/test hooks, callbacks, checkpointing |
| Architecture | PyTorch | Pure `nn.Module` — no training logic |
| Metrics | torchmetrics | Accuracy, F1, top-k — stateful, GPU-safe |

## Experiment Override System

```bash
# Run baseline experiment (overrides multiple config sections)
python src/train.py experiment=baseline

# Override one hyperparameter
python src/train.py model.optimizer.lr=0.001

# Multirun sweep
python src/train.py "model.optimizer.lr=0.001,0.0001,0.00001" --multirun
```

## Quality Gates

```bash
make check   # ruff + mypy + pytest (80% coverage minimum)
make test    # tests only with coverage report
```

## See Also

- `CLAUDE.md` — how to work in this codebase with Claude Code
- `configs/experiment/` — pre-built experiment configs to copy/extend
- `src/models/components/` — add your model architecture here
