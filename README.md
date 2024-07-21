# Poland House Price Prediction

This project is a comprehensive application for predicting house and rent prices in Poland using various machine learning models. The application is built with FastAPI for the backend API and Streamlit for the frontend UI. The project includes data preprocessing, data versioning, model training, and deployment on Google Cloud Platform (GCP).

## Table of Contents

- [Project Overview](#project-overview)
- [Video Demo](#video-demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Deployment](#deployment)
- [Connect with Me](#connect-with-me)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to provide a web application that can predict house and rent prices based on various features such as location, size, and amenities. The backend API is implemented using FastAPI, and the frontend is built with Streamlit. The application is containerized using Docker and deployed on Google Cloud Run. Data is versioned using DVC(Data Version Control).

**Try the Website**: [Poland House Price Prediction](https://streamlit-frontend-2vop66ad7a-uc.a.run.app/)

## Video Demo

Here is a video demo of the application in action:

[![Video Demo](https://img.youtube.com/vi/VTzhQpQiuG4/0.jpg)](https://youtu.be/VTzhQpQiuG4)

## Data Source

The dataset used in this project is sourced from [Kaggle: Apartment Prices in Poland](https://www.kaggle.com/datasets/krzysztofjamroz/apartment-prices-in-poland).

## Features

- **Exploratory Data Analysis**: Analyzing features of the dataset for both renting and apartment prices.
- **Data Processing**: Scripts for loading, preprocessing, and transforming raw data.
- **Data Versioning**: Using DVC (Data Version Control) for versioning datasets to Google Drive.
- **Model Training**: Training scripts for multiple models (Random Forest, CatBoost, XGBoost, LightGBM) and monitoring the results using MLFlow.
- **API**: FastAPI-based backend for serving predictions.
- **Frontend**: Streamlit-based web application for user interaction.
- **Deployment**: Dockerized setup for deployment on GCP Cloud Run.

## Tech Stack

- ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
- ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
- ![Joblib](https://img.shields.io/badge/Joblib-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![CatBoost](https://img.shields.io/badge/CatBoost-FF6F00?style=for-the-badge&logo=catboost&logoColor=white)
- ![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge&logo=xgboost&logoColor=white)
- ![LightGBM](https://img.shields.io/badge/LightGBM-00FF00?style=for-the-badge&logo=lightgbm&logoColor=white)
- ![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
- ![Requests](https://img.shields.io/badge/Requests-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![DVC](https://img.shields.io/badge/DVC-945DD6?style=for-the-badge&logo=dataversioncontrol&logoColor=white)

## Prerequisites

- Python 3.8 or higher
- Docker
- Google Cloud SDK (`gcloud` command line tool)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aliyusifov99/poland-house-price-prediction.git
   cd poland-house-price-prediction
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Google Cloud SDK**:
   Ensure you have the Google Cloud SDK installed and configured. Authenticate and set your project:
   ```bash
   gcloud auth login
   gcloud config set project house-price-prediction-pl
   ```

## Deployment

### FastAPI Backend

1. **Build Docker Image**:
   ```bash
   docker build -t gcr.io/house-price-prediction-pl/fastapi-backend:latest -f Dockerfile .
   ```

2. **Push Docker Image to GCR**:
   ```bash
   docker push gcr.io/house-price-prediction-pl/fastapi-backend:latest
   ```

3. **Deploy to Cloud Run**:
   ```bash
   gcloud run deploy fastapi-backend \
     --image gcr.io/house-price-prediction-pl/fastapi-backend:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --memory 512Mi
   ```

### Streamlit Frontend

1. **Build Docker Image**:
   ```bash
   docker build -t gcr.io/house-price-prediction-pl/streamlit-frontend:latest -f streamlit_Dockerfile .
   ```

2. **Push Docker Image to GCR**:
   ```bash
   docker push gcr.io/house-price-prediction-pl/streamlit-frontend:latest
   ```

3. **Deploy to Cloud Run**:
   ```bash
   gcloud run deploy streamlit-frontend \
     --image gcr.io/house-price-prediction-pl/streamlit-frontend:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --memory 1200Mi
   ```
## Contributing

Contributions are welcome!

## Connect with Me

Feel free to reach out or follow my work through the following platforms:

- [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aliyusifov99)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ali-yusifov/)
- [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/aliyusifovpy)
- [![Portfolio](https://img.shields.io/badge/Personal_Website-4CAF50?style=for-the-badge&logo=google-earth&logoColor=white)](https://www.aliyusifovai.com/)
- [![Support](https://img.shields.io/badge/Buy_Me_A_Coffee-F7DF1E?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/aliyusifov)






