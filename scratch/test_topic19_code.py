import numpy as np
import pandas as pd
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, average_precision_score,
    mean_absolute_error, mean_squared_error, r2_score,
    classification_report
)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

print("=== STEP 1: SMALL BINARY CLASSIFICATION WORKED EXAMPLE (10 samples) ===")
y_true_small = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
y_prob_small = np.array([0.92, 0.85, 0.78, 0.65, 0.35, 0.60, 0.40, 0.30, 0.20, 0.10])
threshold = 0.50
y_pred_small = (y_prob_small >= threshold).astype(int)

cm_small = confusion_matrix(y_true_small, y_pred_small)
tn, fp, fn, tp = cm_small.ravel()
acc_small = accuracy_score(y_true_small, y_pred_small)
prec_small = precision_score(y_true_small, y_pred_small)
rec_small = recall_score(y_true_small, y_pred_small)
spec_small = tn / (tn + fp)
fpr_small = fp / (fp + tn)
fnr_small = fn / (fn + tp)
f1_small = f1_score(y_true_small, y_pred_small)
roc_auc_small = roc_auc_score(y_true_small, y_prob_small)
ap_small = average_precision_score(y_true_small, y_prob_small)

print(f"y_true: {y_true_small}")
print(f"y_prob: {y_prob_small}")
print(f"y_pred: {y_pred_small}")
print(f"Confusion Matrix: TN={tn}, FP={fp}, FN={fn}, TP={tp}")
print(f"Accuracy: {acc_small:.4f}")
print(f"Precision: {prec_small:.4f}")
print(f"Recall: {rec_small:.4f}")
print(f"Specificity: {spec_small:.4f}")
print(f"FPR: {fpr_small:.4f}, FNR: {fnr_small:.4f}")
print(f"F1-Score: {f1_small:.4f}")
print(f"ROC-AUC: {roc_auc_small:.4f}")
print(f"Average Precision (AP): {ap_small:.4f}")

print("\n=== STEP 2: MULTICLASS 3-CLASS WORKED EXAMPLE (Cat=0, Dog=1, Bird=2) ===")
# 15 samples
y_true_multi = np.array([0, 0, 0, 0, 0,  1, 1, 1, 1, 1,  2, 2, 2, 2, 2])
y_pred_multi = np.array([0, 0, 0, 1, 0,  1, 1, 1, 2, 0,  2, 2, 2, 2, 1])

cm_multi = confusion_matrix(y_true_multi, y_pred_multi)
print("Multiclass Confusion Matrix (Rows=True [Cat, Dog, Bird], Cols=Pred):")
print(cm_multi)

prec_macro = precision_score(y_true_multi, y_pred_multi, average='macro')
prec_micro = precision_score(y_true_multi, y_pred_multi, average='micro')
prec_weight = precision_score(y_true_multi, y_pred_multi, average='weighted')

rec_macro = recall_score(y_true_multi, y_pred_multi, average='macro')
rec_micro = recall_score(y_true_multi, y_pred_multi, average='micro')
rec_weight = recall_score(y_true_multi, y_pred_multi, average='weighted')

f1_macro = f1_score(y_true_multi, y_pred_multi, average='macro')
f1_micro = f1_score(y_true_multi, y_pred_multi, average='micro')
f1_weight = f1_score(y_true_multi, y_pred_multi, average='weighted')

print(f"Precision -> Macro: {prec_macro:.4f}, Micro: {prec_micro:.4f}, Weighted: {prec_weight:.4f}")
print(f"Recall    -> Macro: {rec_macro:.4f}, Micro: {rec_micro:.4f}, Weighted: {rec_weight:.4f}")
print(f"F1-Score  -> Macro: {f1_macro:.4f}, Micro: {f1_micro:.4f}, Weighted: {f1_weight:.4f}")
print("\nClassification Report:")
print(classification_report(y_true_multi, y_pred_multi, target_names=['Cat', 'Dog', 'Bird']))

print("\n=== STEP 3: SMALL REGRESSION WORKED EXAMPLE (5 houses) ===")
y_true_reg = np.array([200.0, 250.0, 300.0, 350.0, 400.0])
y_pred_reg = np.array([210.0, 240.0, 320.0, 340.0, 420.0])

residuals = y_true_reg - y_pred_reg
abs_errors = np.abs(residuals)
sq_errors = residuals ** 2

mae_val = mean_absolute_error(y_true_reg, y_pred_reg)
mse_val = mean_squared_error(y_true_reg, y_pred_reg)
rmse_val = np.sqrt(mse_val)
r2_val = r2_score(y_true_reg, y_pred_reg)

print(f"Actual: {y_true_reg}")
print(f"Predicted: {y_pred_reg}")
print(f"Residuals (y - y_hat): {residuals}")
print(f"Absolute Errors: {abs_errors}, Sum: {abs_errors.sum()}")
print(f"Squared Errors: {sq_errors}, Sum: {sq_errors.sum()}")
print(f"MAE: {mae_val:.2f}")
print(f"MSE: {mse_val:.2f}")
print(f"RMSE: {rmse_val:.4f}")
print(f"R² Score: {r2_val:.4f}")

print("\n=== STEP 4: SECTION 25 PRACTICAL WORKFLOWS ===")
# Workflow A: Classification
np.random.seed(42)
n_samples = 250
# 2 informative features
X_cls = np.random.randn(n_samples, 2)
# True log-odds: 1.5 * x0 - 2.0 * x1 + noise
logits = 1.5 * X_cls[:, 0] - 2.0 * X_cls[:, 1] + 0.5 * np.random.randn(n_samples)
y_cls = (logits > 0).astype(int)

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X_cls, y_cls, test_size=0.25, random_state=42, stratify=y_cls
)

clf = LogisticRegression()
clf.fit(X_train_c, y_train_c)
y_pred_c = clf.predict(X_test_c)
y_prob_c = clf.predict_proba(X_test_c)[:, 1]

cm_c = confusion_matrix(y_test_c, y_pred_c)
acc_c = accuracy_score(y_test_c, y_pred_c)
prec_c = precision_score(y_test_c, y_pred_c)
rec_c = recall_score(y_test_c, y_pred_c)
f1_c = f1_score(y_test_c, y_pred_c)
auc_c = roc_auc_score(y_test_c, y_prob_c)
ap_c = average_precision_score(y_test_c, y_prob_c)

print(f"Classification Practical (Test set size = {len(y_test_c)}):")
print(f"  Confusion Matrix: {cm_c.tolist()}")
print(f"  Accuracy: {acc_c:.4f} ({acc_c*100:.2f}%)")
print(f"  Precision: {prec_c:.4f} ({prec_c*100:.2f}%)")
print(f"  Recall: {rec_c:.4f} ({rec_c*100:.2f}%)")
print(f"  F1-Score: {f1_c:.4f}")
print(f"  ROC-AUC: {auc_c:.4f}")
print(f"  Average Precision: {ap_c:.4f}")

# Workflow B: Regression
# Synthetic house price dataset: size (sq ft), bedrooms, distance to city
np.random.seed(42)
n_reg = 250
size = np.random.uniform(800, 3500, n_reg)
dist = np.random.uniform(2, 35, n_reg)
price = 50.0 + 0.12 * size - 2.5 * dist + np.random.normal(0, 25, n_reg)
X_reg = np.column_stack([size, dist])

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_reg, price, test_size=0.25, random_state=42
)

reg = LinearRegression()
reg.fit(X_train_r, y_train_r)
y_pred_r = reg.predict(X_test_r)

mae_r = mean_absolute_error(y_test_r, y_pred_r)
mse_r = mean_squared_error(y_test_r, y_pred_r)
rmse_r = np.sqrt(mse_r)
r2_r = r2_score(y_test_r, y_pred_r)

print(f"\nRegression Practical (Test set size = {len(y_test_r)}):")
print(f"  MAE: {mae_r:.2f} (in thousands INR)")
print(f"  MSE: {mse_r:.2f}")
print(f"  RMSE: {rmse_r:.2f} (in thousands INR)")
print(f"  R2 Score: {r2_r:.4f} ({r2_r*100:.2f}% variance explained)")
