---
name: 10x-data-scientist
description: Use this for ML/data science work. Enforces reproducibility, config-driven design, and experiment tracking. Activate before writing any training or evaluation code.
---

# 10x Data Scientist

Reproducibility is not optional. An experiment that can't be reproduced is a hypothesis, not a result.

## The Reproducibility Contract

Before writing any training code, confirm:
- [ ] Random seed is set and logged: `L.seed_everything(cfg.seed, workers=True)`
- [ ] All hyperparameters come from config, never hardcoded
- [ ] Dataset splits are deterministic (fixed seed or explicit index files)
- [ ] Model checkpoints are saved with the config that produced them

## Config-Driven Design

Every experiment parameter lives in a YAML config:
```yaml
# configs/experiment/my_experiment.yaml
seed: 42
model:
  optimizer:
    lr: 0.001
data:
  batch_size: 64
  train_val_test_split: [0.7, 0.15, 0.15]
```

Run it: `python src/train.py experiment=my_experiment`

## Data Validation Before Training

Always validate data shape and types before the training loop:
```python
assert X.shape[1] == expected_features, f"Expected {expected_features} features, got {X.shape[1]}"
assert not torch.isnan(X).any(), "NaN values in features"
assert y.min() >= 0 and y.max() < num_classes
```

## Experiment Tracking Checklist

Log these at the start of every run:
- All hyperparameters (`save_hyperparameters()` does this automatically in Lightning)
- Dataset size (train/val/test counts)
- Model parameter count
- Git commit hash

## Anti-Patterns

| ❌ | ✅ |
|---|---|
| `random.seed(42)` in training script | `L.seed_everything(cfg.seed, workers=True)` |
| Hardcoded learning rate | `cfg.model.optimizer.lr` from YAML |
| Manual train/test split in notebook | `DataModule` with fixed split logic |
| "It worked on my machine" | CI that reruns training and checks metrics |
