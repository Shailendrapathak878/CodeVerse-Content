import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC, SVR
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, mean_absolute_error, mean_squared_error
from sklearn.datasets import make_classification, make_circles

print("=== 1. MATHEMATICAL FORMULAS VERIFICATION ===")
# Hyperplane 2D: w1*x1 + w2*x2 + b = 0
# Let w = [1.2, 1.6], b = -3.0
w = np.array([1.2, 1.6])
b = -3.0
w_norm = np.linalg.norm(w)
margin_width = 2.0 / w_norm
print(f"w = {w}, norm = {w_norm:.4f}, margin_width = 2 / ||w|| = {margin_width:.4f}")

# Point x_test
x_A = np.array([2.5, 2.0])
dist_A = np.dot(w, x_A) + b
print(f"Point x_A={x_A}: w^T x + b = {dist_A:.4f} -> Distance to hyperplane = |w^T x + b| / ||w|| = {abs(dist_A)/w_norm:.4f}")

# Kernels
x_k = np.array([2.0, 3.0])
z_k = np.array([4.0, 1.0])
dot_prod = np.dot(x_k, z_k)
print(f"Linear Kernel K(x, z) = x^T z = 2*4 + 3*1 = {dot_prod:.4f}")

gamma_val = 0.1
sq_dist = np.sum((x_k - z_k)**2)
rbf_val = np.exp(-gamma_val * sq_dist)
print(f"Squared Euclidean distance ||x - z||^2 = (-2)^2 + (2)^2 = {sq_dist:.4f}")
print(f"RBF Kernel K(x, z) = exp(-0.1 * {sq_dist}) = {rbf_val:.4f}")

r_val = 1.0
d_val = 2
poly_val = (1.0 * dot_prod + r_val)**d_val
print(f"Polynomial Kernel K(x, z) = (1.0 * {dot_prod} + {r_val})^{d_val} = ({dot_prod + r_val})^{d_val} = {poly_val:.4f}")

# Standardization
x_raw = 72.0
mu = 50.0
sigma = 10.0
z_score = (x_raw - mu) / sigma
print(f"Standardization z = ({x_raw} - {mu}) / {sigma} = {z_score:.4f}")

print("\n=== 2. CLASSIFICATION LAB (SYNTHETIC ADMISSIONS DATASET) ===")
np.random.seed(42)
n_samples = 240

# Feature 1: Exam Score (mean 55 vs 75, std 10)
# Feature 2: Project Score (mean 50 vs 72, std 12)
c0_exam = np.random.normal(loc=54.0, scale=9.5, size=n_samples // 2)
c0_proj = np.random.normal(loc=52.0, scale=10.0, size=n_samples // 2)
y_c0 = np.zeros(n_samples // 2, dtype=int)

c1_exam = np.random.normal(loc=76.0, scale=9.5, size=n_samples // 2)
c1_proj = np.random.normal(loc=74.0, scale=10.0, size=n_samples // 2)
y_c1 = np.ones(n_samples // 2, dtype=int)

X1 = np.clip(np.concatenate([c0_exam, c1_exam]), 30.0, 100.0)
X2 = np.clip(np.concatenate([c0_proj, c1_proj]), 30.0, 100.0)
X = np.column_stack([X1, X2])
y = np.concatenate([y_c0, y_c1])

df = pd.DataFrame({'Exam_Score': np.round(X1, 1), 'Project_Score': np.round(X2, 1), 'Admitted': y})
print(f"Dataset Shape: {df.shape}")
print(f"Class Balance:\n{df['Admitted'].value_counts()}")

# Stratified 80/20 train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
print(f"Train samples: {len(X_train)} (Class 0: {sum(y_train==0)}, Class 1: {sum(y_train==1)})")
print(f"Test samples:  {len(X_test)} (Class 0: {sum(y_test==0)}, Class 1: {sum(y_test==1)})")

# Hyperparameter selection using 5-Fold CV on Training Data only
candidate_C = [0.01, 0.1, 1.0, 10.0, 100.0]
print("\nEvaluating C values on Train Split via 5-Fold CV (RBF kernel):")
cv_results = {}
for c in candidate_C:
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('svc', SVC(kernel='rbf', C=c, random_state=42))
    ])
    scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring='accuracy')
    cv_results[c] = scores.mean()
    print(f"  C={c:6.2f} -> Mean CV Accuracy: {scores.mean():.4f} (std: {scores.std():.4f})")

best_C = max(cv_results, key=cv_results.get)
print(f"Optimal C selected via CV: {best_C} (CV Accuracy: {cv_results[best_C]:.4f})")

# Fit final pipeline strictly on training data
final_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42))
])
final_pipeline.fit(X_train, y_train)

# Predict on holdout test set
y_pred = final_pipeline.predict(X_test)

test_acc = accuracy_score(y_test, y_pred)
test_prec = precision_score(y_test, y_pred)
test_rec = recall_score(y_test, y_pred)
test_f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

print(f"\nHoldout Test Performance (N = {len(y_test)}):")
print(f"  Accuracy:  {test_acc:.4f} ({test_acc*100:.1f}%)")
print(f"  Precision: {test_prec:.4f} ({test_prec*100:.1f}%)")
print(f"  Recall:    {test_rec:.4f} ({test_rec*100:.1f}%)")
print(f"  F1-Score:  {test_f1:.4f} ({test_f1*100:.1f}%)")
print(f"Confusion Matrix:\n  TN={tn}, FP={fp}\n  FN={fn}, TP={tp}")

# Support vectors analysis
fitted_svc = final_pipeline.named_steps['svc']
n_sv = fitted_svc.support_vectors_.shape[0]
n_sv_per_class = fitted_svc.n_support_
print(f"Total Support Vectors: {n_sv} (Class 0: {n_sv_per_class[0]}, Class 1: {n_sv_per_class[1]}) out of {len(X_train)} training points ({n_sv/len(X_train)*100:.1f}%)")

print("\n=== 3. C PARAMETER COMPARISON (TRAIN SET ONLY) ===")
for c_val in [0.1, 1.0, 10.0]:
    pipe_c = Pipeline([
        ('scaler', StandardScaler()),
        ('svc', SVC(kernel='rbf', C=c_val, random_state=42))
    ])
    pipe_c.fit(X_train, y_train)
    sv_cnt = pipe_c.named_steps['svc'].support_vectors_.shape[0]
    train_score = pipe_c.score(X_train, y_train)
    test_score = pipe_c.score(X_test, y_test)
    print(f"  C={c_val:4.1f} | Support Vectors: {sv_cnt:2d} ({sv_cnt/len(X_train)*100:.1f}%) | Train Acc: {train_score:.4f} | Test Acc: {test_score:.4f}")

print("\n=== 4. KERNEL COMPARISON ON NONLINEAR CONCENTRIC DATASET ===")
X_circ, y_circ = make_circles(n_samples=200, noise=0.10, factor=0.45, random_state=42)
X_c_tr, X_c_te, y_c_tr, y_c_te = train_test_split(X_circ, y_circ, test_size=0.25, random_state=42, stratify=y_circ)

kernels = ['linear', 'poly', 'rbf']
for k in kernels:
    p_k = Pipeline([
        ('scaler', StandardScaler()),
        ('svc', SVC(kernel=k, degree=2 if k=='poly' else 3, C=1.0, random_state=42))
    ])
    p_k.fit(X_c_tr, y_c_tr)
    tr_acc = p_k.score(X_c_tr, y_c_tr)
    te_acc = p_k.score(X_c_te, y_c_te)
    sv_k = p_k.named_steps['svc'].support_vectors_.shape[0]
    print(f"  Kernel: {k:6s} | SV count: {sv_k:3d} | Train Acc: {tr_acc:.4f} | Test Acc: {te_acc:.4f}")

print("\n=== 5. GAMMA COMPARISON (RBF KERNEL) ===")
for g in [0.1, 1.0, 10.0]:
    p_g = Pipeline([
        ('scaler', StandardScaler()),
        ('svc', SVC(kernel='rbf', C=1.0, gamma=g, random_state=42))
    ])
    p_g.fit(X_c_tr, y_c_tr)
    tr_acc = p_g.score(X_c_tr, y_c_tr)
    te_acc = p_g.score(X_c_te, y_c_te)
    sv_g = p_g.named_steps['svc'].support_vectors_.shape[0]
    print(f"  Gamma: {g:4.1f} | SV count: {sv_g:3d} | Train Acc: {tr_acc:.4f} | Test Acc: {te_acc:.4f}")

print("\n=== 6. FEATURE SCALING COMPARISON ===")
# Generate dataset with disparate scales: Feature 1 (Income: $20k - $120k), Feature 2 (Age: 20 - 60)
np.random.seed(42)
income_c0 = np.random.normal(45000, 12000, 100)
age_c0 = np.random.normal(30, 5, 100)
income_c1 = np.random.normal(75000, 12000, 100)
age_c1 = np.random.normal(45, 5, 100)

X_scale = np.vstack([
    np.column_stack([income_c0, age_c0]),
    np.column_stack([income_c1, age_c1])
])
y_scale = np.array([0]*100 + [1]*100)

X_sc_tr, X_sc_te, y_sc_tr, y_sc_te = train_test_split(X_scale, y_scale, test_size=0.25, random_state=42, stratify=y_scale)

# Without scaling
svc_unscaled = SVC(kernel='rbf', C=1.0, random_state=42)
svc_unscaled.fit(X_sc_tr, y_sc_tr)
acc_unscaled = svc_unscaled.score(X_sc_te, y_sc_te)
sv_unscaled = svc_unscaled.support_vectors_.shape[0]

# With scaling
pipe_scaled = Pipeline([('scaler', StandardScaler()), ('svc', SVC(kernel='rbf', C=1.0, random_state=42))])
pipe_scaled.fit(X_sc_tr, y_sc_tr)
acc_scaled = pipe_scaled.score(X_sc_te, y_sc_te)
sv_scaled = pipe_scaled.named_steps['svc'].support_vectors_.shape[0]

print(f"Unscaled SVM: Test Acc = {acc_unscaled:.4f}, Support Vectors = {sv_unscaled}/{len(X_sc_tr)}")
print(f"Scaled SVM:   Test Acc = {acc_scaled:.4f}, Support Vectors = {sv_scaled}/{len(X_sc_tr)}")

print("\n=== 7. SUPPORT VECTOR REGRESSION (SVR) ===")
# Small synthetic 1D regression dataset: Engine Size (L) -> Fuel Efficiency (MPG)
np.random.seed(42)
engine_size = np.sort(np.random.uniform(1.2, 5.0, 80))
# Non-linear relationship + noise
mpg = 42.0 - 5.5 * engine_size + 0.3 * (engine_size**2) + np.random.normal(0, 1.8, 80)
X_svr = engine_size.reshape(-1, 1)
y_svr = mpg

X_svr_tr, X_svr_te, y_svr_tr, y_svr_te = train_test_split(X_svr, y_svr, test_size=0.25, random_state=42)

svr_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svr', SVR(kernel='rbf', C=10.0, epsilon=1.5))
])
svr_pipe.fit(X_svr_tr, y_svr_tr)
y_svr_pred = svr_pipe.predict(X_svr_te)

svr_mae = mean_absolute_error(y_svr_te, y_svr_pred)
svr_rmse = np.sqrt(mean_squared_error(y_svr_te, y_svr_pred))
n_svr_sv = svr_pipe.named_steps['svr'].support_vectors_.shape[0]

print(f"SVR Holdout MAE:  {svr_mae:.2f} MPG")
print(f"SVR Holdout RMSE: {svr_rmse:.2f} MPG")
print(f"SVR Support Vectors: {n_svr_sv}/{len(X_svr_tr)} (Points violating epsilon tube = {n_svr_sv})")

# Predict for a 2.5L engine
pred_2_5 = svr_pipe.predict([[2.5]])[0]
print(f"Predicted Fuel Efficiency for 2.5L engine: {pred_2_5:.2f} MPG")

print("\n=== ALL PYTHON EXPERIMENTS VERIFIED! ===")
