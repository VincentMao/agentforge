"""Custom evaluation metrics beyond torchmetrics defaults."""

from __future__ import annotations

import torch


def top_k_accuracy(
    logits: torch.Tensor, targets: torch.Tensor, k: int = 3
) -> float:
    """Compute top-k accuracy for multi-class classification.

    Args:
        logits: Unnormalized model outputs of shape (N, num_classes).
        targets: Ground-truth class indices of shape (N,).
        k: Number of top predictions to consider correct.

    Returns:
        Fraction of samples where the true class appears in top-k predictions.

    Example:
        >>> acc = top_k_accuracy(logits, targets, k=3)
        >>> print(f"Top-3 accuracy: {acc:.3f}")
    """
    _, top_k = logits.topk(k, dim=1)
    correct = top_k.eq(targets.view(-1, 1).expand_as(top_k))
    return correct.any(dim=1).float().mean().item()
