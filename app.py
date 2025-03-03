import streamlit as st

st.title("BMI Calculator")

height = st.slider("Enter Your height (in cm): ", 100, 250, 175)
weight = st.slider("Enter you weight (in kg): ", 40, 200, 78)

bmi = weight/((height/100)**2)

st.write("Your BMI is: ", round(bmi, 2))

st.write("### BMI Categories ###")
st.write("- Underweight: BMI is less then 18.5")
st.write("- Normal: BMI is in between 18.5 and 24.9")
st.write("- Overweight: BMI is in between 25 and 29.9")
st.write("- Obesity: BMI is 30 or greater")

