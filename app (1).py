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
total_stops = st.number_input("Total Stops", min_value=0, max_value=4, value=1)

dep_hour = st.number_input("Departure Hour", min_value=0, max_value=23, value=10)
dep_min = st.number_input("Departure Minute", min_value=0, max_value=59, value=0)

arr_hour = st.number_input("Arrival Hour", min_value=0, max_value=23, value=12)
arr_min = st.number_input("Arrival Minute", min_value=0, max_value=59, value=0)

if st.button("Predict Fare"):

    features = pd.DataFrame({
    "Airline":[airline],
    "Source":[source],
    "Destination":[destination],
    "Total_Stops":[total_stops],
    "Journey_Day":[journey_day],
    "Journey_Month":[journey_month],
    "Journey_Year":[journey_year],
    "Duration_Time":[duration_time],
    "Dep_Hour":[dep_hour],
    "Dep_Min":[dep_min],
    "Arr_Hour":[arr_hour],
    "Arr_Min":[arr_min]
})

    prediction = model.predict(features)[0]

    st.success(f"Estimated Flight Fare: ₹ {prediction:,.2f}")
