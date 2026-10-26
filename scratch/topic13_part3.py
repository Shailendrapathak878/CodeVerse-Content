"""
Topic 13: Support Vector Machine (SVM) - Part 3
Contains Sections 11 to 15.
"""

from scratch.topic13_svgs import (
    SVG_KERNEL_COMPARISON,
    SVG_RBF_GAMMA_COMPARISON,
    SVG_FEATURE_SCALING_EFFECT,
    SVG_SVM_WORKFLOW,
    SVG_CLASS_DISTRIBUTION,
    SVG_TRAIN_VAL_PERFORMANCE
)

TOPIC13_PART3 = """
  <!-- SECTION 11 -->
  <section id="sec-11" class="section-card">
    <div class="section-badge">Section 11</div>
    <h2 class="section-title">Visualizing Different Kernels in Action</h2>
    <p class="section-lead">
      To truly understand how kernels alter the decision boundary, let us fit three different SVM models on the exact same non-linear, concentric circle dataset (<code>make_circles</code>). 
      Watch how the geometric manifold adapts to the data topology!
    </p>

    <div class="figure-container">
      __SVG_KERNEL_COMPARISON__
      <div class="figure-caption">
        <strong>Figure 13.8: Kernel Comparison on Concentric Non-Linear Dataset.</strong> The Linear kernel is fundamentally incapable of separating concentric rings (54.0% test accuracy). The Polynomial kernel (d=2) forms a quadratic ellipse, and the RBF kernel forms an optimal radial boundary (both achieving 100.0% test accuracy).
      </div>
    </div>

    <h3 class="sub-title">1. Empirical Performance Breakdown on Concentric Dataset</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Kernel</th>
            <th>Scikit-Learn Formulation</th>
            <th>Support Vectors</th>
            <th>Train Accuracy</th>
            <th>Test Accuracy</th>
            <th>Visual Geometric Shape</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Linear</strong></td>
            <td><code>SVC(kernel='linear')</code></td>
            <td><strong>150 / 150</strong> (100%)</td>
            <td>54.67%</td>
            <td><strong>54.00%</strong></td>
            <td>A flat, straight line cutting across the circles. Complete underfitting.</td>
          </tr>
          <tr>
            <td><strong>Polynomial (d=2)</strong></td>
            <td><code>SVC(kernel='poly', degree=2)</code></td>
            <td><strong>24 / 150</strong> (16.0%)</td>
            <td>100.0%</td>
            <td><strong>100.0%</strong></td>
            <td>A smooth ellipse enclosing the inner core points perfectly.</td>
          </tr>
          <tr>
            <td><strong>RBF (Gaussian)</strong></td>
            <td><code>SVC(kernel='rbf', gamma=1.0)</code></td>
            <td><strong>38 / 150</strong> (25.3%)</td>
            <td>100.0%</td>
            <td><strong>100.0%</strong></td>
            <td>A radial circular contour wrapping the inner cluster seamlessly.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 12 -->
  <section id="sec-12" class="section-card">
    <div class="section-badge">Section 12</div>
    <h2 class="section-title">Understanding Gamma (γ) in RBF SVM</h2>
    <p class="section-lead">
      While the <code>C</code> parameter controls margin softness, the <strong><code>gamma</code> (&gamma;)</strong> parameter controls the <strong>radius of influence</strong> of individual training observations in the RBF kernel. 
      Tuning gamma is the primary tool for balancing bias and variance in non-linear SVMs.
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; The Role of Gamma in the RBF Kernel</div>
      <div class="math-display">K(x, z) = exp( -γ ∥x - z∥² ) = exp( - ∥x - z∥² / (2σ²) )</div>
      <div class="formula-legend">
        <div class="legend-item"><span class="legend-symbol">&gamma; = 1 / (2&sigma;²)</span><span>Inverse variance of the Gaussian distribution</span></div>
        <div class="legend-item"><span class="legend-symbol">High &gamma;</span><span>Tiny radius of influence (&sigma; is small) &rarr; highly localized pockets</span></div>
        <div class="legend-item"><span class="legend-symbol">Low &gamma;</span><span>Huge radius of influence (&sigma; is large) &rarr; smooth, broad influence</span></div>
      </div>
    </div>

    <div class="figure-container">
      __SVG_RBF_GAMMA_COMPARISON__
      <div class="figure-caption">
        <strong>Figure 13.9: RBF Gamma Parameter (&gamma;) Across Three Scales.</strong> Small <code>&gamma; = 0.1</code> creates a broad, smooth boundary. Moderate <code>&gamma; = 1.0</code> achieves optimal generalization. High <code>&gamma; = 10.0</code> fits isolated island pockets around individual data points (severe overfitting).
      </div>
    </div>

    <h3 class="sub-title">1. The Gamma Sensitivity Spectrum</h3>
    <div class="grid-2col">
      <div class="def-box">
        <div class="def-title"><span>&#128313;</span> Small Gamma (e.g. &gamma; = 0.01 or 0.1)</div>
        <p><strong>Behavior:</strong> Each support vector exerts influence over a huge, expansive radius.</p>
        <ul style="margin-left: 1.25rem; font-size: 0.92rem; color: var(--def-card-text);">
          <li>Points far apart still have non-zero similarity.</li>
          <li>Produces a <strong>smooth, broad, gentle</strong> decision surface.</li>
          <li>Acts almost like a linear classifier when &gamma; approaches 0.</li>
          <li><strong>High bias, low variance</strong> (may underfit complex data).</li>
        </ul>
      </div>

      <div class="warn-box">
        <div class="warn-title"><span>&#128314;</span> Large Gamma (e.g. &gamma; = 10 or 100)</div>
        <p><strong>Behavior:</strong> Each support vector exerts influence only in its immediate tiny neighborhood.</p>
        <ul style="margin-left: 1.25rem; font-size: 0.92rem; color: var(--warn-card-text);">
          <li>Similarity drops to zero just a tiny distance away.</li>
          <li>Draws tight, jagged circles ("islands") around individual points.</li>
          <li>Training accuracy often reaches 100%, but test accuracy collapses.</li>
          <li><strong>Low bias, high variance</strong> (classic catastrophic overfitting).</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SECTION 13 -->
  <section id="sec-13" class="section-card">
    <div class="section-badge">Section 13</div>
    <h2 class="section-title">Feature Scaling for Support Vector Machines</h2>
    <p class="section-lead">
      If there is one absolute rule in applied machine learning, it is this: <strong>Support Vector Machines require feature scaling!</strong> 
      Skipping feature scaling before training an SVM is the single most common cause of broken models in industry.
    </p>

    <div class="figure-container">
      __SVG_FEATURE_SCALING_EFFECT__
      <div class="figure-caption">
        <strong>Figure 13.10: Before vs. After Feature Scaling in SVM.</strong> Unscaled features (Income $100k vs Age 40) distort Euclidean distance, causing the algorithm to ignore Age entirely (88.0% test accuracy). Standardization brings both axes into isotropic balance (100.0% test accuracy).
      </div>
    </div>

    <h3 class="sub-title">1. Why Are SVMs Scale-Dependent?</h3>
    <p>
      Unlike Decision Trees (which only perform horizontal/vertical cuts on individual features), SVM computes <strong>Euclidean distances</strong> <code>∥x - z∥² = &sum; (x_j - z_j)²</code> and dot products <code>xᵀz = &sum; x_j z_j</code> across all dimensions simultaneously:
    </p>
    <ul style="margin-left: 1.5rem; margin-top: 0.5rem; color: var(--text-secondary);">
      <li>Suppose Feature 1 is <strong>Annual Salary</strong> ($30,000 to $120,000) and Feature 2 is <strong>Years of Experience</strong> (1 to 15 years).</li>
      <li>A salary difference of $10,000 yields <code>(&Delta;x₁)² = 10,000² = 100,000,000</code>.</li>
      <li>An experience difference of 5 years yields <code>(&Delta;x₂)² = 5² = 25</code>.</li>
      <li>The algorithm views 100,000,000 as vastly more important than 25, completely ignoring Experience!</li>
    </ul>

    <h3 class="sub-title">2. Mathematical Standardization Formula</h3>
    <div class="formula-block">
      <div class="formula-header">&#128290; Z-Score Feature Standardization</div>
      <div class="math-display">z = (x - μ) / σ</div>
      <div class="formula-legend">
        <div class="legend-item"><span class="legend-symbol">x</span><span>Raw input feature value</span></div>
        <div class="legend-item"><span class="legend-symbol">&mu;</span><span>Sample mean of the feature on the training split</span></div>
        <div class="legend-item"><span class="legend-symbol">&sigma;</span><span>Sample standard deviation of the feature on the training split</span></div>
      </div>
    </div>

    <div class="calc-box">
      <div class="calc-step">
        <div class="step-title">Worked Numerical Standardization Example:</div>
        <p>Suppose a student scores <code>x = 72.0</code> on an entrance exam where the training set mean is <code>&mu; = 50.0</code> and standard deviation is <code>&sigma; = 10.0</code>.</p>
        <p><code>z = (72.0 - 50.0) / 10.0 = 22.0 / 10.0 = +2.2000</code></p>
        <p><em>Interpretation:</em> The student performed exactly 2.2 standard deviations above the average cohort.</p>
      </div>
    </div>

    <div class="warn-box">
      <div class="warn-title"><span>&#9888;&#65039;</span> The Golden Data Leakage Rule of Feature Scaling</div>
      <p>
        <strong>NEVER fit the scaler on the entire dataset before train/test splitting!</strong> 
        Fitting <code>StandardScaler</code> on the combined dataset leaks test set statistics (&mu; and &sigma;) into the training process, invalidating your test metrics. 
        Always fit the scaler strictly on <code>X_train</code>, and use it to transform <code>X_test</code> without refitting. 
        The easiest, most robust way to enforce this in production is by bundling both in a scikit-learn <code>Pipeline</code>.
      </p>
    </div>
  </section>

  <!-- SECTION 14 -->
  <section id="sec-14" class="section-card">
    <div class="section-badge">Section 14</div>
    <h2 class="section-title">SVM Classification Workflow</h2>
    <p class="section-lead">
      To build production-grade SVM models, machine learning engineers follow a standardized, rigorous 11-step pipeline that prevents data leakage and ensures reliable generalization.
    </p>

    <div class="figure-container">
      __SVG_SVM_WORKFLOW__
      <div class="figure-caption">
        <strong>Figure 13.15: The End-to-End SVM Machine Learning Pipeline.</strong> Data preparation, stratified splitting, pipeline encapsulation with <code>StandardScaler</code>, 5-Fold cross-validation hyperparameter tuning on train data only, and unbiased holdout test evaluation.
      </div>
    </div>

    <h3 class="sub-title">The 11 Step Execution Protocol</h3>
    <ol style="margin-left: 1.5rem; line-height: 1.7; color: var(--text-secondary);">
      <li><strong>Dataset Formulation:</strong> Inspect feature distributions, check for missing values, and verify target labels.</li>
      <li><strong>Target Stratification:</strong> Partition dataset into training (80%) and holdout test (20%) using <code>stratify=y</code> to preserve class ratios.</li>
      <li><strong>Data Leakage Quarantine:</strong> Lock away the holdout test set completely until final validation.</li>
      <li><strong>Encapsulate Pipeline:</strong> Wrap <code>StandardScaler()</code> and <code>SVC()</code> inside a unified <code>Pipeline</code> object.</li>
      <li><strong>Select Kernel Family:</strong> Choose <code>linear</code> for high-dimensional/sparse data or <code>rbf</code> for general non-linear problems.</li>
      <li><strong>Define Hyperparameter Grid:</strong> Establish search candidate ranges for <code>C &isin; [0.01, 0.1, 1.0, 10.0, 100.0]</code> and <code>gamma</code>.</li>
      <li><strong>K-Fold Cross-Validation:</strong> Evaluate candidate parameters strictly on the training partition using 5-Fold cross-validation.</li>
      <li><strong>Select Optimal Configuration:</strong> Identify the hyperparameter set with the highest mean validation score.</li>
      <li><strong>Fit Final Model:</strong> Retrain the winning pipeline on 100% of the training partition.</li>
      <li><strong>Single Holdout Inference:</strong> Pass the untouched holdout test partition through the pipeline to generate test predictions.</li>
      <li><strong>Comprehensive Evaluation:</strong> Generate the confusion matrix and compute Accuracy, Precision, Recall, and F1-Score.</li>
    </ol>
  </section>

  <!-- SECTION 15 -->
  <section id="sec-15" class="section-card">
    <div class="section-badge">Section 15</div>
    <h2 class="section-title">Complete Python Classification Lab</h2>
    <p class="section-lead">
      Let us execute an end-to-end, fully reproducible classification lab in Python. 
      We simulate university admissions for <code>N = 240</code> applicants based on Exam Score and Project Score. 
      We enforce strict anti-leakage splitting, 5-Fold CV hyperparameter tuning, holdout testing, and assert pipeline sanity.
    </p>

    <div class="figure-container">
      __SVG_CLASS_DISTRIBUTION__
      <div class="figure-caption">
        <strong>Figure 13.12: Admissions Dataset Class Distribution.</strong> 240 university applicant records with a balanced 50/50 target split (120 Admitted vs. 120 Rejected).
      </div>
    </div>

    <div class="code-container">
      <div class="code-header">
        <span>PYTHON 3 (COMPLETE RUNNABLE LAB)</span>
        <span>StandardScaler + SVC Pipeline</span>
      </div>
      <pre><code>import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

# =========================================================
# STEP 1: Reproducible Dataset Generation (N = 240)
# =========================================================
np.random.seed(42)
n_samples = 240

# Class 0: Rejected applicants (lower scores)
c0_exam = np.random.normal(loc=54.0, scale=9.5, size=n_samples // 2)
c0_proj = np.random.normal(loc=52.0, scale=10.0, size=n_samples // 2)
y_c0 = np.zeros(n_samples // 2, dtype=int)

# Class 1: Admitted applicants (higher scores)
c1_exam = np.random.normal(loc=76.0, scale=9.5, size=n_samples // 2)
c1_proj = np.random.normal(loc=74.0, scale=10.0, size=n_samples // 2)
y_c1 = np.ones(n_samples // 2, dtype=int)

X1 = np.clip(np.concatenate([c0_exam, c1_exam]), 30.0, 100.0)
X2 = np.clip(np.concatenate([c0_proj, c1_proj]), 30.0, 100.0)
X = np.column_stack([X1, X2])
y = np.concatenate([y_c0, y_c1])

df = pd.DataFrame({
    'Exam_Score': np.round(X1, 1),
    'Project_Score': np.round(X2, 1),
    'Admitted': y
})

print(f"Generated Dataset Shape: {df.shape}")
print(f"Class Distribution:\\n{df['Admitted'].value_counts()}")

# =========================================================
# STEP 2: Stratified Train / Test Partition (80/20)
# =========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
print(f"Train samples: {len(X_train)} | Test samples: {len(X_test)}")

# =========================================================
# STEP 3: Hyperparameter Selection via 5-Fold Cross-Validation
# =========================================================
candidate_C = [0.01, 0.1, 1.0, 10.0, 100.0]
cv_scores = {}

print("\\nEvaluating Candidate C values using 5-Fold CV on Training Data:")
for c in candidate_C:
    pipe_eval = Pipeline([
        ('scaler', StandardScaler()),
        ('svc', SVC(kernel='rbf', C=c, random_state=42))
    ])
    scores = cross_val_score(pipe_eval, X_train, y_train, cv=5, scoring='accuracy')
    cv_scores[c] = scores.mean()
    print(f"  C = {c:6.2f} -> Mean CV Accuracy: {scores.mean():.4f} (std: {scores.std():.4f})")

best_C = max(cv_scores, key=cv_scores.get)
print(f"\\nOptimal C selected via CV: {best_C} (CV Accuracy: {cv_scores[best_C]:.4f})")

# =========================================================
# STEP 4: Fit Final Production Pipeline on Full Training Split
# =========================================================
final_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42))
])
final_pipeline.fit(X_train, y_train)

# =========================================================
# STEP 5: Single Unbiased Holdout Test Set Evaluation
# =========================================================
y_pred = final_pipeline.predict(X_test)

test_acc = accuracy_score(y_test, y_pred)
test_prec = precision_score(y_test, y_pred)
test_rec = recall_score(y_test, y_pred)
test_f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

print(f"\\n--- Holdout Test Performance (N = {len(y_test)}) ---")
print(f"Test Accuracy:  {test_acc:.4f} ({test_acc*100:.1f}%)")
print(f"Test Precision: {test_prec:.4f} ({test_prec*100:.1f}%)")
print(f"Test Recall:    {test_rec:.4f} ({test_rec*100:.1f}%)")
print(f"Test F1-Score:  {test_f1:.4f} ({test_f1*100:.1f}%)")
print(f"\\nConfusion Matrix:\\n{cm}")

# Support Vectors Inspection
fitted_svc = final_pipeline.named_steps['svc']
n_sv = fitted_svc.support_vectors_.shape[0]
print(f"\\nTotal Support Vectors: {n_sv} / {len(X_train)} ({n_sv/len(X_train)*100:.1f}%)")
print(f"Support Vectors per Class: {fitted_svc.n_support_}")

# Robust Pipeline Assertions
assert test_acc &gt;= 0.85, "Accuracy below acceptable production threshold!"
assert test_f1 &gt;= 0.85, "F1-Score below acceptable production threshold!"
assert len(fitted_svc.support_) == n_sv, "Support vector indices mismatch!"
print("\\n[SUCCESS] All pipeline assertions and evaluations verified!")</code></pre>
    </div>

    <div class="figure-container">
      __SVG_TRAIN_VAL_PERFORMANCE__
      <div class="figure-caption">
        <strong>Figure 13.11: Training vs. Validation Performance Across C Candidates.</strong> 5-Fold cross-validation confirms that <code>C = 0.1 to 1.0</code> achieves peak validation accuracy (97.4%). Larger C values overfit to training noise.
      </div>
    </div>

    <div class="code-container">
      <div class="code-header">
        <span>CONSOLE OUTPUT</span>
        <span>Verified Python 3 Runtime Results</span>
      </div>
      <pre><code>Generated Dataset Shape: (240, 3)
Class Distribution:
Admitted
0    120
1    120
Name: count, dtype: int64
Train samples: 192 | Test samples: 48

Evaluating Candidate C values using 5-Fold CV on Training Data:
  C =   0.01 -> Mean CV Accuracy: 0.7791 (std: 0.2383)
  C =   0.10 -> Mean CV Accuracy: 0.9741 (std: 0.0162)
  C =   1.00 -> Mean CV Accuracy: 0.9690 (std: 0.0251)
  C =  10.00 -> Mean CV Accuracy: 0.9584 (std: 0.0264)
  C = 100.00 -> Mean CV Accuracy: 0.9532 (std: 0.0103)

Optimal C selected via CV: 0.1 (CV Accuracy: 0.9741)

--- Holdout Test Performance (N = 48) ---
Test Accuracy:  0.9167 (91.7%)
Test Precision: 0.8846 (88.5%)
Test Recall:    0.9583 (95.8%)
Test F1-Score:  0.9200 (92.0%)

Confusion Matrix:
[[21  3]
 [ 1 23]]

Total Support Vectors: 32 / 192 (16.7%)
Support Vectors per Class: [16, 16]

[SUCCESS] All pipeline assertions and evaluations verified!</code></pre>
    </div>

    <div class="warn-box">
      <div class="warn-title"><span>&#9888;&#65039;</span> Limitations of Synthetic Lab Data</div>
      <p>
        While this synthetic dataset cleanly illustrates maximum-margin boundaries and RBF projections, synthetic Gaussian clusters possess perfectly uniform variances and lack real-world complexities. 
        Real tabular data features missing entries, non-linear multi-modal distributions, class imbalance, and concept drift over time. 
        Always validate your SVM pipelines against realistic production data before deployment.
      </p>
    </div>
  </section>
"""
