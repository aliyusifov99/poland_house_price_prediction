import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from custom_label_encoder import CustomLabelEncoder
from load_data import load_housing_data, load_rent_data
from data_utils import (drop_id_column, encode_column, impute_most_frequent, impute_median, convert_to_int,
                         drop_columns, categorize_distance_columns, categorize_centre_distance_column, normalize_numerical_features)
from typing import Tuple, Dict

def preprocess_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, Dict, RobustScaler]:
    # Preprocess the data by applying various transformations
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
    df = categorize_centre_distance_column(df)
    df = impute_most_frequent(df, 'buildingMaterial')
    df = impute_most_frequent(df, 'condition')
    df = impute_most_frequent(df, 'hasElevator')

    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    categorical_columns = ['city', 'type', 'ownership', 'buildingMaterial', 'condition',
                           'schoolDistance', 'clinicDistance', 'postOfficeDistance',
                           'kindergartenDistance', 'restaurantDistance', 'collegeDistance', 'pharmacyDistance',
                           'centreDistance', 'hasParkingSpace', 'hasBalcony', 'hasElevator', 'hasSecurity', 'hasStorageRoom']
    
    encoders = {}
    for column in categorical_columns:
        train_df, test_df, encoder = encode_column(train_df, test_df, column)
        encoders[column] = encoder
    
    numerical_columns = ['squareMeters', 'rooms', 'floor', 'floorCount', 'buildYear', 'poiCount']
    train_df, test_df, scaler = normalize_numerical_features(train_df, test_df, numerical_columns)
    
    return train_df, test_df, encoders, scaler

if __name__ == "__main__":
    housing_data = load_housing_data()
    rent_data = load_rent_data()

    train_housing, test_housing, housing_encoders, housing_scaler = preprocess_data(housing_data)
    train_rent, test_rent, rent_encoders, rent_scaler = preprocess_data(rent_data)

    train_housing.to_csv('data/processed/housing/train_housing.csv', index=False)
    test_housing.to_csv('data/processed/housing/test_housing.csv', index=False)
    train_rent.to_csv('data/processed/rent/train_rent.csv', index=False)
    test_rent.to_csv('data/processed/rent/test_rent.csv', index=False)

    joblib.dump(housing_encoders, 'processors_pickle/housing_encoders.pkl')
    joblib.dump(housing_scaler, 'processors_pickle/housing_scaler.pkl')
    joblib.dump(rent_encoders, 'processors_pickle/rent_encoders.pkl')
    joblib.dump(rent_scaler, 'processors_pickle/rent_scaler.pkl')
