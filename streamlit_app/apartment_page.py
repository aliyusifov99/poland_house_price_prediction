import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

def apartment_price_page():
    st.title("Apartment Price Prediction")
    
    city = st.selectbox("City", ['szczecin', 'gdynia', 'krakow', 'poznan', 'bialystok', 'gdansk', 'wroclaw',
                                 'radom', 'rzeszow', 'lodz', 'katowice', 'lublin', 'czestochowa', 'warszawa', 'bydgoszcz'])
    apt_type = st.selectbox("Type", ['blockOfFlats', 'apartmentBuilding', 'tenement'])
    squareMeters = st.number_input("Square Meters", min_value=10.0, value=10.0)
    rooms = st.number_input("Rooms", min_value=1, value=1, step=1)
    floor = st.number_input("Floor", min_value=1, value=1, step=1)
    floorCount = st.number_input("Floor Count", min_value=1, value=1, step=1)
    if floor > floorCount:
        st.error("Floor cannot be greater than Floor Count.")
    buildYear = st.number_input("Build Year", min_value=1850, max_value=2024, value=2010, step=1)
    centreDistance = st.selectbox("Distance to Centre", ['Very Close', 'Close', 'Medium', 'Far', 'Very Far'], help="Very Close: < 1km, Close: 1-3km, Medium: 3-5km, Far: 5-7km, Very Far: > 7km")
    poiCount = st.number_input("Points of Interest Count", min_value=0, value=0, step=1, help="Number of points of interest in 500m range from the apartment (schools, clinics, post offices, kindergartens, restaurants, colleges, pharmacies)")
    schoolDistance = st.selectbox("Distance to School", ['Very Close', 'Close', 'Medium', 'Far', 'Very Far'], help="Very Close: < 0.2km, Close: 0.2-0.5km, Medium: 0.5-1km, Far: 1-2km, Very Far: > 2km")
    clinicDistance = st.selectbox("Distance to Clinic", ['Very Close', 'Close', 'Medium', 'Far', 'Very Far'], help="Very Close: < 0.2km, Close: 0.2-0.5km, Medium: 0.5-1km, Far: 1-2km, Very Far: > 2km")
    postOfficeDistance = st.selectbox("Distance to Post Office", ['Very Close', 'Close', 'Medium', 'Far', 'Very Far'], help="Very Close: < 0.2km, Close: 0.2-0.5km, Medium: 0.5-1km, Far: 1-2km, Very Far: > 2km")
    kindergartenDistance = st.selectbox("Distance to Kindergarten", ['Very Close', 'Close', 'Medium', 'Far', 'Very Far'], help="Very Close: < 0.2km, Close: 0.2-0.5km, Medium: 0.5-1km, Far: 1-2km, Very Far: > 2km")
    restaurantDistance = st.selectbox("Distance to Restaurant", ['Very Close', 'Close', 'Medium', 'Far', 'Very Far'], help="Very Close: < 0.2km, Close: 0.2-0.5km, Medium: 0.5-1km, Far: 1-2km, Very Far: > 2km")
    collegeDistance = st.selectbox("Distance to College", ['Very Close', 'Close', 'Medium', 'Far', 'Very Far'], help="Very Close: < 0.2km, Close: 0.2-0.5km, Medium: 0.5-1km, Far: 1-2km, Very Far: > 2km")
    pharmacyDistance = st.selectbox("Distance to Pharmacy", ['Very Close', 'Close', 'Medium', 'Far', 'Very Far'], help="Very Close: < 0.2km, Close: 0.2-0.5km, Medium: 0.5-1km, Far: 1-2km, Very Far: > 2km")
    ownership = st.selectbox("Ownership", ['condominium', 'cooperative', 'udział'])
    buildingMaterial = st.selectbox("Building Material", ['concreteSlab', 'brick'])
    condition = st.selectbox("Condition", ['low', 'premium'])
    hasParkingSpace = st.selectbox("Has Parking Space", ['yes', 'no'])
    hasBalcony = st.selectbox("Has Balcony", ['yes', 'no'])
    hasElevator = st.selectbox("Has Elevator", ['yes', 'no'])
    hasSecurity = st.selectbox("Has Security", ['yes', 'no'])
    hasStorageRoom = st.selectbox("Has Storage Room", ['yes', 'no'])

    if st.button("Predict Apartment Price"):
        if floor > floorCount:
            st.error("Floor cannot be greater than Floor Count.")
        else:
            url = "https://fastapi-backend-2vop66ad7a-uc.a.run.app/api/predict"
            input_data = {
                "city": city,
                "type": apt_type,
                "squareMeters": squareMeters,
                "rooms": rooms,
                "floor": floor,
                "floorCount": floorCount,
                "buildYear": buildYear,
                "centreDistance": centreDistance,
                "poiCount": poiCount,
                "schoolDistance": schoolDistance,
                "clinicDistance": clinicDistance,
                "postOfficeDistance": postOfficeDistance,
                "kindergartenDistance": kindergartenDistance,
                "restaurantDistance": restaurantDistance,
                "collegeDistance": collegeDistance,
                "pharmacyDistance": pharmacyDistance,
                "ownership": ownership,
                "buildingMaterial": buildingMaterial,
                "condition": condition,
                "hasParkingSpace": hasParkingSpace,
                "hasBalcony": hasBalcony,
                "hasElevator": hasElevator,
                "hasSecurity": hasSecurity,
                "hasStorageRoom": hasStorageRoom
            }

            try:
                response = requests.post(url, json=input_data)
                response.raise_for_status()  # Raise an error for bad status codes
                result = response.json()
                st.success(f"Predicted Apartment Price: PLN {round(result['predicted_price'],0)}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error occurred: {e}")
