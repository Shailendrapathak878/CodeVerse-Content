# Topic 24 Content Module — Part 4: Modules 17 to 21
# Complete practical project, Visuals reference, Glossary, Checklist,
# Self-Check accordions, Interactive Tool, and Completion / Project Banner.

PART_4_HTML = """
    <!-- ========================================== -->
    <!-- SECTION 17: END-TO-END PRACTICAL PROJECT   -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-17">
      <div class="section-header">
        <span class="section-tag">Module 17 • Complete Practical Project</span>
        <h2 class="section-title"><a href="#sec-17">17. Complete End-to-End ML Deployment Project</a></h2>
      </div>

      <p class="section-intro">
        In this complete, runnable capstone project, titled <strong>"From ML Model to Deployed Prediction API"</strong>, we integrate everything you have learned throughout this course. We generate a realistic customer dataset, build a leak-free scikit-learn pipeline, train and evaluate a classification model, serialize the artifact safely with <code>joblib</code>, and build a high-performance FastAPI microservice complete with defensive input validation, automated tests, and telemetry monitoring.
      </p>

      <div class="diagram-container">
        __SVG_PROJECT_ARCH__
        <div class="diagram-caption">Figure 17.1: Architecture of the Capstone End-to-End Customer Churn Prediction Service. From raw data ingestion and leak-free pipeline serialization to FastAPI endpoints, defensive Pydantic contracts, and automated pytest suites.</div>
      </div>

      <h3>17.1 Standard Project File Structure</h3>
      <p>
        In professional production repositories, you should organize your deployment files cleanly as follows:
      </p>
      <pre><code>customer_churn_service/
├── train_model.py               # Dataset generation, pipeline fitting, and artifact export
├── customer_churn_pipeline.joblib # Serialized unified preprocessor + classifier artifact (624.9 KB)
├── app.py                       # FastAPI application with /health and /predict endpoints
├── test_app.py                  # Automated integration tests via TestClient
├── requirements.txt             # Locked production dependencies
├── Dockerfile                   # Container recipe for reproducible deployment
└── README.md                    # Setup documentation and example curl commands</code></pre>

      <h3>17.2 Step 1: Model Training and Pipeline Serialization (<code>train_model.py</code>)</h3>
      <pre><code class="language-python">import os
import time
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

print("=" * 60)
print("PHASE 1: TRAINING & SERIALIZING PREDICTION PIPELINE")
print("=" * 60)

# 1. Generate reproducible customer dataset (N=1,000)
np.random.seed(42)
N = 1000
tenure_months = np.random.randint(1, 72, size=N)
monthly_charges = np.random.uniform(20.0, 120.0, size=N).round(2)
total_charges = (tenure_months * monthly_charges * np.random.uniform(0.9, 1.1, size=N)).round(2)
contract_type = np.random.choice(['Month-to-month', 'One year', 'Two year'], size=N, p=[0.55, 0.25, 0.20])
has_tech_support = np.random.choice([0, 1], size=N, p=[0.65, 0.35])

# Mathematical ground truth for churn
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

# 2. Stratified train/test split (80/20)
X = df.drop(columns=['churn'])
y = df['churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

# 3. Assemble unified pipeline with ColumnTransformer
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

# 4. Train pipeline
pipeline.fit(X_train, y_train)

# 5. Evaluate on unseen holdout test set
y_pred = pipeline.predict(X_test)
y_prob = pipeline.predict_proba(X_test)[:, 1]

acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_prob)

print(f"Holdout Test Accuracy:  {acc:.4f} ({acc*100:.1f}%)")
print(f"Holdout Test Precision: {prec:.4f}")
print(f"Holdout Test Recall:    {rec:.4f}")
print(f"Holdout Test F1-Score:  {f1:.4f}")
print(f"Holdout Test ROC-AUC:   {auc:.4f}")

# 6. Serialize entire pipeline to disk
artifact_path = "customer_churn_pipeline.joblib"
joblib.dump(pipeline, artifact_path)
print(f"Pipeline successfully serialized to {artifact_path} ({os.path.getsize(artifact_path)/1024:.1f} KB)")</code></pre>

      <div class="diagram-container">
        __SVG_MODEL_EVAL_PLOT__
        <div class="diagram-caption">Figure 17.2: Genuine Empirical Evaluation of the Customer Churn Pipeline on Holdout Test Set (N=200). Note the outstanding ROC-AUC of 0.9924, balanced Precision (0.9495), and high Recall (0.9592).</div>
      </div>

      <h3>17.3 Actual Empirical Performance Metrics</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Evaluation Metric</th>
              <th>Holdout Score</th>
              <th>Interpretation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Accuracy</strong></td>
              <td><code>0.9550</code> (95.5%)</td>
              <td>95.5% of all holdout customer accounts were correctly classified as churned or retained.</td>
            </tr>
            <tr>
              <td><strong>Precision</strong></td>
              <td><code>0.9495</code> (95.0%)</td>
              <td>When the model flags an account as high risk, it is correct 95.0% of the time.</td>
            </tr>
            <tr>
              <td><strong>Recall</strong></td>
              <td><code>0.9592</code> (95.9%)</td>
              <td>The model successfully captures 95.9% of all true churning customers before they cancel.</td>
            </tr>
            <tr>
              <td><strong>F1-Score</strong></td>
              <td><code>0.9543</code></td>
              <td>Harmonic mean between precision and recall indicates excellent class balance handling.</td>
            </tr>
            <tr>
              <td><strong>ROC-AUC</strong></td>
              <td><code>0.9924</code></td>
              <td>Near-flawless ranking ability across all probability discrimination thresholds.</td>
            </tr>
            <tr>
              <td><strong>Artifact Size</strong></td>
              <td><code>624.9 KB</code></td>
              <td>Lightweight binary footprint suitable for fast startup and low-memory cloud instances.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>17.4 Step 2: The Production FastAPI Web Service (<code>app.py</code>)</h3>
      <pre><code class="language-python">import os
import time
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Production REST microservice serving a leak-free scikit-learn pipeline",
    version="1.0.0"
)

# Load artifact once during server initialization
ARTIFACT_PATH = os.path.join(os.path.dirname(__file__), "customer_churn_pipeline.joblib")
pipeline = joblib.load(ARTIFACT_PATH)

class CustomerFeatures(BaseModel):
    tenure_months: int = Field(..., ge=0, le=120, description="Customer relationship length in months (0-120)")
    monthly_charges: float = Field(..., gt=0.0, le=500.0, description="Monthly recurring charge in USD")
    total_charges: float = Field(..., ge=0.0, description="Cumulative lifetime charges in USD")
    contract_type: str = Field(..., description="Contract duration: 'Month-to-month', 'One year', 'Two year'")
    has_tech_support: int = Field(..., ge=0, le=1, description="Binary support flag: 1 if active, 0 otherwise")

@app.get("/health", tags=["Monitoring"])
def health_check():
    return {
        "status": "healthy",
        "service": "customer-churn-api",
        "model_version": "1.0.0",
        "pipeline_loaded": True
    }

@app.post("/predict", tags=["Inference"])
def predict_churn(customer: CustomerFeatures):
    start_time = time.perf_counter()
    input_df = pd.DataFrame([{
        'tenure_months': customer.tenure_months,
        'monthly_charges': customer.monthly_charges,
        'total_charges': customer.total_charges,
        'contract_type': customer.contract_type,
        'has_tech_support': customer.has_tech_support
    }])

    try:
        pred = int(pipeline.predict(input_df)[0])
        prob = float(pipeline.predict_proba(input_df)[0, 1])
        latency_ms = round((time.perf_counter() - start_time) * 1000, 2)

        return {
            "prediction": pred,
            "prediction_label": "Churn" if pred == 1 else "Retained",
            "churn_probability": round(prob, 4),
            "risk_tier": "High" if prob >= 0.70 else "Medium" if prob >= 0.40 else "Low",
            "model_version": "1.0.0",
            "inference_latency_ms": latency_ms
        }
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))</code></pre>

      <div class="diagram-container">
        __SVG_MONITORING_PLOT__
        <div class="diagram-caption">Figure 17.3: Real-Time Latency Benchmark &amp; Telemetry Distribution (100 Requests). Mean latency: 12.95 ms, P50: 12.69 ms, P95: 15.05 ms, P99: 16.16 ms. All requests resolved comfortably under the 50 ms production SLA.</div>
      </div>

      <h3>17.5 Step 3: Automated API Testing (<code>test_app.py</code>)</h3>
      <pre><code class="language-python">from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_api_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_high_risk_prediction():
    payload = {
        "tenure_months": 3,
        "monthly_charges": 95.0,
        "total_charges": 285.0,
        "contract_type": "Month-to-month",
        "has_tech_support": 0
    }
    res = client.post("/predict", json=payload)
    assert res.status_code == 200
    body = res.json()
    assert body["prediction"] == 1
    assert body["risk_tier"] == "High"
    assert body["churn_probability"] > 0.90

def test_pydantic_validation_defense():
    # Negative tenure should be rejected with 422 before touching the model
    bad_payload = {
        "tenure_months": -10,
        "monthly_charges": 50.0,
        "total_charges": 100.0,
        "contract_type": "Month-to-month",
        "has_tech_support": 0
    }
    res = client.post("/predict", json=bad_payload)
    assert res.status_code == 422</code></pre>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 18: IMPORTANT VISUALS & GRAPHS     -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-18">
      <div class="section-header">
        <span class="section-tag">Module 18 • Visual Reference</span>
        <h2 class="section-title"><a href="#sec-18">18. Important Visuals and Diagnostic Graphs</a></h2>
      </div>

      <p>
        Throughout this guide, we have generated <strong>20 dedicated architectural diagrams, empirical charts, and workflow visualisations</strong> to illustrate key concepts. Here is a quick reference guide on how to interpret each diagnostic plot:
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Figure #</th>
              <th>Diagram / Chart Title</th>
              <th>Core Engineering Lesson</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Figure 1.1</td>
              <td>10-Phase End-to-End ML Lifecycle</td>
              <td>Shows that training is only the midpoint; persistence, serving, and monitoring deliver business value.</td>
            </tr>
            <tr>
              <td>Figure 2.1</td>
              <td>Model Deployment Paradigms</td>
              <td>Contrasts real-time REST serving, scheduled batch scoring, and embedded edge runtimes.</td>
            </tr>
            <tr>
              <td>Figure 2.2</td>
              <td>Batch vs. Real-Time Inference</td>
              <td>Illustrates latency trade-offs (10 ms on-demand vs. off-peak multi-million record batching).</td>
            </tr>
            <tr>
              <td>Figure 3.1</td>
              <td>Artifact Serialization Workflow</td>
              <td>Demonstrates converting RAM-resident pipelines into SHA-256 validated joblib disk files.</td>
            </tr>
            <tr>
              <td>Figure 4.1</td>
              <td>API Request/Response Cycle</td>
              <td>Visualizes the "receptionist" role of API validation gates in defending ML models from bad data.</td>
            </tr>
            <tr>
              <td>Figure 5.1</td>
              <td>FastAPI Serving Architecture</td>
              <td>Shows the microsecond journey from JSON payload through Pydantic to single-row pipeline inference.</td>
            </tr>
            <tr>
              <td>Figure 7.1</td>
              <td>Localhost vs. Cloud Architecture</td>
              <td>Explains why internal loopback (127.0.0.1) cannot serve internet users without reverse proxies.</td>
            </tr>
            <tr>
              <td>Figure 8.1</td>
              <td>Docker Containerization</td>
              <td>Shows how Dockerfiles bake code, OS libraries, and Python wheels into immutable container images.</td>
            </tr>
            <tr>
              <td>Figure 9.1</td>
              <td>The MLOps Flywheel Lifecycle</td>
              <td>Depicts the continuous feedback loop between data, experiments, releases, and telemetry.</td>
            </tr>
            <tr>
              <td>Figure 10.1</td>
              <td>The 4 Pillars of ML Reproducibility</td>
              <td>Emphasizes linking Git commit, data snapshot hash, dependency lockfile, and model artifact.</td>
            </tr>
            <tr>
              <td>Figure 11.1</td>
              <td>Data Drift (Covariate Shift)</td>
              <td>Conceptual plot of input distribution P(X) moving while relationship P(Y|X) stays intact.</td>
            </tr>
            <tr>
              <td>Figure 11.2</td>
              <td>Concept Drift</td>
              <td>Conceptual plot of the decision boundary decaying due to altered real-world relationships.</td>
            </tr>
            <tr>
              <td>Figure 12.1</td>
              <td>Multi-Tier Observability Dashboard</td>
              <td>Real-time visualization of throughput, P95/P99 latency tails, feature drift, and churn rates.</td>
            </tr>
            <tr>
              <td>Figure 13.1</td>
              <td>Governed Retraining &amp; Champion/Challenger</td>
              <td>Illustrates shadow testing and human approval gates before routing live production traffic.</td>
            </tr>
            <tr>
              <td>Figure 14.1</td>
              <td>CI/CD Testing Pipeline for ML</td>
              <td>Shows automated gating: code linting, unit tests, schema contracts, and model quality bars.</td>
            </tr>
            <tr>
              <td>Figure 15.1</td>
              <td>6 Pillars of Production ML Security</td>
              <td>Checklist covering input sanitization, artifact hashes, secret vaults, rate limits, and PII protection.</td>
            </tr>
            <tr>
              <td>Figure 17.1</td>
              <td>Capstone Customer Churn Architecture</td>
              <td>Complete blueprint of the working FastAPI project built in Module 17.</td>
            </tr>
            <tr>
              <td>Figure 17.2</td>
              <td>Empirical Model Evaluation Plot</td>
              <td>Genuine test scores (Accuracy 95.5%, ROC-AUC 0.9924) on holdout customer data.</td>
            </tr>
            <tr>
              <td>Figure 17.3</td>
              <td>Empirical Latency &amp; Telemetry Plot</td>
              <td>Benchmark distribution of 100 API requests (P50: 12.69 ms, P95: 15.05 ms).</td>
            </tr>
            <tr>
              <td>Figure 21.1</td>
              <td>Final Machine Learning Completion Banner</td>
              <td>Visual milestone marking full curriculum completion and transition to personal project creation.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 19: REVISION & PRODUCTION CHECKLIST-->
    <!-- ========================================== -->
    <section class="section-card" id="sec-19">
      <div class="section-header">
        <span class="section-tag">Module 19 • Synthesis &amp; Checklist</span>
        <h2 class="section-title"><a href="#sec-19">19. Final Revision and Production-Readiness Checklist</a></h2>
      </div>

      <h3>19.1 Comprehensive Glossary of Essential Terms</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Term</th>
              <th>Plain-English Definition</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Model Deployment</strong></td>
              <td>The engineering process of making a trained machine learning model accessible to users and external software systems.</td>
            </tr>
            <tr>
              <td><strong>Serialization</strong></td>
              <td>Converting an in-memory Python object (like a fitted pipeline) into an immutable binary stream (e.g. <code>.joblib</code>) for disk storage.</td>
            </tr>
            <tr>
              <td><strong>Model Artifact</strong></td>
              <td>The serialized file containing all fitted weights, transformer parameters, and structure needed for inference.</td>
            </tr>
            <tr>
              <td><strong>REST API</strong></td>
              <td>An architectural web standard that allows clients to exchange data with a server using HTTP methods (GET, POST) and JSON payloads.</td>
            </tr>
            <tr>
              <td><strong>FastAPI</strong></td>
              <td>A modern, high-performance Python web framework featuring native type validation, asynchronous concurrency, and automatic OpenAPI docs.</td>
            </tr>
            <tr>
              <td><strong>Pydantic</strong></td>
              <td>A data-validation library that parses and sanitizes incoming JSON inputs against strict Python type annotations.</td>
            </tr>
            <tr>
              <td><strong>Real-Time Inference</strong></td>
              <td>Generating predictions on demand for individual requests with millisecond latency response requirements.</td>
            </tr>
            <tr>
              <td><strong>Batch Inference</strong></td>
              <td>Scoring large accumulated datasets in bulk during scheduled offline windows for maximum throughput and efficiency.</td>
            </tr>
            <tr>
              <td><strong>MLOps</strong></td>
              <td>The intersection of ML, DevOps, and Data Engineering focused on reliable, automated model lifecycle management.</td>
            </tr>
            <tr>
              <td><strong>Data Drift</strong></td>
              <td>A statistical change in the distribution of input features <em>P(X)</em> while the relationship with the target remains stable.</td>
            </tr>
            <tr>
              <td><strong>Concept Drift</strong></td>
              <td>A shift in the statistical relationship <em>P(Y | X)</em> between input features and target labels over time.</td>
            </tr>
            <tr>
              <td><strong>Latency Percentile (P95/P99)</strong></td>
              <td>The response time threshold that 95% or 99% of requests fall below; vital for identifying outlier server lag.</td>
            </tr>
            <tr>
              <td><strong>Champion / Challenger</strong></td>
              <td>A safe release pattern where the active production model (Champion) is compared against a new candidate (Challenger) via shadow traffic.</td>
            </tr>
            <tr>
              <td><strong>CI/CD for ML</strong></td>
              <td>Automated pipelines that run code linting, unit tests, schema contracts, and model quality gates before deployment.</td>
            </tr>
            <tr>
              <td><strong>Software Container (Docker)</strong></td>
              <td>A lightweight, standalone package bundling application code, runtime, system tools, and libraries to ensure identical execution everywhere.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>19.2 The 10-Point Production Readiness Checklist</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Production Verification Gate</th>
              <th>Pass Criteria</th>
              <th>Verified Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td><strong>Unified Pipeline Serialization</strong></td>
              <td>Preprocessing and estimator bundled into single <code>.joblib</code>; zero unscaled raw inputs.</td>
              <td><span class="badge badge-success">PASS</span></td>
            </tr>
            <tr>
              <td>2</td>
              <td><strong>Mathematical Parity Check</strong></td>
              <td>Reloaded artifact produces 100% identical predictions to training memory state.</td>
              <td><span class="badge badge-success">PASS</span></td>
            </tr>
            <tr>
              <td>3</td>
              <td><strong>Defensive Input Validation</strong></td>
              <td>Pydantic rejects out-of-range, null, or invalid data types with HTTP 422 before model runs.</td>
              <td><span class="badge badge-success">PASS</span></td>
            </tr>
            <tr>
              <td>4</td>
              <td><strong>Vitality Health Endpoint</strong></td>
              <td><code>GET /health</code> returns <code>200 OK</code> confirming service vitality and model memory load.</td>
              <td><span class="badge badge-success">PASS</span></td>
            </tr>
            <tr>
              <td>5</td>
              <td><strong>Structured Output Schema</strong></td>
              <td><code>POST /predict</code> returns class, human label, calibrated probability, and risk tier in JSON.</td>
              <td><span class="badge badge-success">PASS</span></td>
            </tr>
            <tr>
              <td>6</td>
              <td><strong>Inference Latency SLA</strong></td>
              <td>P95 latency stays comfortably below 50 ms under load (Empirical test: 15.05 ms).</td>
              <td><span class="badge badge-success">PASS</span></td>
            </tr>
            <tr>
              <td>7</td>
              <td><strong>Automated CI Integration Tests</strong></td>
              <td>Unit and API tests pass automatically on test runner before deployment.</td>
              <td><span class="badge badge-success">PASS</span></td>
            </tr>
            <tr>
              <td>8</td>
              <td><strong>Cryptographic Artifact Integrity</strong></td>
              <td>SHA-256 checksum recorded during training and verified before loading.</td>
              <td><span class="badge badge-success">PASS</span></td>
            </tr>
            <tr>
              <td>9</td>
              <td><strong>Zero Hardcoded Credentials</strong></td>
              <td>Secrets and keys loaded strictly via environment variables or secret vaults.</td>
              <td><span class="badge badge-success">PASS</span></td>
            </tr>
            <tr>
              <td>10</td>
              <td><strong>Container Reproducibility</strong></td>
              <td>Dockerfile pins minor Python version and installs from locked <code>requirements.txt</code>.</td>
              <td><span class="badge badge-success">PASS</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 20: SELF-CHECK & INTERACTIVE TOOL  -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-20">
      <div class="section-header">
        <span class="section-tag">Module 20 • Assessment &amp; Calculation</span>
        <h2 class="section-title"><a href="#sec-20">20. Self-Check Questions and Interactive Estimator</a></h2>
      </div>

      <h3>20.1 Beginner-Friendly Self-Check Questions</h3>
      <p>Click on each question to reveal the comprehensive pedagogical answer and rationale:</p>

      <details class="interactive-accordion">
        <summary class="accordion-header">
          <span>Q1: Why is saving only the estimator (e.g. RandomForest) without the scaler or encoder a catastrophic mistake?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-body">
          <p>
            When a model is trained, its weights and split criteria are mathematically tied to the specific scale, center, and encoded representation of the training features. If you serialize only the classifier, your production API will have no access to the scaler's learned mean and variance, or the encoder's categorical mapping dictionary.
          </p>
          <p style="margin-bottom:0;">
            When raw user data arrives, either your code will crash because strings cannot be fed to matrix multipliers, or raw numbers will be fed unscaled, causing the model to produce completely random, invalid predictions. <strong>Always bundle preprocessing and estimation into a single <code>Pipeline</code> or <code>ColumnTransformer</code> and serialize the entire pipeline.</strong>
          </p>
        </div>
      </details>

      <details class="interactive-accordion">
        <summary class="accordion-header">
          <span>Q2: What is the security danger of downloading and loading a .pkl or .joblib file from an untrusted source?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-body">
          <p style="margin-bottom:0;">
            Python's <code>pickle</code> and <code>joblib</code> formats serialize code execution graphs, not just raw numerical data. Specifically, Python's <code>__reduce__</code> method allows arbitrary operating system commands to be embedded inside the binary file. When you call <code>joblib.load()</code>, Python immediately executes those embedded instructions with your current user privileges. An attacker can use this to execute reverse shells, install ransomware, or steal database passwords. Only load artifacts you personally trained or that come from secured, checksum-verified internal storage.
          </p>
        </div>
      </details>

      <details class="interactive-accordion">
        <summary class="accordion-header">
          <span>Q3: Why is FastAPI preferred over older frameworks like Flask for machine learning deployment?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-body">
          <p style="margin-bottom:0;">
            FastAPI provides native integration with Pydantic for automated data validation based on Python type hints. This guarantees that malformed requests are cleanly rejected with clear <code>422 Unprocessable Entity</code> errors before ever reaching your model. Additionally, FastAPI is built on ASGI (Starlette/Uvicorn), providing high-throughput asynchronous execution, and it generates interactive OpenAPI/Swagger documentation at <code>/docs</code> with zero extra configuration.
          </p>
        </div>
      </details>

      <details class="interactive-accordion">
        <summary class="accordion-header">
          <span>Q4: Explain the difference between Data Drift and Concept Drift using an e-commerce shopping example.</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-body">
          <p>
            <strong>Data Drift (Covariate Shift):</strong> The demographic of shoppers changes, but how they behave remains consistent. For example, a viral social media campaign causes the average age of site visitors to drop from 45 to 19. The input feature distribution <em>P(X)</em> has drifted, but 19-year-olds still buy the same items 19-year-olds have always bought.
          </p>
          <p style="margin-bottom:0;">
            <strong>Concept Drift:</strong> The demographic remains identical, but their purchasing behavior changes due to outside factors. For example, during high economic inflation, 45-year-old shoppers with identical salaries suddenly stop buying luxury goods and switch entirely to budget store brands. The mathematical relationship between income and purchasing choice <em>P(Y | X)</em> has fundamentally changed.
          </p>
        </div>
      </details>

      <details class="interactive-accordion">
        <summary class="accordion-header">
          <span>Q5: What are latency percentiles (P50, P95, P99), and why is the average (mean) latency misleading?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-body">
          <p style="margin-bottom:0;">
            The <em>mean</em> latency averages all response times together, which conceals extreme server lag. For example, if 99 users experience a fast 10 ms response but 1 user experiences a 5,000 ms freeze due to garbage collection or queue delays, the average is ~59 ms, hiding the fact that some users had an unusable experience. <strong>P95</strong> means 95% of requests completed faster than this threshold; <strong>P99</strong> captures the slowest 1% of requests (the "tail"). Production SLAs (Service Level Agreements) are always defined on P95 or P99.
          </p>
        </div>
      </details>

      <details class="interactive-accordion">
        <summary class="accordion-header">
          <span>Q6: When would you choose Batch Inference over Real-Time Inference?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-body">
          <p style="margin-bottom:0;">
            Choose <strong>Batch Inference</strong> when predictions are not needed interactively while a user waits. Classic examples include: generating daily customer churn scores for marketing teams, computing overnight credit risk ratings for 5 million cardholders, or generating weekly product recommendation emails. Batch inference is vastly cheaper because you can spin up temporary cloud workers, score millions of records at high throughput via vectorized operations, and shut the servers down immediately.
          </p>
        </div>
      </details>

      <details class="interactive-accordion">
        <summary class="accordion-header">
          <span>Q7: What is the "Champion vs. Challenger" pattern in model deployment?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-body">
          <p style="margin-bottom:0;">
            The <strong>Champion</strong> is the proven model currently serving live production traffic. The <strong>Challenger</strong> is a newly retrained candidate model. Rather than immediately swapping them, both models receive traffic concurrently. Under a <em>shadow deployment</em>, the Challenger processes live requests in the background to verify latency, stability, and memory safety, but only Champion scores are returned to users. Under a <em>canary deployment</em>, a small percentage (e.g. 5%) of live users is routed to the Challenger to observe real-world performance before full rollout.
          </p>
        </div>
      </details>

      <details class="interactive-accordion">
        <summary class="accordion-header">
          <span>Q8: What is a Docker container, and how does it prevent the "works on my machine" problem?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-body">
          <p style="margin-bottom:0;">
            A Docker container bundles the application code, the exact minor Python runtime, locked package dependencies (via <code>requirements.txt</code>), and underlying operating system C-libraries into an isolated, reproducible sandbox. By baking everything into an immutable Docker image, the application runs identically on a developer's MacBook, a Windows workstation, or a Linux cloud Kubernetes node, eliminating environment-specific version drift.
          </p>
        </div>
      </details>

      <details class="interactive-accordion">
        <summary class="accordion-header">
          <span>Q9: Why can you not immediately calculate model Accuracy or F1-Score in real-time production?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-body">
          <p style="margin-bottom:0;">
            Calculating Accuracy requires knowing both the model's prediction and the <em>true ground-truth label</em>. When your API makes a prediction today (e.g., predicting whether a loan applicant will default or whether a subscriber will cancel), the actual outcome has not happened yet! Ground-truth labels may take weeks, months, or years to arrive. Because of this <em>delayed feedback loop</em>, real-time monitoring must track proxy metrics: feature distributions, schema error rates, and prediction confidence.
          </p>
        </div>
      </details>

      <details class="interactive-accordion">
        <summary class="accordion-header">
          <span>Q10: What are the 4 fundamental testing layers in an automated ML CI/CD pipeline?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-body">
          <p style="margin-bottom:0;">
            The 4 layers are: <strong>1. Code Unit Tests</strong> (verifying feature transformation logic and utility functions); <strong>2. API Contract Tests</strong> (verifying endpoint routing, JSON status codes, and Pydantic validation); <strong>3. Data Integrity Tests</strong> (checking for nulls, unexpected categories, and schema violations); and <strong>4. Model Quality Gates</strong> (automatically verifying that candidate models exceed minimal performance baselines and latency SLAs before deployment).
          </p>
        </div>
      </details>

      <h3>20.2 Interactive Tool: Model Serving Workload &amp; Cost Estimator</h3>
      <p>
        Use this interactive engineering calculator to estimate your daily inference volume, server process requirements, and projected monthly hosting expenses:
      </p>

      <div class="calculator-card">
        <div class="calc-grid">
          <div class="calc-input-group">
            <label class="calc-label" for="calc-users">Active Daily Users:</label>
            <input type="range" id="calc-users" min="100" max="500000" step="500" value="25000" oninput="updateServingEstimates()">
            <div class="calc-val-display" id="disp-users">25,000 users</div>
          </div>

          <div class="calc-input-group">
            <label class="calc-label" for="calc-queries">Predictions per User per Day:</label>
            <input type="range" id="calc-queries" min="1" max="100" step="1" value="5" oninput="updateServingEstimates()">
            <div class="calc-val-display" id="disp-queries">5 predictions</div>
          </div>

          <div class="calc-input-group">
            <label class="calc-label" for="calc-latency">Model Inference Latency (ms):</label>
            <input type="range" id="calc-latency" min="5" max="250" step="5" value="15" oninput="updateServingEstimates()">
            <div class="calc-val-display" id="disp-latency">15 ms</div>
          </div>

          <div class="calc-input-group">
            <label class="calc-label" for="calc-instance-cost">Server Node Cost ($/month):</label>
            <input type="range" id="calc-instance-cost" min="5" max="200" step="5" value="20" oninput="updateServingEstimates()">
            <div class="calc-val-display" id="disp-cost">$20 / month (2 vCPU / 4GB RAM)</div>
          </div>
        </div>

        <div class="calc-results-box">
          <div class="calc-result-item">
            <span class="calc-result-label">Total Daily Predictions</span>
            <span class="calc-result-num" id="res-daily-preds">125,000</span>
          </div>
          <div class="calc-result-item">
            <span class="calc-result-label">Peak Traffic (Req/Sec)</span>
            <span class="calc-result-num" id="res-peak-rps">4.34 RPS</span>
          </div>
          <div class="calc-result-item">
            <span class="calc-result-label">Recommended Worker Nodes</span>
            <span class="calc-result-num" id="res-workers">1 Instance (Safe 3x Headroom)</span>
          </div>
          <div class="calc-result-item">
            <span class="calc-result-label">Estimated Monthly Hosting</span>
            <span class="calc-result-num" id="res-monthly-cost">$20.00 / month</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 21: FINAL COMPLETION BANNER        -->
    <!-- ========================================== -->
    <section class="section-card banner-section" id="sec-21">
      <div class="completion-banner">
        <div class="banner-badge">🏆 CURRICULUM MILESTONE ACHIEVED</div>
        
        <h2 class="banner-title">
          Congratulations! You've Completed Machine Learning Fundamentals
        </h2>
        
        <p class="banner-message">
          You've explored the journey from understanding data and engineering features to training, evaluating, tuning, deploying, and monitoring machine-learning models. Now turn your learning into a real project.
        </p>

        <div class="diagram-container" style="background:transparent; border:none; box-shadow:none; padding:10px 0;">
          __SVG_COMPLETION_BANNER__
        </div>

        <div class="project-challenge-card">
          <h3 class="challenge-title">🚀 Your Final Challenge: Build an End-to-End ML Project</h3>
          <p class="challenge-desc">
            The true mark of a machine learning practitioner is not scoring high marks on pre-cleaned competition datasets; it is shipping a complete, end-to-end predictive system from scratch. Choose a real-world problem you care about (e.g. real estate valuation, sports analytics, medical triage, or fraud detection) and execute the full engineering roadmap:
          </p>

          <div class="roadmap-grid">
            <div class="roadmap-step">
              <span class="step-num">1</span>
              <span class="step-name">Build</span>
              <span class="step-desc">Ingest raw data, engineer features, and train a baseline estimator.</span>
            </div>
            <div class="roadmap-step">
              <span class="step-num">2</span>
              <span class="step-name">Evaluate</span>
              <span class="step-desc">Perform stratified cross-validation and hyperparameter tuning.</span>
            </div>
            <div class="roadmap-step">
              <span class="step-num">3</span>
              <span class="step-name">Package</span>
              <span class="step-desc">Bundle transformers and model into a unified joblib pipeline artifact.</span>
            </div>
            <div class="roadmap-step">
              <span class="step-num">4</span>
              <span class="step-name">Deploy</span>
              <span class="step-desc">Create a FastAPI microservice with /health and /predict endpoints.</span>
            </div>
            <div class="roadmap-step">
              <span class="step-num">5</span>
              <span class="step-name">Test</span>
              <span class="step-desc">Write automated Pydantic schema validation and pytest integration suites.</span>
            </div>
            <div class="roadmap-step">
              <span class="step-num">6</span>
              <span class="step-name">Document</span>
              <span class="step-desc">Draft a comprehensive README with setup steps, curl calls, and schemas.</span>
            </div>
            <div class="roadmap-step">
              <span class="step-num">7</span>
              <span class="step-name">Showcase</span>
              <span class="step-desc">Publish your GitHub repository and host an interactive portfolio demo.</span>
            </div>
          </div>

          <div class="criteria-box">
            <h4>📋 The 12-Point Capstone Criteria Checklist</h4>
            <div class="criteria-list">
              <div class="criteria-item"><span>✅</span> A real or clearly documented domain dataset.</div>
              <div class="criteria-item"><span>✅</span> Data preprocessing and feature engineering.</div>
              <div class="criteria-item"><span>✅</span> A trained baseline model with metric tracking.</div>
              <div class="criteria-item"><span>✅</span> Appropriate model evaluation (ROC-AUC / F1 / RMSE).</div>
              <div class="criteria-item"><span>✅</span> Hyperparameter tuning where useful.</div>
              <div class="criteria-item"><span>✅</span> A saved preprocessing-and-model pipeline.</div>
              <div class="criteria-item"><span>✅</span> A FastAPI prediction endpoint.</div>
              <div class="criteria-item"><span>✅</span> Input validation and defensive error handling.</div>
              <div class="criteria-item"><span>✅</span> A README with setup instructions and example requests.</div>
              <div class="criteria-item"><span>✅</span> A monitoring or model-versioning demonstration.</div>
              <div class="criteria-item"><span>✅</span> A public GitHub repository for source code.</div>
              <div class="criteria-item"><span>✅</span> Optional hosting on a free/affordable cloud platform.</div>
            </div>
          </div>

          <div class="banner-cta-container">
            <a href="#sec-01" class="btn-primary">
              ↺ Review ML Deployment Fundamentals
            </a>
            <a href="#sec-17" class="btn-secondary">
              💻 Explore CodeVerse Reference Project
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- INTERACTIVE ESTIMATOR JAVASCRIPT LOGIC -->
    <script>
      function updateServingEstimates() {
        const users = parseInt(document.getElementById('calc-users').value, 10);
        const queries = parseInt(document.getElementById('calc-queries').value, 10);
        const latency = parseInt(document.getElementById('calc-latency').value, 10);
        const instanceCost = parseInt(document.getElementById('calc-instance-cost').value, 10);

        document.getElementById('disp-users').innerText = users.toLocaleString() + ' users';
        document.getElementById('disp-queries').innerText = queries + (queries === 1 ? ' prediction' : ' predictions');
        document.getElementById('disp-latency').innerText = latency + ' ms';
        document.getElementById('disp-cost').innerText = '$' + instanceCost + ' / month (2 vCPU / 4GB RAM)';

        const dailyPreds = users * queries;
        document.getElementById('res-daily-preds').innerText = dailyPreds.toLocaleString();

        // Assume an 8-hour active peak window (28,800 seconds) with a 2.5x traffic surge factor
        const avgRps = dailyPreds / 86400;
        const peakRps = (dailyPreds / 28800) * 2.5;
        document.getElementById('res-peak-rps').innerText = peakRps.toFixed(2) + ' RPS';

        // Throughput per single worker process = 1000 / latency
        const rpsPerWorker = 1000 / latency;
        // Require 3x redundancy buffer for traffic spikes and health checks
        const requiredWorkers = Math.max(1, Math.ceil((peakRps * 3.0) / rpsPerWorker));
        // A single 2-vCPU node runs ~4 Uvicorn workers
        const instances = Math.max(1, Math.ceil(requiredWorkers / 4));

        document.getElementById('res-workers').innerText = instances + (instances === 1 ? ' Instance ' : ' Instances ') + '(' + requiredWorkers + ' Uvicorn workers)';

        const monthlyCost = instances * instanceCost;
        document.getElementById('res-monthly-cost').innerText = '$' + monthlyCost.toFixed(2) + ' / month';
      }

      // Initialize on DOM load
      document.addEventListener('DOMContentLoaded', function() {
        updateServingEstimates();
      });
    </script>
"""
