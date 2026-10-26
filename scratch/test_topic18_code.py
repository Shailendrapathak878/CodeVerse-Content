import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

print("=== STEP 1: STATISTICAL Z-SCORE EXAMPLE ===")
# Small transaction amount dataset (in INR or USD)
# Everyday purchases around 500, with one 500,000 transaction or similar
tx_amounts = np.array([120, 150, 180, 200, 220, 250, 280, 310, 350, 1500])
mean_val = np.mean(tx_amounts)
std_val = np.std(tx_amounts, ddof=0)
z_scores = (tx_amounts - mean_val) / std_val
print(f"Data: {tx_amounts}")
print(f"Mean: {mean_val:.2f}, Std: {std_val:.2f}")
print("Z-scores:", [round(z, 2) for z in z_scores])
outliers_z = tx_amounts[np.abs(z_scores) > 2.5]
print("Flagged (|z| > 2.5):", outliers_z)

print("\n=== STEP 2: IQR EXAMPLE ===")
# Distribution with an extreme outlier
iqr_data = np.array([45, 52, 55, 60, 62, 65, 70, 72, 75, 80, 85, 140])
q1 = np.percentile(iqr_data, 25)
median = np.median(iqr_data)
q3 = np.percentile(iqr_data, 75)
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr
outliers_iqr = iqr_data[(iqr_data < lower_fence) | (iqr_data > upper_fence)]
print(f"Data: {iqr_data}")
print(f"Q1: {q1:.1f}, Median: {median:.1f}, Q3: {q3:.1f}, IQR: {iqr:.1f}")
print(f"Lower Fence: {lower_fence:.1f}, Upper Fence: {upper_fence:.1f}")
print(f"Outliers outside fences:", outliers_iqr)

print("\n=== STEP 3: ISOLATION FOREST 2D SYNTHETIC ===")
rng = np.random.RandomState(42)
# Normal points (200 points clustered around (5, 5))
X_normal = rng.normal(loc=5.0, scale=1.0, size=(200, 2))
# Deliberate anomalies (10 points scattered far away)
X_anom = rng.uniform(low=0.0, high=10.0, size=(10, 2))
# Filter out points that accidentally fall near the cluster
X_anom = X_anom[np.linalg.norm(X_anom - [5, 5], axis=1) > 3.0][:10]
X_iso = np.vstack([X_normal, X_anom])
y_true_iso = np.array([1]*len(X_normal) + [-1]*len(X_anom)) # 1: normal, -1: anomaly

iso_forest = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
iso_preds = iso_forest.fit_predict(X_iso)
iso_scores = iso_forest.decision_function(X_iso)

n_anomalies_flagged = np.sum(iso_preds == -1)
n_normal_flagged = np.sum(iso_preds == 1)
print(f"Total points: {len(X_iso)}")
print(f"Isolation Forest flagged anomalies: {n_anomalies_flagged}, normal: {n_normal_flagged}")
print(f"Min decision score (most abnormal): {iso_scores.min():.4f}")
print(f"Max decision score (most normal): {iso_scores.max():.4f}")

print("\n=== STEP 4: LOCAL OUTLIER FACTOR (LOF) ===")
# Two clusters of different densities
# Cluster 1: dense (100 points, scale 0.5) around (2, 2)
# Cluster 2: sparse (100 points, scale 1.2) around (7, 7)
# Local anomaly: near dense cluster, but locally sparse
c1 = rng.normal(loc=2.0, scale=0.4, size=(100, 2))
c2 = rng.normal(loc=7.0, scale=1.0, size=(100, 2))
local_anom = np.array([[3.2, 3.2], [1.0, 3.5], [8.0, 3.0]])
X_lof = np.vstack([c1, c2, local_anom])

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.04)
lof_preds = lof.fit_predict(X_lof)
lof_factors = -lof.negative_outlier_factor_ # Convert to standard LOF where > 1 means outlier
n_lof_anom = np.sum(lof_preds == -1)
print(f"LOF total points: {len(X_lof)}, flagged anomalies: {n_lof_anom}")
print(f"Max LOF score: {lof_factors.max():.3f}, Mean LOF: {lof_factors.mean():.3f}")

print("\n=== STEP 5: ONE-CLASS SVM ===")
scaler = StandardScaler()
X_oc_scaled = scaler.fit_transform(X_iso)
oc_svm = OneClassSVM(kernel='rbf', gamma='scale', nu=0.05)
oc_preds = oc_svm.fit_predict(X_oc_scaled)
n_oc_anom = np.sum(oc_preds == -1)
print(f"One-Class SVM flagged anomalies: {n_oc_anom}, normal: {np.sum(oc_preds == 1)}")

print("\n=== STEP 6: SYNTHETIC TRANSACTION DETECTION PROJECT ===")
# Transaction amount (₹) and Transaction frequency (tx/hour)
# Normal: 450 transactions, Amount ~ N(1500, 400), Frequency ~ N(3, 1)
# Anomalies: 25 transactions, e.g. High amount + low freq, or massive frequency spike
np.random.seed(42)
n_normal_tx = 475
n_anom_tx = 25

amount_norm = np.random.normal(loc=1200, scale=350, size=n_normal_tx)
amount_norm = np.clip(amount_norm, 100, 3000)
freq_norm = np.random.normal(loc=4, scale=1.5, size=n_normal_tx)
freq_norm = np.clip(freq_norm, 1, 10)
X_proj_norm = np.column_stack([amount_norm, freq_norm])

# Injected anomalies:
# 15 high amount transactions (e.g. ₹5,500 - ₹12,000, with a couple near normal boundary around ₹3,200)
# 10 burst velocity transactions (e.g. freq 12 - 35 tx/hour)
amount_anom_1 = np.array([3200, 3400, 5500, 6200, 7100, 7800, 8500, 9200, 9800, 10500, 11200, 12000, 13500, 14200, 15000], dtype=float)
freq_anom_1 = np.array([4.2, 3.8, 2.5, 4.0, 1.8, 3.2, 2.9, 4.5, 3.0, 2.1, 1.5, 3.8, 2.2, 4.1, 1.9], dtype=float)

amount_anom_2 = np.array([850, 1200, 1400, 1600, 1900, 2100, 2300, 2500, 2700, 2800], dtype=float)
freq_anom_2 = np.array([11.5, 12.0, 15.0, 18.5, 22.0, 26.0, 29.5, 34.0, 38.0, 42.0], dtype=float)

X_proj_anom = np.vstack([
    np.column_stack([amount_anom_1, freq_anom_1]),
    np.column_stack([amount_anom_2, freq_anom_2])
])

X_project = np.vstack([X_proj_norm, X_proj_anom])
# Labels: 0 for normal, 1 for anomaly (ground truth)
y_project_true = np.array([0]*n_normal_tx + [1]*n_anom_tx)

# Train Isolation Forest with contamination=0.05 (25 expected anomalies out of 500)
iso_proj = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
iso_proj_preds = iso_proj.fit_predict(X_project)
# Convert scikit-learn format (1: normal, -1: anomaly) to binary (0: normal, 1: anomaly)
y_project_pred = np.where(iso_proj_preds == -1, 1, 0)

cm = confusion_matrix(y_project_true, y_project_pred)
tn, fp, fn, tp = cm.ravel()
prec = precision_score(y_project_true, y_project_pred)
rec = recall_score(y_project_true, y_project_pred)
f1 = f1_score(y_project_true, y_project_pred)

print(f"Project Dataset: {len(X_project)} transactions ({n_normal_tx} normal, {n_anom_tx} anomalous)")
print(f"Confusion Matrix: TN={tn}, FP={fp}, FN={fn}, TP={tp}")
print(f"Precision: {prec:.4f} ({prec*100:.2f}%)")
print(f"Recall: {rec:.4f} ({rec*100:.2f}%)")
print(f"F1-Score: {f1:.4f}")

# Threshold sweep: Decision Function vs Flagged Counts
scores = iso_proj.decision_function(X_project)
print("\n=== STEP 7: THRESHOLD SWEEP ===")
thresholds = np.linspace(scores.min(), scores.max(), 10)
for th in thresholds:
    flagged = np.sum(scores < th)
    print(f"Threshold: {th:+.3f} -> Flagged: {flagged:3d} ({flagged/len(X_project)*100:.1f}%)")
