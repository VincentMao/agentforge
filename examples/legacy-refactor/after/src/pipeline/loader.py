"""Data loading with validation."""

from pathlib import Path

import pandas as pd


def load_csv(path: Path, required_cols: list[str]) -> pd.DataFrame:
    """Load a CSV file and validate required columns exist.

    Args:
        path: Path to the CSV file.
        required_cols: Column names that must be present.

    Returns:
        Loaded DataFrame with rows containing NaN values dropped.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        KeyError: If any required column is missing from the file.

    Example:
        >>> df = load_csv(Path("data.csv"), ["feat1", "feat2", "label"])
        >>> len(df) > 0
        True
    """
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    df = pd.read_csv(path).dropna()

    missing = set(required_cols) - set(df.columns)
    if missing:
        raise KeyError(f"Missing required columns: {missing}")

    return df
