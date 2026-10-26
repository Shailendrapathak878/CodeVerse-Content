"""
Test and validation script for Topic 10: Logistic Regression.
Validates all manual formulas: Sigmoid function, Log-odds, Odds Ratio,
Log Loss, Confusion Matrix metrics (Accuracy, Precision, Recall, F1),
ROC AUC, threshold variation, and Scikit-Learn Pipeline lab execution.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, roc_curve, log_loss
)

print("=== 1. Sigmoid Function Arithmetic Validation ===")
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

z_test_vals = [0.0, 1.8, -1.8, 5.0, -5.0]
for z in z_test_vals:
    sig_val = sigmoid(z)
    print(f"  z = {z:+4.1f} -> sigma(z) = {sig_val:.4f}")

assert np.isclose(sigmoid(0.0), 0.5)
assert np.isclose(sigmoid(1.8), 0.8581, atol=0.001)
assert np.isclose(sigmoid(-1.8), 0.1419, atol=0.001)
assert np.isclose(sigmoid(5.0), 0.9933, atol=0.001)
assert np.isclose(sigmoid(-5.0), 0.0067, atol=0.001)
assert np.isclose(sigmoid(1.8) + sigmoid(-1.8), 1.0)
print("[PASS] Sigmoid symmetry and values verified!")

print("\n=== 2. Odds, Log-Odds (Logits), and Odds Ratio Validation ===")
# Suppose p = 0.80
p = 0.80
odds = p / (1.0 - p)
log_odds = np.log(odds)
print(f"For probability p = {p:.2f}:")
print(f"  Odds = p / (1 - p) = {odds:.2f} (or {odds:.0f} to 1)")
print(f"  Log-Odds (logit) = ln({odds:.2f}) = {log_odds:.4f}")
assert np.isclose(odds, 4.0)
assert np.isclose(log_odds, 1.3863, atol=0.001)

# Suppose beta_1 = 1.2
beta_1 = 1.2
odds_ratio = np.exp(beta_1)
print(f"For feature slope beta_1 = {beta_1:.2f}:")
print(f"  Odds Ratio = exp({beta_1:.2f}) = {odds_ratio:.4f}")
assert np.isclose(odds_ratio, 3.3201, atol=0.001)
print("[PASS] Odds and Odds Ratio verified!")

print("\n=== 3. Binary Cross-Entropy / Log Loss Validation ===")
# Case 1: True y = 1
# Confident correct: p = 0.90 -> loss = -ln(0.90) = 0.1054
# Confident wrong:   p = 0.10 -> loss = -ln(0.10) = 2.3026
loss_y1_p90 = -np.log(0.90)
loss_y1_p10 = -np.log(0.10)
# Case 2: True y = 0
# Confident correct: p = 0.10 -> loss = -ln(1 - 0.10) = 0.1054
# Confident wrong:   p = 0.90 -> loss = -ln(1 - 0.90) = 2.3026
loss_y0_p10 = -np.log(1.0 - 0.10)
loss_y0_p90 = -np.log(1.0 - 0.90)

print(f"True y=1, Pred p=0.90 (Confident Correct): Log Loss = {loss_y1_p90:.4f}")
print(f"True y=1, Pred p=0.10 (Confident Wrong):   Log Loss = {loss_y1_p10:.4f} (21.8x penalty!)")
print(f"True y=0, Pred p=0.10 (Confident Correct): Log Loss = {loss_y0_p10:.4f}")
print(f"True y=0, Pred p=0.90 (Confident Wrong):   Log Loss = {loss_y0_p90:.4f} (21.8x penalty!)")
assert np.isclose(loss_y1_p90, 0.1054, atol=0.001)
assert np.isclose(loss_y1_p10, 2.3026, atol=0.001)
print("[PASS] Binary log-loss penalty dynamics verified!")

print("\n=== 4. Threshold Variation Validation (6 Samples) ===")
sample_probs = np.array([0.15, 0.35, 0.48, 0.52, 0.75, 0.92])
pred_t05 = (sample_probs >= 0.50).astype(int)
pred_t03 = (sample_probs >= 0.30).astype(int)
pred_t07 = (sample_probs >= 0.70).astype(int)

print(f"Sample Probabilities: {sample_probs}")
print(f"Threshold 0.50 Predictions: {pred_t05} -> {np.sum(pred_t05)} positive")
print(f"Threshold 0.30 Predictions: {pred_t03} -> {np.sum(pred_t03)} positive (higher sensitivity)")
print(f"Threshold 0.70 Predictions: {pred_t07} -> {np.sum(pred_t07)} positive (higher precision)")
assert list(pred_t05) == [0, 0, 0, 1, 1, 1]
assert list(pred_t03) == [0, 1, 1, 1, 1, 1]
assert list(pred_t07) == [0, 0, 0, 0, 1, 1]
print("[PASS] Threshold shifting behavior verified!")

print("\n=== 5. Confusion Matrix & Classification Metrics Validation ===")
# Worked Confusion Matrix Example (100 Patient Medical Screening)
# True Positive (TP) = 18, False Negative (FN) = 2 (Total Sick = 20)
# False Positive (FP) = 6, True Negative (TN) = 74 (Total Healthy = 80)
TP = 18
FN = 2
FP = 6
TN = 74
total_samples = TP + TN + FP + FN
assert total_samples == 100

acc = (TP + TN) / total_samples
prec = TP / (TP + FP)
rec = TP / (TP + FN)
f1 = 2.0 * (prec * rec) / (prec + rec)
tpr = rec
fpr = FP / (FP + TN)

print(f"Confusion Matrix: TP={TP}, FN={FN}, FP={FP}, TN={TN}")
print(f"Accuracy:  {acc:.4f} (92.0%)")
print(f"Precision: {prec:.4f} (75.0%)")
print(f"Recall:    {rec:.4f} (90.0%)")
print(f"F1-Score:  {f1:.4f} (81.8%)")
print(f"FPR:       {fpr:.4f} (7.5%)")

assert np.isclose(acc, 0.9200)
assert np.isclose(prec, 0.7500)
assert np.isclose(rec, 0.9000)
assert np.isclose(f1, 0.8182, atol=0.001)
print("[PASS] Classification metric arithmetic verified!")

print("\n=== 6. Complete Practical Lab Data & Pipeline Verification ===")
# Generate synthetic dataset for Student Course Exam Success (200 students)
# Features:
# 1. Study_Hours (weekly hours, 2 to 30)
# 2. Attendance_Pct (lecture attendance percentage, 40 to 100)
# 3. Previous_Score (prior GPA / exam score, 45 to 98)
# 4. Assignments_Done (homework count, 1 to 10)
# Target: Passed_Exam (0 = Fail, 1 = Pass, approx 65% pass rate)
np.random.seed(42)
n_students = 200

study_hours = np.random.uniform(3, 28, n_students)
attendance = np.random.uniform(45, 99, n_students)
prev_score = np.random.uniform(48, 95, n_students)
assignments = np.random.randint(1, 11, n_students)

# Underlying logistic probability model
z_latent = (
    -11.0
    + 0.18 * study_hours
    + 0.045 * attendance
    + 0.050 * prev_score
    + 0.35 * assignments
    + np.random.normal(0, 0.5, n_students)
)
true_probs = sigmoid(z_latent)
passed = (true_probs >= 0.50).astype(int)

df = pd.DataFrame({
    'Student_ID': [f'STU-{i:04d}' for i in range(1, n_students + 1)],
    'Study_Hours': np.round(study_hours, 1),
    'Attendance_Pct': np.round(attendance, 1),
    'Previous_Score': np.round(prev_score, 1),
    'Assignments_Done': assignments,
    'Passed_Exam': passed
})

print(f"Generated Dataset Shape: {df.shape}")
print(f"Class Distribution: {np.bincount(passed)} (Fail: {np.mean(passed==0):.1%}, Pass: {np.mean(passed==1):.1%})")

# Stratified Train/Test split (80/20)
train_df, test_df = train_test_split(
    df, test_size=0.20, random_state=42, stratify=df['Passed_Exam']
)

# Assert zero overlap
overlap_ids = set(train_df['Student_ID']).intersection(set(test_df['Student_ID']))
assert len(overlap_ids) == 0, "Data Leakage! Train and test share student IDs!"
print(f"Train size: {len(train_df)}, Test size: {len(test_df)}, Shared IDs: {len(overlap_ids)}")

feature_cols = ['Study_Hours', 'Attendance_Pct', 'Previous_Score', 'Assignments_Done']
X_train = train_df[feature_cols]
y_train = train_df['Passed_Exam']
X_test = test_df[feature_cols]
y_test = test_df['Passed_Exam']

# Leak-free Scikit-Learn Pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(random_state=42, C=1.0))
])

# Fit strictly on training data
pipe.fit(X_train, y_train)

# Assert scaler mean equals X_train mean
scaler_fitted = pipe.named_steps['scaler']
assert np.allclose(scaler_fitted.mean_, X_train.mean(axis=0)), "Scaler leaked test data!"
print("[PASS] Zero Data Leakage: Pipeline fitted strictly on X_train!")

# Generate test predictions and probabilities
test_probs = pipe.predict_proba(X_test)[:, 1]
test_preds = pipe.predict(X_test)

test_acc = accuracy_score(y_test, test_preds)
test_prec = precision_score(y_test, test_preds)
test_rec = recall_score(y_test, test_preds)
test_f1 = f1_score(y_test, test_preds)
test_auc = roc_auc_score(y_test, test_probs)
cm = confusion_matrix(y_test, test_preds)

print("\n--- Practical Lab Test Evaluation Metrics ---")
print(f"Test Accuracy:  {test_acc:.4f} ({test_acc:.1%})")
print(f"Test Precision: {test_prec:.4f} ({test_prec:.1%})")
print(f"Test Recall:    {test_rec:.4f} ({test_rec:.1%})")
print(f"Test F1-Score:  {test_f1:.4f} ({test_f1:.1%})")
print(f"Test ROC AUC:   {test_auc:.4f} ({test_auc:.1%})")
print("Confusion Matrix (Test Set):")
print(cm)

logreg_fitted = pipe.named_steps['logreg']
print(f"\nFitted Intercept: {logreg_fitted.intercept_[0]:.4f}")
for col, coef in zip(feature_cols, logreg_fitted.coef_[0]):
    print(f"  {col:18s}: {coef:+.4f} (Odds Ratio: {np.exp(coef):.4f})")

assert test_acc >= 0.85, "Test accuracy should be >= 85% on clean signal!"
assert test_auc >= 0.90, "Test ROC AUC should be >= 90%!"
assert np.all((test_probs >= 0.0) & (test_probs <= 1.0)), "Probabilities must lie strictly in [0, 1]!"

print("\n=== 7. Regularization Strength Comparison (C parameter) ===")
# Compare C=0.01 (heavy regularization) vs C=1.0 vs C=100.0 (weak)
pipe_c_small = Pipeline([('scaler', StandardScaler()), ('logreg', LogisticRegression(C=0.01, random_state=42))])
pipe_c_large = Pipeline([('scaler', StandardScaler()), ('logreg', LogisticRegression(C=100.0, random_state=42))])

pipe_c_small.fit(X_train, y_train)
pipe_c_large.fit(X_train, y_train)

coef_l2_small = pipe_c_small.named_steps['logreg'].coef_[0]
coef_l2_large = pipe_c_large.named_steps['logreg'].coef_[0]

print(f"C=0.01 (Heavy L2 penalty) weights magnitude: {np.linalg.norm(coef_l2_small):.4f}")
print(f"C=1.00 (Standard)        weights magnitude: {np.linalg.norm(logreg_fitted.coef_[0]):.4f}")
print(f"C=100  (Weak penalty)    weights magnitude: {np.linalg.norm(coef_l2_large):.4f}")
assert np.linalg.norm(coef_l2_small) < np.linalg.norm(coef_l2_large), "Small C must shrink weights more strongly!"
print("[PASS] Regularization parameter C behavior verified!")

print("\nALL TOPIC 10 NUMERICAL AND CODE VERIFICATION TESTS PASSED SUCCESSFULLY!")
