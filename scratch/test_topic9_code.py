"""
Test and validation script for Topic 9: Linear Regression.
Validates all manual formulas, OLS closed-form equations, gradient descent,
Scikit-Learn LinearRegression models, metrics (MAE, MSE, RMSE, R2),
and assertions for the practical lab.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("=== 1. Manual Equation Calculations (y = mx + b) ===")
# Example: y_hat = 2x + 5
m, b = 2.0, 5.0
x_vals = [1.0, 3.0, 5.0]
y_preds = [m * x + b for x in x_vals]
print(f"For line y_hat = 2x + 5:")
for x, y_p in zip(x_vals, y_preds):
    print(f"  x = {x} -> y_hat = {y_p}")
assert y_preds == [7.0, 11.0, 15.0]

print("\n=== 2. Closed-Form OLS Analytical Calculation (5 Samples) ===")
# Small dataset for Section 8
# x: Study hours, y: Test Score (or scaled price)
x_demo = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y_demo = np.array([2.0, 3.0, 5.0, 7.0, 8.0])
n_demo = len(x_demo)

x_bar = np.mean(x_demo)
y_bar = np.mean(y_demo)
print(f"x_bar = {x_bar}, y_bar = {y_bar}")
assert x_bar == 3.0 and y_bar == 5.0

# Covariance numerator and variance denominator
num = np.sum((x_demo - x_bar) * (y_demo - y_bar))
den = np.sum((x_demo - x_bar) ** 2)
beta_1 = num / den
beta_0 = y_bar - beta_1 * x_bar

print(f"Numerator (sum (x - x_bar)(y - y_bar)) = {num}")
print(f"Denominator (sum (x - x_bar)^2) = {den}")
print(f"Calculated slope beta_1 = {beta_1:.4f}")
print(f"Calculated intercept beta_0 = {beta_0:.4f}")

# Verification with Scikit-Learn
lr_demo = LinearRegression()
lr_demo.fit(x_demo.reshape(-1, 1), y_demo)
print(f"Scikit-Learn slope: {lr_demo.coef_[0]:.4f}, intercept: {lr_demo.intercept_:.4f}")
assert np.isclose(beta_1, lr_demo.coef_[0])
assert np.isclose(beta_0, lr_demo.intercept_)
# beta_1 = 1.6, beta_0 = 0.2
assert np.isclose(beta_1, 1.6)
assert np.isclose(beta_0, 0.2)

print("\n=== 3. Residuals and Loss Metrics Calculation (4 Samples for Section 6 & 7) ===")
# 4 samples: x = [1, 2, 3, 4], y = [3, 5, 8, 9]
# Suppose fitted line is y_hat = 2.1x + 0.8
x_res = np.array([1.0, 2.0, 3.0, 4.0])
y_actual = np.array([3.0, 5.0, 8.0, 9.0])
y_fitted = 2.1 * x_res + 0.8
residuals = y_actual - y_fitted
squared_res = residuals ** 2
abs_res = np.abs(residuals)

sse = np.sum(squared_res)
mse = np.mean(squared_res)
rmse = np.sqrt(mse)
mae = np.mean(abs_res)

print("Observation Table:")
for i in range(4):
    print(f"  Sample {i+1}: x={x_res[i]}, y={y_actual[i]}, y_hat={y_fitted[i]:.2f}, e={residuals[i]:+.2f}, e^2={squared_res[i]:.4f}, |e|={abs_res[i]:.2f}")
print(f"SSE  = {sse:.4f}")
print(f"MSE  = {mse:.4f}")
print(f"RMSE = {rmse:.4f}")
print(f"MAE  = {mae:.4f}")

assert np.isclose(mse, np.mean((y_actual - y_fitted)**2))
assert np.isclose(rmse, np.sqrt(mse))
assert np.isclose(mae, np.mean(np.abs(y_actual - y_fitted)))

print("\n=== 4. Gradient Descent Verification ===")
# Implement simple gradient descent on demo data to verify convergence
np.random.seed(42)
w = 0.0
b = 0.0
lr_rate = 0.05
epochs = 100
losses = []

for epoch in range(epochs):
    y_p = w * x_demo + b
    loss = np.mean((y_demo - y_p) ** 2)
    losses.append(loss)
    # Gradients
    dw = -2.0 / n_demo * np.sum(x_demo * (y_demo - y_p))
    db = -2.0 / n_demo * np.sum(y_demo - y_p)
    w -= lr_rate * dw
    b -= lr_rate * db

print(f"Gradient Descent after {epochs} epochs: w={w:.4f}, b={b:.4f}, final loss={losses[-1]:.4f}")
assert np.isclose(w, beta_1, atol=0.05), "Gradient descent slope did not converge near OLS slope!"
assert np.isclose(b, beta_0, atol=0.10), "Gradient descent intercept did not converge near OLS intercept!"
assert losses[0] > losses[-1], "Loss did not decrease during gradient descent!"

print("\n=== 5. Complete Practical Lab Data & Pipeline Verification ===")
# Generate synthetic house price dataset
# Features:
# Area (sq ft): 800 to 3500
# Bedrooms: 1 to 5
# Age (years): 1 to 40
# Distance to City Center (miles): 1 to 25
# Target: Price ($k): True relationship: 50 + 0.15*Area + 25*Bedrooms - 1.5*Age - 3.0*Distance + noise
np.random.seed(42)
n_houses = 100
area = np.random.uniform(800, 3200, n_houses)
bedrooms = np.random.choice([1, 2, 3, 4, 5], size=n_houses, p=[0.1, 0.25, 0.35, 0.2, 0.1])
age = np.random.uniform(1, 35, n_houses)
distance = np.random.uniform(2, 20, n_houses)
noise = np.random.normal(0, 20, n_houses)

price = 50.0 + 0.14 * area + 22.0 * bedrooms - 1.2 * age - 2.8 * distance + noise

df = pd.DataFrame({
    'House_ID': [f'HSE-{i:04d}' for i in range(1, n_houses + 1)],
    'Area_SqFt': np.round(area, 0),
    'Bedrooms': bedrooms,
    'Age_Years': np.round(age, 1),
    'Distance_Miles': np.round(distance, 1),
    'Price_kUSD': np.round(price, 1)
})

print(f"Dataset generated. Shape: {df.shape}")
print(df.head(3))

# Train / Test split (80% train, 20% test)
train_df, test_df = train_test_split(df, test_size=0.20, random_state=42)
assert len(train_df) == 80
assert len(test_df) == 20
assert len(set(train_df['House_ID']).intersection(set(test_df['House_ID']))) == 0

# A. Simple Linear Regression (Area -> Price)
X_train_simple = train_df[['Area_SqFt']]
y_train = train_df['Price_kUSD']
X_test_simple = test_df[['Area_SqFt']]
y_test = test_df['Price_kUSD']

slr = LinearRegression()
slr.fit(X_train_simple, y_train)

y_pred_train_simple = slr.predict(X_train_simple)
y_pred_test_simple = slr.predict(X_test_simple)

slr_train_r2 = r2_score(y_train, y_pred_train_simple)
slr_test_r2 = r2_score(y_test, y_pred_test_simple)
slr_test_mae = mean_absolute_error(y_test, y_pred_test_simple)
slr_test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test_simple))

print("\n--- Simple Linear Regression Results (Area only) ---")
print(f"Fitted Slope (Area): {slr.coef_[0]:.4f} kUSD / sq ft")
print(f"Fitted Intercept:    {slr.intercept_:.2f} kUSD")
print(f"Train R2: {slr_train_r2:.4f}")
print(f"Test R2:  {slr_test_r2:.4f}")
print(f"Test MAE: {slr_test_mae:.2f} kUSD")
print(f"Test RMSE: {slr_test_rmse:.2f} kUSD")

# B. Multiple Linear Regression (All 4 features)
feature_cols = ['Area_SqFt', 'Bedrooms', 'Age_Years', 'Distance_Miles']
X_train_multi = train_df[feature_cols]
X_test_multi = test_df[feature_cols]

mlr = LinearRegression()
mlr.fit(X_train_multi, y_train)

y_pred_train_multi = mlr.predict(X_train_multi)
y_pred_test_multi = mlr.predict(X_test_multi)

mlr_train_r2 = r2_score(y_train, y_pred_train_multi)
mlr_test_r2 = r2_score(y_test, y_pred_test_multi)
mlr_test_mae = mean_absolute_error(y_test, y_pred_test_multi)
mlr_test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test_multi))

print("\n--- Multiple Linear Regression Results (4 Features) ---")
print(f"Fitted Intercept: {mlr.intercept_:.2f}")
for col, coef in zip(feature_cols, mlr.coef_):
    print(f"  {col:15s}: {coef:+.4f}")
print(f"Train R2: {mlr_train_r2:.4f}")
print(f"Test R2:  {mlr_test_r2:.4f}")
print(f"Test MAE: {mlr_test_mae:.2f} kUSD")
print(f"Test RMSE: {mlr_test_rmse:.2f} kUSD")

assert mlr_test_r2 > slr_test_r2, "Multiple regression test R2 should be higher than simple regression!"
assert mlr_test_rmse < slr_test_rmse, "Multiple regression test RMSE should be lower than simple regression!"

print("\n=== 6. Outlier Influence Demonstration ===")
# Add single extreme leverage point
x_clean = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
y_clean = np.array([2.1, 3.9, 6.2, 8.1, 10.0, 11.9])
lr_clean = LinearRegression().fit(x_clean.reshape(-1, 1), y_clean)

# Add outlier: x=7 with y=1.0 (huge negative outlier with high leverage)
x_out = np.append(x_clean, [7.0])
y_out = np.append(y_clean, [1.0])
lr_out = LinearRegression().fit(x_out.reshape(-1, 1), y_out)

print(f"Clean slope:   {lr_clean.coef_[0]:.4f}, Clean intercept:   {lr_clean.intercept_:.4f}")
print(f"Outlier slope: {lr_out.coef_[0]:.4f}, Outlier intercept: {lr_out.intercept_:.4f}")
assert lr_out.coef_[0] < lr_clean.coef_[0], "Outlier should pivot the slope downwards!"

print("\nALL NUMERICAL VALIDATION AND CODE TESTS PASSED SUCCESSFULLY!")
