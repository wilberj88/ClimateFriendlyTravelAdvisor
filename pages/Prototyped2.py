import streamlit as st
import replicate
import os
import googlemaps
from datetime import datetime

# App title
st.set_page_config(page_title="🌎 Climate Friendly Travel Advisor")




modes = ["Car", "Train", "Flying"]

factor_emissions = {
    "Train": 1,
    "Car": 10,
    "Flying": 20,
}
factor_time = {
    "Train": 5,
    "Car": 7,
    "Flying": 2,
}
factor_speed = {
    "Train": 10,
    "Car": 7,
    "Flying": 20,
}
factor_confort = {
    "Train": 10,
    "Car": 20,
    "Flying": 30,
}


def emissions():
    pass

def turn_on_bot():
    pass

with st.sidebar:
    st.title('🌎 Climate Friendly Travel Advisor')
    st.header('Prototyped 2')
    st.subheader ('Empowered by Langchain-OpenAI-ChatGPT-API')
    origin = st.text_input('Enter origin:')
    destiny = st.text_input('Enter destiny:')
    prefer_mode = st.selectbox("Prefer mode transport:", modes, index=None)
    activate_advisor = st.button('🤖 Ask Advisor!', on_click=turn_on_bot)
