"""Evaluation-only entry point. Run: python src/eval.py ckpt_path=PATH

Examples:
    python src/eval.py ckpt_path=logs/checkpoints/best.ckpt
    python src/eval.py ckpt_path=best logger=tensorboard
"""

from __future__ import annotations

import hydra
import lightning as L
from omegaconf import DictConfig

from src.utils.instantiators import instantiate_loggers


@hydra.main(version_base=None, config_path="../configs", config_name="eval")
def evaluate(cfg: DictConfig) -> None:
    """Run evaluation on a saved checkpoint.

    Args:
        cfg: Hydra config composed from configs/eval.yaml + overrides.
             ckpt_path is required.
    """
    assert cfg.get("ckpt_path"), "ckpt_path must be provided: python src/eval.py ckpt_path=PATH"

    datamodule: L.LightningDataModule = hydra.utils.instantiate(cfg.data)
    model: L.LightningModule = hydra.utils.instantiate(cfg.model)

    loggers = instantiate_loggers(cfg.get("logger"))
    trainer: L.Trainer = hydra.utils.instantiate(cfg.trainer, logger=loggers)
    trainer.test(model=model, datamodule=datamodule, ckpt_path=cfg.ckpt_path)


if __name__ == "__main__":
    evaluate()
