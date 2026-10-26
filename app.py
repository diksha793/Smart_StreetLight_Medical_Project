import streamlit as st

st.title("Smart StreetLight & Medical Support Project")
st.write("Welcome to the live demo of the Smart StreetLight Medical Project!")

st.subheader("System Status")
if st.button("Check Sensor Status"):
    st.success("All systems operational. Street lights and medical emergency response units are active.")

st.info("You can view the source code and README on GitHub.")