import streamlit as st
import pandas as pd
import pickle

# Load model

model = pickle.load(open("flight_fare_model.pkl", "rb"))

st.set_page_config(
page_title="Flight Fare Prediction",
page_icon="✈️",
layout="centered"
)

st.title("✈️ Flight Fare Prediction")
st.markdown("Predict airline ticket prices using Machine Learning")

st.subheader("Flight Details")

# Encoded values from training

airline = st.number_input("Airline Code", min_value=0, value=0)
source = st.number_input("Source Code", min_value=0, value=0)
destination = st.number_input("Destination Code", min_value=0, value=0)

col1, col2 = st.columns(2)

with col1:
    journey_day = st.selectbox("Journey Day", list(range(1, 32)))
    journey_month = st.selectbox("Journey Month", list(range(1, 13)))

with col2:
    journey_year = st.number_input("Journey Year",min_value=2024,max_value=2035,value=2026)

total_stops = st.selectbox("Total Stops",[0, 1, 2, 3, 4])
duration_time = st.number_input("Duration (Minutes)",min_value=30,value=30)

st.subheader("Departure Time")
col3, col4 = st.columns(2)
with col3:
    dep_hour = st.number_input("Departure Hour",min_value=0,max_value=23,value=10)

with col4:
    dep_min = st.number_input("Departure Minute",min_value=0,max_value=59,value=0)

st.subheader("Arrival Time")

col5, col6 = st.columns(2)

with col5:
    arr_hour = st.number_input("Arrival Hour",min_value=0,max_value=23,value=12)

with col6:
    arr_min = st.number_input("Arrival Minute",min_value=0,max_value=59,value=0)

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

    st.success(
        f"Estimated Flight Fare: ₹ {prediction:,.2f}"
    )

prediction = model.predict(features)[0]

st.success(
    f"Estimated Flight Fare: ₹ {prediction:,.2f}"
)
