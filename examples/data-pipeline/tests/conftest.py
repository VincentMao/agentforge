"""Shared fixtures for data-pipeline tests."""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import torch


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """100-row tabular DataFrame with 10 features and binary label."""
    rng = np.random.default_rng(42)
    X = rng.standard_normal((100, 10))
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    df = pd.DataFrame(X, columns=[f"feat_{i}" for i in range(10)])
    df["label"] = y
    return df


@pytest.fixture
def tmp_data_dir(sample_dataframe: pd.DataFrame, tmp_path: Path) -> Iterator[Path]:
    """Temporary directory with dataset.csv pre-populated."""
    sample_dataframe.to_csv(tmp_path / "dataset.csv", index=False)
    yield tmp_path


@pytest.fixture
def sample_batch() -> tuple[torch.Tensor, torch.Tensor]:
    """A small batch of (features, labels) tensors."""
    return torch.randn(16, 10), torch.randint(0, 2, (16,))
