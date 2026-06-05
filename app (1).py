import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("flight_fare_model.pkl", "rb"))

st.set_page_config(page_title="Flight Fare Prediction")

st.title("✈ Flight Fare Prediction")

# Inputs
airline = st.number_input("Airline Code", min_value=0)
source = st.number_input("Source Code", min_value=0)
destination = st.number_input("Destination Code", min_value=0)

journey_day = st.slider("Journey Day", 1, 31, 15)
journey_month = st.slider("Journey Month", 1, 12, 6)
journey_year = st.number_input("Journey Year", value=2026)

duration_time = st.number_input("Duration (Minutes)", min_value=30)

if st.button("Predict Fare"):

    features = pd.DataFrame({
        "Airline":[airline],
        "Source":[source],
        "Destination":[destination],
        "Journey_Day":[journey_day],
        "Journey_Month":[journey_month],
        "Journey_Year":[journey_year],
        "Duration_Time":[duration_time]
    })

    prediction = model.predict(features)[0]

    st.success(f"Estimated Flight Fare: ₹ {prediction:,.2f}")