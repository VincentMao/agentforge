# data-pipeline

Production-quality ML pipeline following the vizard_project / lightning-hydra-template pattern.
PyTorch Lightning handles the training loop; Hydra handles YAML-driven configuration.

## Quick Start

```bash
pip install -e ".[dev]"
make train        # synthetic data generated automatically
make check        # lint + typecheck + test
```

## Architecture

```
configs/           YAML hierarchy — one file per concern
  train.yaml       Main entry point: compose defaults + CLI overrides
  data/tabular.yaml
  model/mlp.yaml
  experiment/baseline.yaml   Override multiple sections at once
src/
  train.py         Entry point: Hydra → datamodule + model + trainer
  eval.py          Eval-only: load checkpoint → test
  data/datamodule.py         LightningDataModule: prepare + split + load
  data/components/           Pure data functions (cleaners, transformers)
  models/module.py           LightningModule: steps + metrics + optimizer
  models/components/mlp.py   Pure PyTorch architecture
  optimizers/schedulers.py   Custom LR schedulers
  utils/                     Instantiators, metrics, types
tests/
  unit/            Isolated module tests (no training)
  integration/     End-to-end training loop tests
```

## Common Commands

```bash
# Train with defaults
make train

# Train with experiment override
python src/train.py experiment=baseline

# Override individual hyperparameters
python src/train.py model.optimizer.lr=0.01 trainer.max_epochs=50

# Hyperparameter sweep (Hydra multirun)
python src/train.py seed=1,2,3 --multirun

# Evaluate from checkpoint
python src/eval.py ckpt_path=logs/checkpoints/best.ckpt
```

## Extending This Pipeline

**New model architecture:**
1. Create `src/models/components/your_model.py` (pure PyTorch, no Lightning)
2. Create `configs/model/your_model.yaml` (set `net._target_`)
3. Add tests in `tests/unit/test_your_model.py`
4. Train: `python src/train.py model=your_model`

**New dataset:**
1. Create `configs/data/your_data.yaml`
2. Create `src/data/your_datamodule.py` if schema differs
3. Add tests for the new DataModule

## When Claude Helps With This Codebase

```
/10x-data-scientist   Experiment design and reproducibility
/unit-testing         Generate tests for new modules
/code-reviewer        Before committing changes
/architecture-review  When adding new subsystems
```

Always run `make check` before committing.
