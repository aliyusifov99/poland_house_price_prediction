# src/models/run_all_experiments.py
import subprocess

def run_experiment(train_path, test_path, model_type, model_name, experiment_name):
    # Run training
    train_command = [
        "python", "src/models/train_model.py",
        "--train_path", train_path,
        "--model_type", model_type,
        "--model_name", model_name,
        "--experiment_name", experiment_name
    ]
    subprocess.run(train_command)
    
    # Run evaluation
    evaluate_command = [
        "python", "src/models/evaluate_model.py",
        "--model_path", f"models_pickle/{model_name}.pkl",
        "--test_path", test_path,
        "--experiment_name", experiment_name,
        "--model_name", model_name
    ]
    subprocess.run(evaluate_command)

# Define the experiments
experiments = [
    {
        "train_path": "data/processed/housing/train_housing.csv",
        "test_path": "data/processed/housing/test_housing.csv",
        "models": ["random_forest","catboost", "xgboost", "lightgbm"],
        "experiment_name": "apartments_prediction"
    },
    {
        "train_path": "data/processed/rent/train_rent.csv",
        "test_path": "data/processed/rent/test_rent.csv",
        "models": ["random_forest","catboost", "xgboost", "lightgbm"],
        "experiment_name": "rent_prediction"
    }
]

# Run all experiments
for experiment in experiments:
    for model_type in experiment["models"]:
        model_name = f"{model_type}_{experiment['experiment_name'].split('_')[0]}"
        run_experiment(experiment["train_path"], experiment["test_path"], model_type, model_name, experiment["experiment_name"])
