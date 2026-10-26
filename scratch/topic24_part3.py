# Topic 24 Content Module — Part 3: Modules 12 to 16
# High quality, beginner-friendly, Light Mode only, accessible HTML entities.

PART_3_HTML = """
    <!-- ========================================== -->
    <!-- SECTION 12: MONITORING A DEPLOYED MODEL    -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-12">
      <div class="section-header">
        <span class="section-tag">Module 12 • Real-Time Observability</span>
        <h2 class="section-title"><a href="#sec-12">12. Monitoring a Deployed ML Model</a></h2>
      </div>

      <p>
        In traditional IT systems, monitoring answers a straightforward question: <em>"Is the server responding?"</em> If the HTTP status code is <code>200 OK</code> and memory usage is under 70%, the system is declared healthy.
      </p>
      <p>
        In production Machine Learning, an API can return <code>200 OK</code> within 10 milliseconds while returning completely catastrophic predictions. That is why ML observability operates on <strong>four distinct tiers</strong>:
      </p>

      <div class="diagram-container">
        __SVG_MONITORING_DASH__
        <div class="diagram-caption">Figure 12.1: Multi-Tier ML Observability Dashboard. Real-time observability tracking request throughput, P95/P99 latency tails, feature distribution shifts, and business churn outcomes.</div>
      </div>

      <h3>12.1 The Four Tiers of ML Observability</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Tier</th>
              <th>Metrics Tracked</th>
              <th>Alerting Threshold Example</th>
              <th>Action When Triggered</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Service &amp; System Health</strong></td>
              <td>Throughput (req/sec), CPU/RAM load, HTTP 500 error rate, P99 latency.</td>
              <td>Error rate &gt; 1% or P99 latency &gt; 100 ms for 5 minutes.</td>
              <td>Auto-scale server instances; inspect API logs for crash tracebacks.</td>
            </tr>
            <tr>
              <td><strong>2. Data Quality &amp; Integrity</strong></td>
              <td>Missing feature percentage, out-of-range numerical values, unseen categories.</td>
              <td>&gt; 2% missing values in a mandatory column like <code>monthly_charges</code>.</td>
              <td>Alert upstream mobile/frontend engineering team of broken data payload.</td>
            </tr>
            <tr>
              <td><strong>3. Output &amp; Prediction Distribution</strong></td>
              <td>Average predicted probability, proportion of positive class predictions.</td>
              <td>Predicted churn rate swings from historical 28% to 65% in 24 hours.</td>
              <td>Investigate possible upstream data pipeline corruption or bot traffic.</td>
            </tr>
            <tr>
              <td><strong>4. Model Ground-Truth Performance</strong></td>
              <td>Accuracy, Precision, Recall, F1-Score, ROC-AUC.</td>
              <td>Recall on actual churned accounts drops below 0.85 on monthly audit.</td>
              <td>Initiate champion/challenger retraining workflow on recent data.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>12.2 The Delayed Ground-Truth Dilemma</h3>
      <div class="callout callout-warning">
        <div class="callout-title">⏳ The Fundamental Challenge: You Cannot Calculate Accuracy Immediately</div>
        <p style="margin-bottom:0;">
          When a customer hits your prediction endpoint today, you predict they will churn in 60 days. <strong>You cannot calculate Accuracy, Precision, or Recall today</strong> because you do not know if the customer will actually churn until 60 days have passed! Therefore, real-time ML monitoring relies heavily on <em>proxy metrics</em>: input feature distributions, prediction confidence, and schema error rates.
        </p>
      </div>

      <h3>12.3 Privacy and Data Logging Best Practices</h3>
      <p>
        When logging live inference payloads to monitoring databases (like Elasticsearch or PostgreSQL), adhere to strict privacy standards:
      </p>
      <ul>
        <li><strong>Scrub Personally Identifiable Information (PII):</strong> Never log customer names, email addresses, credit card numbers, or passwords.</li>
        <li><strong>Anonymize User Identifiers:</strong> Hash sensitive IDs using SHA-256 before storing them in telemetry logs.</li>
        <li><strong>Set Data Retention Limits:</strong> Automatically purge raw inference request logs after 30 to 90 days to comply with GDPR and privacy regulations.</li>
      </ul>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 13: RETRAINING & MODEL LIFECYCLE   -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-13">
      <div class="section-header">
        <span class="section-tag">Module 13 • Lifecycle Management</span>
        <h2 class="section-title"><a href="#sec-13">13. Retraining and Model Lifecycle Management</a></h2>
      </div>

      <p>
        <strong>Model retraining</strong> is the process of fitting an existing model architecture on fresh, recently gathered training data to restore degraded statistical performance.
      </p>

      <div class="diagram-container">
        __SVG_RETRAINING_LOOP__
        <div class="diagram-caption">Figure 13.1: Governed Retraining &amp; Champion-Challenger Workflow. Models are evaluated through rigorous statistical comparison and human approval gates before production traffic is rerouted.</div>
      </div>

      <h3>13.1 What Triggers a Retraining Pipeline?</h3>
      <ol>
        <li><strong>Scheduled Cadence:</strong> Retraining runs periodically (e.g., weekly for e-commerce recommendations, quarterly for credit scoring).</li>
        <li><strong>Performance Threshold Degradation:</strong> Retraining triggers automatically when audited accuracy or F1-score drops below acceptable business thresholds.</li>
        <li><strong>Severe Data Drift:</strong> Retraining triggers when statistical tests (e.g., Kolmogorov-Smirnov test or Population Stability Index) indicate incoming data has fundamentally diverged from the training baseline.</li>
        <li><strong>Major Domain Events:</strong> Sudden changes in regulations, company pricing structures, or newly introduced product categories.</li>
      </ol>

      <h3>13.2 The Champion vs. Challenger Deployment Strategy</h3>
      <p>
        Never automatically replace an active production model (the <strong>Champion</strong>) simply because a newly retrained candidate (the <strong>Challenger</strong>) finishes training. Instead, follow a disciplined release strategy:
      </p>
      <ul>
        <li>
          <strong>Shadow Deployment:</strong> Both models receive 100% of incoming production traffic. However, only the Champion's predictions are returned to users. The Challenger's predictions are recorded silently in the background to verify stability, latency, and memory safety without risking user experience.
        </li>
        <li>
          <strong>Canary Release / A/B Testing:</strong> 95% of traffic continues to route to the Champion, while 5% routes to the Challenger. If error rates remain zero and business conversion improves over 7 days, traffic is gradually shifted to 100%.
        </li>
      </ul>

      <div class="callout callout-danger">
        <div class="callout-title">🛑 Crucial Safety Rule: Human in the Loop</div>
        <p style="margin-bottom:0;">
          For high-stakes applications (medical diagnosis, lending decisions, criminal justice, or automated trading), <strong>retraining pipelines should never deploy to production without explicit human review and sign-off</strong>. Automated pipelines should package the model and present an audit report; a human domain expert makes the final deployment decision.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 14: CI/CD & AUTOMATED ML TESTING   -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-14">
      <div class="section-header">
        <span class="section-tag">Module 14 • Continuous Integration</span>
        <h2 class="section-title"><a href="#sec-14">14. CI/CD and Automated ML Testing</a></h2>
      </div>

      <p>
        In modern software engineering, <strong>Continuous Integration (CI)</strong> automatically runs tests every time a developer commits code, while <strong>Continuous Delivery (CD)</strong> packages and releases verified code to servers.
      </p>

      <div class="diagram-container">
        __SVG_CICD_WORKFLOW__
        <div class="diagram-caption">Figure 14.1: Automated CI/CD Testing Pipeline for Machine Learning. Every code commit triggers automated linting, unit tests, schema contracts, model performance regression checks, and packaging before deployment.</div>
      </div>

      <h3>14.1 The 4 Testing Layers for Machine Learning</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Testing Layer</th>
              <th>What Is Tested</th>
              <th>Example Python Tool</th>
              <th>Failure Consequence</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Code Unit Tests</strong></td>
              <td>Feature transformation functions, custom encoders, metric calculation logic.</td>
              <td><code>pytest</code></td>
              <td>Pipeline crashes with syntax or runtime exceptions.</td>
            </tr>
            <tr>
              <td><strong>2. API Contract Tests</strong></td>
              <td>HTTP endpoints, status codes, input JSON schemas, 422 error handlers.</td>
              <td><code>TestClient</code> / <code>requests</code></td>
              <td>Frontend apps break when expecting specific JSON keys.</td>
            </tr>
            <tr>
              <td><strong>3. Data Integrity Tests</strong></td>
              <td>Null value checks, range constraints, duplicate row detection.</td>
              <td><code>Great Expectations</code> / <code>Pydantic</code></td>
              <td>Garbage data silently enters training loops.</td>
            </tr>
            <tr>
              <td><strong>4. Model Quality Gates</strong></td>
              <td>Model performance must exceed a strict baseline (e.g. F1 &gt; 0.90) and latency &lt; 30 ms.</td>
              <td>Automated CI evaluation script</td>
              <td>Inferior models are blocked from reaching production servers.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>14.2 Executable Automated Test Suite in Python</h3>
      <p>
        Below is an automated test script using FastAPI's <code>TestClient</code> that runs in seconds inside any CI/CD pipeline:
      </p>

      <pre><code class="language-python">from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check_endpoint():
    # Verify service is healthy and model is loaded.
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["pipeline_loaded"] is True

def test_valid_prediction():
    # Verify endpoint generates valid risk classification.
    payload = {
        "tenure_months": 12,
        "monthly_charges": 75.5,
        "total_charges": 906.0,
        "contract_type": "Month-to-month",
        "has_tech_support": 0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] in [0, 1]
    assert 0.0 &lt;= data["churn_probability"] &lt;= 1.0
    assert data["risk_tier"] in ["Low", "Medium", "High"]

def test_negative_tenure_validation_failure():
    # Verify Pydantic blocks physically impossible negative tenure values.
    invalid_payload = {
        "tenure_months": -5,
        "monthly_charges": 50.0,
        "total_charges": 200.0,
        "contract_type": "Month-to-month",
        "has_tech_support": 0
    }
    response = client.post("/predict", json=invalid_payload)
    assert response.status_code == 422  # Must be rejected before hitting model!</code></pre>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 15: MODEL SECURITY & RELIABILITY   -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-15">
      <div class="section-header">
        <span class="section-tag">Module 15 • Security &amp; Defense</span>
        <h2 class="section-title"><a href="#sec-15">15. Model Security and Reliability</a></h2>
      </div>

      <p>
        A machine learning model running on an open network is an attack surface. Malicious actors can attempt to exploit your system through adversarial inputs, resource exhaustion, or credential theft.
      </p>

      <div class="diagram-container">
        __SVG_SECURITY_CHECKLIST__
        <div class="diagram-caption">Figure 15.1: The 6 Pillars of Production ML Security &amp; Reliability. Rigorous input validation, cryptographic artifact integrity, environment secret isolation, rate limiting, and privacy sanitization.</div>
      </div>

      <h3>15.1 The 6 Pillars of Production ML Security</h3>
      <ol>
        <li>
          <strong>Strict Input Validation:</strong> Always validate incoming feature types and numerical ranges via Pydantic or schema validators. Never feed unvalidated user input directly to numpy or pandas.
        </li>
        <li>
          <strong>Artifact Cryptographic Verification:</strong> Calculate the SHA-256 hash of your <code>.joblib</code> files immediately after training. Verify this checksum before loading the artifact in production to prevent tampering.
        </li>
        <li>
          <strong>Environment Secrets Management:</strong> Never hardcode API keys, database passwords, or cloud credentials in source code or Git repositories. Use environment variables (<code>os.environ.get(...)</code>) or secret vaults (AWS Secrets Manager, HashiCorp Vault).
        </li>
        <li>
          <strong>API Rate Limiting &amp; Authentication:</strong> Protect your inference endpoints behind API keys, OAuth2 tokens, and rate limiters (e.g. max 100 requests per minute per IP) to prevent Denial of Service (DoS) and model scraping.
        </li>
        <li>
          <strong>Privacy &amp; PII Scrubbing:</strong> Ensure no personal data (names, social security numbers, phone numbers) is recorded in server logs or training data without explicit cryptographic anonymization.
        </li>
        <li>
          <strong>Dependency Vulnerability Scanning:</strong> Regularly scan your <code>requirements.txt</code> with tools like <code>pip-audit</code> or Dependabot to detect known Common Vulnerabilities and Exposures (CVEs) in third-party libraries.
        </li>
      </ol>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 16: DEPLOYMENT CHALLENGES & MATRIX -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-16">
      <div class="section-header">
        <span class="section-tag">Module 16 • Practical Troubleshooting</span>
        <h2 class="section-title"><a href="#sec-16">16. Model Deployment Challenges</a></h2>
      </div>

      <p>
        When deploying models in real-world organizations, unexpected bugs occur frequently. Below is a comprehensive diagnostic troubleshooting guide covering the most common production pitfalls:
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Symptom / Error</th>
              <th>Root Cause</th>
              <th>Diagnostic Check</th>
              <th>Practical Fix</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>FileNotFoundError: [Errno 2] No such file</code></td>
              <td>Relative file path assumes the script runs from a specific directory.</td>
              <td>Check <code>os.getcwd()</code> inside the server startup script.</td>
              <td>Use absolute paths via <code>os.path.join(os.path.dirname(__file__), "artifact.joblib")</code>.</td>
            </tr>
            <tr>
              <td><code>ValueError: columns are missing or misordered</code></td>
              <td>Dictionary passed to model without preserving exact training column order.</td>
              <td>Inspect <code>pipeline.feature_names_in_</code> against input keys.</td>
              <td>Construct input DataFrames explicitly specifying the exact ordered column list.</td>
            </tr>
            <tr>
              <td><code>ValueError: Found unknown categories</code></td>
              <td>User submitted a category (e.g. <code>contract_type="Three year"</code>) not seen during training.</td>
              <td>Check unique categories in the training dataset.</td>
              <td>Set <code>OneHotEncoder(handle_unknown='ignore')</code> in your preprocessor.</td>
            </tr>
            <tr>
              <td><code>HTTP 500: Out of Memory (OOM)</code></td>
              <td>Model artifact loaded repeatedly inside the request function instead of once globally.</td>
              <td>Inspect server RAM usage spike on every incoming request.</td>
              <td>Load the model artifact into memory <strong>once</strong> during server startup, outside endpoint functions.</td>
            </tr>
            <tr>
              <td><code>Incompatible version pickle error</code></td>
              <td>Scikit-learn version on the inference server differs from the training machine.</td>
              <td>Run <code>pip list | grep scikit-learn</code> on both environments.</td>
              <td>Pin exact package versions in <code>requirements.txt</code> (e.g. <code>scikit-learn==1.3.0</code>) or use Docker.</td>
            </tr>
            <tr>
              <td><code>HTTP 422 Unprocessable Entity</code></td>
              <td>Client sent a feature with an invalid data type (e.g. string <code>"12"</code> instead of integer <code>12</code>).</td>
              <td>Check the validation error details returned in the 422 JSON response body.</td>
              <td>Review the API documentation at <code>/docs</code> and ensure client types match Pydantic schema.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
