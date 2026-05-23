"""Training entry point. Run: python src/train.py [overrides]

Examples:
    python src/train.py
    python src/train.py experiment=baseline
    python src/train.py model.optimizer.lr=0.01 trainer.max_epochs=50
    python src/train.py seed=1,2,3 --multirun
"""

from __future__ import annotations

import hydra
import lightning as L
from omegaconf import DictConfig

from src.utils.instantiators import instantiate_callbacks, instantiate_loggers


@hydra.main(version_base=None, config_path="../configs", config_name="train")
def train(cfg: DictConfig) -> float | None:
    """Run the full training (and optionally test) pipeline.

    Args:
        cfg: Hydra config composed from configs/train.yaml + overrides.

    Returns:
        Final val/acc metric, or None if training was skipped.
    """
    if cfg.get("seed"):
        L.seed_everything(cfg.seed, workers=True)

    datamodule: L.LightningDataModule = hydra.utils.instantiate(cfg.data)
    model: L.LightningModule = hydra.utils.instantiate(cfg.model)
    callbacks = instantiate_callbacks(cfg.get("callbacks"))
    loggers = instantiate_loggers(cfg.get("logger"))

    trainer: L.Trainer = hydra.utils.instantiate(
        cfg.trainer, callbacks=callbacks, logger=loggers
    )

    if cfg.get("train"):
        trainer.fit(model=model, datamodule=datamodule, ckpt_path=cfg.get("ckpt_path"))

    if cfg.get("test"):
        trainer.test(model=model, datamodule=datamodule, ckpt_path="best")

    val_acc = trainer.callback_metrics.get("val/acc")
    return float(val_acc) if val_acc is not None else None


if __name__ == "__main__":
    train()
