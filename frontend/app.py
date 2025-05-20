import streamlit as st
import requests
import pandas as pd

BASE_URL = "http://api:8000"

st.title("📦 Logistics Dashboard")

# ---------- Table Data Display ----------
st.subheader("📊 All Data Tables")

def show_data(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.subheader(endpoint.capitalize())
        st.dataframe(df)
    else:
        st.error(f"Failed to load {endpoint}")

for endpoint in ["customers", "products", "suppliers", "inventory", "orders", "order_items"]:
    show_data(endpoint)

