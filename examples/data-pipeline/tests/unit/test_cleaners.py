"""Unit tests for data cleaning utilities."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from src.data.components.cleaners import clip_outliers, drop_nulls


@pytest.fixture
def sample_df() -> pd.DataFrame:
    rng = np.random.default_rng(42)
    return pd.DataFrame(
        {"a": rng.standard_normal(50), "b": rng.standard_normal(50)}
    )


def test_drop_nulls_removes_high_null_rows() -> None:
    df = pd.DataFrame({"a": [1.0, None, 3.0], "b": [None, None, 3.0]})
    result = drop_nulls(df, threshold=0.4)
    # row 0: 1 null / 2 cols = 50% > 40% → dropped
    # row 1: 2 nulls / 2 cols = 100% → dropped
    # row 2: 0 nulls → kept
    assert len(result) == 1
    assert result["a"].iloc[0] == pytest.approx(3.0)


def test_drop_nulls_keeps_clean_rows(sample_df: pd.DataFrame) -> None:
    result = drop_nulls(sample_df)
    assert len(result) == len(sample_df)


def test_clip_outliers_bounds_extreme_values(sample_df: pd.DataFrame) -> None:
    # Insert extreme outlier
    sample_df.loc[0, "a"] = 1000.0
    result = clip_outliers(sample_df, cols=["a"], n_std=3.0)
    mean = sample_df["a"].mean()
    std = sample_df["a"].std()
    assert result["a"].max() <= mean + 3.0 * std + 1e-6


def test_clip_outliers_does_not_modify_input(sample_df: pd.DataFrame) -> None:
    original_max = sample_df["a"].max()
    clip_outliers(sample_df, cols=["a"])
    assert sample_df["a"].max() == pytest.approx(original_max)


def test_clip_outliers_raises_on_missing_column(sample_df: pd.DataFrame) -> None:
    with pytest.raises(KeyError, match="nonexistent"):
        clip_outliers(sample_df, cols=["nonexistent"])
