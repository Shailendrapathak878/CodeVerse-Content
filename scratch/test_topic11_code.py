"""
Test and validation script for Topic 11: K-Nearest Neighbors (KNN).
Validates all manual formulas: Euclidean distance, Manhattan distance,
Minkowski distance, manual distance ranking, unweighted vs weighted voting,
feature scaling distortions, classification lab pipeline, and regression lab.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, mean_absolute_error, mean_squared_error
)

print("=== 1. Distance Metrics Arithmetic Validation ===")
# Point A = (2, 3), Point B = (6, 6)
pA = np.array([2.0, 3.0])
pB = np.array([6.0, 6.0])

diff = pB - pA  # (4.0, 3.0)
d_euclidean = np.sqrt(np.sum(diff**2))
d_manhattan = np.sum(np.abs(diff))
p_mink = 3.0
d_minkowski = (np.sum(np.abs(diff)**p_mink))**(1.0 / p_mink)

print(f"Point A: {pA}, Point B: {pB}")
print(f"  Euclidean distance: sqrt(4^2 + 3^2) = {d_euclidean:.4f}")
print(f"  Manhattan distance: |4| + |3| = {d_manhattan:.4f}")
print(f"  Minkowski (p=3): (4^3 + 3^3)^(1/3) = {d_minkowski:.4f}")

assert np.isclose(d_euclidean, 5.0)
assert np.isclose(d_manhattan, 7.0)
assert np.isclose(d_minkowski, 4.4979, atol=0.001)
print("[PASS] Distance metric calculations verified!")

print("\n=== 2. Manual KNN Worked Example Validation ===")
# 6 training points: Sweetness (x1) and Crispness (x2), Class: 0 = Apple, 1 = Orange
train_points = [
    {"id": "T1", "x1": 4.0, "x2": 6.0, "label": "Apple", "class": 0},
    {"id": "T2", "x1": 6.0, "x2": 5.0, "label": "Apple", "class": 0},
    {"id": "T3", "x1": 5.0, "x2": 3.0, "label": "Orange", "class": 1},
    {"id": "T4", "x1": 7.0, "x2": 6.0, "label": "Orange", "class": 1},
    {"id": "T5", "x1": 3.0, "x2": 3.0, "label": "Apple", "class": 0},
    {"id": "T6", "x1": 8.0, "x2": 4.0, "label": "Orange", "class": 1},
]
query_point = np.array([5.0, 5.0])

calc_list = []
for pt in train_points:
    coords = np.array([pt["x1"], pt["x2"]])
    d_euc = np.sqrt(np.sum((coords - query_point)**2))
    d_man = np.sum(np.abs(coords - query_point))
    calc_list.append({
        "id": pt["id"],
        "x1": pt["x1"],
        "x2": pt["x2"],
        "class": pt["class"],
        "label": pt["label"],
        "d_euc": round(d_euc, 4),
        "d_man": round(d_man, 4)
    })

df_calc = pd.DataFrame(calc_list).sort_values("d_euc").reset_index(drop=True)
df_calc["rank"] = df_calc.index + 1
print("Ranked training points by Euclidean distance to Query (5, 5):")
print(df_calc[["rank", "id", "x1", "x2", "label", "d_euc", "d_man"]])

# Verify K=1, K=3, K=5 predictions
pred_k1 = df_calc.loc[0, "class"]
pred_k3 = df_calc.loc[0:2, "class"].mode()[0]
pred_k5 = df_calc.loc[0:4, "class"].mode()[0]

print(f"K=1 Winner: {df_calc.loc[0, 'label']} (Class {pred_k1})")
print(f"K=3 Votes: {dict(df_calc.loc[0:2, 'label'].value_counts())} -> Winner: Class {pred_k3}")
print(f"K=5 Votes: {dict(df_calc.loc[0:4, 'label'].value_counts())} -> Winner: Class {pred_k5}")

assert pred_k1 == 0
assert pred_k3 == 0
assert pred_k5 == 0
print("[PASS] Manual KNN worked example verified!")

print("\n=== 3. Unweighted vs. Distance-Weighted Voting Validation ===")
# Query Q with 3 neighbors:
# Neighbor 1: dist = 1.0, Class 1 (Orange)
# Neighbor 2: dist = 3.0, Class 0 (Apple)
# Neighbor 3: dist = 3.0, Class 0 (Apple)
n_dists = np.array([1.0, 3.0, 3.0])
n_classes = np.array([1, 0, 0])

# Unweighted majority vote
unweighted_votes_c0 = np.sum(n_classes == 0)
unweighted_votes_c1 = np.sum(n_classes == 1)
unweighted_winner = 0 if unweighted_votes_c0 > unweighted_votes_c1 else 1

# Weighted vote: weight = 1 / distance
weights = 1.0 / n_dists
weighted_score_c0 = np.sum(weights[n_classes == 0])
weighted_score_c1 = np.sum(weights[n_classes == 1])
weighted_winner = 0 if weighted_score_c0 > weighted_score_c1 else 1

print(f"Unweighted Votes: Class 0 (Apple) = {unweighted_votes_c0}, Class 1 (Orange) = {unweighted_votes_c1} -> Winner: Class {unweighted_winner}")
print(f"Weighted Scores: Class 0 (Apple) = {weighted_score_c0:.4f}, Class 1 (Orange) = {weighted_score_c1:.4f} -> Winner: Class {weighted_winner}")

assert unweighted_winner == 0, "Unweighted winner should be Class 0 (Apple) by 2 vs 1!"
assert weighted_winner == 1, "Weighted winner should be Class 1 (Orange) by 1.0000 vs 0.6667!"
print("[PASS] Divergent weighted vs unweighted voting scenario verified!")

print("\n=== 4. Feature Scaling Disproportion Validation ===")
person_A = np.array([30.0, 50000.0])  # Age 30, Income $50k
person_B = np.array([50.0, 50100.0])  # Age 50, Income $50.1k
person_C = np.array([31.0, 60000.0])  # Age 31, Income $60k

d_raw_AB = np.sqrt(np.sum((person_B - person_A)**2))
d_raw_AC = np.sqrt(np.sum((person_C - person_A)**2))
print(f"Raw Euclidean Dist(A, B): {d_raw_AB:.2f}")
print(f"Raw Euclidean Dist(A, C): {d_raw_AC:.2f}")
assert d_raw_AB < d_raw_AC, "Raw distance makes B closer to A despite 20-year age gap!"

# Scale data with StandardScaler
all_persons = np.vstack([person_A, person_B, person_C])
scaler_test = StandardScaler().fit(all_persons)
scaled_persons = scaler_test.transform(all_persons)
d_scaled_AB = np.sqrt(np.sum((scaled_persons[1] - scaled_persons[0])**2))
d_scaled_AC = np.sqrt(np.sum((scaled_persons[2] - scaled_persons[0])**2))
print(f"Scaled Euclidean Dist(A, B): {d_scaled_AB:.4f}")
print(f"Scaled Euclidean Dist(A, C): {d_scaled_AC:.4f}")
assert d_scaled_AC < d_scaled_AB, "After scaling, Person C (similar age) is correctly closer!"
print("[PASS] Feature scaling demonstration verified!")

print("\n=== 5. Complete Classification Lab Pipeline Validation ===")
np.random.seed(42)
n_samples = 200

# Create a clean synthetic classification dataset with 2 features
# Class 0: centered around (4.5, 4.5)
# Class 1: centered around (7.0, 7.0)
X0 = np.random.normal(loc=[4.5, 4.5], scale=1.1, size=(100, 2))
y0 = np.zeros(100, dtype=int)

X1 = np.random.normal(loc=[7.0, 7.0], scale=1.1, size=(100, 2))
y1 = np.ones(100, dtype=int)

X = np.vstack([X0, X1])
y = np.concatenate([y0, y1])

df_lab = pd.DataFrame(X, columns=['Feature_1', 'Feature_2'])
df_lab['Target'] = y
df_lab['Sample_ID'] = [f"SMP-{i:04d}" for i in range(1, n_samples + 1)]

print(f"Classification Dataset Shape: {df_lab.shape}")
print(f"Class counts: {np.bincount(y)}")

# Stratified split 80/20
train_df, test_df = train_test_split(
    df_lab, test_size=0.20, random_state=42, stratify=df_lab['Target']
)

# Verify zero leakage
overlap_ids = set(train_df['Sample_ID']).intersection(set(test_df['Sample_ID']))
assert len(overlap_ids) == 0

X_train = train_df[['Feature_1', 'Feature_2']]
y_train = train_df['Target']
X_test = test_df[['Feature_1', 'Feature_2']]
y_test = test_df['Target']

print(f"Train samples: {len(X_train)}, Test samples: {len(X_test)}")

# Cross-validation on training data to select best K
k_candidates = [1, 3, 5, 7, 9, 11, 15, 21]
cv_scores = {}
for k in k_candidates:
    pipe_k = Pipeline([
        ('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier(n_neighbors=k))
    ])
    scores = cross_val_score(pipe_k, X_train, y_train, cv=5, scoring='accuracy')
    cv_scores[k] = np.mean(scores)
    print(f"  Candidate K={k:2d}: 5-Fold CV Accuracy = {cv_scores[k]:.4f}")

best_k = max(cv_scores, key=cv_scores.get)
print(f"Selected Best K based on CV: K={best_k} (CV Accuracy: {cv_scores[best_k]:.4f})")

# Fit final pipeline with K=5 on training data
final_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])
final_pipe.fit(X_train, y_train)

# Assert scaler mean equals X_train mean
scaler_fitted = final_pipe.named_steps['scaler']
assert np.allclose(scaler_fitted.mean_, X_train.mean(axis=0)), "Data leakage in scaler!"

test_preds = final_pipe.predict(X_test)
test_probs = final_pipe.predict_proba(X_test)[:, 1]

acc = accuracy_score(y_test, test_preds)
prec = precision_score(y_test, test_preds)
rec = recall_score(y_test, test_preds)
f1 = f1_score(y_test, test_preds)
cm = confusion_matrix(y_test, test_preds)

print("\n--- Holdout Test Evaluation (N = 40) ---")
print(f"Test Accuracy:  {acc:.4f} ({acc:.1%})")
print(f"Test Precision: {prec:.4f} ({prec:.1%})")
print(f"Test Recall:    {rec:.4f} ({rec:.1%})")
print(f"Test F1-Score:  {f1:.4f} ({f1:.1%})")
print("Confusion Matrix:")
print(cm)

assert acc >= 0.85
assert f1 >= 0.85
print("[PASS] Classification lab pipeline verified!")

print("\n=== 6. KNN Regression Lab Validation ===")
# Synthetic numerical dataset: Predicting House Price ($k) from Square Footage (100 sq ft units)
np.random.seed(42)
n_reg = 80
sqft = np.random.uniform(8.0, 32.0, n_reg)  # 800 to 3200 sq ft
price = 45.0 + (12.5 * sqft) + np.random.normal(0, 15.0, n_reg)  # linear base with noise

X_reg = sqft.reshape(-1, 1)
y_reg = price

X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(
    X_reg, y_reg, test_size=0.25, random_state=42
)

reg_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('knn_reg', KNeighborsRegressor(n_neighbors=5))
])
reg_pipe.fit(X_reg_train, y_reg_train)

reg_preds = reg_pipe.predict(X_reg_test)
mae = mean_absolute_error(y_reg_test, reg_preds)
rmse = np.sqrt(mean_squared_error(y_reg_test, reg_preds))

print(f"KNN Regression (K=5) Holdout MAE:  ${mae:.2f}k USD")
print(f"KNN Regression (K=5) Holdout RMSE: ${rmse:.2f}k USD")
assert mae < 25.0, "Regression MAE should be reasonable on smooth signal!"
print("[PASS] KNN Regression lab verified!")

print("\nALL TOPIC 11 CODE VERIFICATIONS PASSED SUCCESSFULLY!")
