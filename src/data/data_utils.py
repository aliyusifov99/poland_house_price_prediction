# src/data/data_utils.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder, RobustScaler
from typing import Tuple, List

def drop_id_column(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(columns=['id'], errors='ignore')

def encode_column(train_df: pd.DataFrame, test_df: pd.DataFrame, column: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    le = LabelEncoder()
    all_values = list(train_df[column]) + list(test_df[column])
    le.fit(all_values)
    train_df[column] = le.transform(train_df[column])
    test_df[column] = le.transform(test_df[column])
    return train_df, test_df

def impute_most_frequent(df: pd.DataFrame, column: str) -> pd.DataFrame:
    most_frequent = df[column].mode()[0]
    df[column] = df[column].fillna(most_frequent)
    return df

def impute_median(df: pd.DataFrame, column: str) -> pd.DataFrame:
    median_value = df[column].median()
    df[column] = df[column].fillna(median_value)
    return df

def convert_to_int(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[column] = df[column].astype(int)
    return df


def drop_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    return df.drop(columns=columns, errors='ignore')

def categorize_distance_columns(df: pd.DataFrame) -> pd.DataFrame:
    bins = [0, 0.2, 0.5, 1, 2, float('inf')]
    labels = ['Very Close', 'Close', 'Medium', 'Far', 'Very Far']
    distance_columns = ['schoolDistance', 'clinicDistance', 'postOfficeDistance',
                        'kindergartenDistance', 'restaurantDistance', 'collegeDistance', 'pharmacyDistance']
    for column in distance_columns:
        df[column] = pd.cut(df[column], bins=bins, labels=labels)
    return df

def normalize_numerical_features(train_df: pd.DataFrame, test_df: pd.DataFrame, columns: List[str]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    scaler = RobustScaler()
    train_df[columns] = scaler.fit_transform(train_df[columns])
    test_df[columns] = scaler.transform(test_df[columns])
    return train_df, test_df
