
## Project structure

### data/
Contains all data files used in the project. The raw data folder holds the original data files, while the processed data folder contains cleaned and preprocessed files. 

### notebooks/
Contains Jupyter notebooks for different stages of the project:
- **eda/**: For exploratory data analysis.
  - `eda_notebook.ipynb`: EDA notebook.
- **model_experiments/**: For experimenting with different models and evaluating them.
  - `model_experiment_notebook.ipynb`: Model experiment notebook.

### src/
Contains the source code of the project:
- **data/**: Scripts for loading, preprocessing, and utility functions.
  - `load_data.py`: Script to load data.
  - `preprocess_data.py`: Script to preprocess data.
  - `data_utils.py`: Utility functions for data handling.
- **models/**: Scripts for training, evaluating, and making predictions with models.
  - `train_model.py`: Script to train models.
  - `evaluate_model.py`: Script to evaluate models.
  - `predict.py`: Script for model inference.
- **api/**: FastAPI scripts to create and define API endpoints.
  - `main.py`: FastAPI main file.
  - `predict_api.py`: API endpoint definitions.

### ui/
Contains the Streamlit application files, including the main app file and any custom components.
- `app.py`: Streamlit app file.
- **components/**: Custom Streamlit components.

### configs/
Holds configuration files for the project, including settings for DVC, MLflow, and other tools.
- `config.yaml`: Configuration file for the project.
- `dvc.yaml`: DVC pipeline configuration.
- `mlflow.yaml`: MLflow tracking configuration.

### Other Directories and Files
- **.dvc/**: Directory for DVC cache and metadata.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: Provides an overview and instructions for the project.
- **requirements.txt**: Lists Python dependencies for the project.
- **setup.py**: Script for setting up the project as a Python package.
- **mlflow.db**: Database file for MLflow tracking.
- **dvc.lock**: Lock file for DVC to ensure reproducibility.

