"""Hydra config → Python object factories.

Provides helper functions that iterate over a Hydra config dict and
instantiate each object that has a _target_ key. Mirrors the vizard_project
instantiators pattern for callbacks and loggers.
"""

from __future__ import annotations

import hydra
import lightning as L
from omegaconf import DictConfig


def instantiate_callbacks(callbacks_cfg: DictConfig | None) -> list[L.Callback]:
    """Instantiate all callback objects from a Hydra config dict.

    Args:
        callbacks_cfg: Hydra config dict where each value has a _target_ key.
                       Typically from configs/callbacks/*.yaml.

    Returns:
        List of instantiated Lightning callbacks. Empty list if cfg is None.

    Example:
        >>> callbacks = instantiate_callbacks(cfg.callbacks)
        >>> trainer = L.Trainer(callbacks=callbacks)
    """
    callbacks: list[L.Callback] = []
    if callbacks_cfg is None:
        return callbacks
    for _, cb_conf in callbacks_cfg.items():
        if isinstance(cb_conf, DictConfig) and "_target_" in cb_conf:
            callbacks.append(hydra.utils.instantiate(cb_conf))
    return callbacks


def instantiate_loggers(
    logger_cfg: DictConfig | None,
) -> list[L.pytorch.loggers.Logger]:
    """Instantiate all logger objects from a Hydra config dict.

    Args:
        logger_cfg: Hydra config dict where each value has a _target_ key.
                    Typically from configs/logger/*.yaml.

    Returns:
        List of instantiated Lightning loggers. Empty list if cfg is None.
    """
    loggers: list[L.pytorch.loggers.Logger] = []
    if logger_cfg is None:
        return loggers
    for _, lg_conf in logger_cfg.items():
        if isinstance(lg_conf, DictConfig) and "_target_" in lg_conf:
            loggers.append(hydra.utils.instantiate(lg_conf))
    return loggers
