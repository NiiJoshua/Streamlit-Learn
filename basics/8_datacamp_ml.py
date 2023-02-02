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