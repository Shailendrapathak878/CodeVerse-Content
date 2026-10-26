"""
Module: topic10_part4.py
Contains Sections 16 to 21 for Topic 10: Logistic Regression.
"""

from scratch.topic10_svgs import (
    SVG_PROBABILITY_CALIBRATION,
    SVG_LAB_EVALUATION_SCORECARD
)

PART4_HTML = f"""
    <!-- SECTION 16: CALIBRATION AND PROBABILITY INTERPRETATION -->
    <section id="sec-16" class="section-card">
      <span class="section-badge">Section 16</span>
      <h2 class="section-title">Calibration and Probability Interpretation</h2>
      <p class="section-lead">
        When a machine learning model outputs a prediction of <code>p = 0.80</code>, what does that number actually signify? Does it mean the positive outcome is guaranteed, or that the model is &ldquo;80% sure&rdquo;?
      </p>

      <div class="callout card-definition">
        <div class="callout-title">&#128214; The Strict Statistical Meaning of Calibration</div>
        <p>
          A model is <strong>well-calibrated</strong> if predicted probabilities match empirical long-run frequencies.
        </p>
        <p>
          Specifically: If you take 1,000 historical patients who were each assigned an estimated probability of <code>p &approx; 0.80</code>, exactly 800 of those patients should truly have the positive medical condition.
        </p>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_PROBABILITY_CALIBRATION}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.13: Probability Calibration Reliability Diagram.</strong> The diagonal dashed green line represents perfect calibration. Logistic Regression (purple line) naturally hugs this diagonal because it minimizes binary cross-entropy.
        </div>
        <div class="svg-takeaway">
          &#10004; Architectural Advantage: Because Logistic Regression minimizes Log Loss, its raw output probabilities are naturally well-calibrated compared to Naive Bayes or decision trees.
        </div>
      </div>

      <h3 class="sub-title">Discrimination vs. Calibration: Two Different Goals</h3>
      <p>
        A critical insight in advanced machine learning is that <strong>discrimination</strong> and <strong>calibration</strong> are two distinct model qualities:
      </p>
      <ul>
        <li>
          <strong>Discrimination (Measured by ROC AUC):</strong> Can the model correctly rank positive cases above negative cases? A model that outputs <code>p = 0.99</code> for all positives and <code>p = 0.98</code> for all negatives has a perfect <strong>AUC of 1.00</strong>, but its probabilities are terribly uncalibrated!
        </li>
        <li>
          <strong>Calibration (Measured by Brier Score / Log Loss):</strong> Do the numerical probabilities reflect real-world event frequencies? In clinical medicine, insurance pricing, and financial credit risk, calibration is mandatory.
        </li>
      </ul>
    </section>

    <!-- SECTION 17: COMPLETE PYTHON PRACTICAL LAB -->
    <section id="sec-17" class="section-card">
      <span class="section-badge">Section 17</span>
      <h2 class="section-title">Complete Python Practical Lab</h2>
      <p class="section-lead">
        In this end-to-end practical laboratory, we build a production-grade, leak-free binary classification pipeline using scikit-learn on a synthetic dataset of 200 university students.
      </p>

      <div class="callout card-success">
        <div class="callout-title">&#10004; Laboratory Architecture &amp; Anti-Leakage Safeguards</div>
        <ul>
          <li><strong>Stratified Train/Test Split:</strong> Preserves exact 41% Fail / 59% Pass ratio across both training (160) and test (40) splits.</li>
          <li><strong>Zero Data Leakage:</strong> <code>StandardScaler</code> is nested inside a scikit-learn <code>Pipeline</code> so mean and standard deviation are fitted exclusively on training data.</li>
          <li><strong>Clean Metric Validation:</strong> All test predictions, confusion matrices, and ROC metrics are calculated on unseen holdout test samples.</li>
        </ul>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_LAB_EVALUATION_SCORECARD}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.14: Practical Lab Test Evaluation Scorecard.</strong> Performance achieved on the 40 holdout test students: 95.00% Accuracy, 100.00% Precision, 91.67% Recall, 95.65% F1-Score, and 1.0000 ROC AUC.
        </div>
      </div>

      <h3 class="sub-title">Complete Executable Python Source Code</h3>
      <div class="code-block">
        <div class="code-header">
          <span class="code-title">&#128013; topic10_logistic_regression_lab.py &bull; Verified Production Code</span>
          <span class="code-lang">Python 3</span>
        </div>
        <pre><code>import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, classification_report
)

# =====================================================================
# 1. GENERATE REPRODUCIBLE DATASET (200 Students)
# =====================================================================
np.random.seed(42)
n_students = 200

# Continuous input features
study_hours = np.random.uniform(3.0, 28.0, n_students)       # Weekly study hours
attendance = np.random.uniform(45.0, 99.0, n_students)       # Lecture attendance %
prev_score = np.random.uniform(48.0, 95.0, n_students)       # Prior exam score
assignments = np.random.randint(1, 11, n_students)           # Completed homeworks (1-10)

# Latent log-odds model (intercept tuned to -11.0 for balanced classes)
z_latent = (
    -11.0
    + (0.18 * study_hours)
    + (0.045 * attendance)
    + (0.050 * prev_score)
    + (0.35 * assignments)
    + np.random.normal(0, 0.5, n_students)
)
true_probs = 1.0 / (1.0 + np.exp(-z_latent))
passed = (true_probs >= 0.50).astype(int)

df = pd.DataFrame({{
    'Student_ID': [f'STU-{{i:04d}}' for i in range(1, n_students + 1)],
    'Study_Hours': np.round(study_hours, 1),
    'Attendance_Pct': np.round(attendance, 1),
    'Previous_Score': np.round(prev_score, 1),
    'Assignments_Done': assignments,
    'Passed_Exam': passed
}})

print(f"Dataset Shape: {{df.shape}}")
print(f"Class Distribution: Fail = {{np.sum(passed == 0)}} ({{np.mean(passed == 0):.1%}}), "
      f"Pass = {{np.sum(passed == 1)}} ({{np.mean(passed == 1):.1%}})")

# =====================================================================
# 2. STRATIFIED TRAIN / TEST SPLIT (80% Train / 20% Test)
# =====================================================================
train_df, test_df = train_test_split(
    df, test_size=0.20, random_state=42, stratify=df['Passed_Exam']
)

# Assert zero leakage
overlap = set(train_df['Student_ID']).intersection(set(test_df['Student_ID']))
assert len(overlap) == 0, "Data Leakage: Overlapping student records!"

feature_cols = ['Study_Hours', 'Attendance_Pct', 'Previous_Score', 'Assignments_Done']
X_train, y_train = train_df[feature_cols], train_df['Passed_Exam']
X_test, y_test = test_df[feature_cols], test_df['Passed_Exam']

print(f"Train samples: {{len(X_train)}}, Test samples: {{len(X_test)}}")

# =====================================================================
# 3. BUILD LEAK-FREE PIPELINE (Scaler + Logistic Regression)
# =====================================================================
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(random_state=42, C=1.0))
])

# Fit strictly on training data
pipe.fit(X_train, y_train)

# Assert scaler mean equals training mean (never touched test set!)
scaler = pipe.named_steps['scaler']
assert np.allclose(scaler.mean_, X_train.mean(axis=0))
print("[PASS] Scaler fitted strictly on training data.")

# =====================================================================
# 4. PREDICTIONS AND EVALUATION ON UNSEEN TEST SET
# =====================================================================
test_probs = pipe.predict_proba(X_test)[:, 1]
test_preds = pipe.predict(X_test)

# Verify probability bounds
assert np.all((test_probs >= 0.0) & (test_probs <= 1.0))

acc = accuracy_score(y_test, test_preds)
prec = precision_score(y_test, test_preds)
rec = recall_score(y_test, test_preds)
f1 = f1_score(y_test, test_preds)
auc = roc_auc_score(y_test, test_probs)
cm = confusion_matrix(y_test, test_preds)

print("\\n" + "="*50)
print("TEST SET EVALUATION METRICS (N = 40)")
print("="*50)
print(f"Test Accuracy:  {{acc:.4f}} ({{acc:.1%}})")
print(f"Test Precision: {{prec:.4f}} ({{prec:.1%}})")
print(f"Test Recall:    {{rec:.4f}} ({{rec:.1%}})")
print(f"Test F1-Score:  {{f1:.4f}} ({{f1:.1%}})")
print(f"Test ROC AUC:   {{auc:.4f}} ({{auc:.1%}})")
print("\\nTest Confusion Matrix:")
print(cm)

# =====================================================================
# 5. MODEL INTERPRETATION (Coefficients & Odds Ratios)
# =====================================================================
model = pipe.named_steps['logreg']
print(f"\\nFitted Intercept (&beta;0): {{model.intercept_[0]:+.4f}}")
print("Standardized Feature Coefficients:")
for col, coef in zip(feature_cols, model.coef_[0]):
    odds_ratio = np.exp(coef)
    print(f"  {{col:18s}}: {{coef:+.4f}} (Odds Ratio: {{odds_ratio:.4f}})")

# =====================================================================
# 6. REGULARIZATION COMPARISON (C Parameter)
# =====================================================================
pipe_c_small = Pipeline([('scaler', StandardScaler()), ('logreg', LogisticRegression(C=0.01, random_state=42))])
pipe_c_large = Pipeline([('scaler', StandardScaler()), ('logreg', LogisticRegression(C=100.0, random_state=42))])

pipe_c_small.fit(X_train, y_train)
pipe_c_large.fit(X_train, y_train)

w_small = np.linalg.norm(pipe_c_small.named_steps['logreg'].coef_[0])
w_mid = np.linalg.norm(model.coef_[0])
w_large = np.linalg.norm(pipe_c_large.named_steps['logreg'].coef_[0])

print(f"\\nRegularization Weight Norms:")
print(f"  C = 0.01 (Heavy Penalty): ||w|| = {{w_small:.4f}}")
print(f"  C = 1.00 (Default):       ||w|| = {{w_mid:.4f}}")
print(f"  C = 100  (Weak Penalty):  ||w|| = {{w_large:.4f}}")
assert w_small < w_large, "Small C must produce smaller weight magnitude!"
print("[PASS] All practical lab pipeline tests passed successfully!")</code></pre>
      </div>
    </section>

    <!-- SECTION 18: REAL-LIFE CASE STUDIES -->
    <section id="sec-18" class="section-card">
      <span class="section-badge">Section 18</span>
      <h2 class="section-title">Real-Life Case Studies</h2>
      <p class="section-lead">
        To build intuition for how Logistic Regression functions in production, examine four diverse real-world case studies spanning security, commerce, finance, and education.
      </p>

      <!-- Case A -->
      <h3 class="sub-title">&#128231; Case Study A: Email Spam Detection</h3>
      <div class="table-wrapper">
        <table>
          <tbody>
            <tr>
              <td><strong>Problem Statement</strong></td>
              <td>Filter incoming email messages into Inbox (Class 0: Ham) vs. Junk Folder (Class 1: Spam).</td>
            </tr>
            <tr>
              <td><strong>Input Features</strong></td>
              <td>Frequency of words (<em>&ldquo;free&rdquo;</em>, <em>&ldquo;cash&rdquo;</em>, <em>&ldquo;urgent&rdquo;</em>), presence of suspicious URLs, DKIM verification status, sender domain age.</td>
            </tr>
            <tr>
              <td><strong>Why Logistic Regression?</strong></td>
              <td>Fast inference (&lt; 1 ms per email), handles high-dimensional sparse text vectors, and outputs calibrated probabilities for threshold tuning.</td>
            </tr>
            <tr>
              <td><strong>Critical Metric &amp; Threshold</strong></td>
              <td><strong>Precision is King!</strong> A False Positive (diverting an important business or tax email to spam) causes severe harm. Engineers set <code>&tau; = 0.85</code>.</td>
            </tr>
            <tr>
              <td><strong>Limitations &amp; Ethics</strong></td>
              <td>Spammers continually evolve phrasing (adversarial concept drift), requiring continuous model retraining.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Case B -->
      <h3 class="sub-title">&#128188; Case Study B: Customer Churn Prediction</h3>
      <div class="table-wrapper">
        <table>
          <tbody>
            <tr>
              <td><strong>Problem Statement</strong></td>
              <td>Predict whether a SaaS subscriber will cancel their monthly subscription within the next 30 days.</td>
            </tr>
            <tr>
              <td><strong>Input Features</strong></td>
              <td>Login frequency drop, open unresolved support tickets, contract duration, monthly spend, days since last feature use.</td>
            </tr>
            <tr>
              <td><strong>Why Logistic Regression?</strong></td>
              <td>Coefficients directly explain <em>why</em> customers churn, allowing customer success teams to intervene proactively.</td>
            </tr>
            <tr>
              <td><strong>Critical Metric &amp; Threshold</strong></td>
              <td><strong>Recall &amp; F1-Score:</strong> Missing an at-risk customer (False Negative) loses thousands in annual recurring revenue. Threshold tuned to <code>&tau; = 0.40</code>.</td>
            </tr>
            <tr>
              <td><strong>Limitations &amp; Ethics</strong></td>
              <td>Avoid offering discounts only to high churn risks if it incentivizes customers to artificially reduce usage.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Case C -->
      <h3 class="sub-title">&#128179; Case Study C: Financial Credit Card Fraud Detection</h3>
      <div class="table-wrapper">
        <table>
          <tbody>
            <tr>
              <td><strong>Problem Statement</strong></td>
              <td>Flag unauthorized credit card transactions in real-time before merchant settlement.</td>
            </tr>
            <tr>
              <td><strong>Input Features</strong></td>
              <td>Transaction amount, merchant category code, geographical distance from last swipe, velocity (swipes in past hour).</td>
            </tr>
            <tr>
              <td><strong>Why Logistic Regression?</strong></td>
              <td>Extremely low computational latency required for payment gateway authorization (&lt; 50 ms).</td>
            </tr>
            <tr>
              <td><strong>Critical Metric &amp; Threshold</strong></td>
              <td><strong>Recall &amp; Precision-Recall AUC (PR-AUC):</strong> Heavy class imbalance (99.8% legitimate vs. 0.2% fraud). Accuracy is completely meaningless.</td>
            </tr>
            <tr>
              <td><strong>Limitations &amp; Ethics</strong></td>
              <td>Frequent false alarms freeze cards while cardholders travel, causing embarrassment and churn.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Case D -->
      <h3 class="sub-title">&#127891; Case Study D: University Course Exam Pass/Fail</h3>
      <div class="table-wrapper">
        <table>
          <tbody>
            <tr>
              <td><strong>Problem Statement</strong></td>
              <td>Identify students at risk of failing mid-semester so academic advisors can provide tutoring.</td>
            </tr>
            <tr>
              <td><strong>Input Features</strong></td>
              <td>Weekly study hours, lecture attendance percentage, previous prerequisite score, completed assignments.</td>
            </tr>
            <tr>
              <td><strong>Why Logistic Regression?</strong></td>
              <td>Interpretable coefficients provide transparent advice: <em>&ldquo;Completing 2 more assignments triples your pass odds.&rdquo;</em></td>
            </tr>
            <tr>
              <td><strong>Critical Metric &amp; Threshold</strong></td>
              <td><strong>Balanced F1-Score:</strong> Balanced classes allow standard threshold <code>&tau; = 0.50</code> with high overall accuracy (95.0%).</td>
            </tr>
            <tr>
              <td><strong>Limitations &amp; Ethics</strong></td>
              <td>Model predictions must never be used to discourage students or deny enrollment opportunities.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 19: KEY VISUALIZATIONS & GRAPHS -->
    <section id="sec-19" class="section-card">
      <span class="section-badge">Section 19</span>
      <h2 class="section-title">Key Visualizations &amp; Graphic Gallery</h2>
      <p class="section-lead">
        Visual learning reinforces deep mathematical understanding. Below is a complete visual index of the 14 core diagrams embedded across this chapter:
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Figure #</th>
              <th>Diagram Title</th>
              <th>Core Educational Purpose</th>
              <th>Key Takeaway</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>10.1</strong></td>
              <td>Logistic Architecture Hero</td>
              <td>4-stage pipeline: X &rarr; z &rarr; &sigma;(z) &rarr; &tau; &rarr; &#375;</td>
              <td>Models class probability, not hard labels directly.</td>
            </tr>
            <tr>
              <td><strong>10.2</strong></td>
              <td>Linear vs. Sigmoid Fit</td>
              <td>Demonstrates out-of-bounds probability violations.</td>
              <td>Linear models yield &lt;0 or &gt;1; sigmoid binds to (0, 1).</td>
            </tr>
            <tr>
              <td><strong>10.3</strong></td>
              <td>Sigmoid Curve &amp; Asymptotes</td>
              <td>Geometry, center point (0, 0.5), and saturation.</td>
              <td>Symmetry: <code>&sigma;(z) + &sigma;(-z) = 1.0</code>.</td>
            </tr>
            <tr>
              <td><strong>10.4</strong></td>
              <td>Probability &rarr; Odds &rarr; Logit</td>
              <td>Mathematical bridge across likelihood spaces.</td>
              <td>Log-odds map bounded probability onto continuous real space.</td>
            </tr>
            <tr>
              <td><strong>10.5</strong></td>
              <td>Threshold Shifting (&tau;)</td>
              <td>Compares classifications under &tau; = 0.3, 0.5, 0.7.</td>
              <td>Lower &tau; boosts Recall; higher &tau; boosts Precision.</td>
            </tr>
            <tr>
              <td><strong>10.6</strong></td>
              <td>1D &amp; 2D Decision Boundaries</td>
              <td>Cutoff point in 1D vs. dividing line in 2D space.</td>
              <td>Standard boundary is linear: <code>&beta;<sub>0</sub> + &sum; &beta;<sub>j</sub>x<sub>j</sub> = 0</code>.</td>
            </tr>
            <tr>
              <td><strong>10.7</strong></td>
              <td>Binary Log Loss Curves</td>
              <td>Penalties for positive and negative examples.</td>
              <td>Confident incorrect predictions incur 21.8&times; penalty.</td>
            </tr>
            <tr>
              <td><strong>10.8</strong></td>
              <td>Regularization L2 &amp; C Parameter</td>
              <td>Weight shrinkage under C = 0.01, 1.0, 100.0.</td>
              <td>Smaller C = stronger penalty = smaller weights.</td>
            </tr>
            <tr>
              <td><strong>10.9</strong></td>
              <td>Confusion Matrix Heatmap</td>
              <td>2&times;2 grid showing TP, FN, FP, TN (N=100).</td>
              <td>Inspect all four cells before trusting accuracy.</td>
            </tr>
            <tr>
              <td><strong>10.10</strong></td>
              <td>Precision-Recall Trade-off</td>
              <td>Inverse relationship as threshold shifts 0 to 1.</td>
              <td>Cannot simultaneously maximize Precision and Recall.</td>
            </tr>
            <tr>
              <td><strong>10.11</strong></td>
              <td>ROC Curve &amp; AUC Area</td>
              <td>TPR vs. FPR across all operating thresholds.</td>
              <td>Measures global ranking discrimination (AUC &approx; 1.00).</td>
            </tr>
            <tr>
              <td><strong>10.12</strong></td>
              <td>Class Imbalance Illusion</td>
              <td>95% normal vs. 5% fraud dummy classifier trap.</td>
              <td>A dumb model scores 95% accuracy while catching 0% fraud.</td>
            </tr>
            <tr>
              <td><strong>10.13</strong></td>
              <td>Probability Calibration</td>
              <td>Reliability diagram comparing observed vs. predicted.</td>
              <td>Logistic regression is naturally well-calibrated.</td>
            </tr>
            <tr>
              <td><strong>10.14</strong></td>
              <td>Lab Scorecard &amp; Metrics</td>
              <td>Verified test metrics on 40 holdout test students.</td>
              <td>95.0% Accuracy, 100% Precision, 91.7% Recall, 95.7% F1.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 20: 18 COMMON BEGINNER MISTAKES -->
    <section id="sec-20" class="section-card">
      <span class="section-badge">Section 20</span>
      <h2 class="section-title">18 Common Beginner Mistakes &amp; How to Avoid Them</h2>
      <p class="section-lead">
        Avoid these eighteen frequent conceptual, mathematical, and implementation traps when building classification models:
      </p>

      <div class="step-list">
        <!-- Mistake 1 -->
        <div class="step-card">
          <div class="step-number">1</div>
          <div class="step-body">
            <h4>Thinking Logistic Regression Is Ordinary Linear Regression</h4>
            <p><strong>The Mistake:</strong> Assuming the model fits a straight line directly to binary target labels.</p>
            <p><strong>The Fix:</strong> Understand that Logistic Regression fits a linear equation to <em>log-odds</em>, which is transformed into probabilities via the non-linear sigmoid function.</p>
          </div>
        </div>

        <!-- Mistake 2 -->
        <div class="step-card">
          <div class="step-number">2</div>
          <div class="step-body">
            <h4>Confusing Regression with Classification</h4>
            <p><strong>The Mistake:</strong> Using Mean Squared Error (MSE) or R<sup>2</sup> to evaluate classification quality.</p>
            <p><strong>The Fix:</strong> Use classification metrics: Accuracy, Precision, Recall, F1-Score, Confusion Matrix, and ROC AUC.</p>
          </div>
        </div>

        <!-- Mistake 3 -->
        <div class="step-card">
          <div class="step-number">3</div>
          <div class="step-body">
            <h4>Assuming the Model Directly Outputs Discrete Hard Classes</h4>
            <p><strong>The Mistake:</strong> Treating predictions as purely categorical without recognizing the underlying continuous probability.</p>
            <p><strong>The Fix:</strong> Use <code>model.predict_proba(X)</code> to access rich, calibrated class probabilities before applying thresholds.</p>
          </div>
        </div>

        <!-- Mistake 4 -->
        <div class="step-card">
          <div class="step-number">4</div>
          <div class="step-body">
            <h4>Believing Sigmoid Output Equals a Guaranteed Outcome</h4>
            <p><strong>The Mistake:</strong> Treating <code>p = 0.90</code> as certainty.</p>
            <p><strong>The Fix:</strong> Recognize that probabilities represent statistical likelihoods under model assumptions; 10% of such cases will still fail.</p>
          </div>
        </div>

        <!-- Mistake 5 -->
        <div class="step-card">
          <div class="step-number">5</div>
          <div class="step-body">
            <h4>Confusing Probability with Odds</h4>
            <p><strong>The Mistake:</strong> Saying an odds of 4.0 means an 80% chance or vice-versa.</p>
            <p><strong>The Fix:</strong> Remember <code>Odds = p / (1 - p)</code>. For <code>p = 0.80</code>, <code>Odds = 4.0</code> (4 to 1).</p>
          </div>
        </div>

        <!-- Mistake 6 -->
        <div class="step-card">
          <div class="step-number">6</div>
          <div class="step-body">
            <h4>Confusing Log-Odds with Probability</h4>
            <p><strong>The Mistake:</strong> Interpreting linear score <code>z = +1.386</code> directly as a percentage.</p>
            <p><strong>The Fix:</strong> Apply the sigmoid transformation <code>&sigma;(z)</code> to convert log-odds into true probabilities.</p>
          </div>
        </div>

        <!-- Mistake 7 -->
        <div class="step-card">
          <div class="step-number">7</div>
          <div class="step-body">
            <h4>Blindly Assuming &tau; = 0.50 Is Always the Best Threshold</h4>
            <p><strong>The Mistake:</strong> Never adjusting the threshold in cost-sensitive domains like medical diagnosis or fraud.</p>
            <p><strong>The Fix:</strong> Tune the operating threshold on validation data to balance the real-world costs of False Positives vs. False Negatives.</p>
          </div>
        </div>

        <!-- Mistake 8 -->
        <div class="step-card">
          <div class="step-number">8</div>
          <div class="step-body">
            <h4>Relying on Accuracy Alone for Imbalanced Datasets</h4>
            <p><strong>The Mistake:</strong> Celebrating a 99% accuracy on a dataset where 99% of samples are negative.</p>
            <p><strong>The Fix:</strong> Evaluate Recall, Precision, PR-AUC, and the Confusion Matrix.</p>
          </div>
        </div>

        <!-- Mistake 9 -->
        <div class="step-card">
          <div class="step-number">9</div>
          <div class="step-body">
            <h4>Confusing Precision with Recall</h4>
            <p><strong>The Mistake:</strong> Forgetting which metric evaluates false alarms vs. missed positives.</p>
            <p><strong>The Fix:</strong> <em>Precision</em> = How clean are your alarms? (TP / (TP+FP)); <em>Recall</em> = Did you catch all positive cases? (TP / (TP+FN)).</p>
          </div>
        </div>

        <!-- Mistake 10 -->
        <div class="step-card">
          <div class="step-number">10</div>
          <div class="step-body">
            <h4>Reversing False Positives and False Negatives</h4>
            <p><strong>The Mistake:</strong> Swapping Type I and Type II errors during business reviews.</p>
            <p><strong>The Fix:</strong> False Positive = False Alarm (healthy labeled sick); False Negative = Missed Event (sick labeled healthy).</p>
          </div>
        </div>

        <!-- Mistake 11 -->
        <div class="step-card">
          <div class="step-number">11</div>
          <div class="step-body">
            <h4>Calculating Evaluation Metrics on Training Data Only</h4>
            <p><strong>The Mistake:</strong> Reporting training accuracy as expected production performance.</p>
            <p><strong>The Fix:</strong> Always evaluate on an untouched, holdout test dataset or via cross-validation.</p>
          </div>
        </div>

        <!-- Mistake 12 -->
        <div class="step-card">
          <div class="step-number">12</div>
          <div class="step-body">
            <h4>Fitting Feature Scalers Before Splitting Data (Data Leakage)</h4>
            <p><strong>The Mistake:</strong> Calling <code>scaler.fit(df)</code> on the entire dataset before <code>train_test_split</code>.</p>
            <p><strong>The Fix:</strong> Use a scikit-learn <code>Pipeline</code> so <code>StandardScaler</code> is fitted exclusively on training samples.</p>
          </div>
        </div>

        <!-- Mistake 13 -->
        <div class="step-card">
          <div class="step-number">13</div>
          <div class="step-body">
            <h4>Tuning the Decision Threshold on the Test Set</h4>
            <p><strong>The Mistake:</strong> Trying multiple thresholds on test data and picking the one with highest accuracy.</p>
            <p><strong>The Fix:</strong> This causes test-set overfitting! Optimize the threshold on a validation split, then test once on the test set.</p>
          </div>
        </div>

        <!-- Mistake 14 -->
        <div class="step-card">
          <div class="step-number">14</div>
          <div class="step-body">
            <h4>Treating Model Coefficients as Proof of Causal Relationships</h4>
            <p><strong>The Mistake:</strong> Claiming feature <code>X</code> causes outcome <code>y</code> because its coefficient is positive.</p>
            <p><strong>The Fix:</strong> Observational regression proves statistical association, not causality. Confounding variables may be present.</p>
          </div>
        </div>

        <!-- Mistake 15 -->
        <div class="step-card">
          <div class="step-number">15</div>
          <div class="step-body">
            <h4>Assuming High ROC AUC Guarantees Good Probability Calibration</h4>
            <p><strong>The Mistake:</strong> Believing a model with AUC = 0.95 outputs trustworthy probabilities.</p>
            <p><strong>The Fix:</strong> AUC measures ranking order only. Inspect reliability diagrams and Brier score to verify probability calibration.</p>
          </div>
        </div>

        <!-- Mistake 16 -->
        <div class="step-card">
          <div class="step-number">16</div>
          <div class="step-body">
            <h4>Ignoring Regularization and Scikit-Learn&rsquo;s C Parameter</h4>
            <p><strong>The Mistake:</strong> Leaving <code>C=1.0</code> unexamined when working with collinear or high-dimensional features.</p>
            <p><strong>The Fix:</strong> Tune <code>C</code> using <code>GridSearchCV</code> or <code>LogisticRegressionCV</code> to find the optimal regularization strength.</p>
          </div>
        </div>

        <!-- Mistake 17 -->
        <div class="step-card">
          <div class="step-number">17</div>
          <div class="step-body">
            <h4>Interpreting Synthetic Benchmark Performance as Real-World Accuracy</h4>
            <p><strong>The Mistake:</strong> Assuming a 95% test score on clean synthetic data guarantees 95% in messy production.</p>
            <p><strong>The Fix:</strong> Real-world data contains noise, missing entries, label errors, and distribution shifts. Always validate in shadow mode.</p>
          </div>
        </div>

        <!-- Mistake 18 -->
        <div class="step-card">
          <div class="step-number">18</div>
          <div class="step-body">
            <h4>Ignoring the Unequal Business Costs of Classification Errors</h4>
            <p><strong>The Mistake:</strong> Optimizing purely for mathematical symmetry when business losses are heavily asymmetric.</p>
            <p><strong>The Fix:</strong> Calculate expected cost: <code>Cost = (FP &times; Cost<sub>FP</sub>) + (FN &times; Cost<sub>FN</sub>)</code> and pick the threshold minimizing total dollar loss.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 21: GLOSSARY, SUMMARY AND REVISION -->
    <section id="sec-21" class="section-card">
      <span class="section-badge">Section 21</span>
      <h2 class="section-title">Glossary, Checklist &amp; Comprehensive Revision</h2>
      <p class="section-lead">
        Consolidate your knowledge with a complete chapter summary, training checklist, technical glossary, and interactive revision problems.
      </p>

      <h3 class="sub-title">&#128221; 10-Point Chapter Summary</h3>
      <ol>
        <li><strong>Classification vs Regression:</strong> Regression predicts continuous quantities; Classification categorizes observations into discrete qualitative classes.</li>
        <li><strong>The Name Paradox:</strong> Logistic regression is a classification model that computes an internal linear regression score and filters it through a sigmoid function.</li>
        <li><strong>The Sigmoid Function:</strong> <code>&sigma;(z) = 1 / (1 + e<sup>-z</sup>)</code> compresses any real number into a valid probability strictly within (0, 1).</li>
        <li><strong>Odds &amp; Logits:</strong> Odds represent <code>p / (1 - p)</code>. Taking the natural log yields the logit, which scales linearly with input features.</li>
        <li><strong>Odds Ratio:</strong> <code>e<sup>&beta;<sub>j</sub></sup></code> represents the multiplicative change in the odds of the positive outcome per unit increase in feature <code>x<sub>j</sub></code>.</li>
        <li><strong>Decision Boundary:</strong> Standard Logistic Regression produces a linear boundary in the original feature space: <code>&beta;<sub>0</sub> + &sum; &beta;<sub>j</sub>x<sub>j</sub> = 0</code>.</li>
        <li><strong>Log Loss (Binary Cross-Entropy):</strong> Minimizes negative log-likelihood, heavily penalizing confident wrong predictions exponentially.</li>
        <li><strong>Confusion Matrix:</strong> Decomposes predictions into TP, FN, FP, and TN. Accuracy alone is dangerous on imbalanced datasets.</li>
        <li><strong>ROC &amp; AUC:</strong> Plots Recall vs. False Positive Rate across all thresholds. AUC measures ranking discrimination (0.5 = coin flip; 1.0 = perfect).</li>
        <li><strong>Production Anti-Leakage:</strong> Always bundle feature scalers and models inside a scikit-learn <code>Pipeline</code> to prevent data leakage from test data.</li>
      </ol>

      <h3 class="sub-title">&#9745; The 8-Step Training &amp; Evaluation Checklist</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Step #</th>
              <th>Action Item</th>
              <th>Verification Test</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>Inspect Class Balance</td>
              <td>Check positive class ratio (e.g., 50/50 vs 99/1). Plan evaluation metric accordingly.</td>
            </tr>
            <tr>
              <td>2</td>
              <td>Split Data First</td>
              <td>Execute stratified <code>train_test_split</code>. Verify 0 shared sample IDs.</td>
            </tr>
            <tr>
              <td>3</td>
              <td>Enforce Pipeline Encapsulation</td>
              <td>Bundle <code>StandardScaler</code> and <code>LogisticRegression</code> inside <code>Pipeline</code>.</td>
            </tr>
            <tr>
              <td>4</td>
              <td>Fit on Training Only</td>
              <td>Call <code>pipeline.fit(X_train, y_train)</code>. Never call fit on test data!</td>
            </tr>
            <tr>
              <td>5</td>
              <td>Inspect Probabilities</td>
              <td>Verify <code>0.0 &le; test_probs &le; 1.0</code> and check distribution spread.</td>
            </tr>
            <tr>
              <td>6</td>
              <td>Compute Full Confusion Matrix</td>
              <td>Print TP, FN, FP, and TN counts on unseen test samples.</td>
            </tr>
            <tr>
              <td>7</td>
              <td>Assess Precision, Recall &amp; F1</td>
              <td>Ensure metrics align with business error costs.</td>
            </tr>
            <tr>
              <td>8</td>
              <td>Tune Threshold on Validation Set</td>
              <td>Adjust &tau; if domain requires higher recall or higher precision. Never tune on test set!</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">&#128218; Comprehensive Technical Glossary (16 Terms)</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Term</th>
              <th>Concise Definition</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Binary Classification</strong></td>
              <td>Supervised machine learning where the target variable has exactly two discrete classes (0 and 1).</td>
            </tr>
            <tr>
              <td><strong>Sigmoid Function</strong></td>
              <td>S-shaped activation function <code>1 / (1 + e<sup>-z</sup>)</code> mapping (-&infin;, +&infin;) into (0, 1).</td>
            </tr>
            <tr>
              <td><strong>Linear Score (z)</strong></td>
              <td>Unbounded weighted sum of input features: <code>z = &beta;<sub>0</sub> + &sum; &beta;<sub>j</sub>x<sub>j</sub></code>.</td>
            </tr>
            <tr>
              <td><strong>Odds</strong></td>
              <td>Ratio of success probability to failure probability: <code>p / (1 - p)</code>.</td>
            </tr>
            <tr>
              <td><strong>Log-Odds (Logit)</strong></td>
              <td>Natural logarithm of the odds: <code>ln(p / (1 - p))</code>. Scales linearly with features.</td>
            </tr>
            <tr>
              <td><strong>Odds Ratio (OR)</strong></td>
              <td>Multiplicative change in odds per 1-unit feature increase: <code>e<sup>&beta;<sub>j</sub></sup></code>.</td>
            </tr>
            <tr>
              <td><strong>Decision Threshold (&tau;)</strong></td>
              <td>Probability cutoff (default 0.50) converting estimated probabilities into discrete class labels.</td>
            </tr>
            <tr>
              <td><strong>Decision Boundary</strong></td>
              <td>Geometric surface where <code>P(y=1|x) = &tau;</code> (or <code>z = 0</code> at &tau;=0.50).</td>
            </tr>
            <tr>
              <td><strong>Log Loss</strong></td>
              <td>Binary cross-entropy loss function penalizing probability errors exponentially.</td>
            </tr>
            <tr>
              <td><strong>Maximum Likelihood</strong></td>
              <td>Optimization method finding parameters that maximize the probability of observed training data.</td>
            </tr>
            <tr>
              <td><strong>Confusion Matrix</strong></td>
              <td>2&times;2 contingency table cross-tabulating actual ground truth vs. predicted classes.</td>
            </tr>
            <tr>
              <td><strong>Precision</strong></td>
              <td>Fraction of positive predictions that were correct: <code>TP / (TP + FP)</code>.</td>
            </tr>
            <tr>
              <td><strong>Recall (Sensitivity)</strong></td>
              <td>Fraction of true positive cases caught by model: <code>TP / (TP + FN)</code>.</td>
            </tr>
            <tr>
              <td><strong>F1-Score</strong></td>
              <td>Harmonic mean of Precision and Recall: <code>2 &times; (P &times; R) / (P + R)</code>.</td>
            </tr>
            <tr>
              <td><strong>ROC AUC</strong></td>
              <td>Area under Receiver Operating Characteristic curve measuring global ranking discrimination.</td>
            </tr>
            <tr>
              <td><strong>C Parameter</strong></td>
              <td>Scikit-learn&rsquo;s inverse regularization parameter (<code>C = 1 / &lambda;</code>). Smaller C = stronger penalty.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">&#129518; 12 Interactive Revision Questions &amp; Solutions</h3>

      <!-- Question 1 -->
      <details class="accordion">
        <summary class="accordion-summary">Q1: Why is Logistic Regression called &ldquo;regression&rdquo; if it performs classification?</summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> Internally, the model computes an unbounded continuous linear regression score (<code>z = &beta;<sub>0</sub> + &sum; &beta;<sub>j</sub>x<sub>j</sub></code>) representing the log-odds of the positive class. It transforms that continuous score into a bounded probability using the sigmoid function and classifies based on a threshold.</p>
        </div>
      </details>

      <!-- Question 2 -->
      <details class="accordion">
        <summary class="accordion-summary">Q2 (Numerical): Calculate the exact sigmoid probability when the linear score is z = +1.8.</summary>
        <div class="accordion-content">
          <p><strong>Step-by-step Solution:</strong></p>
          <ol>
            <li>Formula: <code>&sigma;(z) = 1 / (1 + e<sup>-z</sup>)</code></li>
            <li>Calculate <code>e<sup>-1.8</sup> &approx; 0.165299</code></li>
            <li>Denominator: <code>1 + 0.165299 = 1.165299</code></li>
            <li>Sigmoid: <code>1 / 1.165299 = <strong>0.8581 (85.81%)</strong></code></li>
          </ol>
        </div>
      </details>

      <!-- Question 3 -->
      <details class="accordion">
        <summary class="accordion-summary">Q3 (Numerical): An event has probability p = 0.80. What are its Odds and Log-Odds?</summary>
        <div class="accordion-content">
          <p><strong>Step-by-step Solution:</strong></p>
          <ul>
            <li><code>Odds = p / (1 - p) = 0.80 / (1 - 0.80) = 0.80 / 0.20 = <strong>4.0</strong></code> (or &ldquo;4 to 1&rdquo;).</li>
            <li><code>Log-Odds = ln(4.0) = <strong>+1.3863</strong></code>.</li>
          </ul>
        </div>
      </details>

      <!-- Question 4 -->
      <details class="accordion">
        <summary class="accordion-summary">Q4: If a feature&rsquo;s learned slope is &beta; = +1.20, what is its Odds Ratio and plain-English interpretation?</summary>
        <div class="accordion-content">
          <p><strong>Solution:</strong></p>
          <p><code>Odds Ratio = e<sup>1.20</sup> = <strong>3.3201</strong></code>.</p>
          <p><em>Interpretation:</em> Holding all other features fixed, a one-unit increase in this feature multiplies the odds of the outcome by approximately 3.32 (a 232% increase in odds, NOT probability).</p>
        </div>
      </details>

      <!-- Question 5 -->
      <details class="accordion">
        <summary class="accordion-summary">Q5 (Numerical): Calculate Log Loss when actual label y = 1 and predicted probability is p = 0.90 vs. p = 0.10.</summary>
        <div class="accordion-content">
          <p><strong>Solution:</strong></p>
          <ul>
            <li>When <code>p = 0.90</code> (Confident Correct): <code>Loss = -ln(0.90) = <strong>0.1054</strong></code>.</li>
            <li>When <code>p = 0.10</code> (Confident WRONG): <code>Loss = -ln(0.10) = <strong>2.3026</strong></code>.</li>
            <li>The confident incorrect prediction is penalized <strong>21.8 times more severely</strong> (2.3026 / 0.1054 = 21.84)!</li>
          </ul>
        </div>
      </details>

      <!-- Question 6 -->
      <details class="accordion">
        <summary class="accordion-summary">Q6 (Confusion Matrix Problem): In a cancer clinic test of 100 patients, TP=18, FN=2, FP=6, TN=74. Calculate Accuracy, Precision, Recall, and F1-score.</summary>
        <div class="accordion-content">
          <p><strong>Step-by-step Solution:</strong></p>
          <ul>
            <li><code>Accuracy = (18 + 74) / 100 = 92 / 100 = <strong>92.00%</strong></code></li>
            <li><code>Precision = 18 / (18 + 6) = 18 / 24 = <strong>75.00%</strong></code></li>
            <li><code>Recall = 18 / (18 + 2) = 18 / 20 = <strong>90.00%</strong></code></li>
            <li><code>F1 = 2 &times; (0.75 &times; 0.90) / (0.75 + 0.90) = 1.35 / 1.65 = <strong>81.82%</strong></code></li>
          </ul>
        </div>
      </details>

      <!-- Question 7 -->
      <details class="accordion">
        <summary class="accordion-summary">Q7: Why does a threshold change from &tau; = 0.50 to &tau; = 0.30 increase Recall?</summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> Lowering the bar makes it easier for samples to be classified as positive. Borderline positive cases with probabilities between 0.30 and 0.49 that were previously missed (False Negatives) are now captured as True Positives. Because Recall is <code>TP / (TP + FN)</code>, capturing more positives increases Recall.</p>
        </div>
      </details>

      <!-- Question 8 -->
      <details class="accordion">
        <summary class="accordion-summary">Q8: What is the geometric shape of the decision boundary in standard Logistic Regression with 2 input features?</summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> A straight line in the 2D feature plane given by the equation: <code>&beta;<sub>0</sub> + &beta;<sub>1</sub>x<sub>1</sub> + &beta;<sub>2</sub>x<sub>2</sub> = 0</code> (at threshold &tau; = 0.50).</p>
        </div>
      </details>

      <!-- Question 9 -->
      <details class="accordion">
        <summary class="accordion-summary">Q9: In scikit-learn, does setting C = 0.01 increase or decrease regularization?</summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> It <strong>greatly increases regularization</strong>. Parameter <code>C</code> is the inverse of regularization strength (<code>C = 1 / &lambda;</code>). A tiny C value represents a massive penalty on large coefficients, shrinking weights aggressively towards zero.</p>
        </div>
      </details>

      <!-- Question 10 -->
      <details class="accordion">
        <summary class="accordion-summary">Q10: Why does a dummy model on an imbalanced dataset (99% normal, 1% fraud) get 99% accuracy while being completely useless?</summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> By always predicting &ldquo;Normal&rdquo;, the model is correct on all 99 normal transactions (<code>99 / 100 = 99% accuracy</code>). However, it detects exactly 0 fraud cases (<code>Recall = 0.0%</code>), failing its entire business purpose.</p>
        </div>
      </details>

      <!-- Question 11 -->
      <details class="accordion">
        <summary class="accordion-summary">Q11 (Scenario Problem): An airport security scanner flags luggage for contraband. A false alarm causes a 2-minute manual bag search. A false negative lets an explosive onto an aircraft. Should you set &tau; high (0.80) or low (0.20)?</summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> Set <code>&tau; = 0.20</code> (low threshold). The cost of a False Negative (catastrophic disaster) vastly outweighs the minor inconvenience of a False Positive (a 2-minute inspection). You must maximize Recall!</p>
        </div>
      </details>

      <!-- Question 12 -->
      <details class="accordion">
        <summary class="accordion-summary">Q12 (Python Exercise): Write a 5-line scikit-learn code snippet to train Logistic Regression with balanced class weights inside a leak-free pipeline.</summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong></p>
          <pre><code>from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(class_weight='balanced', random_state=42))
])
pipe.fit(X_train, y_train)</code></pre>
        </div>
      </details>
    </section>
"""
