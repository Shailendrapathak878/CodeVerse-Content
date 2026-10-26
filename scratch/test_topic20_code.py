# Python code test and numerical verification for Topic 20: Cross-Validation & Model Validation

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import (
    train_test_split, KFold, StratifiedKFold, cross_val_score,
    GridSearchCV, RandomizedSearchCV, learning_curve, validation_curve,
    TimeSeriesSplit, GroupKFold
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

print("=== TOPIC 20 NUMERICAL AND CODE VERIFICATION ===")

# 1. Stratified vs Ordinary K-Fold on Imbalanced Dataset
print("\n--- 1. Stratified vs Ordinary K-Fold (100 samples: 90 Class 0, 10 Class 1) ---")
np.random.seed(42)
y_imbal = np.array([0]*90 + [1]*10)
X_imbal = np.random.randn(100, 2)

kf = KFold(n_splits=5, shuffle=True, random_state=42)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("Ordinary K-Fold minority class counts per fold:")
for fold_idx, (train_idx, val_idx) in enumerate(kf.split(X_imbal, y_imbal)):
    n_minority = np.sum(y_imbal[val_idx] == 1)
    print(f"  Fold {fold_idx+1}: {n_minority} minority samples (out of {len(val_idx)} total)")

print("Stratified K-Fold minority class counts per fold:")
for fold_idx, (train_idx, val_idx) in enumerate(skf.split(X_imbal, y_imbal)):
    n_minority = np.sum(y_imbal[val_idx] == 1)
    print(f"  Fold {fold_idx+1}: {n_minority} minority samples (out of {len(val_idx)} total)")

# 2. Iris Dataset: 5-Fold Cross Validation Workflow
print("\n--- 2. Iris 5-Fold Cross-Validation Workflow ---")
iris = load_iris()
X, y = iris.data, iris.target

# Holdout final test set (20% = 30 samples, train = 120 samples)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
print(f"Dataset: Total N={len(X)}, Train N={len(X_train)}, Final Test N={len(X_test)}")

# Single train/validation split comparison on X_train (60% train_sub, 20% val_sub)
X_sub_tr, X_sub_val, y_sub_tr, y_sub_val = train_test_split(
    X_train, y_train, test_size=0.25, random_state=42, stratify=y_train
)
single_model = KNeighborsClassifier(n_neighbors=5)
single_model.fit(X_sub_tr, y_sub_tr)
single_val_acc = single_model.score(X_sub_val, y_sub_val)
print(f"Single Train/Val Split Accuracy: {single_val_acc:.4f} ({single_val_acc*100:.1f}%)")

# 5-Fold Cross-Validation on X_train
knn_cv = KNeighborsClassifier(n_neighbors=5)
skf_5 = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(knn_cv, X_train, y_train, cv=skf_5, scoring="accuracy")

print("5-Fold CV Scores on X_train:")
for i, s in enumerate(cv_scores):
    print(f"  Fold {i+1}: {s:.4f} ({s*100:.1f}%)")
mean_cv = np.mean(cv_scores)
std_cv = np.std(cv_scores)
print(f"Mean CV Score: {mean_cv:.4f} ({mean_cv*100:.2f}%) +/- {std_cv:.4f}")

# 3. GridSearchCV
print("\n--- 3. GridSearchCV on X_train ---")
param_grid = {
    'n_neighbors': [1, 3, 5, 7, 9, 11],
    'weights': ['uniform', 'distance']
}
grid_search = GridSearchCV(
    KNeighborsClassifier(),
    param_grid,
    cv=skf_5,
    scoring='accuracy',
    return_train_score=True
)
grid_search.fit(X_train, y_train)
print(f"GridSearch Best Parameters: {grid_search.best_params_}")
print(f"GridSearch Best CV Score:   {grid_search.best_score_:.4f} ({grid_search.best_score_*100:.2f}%)")

# Final Test evaluation of best model
best_knn = grid_search.best_estimator_
final_test_score = best_knn.score(X_test, y_test)
print(f"Final Test Set Evaluation: {final_test_score:.4f} ({final_test_score*100:.2f}%)")

# 4. RandomizedSearchCV
print("\n--- 4. RandomizedSearchCV on X_train ---")
param_dist = {
    'n_neighbors': list(range(1, 15)),
    'weights': ['uniform', 'distance'],
    'p': [1, 2]  # Manhattan vs Euclidean distance
}
rand_search = RandomizedSearchCV(
    KNeighborsClassifier(),
    param_dist,
    n_iter=10,
    cv=skf_5,
    scoring='accuracy',
    random_state=42
)
rand_search.fit(X_train, y_train)
print(f"RandomizedSearch Best Parameters: {rand_search.best_params_}")
print(f"RandomizedSearch Best CV Score:   {rand_search.best_score_:.4f} ({rand_search.best_score_*100:.2f}%)")

# 5. Learning Curve
print("\n--- 5. Learning Curve Computation ---")
train_sizes, train_scores, val_scores = learning_curve(
    DecisionTreeClassifier(max_depth=3, random_state=42),
    X_train, y_train,
    cv=skf_5,
    train_sizes=np.linspace(0.2, 1.0, 5),
    scoring='accuracy',
    random_state=42
)
train_mean = np.mean(train_scores, axis=1)
val_mean = np.mean(val_scores, axis=1)
for ts, tm, vm in zip(train_sizes, train_mean, val_mean):
    print(f"  Train Size: {ts:2d} -> Train Acc: {tm:.4f}, Val Acc: {vm:.4f}, Gap: {tm - vm:.4f}")

# 6. Validation Curve (varying max_depth on Decision Tree)
print("\n--- 6. Validation Curve (varying max_depth) ---")
depth_range = [1, 2, 3, 4, 5, 6, 8, 10]
vc_train_scores, vc_val_scores = validation_curve(
    DecisionTreeClassifier(random_state=42),
    X_train, y_train,
    param_name="max_depth",
    param_range=depth_range,
    cv=skf_5,
    scoring="accuracy"
)
vc_tr_mean = np.mean(vc_train_scores, axis=1)
vc_val_mean = np.mean(vc_val_scores, axis=1)
for d, tr_m, val_m in zip(depth_range, vc_tr_mean, vc_val_mean):
    print(f"  max_depth={d:2d} -> Train: {tr_m:.4f}, Val: {val_m:.4f}")

# 7. Leakage Demonstration (Scaling before CV vs Inside Pipeline)
print("\n--- 7. Data Leakage Demonstration ---")
# Breast cancer dataset has large variance in feature scales
cancer = load_breast_cancer()
Xc, yc = cancer.data, cancer.target
Xc_train, Xc_test, yc_train, yc_test = train_test_split(Xc, yc, test_size=0.25, random_state=42, stratify=yc)

# Safe Pipeline
safe_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(max_iter=1000, random_state=42))
])
safe_scores = cross_val_score(safe_pipeline, Xc_train, yc_train, cv=5, scoring='accuracy')
print(f"Safe Pipeline CV Mean: {np.mean(safe_scores):.4f} +/- {np.std(safe_scores):.4f}")

# 8. Time-Series Split Verification
print("\n--- 8. Time-Series Split Verification ---")
tscv = TimeSeriesSplit(n_splits=5)
X_dummy = np.arange(60).reshape(30, 2)
for fold_idx, (tr_idx, val_idx) in enumerate(tscv.split(X_dummy)):
    print(f"  TS Split {fold_idx+1}: Train indices {tr_idx[0]}..{tr_idx[-1]} (size {len(tr_idx)}), Val indices {val_idx[0]}..{val_idx[-1]} (size {len(val_idx)})")

# 9. Group K-Fold Verification
print("\n--- 9. Group K-Fold Verification ---")
groups = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6])
y_grp = np.random.randint(0, 2, len(groups))
X_grp = np.random.randn(len(groups), 2)
gkf = GroupKFold(n_splits=3)
for fold_idx, (tr_idx, val_idx) in enumerate(gkf.split(X_grp, y_grp, groups=groups)):
    val_groups = np.unique(groups[val_idx])
    train_groups = np.unique(groups[tr_idx])
    overlap = set(val_groups).intersection(set(train_groups))
    print(f"  Group Fold {fold_idx+1}: Train groups {train_groups}, Val groups {val_groups}, Overlap: {len(overlap)}")

print("\n=== VERIFICATION FINISHED SUCCESSFULLY ===")
