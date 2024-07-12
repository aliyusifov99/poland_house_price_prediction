# src/data/data_utils.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder, RobustScaler

def drop_id_column(df):
    if 'id' in df.columns:
        df = df.drop(columns=['id'])
    return df

def encode_city_column(train_df, test_df):
    le = LabelEncoder()
    train_df['city'] = le.fit_transform(train_df['city'])
    test_df['city'] = le.transform(test_df['city'])
    return train_df, test_df

def impute_type_column(df):
    # Fill missing values in the 'type' column with the most frequent value
    most_frequent_type = df['type'].mode()[0]
    df['type'] = df['type'].fillna(most_frequent_type)
    return df

def encode_type_column(train_df, test_df):
    le = LabelEncoder()
    train_df['type'] = le.fit_transform(train_df['type'])
    test_df['type'] = le.transform(test_df['type'])
    return train_df, test_df

def impute_floor_column(df):
    # Fill missing values in the 'floor' column with the median value
    median_floor = df['floor'].median()
    df['floor'] = df['floor'].fillna(median_floor)
    return df

def convert_floor_to_int(df):
    df['floor'] = df['floor'].astype(int)
    return df

def impute_floorCount_column(df):
    # Fill missing values in the 'floorCount' column with the median value
    median_floorCount = df['floorCount'].median()
    df['floorCount'] = df['floorCount'].fillna(median_floorCount)
    return df

def convert_floorCount_to_int(df):
    df['floorCount'] = df['floorCount'].astype(int)
    return df

def normalize_numerical_features(train_df, test_df, columns):
    scaler = RobustScaler()
    train_df[columns] = scaler.fit_transform(train_df[columns])
    test_df[columns] = scaler.transform(test_df[columns])
    return train_df, test_df
    