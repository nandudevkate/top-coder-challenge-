import json
import joblib
from sklearn.linear_model import LinearRegression

# Load public test cases
with open("public_cases.json", "r") as f:
    data = json.load(f)

X, y = [], []

for case in data:
    x = case["input"]
    X.append([
        x["trip_duration_days"],
        x["miles_traveled"],
        x["total_receipts_amount"]
    ])
    y.append(case["expected_output"])

# Train fast + small model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
print("✅ Linear regression model saved as model.pkl")
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

