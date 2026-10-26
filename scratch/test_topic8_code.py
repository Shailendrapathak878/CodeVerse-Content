"""
Test script for Topic 8: Train, Validation & Test Sets.
Verifies all sample-size calculations, stratified splits, group splitting,
time-series splitting, zero-overlap assertions, and pipeline model selection.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GroupShuffleSplit, TimeSeriesSplit
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

print("=== 1. Sample Size Calculations (N = 1000, 70/15/15) ===")
N = 1000
r_train, r_val, r_test = 0.70, 0.15, 0.15
assert np.isclose(r_train + r_val + r_test, 1.0)
N_train = int(N * r_train)
N_val = int(N * r_val)
N_test = int(N * r_test)
print(f"Total: {N} -> Train: {N_train} (70%), Val: {N_val} (15%), Test: {N_test} (15%)")
assert N_train + N_val + N_test == N

print("\n=== 2. Stratified 70/15/15 Splitting on Imbalanced Dataset ===")
# Generate synthetic dataset of 200 samples with 80% Class 0 (160) and 20% Class 1 (40)
np.random.seed(42)
n_samples = 200
ids = np.array([f"REC-{i:04d}" for i in range(1, n_samples + 1)])
X = np.random.randn(n_samples, 4)
# Class 0: 160 samples, Class 1: 40 samples (80% / 20% imbalance)
y = np.array([0] * 160 + [1] * 40)
# Shuffle randomly to simulate real unsorted raw data
perm = np.random.permutation(n_samples)
ids, X, y = ids[perm], X[perm], y[perm]

# Step 1: 70% Train, 30% Temp (Val + Test)
X_train, X_temp, y_train, y_temp, ids_train, ids_temp = train_test_split(
    X, y, ids, test_size=0.30, random_state=42, stratify=y
)

# Step 2: Split 30% Temp equally (50/50) into 15% Val and 15% Test
X_val, X_test, y_val, y_test, ids_val, ids_test = train_test_split(
    X_temp, y_temp, ids_temp, test_size=0.50, random_state=42, stratify=y_temp
)

print(f"Train samples: {len(X_train)} ({len(X_train)/n_samples:.1%})")
print(f"Val samples:   {len(X_val)} ({len(X_val)/n_samples:.1%})")
print(f"Test samples:  {len(X_test)} ({len(X_test)/n_samples:.1%})")
assert len(X_train) == 140  # 70% of 200
assert len(X_val) == 30     # 15% of 200
assert len(X_test) == 30    # 15% of 200

# Verify zero ID overlap
overlap_train_val = set(ids_train).intersection(set(ids_val))
overlap_train_test = set(ids_train).intersection(set(ids_test))
overlap_val_test = set(ids_val).intersection(set(ids_test))
assert len(overlap_train_val) == 0, f"Leakage: Train/Val overlap {overlap_train_val}"
assert len(overlap_train_test) == 0, f"Leakage: Train/Test overlap {overlap_train_test}"
assert len(overlap_val_test) == 0, f"Leakage: Val/Test overlap {overlap_val_test}"
print("Zero ID Overlap Verified across Train, Val, and Test sets!")

# Verify Stratified Class Proportions (approx 80% Class 0 and 20% Class 1)
def check_props(subset_y, name):
    c0 = np.sum(subset_y == 0)
    c1 = np.sum(subset_y == 1)
    p1 = c1 / len(subset_y)
    print(f"  {name}: Total={len(subset_y)}, Class 0={c0} ({c0/len(subset_y):.1%}), Class 1={c1} ({p1:.1%})")
    assert np.isclose(p1, 0.20, atol=0.03), f"Stratification failed for {name}!"

print("Class Distribution Check:")
check_props(y, "Original")
check_props(y_train, "Train Set")
check_props(y_val, "Val Set  ")
check_props(y_test, "Test Set ")

print("\n=== 3. Model Selection on Validation Set & Final Unbiased Test ===")
# Candidate 1: KNN with k=3
pipe1 = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_neighbors=3))])
pipe1.fit(X_train, y_train)
val_acc1 = pipe1.score(X_val, y_val)

# Candidate 2: KNN with k=7
pipe2 = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_neighbors=7))])
pipe2.fit(X_train, y_train)
val_acc2 = pipe2.score(X_val, y_val)

print(f"Candidate 1 (k=3) Validation Accuracy: {val_acc1:.2%}")
print(f"Candidate 2 (k=7) Validation Accuracy: {val_acc2:.2%}")

# Pick winner based strictly on VALIDATION performance (Never touch Test!)
best_pipe = pipe1 if val_acc1 >= val_acc2 else pipe2
best_name = "Candidate 1 (k=3)" if val_acc1 >= val_acc2 else "Candidate 2 (k=7)"
print(f"Selected Model based on Validation: {best_name}")

# Final Unbiased Evaluation on Held-out Test Set (ONLY ONCE)
final_test_acc = best_pipe.score(X_test, y_test)
print(f"Final Unbiased Test Accuracy: {final_test_acc:.2%}")

# Verify no test data leaked into training scaler
scaler_fitted = best_pipe.named_steps['scaler']
assert np.allclose(scaler_fitted.mean_, X_train.mean(axis=0)), "Scaler mean does not match X_train!"
print("Zero Leakage Assertion: Scaler fitted strictly on X_train!")

print("\n=== 4. Group-Based Splitting Demonstration (Patient / Customer Leakage) ===")
# 10 records from 4 patients: Patient A has 3 scans, B has 2, C has 3, D has 2
patient_groups = np.array(['PAT-A', 'PAT-A', 'PAT-A', 'PAT-B', 'PAT-B', 'PAT-C', 'PAT-C', 'PAT-C', 'PAT-D', 'PAT-D'])
gss = GroupShuffleSplit(n_splits=1, train_size=0.7, random_state=42)
train_idx, test_idx = next(gss.split(X[:10], y[:10], patient_groups))

train_patients = set(patient_groups[train_idx])
test_patients = set(patient_groups[test_idx])
print(f"Train Patients: {train_patients}")
print(f"Test Patients:  {test_patients}")
assert len(train_patients.intersection(test_patients)) == 0
print("Group Independence Verified: No patient appears in both Train and Test!")

print("\n=== 5. Time-Series Chronological Splitting Demonstration ===")
# 6 chronological dates
dates = pd.date_range("2026-01-01", periods=6, freq="D")
tss = TimeSeriesSplit(n_splits=3)
for fold, (t_idx, v_idx) in enumerate(tss.split(dates), 1):
    print(f"Fold {fold}: Train dates {dates[t_idx[0]].strftime('%m-%d')} to {dates[t_idx[-1]].strftime('%m-%d')} | Val dates {dates[v_idx[0]].strftime('%m-%d')} to {dates[v_idx[-1]].strftime('%m-%d')}")
    assert max(t_idx) < min(v_idx), "Lookahead leakage in TimeSeriesSplit!"
print("Chronological Integrity Verified: No future dates leak into past training!")

print("\nALL TOPIC 8 VERIFICATION TESTS PASSED SUCCESSFULLY!")
