"""
Verification test script for Topic 7: Feature Scaling & Normalization
Tests all mathematical calculations, Scaler transformations, and Section 13 Lab code.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

print("--- 1. Min-Max Scaling (10, 20, 30) ---")
x = np.array([[10], [20], [30]])
mm = MinMaxScaler()
x_mm = mm.fit_transform(x)
print("Fitted min:", mm.data_min_, "max:", mm.data_max_)
print("Scaled:\n", x_mm.flatten())
assert np.allclose(x_mm.flatten(), [0.0, 0.5, 1.0])

# Unseen test value: 40
x_test = np.array([[40]])
x_test_mm = mm.transform(x_test)
print("Unseen 40 scaled:", x_test_mm.flatten())
assert np.allclose(x_test_mm.flatten(), [1.5])

# Constant feature
x_const = np.array([[20], [20], [20]])
mm_const = MinMaxScaler()
x_const_mm = mm_const.fit_transform(x_const)
print("Constant feature scaled:\n", x_const_mm.flatten())
assert np.allclose(x_const_mm.flatten(), [0.0, 0.0, 0.0])

print("\n--- 2. Standardization Z-Score (10, 20, 30) ---")
ss = StandardScaler()
x_ss = ss.fit_transform(x)
print("Fitted mean:", ss.mean_, "std:", ss.scale_)
print("Standardized:\n", x_ss.flatten())
expected_std = np.sqrt(200/3)
assert np.isclose(ss.scale_[0], expected_std)
assert np.allclose(x_ss.flatten(), [-10/expected_std, 0.0, 10/expected_std])
print("Mean of z:", x_ss.mean(), "Std of z:", x_ss.std())

print("\n--- 3. Robust Scaling with Outlier ---")
# Dataset (N=9): [20, 25, 30, 35, 40, 45, 50, 55, 500]
# Q1 (index 2) = 30, Median (index 4) = 40, Q3 (index 6) = 50 -> IQR = 20
x_out = np.array([[20], [25], [30], [35], [40], [45], [50], [55], [500]])
rs = RobustScaler()
x_rs = rs.fit_transform(x_out)
print("Center (median):", rs.center_, "Scale (IQR):", rs.scale_)
print("Robust scaled:\n", x_rs.flatten())
assert np.isclose(rs.center_[0], 40.0)
assert np.isclose(rs.scale_[0], 20.0)
assert np.allclose(x_rs.flatten(), [-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 23.0])

# Show how MinMaxScaler crushes the same data
mm_out = MinMaxScaler().fit_transform(x_out)
print("MinMax with outlier (crushed):\n", np.round(mm_out.flatten(), 4))

print("\n--- 4. Vector Normalization (Row-wise) ---")
v = np.array([[3.0, 4.0]])
norm_l2 = Normalizer(norm='l2')
v_l2 = norm_l2.fit_transform(v)
print("L2 normalized [3, 4]:", v_l2.flatten())
assert np.allclose(v_l2.flatten(), [0.6, 0.8])
assert np.isclose(np.linalg.norm(v_l2), 1.0)

norm_l1 = Normalizer(norm='l1')
v_l1 = norm_l1.fit_transform(v)
print("L1 normalized [3, 4]:", v_l1.flatten())
assert np.allclose(v_l1.flatten(), [3/7, 4/7])
assert np.isclose(np.sum(np.abs(v_l1)), 1.0)

print("\n--- 5. Section 13 Practical Lab End-to-End ---")
# 12 samples with mixed scales and 1 extreme income outlier
raw_data = {
    'Customer_ID': [f'CUST-{i:03d}' for i in range(1, 13)],
    'Age': [22, 25, 28, 32, 35, 40, 45, 50, 55, 60, 29, 38],
    'Annual_Income': [32000, 45000, 52000, 68000, 75000, 82000, 95000, 110000, 125000, 850000, 48000, 78000],
    'Experience_Years': [1, 3, 5, 8, 10, 15, 18, 22, 25, 30, 4, 12],
    'Purchases_Count': [3, 5, 8, 12, 15, 18, 22, 28, 35, 42, 7, 16],
    'High_Value': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(raw_data)
features = ['Age', 'Annual_Income', 'Experience_Years', 'Purchases_Count']
X = df[features]
y = df['High_Value']

print("Raw Dataset Summary Statistics:")
print(X.describe().T[['min', 'mean', '50%', 'max', 'std']])

# Comparison of scalers on full feature set
X_minmax = pd.DataFrame(MinMaxScaler().fit_transform(X), columns=features)
X_standard = pd.DataFrame(StandardScaler().fit_transform(X), columns=features)
X_robust = pd.DataFrame(RobustScaler().fit_transform(X), columns=features)

print("\nIncome Column Scaled Comparison (first 5 + outlier row 9):")
comp_df = pd.DataFrame({
    'Raw_Income': X['Annual_Income'],
    'MinMax': np.round(X_minmax['Annual_Income'], 3),
    'Standard': np.round(X_standard['Annual_Income'], 3),
    'Robust': np.round(X_robust['Annual_Income'], 3)
})
print(comp_df.iloc[[0, 1, 2, 3, 4, 9]])

# Train/Test Split (Leakage-safe)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
print(f"\nTrain shape: {X_train.shape}, Test shape: {X_test.shape}")

# Build Pipeline
pipe = Pipeline([
    ('scaler', RobustScaler()),
    ('classifier', KNeighborsClassifier(n_neighbors=3))
])

# Fit on training data ONLY
pipe.fit(X_train, y_train)
train_score = pipe.score(X_train, y_train)
test_score = pipe.score(X_test, y_test)
print(f"Pipeline fitted successfully! Train Acc: {train_score:.2f}, Test Acc: {test_score:.2f}")

# Verify no data leakage: scaler center and scale computed on X_train only
fitted_scaler = pipe.named_steps['scaler']
expected_train_median = X_train['Annual_Income'].median()
assert np.isclose(fitted_scaler.center_[1], expected_train_median), "Leakage detected! Scaler median doesn't match X_train!"
print(f"Verified zero leakage: Scaler income median {fitted_scaler.center_[1]} == Train median {expected_train_median}")

print("\nALL NUMERICAL TESTS PASSED SUCCESSFULLY!")
