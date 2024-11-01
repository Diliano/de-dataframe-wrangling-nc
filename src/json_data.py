import pandas as pd


def create_df(filename):
    df = pd.read_json(filename)
    return pd.json_normalize(df["doughnut_data"])


def increase_price(df):
    pass


def get_best_value(df):
    pass
