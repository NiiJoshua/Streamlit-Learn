# imports
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title('Collection of graphs')
st.subheader('Bar graph')

# Bar Graph
rand = np.random.normal(1,2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

# Libe Graph
st.subheader('Line graph')

data = np.random.rand(10,2)
df = pd.DataFrame(data,columns=['x','y'])
st.line_chart(df)


# Bar Chart
st.subheader('Bar graph')
df = pd.DataFrame(np.random.rand(10,2), columns=['x','y'])
st.bar_chart(df)