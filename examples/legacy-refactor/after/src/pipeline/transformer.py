"""Feature transformations — pure functions, no side effects."""

import math

import pandas as pd


def scale_linear(df: pd.DataFrame, col: str, factor: float = 2.0) -> pd.DataFrame:
    """Multiply a column by a scalar factor.

    Args:
        df: Input DataFrame. Not modified in place.
        col: Column to scale.
        factor: Multiplication factor. Defaults to 2.0.

    Returns:
        New DataFrame with the column scaled. Input is unchanged.

    Raises:
        KeyError: If col is not in df.columns.
    """
    if col not in df.columns:
        raise KeyError(f"Column '{col}' not found in DataFrame")
    result = df.copy()
    result[col] = result[col] * factor
    return result


def normalize(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Z-score normalize a column (mean=0, std=1).

    Args:
        df: Input DataFrame. Not modified in place.
        col: Column to normalize.

    Returns:
        New DataFrame with the column normalized. Input is unchanged.

    Raises:
        KeyError: If col is not in df.columns.
        ValueError: If the column has zero standard deviation.

    Example:
        >>> result = normalize(df, "feat2")
        >>> abs(result["feat2"].mean()) < 1e-6
        True
    """
    if col not in df.columns:
        raise KeyError(f"Column '{col}' not found in DataFrame")

    std = df[col].std()
    if std == 0 or math.isnan(std):
        raise ValueError(
            f"Column '{col}' has zero standard deviation; cannot normalize"
        )

    result = df.copy()
    result[col] = (result[col] - result[col].mean()) / std
    return result
