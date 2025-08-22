import random
import time
import pandas as pd
from datetime import datetime

def generate_patient_data():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "bp_systolic": random.randint(90, 160),
        "bp_diastolic": random.randint(60, 100),
        "heart_rate": random.randint(50, 120),
        "glucose": random.randint(70, 200),
        "spo2": random.randint(85, 100)
    }

if __name__ == "__main__":
    data = []
    for _ in range(10):   # generate 10 sample readings
        data.append(generate_patient_data())
        time.sleep(1)  # simulate time gap

    df = pd.DataFrame(data)
    df.to_csv("patient_data.csv", index=False)
    print("Sample patient data generated → patient_data.csv")
