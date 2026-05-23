"""Tests for pipeline/loader.py."""

import pytest
from pathlib import Path

import pandas as pd

from src.pipeline.loader import load_csv


def test_load_csv_returns_dataframe(tmp_path: Path) -> None:
    csv = tmp_path / "data.csv"
    csv.write_text("feat1,feat2,label\n1.0,2.0,0\n3.0,4.0,1\n")
    result = load_csv(csv, required_cols=["feat1", "feat2", "label"])
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2


def test_load_csv_drops_null_rows(tmp_path: Path) -> None:
    csv = tmp_path / "data.csv"
    csv.write_text("feat1,feat2,label\n1.0,,0\n3.0,4.0,1\n")
    result = load_csv(csv, required_cols=["feat1", "feat2", "label"])
    assert len(result) == 1


def test_load_csv_raises_on_missing_file() -> None:
    with pytest.raises(FileNotFoundError, match="not found"):
        load_csv(Path("/nonexistent/path.csv"), required_cols=[])


def test_load_csv_raises_on_missing_column(tmp_path: Path) -> None:
    csv = tmp_path / "data.csv"
    csv.write_text("feat1,label\n1.0,0\n")
    with pytest.raises(KeyError, match="feat2"):
        load_csv(csv, required_cols=["feat1", "feat2", "label"])
