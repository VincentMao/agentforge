"""Tests for pipeline/trainer.py and utils/config.py."""

import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from src.pipeline.trainer import run
from src.utils.config import default_config
from src.utils.types import PipelineConfig


@pytest.fixture
def csv_path(tmp_path: Path) -> Path:
    """Write a small valid CSV and return its path."""
    rng = np.random.default_rng(0)
    df = pd.DataFrame({
        "feat1": rng.standard_normal(50),
        "feat2": rng.standard_normal(50),
        "feat3": rng.standard_normal(50),
        "label": rng.integers(0, 2, 50),
    })
    p = tmp_path / "data.csv"
    df.to_csv(p, index=False)
    return p


def test_run_returns_float_accuracy(tmp_path: Path, csv_path: Path) -> None:
    config = default_config(csv_path, tmp_path / "model.pkl")
    score = run(config)
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0


def test_run_writes_model_file(tmp_path: Path, csv_path: Path) -> None:
    model_path = tmp_path / "models" / "rf.pkl"
    config = default_config(csv_path, model_path)
    run(config)
    assert model_path.exists()


def test_run_model_is_loadable(tmp_path: Path, csv_path: Path) -> None:
    model_path = tmp_path / "model.pkl"
    config = default_config(csv_path, model_path)
    run(config)
    with model_path.open("rb") as f:
        clf = pickle.load(f)
    assert hasattr(clf, "predict")


def test_run_raises_on_missing_csv(tmp_path: Path) -> None:
    config = default_config(
        tmp_path / "nonexistent.csv",
        tmp_path / "model.pkl",
    )
    with pytest.raises(FileNotFoundError):
        run(config)


def test_default_config_feature_cols(tmp_path: Path) -> None:
    config = default_config(tmp_path / "d.csv", tmp_path / "m.pkl")
    assert config.feature_cols == ["feat1", "feat2", "feat3"]
    assert config.label_col == "label"
    assert config.n_estimators == 100


def test_pipeline_config_is_frozen(tmp_path: Path) -> None:
    config = default_config(tmp_path / "d.csv", tmp_path / "m.pkl")
    with pytest.raises((AttributeError, TypeError)):
        config.n_estimators = 999  # type: ignore[misc]
