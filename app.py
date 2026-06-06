import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Flight Fare Prediction",
    page_icon="✈️",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------
@st.cache_resource
def load_model():
    return pickle.load(open("flight_fare_model.pkl", "rb"))

@st.cache_data
def load_data():
    return pd.read_excel("Flight_Fare.xlsx")

model = load_model()
df = load_data()

# -------------------------
# Sidebar
# -------------------------
page = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "EDA Dashboard",
        "Prediction"
    ]
)

# -------------------------
# HOME
# -------------------------
if page == "Home":

    st.title("✈️ Flight Fare Prediction")

    st.write("""
    Predict airline ticket prices using Machine Learning.
    """)

    st.subheader("Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.dataframe(df.head())

# -------------------------
# EDA
# -------------------------
elif page == "EDA Dashboard":

    st.title("📊 Exploratory Data Analysis")

    tab1, tab2, tab3 = st.tabs([
        "Airlines",
        "Duration vs Price",
        "Stops vs Price"
    ])

    with tab1:

        fig, ax = plt.subplots(figsize=(8,5))

        sns.countplot(
            y=df["Airline"],
            order=df["Airline"].value_counts().index,
            ax=ax
        )

        st.pyplot(fig)

    with tab2:

        fig, ax = plt.subplots(figsize=(8,5))

        sns.scatterplot(
            data=df,
            x="Duration_Time",
            y="Price",
            ax=ax
        )

        st.pyplot(fig)

    with tab3:

        fig, ax = plt.subplots(figsize=(8,5))

        sns.boxplot(
            data=df,
            x="Total_Stops",
            y="Price",
            ax=ax
        )

        st.pyplot(fig)

# -------------------------
# PREDICTION
# -------------------------
elif page == "Prediction":

    st.title("💰 Predict Flight Fare")

    airline = st.number_input(
        "Airline (Encoded Value)",
        min_value=0
    )

    source = st.number_input(
        "Source (Encoded Value)",
        min_value=0
    )

    destination = st.number_input(
        "Destination (Encoded Value)",
        min_value=0
    )

    total_stops = st.selectbox(
        "Total Stops",
        [0,1,2,3,4]
    )

    journey_day = st.slider(
        "Journey Day",
        1,31,15
    )

    journey_month = st.slider(
        "Journey Month",
        1,12,6
    )

    journey_year = st.number_input(
        "Journey Year",
        value=2019
    )

    duration_time = st.number_input(
        "Duration (Minutes)",
        min_value=30
    )

    if st.button("Predict Fare"):

        input_df = pd.DataFrame({

            "Airline":[airline],
            "Source":[source],
            "Destination":[destination],
            "Total_Stops":[total_stops],
            "Journey_Day":[journey_day],
            "Journey_Month":[journey_month],
            "Journey_Year":[journey_year],
            "Duration_Time":[duration_time]

        })

        prediction = model.predict(input_df)[0]

        st.success(
            f"Estimated Flight Fare: ₹ {prediction:,.0f}"
        )
