import streamlit as st
import requests

BASE_URL = "http://api:8000"

st.title("➕ Add a New Product")

name = st.text_input("Product Name")
price = st.number_input("Price", min_value=0.0)
stock = st.number_input("Stock", min_value=0)

if st.button("Add Product"):
    if name:
        data = {"name": name, "price": price, "stock": stock}
        res = requests.post(f"{BASE_URL}/products", json=data)
        if res.status_code == 200:
            st.success("Product added successfully!")
        else:
            st.error("Failed to add product")
    else:
        st.warning("Name cannot be empty")
