import streamlit as st
import numpy as np
import tensorflow as tf

# -------------------------------
# Load TinyML Model
# -------------------------------
@st.cache_resource
def load_model():
    # Replace with your tiny ML model path
    return tf.keras.models.load_model("tinyml_model.h5")

model = load_model()

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="🧠 NeuroNet TinyML", page_icon="🧑‍⚕️", layout="wide")

st.title("🧠 NeuroNet TinyML Stress Detection")
st.write("Running a lightweight ML model locally to detect stress patterns from simulated EEG data.")

# -------------------------------
# Patient Info Card
# -------------------------------
with st.container():
    st.subheader("👤 Patient Information")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Name", "John Doe")
    col2.metric("ID", "P1234")
    col3.metric("Age", "45")
    col4.metric("Condition", "Hypertension")
st.divider()

# -------------------------------
# Input Section
# -------------------------------
st.subheader("📊 Enter EEG Sensor Data")

col1, col2, col3 = st.columns(3)
alpha = col1.slider("Alpha Waves", 0.0, 1.0, 0.5)
beta = col2.slider("Beta Waves", 0.0, 1.0, 0.5)
theta = col3.slider("Theta Waves", 0.0, 1.0, 0.5)

# Prepare input
input_data = np.array([[alpha, beta, theta]])

# -------------------------------
# Run Prediction
# -------------------------------
if st.button("🔍 Analyze Stress Level"):
    prediction = model.predict(input_data)[0][0]  # Assuming single output neuron
    stress_level = "High Stress" if prediction > 0.5 else "Low Stress"

    # Display Result
    st.subheader("🧾 Result")
    st.metric("Stress Level", stress_level, f"{prediction:.2f}")

    # Feedback
    if stress_level == "High Stress":
        st.warning("⚠️ Patient shows signs of stress. Consider relaxation therapy.")
    else:
        st.success("✅ Patient is in a relaxed state.")

