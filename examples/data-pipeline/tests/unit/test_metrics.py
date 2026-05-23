"""Unit tests for custom metrics."""

from __future__ import annotations

import torch
import pytest

from src.utils.metrics import top_k_accuracy


def test_top_k_accuracy_perfect_predictions() -> None:
    logits = torch.tensor([[10.0, 0.0, 0.0], [0.0, 10.0, 0.0]])
    targets = torch.tensor([0, 1])
    acc = top_k_accuracy(logits, targets, k=1)
    assert acc == pytest.approx(1.0)


def test_top_k_accuracy_all_wrong() -> None:
    logits = torch.tensor([[0.0, 10.0, 0.0], [10.0, 0.0, 0.0]])
    targets = torch.tensor([0, 1])
    acc = top_k_accuracy(logits, targets, k=1)
    assert acc == pytest.approx(0.0)


def test_top_k_accuracy_top3_includes_correct() -> None:
    # True label is 2, model ranks it 3rd
    logits = torch.tensor([[10.0, 5.0, 1.0]])
    targets = torch.tensor([2])
    assert top_k_accuracy(logits, targets, k=3) == pytest.approx(1.0)
    assert top_k_accuracy(logits, targets, k=1) == pytest.approx(0.0)
