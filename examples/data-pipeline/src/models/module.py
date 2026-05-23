"""LightningModule: training hooks, metrics, and optimizer configuration.

Separates training logic from model architecture (architecture is in components/).
Mirrors the vizard_project LitModule pattern with per-step logging and epoch callbacks.
"""

from __future__ import annotations

from typing import Any, Callable

import lightning as L
import torch
import torch.nn as nn
from torchmetrics import Accuracy, F1Score

from src.models.components.mlp import MLP


class TabularLitModule(L.LightningModule):
    """Lightning training module for tabular classification.

    Handles training/validation/test steps, metric tracking, and optimizer setup.
    Uses partial callables from Hydra config for optimizer and scheduler instantiation.

    Args:
        net: Initialized model architecture (e.g., MLP).
        optimizer: Partial optimizer callable; called with params= at configure_optimizers.
        scheduler: Optional partial LR scheduler callable.
        compile: Whether to torch.compile the model (PyTorch 2.0+).
    """

    def __init__(
        self,
        net: MLP,
        optimizer: Callable[..., torch.optim.Optimizer],
        scheduler: Callable[..., torch.optim.lr_scheduler.LRScheduler] | None = None,
        compile: bool = False,
    ) -> None:
        super().__init__()
        # Callables can't be pickled for checkpointing — store separately
        self.save_hyperparameters(ignore=["net", "optimizer", "scheduler"])
        self.optimizer_partial = optimizer
        self.scheduler_partial = scheduler
        self.net = net
        self.criterion = nn.CrossEntropyLoss()

        last_layer = net.network[-1]
        assert isinstance(last_layer, nn.Linear), "MLP must end with nn.Linear"
        num_classes = last_layer.out_features

        self.train_acc = Accuracy(task="multiclass", num_classes=num_classes)
        self.val_acc = Accuracy(task="multiclass", num_classes=num_classes)
        self.test_acc = Accuracy(task="multiclass", num_classes=num_classes)
        self.test_f1 = F1Score(
            task="multiclass", num_classes=num_classes, average="macro"
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Run forward pass through the network."""
        return self.net(x)

    def _shared_step(
        self, batch: tuple[torch.Tensor, torch.Tensor]
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Compute loss and predictions for a batch.

        Returns:
            Tuple of (loss, predictions, targets).
        """
        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y)
        preds = torch.argmax(logits, dim=1)
        return loss, preds, y

    def training_step(
        self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> torch.Tensor:
        loss, preds, targets = self._shared_step(batch)
        self.train_acc(preds, targets)
        self.log("train/loss", loss, on_step=False, on_epoch=True, prog_bar=True)
        self.log("train/acc", self.train_acc, on_step=False, on_epoch=True)
        return loss

    def validation_step(
        self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> None:
        loss, preds, targets = self._shared_step(batch)
        self.val_acc(preds, targets)
        self.log("val/loss", loss, on_step=False, on_epoch=True, prog_bar=True)
        self.log("val/acc", self.val_acc, on_step=False, on_epoch=True)

    def test_step(
        self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> None:
        loss, preds, targets = self._shared_step(batch)
        self.test_acc(preds, targets)
        self.test_f1(preds, targets)
        self.log("test/loss", loss)
        self.log("test/acc", self.test_acc)
        self.log("test/f1", self.test_f1)

    def on_train_epoch_end(self) -> None:
        """Called at the end of each training epoch. Add custom logic here."""

    def on_validation_epoch_end(self) -> None:
        """Called at the end of each validation epoch."""

    def configure_optimizers(self) -> dict[str, Any]:
        """Set up optimizer and optional LR scheduler.

        Returns:
            Dict with optimizer and (optionally) lr_scheduler config.
        """
        optimizer = self.optimizer_partial(params=self.parameters())
        if self.scheduler_partial is None:
            return {"optimizer": optimizer}
        scheduler = self.scheduler_partial(optimizer=optimizer)
        return {
            "optimizer": optimizer,
            "lr_scheduler": {
                "scheduler": scheduler,
                "monitor": "val/loss",
                "interval": "epoch",
                "frequency": 1,
            },
        }
