# src/models/predict.py
import pandas as pd
import joblib

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def predict(model_path: str, data_path: str) -> pd.DataFrame:
    # Load model
    model = joblib.load(model_path)
    
    # Load data
    data = load_data(data_path)
    
    # Make predictions
    predictions = model.predict(data)
    
    return pd.DataFrame(predictions, columns=['predictions'])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Make predictions")
    parser.add_argument('--model_path', type=str, required=True, help="Path to the trained model")
    parser.add_argument('--data_path', type=str, required=True, help="Path to the data to predict")
    args = parser.parse_args()
    
    predictions = predict(args.model_path, args.data_path)
    print(predictions)
