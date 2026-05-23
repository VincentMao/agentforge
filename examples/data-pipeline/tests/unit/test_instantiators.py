"""Unit tests for Hydra config instantiators."""

from __future__ import annotations

from omegaconf import OmegaConf

from src.utils.instantiators import instantiate_callbacks, instantiate_loggers


def test_instantiate_callbacks_returns_empty_for_none() -> None:
    result = instantiate_callbacks(None)
    assert result == []


def test_instantiate_loggers_returns_empty_for_none() -> None:
    result = instantiate_loggers(None)
    assert result == []


def test_instantiate_callbacks_with_real_callback() -> None:
    cfg = OmegaConf.create(
        {
            "early_stopping": {
                "_target_": "lightning.pytorch.callbacks.EarlyStopping",
                "monitor": "val/loss",
                "patience": 5,
                "mode": "min",
            }
        }
    )
    callbacks = instantiate_callbacks(cfg)
    assert len(callbacks) == 1


def test_instantiate_callbacks_skips_non_target_entries() -> None:
    cfg = OmegaConf.create({"plain_value": 42})
    result = instantiate_callbacks(cfg)
    assert result == []
