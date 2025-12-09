import pandas as pd


def load_site_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

