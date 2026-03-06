# Customer Churn Prediction App

## Overview

This project predicts whether a  customer is likely to churn (leave the service) based on customer attributes such as age, gender, tenure, and monthly charges.

The prediction model is deployed using a **Streamlit web application**, allowing users to input customer details and instantly see whether the customer is likely to churn.

---

## Features

* Interactive web interface built with Streamlit
* Machine learning model for churn prediction
* Real-time prediction based on user input
* Data preprocessing using a saved scaler
* Simple and user-friendly UI

---

## Technologies Used

* Python
* NumPy
* Scikit-learn
* Joblib
* Streamlit

---

## Input Features Used

The model uses the following features:

| Feature        | Description                                             |
| -------------- | ------------------------------------------------------- |
| Age            | Age of the customer                                     |
| Gender         | Customer gender (Male/Female)                           |
| Tenure         | Number of months the customer has been with the company |
| MonthlyCharges | Monthly bill amount                                     |

Feature order used in the model:

Age → Gender → Tenure → MonthlyCharges

---

## Encoding

Gender Encoding:

* Male = 0
* Female = 1

Churn Prediction:

* 0 = No
* 1 = Yes

---

## Project Structure

```
customer-churn-prediction
│
├── app.py
├── notebook.ipynb
├── model.pkl
├── scaler.pkl
├── customer_churn_data.csv
└── README.md
```

---

## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/vanshika1305/customer-churn-prediction.git
```

### 2. Navigate to the project folder

```
cd customer-churn-prediction
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```
streamlit run app.py
```

---

## App Workflow

1. User enters customer information.
2. Input data is converted to numeric format.
3. Data is scaled using the saved scaler.
4. The trained machine learning model predicts churn.
5. The result is displayed in the Streamlit interface.

---

## Author

Vanshika Rajput
B.Tech Student 
