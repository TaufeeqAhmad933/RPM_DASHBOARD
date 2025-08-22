# simulate_data.py

import time
import random

def generate_vitals():
    """Simulate one patient's vitals."""
    return {
        "heart_rate": random.randint(60, 100),          # bpm
        "systolic_bp": random.randint(100, 140),        # mmHg
        "diastolic_bp": random.randint(70, 90),         # mmHg
        "spo2": random.randint(94, 100),                # %
        "resp_rate": random.randint(12, 20)             # breaths/min
    }

def live_stream(interval=2):
    """Continuously stream simulated vitals every `interval` seconds."""
    while True:
        vitals = generate_vitals()
        print(vitals)   # <-- for now, just print to console
        time.sleep(interval)

if __name__ == "__main__":
    live_stream(interval=2)  # change interval if you want faster/slower
