import pandas as pd
from typing import Dict
from sklearn.preprocessing import LabelEncoder, RobustScaler

def preprocess_input(data: pd.DataFrame, encoders: Dict[str, LabelEncoder], scaler: RobustScaler) -> pd.DataFrame:
    # Apply encoders
    for column, encoder in encoders.items():
        if column in data.columns:
            data[column] = encoder.transform(data[column])
    
    # Apply scaler
    numerical_columns = ['squareMeters', 'rooms', 'floor', 'floorCount', 'buildYear', 'poiCount']
    data[numerical_columns] = scaler.transform(data[numerical_columns])
    
    return data
