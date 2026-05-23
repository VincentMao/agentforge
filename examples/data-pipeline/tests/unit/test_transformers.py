"""Unit tests for feature transformation utilities."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from src.data.components.transformers import log1p_transform, z_score_normalize


@pytest.fixture
def sample_df() -> pd.DataFrame:
    rng = np.random.default_rng(42)
    return pd.DataFrame(
        {"a": rng.standard_normal(50) + 5, "b": rng.standard_normal(50) + 3}
    )


def test_z_score_normalize_produces_zero_mean(sample_df: pd.DataFrame) -> None:
    result = z_score_normalize(sample_df, ["a"])
    assert result["a"].mean() == pytest.approx(0.0, abs=1e-6)


def test_z_score_normalize_produces_unit_std(sample_df: pd.DataFrame) -> None:
    result = z_score_normalize(sample_df, ["a"])
    assert result["a"].std() == pytest.approx(1.0, abs=1e-6)


def test_z_score_normalize_does_not_modify_input(sample_df: pd.DataFrame) -> None:
    original_mean = sample_df["a"].mean()
    z_score_normalize(sample_df, ["a"])
    assert sample_df["a"].mean() == pytest.approx(original_mean)


def test_z_score_normalize_raises_on_missing_column(sample_df: pd.DataFrame) -> None:
    with pytest.raises(KeyError, match="nonexistent"):
        z_score_normalize(sample_df, ["nonexistent"])


def test_z_score_normalize_raises_on_constant_column() -> None:
    df = pd.DataFrame({"a": [5.0] * 10})
    with pytest.raises(ValueError, match="zero std"):
        z_score_normalize(df, ["a"])


def test_log1p_transform_reduces_range(sample_df: pd.DataFrame) -> None:
    result = log1p_transform(sample_df, ["a"])
    assert result["a"].max() < sample_df["a"].max()


def test_log1p_transform_raises_on_negative_values() -> None:
    df = pd.DataFrame({"a": [-1.0, 2.0, 3.0]})
    with pytest.raises(ValueError, match="negative"):
        log1p_transform(df, ["a"])


def test_log1p_transform_raises_on_missing_column(sample_df: pd.DataFrame) -> None:
    with pytest.raises(KeyError, match="nonexistent"):
        log1p_transform(sample_df, ["nonexistent"])
