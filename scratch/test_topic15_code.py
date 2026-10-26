import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import (
    VotingClassifier,
    BaggingClassifier,
    RandomForestClassifier,
    RandomForestRegressor,
    AdaBoostClassifier,
    GradientBoostingClassifier,
    GradientBoostingRegressor,
    StackingClassifier
)
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, mean_absolute_error, mean_squared_error, r2_score
)
from sklearn.datasets import make_moons
import xgboost as xgb

print("=== 1. MATHEMATICAL VERIFICATION ===")
# Hard Voting vs Soft Voting
# Model A, B, C probabilities for Class 0 and Class 1
probs_A = np.array([0.40, 0.60])  # predicts Class 1
probs_B = np.array([0.45, 0.55])  # predicts Class 1
probs_C = np.array([0.70, 0.30])  # predicts Class 0

# Hard voting:
preds_hard = [np.argmax(probs_A), np.argmax(probs_B), np.argmax(probs_C)]
hard_winner = 1 if preds_hard.count(1) > preds_hard.count(0) else 0
print(f"Hard Voting Predictions: Model A={preds_hard[0]}, Model B={preds_hard[1]}, Model C={preds_hard[2]}")
print(f"Hard Voting Winner: Class {hard_winner} (Votes: Class 1 = 2, Class 0 = 1)")

# Soft voting (equal weights average):
avg_probs = (probs_A + probs_B + probs_C) / 3.0
soft_winner = np.argmax(avg_probs)
print(f"Soft Voting Combined Probabilities: P(C0) = {avg_probs[0]:.4f}, P(C1) = {avg_probs[1]:.4f}")
print(f"Soft Voting Winner: Class {soft_winner} ({avg_probs[soft_winner]*100:.2f}% confidence)")
print("Notice: Hard voting selected Class 1, but Soft voting selected Class 0 due to Model C's decisive conviction!")

# Weighted Regression Averaging:
preds_reg = np.array([75.0, 82.0, 68.0])
weights = np.array([0.5, 0.3, 0.2])
weighted_avg = np.sum(preds_reg * weights)
simple_avg = np.mean(preds_reg)
print(f"Regression Simple Average: ({preds_reg[0]} + {preds_reg[1]} + {preds_reg[2]}) / 3 = {simple_avg:.2f}")
print(f"Regression Weighted Average: 0.5*75 + 0.3*82 + 0.2*68 = {weighted_avg:.2f}")

# Bootstrap OOB mathematical proportion:
np.random.seed(42)
N = 1000
bootstrap_indices = np.random.choice(N, size=N, replace=True)
unique_in_sample = len(np.unique(bootstrap_indices))
oob_count = N - unique_in_sample
print(f"Bootstrap Sample (N={N}): In-Sample Unique = {unique_in_sample} ({unique_in_sample/N*100:.1f}%), OOB = {oob_count} ({oob_count/N*100:.1f}%)")
print(f"Theoretical OOB limit: 1/e = {1/np.e:.4f} ({1/np.e*100:.2f}%)")

print("\n=== 2. CLASSIFICATION LAB: MULTI-MODEL BENCHMARK ===")
# Synthetic non-linear dataset: 240 samples, 2 features (make_moons + noise)
X_moons, y_moons = make_moons(n_samples=240, noise=0.25, random_state=42)

# 60% Train, 20% Validation, 20% Final Test (Stratified)
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X_moons, y_moons, test_size=0.20, random_state=42, stratify=y_moons
)
X_train, X_val, y_train, y_val = train_test_split(
    X_train_val, y_train_val, test_size=0.25, random_state=42, stratify=y_train_val
)

print(f"Data Splits: Train={len(X_train)} (60%), Val={len(X_val)} (20%), Test={len(X_test)} (20%)")

# Base models & Ensembles
models = {
    "Logistic Regression": Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression(random_state=42))]),
    "Single Decision Tree": DecisionTreeClassifier(max_depth=3, random_state=42),
    "Bagging (50 Trees)": BaggingClassifier(estimator=DecisionTreeClassifier(max_depth=4), n_estimators=50, random_state=42),
    "Random Forest (100 Trees)": RandomForestClassifier(n_estimators=100, max_depth=5, oob_score=True, random_state=42),
    "AdaBoost (50 Trees)": AdaBoostClassifier(n_estimators=50, learning_rate=0.8, random_state=42),
    "Gradient Boosting (60 Trees)": GradientBoostingClassifier(n_estimators=60, learning_rate=0.1, max_depth=3, random_state=42),
    "XGBoost (50 Trees)": xgb.XGBClassifier(n_estimators=50, learning_rate=0.1, max_depth=3, eval_metric='logloss', random_state=42),
    "Soft Voting Ensemble": VotingClassifier(
        estimators=[
            ('lr', Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression(random_state=42))])),
            ('rf', RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)),
            ('gb', GradientBoostingClassifier(n_estimators=60, learning_rate=0.1, max_depth=3, random_state=42))
        ],
        voting='soft'
    ),
    "Stacking Classifier": StackingClassifier(
        estimators=[
            ('dt', DecisionTreeClassifier(max_depth=4, random_state=42)),
            ('rf', RandomForestClassifier(n_estimators=80, max_depth=4, random_state=42)),
            ('ada', AdaBoostClassifier(n_estimators=40, random_state=42))
        ],
        final_estimator=LogisticRegression(random_state=42),
        cv=5
    )
}

val_results = {}
test_results = {}

print("\n--- Model Training & Validation / Test Evaluation ---")
for name, clf in models.items():
    clf.fit(X_train, y_train)
    val_preds = clf.predict(X_val)
    test_preds = clf.predict(X_test)
    
    val_acc = accuracy_score(y_val, val_preds)
    test_acc = accuracy_score(y_test, test_preds)
    test_prec = precision_score(y_test, test_preds)
    test_rec = recall_score(y_test, test_preds)
    test_f1 = f1_score(y_test, test_preds)
    
    val_results[name] = val_acc
    test_results[name] = {
        'val_acc': val_acc,
        'test_acc': test_acc,
        'test_prec': test_prec,
        'test_rec': test_rec,
        'test_f1': test_f1
    }
    print(f"{name:28s} | Val Acc: {val_acc:.4f} | Test Acc: {test_acc:.4f} | Test F1: {test_f1:.4f}")

# Best model on validation
best_model_name = max(val_results, key=val_results.get)
print(f"\nBest Model selected via Validation: '{best_model_name}' (Val Acc: {val_results[best_model_name]:.4f})")

# Test evaluation of best model
best_clf = models[best_model_name]
y_test_pred = best_clf.predict(X_test)
cm = confusion_matrix(y_test, y_test_pred)
print(f"\nFinal Test Confusion Matrix for '{best_model_name}':\n{cm}")
tn, fp, fn, tp = cm.ravel()
print(f"  TN={tn}, FP={fp}, FN={fn}, TP={tp}")

# Random Forest OOB Score check
rf_model = models["Random Forest (100 Trees)"]
print(f"\nRandom Forest OOB Score: {rf_model.oob_score_:.4f} ({rf_model.oob_score_*100:.2f}%)")
print(f"Random Forest Feature Importances: {rf_model.feature_importances_}")

print("\n=== 3. REGRESSION LAB: ENSEMBLE COMPARISON ===")
# Synthetic non-linear 1D regression dataset: 160 samples
np.random.seed(42)
X_reg = np.linspace(-3, 3, 160).reshape(-1, 1)
y_reg = np.sin(X_reg).ravel() + 0.3 * X_reg.ravel() + np.random.normal(0, 0.25, size=160)

X_r_train, X_r_test, y_r_train, y_r_test = train_test_split(X_reg, y_reg, test_size=0.25, random_state=42)

reg_models = {
    "Single Decision Tree Regressor": DecisionTreeRegressor(max_depth=3, random_state=42),
    "Random Forest Regressor (80 Trees)": RandomForestRegressor(n_estimators=80, max_depth=4, random_state=42),
    "Gradient Boosting Regressor (60 Trees)": GradientBoostingRegressor(n_estimators=60, learning_rate=0.1, max_depth=3, random_state=42)
}

print(f"Regression Data: Train={len(X_r_train)}, Test={len(X_r_test)}")
reg_results = {}
for r_name, r_model in reg_models.items():
    r_model.fit(X_r_train, y_r_train)
    r_preds = r_model.predict(X_r_test)
    mae = mean_absolute_error(y_r_test, r_preds)
    rmse = np.sqrt(mean_squared_error(y_r_test, r_preds))
    r2 = r2_score(y_r_test, r_preds)
    reg_results[r_name] = {'mae': mae, 'rmse': rmse, 'r2': r2}
    print(f"{r_name:38s} | MAE: {mae:.4f} | RMSE: {rmse:.4f} | R2: {r2:.4f}")

# Averaging Regressor
preds_tree = reg_models["Single Decision Tree Regressor"].predict(X_r_test)
preds_rf = reg_models["Random Forest Regressor (80 Trees)"].predict(X_r_test)
preds_gb = reg_models["Gradient Boosting Regressor (60 Trees)"].predict(X_r_test)
avg_preds = (preds_tree + preds_rf + preds_gb) / 3.0
avg_mae = mean_absolute_error(y_r_test, avg_preds)
avg_rmse = np.sqrt(mean_squared_error(y_r_test, avg_preds))
avg_r2 = r2_score(y_r_test, avg_preds)
print(f"{'Averaging Ensemble (Tree + RF + GB)':38s} | MAE: {avg_mae:.4f} | RMSE: {avg_rmse:.4f} | R2: {avg_r2:.4f}")

print("\n=== 4. GRADIENT BOOSTING LOSS ACROSS STAGES ===")
gb_model = models["Gradient Boosting (60 Trees)"]
train_deviance = gb_model.train_score_
print(f"GB Initial Training Loss: {train_deviance[0]:.4f} -> Final Loss (Stage 60): {train_deviance[-1]:.4f}")

print("\nALL ENSEMBLE CALCULATIONS AND CODE LABS COMPLETED SUCCESSFULLY.")
