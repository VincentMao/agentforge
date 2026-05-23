"""Shared pytest fixtures for the legacy-refactor after/ example."""

import pytest
import numpy as np
import pandas as pd


@pytest.fixture
def sample_df() -> pd.DataFrame:
    """100-row DataFrame with controlled seed."""
    rng = np.random.default_rng(42)
    return pd.DataFrame({
        "feat1": rng.standard_normal(100),
        "feat2": rng.standard_normal(100),
        "feat3": rng.standard_normal(100),
        "label": rng.integers(0, 2, 100),
    })


@pytest.fixture
def single_row_df() -> pd.DataFrame:
    """Single-row DataFrame for edge case tests (std=0 scenario)."""
    return pd.DataFrame({
        "feat1": [5.0],
        "feat2": [3.0],
        "feat3": [1.0],
        "label": [1],
    })
