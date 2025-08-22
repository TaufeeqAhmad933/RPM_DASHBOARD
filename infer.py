import joblib
import numpy as np

# Load model
model = joblib.load("risk_model.pkl")

# Example patient input
sample = np.array([[140, 150, 95, 88, 101]])  
# [heart_rate, bp_sys, bp_dia, spo2, temp]

# Predict
pred = model.predict(sample)[0]
risk_map = {0: "Low", 1: "Medium", 2: "High"}

print("Predicted Risk:", risk_map[pred])
