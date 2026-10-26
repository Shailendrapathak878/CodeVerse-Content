# Topic 21 Python Verification Script
# Generates reproducible synthetic data, fits Polynomial, Ridge, Lasso, ElasticNet,
# computes exact MSE, R2, coefficients, learning curve, and validation curve values.

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, RidgeCV, LassoCV
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve, validation_curve, KFold
from sklearn.metrics import mean_squared_error, r2_score

# 1. Generate Synthetic Dataset: True function f(x) = cos(1.5 * pi * x) + noise
np.random.seed(42)
n_samples = 40
X = np.sort(np.random.uniform(0, 1, n_samples))
true_fun = lambda x: np.cos(1.5 * np.pi * x)
y = true_fun(X) + np.random.normal(0, 0.15, n_samples)

X_2d = X.reshape(-1, 1)

# Split 80% train, 20% holdout test
X_train, X_test, y_train, y_test = train_test_split(
    X_2d, y, test_size=0.25, random_state=42
)
# N_train = 30, N_test = 10
# Sort train for nice plotting if needed
sort_idx = np.argsort(X_train.ravel())
X_train_sorted = X_train[sort_idx]
y_train_sorted = y_train[sort_idx]

print(f"Total samples: {n_samples}, Train: {len(X_train)}, Test: {len(X_test)}")

# 2. Fit Polynomial Models: Degree 1, Degree 3, Degree 10
degrees = [1, 3, 10]
poly_results = {}

for deg in degrees:
    pipe = Pipeline([
        ('poly', PolynomialFeatures(degree=deg, include_bias=False)),
        ('linear', LinearRegression())
    ])
    pipe.fit(X_train, y_train)
    
    train_pred = pipe.predict(X_train)
    test_pred = pipe.predict(X_test)
    
    train_mse = mean_squared_error(y_train, train_pred)
    test_mse = mean_squared_error(y_test, test_pred)
    train_r2 = r2_score(y_train, train_pred)
    test_r2 = r2_score(y_test, test_pred)
    
    # 5-fold CV MSE on training set
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = -cross_val_score(pipe, X_train, y_train, cv=kf, scoring='neg_mean_squared_error')
    cv_mse_mean = np.mean(cv_scores)
    cv_mse_std = np.std(cv_scores)
    
    poly_results[deg] = {
        'train_mse': train_mse,
        'test_mse': test_mse,
        'train_r2': train_r2,
        'test_r2': test_r2,
        'cv_mse_mean': cv_mse_mean,
        'cv_mse_std': cv_mse_std,
        'coeffs': pipe.named_steps['linear'].coef_,
        'intercept': pipe.named_steps['linear'].intercept_
    }
    
    print(f"--- Degree {deg} ---")
    print(f"  Train MSE: {train_mse:.4f}, Test MSE: {test_mse:.4f}")
    print(f"  Train R2:  {train_r2:.4f}, Test R2:  {test_r2:.4f}")
    print(f"  5-Fold CV MSE: {cv_mse_mean:.4f} +/- {cv_mse_std:.4f}")
    print(f"  Coeff max abs: {np.max(np.abs(pipe.named_steps['linear'].coef_)):.2f}")

# 3. Regularization on Degree 10 Polynomial
# Compare: Unregularized OLS, Ridge (alpha=0.1), Lasso (alpha=0.01), ElasticNet (alpha=0.01, l1_ratio=0.5)
reg_models = {
    'Unregularized OLS': LinearRegression(),
    'Ridge (L2, alpha=0.1)': Ridge(alpha=0.1, random_state=42),
    'Lasso (L1, alpha=0.01)': Lasso(alpha=0.01, random_state=42, max_iter=10000),
    'Elastic Net (alpha=0.01)': ElasticNet(alpha=0.01, l1_ratio=0.5, random_state=42, max_iter=10000)
}

reg_results = {}
for name, model in reg_models.items():
    pipe = Pipeline([
        ('poly', PolynomialFeatures(degree=10, include_bias=False)),
        ('scaler', StandardScaler()),
        ('model', model)
    ])
    pipe.fit(X_train, y_train)
    
    train_pred = pipe.predict(X_train)
    test_pred = pipe.predict(X_test)
    
    train_mse = mean_squared_error(y_train, train_pred)
    test_mse = mean_squared_error(y_test, test_pred)
    
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = -cross_val_score(pipe, X_train, y_train, cv=kf, scoring='neg_mean_squared_error')
    cv_mse_mean = np.mean(cv_scores)
    
    coeffs = pipe.named_steps['model'].coef_
    zeros = np.sum(np.isclose(coeffs, 0.0, atol=1e-3))
    
    reg_results[name] = {
        'train_mse': train_mse,
        'test_mse': test_mse,
        'cv_mse_mean': cv_mse_mean,
        'coeffs': coeffs,
        'zero_count': zeros
    }
    print(f"\\n--- {name} ---")
    print(f"  Train MSE: {train_mse:.4f}, Test MSE: {test_mse:.4f}, CV MSE: {cv_mse_mean:.4f}")
    print(f"  Zero coeffs count: {zeros}/10")
    print(f"  Coefficients: {np.round(coeffs, 3)}")

# 4. Regularization Strength Sweep (Alpha Tuning for Ridge)
alphas = np.logspace(-4, 3, 8)
train_scores, val_scores = validation_curve(
    Pipeline([
        ('poly', PolynomialFeatures(degree=10, include_bias=False)),
        ('scaler', StandardScaler()),
        ('ridge', Ridge(random_state=42))
    ]),
    X_train, y_train,
    param_name='ridge__alpha',
    param_range=alphas,
    cv=5,
    scoring='neg_mean_squared_error'
)
train_mse_sweep = -np.mean(train_scores, axis=1)
val_mse_sweep = -np.mean(val_scores, axis=1)

print("\\n--- Ridge Alpha Sweep ---")
for a, tr_m, val_m in zip(alphas, train_mse_sweep, val_mse_sweep):
    print(f"  Alpha {a:8.4f}: Train MSE = {tr_m:.4f}, Val MSE = {val_m:.4f}")

best_alpha_idx = np.argmin(val_mse_sweep)
print(f"Optimal Alpha: {alphas[best_alpha_idx]:.4f} with min Val MSE = {val_mse_sweep[best_alpha_idx]:.4f}")

# 5. Learning Curve for Good Fit (Degree 3) vs Overfit (Degree 10 OLS)
train_sizes, tr_sc_g, val_sc_g = learning_curve(
    Pipeline([
        ('poly', PolynomialFeatures(degree=3, include_bias=False)),
        ('linear', LinearRegression())
    ]),
    X_train, y_train,
    train_sizes=np.linspace(0.2, 1.0, 5),
    cv=5,
    scoring='neg_mean_squared_error'
)
print("\\n--- Learning Curve Degree 3 (Good Fit) ---")
for sz, tr, val in zip(train_sizes, -np.mean(tr_sc_g, axis=1), -np.mean(val_sc_g, axis=1)):
    print(f"  Train Size {sz:2d}: Train MSE = {tr:.4f}, Val MSE = {val:.4f}, Gap = {val - tr:.4f}")
