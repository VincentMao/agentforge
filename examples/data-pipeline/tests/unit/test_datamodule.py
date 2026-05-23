"""Unit tests for TabularDataModule."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.data.datamodule import TabularDataModule


def test_datamodule_creates_three_splits(tmp_data_dir: Path) -> None:
    dm = TabularDataModule(data_dir=str(tmp_data_dir), batch_size=16)
    dm.prepare_data()
    dm.setup("fit")

    assert len(dm.train_dataloader().dataset) > 0
    assert len(dm.val_dataloader().dataset) > 0
    assert len(dm.test_dataloader().dataset) > 0


def test_datamodule_splits_sum_to_dataset_size(tmp_data_dir: Path) -> None:
    dm = TabularDataModule(data_dir=str(tmp_data_dir), batch_size=16)
    dm.prepare_data()
    dm.setup("fit")

    total = (
        len(dm.train_dataloader().dataset)
        + len(dm.val_dataloader().dataset)
        + len(dm.test_dataloader().dataset)
    )
    assert total == 100  # matches sample_dataframe fixture size


def test_datamodule_generates_synthetic_data_if_missing(tmp_path: Path) -> None:
    """If dataset.csv is absent, prepare_data() creates it."""
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()
    dm = TabularDataModule(data_dir=str(empty_dir))
    dm.prepare_data()
    assert (empty_dir / "dataset.csv").exists()


def test_datamodule_batch_shape(tmp_data_dir: Path) -> None:
    dm = TabularDataModule(data_dir=str(tmp_data_dir), batch_size=16)
    dm.prepare_data()
    dm.setup("fit")

    batch = next(iter(dm.train_dataloader()))
    x, y = batch
    assert x.shape[1] == 10  # 10 features
    assert y.shape[0] == x.shape[0]


def test_datamodule_setup_required_before_dataloaders(tmp_data_dir: Path) -> None:
    dm = TabularDataModule(data_dir=str(tmp_data_dir), batch_size=16)
    dm.prepare_data()
    with pytest.raises(AssertionError, match="setup"):
        dm.train_dataloader()
