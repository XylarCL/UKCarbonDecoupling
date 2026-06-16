import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def filter_countries(df, countries):
    return df[df["country"].isin(countries)]

def filter_years(df, start_year, end_year):
    return df[(df["year"] >= start_year) & (df["year"] <= end_year)]

def clean_missing_values(df):
    return df.dropna(subset=["co2", "gdp"])

def convert_numbers(df):
    df["gdp"] = df["gdp"].astype("int64")
    return df