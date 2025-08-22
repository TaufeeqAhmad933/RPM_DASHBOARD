# frontend/app.py

import streamlit as st
import requests

# App title
st.title("🏥 RPM Dashboard")

# Sidebar for inputs
st.sidebar.header("Enter Patient Vitals")
heart_rate = st.sidebar.number_input("Heart Rate", 60, 180, 90)
bp_sys = st.sidebar.number_input("Systolic BP", 90, 180, 120)
bp_dia = st.sidebar.number_input("Diastolic BP", 60, 120, 80)
spo2 = st.sidebar.number_input("SpO2 (%)", 85, 100, 95)
temp = st.sidebar.number_input("Temperature (°F)", 95.0, 105.0, 98.6)

# Predict button
if st.sidebar.button("Predict Risk"):
    payload = {
        "heart_rate": heart_rate,
        "bp_sys": bp_sys,
        "bp_dia": bp_dia,
        "spo2": spo2,
        "temp": temp
    }

    try:
        # Send data to FastAPI backend
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"✅ Predicted Risk: **{result['risk']}**")
        else:
            st.error(f"⚠️ Error {response.status_code}: Could not get prediction")

    except requests.exceptions.ConnectionError:
        st.error("🚫 Could not connect to backend. Is FastAPI running?")

# ----------------------
# About this Project Section
# ----------------------
st.markdown("---")  # horizontal line
st.subheader("📖 About this Project")

with st.expander("Click to read more"):
    st.markdown("""
    This **Remote Patient Monitoring (RPM) Dashboard** is a demo project that integrates:

    - **Frontend:** Streamlit app (this dashboard) where users can enter patient vitals  
    - **Backend:** FastAPI service that receives data and applies risk-prediction rules  
    - **Risk Prediction:** A simple rules-based classifier (simulated model) predicts **Low**, **Medium**, or **High** risk based on thresholds of vitals like Heart Rate, Blood Pressure, SpO₂, and Temperature.  
    - **Live Monitoring (other dashboard):** Simulates real-time vitals with trends and prediction button for continuous monitoring.  

    ### Process:
    1. User enters vitals in the sidebar.  
    2. The app sends these values to the FastAPI backend (`/predict` endpoint).  
    3. Backend processes the data using rule-based thresholds.  
    4. The predicted **risk level** is returned and displayed here.  

    ⚠️ **Note:** This is for demonstration purposes only and is *not* a medical diagnostic tool.  
    """)
