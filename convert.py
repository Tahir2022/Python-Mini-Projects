import requests
import streamlit as st

API_URL = "https://api.exchangerate.host/latest"


@st.cache_data
def get_rates(base: str = "USD"):
    params = {"base": base}
    resp = requests.get(API_URL, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data.get("rates", {})
