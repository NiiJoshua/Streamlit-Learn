import streamlit as st
from datetime import date

st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):
    time.sleep(10)