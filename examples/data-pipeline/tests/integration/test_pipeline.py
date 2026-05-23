"""Integration test: end-to-end training loop with real data."""

from __future__ import annotations

from pathlib import Path

import torch
import torch.optim as optim

import lightning as L

from src.data.datamodule import TabularDataModule
from src.models.components.mlp import MLP
from src.models.module import TabularLitModule


def test_full_training_loop_completes(tmp_data_dir: Path) -> None:
    """Train for 1 epoch end-to-end without errors."""
    L.seed_everything(42)

    dm = TabularDataModule(data_dir=str(tmp_data_dir), batch_size=32)
    dm.prepare_data()

    net = MLP(input_dim=10, hidden_dims=[32], output_dim=2)

    def adam_partial(params: torch.nn.parameter.Parameter) -> optim.Adam:
        return optim.Adam(params, lr=1e-3)

    model = TabularLitModule(net=net, optimizer=adam_partial)

    trainer = L.Trainer(
        max_epochs=1,
        enable_progress_bar=False,
        enable_model_summary=False,
        logger=False,
    )
    trainer.fit(model=model, datamodule=dm)

    assert "val/loss" in trainer.callback_metrics
    assert "val/acc" in trainer.callback_metrics


def test_test_phase_produces_metrics(tmp_data_dir: Path) -> None:
    """Test phase runs and produces test/acc and test/f1."""
    L.seed_everything(42)

    dm = TabularDataModule(data_dir=str(tmp_data_dir), batch_size=32)
    dm.prepare_data()

    net = MLP(input_dim=10, hidden_dims=[32], output_dim=2)

    def adam_partial(params: torch.nn.parameter.Parameter) -> optim.Adam:
        return optim.Adam(params, lr=1e-3)

    model = TabularLitModule(net=net, optimizer=adam_partial)

    trainer = L.Trainer(
        max_epochs=1,
        enable_progress_bar=False,
        enable_model_summary=False,
        logger=False,
    )
    trainer.fit(model=model, datamodule=dm)
    trainer.test(model=model, datamodule=dm)

    assert "test/acc" in trainer.callback_metrics
    assert "test/f1" in trainer.callback_metrics
