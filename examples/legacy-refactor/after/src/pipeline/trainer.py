"""Model training — orchestrates loader + transformer + sklearn model."""

from __future__ import annotations

import pickle
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from .loader import load_csv
from .transformer import normalize, scale_linear
from ..utils.types import PipelineConfig


def run(config: PipelineConfig) -> float:
    """Load data, transform features, train model, persist, return train accuracy.

    Args:
        config: Pipeline configuration defining paths, features, and hyperparameters.

    Returns:
        Training accuracy score (float in [0, 1]).

    Raises:
        FileNotFoundError: If config.data_path does not exist.
        KeyError: If required feature columns are missing from the data.
    """
    df = load_csv(
        config.data_path,
        config.feature_cols + [config.label_col],
    )
    df = scale_linear(df, config.feature_cols[0])
    df = normalize(df, config.feature_cols[1])

    X = df[config.feature_cols].values
    y = df[config.label_col].values

    clf = RandomForestClassifier(
        n_estimators=config.n_estimators,
        random_state=config.random_state,
    )
    clf.fit(X, y)

    config.model_path.parent.mkdir(parents=True, exist_ok=True)
    with config.model_path.open("wb") as f:
        pickle.dump(clf, f)

    return float(clf.score(X, y))
