# imports
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import graphviz as gv


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

# Area Chart
st.subheader('Area chart')
ac = pd.DataFrame(np.random.randn(10,2), columns=['x','y'])
st.area_chart(ac)

# Scatter Plot
st.subheader('Scatter plot')
sp = pd.DataFrame(np.random.randn(500,3), columns=['x','y','z'])
c = alt.Chart(sp).mark_circle().encode(
    x='x', y='y', size='z', color='z', tooltip=['x','y','z'])
st.altair_chart(c, use_container_width=True)

# Flow Chart
st.subheader('Flow Chart')

st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')

# Maps
st.subheader('Maps')
map = pd.DataFrame(np.random.randn(500,2) / [50/50] + [37.76, -122.4], columns=['lat','lon'])
st.map(map)