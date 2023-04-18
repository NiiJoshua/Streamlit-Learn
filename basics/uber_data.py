from types import LambdaType
import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Uber pickups in NYC')

dateColumn = 'date/time'
data_url = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

@st.cache

def load_data(nrows):
    data = pd.read_csv(data_url, nrows=nrows)
    lowercase = lambda x:str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[dateColumn] = pd.to_datetime(data[dateColumn])
    return data

data_Load_state = st.text('Loading data')
data = load_data(10000)

data_Load_state.text("Done ! (using st.cache)")
if st.button('Show raw data'):
    st.subheader('Raw data')
    with st.spinner('Loading data ...'):
        time.sleep(1)
    st.write(data)
st.subheader('Number of pickup by hour')
histValues = np.histogram(data[dateColumn].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(histValues)

hourToFilter = st.slider('hour', 0,23,10)
filteredData = data[data[dateColumn].dt.hour == hourToFilter]

st.subheader(f'Map of all pickups at {hourToFilter} hrs')
st.map(filteredData)


