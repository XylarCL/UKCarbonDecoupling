

from src2.dataCleaning import (
    load_data,
    filter_countries,
    filter_years,
    clean_missing_values,
    convert_numbers
)

from src2.analysis import (
    visual_normality_test
)

list_countries = ["United Kingdom", "France", "Germany"]
start_year = 1990
end_year = 2022

# Load Data & clean data
co2 = load_data("data/owid-co2-data.csv")
energy = load_data("data//owid-energy-data.csv")

co2 = filter_countries(co2, list_countries)
energy = filter_countries(co2, list_countries)

co2 = filter_years(co2, start_year, end_year)
energy = filter_years(co2, start_year, end_year)

co2 = clean_missing_values(co2)
energy = clean_missing_values(energy)

co2 = convert_numbers(co2)

# Analaysis
visual_normality_test(co2, "gdp", list_countries, start_year, end_year)
visual_normality_test(co2, "total_ghg", list_countries, start_year, end_year)