"""Custom learning rate schedulers.

Drop-in replacements for standard torch schedulers with additional features.
"""

from __future__ import annotations

import math

import torch.optim as optim


class WarmupCosineScheduler(optim.lr_scheduler.LRScheduler):
    """Linear warmup followed by cosine annealing to min_lr.

    Commonly used in transformer and large-model training where cold-start
    instability benefits from a gentle ramp-up period.

    Args:
        optimizer: Wrapped optimizer.
        warmup_steps: Number of steps for linear warmup phase.
        total_steps: Total training steps (warmup + cosine decay).
        min_lr: Minimum learning rate at the end of cosine decay.
        last_epoch: Last epoch index (for resuming; default -1 starts fresh).

    Example:
        >>> scheduler = WarmupCosineScheduler(optimizer, warmup_steps=100, total_steps=1000)
        >>> for step in range(1000):
        ...     optimizer.step()
        ...     scheduler.step()
    """

    def __init__(
        self,
        optimizer: optim.Optimizer,
        warmup_steps: int,
        total_steps: int,
        min_lr: float = 1e-6,
        last_epoch: int = -1,
    ) -> None:
        self.warmup_steps = warmup_steps
        self.total_steps = total_steps
        self.min_lr = min_lr
        super().__init__(optimizer, last_epoch)

    def get_lr(self) -> list[float]:
        """Compute LR for the current step."""
        step = self.last_epoch
        if step < self.warmup_steps:
            scale = step / max(1, self.warmup_steps)
        else:
            progress = (step - self.warmup_steps) / max(
                1, self.total_steps - self.warmup_steps
            )
            scale = 0.5 * (1 + math.cos(math.pi * progress))
        return [max(self.min_lr, base_lr * scale) for base_lr in self.base_lrs]
