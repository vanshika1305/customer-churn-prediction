#gender 1 is female 0 male
#churn 1 is yes 0 no
#scalar is exported as scalar.pkl
#Model is exported as model.pkl
#Order of the X ['Age', 'Gender', 'Tenure', 'MonthlyCharges']

import streamlit as st
import joblib 
import numpy as np

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the predict button for getting a prediction.")

st.divider()

age = st.number_input("Enter age",min_value = 10,max_value=100,value=30)


gender = st.selectbox("Enter the Gender",["Male","Female"])

tenure = st.number_input("Enter Tenure",min_value=0,max_value=130,value=10)


monthlycharge = st.number_input("Enter Monthly Charge",min_value=30,max_value=150)

st.divider()

predictbutton = st.button("Predict!")

st.divider()

if predictbutton:

    gender_selected = 1 if gender == "Female" else 0

    X = [age,gender_selected,tenure,monthlycharge]

    X1 = np.array(X)

    X_array = scaler.transform([X1])

    prediction = model.predict(X_array)[0]

    predicted = "Yes" if prediction == 1 else "No"

    st.balloons()

    st.write(f"Predicted: {predicted}")

else:
    st.write("Please enter the values and use predict button")

