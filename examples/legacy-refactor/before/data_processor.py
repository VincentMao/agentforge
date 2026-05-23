# data_processor.py
# Classic research code: written fast, never refactored.
# "It works on my machine." No types. No tests. One function does everything.

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

data = None     # global state — breaks predict() if process() not called first
model = None    # global state


def process():
    global data, model

    # load and clean
    df = pd.read_csv('data.csv')
    df = df.dropna()
    df['feat1'] = df['feat1'].apply(lambda x: x*2)
    df['feat2'] = (df['feat2'] - df['feat2'].mean()) / df['feat2'].std()
    data = df

    # train
    X = df[['feat1', 'feat2', 'feat3']]
    y = df['label']
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    # save
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("done!")

    return model.score(X, y)


def predict(x1, x2, x3):
    # crashes with AttributeError if process() not called first
    return model.predict([[x1, x2, x3]])
