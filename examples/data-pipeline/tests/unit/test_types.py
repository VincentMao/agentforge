"""Unit tests for shared type definitions."""

from __future__ import annotations

import pytest
from src.utils.types import TrainingMetrics


def test_training_metrics_defaults() -> None:
    m = TrainingMetrics(train_loss=0.1, val_loss=0.2, val_acc=0.9)
    assert m.test_acc is None
    assert m.test_f1 is None


def test_training_metrics_with_test_results() -> None:
    m = TrainingMetrics(
        train_loss=0.1, val_loss=0.2, val_acc=0.9, test_acc=0.88, test_f1=0.87
    )
    assert m.test_acc == pytest.approx(0.88)
    assert m.test_f1 == pytest.approx(0.87)


def test_training_metrics_is_frozen() -> None:
    m = TrainingMetrics(train_loss=0.1, val_loss=0.2, val_acc=0.9)
    with pytest.raises(Exception):  # frozen dataclass raises FrozenInstanceError
        m.train_loss = 0.5  # type: ignore[misc]
