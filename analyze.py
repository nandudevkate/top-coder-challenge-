import json
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load and normalize data
with open('public_cases.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
inputs = pd.json_normalize(df['input'])
df = pd.concat([inputs, df['expected_output']], axis=1)

# Prepare for modeling
X = df[['trip_duration_days', 'miles_traveled', 'total_receipts_amount']]
y = df['expected_output']

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Print the coefficients
print("Estimated formula:")
print(f"Base (intercept): {model.intercept_:.2f}")
for name, coef in zip(X.columns, model.coef_):
    print(f"{name}: {coef:.2f}")
