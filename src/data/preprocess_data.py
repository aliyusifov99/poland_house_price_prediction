# src/data/preprocess_data.py
import pandas as pd
from sklearn.model_selection import train_test_split
from load_data import load_housing_data, load_rent_data
from data_utils import drop_id_column, encode_city_column, impute_type_column, encode_type_column, normalize_numerical_features, impute_floor_column, convert_floor_to_int, impute_floorCount_column, convert_floorCount_to_int

def preprocess_data(df):
    # Drop ID column
    df = drop_id_column(df)

    # Impute missing values in the 'type' column
    df = impute_type_column(df)
    
    # Impute missing values in the 'floor' column and convert to integer
    df = impute_floor_column(df)
    df = convert_floor_to_int(df)
    
    # Impute missing values in the 'floorCount' column and convert to integer
    df = impute_floorCount_column(df)
    df = convert_floorCount_to_int(df)
    
    # Split the data into training and test sets
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    # Encode city and type columns
    train_df, test_df = encode_city_column(train_df, test_df)
    train_df, test_df = encode_type_column(train_df, test_df)
    
    # Normalize numerical features
    numerical_columns = ['squareMeters', 'rooms', 'floor', 'floorCount']  # Add other numerical columns as needed
    train_df, test_df = normalize_numerical_features(train_df, test_df, numerical_columns)
    
    return train_df, test_df

if __name__ == "__main__":
    # Load raw data
    housing_data = load_housing_data()
    rent_data = load_rent_data()

    # Preprocess data
    train_housing, test_housing = preprocess_data(housing_data)
    train_rent, test_rent = preprocess_data(rent_data)

    # Save processed data
    train_housing.to_csv('data/processed/housing/train_housing.csv', index=False)
    test_housing.to_csv('data/processed/housing/test_housing.csv', index=False)
    train_rent.to_csv('data/processed/rent/train_rent.csv', index=False)
    test_rent.to_csv('data/processed/rent/test_rent.csv', index=False)
