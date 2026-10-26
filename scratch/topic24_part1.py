# Topic 24 Content Module — Part 1: Modules 01 to 05
# High quality, beginner-friendly, Light Mode only, accessible HTML entities.

PART_1_HTML = """
    <!-- ========================================== -->
    <!-- SECTION 01: FROM TRAINING TO DEPLOYMENT    -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-01">
      <div class="section-header">
        <span class="section-tag">Module 01 • The ML Lifecycle</span>
        <h2 class="section-title"><a href="#sec-01">1. From Machine Learning Training to Deployment</a></h2>
      </div>

      <div class="callout callout-important">
        <div class="callout-title">🎓 The Core Analogy: Educating a Student vs. Hiring Them for the Job</div>
        <p>
          Training a machine-learning model is like <strong>teaching a student in a classroom</strong> to solve complex mathematics problems. You provide textbooks (training data), guide them through practice problems (feature engineering), correct their mistakes during study sessions (loss optimization), and test their final knowledge with an exam (evaluation on a holdout test set).
        </p>
        <p style="margin-bottom:0;">
          <strong>Deployment</strong> is like hiring that graduate to sit at a professional service desk and answer live questions from real clients all day. <strong>MLOps</strong> is the human resources, quality assurance, and ongoing training system that ensures your employee remains punctual, follows company procedures, handles rude or confused customers gracefully, and updates their knowledge when regulations change.
        </p>
      </div>

      <h3>1.1 Why a Trained Model in a Notebook Is Not an Application</h3>
      <p>
        Throughout Topics 1 through 23, you focused on the scientific and statistical aspects of Machine Learning: formulating problems, engineering features, training estimators (linear regression, decision trees, random forests, neural networks), tuning hyperparameters, and measuring validation metrics.
      </p>
      <p>
        When you reach the final cell of a Jupyter notebook and observe an impressive <code>Accuracy = 95.5%</code>, it is tempting to think the project is finished. In reality, you have only completed the laboratory phase:
      </p>
      <ul>
        <li>
          <strong>Memory Isolation:</strong> A model in a Jupyter notebook lives only inside your computer's RAM. As soon as you shut down the kernel, that trained intelligence ceases to exist unless serialized to disk.
        </li>
        <li>
          <strong>No Communication Pathway:</strong> Real-world users, mobile apps, and business databases cannot directly reach inside a Jupyter notebook cell to pass feature numbers and receive predictions.
        </li>
        <li>
          <strong>Brittle Environments:</strong> Notebooks frequently run cells out of chronological order and rely on global variables. An algorithm that executes perfectly on a data scientist's laptop often crashes immediately on a server with different library versions.
        </li>
        <li>
          <strong>Data Cleansing Dependencies:</strong> If your model expects scaled numerical features and one-hot encoded categories, the application receiving raw user input must perform those exact same transformations flawlessly before passing numbers to the estimator.
        </li>
      </ul>

      <div class="diagram-container">
        __SVG_ML_LIFECYCLE__
        <div class="diagram-caption">Figure 1.1: The Complete 10-Phase Machine Learning Lifecycle. Notice that model training and evaluation represent only the middle third; model serialization, API deployment, continuous monitoring, and lifecycle governance constitute the engineering backbone that delivers business value.</div>
      </div>

      <h3>1.2 Why Trained Models Fail in Production</h3>
      <p>
        Deploying a machine learning model is fundamentally different from deploying traditional deterministic software (such as a database query or a shopping cart calculator). In traditional software, if the code passes unit tests, it will produce identical outputs for given inputs forever. In Machine Learning, systems fail silently in production for four primary reasons:
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Failure Mode</th>
              <th>Laboratory Environment</th>
              <th>Live Production Environment</th>
              <th>Consequence</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Missing Preprocessing</strong></td>
              <td>Carefully cleaned pandas DataFrames with no missing cells.</td>
              <td>User submits empty form fields, string typos, or unexpected currencies.</td>
              <td>Crash (<code>ValueError</code>) or nonsensical predictions returned to client.</td>
            </tr>
            <tr>
              <td><strong>Data Distribution Shift</strong></td>
              <td>Static historical training dataset collected in 2023.</td>
              <td>Consumer behavior, inflation, or fraud patterns shift in 2026.</td>
              <td>Silent degradation: accuracy plunges while the code returns HTTP 200 OK without errors.</td>
            </tr>
            <tr>
              <td><strong>Training-Serving Skew</strong></td>
              <td>Features calculated with complex offline SQL scripts over hours.</td>
              <td>Inference API must calculate identical features in under 20 milliseconds.</td>
              <td>Calculated features differ subtly, causing the model to make wild errors on live inputs.</td>
            </tr>
            <tr>
              <td><strong>Hardware &amp; Latency Bottlenecks</strong></td>
              <td>Heavy batch inference runs overnight on a powerful GPU workstation.</td>
              <td>1,000 simultaneous mobile users hit a lightweight web server at 9:00 AM.</td>
              <td>Server runs out of memory (OOM), HTTP requests time out, users abandon the app.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-tip">
        <div class="callout-title">💡 The Core Takeaway</div>
        <p style="margin-bottom:0;">
          <strong>Deployment is a separate, vital engineering discipline.</strong> Building a great model requires statistical intuition; deploying and maintaining a model requires robust software architecture, defensive input validation, automated testing, and active observability.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 02: WHAT IS MODEL DEPLOYMENT?      -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-02">
      <div class="section-header">
        <span class="section-tag">Module 02 • Core Architecture</span>
        <h2 class="section-title"><a href="#sec-02">2. What Is Model Deployment?</a></h2>
      </div>

      <p>
        At its simplest level, <strong>model deployment</strong> is the technical process of taking a trained mathematical artifact (weights, decision rules, and transformation parameters) and integrating it into an operational environment where it can accept new, unseen data and return actionable predictions.
      </p>

      <div class="diagram-container">
        __SVG_DEPLOYMENT_ARCH__
        <div class="diagram-caption">Figure 2.1: Model Deployment Paradigms. Predictions can be served synchronously on demand via REST APIs, asynchronously in massive scheduled batches, or embedded directly inside local client devices.</div>
      </div>

      <h3>2.1 The Two Primary Serving Paradigms</h3>
      <p>
        Every machine learning workload falls into one of two fundamental operational modes based on whether the prediction is needed immediately by an interactive user or asynchronously in bulk:
      </p>

      <div class="diagram-container">
        __SVG_BATCH_VS_REALTIME__
        <div class="diagram-caption">Figure 2.2: Batch Inference vs. Real-Time Inference. Real-time serving prioritizes low latency for individual requests; batch scoring prioritizes high throughput for massive datasets during off-peak hours.</div>
      </div>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Real-Time Inference (Online / On-Demand)</th>
              <th>Batch Inference (Offline / Scheduled)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Trigger</strong></td>
              <td>Interactive event: user clicks a button, API call arrives.</td>
              <td>Scheduled timer (cron job) or database event (midnight batch).</td>
            </tr>
            <tr>
              <td><strong>Payload Size</strong></td>
              <td>Single record or small array (1 to 10 records).</td>
              <td>Massive dataset (10,000 to 100,000,000 rows).</td>
            </tr>
            <tr>
              <td><strong>Latency Target</strong></td>
              <td>Strict: 10 to 100 milliseconds.</td>
              <td>Relaxed: Minutes to several hours.</td>
            </tr>
            <tr>
              <td><strong>Hardware &amp; Cost</strong></td>
              <td>Always-on server or auto-scaling cluster; costs run 24/7.</td>
              <td>Ephemeral compute: spin up instances, score, shut down.</td>
            </tr>
            <tr>
              <td><strong>Typical Examples</strong></td>
              <td>Credit card fraud detection, dynamic pricing, autocomplete.</td>
              <td>Weekly churn scoring, monthly loan risk reports, email marketing.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>2.2 When Is a Notebook Sufficient vs. When Is an App Required?</h3>
      <ul>
        <li>
          <strong>A Notebook Is Sufficient When:</strong> You are exploring a new research idea, presenting findings to internal stakeholders, generating a one-time quarterly forecast chart, or testing whether a predictive signal even exists in the data.
        </li>
        <li>
          <strong>An Application Is Required When:</strong> The predictions must drive automated actions (e.g., blocking a stolen credit card), external users need access through a web or mobile interface, multiple systems must query the model concurrently, or predictions must run reliably on a recurring schedule without manual human intervention.
        </li>
      </ul>

      <div class="callout callout-warning">
        <div class="callout-title">⚠️ Clarification: Not Every ML Project Requires Public Cloud Hosting</div>
        <p style="margin-bottom:0;">
          A common misconception among beginners is that deployment requires renting expensive cloud clusters on AWS, Google Cloud, or Azure. In reality, millions of production models run locally on edge devices (smartphones, IoT sensors, hospital workstations, or internal on-premise servers). Deploying locally or on private networks is often faster, costs zero cloud subscription fees, and guarantees complete data privacy.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 03: MODEL ARTIFACT & SERIALIZATION -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-03">
      <div class="section-header">
        <span class="section-tag">Module 03 • Persistence &amp; Integrity</span>
        <h2 class="section-title"><a href="#sec-03">3. Model Artifact and Serialization</a></h2>
      </div>

      <p>
        When a scikit-learn model finishes training, what actually exists inside Python? It is a complex hierarchy of Python objects, numpy arrays holding floating-point weights, tree structures with split indices, and dictionary mappings. To make this trained state usable outside the active Python process, we must perform <strong>serialization</strong>.
      </p>

      <div class="diagram-container">
        __SVG_ARTIFACT_WORKFLOW__
        <div class="diagram-caption">Figure 3.1: Model Serialization &amp; Deserialization Workflow. Memory-resident pipelines are converted into binary byte streams, stored on persistent disk as artifacts, and safely loaded into inference servers.</div>
      </div>

      <h3>3.1 What Is a Model Artifact?</h3>
      <p>
        A <strong>model artifact</strong> is a file (or collection of files) stored on persistent storage that contains all the learned parameters, structure, and metadata required to reconstruct the exact mathematical state of an estimator and its associated transformers.
      </p>

      <h3>3.2 Why You Must Serialize the Entire Pipeline, Not Just the Estimator</h3>
      <div class="callout callout-important">
        <div class="callout-title">🚨 The #1 Fatal Mistake in ML Deployment</div>
        <p>
          Beginners frequently train a model like this:
        </p>
        <pre><code class="language-python"># DO NOT DO THIS!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)

# Saving ONLY the classifier:
joblib.dump(model, "my_model.joblib")  # DISASTER WAITING TO HAPPEN!</code></pre>
        <p style="margin-bottom:0;">
          If you save only the estimator, your inference server has no record of the scaler's means or standard deviations! When a real customer sends raw unscaled values, passing them into the raw classifier produces wildly incorrect predictions. <strong>Always bundle preprocessing and estimation into a single <code>Pipeline</code> or <code>ColumnTransformer</code> and serialize the entire pipeline as a unified artifact.</strong>
        </p>
      </div>

      <h3>3.3 Joblib vs. Pickle</h3>
      <p>
        Python includes a built-in module named <code>pickle</code> for serializing arbitrary objects. However, scientific computing libraries like scikit-learn and numpy strongly recommend <strong><code>joblib</code></strong>:
      </p>
      <ul>
        <li><code>pickle</code> serializes Python objects recursively, which can be slow and memory-intensive when handling arrays with millions of floating-point numbers.</li>
        <li><code>joblib</code> is specifically optimized for large numpy data buffers. It performs efficient disk compression, supports fast zero-copy memory mapping, and handles multi-array structures seamlessly.</li>
      </ul>

      <h3>3.4 Reproducible Code: Train, Save, Reload, and Verify</h3>
      <p>
        Here is a complete, runnable Python snippet demonstrating safe serialization and verification on our customer churn pipeline:
      </p>

      <pre><code class="language-python">import joblib
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier

# 1. Define preprocessor for mixed tabular data
num_cols = ['tenure_months', 'monthly_charges', 'total_charges', 'has_tech_support']
cat_cols = ['contract_type']

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
])

# 2. Assemble unified pipeline
full_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42))
])

# 3. Fit pipeline on training data
full_pipeline.fit(X_train, y_train)

# 4. Serialize the unified artifact to disk
artifact_path = "customer_churn_pipeline.joblib"
joblib.dump(full_pipeline, artifact_path)
print(f"Artifact saved: {artifact_path}")

# 5. Deserialization: Load artifact into a fresh environment
loaded_pipeline = joblib.load(artifact_path)

# 6. Verify mathematical parity on test samples
original_preds = full_pipeline.predict(X_test)
reloaded_preds = loaded_pipeline.predict(X_test)
assert np.array_equal(original_preds, reloaded_preds), "Parity error detected!"
print("Verification PASSED: 100% identical predictions across memory & disk.")</code></pre>

      <div class="callout callout-danger">
        <div class="callout-title">🔒 Critical Security Warning: The Pickle/Joblib Vulnerability</div>
        <p>
          Both <code>pickle</code> and <code>joblib</code> execute arbitrary Python bytecode during deserialization via the <code>__reduce__</code> magic method. If an attacker tampers with your <code>.joblib</code> or <code>.pkl</code> file, or if you download an unverified model file from an untrusted public internet source, <strong>loading that file can instantly execute malicious shell commands, install ransomware, or steal server credentials</strong>.
        </p>
        <p style="margin-bottom:0;">
          <strong>Golden Rule:</strong> Only deserialize model artifacts that were generated by your own secured training pipelines and stored in access-controlled object storage with cryptographic checksum (SHA-256) validation.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 04: SERVING PREDICTIONS VIA API    -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-04">
      <div class="section-header">
        <span class="section-tag">Module 04 • API Fundamentals</span>
        <h2 class="section-title"><a href="#sec-04">4. Serving Predictions Through an API</a></h2>
      </div>

      <div class="callout callout-important">
        <div class="callout-title">🛎️ The Everyday Analogy: The Clinic Receptionist</div>
        <p>
          Imagine a busy specialist clinic. Patients do not burst directly into the surgeon's operating room while holding messy handwritten notes. Instead, a trained <strong>receptionist</strong> sits at the front desk:
        </p>
        <ol>
          <li>The receptionist greets the visitor and reviews their intake form (<strong>HTTP Request &amp; Input Validation</strong>).</li>
          <li>If fields are missing or numbers are absurd (e.g. negative age), the receptionist politely rejects the form immediately (<strong>HTTP 422 Unprocessable Entity</strong>).</li>
          <li>If the form is valid, the receptionist neatly transcribes the vitals and walks into the examination room (<strong>Invoking the ML Pipeline</strong>).</li>
          <li>The specialist reviews the numbers, makes a diagnosis, and hands the chart back (<strong>Model Inference</strong>).</li>
          <li>The receptionist places the result into a clean, standardized envelope and hands it to the patient (<strong>JSON HTTP Response</strong>).</li>
        </ol>
        <p style="margin-bottom:0;">
          In modern software architecture, an <strong>API (Application Programming Interface)</strong> is that receptionist. It shields your model from malformed data and provides a universally understood communication protocol.
        </p>
      </div>

      <div class="diagram-container">
        __SVG_API_FLOW__
        <div class="diagram-caption">Figure 4.1: Client-Server API Request/Response Cycle. Notice how the API web layer acts as an impermeable validation gate, guaranteeing that only sanitised, valid payloads reach the internal ML inference pipeline.</div>
      </div>

      <h3>4.1 Core Web Concepts for Machine Learning Engineers</h3>
      <ul>
        <li>
          <strong>Client &amp; Server:</strong> The <em>client</em> is any software that requests a prediction (a Flutter mobile app, a React website, or an automated batch script). The <em>server</em> is the listening computer hosting your Python runtime and loaded model.
        </li>
        <li>
          <strong>HTTP Methods:</strong> While web browsers use <code>GET</code> to view web pages, prediction APIs use <strong><code>POST</code></strong>. <code>POST</code> allows the client to send a structured body containing customer feature variables safely.
        </li>
        <li>
          <strong>Endpoint:</strong> A specific URL path that handles a dedicated task (e.g., <code>/health</code> for service monitoring, <code>/predict</code> for scoring).
        </li>
        <li>
          <strong>JSON (JavaScript Object Notation):</strong> The universal text format for exchanging structured data across programming languages. A Python dictionary maps 1-to-1 with JSON:
          <pre><code class="language-json">{
  "tenure_months": 12,
  "monthly_charges": 75.50,
  "total_charges": 906.00,
  "contract_type": "Month-to-month",
  "has_tech_support": 0
}</code></pre>
        </li>
        <li>
          <strong>HTTP Status Codes:</strong> The standard numerical codes that communicate request status:
          <ul>
            <li><code>200 OK</code>: The prediction was generated successfully.</li>
            <li><code>422 Unprocessable Entity</code>: The input data violated validation rules (e.g., negative tenure).</li>
            <li><code>500 Internal Server Error</code>: An unhandled exception occurred inside the Python backend.</li>
          </ul>
        </li>
      </ul>

      <h3>4.2 The Crucial Boundary: API Layer vs. ML Model</h3>
      <p>
        Keep your concerns strictly separated. The API layer (FastAPI, Flask) handles network connections, authentication, request rate limiting, and input schema validation. The ML model (scikit-learn pipeline) handles mathematical transformation and statistical scoring. Keeping them decoupled ensures you can update your machine learning model without touching your web routing code, or vice versa.
      </p>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 05: FASTAPI APPLICATION            -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-05">
      <div class="section-header">
        <span class="section-tag">Module 05 • Practical Web Service</span>
        <h2 class="section-title"><a href="#sec-05">5. Build a Beginner-Friendly FastAPI Application</a></h2>
      </div>

      <p>
        Why choose <strong>FastAPI</strong> for machine learning deployment? Unlike older frameworks like Flask or Django, FastAPI offers three critical advantages:
      </p>
      <ol>
        <li><strong>Automatic Input Validation via Pydantic:</strong> Incoming JSON is automatically validated against strict type annotations and range constraints before your model code ever runs.</li>
        <li><strong>High Performance:</strong> Built on top of Starlette and Uvicorn, FastAPI provides asynchronous concurrency with near-Go/Node speeds.</li>
        <li><strong>Automatic Interactive Documentation:</strong> FastAPI automatically generates interactive Swagger UI documentation at <code>/docs</code>, allowing you to test endpoints directly in your web browser.</li>
      </ol>

      <div class="diagram-container">
        __SVG_FASTAPI_ARCH__
        <div class="diagram-caption">Figure 5.1: FastAPI High-Performance Serving Architecture. Incoming requests are parsed, validated against the Pydantic schema, transformed into a single-row DataFrame, passed through the pre-loaded pipeline, and returned as structured JSON.</div>
      </div>

      <h3>5.1 The Complete FastAPI Application Code (<code>app.py</code>)</h3>
      <p>
        Below is the clean, self-contained production code tested and verified on our Customer Churn model:
      </p>

      <pre><code class="language-python">import time
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# 1. Initialize FastAPI Application
app = FastAPI(
    title="Customer Churn Prediction API",
    description="Production REST microservice serving a leak-free scikit-learn pipeline",
    version="1.0.0"
)

# 2. Load the trained model artifact into memory ONCE at application startup
ARTIFACT_PATH = "customer_churn_pipeline.joblib"
try:
    pipeline = joblib.load(ARTIFACT_PATH)
    print(f"Successfully loaded model artifact from {ARTIFACT_PATH}")
except Exception as e:
    raise RuntimeError(f"Failed to load model artifact: {e}")

# 3. Define the Input Schema with Defensive Range Constraints using Pydantic
class CustomerFeatures(BaseModel):
    tenure_months: int = Field(..., ge=0, le=120, description="Customer relationship length in months (0-120)")
    monthly_charges: float = Field(..., gt=0.0, le=500.0, description="Monthly recurring charge in USD")
    total_charges: float = Field(..., ge=0.0, description="Cumulative lifetime charges in USD")
    contract_type: str = Field(..., description="Contract duration: 'Month-to-month', 'One year', 'Two year'")
    has_tech_support: int = Field(..., ge=0, le=1, description="Binary support flag: 1 if active, 0 otherwise")

    class Config:
        json_schema_extra = {
            "example": {
                "tenure_months": 6,
                "monthly_charges": 89.50,
                "total_charges": 537.00,
                "contract_type": "Month-to-month",
                "has_tech_support": 0
            }
        }

# 4. Define Health Check Endpoint
@app.get("/health", tags=["Monitoring"])
def health_check():
    # Returns server vitality and loaded model metadata.
    return {
        "status": "healthy",
        "service": "customer-churn-api",
        "model_version": "1.0.0",
        "pipeline_loaded": True
    }

# 5. Define Real-Time Prediction Endpoint
@app.post("/predict", tags=["Inference"])
def predict_churn(customer: CustomerFeatures):
    # Generates real-time churn probability and risk tier for a customer.
    start_time = time.perf_counter()

    # Convert incoming schema to pandas DataFrame matching pipeline column names
    input_data = pd.DataFrame([{
        'tenure_months': customer.tenure_months,
        'monthly_charges': customer.monthly_charges,
        'total_charges': customer.total_charges,
        'contract_type': customer.contract_type,
        'has_tech_support': customer.has_tech_support
    }])

    try:
        # Generate predictions through the unified pipeline
        prediction = int(pipeline.predict(input_data)[0])
        probability = float(pipeline.predict_proba(input_data)[0, 1])
        latency_ms = round((time.perf_counter() - start_time) * 1000, 2)

        # Categorize business risk tier
        if probability >= 0.70:
            risk_tier = "High"
        elif probability >= 0.40:
            risk_tier = "Medium"
        else:
            risk_tier = "Low"

        return {
            "prediction": prediction,
            "prediction_label": "Churn" if prediction == 1 else "Retained",
            "churn_probability": round(probability, 4),
            "risk_tier": risk_tier,
            "model_version": "1.0.0",
            "inference_latency_ms": latency_ms
        }
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(err)}")</code></pre>

      <h3>5.2 Step-by-Step Instructions: Running Locally</h3>
      <ol>
        <li>
          <strong>Install the required dependencies:</strong>
          <pre><code class="language-bash">pip install fastapi uvicorn scikit-learn pandas joblib pydantic</code></pre>
        </li>
        <li>
          <strong>Launch the Uvicorn ASGI server:</strong>
          <pre><code class="language-bash">uvicorn app:app --host 127.0.0.1 --port 8000 --reload</code></pre>
          The terminal will display: <code>Application startup complete. Uvicorn running on http://127.0.0.1:8000</code>.
        </li>
        <li>
          <strong>Open your web browser</strong> and navigate to <a href="http://127.0.0.1:8000/docs" target="_blank" rel="noopener"><code>http://127.0.0.1:8000/docs</code></a> to explore the automatic interactive Swagger documentation.
        </li>
      </ol>

      <h3>5.3 Verified Request and Response Tests</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Test Scenario</th>
              <th>Request Payload (JSON)</th>
              <th>HTTP Status &amp; Response Body</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Health Check</strong></td>
              <td><code>GET /health</code></td>
              <td>
                <span class="badge badge-success">HTTP 200 OK</span>
                <pre><code class="language-json">{
  "status": "healthy",
  "service": "customer-churn-api",
  "model_version": "1.0.0",
  "pipeline_loaded": true
}</code></pre>
              </td>
            </tr>
            <tr>
              <td><strong>High-Risk Customer (New, high bill, Month-to-month)</strong></td>
              <td>
                <pre><code class="language-json">{
  "tenure_months": 3,
  "monthly_charges": 95.0,
  "total_charges": 285.0,
  "contract_type": "Month-to-month",
  "has_tech_support": 0
}</code></pre>
              </td>
              <td>
                <span class="badge badge-success">HTTP 200 OK</span>
                <pre><code class="language-json">{
  "prediction": 1,
  "prediction_label": "Churn",
  "churn_probability": 0.9996,
  "risk_tier": "High",
  "model_version": "1.0.0",
  "inference_latency_ms": 12.69
}</code></pre>
              </td>
            </tr>
            <tr>
              <td><strong>Low-Risk Loyal Customer (4 yr tenure, Two year contract)</strong></td>
              <td>
                <pre><code class="language-json">{
  "tenure_months": 48,
  "monthly_charges": 45.0,
  "total_charges": 2160.0,
  "contract_type": "Two year",
  "has_tech_support": 1
}</code></pre>
              </td>
              <td>
                <span class="badge badge-success">HTTP 200 OK</span>
                <pre><code class="language-json">{
  "prediction": 0,
  "prediction_label": "Retained",
  "churn_probability": 0.0005,
  "risk_tier": "Low",
  "model_version": "1.0.0",
  "inference_latency_ms": 11.84
}</code></pre>
              </td>
            </tr>
            <tr>
              <td><strong>Invalid Payload (Negative tenure &amp; bill &gt; $500)</strong></td>
              <td>
                <pre><code class="language-json">{
  "tenure_months": -5,
  "monthly_charges": 999.0,
  "total_charges": 100.0,
  "contract_type": "Month-to-month",
  "has_tech_support": 0
}</code></pre>
              </td>
              <td>
                <span class="badge badge-warning">HTTP 422 Unprocessable Entity</span>
                <pre><code class="language-json">{
  "detail": [
    {
      "loc": ["body", "tenure_months"],
      "msg": "Input should be greater than or equal to 0",
      "type": "greater_than_equal"
    },
    {
      "loc": ["body", "monthly_charges"],
      "msg": "Input should be less than or equal to 500",
      "type": "less_than_equal"
    }
  ]
}</code></pre>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
