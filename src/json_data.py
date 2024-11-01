import pandas as pd


def create_df(filename):
    df = pd.read_json(filename)
    return pd.json_normalize(df["doughnut_data"])


def increase_price(df, percentage):
    df["price"] = df["price"] * ((100 + percentage) / 100)
    return df


def get_best_value(df):
    df["cost_per_calorie"] = df["price"] / df["calories"]
    return df.nsmallest(1, "cost_per_calorie")
