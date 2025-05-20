import streamlit as st
import requests
import pandas as pd

BASE_URL = "http://api:8000"

st.title("📦 Logistics Dashboard")

# ---------- Product Lookup Feature ----------
st.subheader("🔍 Look Up Product by ID")

product_id = st.text_input("Enter Product ID", placeholder="e.g., 1")

if st.button("Search Product"):
    if product_id.isdigit():
        response = requests.get(f"{BASE_URL}/products/{product_id}")
        if response.status_code == 200:
            product = response.json()
            st.success("Product found!")
            st.json(product)
        elif response.status_code == 404:
            st.error("Product not found.")
        else:
            st.error("An error occurred while fetching the product.")
    else:
        st.warning("Please enter a valid numeric Product ID.")

