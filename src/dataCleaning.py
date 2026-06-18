import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def filter_countries(df, country):
    return df[df["country"] == country]

def filter_years(df, start_year, end_year):
    return df[(df["year"] >= start_year) & (df["year"] <= end_year)]

def convert_numbers_from_scientific(df, value):
    df[value] = df[value].astype("int64")
    return df