# Topic 24 Content Module — Part 2: Modules 06 to 11
# High quality, beginner-friendly, Light Mode only, accessible HTML entities.

PART_2_HTML = """
    <!-- ========================================== -->
    <!-- SECTION 06: BATCH VS REAL-TIME INFERENCE   -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-06">
      <div class="section-header">
        <span class="section-tag">Module 06 • Inference Paradigms</span>
        <h2 class="section-title"><a href="#sec-06">6. Batch Inference vs. Real-Time Inference</a></h2>
      </div>

      <p>
        One of the most consequential architectural decisions an ML engineer makes is selecting between <strong>Batch Inference</strong> and <strong>Real-Time (Online) Inference</strong>. Choosing the wrong paradigm can lead to millions of wasted dollars in cloud server bills or unacceptable delays for end users.
      </p>

      <h3>6.1 Architectural Trade-Offs</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Architecture Metric</th>
              <th>Real-Time Inference (Online API)</th>
              <th>Batch Inference (Offline Scoring)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Primary Objective</strong></td>
              <td>Ultra-low latency for interactive user sessions.</td>
              <td>Massive throughput and cost efficiency per record.</td>
            </tr>
            <tr>
              <td><strong>Response Time</strong></td>
              <td>10 ms to 150 ms per request.</td>
              <td>Minutes to hours for millions of rows.</td>
            </tr>
            <tr>
              <td><strong>Infrastructure Availability</strong></td>
              <td>High-availability (99.99% uptime), redundant load balancers, auto-scaling.</td>
              <td>Ephemeral worker nodes; spun up on demand, shut down when job completes.</td>
            </tr>
            <tr>
              <td><strong>Failure Impact</strong></td>
              <td>High: individual user request fails immediately in the app UI.</td>
              <td>Low: failed batches can be cleanly restarted without user disruption.</td>
            </tr>
            <tr>
              <td><strong>Caching Strategy</strong></td>
              <td>In-memory Redis/Memcached stores for frequent feature vectors.</td>
              <td>Pre-computed predictions stored in database tables (e.g. PostgreSQL, BigQuery).</td>
            </tr>
            <tr>
              <td><strong>Cost Profile</strong></td>
              <td>Continuous hosting expenses (servers stay idle waiting for traffic).</td>
              <td>Predictable, spot-instance compute; costs scale strictly with data volume.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>6.2 Vectorized Batch Prediction in Python</h3>
      <p>
        Notice that batch inference does <em>not</em> mean calling an API in a <code>for</code> loop one row at a time! Calling a REST endpoint for 100,000 customers in a loop creates massive network overhead. Instead, high-throughput batch scoring loads the model once and evaluates thousands of rows concurrently via matrix operations:
      </p>

      <pre><code class="language-python">import joblib
import pandas as pd

# 1. Load the pre-trained pipeline once
pipeline = joblib.load("customer_churn_pipeline.joblib")

# 2. Ingest 50,000 customer records from database or data lake
batch_df = pd.read_parquet("overnight_customer_snapshot.parquet")
print(f"Scoring batch of {len(batch_df):,} customers...")

# 3. Vectorized scoring directly via pipeline:
# Entire batch is transformed and evaluated in a few seconds!
batch_df["churn_probability"] = pipeline.predict_proba(batch_df)[:, 1].round(4)
batch_df["predicted_churn"] = (batch_df["churn_probability"] >= 0.50).astype(int)

# 4. Save results to the operational marketing database
batch_df[["customer_id", "churn_probability", "predicted_churn"]].to_sql(
    "marketing_daily_churn_scores", 
    con=db_engine, 
    if_exists="replace", 
    index=False
)
print("Batch scoring completed successfully. Marketing campaigns ready for execution.")</code></pre>

      <div class="callout callout-tip">
        <div class="callout-title">💡 Important Clarification: Batch Prediction vs. Retraining</div>
        <p style="margin-bottom:0;">
          Beginners often confuse <em>batch scoring</em> with <em>model retraining</em>. Batch prediction does <strong>not</strong> update or adjust the model's weights. It simply passes a large batch of fresh rows through the frozen, pre-trained pipeline to calculate scores.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 07: LOCAL VS CLOUD DEPLOYMENT      -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-07">
      <div class="section-header">
        <span class="section-tag">Module 07 • Hosting Environments</span>
        <h2 class="section-title"><a href="#sec-07">7. Local Deployment vs. Cloud Deployment</a></h2>
      </div>

      <p>
        When you run <code>uvicorn app:app</code> on your computer, FastAPI listens on <code>http://127.0.0.1:8000</code>. This is known as <strong>localhost</strong>. While localhost is wonderful for interactive development, debugging, and rapid prototyping, it is strictly isolated to your personal machine.
      </p>

      <div class="diagram-container">
        __SVG_LOCAL_VS_CLOUD__
        <div class="diagram-caption">Figure 7.1: Localhost vs. Cloud Deployment Architecture. Localhost is accessible solely from your internal loopback network interface; cloud deployments expose a public domain through firewalls, load balancers, and container orchestration clusters.</div>
      </div>

      <h3>7.1 Why Localhost Cannot Serve Global Users</h3>
      <ul>
        <li><strong>No Public IP or DNS:</strong> Your laptop sits behind a home or office router performing Network Address Translation (NAT) and blocking inbound connection requests.</li>
        <li><strong>Sleep and Power Offs:</strong> If you close your laptop lid or disconnect your Wi-Fi, the prediction service immediately terminates.</li>
        <li><strong>Resource Contention:</strong> Running intensive games, video editing, or background builds on your workstation steals CPU cycles and RAM from the inference process.</li>
      </ul>

      <h3>7.2 Environment Comparison: Where Should You Deploy?</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Hosting Tier</th>
              <th>Setup Complexity</th>
              <th>Cost Considerations</th>
              <th>Accessibility</th>
              <th>Best Suited For</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Localhost (Developer Laptop)</strong></td>
              <td>Zero: run one Python terminal command.</td>
              <td>$0.00 completely free.</td>
              <td>Only your personal computer.</td>
              <td>Algorithm prototyping, writing unit tests, and local API verification.</td>
            </tr>
            <tr>
              <td><strong>Free / PaaS Cloud (Render, Hugging Face, Railway)</strong></td>
              <td>Low: connect GitHub repo and click deploy.</td>
              <td>Free tier available (with severe sleep &amp; RAM limits).</td>
              <td>Public HTTPS URL worldwide.</td>
              <td>Student portfolio demos, resume showcases, hackathons.</td>
            </tr>
            <tr>
              <td><strong>Virtual Private Server (VPS / DigitalOcean, Linode)</strong></td>
              <td>Medium: manage Linux OS, SSH, Nginx, and systemd.</td>
              <td>$5 to $20 fixed monthly fee.</td>
              <td>Public HTTPS URL with custom domain.</td>
              <td>Small startups, side projects, internal team tools.</td>
            </tr>
            <tr>
              <td><strong>Enterprise Cloud (AWS SageMaker, GCP Vertex AI, K8s)</strong></td>
              <td>High: IAM roles, VPC peering, Kubernetes YAML, CI/CD.</td>
              <td>Hundreds to thousands of dollars per month.</td>
              <td>Global high-availability, multi-region failover.</td>
              <td>Large enterprises processing millions of mission-critical transactions.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-warning">
        <div class="callout-title">⚠️ The Reality of Free-Tier Cloud Hosting</div>
        <p style="margin-bottom:0;">
          While free-tier platforms (such as Render, Fly.io, or Hugging Face Spaces) are fantastic for learning, be aware of their technical constraints: <strong>cold starts</strong> (your server takes 45–60 seconds to wake up after 15 minutes of inactivity), strict 512MB RAM ceilings (which will crash if loading large deep-learning models), and monthly usage hour caps. Never promise clients that free-tier infrastructure is a permanent production solution.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 08: DOCKER & CONTAINERS            -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-08">
      <div class="section-header">
        <span class="section-tag">Module 08 • Containerization</span>
        <h2 class="section-title"><a href="#sec-08">8. Introduction to Docker and Containers</a></h2>
      </div>

      <p>
        Every software developer eventually encounters the dreaded phrase: <em>"Well, it worked on my machine!"</em>
      </p>
      <p>
        In Machine Learning, this nightmare happens constantly. You develop a pipeline using Python 3.10, NumPy 1.24, and scikit-learn 1.3 on macOS. You then push your code to an Ubuntu production server running Python 3.11 with an older OpenBLAS C-library. Suddenly, your serialized model refuses to load with an cryptic <code>ModuleNotFoundError</code> or segmentation fault.
      </p>

      <div class="diagram-container">
        __SVG_DOCKER_CONTAINER__
        <div class="diagram-caption">Figure 8.1: Containerization with Docker. A Dockerfile provides the deterministic recipe to bake source code, Python runtimes, and system C-libraries into an immutable container image that runs identically on any operating system.</div>
      </div>

      <h3>8.1 What Is a Container?</h3>
      <p>
        Just as standardized steel shipping containers allow cargo ships to transport bananas, electronics, or furniture interchangeably without worrying about package shapes, a <strong>software container</strong> packages an entire application along with its operating system libraries, Python interpreter, environment variables, and dependencies into an isolated runtime sandbox.
      </p>
      <ul>
        <li><strong>Image:</strong> The immutable, frozen blueprint or recipe (like a class in programming).</li>
        <li><strong>Container:</strong> The live, running instance instantiated from that image (like an object in programming).</li>
        <li><strong>Dockerfile:</strong> A plain text file containing sequential instructions that Docker executes to construct the image.</li>
      </ul>

      <h3>8.2 A Beginner-Friendly Dockerfile for FastAPI</h3>
      <p>
        Here is a production-grade, minimal Dockerfile for our Customer Churn API:
      </p>

      <pre><code class="language-dockerfile"># 1. Base image: lightweight Python 3.10 Debian distribution
FROM python:3.10-slim

# 2. Set working directory inside the container filesystem
WORKDIR /app

# 3. Set environment variables for clean Python execution
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 4. Copy dependency specification first to leverage Docker layer caching
COPY requirements.txt .

# 5. Install dependencies without caching wheel archives to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application source code and trained model artifact
COPY app.py .
COPY customer_churn_pipeline.joblib .

# 7. Document the port the container listens on
EXPOSE 8000

# 8. Start the production Uvicorn web server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]</code></pre>

      <h3>8.3 Line-by-Line Instruction Walkthrough</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Instruction</th>
              <th>Technical Meaning</th>
              <th>Why It Matters for ML Deployment</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>FROM python:3.10-slim</code></td>
              <td>Inherits a sanitized, lightweight Linux image containing pre-compiled Python 3.10.</td>
              <td>Locks the exact minor Python version so numerical libraries compile consistently.</td>
            </tr>
            <tr>
              <td><code>WORKDIR /app</code></td>
              <td>Creates and sets the default execution directory inside the container.</td>
              <td>Prevents files from being scattered across the root Linux filesystem.</td>
            </tr>
            <tr>
              <td><code>COPY requirements.txt .</code></td>
              <td>Copies the list of Python packages into the container before copying code.</td>
              <td>Enables Docker layer caching: dependencies are not reinstalled on every code edit!</td>
            </tr>
            <tr>
              <td><code>RUN pip install ...</code></td>
              <td>Installs scikit-learn, FastAPI, and joblib in isolated container space.</td>
              <td>Ensures no dependency conflicts with the host computer's global packages.</td>
            </tr>
            <tr>
              <td><code>COPY . .</code></td>
              <td>Copies <code>app.py</code> and <code>customer_churn_pipeline.joblib</code>.</td>
              <td>Bakes the trained artifact directly into the immutable runtime image.</td>
            </tr>
            <tr>
              <td><code>CMD ["uvicorn", ...]</code></td>
              <td>The command executed when the container starts up.</td>
              <td>Binds to <code>0.0.0.0</code> so network traffic from outside the container reaches the app.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-important">
        <div class="callout-title">ℹ️ Docker Execution Status in Current Environment</div>
        <p style="margin-bottom:0;">
          <strong>Status: NOT TESTED (Docker CLI not installed on host machine).</strong><br>
          In professional enterprise environments, you would build and execute this image using <code>docker build -t churn-api:v1 .</code> and <code>docker run -p 8000:8000 churn-api:v1</code>. However, Docker is not required for completing our beginner local Python deployment exercises.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 09: WHAT IS MLOPS?                 -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-09">
      <div class="section-header">
        <span class="section-tag">Module 09 • Engineering Discipline</span>
        <h2 class="section-title"><a href="#sec-09">9. What Is MLOps?</a></h2>
      </div>

      <p>
        <strong>MLOps (Machine Learning Operations)</strong> is the systematic intersection of Machine Learning, DevOps, and Data Engineering. It encompasses the principles, automation pipelines, and cultural practices required to design, build, deploy, monitor, and govern production ML models reliably and efficiently.
      </p>

      <div class="diagram-container">
        __SVG_MLOPS_LIFECYCLE__
        <div class="diagram-caption">Figure 9.1: The MLOps Flywheel Lifecycle. Continuous iteration between data engineering, experiment tracking, pipeline validation, automated deployment gates, real-time observability, and governed retraining.</div>
      </div>

      <h3>9.1 Why Traditional DevOps Is Not Enough for Machine Learning</h3>
      <p>
        Traditional software engineering focuses on code: <code>Code &rarr; Build &rarr; Test &rarr; Release</code>. If the code is well-tested and doesn't change, the software works indefinitely.
      </p>
      <p>
        Machine Learning systems, however, are governed by a three-variable equation: <strong>Code + Data = Model</strong>.
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Traditional DevOps</th>
              <th>Production MLOps</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Primary Asset</strong></td>
              <td>Deterministic source code and compiled binaries.</td>
              <td>Code, massive non-deterministic datasets, and learned model artifacts.</td>
            </tr>
            <tr>
              <td><strong>Verification</strong></td>
              <td>Unit tests, integration tests, static code linting.</td>
              <td>Code tests + Data validation + Statistical drift checks + Model quality gates.</td>
            </tr>
            <tr>
              <td><strong>Degradation Mechanism</strong></td>
              <td>Software bugs introduced by human code modifications.</td>
              <td>Silent statistical drift: code remains 100% bug-free while accuracy degrades.</td>
            </tr>
            <tr>
              <td><strong>Monitoring Focus</strong></td>
              <td>Server health: CPU utilization, memory usage, HTTP error rates.</td>
              <td>Server health + Feature distributions + Output drift + Prediction confidence.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-tip">
        <div class="callout-title">💡 The Pragmatic Rule: Avoid Premature Over-Engineering</div>
        <p style="margin-bottom:0;">
          MLOps does <em>not</em> mean you must immediately deploy a 10-node Kubernetes cluster with automated daily retraining and Kafka streaming. The level of MLOps automation should match your project's business impact and risk. A simple model deployed on FastAPI with clean logging, scheduled validation, and a local version log is often 100% sufficient for small teams!
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 10: VERSIONING & EXPERIMENT LOG    -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-10">
      <div class="section-header">
        <span class="section-tag">Module 10 • Reproducibility</span>
        <h2 class="section-title"><a href="#sec-10">10. Model Versioning and Experiment Tracking</a></h2>
      </div>

      <p>
        Imagine a scenario: six months after deploying your customer churn model, a regulatory audit asks why a specific customer was denied an account upgrade. Can you reproduce the exact prediction? Do you know which dataset trained that model, which hyperparameters were used, which commit hash created it, and what library versions were active?
      </p>

      <div class="diagram-container">
        __SVG_EXPERIMENT_TRACKING__
        <div class="diagram-caption">Figure 10.1: The 4 Pillars of ML Reproducibility. True reproducibility requires tracking the exact Git commit, data snapshot hash, Python dependency manifest, and serialized model artifact simultaneously.</div>
      </div>

      <h3>10.1 Why File Naming Alone Is a Disaster</h3>
      <div class="callout callout-warning">
        <div class="callout-title">⚠️ The Anti-Pattern: Chaos by Filename</div>
        <p style="margin-bottom:0;">
          Never track models like this: <code>churn_model.joblib</code>, <code>churn_model_v2.joblib</code>, <code>churn_model_final.joblib</code>, <code>churn_model_final_MAYBE.joblib</code>. This provides zero visibility into hyperparameters, test scores, or training dates, and will inevitably lead to accidentally deploying an inferior or debug model to production.
        </p>
      </div>

      <h3>10.2 Simple, Reproducible Experiment Logging in Python</h3>
      <p>
        While enterprise platforms like <strong>MLflow</strong> or <strong>Weights &amp; Biases</strong> automate this, you can implement robust experiment logging with zero extra dependencies using a simple structured JSON or CSV ledger:
      </p>

      <pre><code class="language-python">import json
import os
import hashlib
from datetime import datetime

def log_experiment(model_name, hyperparams, metrics, artifact_path):
    # Logs an immutable record of an ML experiment run to disk.
    log_file = "experiments_ledger.json"
    
    # Calculate SHA-256 hash of the trained artifact for tamper detection
    with open(artifact_path, "rb") as f:
        artifact_hash = hashlib.sha256(f.read()).hexdigest()[:12]
        
    experiment_record = {
        "experiment_id": f"EXP_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "timestamp": datetime.now().isoformat(),
        "model_name": model_name,
        "artifact_path": artifact_path,
        "artifact_sha256": artifact_hash,
        "hyperparameters": hyperparams,
        "evaluation_metrics": metrics,
        "environment": {
            "python_version": "3.10.11",
            "sklearn_version": "1.3.0"
        }
    }
    
    # Append to JSON records
    records = []
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            records = json.load(f)
            
    records.append(experiment_record)
    with open(log_file, "w") as f:
        json.dump(records, f, indent=2)
        
    print(f"Logged experiment {experiment_record['experiment_id']} to {log_file}")</code></pre>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 11: DATA DRIFT VS CONCEPT DRIFT    -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-11">
      <div class="section-header">
        <span class="section-tag">Module 11 • Statistical Degradation</span>
        <h2 class="section-title"><a href="#sec-11">11. Data Drift and Concept Drift</a></h2>
      </div>

      <p>
        In traditional software, a function calculating compound interest continues to output accurate numbers forever. In Machine Learning, models begin degrading the moment they are deployed because the real world is constantly changing. This degradation manifests in two distinct forms:
      </p>

      <div class="diagram-container">
        __SVG_DATA_DRIFT__
        <div class="diagram-caption">Figure 11.1: Data Drift (Covariate Shift). The probability distribution of the input features P(X) shifts over time, but the underlying mathematical relationship between features and the target P(Y|X) remains unchanged.</div>
      </div>

      <div class="diagram-container">
        __SVG_CONCEPT_DRIFT__
        <div class="diagram-caption">Figure 11.2: Concept Drift. The statistical relationship between features and the target P(Y|X) fundamentally alters over time, rendering the trained decision boundary obsolete even if input values look similar.</div>
      </div>

      <h3>11.1 Understanding the Difference</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Drift Type</th>
              <th>Mathematical Definition</th>
              <th>Everyday Intuition</th>
              <th>Real-World Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Data Drift (Covariate Shift)</strong></td>
              <td><em>P(X)</em> changes,<br><em>P(Y | X)</em> is stable.</td>
              <td>The types of customers walking into your store change, but each customer behaves normally for their demographic.</td>
              <td>A marketing campaign brings younger users onto a streaming platform: average age drops from 45 to 22, but young users still churn at their historical baseline rate.</td>
            </tr>
            <tr>
              <td><strong>Concept Drift</strong></td>
              <td><em>P(Y | X)</em> changes,<br><em>P(X)</em> may be stable.</td>
              <td>The exact same customers walk into your store, but their spending behavior radically shifts due to outside events.</td>
              <td>A global pandemic or economic shock occurs: customers with identical incomes suddenly stop booking flights and begin hoarding cash.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-important">
        <div class="callout-title">⚠️ Vital Rule: Drift Does Not Automatically Equal Failure</div>
        <p style="margin-bottom:0;">
          Detecting a shift in an input feature's distribution (e.g. median monthly charges rising by 10% due to inflation) does <strong>not</strong> automatically mean the model's accuracy has collapsed. It simply means the model is operating in unfamiliar statistical territory. Retraining should be triggered when performance metrics on verified labels drop or when feature values move far outside the training distribution support.
        </p>
      </div>
    </section>
"""
