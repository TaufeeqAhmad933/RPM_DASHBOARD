import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Generate simulated dataset
def generate_data(n=1000):
    data = {
        "heart_rate": np.random.randint(60, 180, n),
        "bp_sys": np.random.randint(90, 180, n),
        "bp_dia": np.random.randint(60, 120, n),
        "spo2": np.random.randint(85, 100, n),
        "temp": np.random.uniform(96, 105, n)
    }
    df = pd.DataFrame(data)

    # Risk labeling (rule-based for training)
    conditions = []
    for _, row in df.iterrows():
        if row["heart_rate"] > 130 or row["spo2"] < 90 or row["temp"] > 102:
            conditions.append("High")
        elif row["bp_sys"] > 140 or row["bp_dia"] > 95 or row["temp"] > 100:
            conditions.append("Medium")
        else:
            conditions.append("Low")

    df["risk"] = conditions
    return df

# Generate dataset
df = generate_data()

# Features & Labels
X = df[["heart_rate", "bp_sys", "bp_dia", "spo2", "temp"]]
y = df["risk"]

# Encode labels
y_encoded = y.replace({"Low":0, "Medium":1, "High":2})

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train Model
model = LogisticRegression(max_iter=1000, multi_class="multinomial")
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "risk_model.pkl")

print("✅ Model trained & saved as risk_model.pkl")
print("Accuracy:", model.score(X_test, y_test))
