# src/data/preprocess_data.py
import pandas as pd
from sklearn.model_selection import train_test_split
from load_data import load_housing_data, load_rent_data
from data_utils import (drop_id_column, encode_column, impute_most_frequent, impute_median, convert_to_int,
                         drop_columns, categorize_distance_columns, normalize_numerical_features)
from typing import Tuple

def preprocess_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df = drop_id_column(df)
    df = impute_most_frequent(df, 'type')
    df = impute_median(df, 'floor')
    df = convert_to_int(df, 'floor')
    df = impute_median(df, 'floorCount')
    df = convert_to_int(df, 'floorCount')
    df = impute_median(df, 'buildYear')
    df = convert_to_int(df, 'buildYear')
    df = drop_columns(df, ['longitude', 'latitude'])
    distance_columns = ['schoolDistance', 'clinicDistance', 'postOfficeDistance',
                        'kindergartenDistance', 'restaurantDistance', 'collegeDistance', 'pharmacyDistance']
    for column in distance_columns:
        df = impute_median(df, column)
    df = categorize_distance_columns(df)
    df = impute_most_frequent(df, 'buildingMaterial')
    df = impute_most_frequent(df, 'condition')
    df = impute_most_frequent(df, 'hasElevator')

    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    categorical_columns = ['city', 'type', 'ownership', 'buildingMaterial', 'condition',
                           'schoolDistance', 'clinicDistance', 'postOfficeDistance',
                           'kindergartenDistance', 'restaurantDistance', 'collegeDistance', 'pharmacyDistance',
                           'hasParkingSpace', 'hasBalcony', 'hasElevator', 'hasSecurity', 'hasStorageRoom']
    for column in categorical_columns:
        train_df, test_df = encode_column(train_df, test_df, column)
    
    numerical_columns = ['squareMeters', 'rooms', 'floor', 'floorCount', 'buildYear', 'poiCount', 'price']
    train_df, test_df = normalize_numerical_features(train_df, test_df, numerical_columns)
    
    return train_df, test_df

if __name__ == "__main__":
    housing_data = load_housing_data()
    rent_data = load_rent_data()

    train_housing, test_housing = preprocess_data(housing_data)
    train_rent, test_rent = preprocess_data(rent_data)

    train_housing.to_csv('data/processed/housing/train_housing.csv', index=False)
    test_housing.to_csv('data/processed/housing/test_housing.csv', index=False)
    train_rent.to_csv('data/processed/rent/train_rent.csv', index=False)
    test_rent.to_csv('data/processed/rent/test_rent.csv', index=False)
