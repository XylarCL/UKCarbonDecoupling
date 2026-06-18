def create_gdp_per_metrics(df):
    df["gdp_per_capita"] = df["gdp"]/df["population"]
    return df


def create_percentage_metrics(df, value):
    df[value + "_percent_1990"] = df[value]/df[value].iloc[0] * 100
    return df