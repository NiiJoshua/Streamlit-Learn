import streamlit as st

st.title('Welcome to BMI calculator')
weight = st.number_input("Enter your weight in kg")
status = st.radio('Select your height in any format: ',('cm','meters','feet'))

if (status == 'cm'):
    height  = st.number_input('Centimeters')

    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter a value")

elif (status == 'meters'):
    height = st.number_input('Meters')
    try:
        bim = weight/ (height **2)
    except:
        st.text("Please enter a value for height")

else:
    height = st.number_input("Feet")

    try:
        bmi = weight / (((height/3.28))**2)

if (st.button('Calculate BMI')):
    st.text(f"Your BMI index is {bmi}")
    if (bmi < 16):
        st.error("You are vert overweight")
    elif (bmi >=16 and bmi < 18.5):
        st.warning("You are overweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("You are healthy, keep up the lifestyle")
    elif (bmi >= 25 and bmi < 30):
        st.warning("You are overweight")
    elif (bmi >=30):
        st.error("Extremely overweight")