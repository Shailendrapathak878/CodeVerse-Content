"""
Test and validation script for Topic 12: Decision Trees.
Validates all manual formulas: Gini Impurity, Entropy, Information Gain,
Gini Reduction, DecisionTreeClassifier lab pipeline, DecisionTreeRegressor lab pipeline,
feature importances, confusion matrix metrics, and anti-leakage checks.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_text
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, mean_absolute_error, mean_squared_error
)

print("=== 1. Gini Impurity Arithmetic Validation ===")
# Pure Node: [10, 0]
p_pure = np.array([1.0, 0.0])
gini_pure = 1.0 - np.sum(p_pure**2)

# Balanced Node: [10, 10]
p_bal = np.array([0.5, 0.5])
gini_bal = 1.0 - np.sum(p_bal**2)

# Imbalanced Node: [14, 6]
p_imbal = np.array([14.0/20.0, 6.0/20.0])
gini_imbal = 1.0 - np.sum(p_imbal**2)

print(f"Gini Pure [10, 0]:       {gini_pure:.4f} (Expected: 0.0000)")
print(f"Gini Balanced [10, 10]:  {gini_bal:.4f} (Expected: 0.5000)")
print(f"Gini Imbalanced [14, 6]: {gini_imbal:.4f} (Expected: 0.4200)")

assert np.isclose(gini_pure, 0.0)
assert np.isclose(gini_bal, 0.5)
assert np.isclose(gini_imbal, 0.4200)
print("[PASS] Gini Impurity calculations verified!")

print("\n=== 2. Entropy Arithmetic Validation ===")
def calc_entropy(counts):
    total = np.sum(counts)
    if total == 0:
        return 0.0
    p = counts / total
    # Convention: 0 * log2(0) = 0
    p_nonzero = p[p > 0]
    return -np.sum(p_nonzero * np.log2(p_nonzero))

ent_pure = calc_entropy(np.array([10, 0]))
ent_bal = calc_entropy(np.array([10, 10]))
ent_imbal = calc_entropy(np.array([14, 6]))

print(f"Entropy Pure [10, 0]:       {ent_pure:.4f} (Expected: 0.0000)")
print(f"Entropy Balanced [10, 10]:  {ent_bal:.4f} (Expected: 1.0000)")
print(f"Entropy Imbalanced [14, 6]: {ent_imbal:.4f} (Expected: 0.8813)")

assert np.isclose(ent_pure, 0.0)
assert np.isclose(ent_bal, 1.0)
assert np.isclose(ent_imbal, 0.8813, atol=0.001)
print("[PASS] Entropy calculations verified!")

print("\n=== 3. Information Gain Arithmetic Validation ===")
# Parent node: 20 students (10 Pass, 10 Fail)
parent_counts = np.array([10, 10])
h_parent = calc_entropy(parent_counts)

# Split on Study Hours >= 5:
# Left Child (Hours < 5): 8 students (1 Pass, 7 Fail)
left_counts = np.array([1, 7])
h_left = calc_entropy(left_counts)

# Right Child (Hours >= 5): 12 students (9 Pass, 3 Fail)
right_counts = np.array([9, 3])
h_right = calc_entropy(right_counts)

# Weighted Child Entropy
w_left = 8.0 / 20.0
w_right = 12.0 / 20.0
h_children_weighted = (w_left * h_left) + (w_right * h_right)

# Information Gain
info_gain = h_parent - h_children_weighted

print(f"Parent Entropy H(parent):           {h_parent:.4f}")
print(f"Left Child Entropy H(left):         {h_left:.4f}")
print(f"Right Child Entropy H(right):       {h_right:.4f}")
print(f"Weighted Children Entropy:          {h_children_weighted:.4f}")
print(f"Information Gain (IG):              {info_gain:.4f} (Expected: ~0.2958)")

assert np.isclose(h_parent, 1.0)
assert np.isclose(h_left, 0.5436, atol=0.001)
assert np.isclose(h_right, 0.8113, atol=0.001)
assert np.isclose(h_children_weighted, 0.7042, atol=0.001)
assert np.isclose(info_gain, 0.2958, atol=0.001)

# Gini Gain for the exact same split:
def calc_gini(counts):
    total = np.sum(counts)
    if total == 0:
        return 0.0
    p = counts / total
    return 1.0 - np.sum(p**2)

g_parent = calc_gini(parent_counts)
g_left = calc_gini(left_counts)
g_right = calc_gini(right_counts)
g_children_weighted = (w_left * g_left) + (w_right * g_right)
gini_gain = g_parent - g_children_weighted

print(f"Parent Gini:                        {g_parent:.4f}")
print(f"Left Gini:                          {g_left:.4f}")
print(f"Right Gini:                         {g_right:.4f}")
print(f"Weighted Children Gini:             {g_children_weighted:.4f}")
print(f"Gini Impurity Reduction (Gini Gain):{gini_gain:.4f} (Expected: 0.1875)")

assert np.isclose(g_parent, 0.5000)
assert np.isclose(g_left, 0.2188, atol=0.001)
assert np.isclose(g_right, 0.3750, atol=0.001)
assert np.isclose(g_children_weighted, 0.3125, atol=0.001)
assert np.isclose(gini_gain, 0.1875, atol=0.001)
print("[PASS] Information Gain and Gini Gain verified!")

print("\n=== 4. Complete Classification Lab Pipeline Validation ===")
np.random.seed(42)
n_total = 240

# Feature 1: Study Hours per week (range ~ 1 to 14)
# Feature 2: Lecture Attendance Percentage (range ~ 40 to 100%)
# Target: 0 = Fail, 1 = Pass

# Class 0 (Fail): lower study hours and attendance
study_c0 = np.random.normal(loc=4.5, scale=1.5, size=120)
attend_c0 = np.random.normal(loc=65.0, scale=10.0, size=120)
y_c0 = np.zeros(120, dtype=int)

# Class 1 (Pass): higher study hours and attendance
study_c1 = np.random.normal(loc=8.5, scale=1.6, size=120)
attend_c1 = np.random.normal(loc=85.0, scale=8.0, size=120)
y_c1 = np.ones(120, dtype=int)

X_study = np.clip(np.concatenate([study_c0, study_c1]), 1.0, 15.0)
X_attend = np.clip(np.concatenate([attend_c0, attend_c1]), 40.0, 100.0)
y_all = np.concatenate([y_c0, y_c1])

df_lab = pd.DataFrame({
    'Study_Hours': np.round(X_study, 1),
    'Attendance_Pct': np.round(X_attend, 1),
    'Passed_Exam': y_all,
    'Student_ID': [f"STD-{i:04d}" for i in range(1, n_total + 1)]
})

print(f"Classification Dataset Shape: {df_lab.shape}")
print(f"Class Balance:\n{df_lab['Passed_Exam'].value_counts()}")

# Stratified split: 80% train (192), 20% test (48)
train_df, test_df = train_test_split(
    df_lab, test_size=0.20, random_state=42, stratify=df_lab['Passed_Exam']
)

# Zero leakage check
overlap = set(train_df['Student_ID']).intersection(set(test_df['Student_ID']))
assert len(overlap) == 0
print(f"Train samples: {len(train_df)}, Test samples: {len(test_df)} (Zero overlap)")

X_train = train_df[['Study_Hours', 'Attendance_Pct']]
y_train = train_df['Passed_Exam']
X_test = test_df[['Study_Hours', 'Attendance_Pct']]
y_test = test_df['Passed_Exam']

# 5-Fold Cross-Validation on training data across candidate max_depths
depth_candidates = [1, 2, 3, 4, 5, 6, 8, 10]
cv_scores = {}
train_scores = {}

for d in depth_candidates:
    dt = DecisionTreeClassifier(max_depth=d, criterion='gini', random_state=42)
    scores = cross_val_score(dt, X_train, y_train, cv=5, scoring='accuracy')
    dt.fit(X_train, y_train)
    cv_scores[d] = np.mean(scores)
    train_scores[d] = accuracy_score(y_train, dt.predict(X_train))
    print(f"  max_depth={d:2d} -> Train Acc: {train_scores[d]:.4f} | 5-Fold CV Acc: {cv_scores[d]:.4f}")

best_depth = max(cv_scores, key=cv_scores.get)
print(f"Selected Optimal Depth: max_depth={best_depth} (CV Acc: {cv_scores[best_depth]:.4f})")

# Fit final model with chosen best_depth (or standard depth 3 for clean pedagogy)
final_dt = DecisionTreeClassifier(max_depth=3, criterion='gini', random_state=42)
final_dt.fit(X_train, y_train)

# Test evaluation
y_test_pred = final_dt.predict(X_test)
acc = accuracy_score(y_test, y_test_pred)
prec = precision_score(y_test, y_test_pred)
rec = recall_score(y_test, y_test_pred)
f1 = f1_score(y_test, y_test_pred)
cm = confusion_matrix(y_test, y_test_pred)

print("\n--- Holdout Test Set Performance (N = 48) ---")
print(f"Test Accuracy:  {acc:.4f} ({acc:.1%})")
print(f"Test Precision: {prec:.4f} ({prec:.1%})")
print(f"Test Recall:    {rec:.4f} ({rec:.1%})")
print(f"Test F1-Score:  {f1:.4f} ({f1:.1%})")
print("Confusion Matrix:")
print(cm)

# Feature importances
feat_importances = pd.Series(final_dt.feature_importances_, index=X_train.columns)
print("\nFeature Importances (MDI / Gini Importance):")
for feat, imp in feat_importances.items():
    print(f"  {feat}: {imp:.4f} ({imp:.1%})")

assert acc >= 0.85
assert f1 >= 0.85
print("[PASS] Classification lab verified successfully!")

print("\n=== 5. Complete Decision Tree Regression Lab Validation ===")
np.random.seed(42)
n_reg = 100

# Feature: House Size in 100 sq ft (range 8.0 to 32.0 -> 800 to 3200 sq ft)
# Target: House Price in $k USD
sqft_reg = np.random.uniform(8.0, 32.0, n_reg)
noise = np.random.normal(0, 18.0, n_reg)
price_reg = 50.0 + (11.5 * sqft_reg) + noise

df_reg = pd.DataFrame({
    'Living_Area_100sqft': np.round(sqft_reg, 1),
    'Price_kUSD': np.round(price_reg, 1)
})

X_r = df_reg[['Living_Area_100sqft']]
y_r = df_reg['Price_kUSD']

X_r_train, X_r_test, y_r_train, y_r_test = train_test_split(
    X_r, y_r, test_size=0.25, random_state=42
)

reg_tree = DecisionTreeRegressor(max_depth=3, random_state=42)
reg_tree.fit(X_r_train, y_r_train)

y_r_pred = reg_tree.predict(X_r_test)
mae_reg = mean_absolute_error(y_r_test, y_r_pred)
rmse_reg = np.sqrt(mean_squared_error(y_r_test, y_r_pred))

print(f"Regression Tree (max_depth=3) Holdout MAE:  ${mae_reg:.2f}k USD")
print(f"Regression Tree (max_depth=3) Holdout RMSE: ${rmse_reg:.2f}k USD")

# Verify sample prediction
test_house = pd.DataFrame({'Living_Area_100sqft': [20.0]})
pred_house_price = reg_tree.predict(test_house)[0]
print(f"Predicted price for 2,000 sq ft house: ${pred_house_price:.2f}k USD")

assert mae_reg < 25.0
assert rmse_reg < 30.0
print("[PASS] Regression lab verified successfully!")

print("\nALL MATHEMATICAL & CODE VERIFICATIONS FOR TOPIC 12 COMPLETED SUCCESSFULLY!")
