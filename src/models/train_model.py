# src/models/train_model.py
import os
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import lightgbm as lgb
import xgboost as xgb
from catboost import CatBoostRegressor
import joblib

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def train_model(train_path: str, model_type: str, model_name: str, experiment_name: str) -> None:
    # Load data
    df = load_data(train_path)
    
    # Split data into train and validation sets
    train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)
    
    # Separate features and target
    X_train = train_df.drop(columns=['price'])
    y_train = train_df['price']
    X_val = val_df.drop(columns=['price'])
    y_val = val_df['price']
    
    # Initialize model
    if model_type == 'random_forest':
        model = RandomForestRegressor()
    elif model_type == 'lightgbm':
        model = lgb.LGBMRegressor()
    elif model_type == 'xgboost':
        model = xgb.XGBRegressor()
    elif model_type == 'catboost':
        model = CatBoostRegressor(verbose=0)
    else:
        raise ValueError("Invalid model type")
    
    # Start an MLflow run
    mlflow.set_experiment(experiment_name)
    with mlflow.start_run(run_name=model_name):
        # Train model
        print(f"Training {model_name} model")
        model.fit(X_train, y_train)
        
        # Predict on training set
        y_train_pred = model.predict(X_train)
        train_r2 = r2_score(y_train, y_train_pred)
        mlflow.log_metric('train_r2', train_r2)
        
        # Predict on validation set
        y_val_pred = model.predict(X_val)
        val_mse = mean_squared_error(y_val, y_val_pred)
        val_r2 = r2_score(y_val, y_val_pred)
        mlflow.log_metric('val_mse', val_mse)
        mlflow.log_metric('val_r2', val_r2)
        
        # Log model parameters
        mlflow.log_params(model.get_params())
        
        # Log model in MLflow
        mlflow.sklearn.log_model(model, model_name)
        
        # Ensure the models directory exists
        os.makedirs('models', exist_ok=True)
        
        # Save model to a file using joblib
        joblib.dump(model, f'models/{model_name}.pkl')
        print(f"Model saved in models/{model_name}.pkl")

        print(f"Model: {model_name}")
        print(f"Training R2: {train_r2}")
        print(f"Validation MSE: {val_mse}")
        print(f"Validation R2: {val_r2}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Train and evaluate model")
    parser.add_argument('--train_path', type=str, required=True, help="Path to the training data")
    parser.add_argument('--model_type', type=str, required=True, choices=['random_forest', 'lightgbm', 'xgboost', 'catboost'], help="Type of model to train")
    parser.add_argument('--model_name', type=str, required=True, help="Name of the model to log in MLflow and save")
    parser.add_argument('--experiment_name', type=str, required=True, help="Name of the MLflow experiment")
    args = parser.parse_args()
    
    train_model(args.train_path, args.model_type, args.model_name, args.experiment_name)
