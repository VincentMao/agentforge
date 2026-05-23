# configs/

Hydra YAML configuration hierarchy. Each subdirectory is one config group.

## How Hydra Composes This

`train.yaml` defines the `defaults` list — which config from each group to use.
Override at runtime with CLI: `python src/train.py model.optimizer.lr=0.01`

## Config Groups

| Directory | Controls |
|---|---|
| `data/` | Dataset path, batch size, train/val/test split |
| `model/` | Architecture, optimizer, LR scheduler |
| `callbacks/` | ModelCheckpoint, EarlyStopping, etc. |
| `trainer/` | Lightning Trainer: epochs, gradient clipping, GPU |
| `logger/` | WandbLogger, TensorBoardLogger |
| `experiment/` | Override multiple groups at once for a named experiment |

## Running an Experiment

```bash
# Use the baseline experiment (overrides data + model)
python src/train.py experiment=baseline

# Override a single value
python src/train.py model.optimizer.lr=0.0001

# Multirun sweep
python src/train.py "model.optimizer.lr=0.001,0.0001" --multirun
```
