import streamlit as st
import googlemaps
import gmaps
from datetime import datetime
from ipywidgets import embed
import streamlit.components.v1 as components

# set page layout
st.set_page_config(
    page_title="Climate Friendly Travel Advisor",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🌎 Climate Friendly Travel Advisor📍")

with st.sidebar:
    st.header("Plan your Trip")
    st.subheader("& discuss with me 🤖")
    origin = st.text_input(
        "Origin Point 👇")
    end = st.text_input(
        "End Point 👇")
    when = st.text_input(
        "When 👇")
    st.button("Calculate CO2 Alternatives", type="primary")
   
