import streamlit as st
import requests

st.title("Streamlit Interface")
response = requests.get("http://api:8000/")
st.write(response.json())
