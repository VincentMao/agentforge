# helpers.py - dump of utilities with no clear ownership

def f1(x): return x * 2
def f2(data, col): return (data[col] - data[col].mean()) / data[col].std()
def load(path):
    import pandas as pd
    return pd.read_csv(path)
def save(obj, path):
    import pickle
    with open(path, 'wb') as f: pickle.dump(obj, f)
def get_score(model, X, y): return model.score(X, y)
