# imports
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('Collection of graphs')
st.subheader('Bar graph')

# Bar Graph
rand = np.random.normal(1,2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)