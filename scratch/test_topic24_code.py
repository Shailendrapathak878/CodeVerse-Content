import os
import time
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

def run_tests():
    print("=" * 60)
    print("TOPIC 24 TECHNICAL VALIDATION: MODEL DEPLOYMENT & MLOPS")
    print("=" * 60)

    # 1. Reproducible Dataset: Customer Retention / Churn (N=1,000)
    np.random.seed(42)
    N = 1000
    tenure_months = np.random.randint(1, 72, size=N)
    monthly_charges = np.random.uniform(20.0, 120.0, size=N).round(2)
    total_charges = (tenure_months * monthly_charges * np.random.uniform(0.9, 1.1, size=N)).round(2)
    contract_type = np.random.choice(['Month-to-month', 'One year', 'Two year'], size=N, p=[0.55, 0.25, 0.20])
    has_tech_support = np.random.choice([0, 1], size=N, p=[0.65, 0.35])

    # Ground truth churn logic: high monthly charges, month-to-month contract, low tenure -> higher churn
    contract_factor = np.where(contract_type == 'Month-to-month', 1.8, np.where(contract_type == 'One year', 0.6, 0.2))
    logits = (0.03 * monthly_charges - 0.05 * tenure_months + 1.2 * contract_factor - 0.8 * has_tech_support - 1.5)
    churn_prob = 1 / (1 + np.exp(-logits))
    churned = (churn_prob > 0.5).astype(int)

    df = pd.DataFrame({
        'tenure_months': tenure_months,
        'monthly_charges': monthly_charges,
        'total_charges': total_charges,
        'contract_type': contract_type,
        'has_tech_support': has_tech_support,
        'churn': churned
    })

    print(f"\n1. Dataset Loaded: {len(df)} rows, Churn rate: {churned.mean():.1%}")

    # 2. Train / Test Split
    X = df.drop(columns=['churn'])
    y = df['churn']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
    print(f"   Train split: {len(X_train)} rows | Test split: {len(X_test)} rows")

    # 3. Assemble Full Preprocessing & Model Pipeline
    num_cols = ['tenure_months', 'monthly_charges', 'total_charges', 'has_tech_support']
    cat_cols = ['contract_type']

    preprocessor = ColumnTransformer(transformers=[
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
    ])

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42))
    ])

    # 4. Train and Evaluate
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    y_prob = pipeline.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)

    print("\n2. Model Evaluation on Holdout Test Set:")
    print(f"   Accuracy:  {acc:.4f} ({acc*100:.1f}%)")
    print(f"   Precision: {prec:.4f}")
    print(f"   Recall:    {rec:.4f}")
    print(f"   F1-Score:  {f1:.4f}")
    print(f"   ROC-AUC:   {auc:.4f}")

    # 5. Model Serialization with Joblib
    artifact_path = os.path.join("scratch", "customer_churn_pipeline.joblib")
    joblib.dump(pipeline, artifact_path)
    file_size_kb = os.path.getsize(artifact_path) / 1024
    print(f"\n3. Model Artifact Serialized to: {artifact_path} ({file_size_kb:.1f} KB)")

    # 6. Model Deserialization & Parity Check
    loaded_pipeline = joblib.load(artifact_path)
    reloaded_preds = loaded_pipeline.predict(X_test)
    assert np.array_equal(y_pred, reloaded_preds), "Reloaded model predictions mismatch!"
    print("   Parity check PASSED: Loaded artifact produces 100% identical predictions.")

    # 7. FastAPI Application Definition
    app = FastAPI(
        title="Customer Churn Prediction Service",
        description="Production prediction API demonstrating leak-free inference",
        version="1.0.0"
    )

    class CustomerFeatures(BaseModel):
        tenure_months: int = Field(..., ge=0, le=120, description="Customer tenure in months")
        monthly_charges: float = Field(..., gt=0.0, le=500.0, description="Monthly recurring bill in USD")
        total_charges: float = Field(..., ge=0.0, description="Cumulative charges in USD")
        contract_type: str = Field(..., description="Contract duration: 'Month-to-month', 'One year', 'Two year'")
        has_tech_support: int = Field(..., ge=0, le=1, description="Binary flag: 1 if active, 0 otherwise")

        class Config:
            json_schema_extra = {
                "example": {
                    "tenure_months": 12,
                    "monthly_charges": 75.50,
                    "total_charges": 906.00,
                    "contract_type": "Month-to-month",
                    "has_tech_support": 0
                }
            }

    @app.get("/health")
    def health_check():
        return {
            "status": "healthy",
            "service": "customer-churn-api",
            "model_version": "1.0.0",
            "pipeline_loaded": True
        }

    @app.post("/predict")
    def predict_churn(customer: CustomerFeatures):
        start_t = time.perf_counter()
        
        # Convert schema to pandas DataFrame with identical columns
        input_df = pd.DataFrame([{
            'tenure_months': customer.tenure_months,
            'monthly_charges': customer.monthly_charges,
            'total_charges': customer.total_charges,
            'contract_type': customer.contract_type,
            'has_tech_support': customer.has_tech_support
        }])
        
        # Prediction via pipeline
        pred = int(loaded_pipeline.predict(input_df)[0])
        prob = float(loaded_pipeline.predict_proba(input_df)[0, 1])
        latency_ms = round((time.perf_counter() - start_t) * 1000, 2)
        
        return {
            "prediction": pred,
            "prediction_label": "Churn" if pred == 1 else "Retained",
            "churn_probability": round(prob, 4),
            "risk_tier": "High" if prob >= 0.7 else "Medium" if prob >= 0.4 else "Low",
            "model_version": "1.0.0",
            "inference_latency_ms": latency_ms
        }

    # 8. Automated API Tests via TestClient
    client = TestClient(app)

    # Test 1: Health check
    res_health = client.get("/health")
    print(f"\n4. FastAPI /health Endpoint Test:")
    print(f"   Status Code: {res_health.status_code}")
    print(f"   Response: {res_health.json()}")
    assert res_health.status_code == 200

    # Test 2: Valid High-Risk Customer Prediction
    valid_payload = {
        "tenure_months": 3,
        "monthly_charges": 95.0,
        "total_charges": 285.0,
        "contract_type": "Month-to-month",
        "has_tech_support": 0
    }
    res_pred = client.post("/predict", json=valid_payload)
    print(f"\n5. FastAPI /predict Endpoint Test (High Risk):")
    print(f"   Status Code: {res_pred.status_code}")
    print(f"   Response: {res_pred.json()}")
    assert res_pred.status_code == 200
    assert "churn_probability" in res_pred.json()

    # Test 3: Valid Loyal Low-Risk Customer Prediction
    loyal_payload = {
        "tenure_months": 48,
        "monthly_charges": 45.0,
        "total_charges": 2160.0,
        "contract_type": "Two year",
        "has_tech_support": 1
    }
    res_loyal = client.post("/predict", json=loyal_payload)
    print(f"\n6. FastAPI /predict Endpoint Test (Low Risk Loyal):")
    print(f"   Status Code: {res_loyal.status_code}")
    print(f"   Response: {res_loyal.json()}")
    assert res_loyal.status_code == 200

    # Test 4: Invalid Payload (tenure_months negative, monthly_charges > 500)
    invalid_payload = {
        "tenure_months": -5,
        "monthly_charges": 999.0,
        "total_charges": 100.0,
        "contract_type": "Month-to-month",
        "has_tech_support": 0
    }
    res_invalid = client.post("/predict", json=invalid_payload)
    print(f"\n7. FastAPI Input Validation Rejection Test (Negative Tenure & Out of range):")
    print(f"   Status Code: {res_invalid.status_code} (Expected 422 Unprocessable Entity)")
    assert res_invalid.status_code == 422
    print("   Input validation test PASSED: Invalid requests cleanly blocked by Pydantic.")

    # 9. Latency Benchmark (100 Requests)
    latencies = []
    for _ in range(100):
        t0 = time.perf_counter()
        client.post("/predict", json=valid_payload)
        latencies.append((time.perf_counter() - t0) * 1000)

    p50 = np.percentile(latencies, 50)
    p95 = np.percentile(latencies, 95)
    p99 = np.percentile(latencies, 99)
    print(f"\n8. Inference Latency Benchmark (100 Requests):")
    print(f"   Mean: {np.mean(latencies):.2f} ms")
    print(f"   P50:  {p50:.2f} ms")
    print(f"   P95:  {p95:.2f} ms")
    print(f"   P99:  {p99:.2f} ms")

if __name__ == '__main__':
    run_tests()
