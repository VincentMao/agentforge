"""Unit tests for custom LR schedulers."""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.optim as optim
import pytest

from src.optimizers.schedulers import WarmupCosineScheduler


@pytest.fixture
def optimizer() -> optim.Adam:
    model = nn.Linear(10, 2)
    return optim.Adam(model.parameters(), lr=0.1)


def test_warmup_increases_lr(optimizer: optim.Adam) -> None:
    scheduler = WarmupCosineScheduler(optimizer, warmup_steps=5, total_steps=20)
    lrs = []
    for _ in range(5):
        scheduler.step()
        lrs.append(optimizer.param_groups[0]["lr"])
    # LR should increase during warmup
    assert lrs[-1] > lrs[0]


def test_cosine_decreases_lr_after_warmup(optimizer: optim.Adam) -> None:
    scheduler = WarmupCosineScheduler(optimizer, warmup_steps=2, total_steps=10)
    # Skip past warmup
    for _ in range(3):
        scheduler.step()
    lr_after_warmup = optimizer.param_groups[0]["lr"]
    # Advance further into cosine decay
    for _ in range(5):
        scheduler.step()
    lr_later = optimizer.param_groups[0]["lr"]
    assert lr_later < lr_after_warmup


def test_lr_never_below_min_lr(optimizer: optim.Adam) -> None:
    min_lr = 1e-4
    scheduler = WarmupCosineScheduler(
        optimizer, warmup_steps=2, total_steps=10, min_lr=min_lr
    )
    for _ in range(15):
        scheduler.step()
    assert optimizer.param_groups[0]["lr"] >= min_lr
