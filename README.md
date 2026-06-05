# ✈️ Flight Fare Prediction Using Machine Learning

## 📌 Project Overview

This project predicts airline ticket prices based on various flight-related factors such as airline, source city, destination city, journey date, duration, and number of stops.

The objective is to build a machine learning model that helps travelers and businesses estimate flight fares before booking.

---

## 🎯 Problem Statement

Flight ticket prices fluctuate frequently due to multiple factors. Predicting fares accurately can help customers make informed travel decisions and assist travel companies in pricing strategies.

This project leverages machine learning techniques to predict flight fares using historical flight data.

---

## 📂 Dataset Information

The dataset contains flight booking information with features such as:

| Feature         | Description                          |
| --------------- | ------------------------------------ |
| Airline         | Airline company                      |
| Date_of_Journey | Travel date                          |
| Source          | Departure city                       |
| Destination     | Arrival city                         |
| Route           | Flight route                         |
| Dep_Time        | Departure time                       |
| Arrival_Time    | Arrival time                         |
| Duration        | Flight duration                      |
| Total_Stops     | Number of stops                      |
| Additional_Info | Extra flight details                 |
| Price           | Flight ticket fare (Target Variable) |

### Target Variable

```text
Price
```

The model predicts the flight ticket fare in Indian Rupees (₹).

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Jupyter Notebook

---

## 🚀 Project Workflow

### 1. Data Collection

* Imported flight fare dataset
* Loaded data using Pandas

### 2. Data Cleaning

* Removed null values
* Checked duplicate records
* Corrected data formats

### 3. Feature Engineering

Extracted useful information from:

* Journey Date
* Departure Time
* Arrival Time
* Duration

Created features such as:

* Journey Day
* Journey Month
* Departure Hour
* Departure Minute
* Arrival Hour
* Arrival Minute

### 4. Encoding Categorical Features

Applied encoding techniques on:

* Airline
* Source
* Destination
* Total Stops

### 5. Feature Selection

Selected important variables affecting ticket prices.

### 6. Model Training

Several regression algorithms were trained and compared.

### 7. Model Evaluation

Models were evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

### 8. Model Saving

Saved the best-performing model using Joblib for future deployment.

---

## 🤖 Machine Learning Models Used

### Linear Regression

Baseline regression model.

### Decision Tree Regressor

Captures nonlinear relationships in the data.

### Random Forest Regressor

Ensemble model providing improved prediction accuracy.

### Extra Trees Regressor

Uses multiple randomized decision trees for better generalization.

---

## 📊 Model Performance

Models were compared based on:

| Metric   | Description              |
| -------- | ------------------------ |
| R² Score | Goodness of fit          |
| MAE      | Average prediction error |
| MSE      | Squared prediction error |
| RMSE     | Root Mean Squared Error  |

The model with the highest R² score and lowest prediction error was selected.

---

# 🎯 Sample Prediction

## Sample Input

| Feature            | Value  |
| ------------------ | ------ |
| Airline            | IndiGo |
| Source             | Delhi  |
| Destination        | Cochin |
| Total Stops        | 1      |
| Journey Day        | 24     |
| Journey Month      | 3      |
| Departure Hour     | 22     |
| Departure Minute   | 20     |
| Arrival Hour       | 1      |
| Arrival Minute     | 10     |
| Duration (Minutes) | 170    |

```python
sample_data = [[
    3,
    2,
    1,
    1,
    24,
    3,
    22,
    20,
    1,
    10,
    170
]]
```

## Prediction

```python
prediction = model.predict(sample_data)
print(prediction)
```

## Output

```text
₹5,487
```

### Interpretation

✅ Estimated Flight Fare = **₹5,487**

---

## ✈️ Another Example

### Input

| Feature            | Value     |
| ------------------ | --------- |
| Airline            | Air India |
| Source             | Kolkata   |
| Destination        | Bangalore |
| Total Stops        | 2         |
| Journey Day        | 15        |
| Journey Month      | 6         |
| Departure Hour     | 9         |
| Departure Minute   | 30        |
| Arrival Hour       | 18        |
| Arrival Minute     | 45        |
| Duration (Minutes) | 320       |

### Output

```text
₹9,235
```

### Interpretation

✅ Estimated Flight Fare = **₹9,235**

---

## 📁 Project Structure

```text
Flight-Fare-Prediction/
│
├── flight.ipynb
├── Data_Train.xlsx
├── Test_set.xlsx
├── flight_fare_model.pkl
├── README.md
├── requirements.txt
│
└── images/
```

---

## 💾 Saving the Model

```python
import joblib

joblib.dump(model, "flight_fare_model.pkl")
```

Load the model:

```python
model = joblib.load("flight_fare_model.pkl")
```

---

## 📈 Key Insights

* Airline significantly impacts ticket prices.
* Flights with multiple stops generally cost less.
* Duration is one of the strongest predictors of fare.
* Travel month and departure time affect pricing patterns.
* Random Forest and Extra Trees models often outperform simple regression models.

---

## 🔮 Future Enhancements

* Build a Streamlit web application.
* Deploy on Render or Hugging Face Spaces.
* Integrate live flight APIs.
* Add real-time fare prediction.
* Develop an interactive dashboard.
* Implement advanced hyperparameter tuning.

---





## 📜 Requirements

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
joblib
jupyter
```

---

## 👨‍💻 Author

**P. Purandhar**

* Aspiring Data Scientist
* Machine Learning Enthusiast
* Kaggle Competitor (Top 3400 Rank)
