# Topic 22 Python Verification Script
# Hyperparameter Tuning: Manual, Grid Search, Random Search, Nested CV, Learning & Validation Curves
# Using breast cancer dataset (binary classification, N=569, 30 features)

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import (
    train_test_split, KFold, StratifiedKFold, cross_val_score,
    GridSearchCV, RandomizedSearchCV, learning_curve, validation_curve
)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# 1. Load Data & Create Train/Holdout Test Split (80% Train, 20% Vaulted Test)
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"Dataset: Breast Cancer (Total={len(X)}, Train={len(X_train)}, Holdout Test={len(X_test)})")
print(f"Target Distribution: Malignant={sum(y==0)} ({sum(y==0)/len(y):.1%}), Benign={sum(y==1)} ({sum(y==1)/len(y):.1%})")

# 2. Section 03 & 05: Manual Hyperparameter Tuning on KNN
# Compare n_neighbors in [1, 3, 5, 7, 9, 11, 15, 21, 31]
k_values = [1, 3, 5, 7, 9, 11, 15, 21, 31]
manual_results = []

print("\n--- 2. MANUAL TUNING: KNN (Scaled) ---")
for k in k_values:
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier(n_neighbors=k))
    ])
    pipe.fit(X_train, y_train)
    tr_acc = pipe.score(X_train, y_train)
    cv_scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring='accuracy')
    cv_mean = np.mean(cv_scores)
    cv_std = np.std(cv_scores)
    manual_results.append((k, tr_acc, cv_mean, cv_std))
    print(f"  k={k:2d} | Train Acc: {tr_acc:.4f} | 5-Fold CV Acc: {cv_mean:.4f} +/- {cv_std:.4f}")

# 3. Section 08: GridSearchCV Practical
# KNN Grid Search: n_neighbors, weights, metric
knn_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

param_grid_knn = {
    'knn__n_neighbors': [3, 5, 7, 9, 11, 15],
    'knn__weights': ['uniform', 'distance'],
    'knn__p': [1, 2] # Manhattan vs Euclidean
}
# Total configurations = 6 * 2 * 2 = 24. Total fits = 24 * 5 = 120 fits.

grid_search = GridSearchCV(
    knn_pipe,
    param_grid=param_grid_knn,
    cv=5,
    scoring='accuracy',
    return_train_score=True,
    n_jobs=1
)
grid_search.fit(X_train, y_train)

print("\n--- 3. GridSearchCV RESULTS ---")
print(f"Total configurations: {len(grid_search.cv_results_['params'])}")
print(f"Best Params: {grid_search.best_params_}")
print(f"Best 5-Fold CV Accuracy: {grid_search.best_score_:.4f}")

# Test set evaluation of best model
best_knn = grid_search.best_estimator_
test_acc_grid = best_knn.score(X_test, y_test)
print(f"Holdout Test Accuracy: {test_acc_grid:.4f}")

# Top 5 configurations
print("\nTop 5 Grid Configurations:")
rank_indices = np.argsort(grid_search.cv_results_['rank_test_score'])[:5]
for idx in rank_indices:
    p = grid_search.cv_results_['params'][idx]
    mean_s = grid_search.cv_results_['mean_test_score'][idx]
    std_s = grid_search.cv_results_['std_test_score'][idx]
    print(f"  Score: {mean_s:.4f} +/- {std_s:.4f} | Params: {p}")

# 4. Section 10: RandomizedSearchCV Practical
# Random Forest Random Search: n_estimators, max_depth, min_samples_split, min_samples_leaf
rf = RandomForestClassifier(random_state=42)
param_dist_rf = {
    'n_estimators': [20, 50, 100, 150, 200],
    'max_depth': [3, 5, 8, 12, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None]
}
# Total potential combinations = 5 * 5 * 3 * 3 * 3 = 675 combinations!
# Random Search will evaluate n_iter = 20 configurations = 20 * 5 = 100 fits.

random_search = RandomizedSearchCV(
    rf,
    param_distributions=param_dist_rf,
    n_iter=20,
    cv=5,
    scoring='accuracy',
    random_state=42,
    n_jobs=1
)
random_search.fit(X_train, y_train)

print("\n--- 4. RandomizedSearchCV RESULTS ---")
print(f"Evaluated 20 random configurations out of 675 total!")
print(f"Best Params: {random_search.best_params_}")
print(f"Best 5-Fold CV Accuracy: {random_search.best_score_:.4f}")

test_acc_rand = random_search.best_estimator_.score(X_test, y_test)
print(f"Holdout Test Accuracy: {test_acc_rand:.4f}")

# 5. Section 13: Metric Selection & Trade-offs
# Compare default model vs tuned model across Accuracy, Precision, Recall, F1, ROC-AUC
y_pred_grid = best_knn.predict(X_test)
y_prob_grid = best_knn.predict_proba(X_test)[:, 1]

print("\n--- 5. METRIC AUDIT (Best Tuned KNN on Test Set) ---")
print(f"  Accuracy:  {accuracy_score(y_test, y_pred_grid):.4f}")
print(f"  Precision: {precision_score(y_test, y_pred_grid):.4f}")
print(f"  Recall:    {recall_score(y_test, y_pred_grid):.4f}")
print(f"  F1 Score:  {f1_score(y_test, y_pred_grid):.4f}")
print(f"  ROC-AUC:   {roc_auc_score(y_test, y_prob_grid):.4f}")

# 6. Section 18: Validation Curve (Decision Tree max_depth from 1 to 15)
depth_range = range(1, 16)
dt = DecisionTreeClassifier(random_state=42)
tr_sc_dt, val_sc_dt = validation_curve(
    dt, X_train, y_train,
    param_name='max_depth',
    param_range=depth_range,
    cv=5,
    scoring='accuracy'
)
tr_mean_dt = np.mean(tr_sc_dt, axis=1)
val_mean_dt = np.mean(val_sc_dt, axis=1)

print("\n--- 6. VALIDATION CURVE: Decision Tree max_depth ---")
for d, tr, val in zip(depth_range, tr_mean_dt, val_mean_dt):
    print(f"  Depth {d:2d} | Train Acc: {tr:.4f} | Val Acc: {val:.4f} | Gap: {tr - val:.4f}")

# 7. Section 18: Learning Curve (Best Tuned Model)
train_sizes, tr_sc_lc, val_sc_lc = learning_curve(
    best_knn, X_train, y_train,
    train_sizes=np.linspace(0.1, 1.0, 5),
    cv=5,
    scoring='accuracy'
)
print("\n--- 7. LEARNING CURVE: Tuned KNN ---")
for sz, tr, val in zip(train_sizes, np.mean(tr_sc_lc, axis=1), np.mean(val_sc_lc, axis=1)):
    print(f"  Train Size {sz:3d} | Train Acc: {tr:.4f} | Val Acc: {val:.4f} | Gap: {tr - val:.4f}")

# 8. Section 20: Nested Cross-Validation (5 outer folds, 3 inner folds)
# Evaluates model-selection procedure without test set bias
inner_cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
outer_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

nested_clf = GridSearchCV(
    estimator=knn_pipe,
    param_grid={'knn__n_neighbors': [3, 5, 7, 9, 11]},
    cv=inner_cv,
    scoring='accuracy'
)
nested_scores = cross_val_score(nested_clf, X_train, y_train, cv=outer_cv, scoring='accuracy')
print("\n--- 8. NESTED CROSS-VALIDATION ---")
print(f"Outer Fold Accuracies: {np.round(nested_scores, 4)}")
print(f"Nested CV Mean Accuracy: {np.mean(nested_scores):.4f} +/- {np.std(nested_scores):.4f}")
