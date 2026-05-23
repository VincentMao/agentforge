"""Unit tests for TabularLitModule."""

from __future__ import annotations

import torch
import torch.optim as optim
import pytest

from src.models.components.mlp import MLP
from src.models.module import TabularLitModule


@pytest.fixture
def mlp() -> MLP:
    return MLP(input_dim=10, hidden_dims=[32, 64], output_dim=2)


@pytest.fixture
def module(mlp: MLP) -> TabularLitModule:
    def adam_partial(params: torch.nn.parameter.Parameter) -> optim.Adam:
        return optim.Adam(params, lr=1e-3)

    return TabularLitModule(net=mlp, optimizer=adam_partial)


def test_module_forward_shape(
    module: TabularLitModule,
    sample_batch: tuple[torch.Tensor, torch.Tensor],
) -> None:
    x, _ = sample_batch
    logits = module(x)
    assert logits.shape == (16, 2)


def test_module_training_step_returns_loss(
    module: TabularLitModule,
    sample_batch: tuple[torch.Tensor, torch.Tensor],
) -> None:
    loss = module.training_step(sample_batch, batch_idx=0)
    assert isinstance(loss, torch.Tensor)
    assert loss.ndim == 0  # scalar
    assert loss.item() > 0


def test_module_configure_optimizers_returns_dict(
    module: TabularLitModule,
) -> None:
    result = module.configure_optimizers()
    assert "optimizer" in result
    assert isinstance(result["optimizer"], optim.Adam)


def test_module_configure_optimizers_with_scheduler(mlp: MLP) -> None:
    def adam_partial(params: torch.nn.parameter.Parameter) -> optim.Adam:
        return optim.Adam(params, lr=1e-3)

    def scheduler_partial(
        optimizer: optim.Optimizer,
    ) -> optim.lr_scheduler.ReduceLROnPlateau:
        return optim.lr_scheduler.ReduceLROnPlateau(optimizer)

    mod = TabularLitModule(net=mlp, optimizer=adam_partial, scheduler=scheduler_partial)
    result = mod.configure_optimizers()
    assert "lr_scheduler" in result


def test_mlp_wrong_final_layer_raises() -> None:
    """MLP ending with non-Linear raises AssertionError."""
    import torch.nn as nn

    bad_net = MLP(input_dim=10, hidden_dims=[32], output_dim=2)
    bad_net.network = nn.Sequential(nn.Linear(10, 2), nn.ReLU())  # ends with ReLU

    def adam_partial(params: torch.nn.parameter.Parameter) -> optim.Adam:
        return optim.Adam(params, lr=1e-3)

    with pytest.raises(AssertionError, match="nn.Linear"):
        TabularLitModule(net=bad_net, optimizer=adam_partial)
