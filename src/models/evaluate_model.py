# src/models/evaluate_model.py
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import mlflow

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def evaluate_model(model_path: str, test_path: str, experiment_name: str, model_name: str) -> None:
    # Load model
    model = joblib.load(model_path)
    
    # Load data
    test_df = load_data(test_path)
    
    # Separate features and target
    X_test = test_df.drop(columns=['price'])
    y_test = test_df['price']
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Evaluate model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Log metrics in MLflow
    mlflow.set_experiment(experiment_name)
    with mlflow.start_run(run_name=f"evaluation_{model_name}"):
        mlflow.log_metric('test_mse', mse)
        mlflow.log_metric('test_r2', r2)
        mlflow.log_artifact(model_path)
    
    print(f"Model: {model_name}")
    print(f"Test MSE: {mse}")
    print(f"Test R2: {r2}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Evaluate model")
    parser.add_argument('--model_path', type=str, required=True, help="Path to the trained model")
    parser.add_argument('--test_path', type=str, required=True, help="Path to the test data")
    parser.add_argument('--experiment_name', type=str, required=True, help="Name of the MLflow experiment")
    parser.add_argument('--model_name', type=str, required=True, help="Name of the model")
    args = parser.parse_args()
    
    evaluate_model(args.model_path, args.test_path, args.experiment_name, args.model_name)
