import streamlit as st
import requests

st.title("Car price predictor")


make_year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2020
)

engine_capacity = st.number_input(
    "Engine capacity (CC)",
    min_value=500,
    max_value=5000,
    value=2000
)

km_driven = st.number_input(
    "Kilometers driven",
    min_value=0,
    value=30000
)

if st.button("Predict"):
    data = {
        "make_year": make_year,
        "engine_capacity": engine_capacity,
        "km_driven": km_driven
    }

    response = requests.post("http://api:8000/predict",json=data)
    result = response.json()

    st.write(result)
    
    st.success(f"Estimated price: {result['predicted_price']}")