# imports
import streamlit as st
import pandas as pd
import numpy as np
import pickle #to load a saved model
import base64 #to open .gif files in streamlit

@st.cache(suppress_st_warning=True) # cache makes performant easier
def get_fvalue(val):
    feature_dict = {"No":1, "Yes":2}
    for key, value in feature_dict.items():
        if val == key:
            return value

def get_value(val, my_dict):
    for key,value in my_dict.items():
        if val==key:
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode == 'Home':
    st.title('Loan Prediction :')
    st.image('loan.jpeg')
    st.markdown('Dataset :')
    data = pd.read_csv('loan_dataset.csv')
    st.write(data.head())
    st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))

elif app_mode == 'Prediction':
    st.subheader('Sir/Mme, you need complete the following to process your load')
    st.sidebar.header("Information about the client :")
    gender_dict = {"Male":1, "Female":2}
    feature_dict = {"No":1, "Yes":2}
    edu = {"Graduate":1, "Not Graduate":2}
    prop = {'Rural':1, 'Urban':2, 'Semiurban':3}
    
    ApplicantIncome = st.sidebar.slider('Applicant Income',0,10000,0)
    CoapplicantIncome = st.sidebar.slider('Coapplicant Income',0,10000,0)
    LoanAmount = st.sidebar.slider('Loan Amount in K$',9.0,700.0,200.0)
    Loan_Amount_Term = st.sidebar.selectbox('Loan Tern Amount',(12.0,36.0,60.0,84.0,120.0,180.0,240.0,300.0,360.0))
    Credit_History = st.sidebar.radio('Credit History',(0.0,1.0))
    Gender = st.sidebar.radio('Gender',tuple(gender_dict.keys()))
    Married = st.sidebar.radio('Married',tuple(feature_dict.keys()))
    Self_Employed = st.sidebar.radio('Self Employed',tuple(feature_dict.keys()))
    Dependents = st.sidebar.radio('Dependents',options=['0','1','2','3+'])
    Education = st.sidebar.radio('Education',tuple(edu.keys()))
    Property_Area = st.sidebar.radio('Property Area',tuple(prop.keys()))


    class_0, class_1, class_2, class_3 = 0,0,0,0
    if Dependents == '0':
        class_0 = 1
    elif Dependents =='1': 
        class_1 = 1
    elif Dependents == '2':
        class_2 = 1
    else:
        class_3 = 1

    Rural, Urban, Semiurban = 0,0,0
    if Property_Area == 'Urban':
        Urban = 1
    elif Property_Area == 'Semiurban':
        Semiurban = 1
    else: 
        Rural = 1 

    
    catCols = {
        'Gender':Gender,
        'Maried':Married,
        'Dependents':Dependents,
        'Education': Education,
        'ApplicantIncome':ApplicantIncome,
        'CoapplicantIncome':CoapplicantIncome,
        'SelfEmployed': Self_Employed,
        'LoanAmount':LoanAmount,
        'Loan_Amount_Term':Loan_Amount_Term,
        'Credit_History':Credit_History,
        'Property_Area':[Rural,Urban,Semiurban],

    }
    feature_list = [
        ApplicantIncome,
        CoapplicantIncome,
        LoanAmount,
        Loan_Amount_Term,
        Credit_History,
        get_value(Gender, gender_dict),
        get_fvalue(Married),
        catCols['Dependents'][0],
        catCols['Dependents'][1],
        catCols['Dependents'][2],
        catCols['Dependents'][3],
        get_value(Education,edu),
        get_fvalue(Self_Employed),
        catCols['Property_Area'][0],
        catCols['Property_Area'][1],
        catCols['Property_Area'][2],
    ]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"): 