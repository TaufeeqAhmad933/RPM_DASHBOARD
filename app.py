from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI
app = FastAPI()

# Load ML model
model = joblib.load("risk_model.pkl")

# Input schema
class Vitals(BaseModel):
    heart_rate: int
    bp_sys: int
    bp_dia: int
    spo2: int
    temp: float

@app.get("/")
def root():
    return {"message": "Vivnovation API is running 🚀"}

@app.post("/predict")
def predict(vitals: Vitals):
    # Prepare input
    X = np.array([[vitals.heart_rate, vitals.bp_sys, vitals.bp_dia, vitals.spo2, vitals.temp]])
    
    # Predict risk
    pred = model.predict(X)[0]
    risk_map = {0: "Low", 1: "Medium", 2: "High"}
    risk = risk_map[pred]

    return {"risk": risk}
