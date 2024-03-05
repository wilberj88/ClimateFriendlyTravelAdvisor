import streamlit as st
import replicate
import os

# App title
st.set_page_config(page_title="🌎 Climate Friendly Travel Advisor")

def turn_on_bot():
    pass

with st.sidebar:
    st.title('🌎 Climate Friendly Travel Advisor')
    st.header('Prototyped 2')
    st.subheader ('Empowered by Langchain-OpenAI-ChatGPT-API')
    origin = st.text_input('Enter origin:')
    destiny = st.text_input('Enter destiny:')
    activate_advisor = st.button('🤖 Ask Advisor!', on_click=turn_on_bot)
