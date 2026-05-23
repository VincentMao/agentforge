"""Tests for pipeline/transformer.py."""

import pytest
import pandas as pd

from src.pipeline.transformer import normalize, scale_linear


def test_normalize_produces_zero_mean(sample_df: pd.DataFrame) -> None:
    result = normalize(sample_df, "feat1")
    assert result["feat1"].mean() == pytest.approx(0.0, abs=1e-6)


def test_normalize_produces_unit_variance(sample_df: pd.DataFrame) -> None:
    result = normalize(sample_df, "feat1")
    assert result["feat1"].std() == pytest.approx(1.0, abs=1e-6)


def test_normalize_does_not_modify_input(sample_df: pd.DataFrame) -> None:
    original_mean = sample_df["feat1"].mean()
    normalize(sample_df, "feat1")
    assert sample_df["feat1"].mean() == original_mean


def test_normalize_raises_on_missing_column(sample_df: pd.DataFrame) -> None:
    with pytest.raises(KeyError, match="nonexistent"):
        normalize(sample_df, "nonexistent")


def test_normalize_raises_on_zero_std(single_row_df: pd.DataFrame) -> None:
    """A column with std=0 (constant value) cannot be normalized."""
    constant_df = single_row_df.copy()
    constant_df["feat1"] = 1.0
    with pytest.raises(ValueError, match="zero standard deviation"):
        normalize(constant_df, "feat1")


def test_scale_linear_doubles_values_by_default(sample_df: pd.DataFrame) -> None:
    result = scale_linear(sample_df, "feat1")
    pd.testing.assert_series_equal(result["feat1"], sample_df["feat1"] * 2)


def test_scale_linear_does_not_modify_input(sample_df: pd.DataFrame) -> None:
    original = sample_df["feat1"].copy()
    scale_linear(sample_df, "feat1")
    pd.testing.assert_series_equal(sample_df["feat1"], original)


def test_scale_linear_raises_on_missing_column(sample_df: pd.DataFrame) -> None:
    with pytest.raises(KeyError, match="missing_col"):
        scale_linear(sample_df, "missing_col")
