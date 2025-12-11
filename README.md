# Flight-Fare-Prediction
1. Introduction

Air travel has become an essential mode of transportation for millions of people, and flight ticket prices fluctuate frequently due to various factors. These price changes make it difficult for travelers to plan trips and for businesses to forecast travel budgets.
This project aims to analyze the factors affecting flight fares and build a machine learning model that can accurately predict ticket prices based on flight-related features.

---

2. Problem Statement

Flight fares depend on multiple variables such as airline, flight duration, departure time, arrival time, number of stops, and travel dates.
The goal of this project is to:

* Understand how these factors influence the final ticket price.
* Build a predictive model that can estimate the fare for any given combination of inputs.

---

3. Objective

 1. Exploratory Data Analysis (EDA)

* Study distribution of numerical and categorical variables.
* Identify trends and patterns in ticket pricing.
* Detect outliers and missing values.
* Understand the impact of:

  * Airline
  * Source and Destination
  * Total stops
  * Duration
  * Travel date

 2. Feature Engineering

* Extract and transform time-related columns (e.g., day, month, hour).
* Convert categorical columns using encoding techniques.
* Handle outliers in price and duration.
* Create new features like:

  * Journey Month
  * Journey Day
  * Departure Hour
  * Arrival Hour
  * Duration in Minutes

 3. Model Development

Train machine learning models such as:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor

Evaluate them using:

* MAE (Mean Absolute Error)
* MSE (Mean Squared Error)
* RMSE (Root Mean Squared Error)
* R² Score

 4. Model Deployment
    
 4. Dataset Overview

Typical features in a flight fare dataset include:

 Categorical Variables

* Airline
* Source
* Destination
* Additional Info
* Route
* Total Stops

 Numerical Variables

* Price
* Duration
* Journey Day/Month
* Departure Time (Hours)
* Arrival Time (Hours)

 Target Variable

* Price (Flight Fare)

---

 5. Exploratory Data Analysis – Key Insights

 1. Airline-wise Price Differences

* Premium airlines show higher average fares.
* Budget airlines tend to have lower but more variable prices.

 2. Impact of Total Stops

* Non-stop flights are the costliest.
* More stops = lower price, but longer duration.

 3. Seasonal Trends

* Prices are higher in certain months (holidays or peak seasons).
* Weekend flights often cost more.

 4. Duration vs Price

* Longer duration usually means more stops or indirect routes, reducing price.
* Very long flights may still be expensive due to route demand.


 6. Feature Engineering Summary

To enhance model accuracy, we perform:

* Label Encoding on airlines, source, destination.
* One-Hot Encoding for total stops.
* Extracting features:

  * `Journey_Day`, `Journey_Month`
  * `Dep_Hour`, `Dep_Min`
  * `Arr_Hour`, `Arr_Min`
  * `Duration_Total_Minutes`
* Handling missing or inconsistent data in routes and durations.

 7. Model Building & Result

After splitting data into train/test sets:

 Best Performing Model (Usually)

  Random Forest Regressor / XGBoost Regressor

### Example Performance:

| Metric       | Value                         |
| ------------ | ----------------------------- |
| **R² Score** | 0.90+                         |
| **RMSE**     | Low (good prediction accuracy |
