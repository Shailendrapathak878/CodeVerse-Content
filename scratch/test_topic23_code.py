import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, OneHotEncoder, OrdinalEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report

def run_tests():
    print("=" * 60)
    print("TOPIC 23 TECHNICAL VALIDATION: FEATURE ENGINEERING & ML PIPELINES")
    print("=" * 60)

    # 1. Missing Value Imputation: Mean vs Median with Outlier
    data_inc = np.array([35000, 42000, 48000, 52000, 2500000])
    mean_val = np.mean(data_inc)
    median_val = np.median(data_inc)
    print(f"\n1. Missing Value Imputation Demonstration:")
    print(f"   Incomes: {data_inc.tolist()}")
    print(f"   Mean:   ${mean_val:,.2f} (pulled up by outlier)")
    print(f"   Median: ${median_val:,.2f} (robust to outlier)")

    # 2. Categorical Encoding
    cities = np.array([['Tokyo'], ['Paris'], ['New York'], ['London']])
    ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    ohe.fit(cities)
    unseen_city = np.array([['Sydney'], ['Paris']])
    transformed_unseen = ohe.transform(unseen_city)
    print(f"\n2. One-Hot Encoding with handle_unknown='ignore':")
    print(f"   Categories: {ohe.categories_[0].tolist()}")
    print(f"   Transform ['Sydney', 'Paris']:\n{transformed_unseen}")

    # Ordinal Encoding
    edu = np.array([['High School'], ['Bachelor'], ['Master'], ['PhD']])
    oe = OrdinalEncoder(categories=[['High School', 'Bachelor', 'Master', 'PhD']])
    edu_encoded = oe.fit_transform(edu)
    print(f"\n   Ordinal Encoding of Education:")
    for orig, enc in zip(edu.flatten(), edu_encoded.flatten()):
        print(f"     {orig} -> {int(enc)}")

    # 3. Scaling Demonstration
    X_scale_demo = np.array([[10], [20], [30], [40], [100]])
    ss = StandardScaler().fit(X_scale_demo)
    mm = MinMaxScaler().fit(X_scale_demo)
    print(f"\n3. Scaling Demonstration on {X_scale_demo.flatten().tolist()}:")
    print(f"   Mean: {ss.mean_[0]:.2f}, Std: {np.sqrt(ss.var_[0]):.2f}")
    print(f"   Standardized: {ss.transform(X_scale_demo).flatten().round(2).tolist()}")
    print(f"   Min-Max [0, 1]: {mm.transform(X_scale_demo).flatten().round(2).tolist()}")

    # 4. Polynomial Features
    X_poly = np.array([[2, 3], [4, 5]])
    pf = PolynomialFeatures(degree=2, include_bias=False)
    poly_out = pf.fit_transform(X_poly)
    print(f"\n4. Polynomial Features (degree=2) on [x1, x2]:")
    print(f"   Input shape: {X_poly.shape} -> Output shape: {poly_out.shape}")
    print(f"   Feature names: {pf.get_feature_names_out(['x1', 'x2']).tolist()}")
    print(f"   Row [2, 3] transformed: {poly_out[0].tolist()}")

    # 5. Realistic Synthetic Dataset for End-to-End Practical
    np.random.seed(42)
    N = 1000
    
    age = np.random.randint(21, 65, size=N)
    income = np.random.lognormal(mean=10.5, sigma=0.6, size=N).round(-2)
    credit_score = np.random.randint(450, 850, size=N)
    loan_amount = (income * np.random.uniform(0.2, 4.0, size=N)).round(-2)
    tenure_months = np.random.randint(6, 120, size=N)
    
    city = np.random.choice(['New York', 'San Francisco', 'Chicago', 'Austin', 'Seattle'], size=N, p=[0.3, 0.2, 0.2, 0.15, 0.15])
    education = np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], size=N, p=[0.25, 0.45, 0.22, 0.08])
    employment_type = np.random.choice(['Salaried', 'Self-Employed', 'Contract', 'Freelance'], size=N, p=[0.55, 0.25, 0.12, 0.08])
    
    # Days since signup
    days_as_customer = np.random.randint(30, 1800, size=N)
    
    # Ground truth formula for loan approval:
    # High income, high credit score, low debt-to-income ratio, older customer -> Higher approval
    dti = loan_amount / (income + 1e-5)
    z = (
        0.00004 * income 
        + 0.012 * credit_score 
        - 1.2 * dti 
        + 0.04 * age 
        + 0.0008 * days_as_customer 
        + (education == 'PhD') * 0.8
        + (education == 'Master') * 0.4
        + (employment_type == 'Salaried') * 0.5
        - 11.5
    )
    prob = 1 / (1 + np.exp(-z))
    loan_approved = (prob > 0.5).astype(int)
    
    # Inject missing values realistically
    income_missing = income.astype(float)
    income_missing[np.random.choice(N, size=int(N * 0.05), replace=False)] = np.nan
    
    credit_missing = credit_score.astype(float)
    credit_missing[np.random.choice(N, size=int(N * 0.03), replace=False)] = np.nan
    
    employment_missing = employment_type.copy()
    employment_missing[np.random.choice(N, size=int(N * 0.04), replace=False)] = None
    
    df = pd.DataFrame({
        'age': age,
        'income': income_missing,
        'credit_score': credit_missing,
        'loan_amount': loan_amount,
        'tenure_months': tenure_months,
        'days_as_customer': days_as_customer,
        'city': city,
        'education': education,
        'employment_type': employment_missing,
        'loan_approved': loan_approved
    })
    
    print(f"\n5. Synthetic Customer Loan Dataset:")
    print(f"   Total rows: {len(df)}, Features: {df.shape[1]-1}")
    print(f"   Target distribution: Approved={loan_approved.sum()} ({loan_approved.mean():.1%}), Rejected={(1-loan_approved).sum()} ({(1-loan_approved.mean()):.1%})")
    print(f"   Missing values per column:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
    
    # Split BEFORE any preprocessing to prevent leakage
    X = df.drop(columns=['loan_approved'])
    y = df['loan_approved']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
    
    print(f"\n   Train set: {X_train.shape[0]} rows | Test set: {X_test.shape[0]} rows")
    
    # Baseline Model: Raw features with naive median/mode imputation, no feature engineering
    num_cols_raw = ['age', 'income', 'credit_score', 'loan_amount', 'tenure_months', 'days_as_customer']
    cat_cols_raw = ['city', 'education', 'employment_type']
    
    num_transformer_raw = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    cat_transformer_raw = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    preprocessor_raw = ColumnTransformer(transformers=[
        ('num', num_transformer_raw, num_cols_raw),
        ('cat', cat_transformer_raw, cat_cols_raw)
    ])
    
    baseline_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor_raw),
        ('classifier', LogisticRegression(random_state=42, max_iter=1000))
    ])
    
    # Cross-validation on Baseline
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    baseline_cv_scores = cross_val_score(baseline_pipeline, X_train, y_train, cv=cv, scoring='accuracy')
    baseline_pipeline.fit(X_train, y_train)
    baseline_test_preds = baseline_pipeline.predict(X_test)
    baseline_test_acc = accuracy_score(y_test, baseline_test_preds)
    baseline_test_f1 = f1_score(y_test, baseline_test_preds)
    baseline_test_auc = roc_auc_score(y_test, baseline_pipeline.predict_proba(X_test)[:, 1])
    
    print(f"\n6. Baseline Pipeline (Raw Features + LogisticRegression):")
    print(f"   5-Fold CV Accuracy: {baseline_cv_scores.mean():.4f} +/- {baseline_cv_scores.std():.4f}")
    print(f"   Holdout Test Accuracy:  {baseline_test_acc:.4f}")
    print(f"   Holdout Test F1-Score:  {baseline_test_f1:.4f}")
    print(f"   Holdout Test ROC-AUC:   {baseline_test_auc:.4f}")
    
    # Feature Engineering Step:
    # Add domain features:
    # 1. debt_to_income = loan_amount / (income + 1)
    # 2. loan_to_age = loan_amount / age
    # 3. tenure_to_age = tenure_months / (age * 12)
    # 4. log_income = np.log1p(income)
    
    def engineer_features(data):
        df_eng = data.copy()
        df_eng['debt_to_income'] = df_eng['loan_amount'] / (df_eng['income'] + 1.0)
        df_eng['loan_to_age'] = df_eng['loan_amount'] / df_eng['age']
        df_eng['tenure_ratio'] = df_eng['tenure_months'] / (df_eng['age'] * 12.0)
        return df_eng
        
    X_train_eng = engineer_features(X_train)
    X_test_eng = engineer_features(X_test)
    
    num_cols_eng = ['age', 'income', 'credit_score', 'loan_amount', 'tenure_months', 'days_as_customer',
                    'debt_to_income', 'loan_to_age', 'tenure_ratio']
    
    # Advanced Preprocessing Pipeline
    num_transformer_eng = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    preprocessor_eng = ColumnTransformer(transformers=[
        ('num', num_transformer_eng, num_cols_eng),
        ('cat', cat_transformer_raw, cat_cols_raw)
    ])
    
    rf_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor_eng),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    
    rf_cv_scores = cross_val_score(rf_pipeline, X_train_eng, y_train, cv=cv, scoring='accuracy')
    print(f"\n7. Feature-Engineered Random Forest (Default Params):")
    print(f"   5-Fold CV Accuracy: {rf_cv_scores.mean():.4f} +/- {rf_cv_scores.std():.4f}")
    
    # Hyperparameter Tuning INSIDE Pipeline with GridSearchCV
    param_grid = {
        'preprocessor__num__imputer__strategy': ['mean', 'median'],
        'classifier__n_estimators': [50, 100],
        'classifier__max_depth': [5, 8, 12],
        'classifier__min_samples_leaf': [2, 4]
    }
    
    grid_search = GridSearchCV(
        rf_pipeline,
        param_grid=param_grid,
        cv=cv,
        scoring='roc_auc',
        n_jobs=-1
    )
    
    grid_search.fit(X_train_eng, y_train)
    best_pipe = grid_search.best_estimator_
    
    print(f"\n8. Hyperparameter Tuning Inside Pipeline (GridSearchCV):")
    print(f"   Total parameter combinations: {len(grid_search.cv_results_['params'])}")
    print(f"   Best Parameters: {grid_search.best_params_}")
    print(f"   Best 5-Fold CV ROC-AUC: {grid_search.best_score_:.4f}")
    
    # Evaluate on Holdout Test Set
    test_preds = best_pipe.predict(X_test_eng)
    test_probs = best_pipe.predict_proba(X_test_eng)[:, 1]
    
    final_acc = accuracy_score(y_test, test_preds)
    final_prec = precision_score(y_test, test_preds)
    final_rec = recall_score(y_test, test_preds)
    final_f1 = f1_score(y_test, test_preds)
    final_auc = roc_auc_score(y_test, test_probs)
    
    print(f"\n9. Final Holdout Test Set Evaluation (Tuned Feature-Engineered Pipeline):")
    print(f"   Accuracy:  {final_acc:.4f} (Baseline: {baseline_test_acc:.4f}) -> Delta: {final_acc - baseline_test_acc:+.4f}")
    print(f"   Precision: {final_prec:.4f}")
    print(f"   Recall:    {final_rec:.4f}")
    print(f"   F1-Score:  {final_f1:.4f} (Baseline: {baseline_test_f1:.4f}) -> Delta: {final_f1 - baseline_test_f1:+.4f}")
    print(f"   ROC-AUC:   {final_auc:.4f} (Baseline: {baseline_test_auc:.4f}) -> Delta: {final_auc - baseline_test_auc:+.4f}")
    
    # 10. Feature Selection with SelectKBest inside Pipeline
    select_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor_eng),
        ('selector', SelectKBest(score_func=f_classif, k=10)),
        ('classifier', LogisticRegression(random_state=42, max_iter=1000))
    ])
    select_cv = cross_val_score(select_pipeline, X_train_eng, y_train, cv=cv, scoring='accuracy')
    print(f"\n10. Pipeline with Feature Selection (SelectKBest k=10 + LogisticRegression):")
    print(f"    5-Fold CV Accuracy: {select_cv.mean():.4f} +/- {select_cv.std():.4f}")

if __name__ == '__main__':
    run_tests()
