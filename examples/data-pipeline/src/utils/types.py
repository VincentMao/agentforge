"""Shared type definitions for the data pipeline."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TrainingMetrics:
    """Metrics collected at the end of a training run.

    Args:
        train_loss: Final training loss.
        val_loss: Final validation loss.
        val_acc: Final validation accuracy.
        test_acc: Test accuracy (None if test phase was skipped).
        test_f1: Test macro-F1 score (None if test phase was skipped).
    """

    train_loss: float
    val_loss: float
    val_acc: float
    test_acc: float | None = None
    test_f1: float | None = None
