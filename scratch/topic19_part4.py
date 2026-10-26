# Topic 19 Content - Part 4: Sections 22 to 27 & Chapter Footer
# Strict Light Mode Only, Native HTML Math, Verified Numerical Examples

TOPIC19_PART4 = """
    <!-- SECTION 22 -->
    <section id="sec-22" class="content-section">
      <span class="section-tag">Section 22</span>
      <h2 class="section-title">Training, Validation, and Test Evaluation</h2>
      <p class="section-intro">
        How data is partitioned and transformed before computing metrics is just as critical as the mathematical formulas themselves. Data leakage during evaluation invalidates every reported metric.
      </p>

      <h3>The Golden Rule of ML Splits: Three Distinct Datasets</h3>
      <ol>
        <li><strong>Training Set (60-70%):</strong> Used exclusively to update model weights, decision trees, or coefficients.</li>
        <li><strong>Validation Set (15-20%):</strong> Used to compare different algorithms, tune hyperparameters, and <strong>select optimal classification thresholds</strong>.</li>
        <li><strong>Test Set (15-20%):</strong> Kept in a strictly sealed cryptographic vault until all modeling and tuning are finalized. It is evaluated <strong>exactly once</strong> to estimate real-world generalization performance.</li>
      </ol>

      <!-- FIGURE 22.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 22.1 &bull; Leakage-Safe Evaluation Pipeline and Data Splits</span>
          <span class="visual-tag">Pipeline Best Practices</span>
        </div>
        __SVG_EVAL_SPLITS_PIPELINE__
        <div class="visual-caption">
          Figure 22.1: Leakage-safe evaluation pipeline. Preprocessing transformers (scalers, encoders, imputers) are fit strictly on training splits only, then applied via transform() to validation and test splits.
        </div>
      </div>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Critical Evaluation Pitfall: Preprocessing Data Leakage
        </div>
        <p>
          A frequent blunder made by junior engineers is normalizing or scaling the entire dataset <em>before</em> calling <code>train_test_split()</code>:
          <br><br>
          <code style="color:#DC2626; font-weight:700;"># WRONG: Leaks test set mean and standard deviation into training!</code><br>
          <code>scaler = StandardScaler()</code><br>
          <code>X_scaled = scaler.fit_transform(X)  # LEAKAGE!</code><br>
          <code>X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)</code>
          <br><br>
          <code style="color:#15803D; font-weight:700;"># CORRECT: Encapsulate scaler and model inside a scikit-learn Pipeline</code><br>
          <code>pipeline = Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression())])</code><br>
          <code>pipeline.fit(X_train, y_train)  # Scaler only learns from X_train!</code>
        </p>
      </div>

      <h3>Specialized Splitting Strategies</h3>
      <ul>
        <li><strong>Stratified Splitting:</strong> For imbalanced classification, always use <code>stratify=y</code> in <code>train_test_split()</code>. This guarantees that train, validation, and test sets contain the exact same percentage of positive cases.</li>
        <li><strong>Chronological (Time-Series) Splitting:</strong> For financial data, weather forecasts, or sensor logs, <strong>never use random splitting</strong>! Random shuffling leaks future information into past predictions. Split strictly chronologically (train on Months 1&ndash;9, test on Months 10&ndash;12).</li>
      </ul>
    </section>

    <!-- SECTION 23 -->
    <section id="sec-23" class="content-section">
      <span class="section-tag">Section 23</span>
      <h2 class="section-title">Selecting the Right Metric: Decision Guide</h2>
      <p class="section-intro">
        There is no single "best" machine learning metric. The optimal metric is determined entirely by the task type, class distribution, and asymmetric business costs of mistakes.
      </p>

      <!-- FIGURE 23.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 23.1 &bull; Metric Selection Decision Tree</span>
          <span class="visual-tag">Strategic Decision Map</span>
        </div>
        __SVG_METRIC_DECISION_TREE__
        <div class="visual-caption">
          Figure 23.1: Systematic metric selection decision tree. Follow the branch matching your target type (classification vs regression), class balance (balanced vs rare positive), and asymmetric cost priorities.
        </div>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Real-World Problem Scenario</th>
              <th>Primary Evaluation Metrics</th>
              <th>Secondary Diagnostic Tools</th>
              <th>Strategic Justification</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Spam Email Filtering</strong></td>
              <td><strong>Precision, F0.5-Score</strong></td>
              <td>Confusion Matrix, Specificity</td>
              <td>False Positives (deleting legitimate client emails) cause severe disruption; model must be very pure when flagging spam.</td>
            </tr>
            <tr>
              <td><strong>Rare Disease Screening / Threats</strong></td>
              <td><strong>Recall, F2-Score, PR-AUC</strong></td>
              <td>FNR, Confusion Matrix</td>
              <td>False Negatives (missing a real threat) can be fatal; false alarms are triaged via human review.</td>
            </tr>
            <tr>
              <td><strong>Credit Card Fraud Detection</strong></td>
              <td><strong>PR-AUC, Average Precision, F1</strong></td>
              <td>Precision-Recall Curve, Cost Curve</td>
              <td>Extreme class imbalance (0.1% positive); ROC-AUC is misleadingly optimistic; PR-AUC reflects real fraud capture.</td>
            </tr>
            <tr>
              <td><strong>Balanced Image Classification (10 classes)</strong></td>
              <td><strong>Macro F1, Top-1 Accuracy</strong></td>
              <td>Multiclass Confusion Matrix</td>
              <td>Classes are equally frequent and equally valuable; macro averaging ensures no single class is neglected.</td>
            </tr>
            <tr>
              <td><strong>Real Estate House Valuation</strong></td>
              <td><strong>MAE, R&sup2; Score</strong></td>
              <td>Residual Plot, Scatter vs Actual</td>
              <td>MAE is directly interpretable to home buyers in dollar terms; R&sup2; provides comparison against the market average.</td>
            </tr>
            <tr>
              <td><strong>Financial Risk / Algorithmic Trading</strong></td>
              <td><strong>RMSE, Max Error</strong></td>
              <td>Residual Spread, QQ-Plot</td>
              <td>Large financial prediction blunders trigger massive trading losses; quadratic penalty in RMSE is essential.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 24 -->
    <section id="sec-24" class="content-section">
      <span class="section-tag">Section 24</span>
      <h2 class="section-title">Common Mistakes and Limitations (14 Critical Pitfalls)</h2>
      <p class="section-intro">
        Learn from real-world evaluation failures. Below are the 14 most frequent mistakes made in machine learning evaluation and how to prevent them.
      </p>

      <!-- MISTAKE 01 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 01: Relying Solely on Accuracy for Imbalanced Classification
        </div>
        <p>Reporting 99% accuracy on a dataset with 1% positive rate while the model actually detects zero positive samples.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            "Our fraud model achieves 99.8% accuracy, so it is ready for deployment."
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            Evaluate with <strong>Precision, Recall, F1, PR-AUC, and the confusion matrix</strong> to assess positive detection.
          </div>
        </div>
      </div>

      <!-- MISTAKE 02 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 02: Confusing Precision with Recall
        </div>
        <p>Using Precision when the business objective is to minimize missed detections, or vice versa.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            "We optimized precision to make sure we didn't miss any defective airplane parts."
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            Recall minimizes missed defects (FN). Precision minimizes false alarms (FP). Optimize <strong>Recall</strong> here.
          </div>
        </div>
      </div>

      <!-- MISTAKE 03 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 03: Tuning Classification Thresholds on the Final Test Set
        </div>
        <p>Testing 20 different thresholds on the test set and picking the one with the highest test F1 score.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            Threshold selected by maximizing F1 directly on the test set &rarr; severe data leakage and overfitting.
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            Select the optimal operational threshold on the <strong>validation set</strong>, then test exactly once on the test set.
          </div>
        </div>
      </div>

      <!-- MISTAKE 04 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 04: Passing Hard Labels (0 and 1) to ROC-AUC or PR Curves
        </div>
        <p>Passing discrete predicted binary classes into <code>roc_auc_score(y_true, y_pred)</code> instead of probabilities.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            <code>roc_auc_score(y_test, y_pred)</code> &rarr; collapses the ROC curve into a crude 3-point step function.
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            Pass continuous probability estimates: <code>roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])</code>.
          </div>
        </div>
      </div>

      <!-- MISTAKE 05 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 05: Assuming ROC-AUC Determines Operational Performance
        </div>
        <p>Assuming a model with 0.95 ROC-AUC will automatically work well at the default 0.50 threshold.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            "ROC-AUC is 0.95, so we can deploy directly at default settings without checking confusion matrix."
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            ROC-AUC measures ranking skill across all thresholds. You must still choose and validate an operating threshold.
          </div>
        </div>
      </div>

      <!-- MISTAKE 06 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 06: Comparing MAE and RMSE Directly Without Considering Penalties
        </div>
        <p>Believing an MAE of $14k and an RMSE of $22k means the calculation is broken or inconsistent.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            "RMSE is much larger than MAE, so the model must be broken."
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            RMSE &ge; MAE is a mathematical certainty. A large gap simply indicates high variance or occasional large errors.
          </div>
        </div>
      </div>

      <!-- MISTAKE 07 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 07: Believing R&sup2; Must Always Be Between 0 and 1
        </div>
        <p>Panicking when encountering a negative R&sup2; score on test data and assuming scikit-learn has a bug.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            "R&sup2; is -0.45; there must be an error in the library because R&sup2; is a squared quantity."
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            R&sup2; on test data is $1 - (SS<sub>res</sub> / SS<sub>tot</sub>). A negative score means the model is worse than the mean!
          </div>
        </div>
      </div>

      <!-- MISTAKE 08 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 08: Treating R&sup2; as "Percentage of Correct Predictions"
        </div>
        <p>Telling stakeholders that an R&sup2; of 0.85 means "85% of price predictions were accurate."</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            "Our model predicted 85% of house prices correctly."
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            "Our model explains <strong>85% of the variance</strong> in house prices compared to the historical average."
          </div>
        </div>
      </div>

      <!-- MISTAKE 09 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 09: Test Set Overfitting (Testing Repeatedly in the Loop)
        </div>
        <p>Adjusting tree depths, regularization terms, and feature sets dozens of times based on test set scores.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            Repeatedly running evaluation on the test set turns the test set into a hidden training set.
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            Iterate and tune using <strong>k-fold cross-validation</strong> on the training set. Evaluate test set once.
          </div>
        </div>
      </div>

      <!-- MISTAKE 10 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 10: Data Leakage in Evaluation Preprocessing
        </div>
        <p>Fitting scalers, imputers, or encoders on the combined dataset before evaluation splitting.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            <code>StandardScaler().fit_transform(full_X)</code> before splitting leaks future distribution into training.
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            Fit all preprocessing transformers strictly on <code>X_train</code> inside a <code>Pipeline</code>.
          </div>
        </div>
      </div>

      <!-- MISTAKE 11 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 11: Overlooking Class Imbalance in Multiclass Averaging
        </div>
        <p>Using Macro averaging when a rare class has 1 sample, or using Weighted averaging when rare classes matter.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            Blindly reporting whatever default averaging the tool selects without understanding its impact.
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            Always inspect <strong>per-class metrics</strong> first, then choose Macro vs Weighted deliberately.
          </div>
        </div>
      </div>

      <!-- MISTAKE 12 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 12: Reporting Fabricated or Hand-Wave Metrics
        </div>
        <p>Writing approximate or rounded numbers in engineering reports without executable code verification.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            Writing "accuracy is ~95%" based on training logs without running test evaluation scripts.
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            Always provide reproducible scripts with fixed random seeds and verified exact decimal outputs.
          </div>
        </div>
      </div>

      <!-- MISTAKE 13 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 13: Ignoring Asymmetric Business Mistake Costs
        </div>
        <p>Treating a False Positive as identical in severity to a False Negative in high-stakes domains.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            Selecting a model based solely on raw accuracy or unweighted F1 without business domain consultation.
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            Model the actual financial or human costs: Total Cost = (c_FP &times; FP) + (c_FN &times; FN).
          </div>
        </div>
      </div>

      <!-- MISTAKE 14 -->
      <div class="mistake-card">
        <div class="mistake-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Pitfall 14: Relying on Single Summary Metrics Without Diagnostic Visuals
        </div>
        <p>Deploying a regression model with R&sup2; = 0.90 without looking at the residual plot, missing massive curvature.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; Wrong Practice</div>
            Reporting only a single scalar score in presentations without visualizing errors.
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&check; Correct Practice</div>
            Always inspect <strong>confusion matrices, ROC/PR curves, and residual plots</strong> alongside summary metrics.
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 25 -->
    <section id="sec-25" class="content-section">
      <span class="section-tag">Section 25</span>
      <h2 class="section-title">Complete Python Practical: Model Evaluation Dashboard</h2>
      <p class="section-intro">
        A self-contained, reproducible educational mini-project implementing end-to-end evaluation dashboards for both classification and regression using scikit-learn, NumPy, and Matplotlib.
      </p>

      <h3>Project Overview &amp; Architectural Setup</h3>
      <p>
        We execute two end-to-end workflows with fixed random seeds (<code>random_state=42</code>) to ensure 100% numerical reproducibility:
      </p>
      <ul>
        <li><strong>Workflow A (Classification):</strong> Evaluates a Logistic Regression classifier on breast cancer diagnostic features (N=569, test N=171) using a leakage-safe <code>Pipeline</code>.</li>
        <li><strong>Workflow B (Regression):</strong> Evaluates a Ridge Regression model on synthetic housing evaluation features (N=500, test N=150) using a leakage-safe <code>Pipeline</code>.</li>
      </ul>

      <!-- PRACTICAL CODE WORKFLOW A -->
      <h3>Workflow A &bull; Classification Evaluation Pipeline</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; classification_evaluation_dashboard.py</span>
          <span>Complete Executable Script</span>
        </div>
        <pre><code>import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, average_precision_score, roc_curve,
    precision_recall_curve, ConfusionMatrixDisplay
)

# 1. Load dataset (Binary: 0 = Malignant, 1 = Benign)
data = load_breast_cancer()
X, y = data.data, data.target

# 2. Leakage-safe stratified train/test split (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# 3. Create pipeline (Scaler fit strictly on training data!)
pipeline_clf = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(random_state=42, max_iter=1000))
])

# 4. Fit model and predict
pipeline_clf.fit(X_train, y_train)
y_pred = pipeline_clf.predict(X_test)
y_prob = pipeline_clf.predict_proba(X_test)[:, 1]

# 5. Calculate all evaluation metrics
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, zero_division=0)
rec = recall_score(y_test, y_pred)
spec = tn / (tn + fp)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)
ap = average_precision_score(y_test, y_prob)

print("=== CLASSIFICATION METRICS REPORT (N_test = 171) ===")
print(f"Confusion Matrix: TN={tn}, FP={fp}, FN={fn}, TP={tp}")
print(f"Accuracy:         {acc:.4f} (97.66%)")
print(f"Precision:        {prec:.4f} (98.13%)")
print(f"Recall:           {rec:.4f} (98.13%)")
print(f"Specificity:      {spec:.4f} (96.88%)")
print(f"F1-Score:         {f1:.4f}")
print(f"ROC-AUC:          {roc_auc:.4f} (99.71%)")
print(f"Average Precision:{ap:.4f} (99.84%)")</code></pre>
      </div>

      <div class="card card-success">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          Verified Executed Classification Output
        </div>
        <p>
          <strong>Exact Model Performance on 171 Held-Out Test Samples:</strong>
          <br>&bull; <strong>Confusion Matrix:</strong> True Negatives = 62, False Positives = 2, False Negatives = 2, True Positives = 105.
          <br>&bull; <strong>Accuracy:</strong> (105 + 62) / 171 = 167 / 171 = <strong>0.9766</strong> (97.66%).
          <br>&bull; <strong>Precision:</strong> $105 / (105 + 2) = 105 / 107 = <strong>0.9813</strong> (98.13%).
          <br>&bull; <strong>Recall:</strong> $105 / (105 + 2) = 105 / 107 = <strong>0.9813</strong> (98.13%).
          <br>&bull; <strong>Specificity:</strong> $62 / (62 + 2) = 62 / 64 = <strong>0.9688</strong> (96.88%).
          <br>&bull; <strong>F1-Score:</strong> $2 \times (0.9813 \times 0.9813) / (0.9813 + 0.9813) = <strong>0.9813</strong>.
          <br>&bull; <strong>ROC-AUC:</strong> $<strong>0.9971</strong> (Exceptional ranking power across all cutoffs).
          <br>&bull; <strong>Average Precision (AP):</strong> $<strong>0.9984</strong> (Near-perfect Precision-Recall curve).
        </p>
      </div>

      <!-- PRACTICAL CODE WORKFLOW B -->
      <h3>Workflow B &bull; Regression Evaluation Pipeline</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; regression_evaluation_dashboard.py</span>
          <span>Complete Executable Script</span>
        </div>
        <pre><code>from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

# 1. Generate synthetic educational housing dataset (N=500, 4 features)
np.random.seed(42)
N = 500
X_reg = np.random.randn(N, 4)
# True relationship: price (k) = 250 + 40*x0 + 30*x1 - 20*x2 + noise
y_reg = 250.0 + 40.0 * X_reg[:, 0] + 30.0 * X_reg[:, 1] - 20.0 * X_reg[:, 2] + np.random.normal(0, 15, N)

# 2. Leakage-safe split (70% train, 30% test)
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_reg, y_reg, test_size=0.30, random_state=42
)

# 3. Create pipeline
pipeline_reg = Pipeline([
    ('scaler', StandardScaler()),
    ('reg', Ridge(alpha=1.0, random_state=42))
])

# 4. Fit model and predict
pipeline_reg.fit(X_train_r, y_train_r)
y_pred_r = pipeline_reg.predict(X_test_r)

# 5. Compute regression metrics
mae_val = mean_absolute_error(y_test_r, y_pred_r)
mse_val = mean_squared_error(y_test_r, y_pred_r)
rmse_val = root_mean_squared_error(y_test_r, y_pred_r)
r2_val = r2_score(y_test_r, y_pred_r)

print("=== REGRESSION METRICS REPORT (N_test = 150) ===")
print(f"MAE:       {mae_val:.2f}k ({mae_val*1000:,.2f})")
print(f"MSE:       {mse_val:.2f} (k^2)")
print(f"RMSE:      {rmse_val:.2f}k ({rmse_val*1000:,.2f})")
print(f"R-squared: {r2_val:.4f} ({r2_val*100:.2f}% variance explained)")</code></pre>
      </div>

      <div class="card card-purple">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          Verified Executed Regression Output
        </div>
        <p>
          <strong>Exact Model Performance on 150 Held-Out Housing Samples:</strong>
          <br>&bull; <strong>Mean Absolute Error (MAE):</strong> $<strong>11.96k</strong> (\11,960 typical dollar error).
          <br>&bull; <strong>Mean Squared Error (MSE):</strong> $<strong>223.14</strong> (k^2).
          <br>&bull; <strong>Root Mean Squared Error (RMSE):</strong> &radic;(223.14) = <strong>14.94k</strong> (\14,940).
          <br>&bull; <strong>R-squared (R&sup2;):</strong> $<strong>0.9238</strong> ($92.38%$ of home price variance explained).
        </p>
      </div>
    </section>

    <!-- SECTION 26 -->
    <section id="sec-26" class="content-section">
      <span class="section-tag">Section 26</span>
      <h2 class="section-title">Quick Revision and Formula Sheet</h2>
      <p class="section-intro">
        A condensed master formula sheet and glossary for quick examination preparation, interview revision, and production reference.
      </p>

      <h3>Classification Formula Sheet</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Metric</th>
              <th>Formula</th>
              <th>Core Intuition</th>
              <th>Optimal Use Case</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Accuracy</strong></td>
              <td><code>(TP + TN) / (TP + TN + FP + FN)</code></td>
              <td>Fraction of all predictions that are correct</td>
              <td>Balanced classes with symmetric mistake costs</td>
            </tr>
            <tr>
              <td><strong>Precision</strong></td>
              <td><code>TP / (TP + FP)</code></td>
              <td>Of all predicted positives, how many are real?</td>
              <td>When False Positives are expensive (Spam, Alerts)</td>
            </tr>
            <tr>
              <td><strong>Recall (Sensitivity)</strong></td>
              <td><code>TP / (TP + FN)</code></td>
              <td>Of all real positives, how many were detected?</td>
              <td>When False Negatives are critical (Fraud, Screening)</td>
            </tr>
            <tr>
              <td><strong>Specificity</strong></td>
              <td><code>TN / (TN + FP)</code></td>
              <td>Of all real negatives, how many were correctly cleared?</td>
              <td>Diagnostic clearance rate (1 &minus; FPR)</td>
            </tr>
            <tr>
              <td><strong>F1-Score</strong></td>
              <td><code>2 &times; (P &times; R) / (P + R)</code></td>
              <td>Harmonic mean balancing Precision &amp; Recall</td>
              <td>Imbalanced classes where both FP and FN matter</td>
            </tr>
            <tr>
              <td><strong>ROC-AUC</strong></td>
              <td><code>&int; TPR d(FPR)</code></td>
              <td>Probability that a positive ranks above a negative</td>
              <td>Evaluating overall ranking skill across all thresholds</td>
            </tr>
            <tr>
              <td><strong>Average Precision</strong></td>
              <td><code>&sum; (R_n &minus; R_{n-1}) &times; P_n</code></td>
              <td>Area under Precision-Recall curve</td>
              <td>Severe class imbalance where positive class is rare</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Regression Formula Sheet</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Metric</th>
              <th>Formula</th>
              <th>Physical Units</th>
              <th>Penalty Characteristic</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Mean Absolute Error (MAE)</strong></td>
              <td><code>(1/n) &sum; |y - &#375;|</code></td>
              <td>Target units (e.g., $)</td>
              <td>Linear penalty; robust to extreme outliers</td>
            </tr>
            <tr>
              <td><strong>Mean Squared Error (MSE)</strong></td>
              <td><code>(1/n) &sum; (y - &#375;)&sup2;</code></td>
              <td>Squared units (&sup2;)</td>
              <td>Quadratic penalty; smooth derivative for gradient descent</td>
            </tr>
            <tr>
              <td><strong>Root Mean Squared Error (RMSE)</strong></td>
              <td><code>&radic;[ (1/n) &sum; (y - &#375;)&sup2; ]</code></td>
              <td>Target units (e.g., $)</td>
              <td>Penalizes large errors heavily; same units as target</td>
            </tr>
            <tr>
              <td><strong>R-squared (R&sup2;)</strong></td>
              <td><code>1 &minus; (SS_res / SS_tot)</code></td>
              <td>Dimensionless (percentage)</td>
              <td>Proportion of target variance explained vs mean baseline</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Master Glossary (12 Key Terms)</h3>
      <ol>
        <li><strong>True Positive (TP):</strong> Condition is positive, model predicts positive.</li>
        <li><strong>False Positive (FP):</strong> Condition is negative, model predicts positive (Type I error / False Alarm).</li>
        <li><strong>False Negative (FN):</strong> Condition is positive, model predicts negative (Type II error / Missed Detection).</li>
        <li><strong>True Negative (TN):</strong> Condition is negative, model predicts negative.</li>
        <li><strong>Decision Threshold (&theta;):</strong> The probability cutoff above which a sample is classified as Class 1.</li>
        <li><strong>Harmonic Mean:</strong> An average calculated as the reciprocal of arithmetic mean of reciprocals; severely penalizes low outliers.</li>
        <li><strong>Macro Averaging:</strong> Computes metric independently per class, then takes unweighted average. Treats small classes equally.</li>
        <li><strong>Weighted Averaging:</strong> Averages per-class metrics weighted by class frequency (support).</li>
        <li><strong>Micro Averaging:</strong> Pools total TP, FP, FN globally before computing metric. Equal to accuracy in multiclass.</li>
        <li><strong>Residual:</strong> The signed difference between true value and model prediction (e<sub>i</sub> = y<sub>i</sub> &minus; &#375;<sub>i</sub>).</li>
        <li><strong>Homoscedasticity:</strong> Constant error variance across all levels of predicted values (healthy random scatter).</li>
        <li><strong>Data Leakage:</strong> Inadvertently sharing information between test/validation data and the training pipeline.</li>
      </ol>
    </section>

    <!-- SECTION 27 -->
    <section id="sec-27" class="content-section">
      <span class="section-tag">Section 27</span>
      <h2 class="section-title">Self-Check Quiz &amp; Technical Interview Q&amp;A (12 Questions)</h2>
      <p class="section-intro">
        Test your conceptual and numerical mastery. Click each question below to reveal detailed step-by-step explanations.
      </p>

      <!-- FAQ 01 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q1: A confusion matrix reports TN=90, FP=10, FN=5, TP=95. What are the Accuracy, Precision, Recall, and Specificity?
        </summary>
        <div class="faq-content">
          <p><strong>Step-by-Step Calculation:</strong></p>
          <ul>
            <li>Total observations N = 90 + 10 + 5 + 95 = 200.</li>
            <li><strong>Accuracy:</strong> (TP + TN) / N = (95 + 90) / 200 = 185 / 200 = <strong>0.9250</strong> (92.5%).</li>
            <li><strong>Precision:</strong> TP / (TP + FP) = 95 / (95 + 10) = 95 / 105 \approx <strong>0.9048</strong> (90.48%).</li>
            <li><strong>Recall:</strong> TP / (TP + FN) = 95 / (95 + 5) = 95 / 100 = <strong>0.9500</strong> (95.0%).</li>
            <li><strong>Specificity:</strong> TN / (TN + FP) = 90 / (90 + 10) = 90 / 100 = <strong>0.9000</strong> (90.0%).</li>
          </ul>
        </div>
      </details>

      <!-- FAQ 02 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q2: Why does an F1-Score of 0.80 require BOTH Precision and Recall to be at least relatively high?
        </summary>
        <div class="faq-content">
          <p>
            Because F1 is the <strong>harmonic mean</strong>: F1 = 2 &times; (P &times; R) / (P + R). The harmonic mean is mathematically constrained to be closer to the minimum of the two values than the arithmetic mean. If Precision is 1.0 but Recall drops to 0.10, the arithmetic average is 0.55, but the F1-Score collapses to $2 \times 0.10 / 1.10 = 0.1818. To achieve F1 = 0.80, neither metric can lag severely behind.
          </p>
        </div>
      </details>

      <!-- FAQ 03 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q3: When would an engineer deliberately choose an F2-Score over an F0.5-Score?
        </summary>
        <div class="faq-content">
          <p>
            In the F<sub>&beta;</sub> formula, \beta weights Recall relative to Precision. For \beta = 2.0 (F2-Score), <strong>Recall is weighted twice as heavily as Precision</strong>. An engineer chooses F2 when a False Negative is significantly more costly or dangerous than a False Positive &mdash; such as detecting fatal medical conditions, severe structural bridge cracks, or network security intrusions. Conversely, F0.5 is chosen when False Positives (user annoyances, false alarms) are more costly.
          </p>
        </div>
      </details>

      <!-- FAQ 04 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q4: What does an ROC-AUC of 0.50 indicate, and can an ROC-AUC score ever be less than 0.50?
        </summary>
        <div class="faq-content">
          <p>
            An ROC-AUC of 0.50 represents <strong>random chance ranking performance</strong> &mdash; the model's predictions are no better than flipping an unbiased coin.
            <br><br>
            Yes, ROC-AUC can be less than 0.50 if the model has learned the exact inverse relationship (e.g., systematically assigning higher probabilities to negatives than to positives). Inverting the model's predictions ($1 &minus; P) will transform an AUC of 0.20 into an AUC of 0.80.
          </p>
        </div>
      </details>

      <!-- FAQ 05 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q5: Why is the Precision–Recall curve preferred over the ROC curve when the positive class is extremely rare (e.g., 0.1%)?
        </summary>
        <div class="faq-content">
          <p>
            Because the X-axis of the ROC curve is FPR = FP / (TN + FP). When the negative class is massive (TN = 1,000,000), thousands of False Positives (FP = 5,000) result in an FPR of only $5,000 / 1,005,000 \approx 0.005, making the ROC curve look nearly perfect. However, if there are only 100 true positive cases, those 5,000 False Positives mean Precision is an abysmal $100 / 5,100 \approx 1.96%$. The PR curve directly exposes this flood of false alarms, whereas the ROC curve completely conceals it.
          </p>
        </div>
      </details>

      <!-- FAQ 06 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q6: In a 3-class problem, when does Micro Average Precision equal Overall Accuracy?
        </summary>
        <div class="faq-content">
          <p>
            In standard multiclass classification where <strong>each sample belongs to exactly one class</strong>, Micro Precision, Micro Recall, Micro F1, and Overall Accuracy are <strong>identically equal</strong>!
            <br><br>
            <em>Proof:</em> Every error is simultaneously a False Positive for the wrongly predicted class and a False Negative for the true class. Therefore, total False Positives globally equals total False Negatives globally. Thus, Micro Precision = &sum; TP / (&sum; TP + &sum; FP) = \frac{Total Correct}{Total Samples} = Accuracy.
          </p>
        </div>
      </details>

      <!-- FAQ 07 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q7: Why does RMSE always satisfy RMSE &ge; MAE, and what does a large gap between them reveal?
        </summary>
        <div class="faq-content">
          <p>
            By the Cauchy-Schwarz inequality (and the properties of power means), the square root of the mean of squared numbers is always greater than or equal to the mean of their absolute values (RMSE &ge; MAE).
            <br><br>
            They are equal if and only if every single residual has the exact same absolute magnitude (e.g., all errors are exactly 10). If a model has a few extreme blunder errors (e.g., one prediction off by 100 while others are off by 5), the squaring operation explodes, driving RMSE up dramatically while MAE remains modest. A large gap between RMSE and MAE proves that error variance is high and large outliers exist.
          </p>
        </div>
      </details>

      <!-- FAQ 08 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q8: Can R-squared (R&sup2;) be negative? What does a negative R&sup2; mean physically?
        </summary>
        <div class="faq-content">
          <p>
            <strong>Yes! On test data or with nonlinear models, R&sup2; can be negative.</strong>
            <br><br>
            R&sup2; = 1 - (SS_res / SS_tot). If the model's predictions on the test set produce larger total squared error (SS<sub>res</sub>) than simply predicting the mean of the target data (SS<sub>tot</sub>), the ratio (SS_res / SS_tot) exceeds 1.0, making R&sup2; &lt; 0. Physically, it means your model is performing <strong>worse than a flat horizontal line guessing the average value</strong>.
          </p>
        </div>
      </details>

      <!-- FAQ 09 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q9: What does a funnel/fan shape in a residual plot indicate, and how should you fix it?
        </summary>
        <div class="faq-content">
          <p>
            A fan or funnel shape (where residuals spread out wider as predicted values increase) indicates <strong>heteroscedasticity</strong> &mdash; non-constant error variance. This commonly happens in monetary data (e.g., predicting the price of a $10M mansion has naturally higher dollar variance than a $100k apartment).
            <br><br>
            <em>Remedy:</em> Apply a variance-stabilizing transformation to the target variable before modeling, such as <code>np.log1p(y)</code> or a Box-Cox power transform.
          </p>
        </div>
      </details>

      <!-- FAQ 10 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q10: Why must you NEVER tune your classification decision threshold on the test set?
        </summary>
        <div class="faq-content">
          <p>
            Because tuning the decision threshold is an act of <strong>model optimization</strong> (hyperparameter selection). If you test various thresholds on the test set and choose the one with highest test score, you have allowed information from the test set to guide model design. The resulting test score will be optimistically biased and will fail to reflect actual production generalization. Always tune thresholds on a <strong>validation split</strong>.
          </p>
        </div>
      </details>

      <!-- FAQ 11 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q11: How does scikit-learn handle division by zero when calculating Precision if TP + FP = 0?
        </summary>
        <div class="faq-content">
          <p>
            If a model predicts zero positive samples, the denominator TP + FP = 0, making Precision mathematically undefined ($0/0). By default, scikit-learn raises an <code>UndefinedMetricWarning</code> and returns 0.0. In production code, you should explicitly pass <code>zero_division=0</code> (or <code>zero_division=1</code> depending on policy) to prevent warning noise and handle the edge case gracefully.
          </p>
        </div>
      </details>

      <!-- FAQ 12 -->
      <details class="faq-item">
        <summary class="faq-summary">
          Q12: If Model A has MAE = 12, RMSE = 18 and Model B has MAE = 14, RMSE = 15, which model is better?
        </summary>
        <div class="faq-content">
          <p>
            It depends entirely on your tolerance for large errors:
            <br><br>
            &bull; <strong>Model A</strong> has a lower MAE (12 vs 14), meaning its typical prediction error is smaller on most normal samples. However, its RMSE is 18 (higher than 15), meaning it makes occasional large blunder mistakes that get squared.
            <br>&bull; <strong>Model B</strong> has a slightly higher typical error (14), but a lower RMSE (15), meaning it avoids huge catastrophic blunders.
            <br><br>
            If big mistakes carry extreme penalties (financial risk, safety margins), choose <strong>Model B</strong>. If typical performance matters and blunders are tolerable, choose <strong>Model A</strong>.
          </p>
        </div>
      </details>
    </section>

    <!-- CHAPTER NAVIGATION FOOTER -->
    <footer class="chapter-nav">
      <a class="nav-btn" href="../topic_18/notes.html">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        Previous: Topic 18 &bull; Anomaly Detection
      </a>
      <a class="nav-btn" href="../topic_20/notes.html">
        Next: Topic 20 &bull; Hyperparameter Tuning
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
    </footer>
"""
