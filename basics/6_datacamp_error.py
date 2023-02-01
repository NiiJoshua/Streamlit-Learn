import streamlit as st

# container
container = st.container()
container.write('This is written inside the container')
st.write('This is written outside the container')

st.success("Congratulations, you did it !")
st.error("Error")
st.warning("Warning")
st.info("It is easier to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))