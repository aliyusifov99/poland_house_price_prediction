# src/data/load_data.py
import pandas as pd

def load_housing_data(path='data/raw/housing/apartments.csv'):
    return pd.read_csv(path)

def load_rent_data(path='data/raw/rent/rent.csv'):
    return pd.read_csv(path)

if __name__ == "__main__":
    housing_data = load_housing_data()
    rent_data = load_rent_data()
    print(housing_data.head())
    print(rent_data.head())
