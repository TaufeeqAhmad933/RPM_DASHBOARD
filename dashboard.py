import streamlit as st
import time
import random
import pandas as pd

# ---- Simulate vitals (from simulate_data.py) ----
def generate_vitals():
    return {
        "Heart Rate": random.randint(60, 100),
        "Systolic BP": random.randint(100, 140),
        "Diastolic BP": random.randint(70, 90),
        "SpO2": random.randint(85, 100),   # widened to test risks
        "Respiratory Rate": random.randint(12, 25)
    }

# ---- Risk Evaluation Logic ----
def determine_risk(vitals):
    score = 0
    if vitals["Heart Rate"] < 60 or vitals["Heart Rate"] > 100:
        score += 1
    if vitals["Systolic BP"] > 140 or vitals["Diastolic BP"] > 90:
        score += 1
    if vitals["SpO2"] < 90:
        score += 2
    if vitals["Respiratory Rate"] < 12 or vitals["Respiratory Rate"] > 20:
        score += 1

    if score == 0:
        return "🟢 Low Risk"
    elif score <= 2:
        return "🟠 Medium Risk"
    else:
        return "🔴 High Risk"

# ---- Streamlit UI ----
st.set_page_config(page_title="Patient Vitals Dashboard", layout="wide")
st.title("🩺 Live Patient Monitoring Dashboard")

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["Heart Rate", "Systolic BP", "Diastolic BP", "SpO2", "Respiratory Rate"])

# Create layout
col1, col2 = st.columns(2)

with col1:
    heart_rate_text = st.empty()
    bp_text = st.empty()
    spo2_text = st.empty()
    resp_text = st.empty()

with col2:
    st.subheader("📊 Vital Trends (Live)")
    chart_area = st.empty()

# Predict button
if st.button("⚠️ Predict Risk"):
    st.subheader("Risk Analysis")
    st.line_chart(st.session_state.history)

    if not st.session_state.history.empty:
        latest_vitals = st.session_state.history.iloc[-1].to_dict()
        risk_level = determine_risk(latest_vitals)
        st.write(f"**Risk Level:** {risk_level}")
    else:
        st.warning("⚠️ No data collected yet to predict risk!")

# Live loop (runs until you stop it)
while True:
    vitals = generate_vitals()

    # Update metrics
    heart_rate_text.metric("Heart Rate", f"{vitals['Heart Rate']} bpm")
    bp_text.metric("Blood Pressure", f"{vitals['Systolic BP']}/{vitals['Diastolic BP']} mmHg")
    spo2_text.metric("SpO2", f"{vitals['SpO2']} %")
    resp_text.metric("Respiratory Rate", f"{vitals['Respiratory Rate']} bpm")

    # Append to history
    st.session_state.history.loc[len(st.session_state.history)] = vitals

    # Update chart in real-time
    chart_area.line_chart(st.session_state.history)

    time.sleep(2)
