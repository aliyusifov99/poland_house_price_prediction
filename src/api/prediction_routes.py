# src/api/prediction_routes.py
from fastapi import APIRouter, HTTPException
import joblib
import pandas as pd
import sys
import os
from src.api.apartment_features import ApartmentFeatures
from src.api.preprocess import preprocess_input

# Ensure the custom_label_encoder module is available in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))

# Adjust the import path for custom label encoder
from custom_label_encoder import CustomLabelEncoder

router = APIRouter()

# Determine the correct paths for the models
model_dir = "/app/models_pickle"
apartment_model_path = os.path.join(model_dir, 'random_forest_apartments.pkl')
rent_model_path = os.path.join(model_dir, 'random_forest_rent.pkl')

# Load the trained model and processors for apartments
apartment_model = joblib.load(apartment_model_path)
apartment_encoders = joblib.load('/app/processors_pickle/housing_encoders.pkl')
apartment_scaler = joblib.load('/app/processors_pickle/housing_scaler.pkl')

# Load the trained model and processors for rent
rent_model = joblib.load(rent_model_path)
rent_encoders = joblib.load('/app/processors_pickle/rent_encoders.pkl')
rent_scaler = joblib.load('/app/processors_pickle/rent_scaler.pkl')


@router.post("/predict")
def predict(features: ApartmentFeatures):
    try:
        # Convert input features to DataFrame
        input_data = pd.DataFrame([features.dict()])
        
        # Preprocess input data
        input_data = preprocess_input(input_data, apartment_encoders, apartment_scaler)
        
        # Predict using the loaded model
        prediction = apartment_model.predict(input_data)
        
        # Convert the prediction to a standard Python float
        predicted_price = float(prediction[0])
        
        # Return the prediction
        return {"predicted_price": predicted_price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict_rent")
def predict_rent(features: ApartmentFeatures):
    try:
        # Convert input features to DataFrame
        input_data = pd.DataFrame([features.dict()])
        
        # Preprocess input data
        input_data = preprocess_input(input_data, rent_encoders, rent_scaler)
        
        # Predict using the loaded model
        prediction = rent_model.predict(input_data)
        
        # Convert the prediction to a standard Python float
        predicted_rent = float(prediction[0])
        
        # Return the prediction
        return {"predicted_rent": predicted_rent}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
