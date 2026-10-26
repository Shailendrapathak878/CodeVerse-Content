"""
Topic 13: Support Vector Machine (SVM) - Part 4
Contains Sections 16 to 23.
"""

from scratch.topic13_svgs import (
    SVG_CONFUSION_MATRIX_HEATMAP,
    SVG_SVR_REGRESSION
)

TOPIC13_PART4 = """
  <!-- SECTION 16 -->
  <section id="sec-16" class="section-card">
    <div class="section-badge">Section 16</div>
    <h2 class="section-title">Support Vector Regression (SVR)</h2>
    <p class="section-lead">
      While SVM is most famous for classification, its geometric principles adapt elegantly to continuous numerical prediction. 
      This formulation is called <strong>Support Vector Regression (SVR)</strong>.
    </p>

    <div class="figure-container">
      __SVG_SVR_REGRESSION__
      <div class="figure-caption">
        <strong>Figure 13.14: Support Vector Regression (SVR) and the &epsilon;-Insensitive Tube.</strong> SVR fits a continuous curve inside an envelope of width <code>2&epsilon;</code>. Residual errors within the tube are ignored; only observations that touch or breach the tube boundaries become support vectors.
      </div>
    </div>

    <h3 class="sub-title">1. The Epsilon-Insensitive (&epsilon;) Loss Principle</h3>
    <p>
      In Ordinary Least Squares (Linear Regression), every single point's error is squared and penalized, meaning outliers can drastically tug the line. 
      In SVR, Vladimir Vapnik introduced the <strong>&epsilon;-insensitive loss function</strong> <code>L_&epsilon;(y, f(x))</code>:
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; The Epsilon-Insensitive Loss Function</div>
      <div class="math-display">L_ε(y, f(x)) = 0 &nbsp; if |y - f(x)| ≤ ε &nbsp;&nbsp;|&nbsp;&nbsp; |y - f(x)| - ε &nbsp; if |y - f(x)| > ε</div>
      <div class="formula-legend">
        <div class="legend-item"><span class="legend-symbol">&epsilon; (epsilon)</span><span>Tolerance threshold creating an error-free corridor around f(x)</span></div>
        <div class="legend-item"><span class="legend-symbol">Inside Tube</span><span>Any data point with |y - f(x)| &le; &epsilon; contributes zero loss!</span></div>
        <div class="legend-item"><span class="legend-symbol">Outside Tube</span><span>Points outside incur a linear penalty via slack variables &xi;ᵢ and &xi;ᵢ*</span></div>
      </div>
    </div>

    <h3 class="sub-title">2. Fundamental Difference Between SVC and SVR</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Property</th>
            <th>Support Vector Classification (SVC)</th>
            <th>Support Vector Regression (SVR)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Target Variable y</strong></td>
            <td>Discrete categorical labels (e.g. +1 or -1).</td>
            <td>Continuous numerical values (e.g. Price, MPG, Temperature).</td>
          </tr>
          <tr>
            <td><strong>Corridor Role</strong></td>
            <td>Wants the corridor (margin) to be <strong>as empty as possible</strong>.</td>
            <td>Wants as many data points <strong>inside the corridor (&epsilon;-tube) as possible</strong>.</td>
          </tr>
          <tr>
            <td><strong>Support Vectors</strong></td>
            <td>Points on the margin boundary or misclassified across it.</td>
            <td>Points lying <strong>strictly on or outside</strong> the &epsilon;-insensitive tube.</td>
          </tr>
          <tr>
            <td><strong>Key Hyperparameters</strong></td>
            <td><code>C</code>, <code>kernel</code>, <code>gamma</code></td>
            <td><code>C</code>, <code>epsilon</code> (&epsilon;), <code>kernel</code>, <code>gamma</code></td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3 class="sub-title">3. Executable Python SVR Implementation</h3>
    <div class="code-container">
      <div class="code-header">
        <span>PYTHON 3: SUPPORT VECTOR REGRESSION</span>
        <span>Vehicle Fuel Efficiency Lab</span>
      </div>
      <pre><code>from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# 1. Generate Non-Linear Engine Size (L) -> Fuel Efficiency (MPG)
np.random.seed(42)
engine_size = np.sort(np.random.uniform(1.2, 5.0, 80))
mpg = 42.0 - 5.5 * engine_size + 0.3 * (engine_size**2) + np.random.normal(0, 1.8, 80)

X_svr = engine_size.reshape(-1, 1)
y_svr = mpg

# 2. Build Scaler + SVR Pipeline
svr_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svr', SVR(kernel='rbf', C=10.0, epsilon=1.5))
])

# 3. Fit Model on Training Partition (60 samples)
svr_pipe.fit(X_svr[:60], y_svr[:60])
y_test_pred = svr_pipe.predict(X_svr[60:])

# 4. Evaluate Holdout Metrics
mae = mean_absolute_error(y_svr[60:], y_test_pred)
rmse = np.sqrt(mean_squared_error(y_svr[60:], y_test_pred))
n_sv = svr_pipe.named_steps['svr'].support_vectors_.shape[0]

print(f"SVR Holdout MAE:  {mae:.2f} MPG")
print(f"SVR Holdout RMSE: {rmse:.2f} MPG")
print(f"Support Vectors Violating Tube: {n_sv} / 60 training points")

# Predict MPG for a 2.5L engine
pred_mpg = svr_pipe.predict([[2.5]])[0]
print(f"Estimated MPG for 2.5L Engine: {pred_mpg:.2f} MPG")</code></pre>
    </div>

    <div class="code-container">
      <div class="code-header">
        <span>CONSOLE OUTPUT</span>
        <span>Verified Python 3 Runtime Results</span>
      </div>
      <pre><code>SVR Holdout MAE:  1.37 MPG
SVR Holdout RMSE: 1.80 MPG
Support Vectors Violating Tube: 27 / 60 training points
Estimated MPG for 2.5L Engine: 29.47 MPG</code></pre>
    </div>
  </section>

  <!-- SECTION 17 -->
  <section id="sec-17" class="section-card">
    <div class="section-badge">Section 17</div>
    <h2 class="section-title">Classification Evaluation Metrics &amp; Confusion Matrix</h2>
    <p class="section-lead">
      Evaluating a classifier goes far beyond reporting a single overall accuracy figure. 
      To understand the real-world reliability of an SVM, we inspect the <strong>Confusion Matrix</strong> and its four derived metrics.
    </p>

    <div class="figure-container">
      __SVG_CONFUSION_MATRIX_HEATMAP__
      <div class="figure-caption">
        <strong>Figure 13.13: Holdout Test Set Confusion Matrix (N = 48).</strong> Visual breakdown of true outcomes vs. SVM predictions. Out of 48 held-out test students, the model correctly identified 21 rejections (TN) and 23 admissions (TP), while making 3 False Positives and only 1 False Negative.
      </div>
    </div>

    <h3 class="sub-title">1. The Four Confusion Matrix Quadrants</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Metric Symbol</th>
            <th>Engineering Name</th>
            <th>Student Admissions Context</th>
            <th>Observed Count</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>TN</strong></td>
            <td>True Negative</td>
            <td>Applicant was truly Rejected and predicted as Rejected.</td>
            <td><strong>21</strong></td>
          </tr>
          <tr>
            <td><strong>FP</strong></td>
            <td>False Positive (Type I Error)</td>
            <td>Applicant was Rejected, but model predicted Admitted.</td>
            <td><strong>3</strong></td>
          </tr>
          <tr>
            <td><strong>FN</strong></td>
            <td>False Negative (Type II Error)</td>
            <td>Applicant was Admitted, but model missed and predicted Rejected.</td>
            <td><strong>1</strong></td>
          </tr>
          <tr>
            <td><strong>TP</strong></td>
            <td>True Positive</td>
            <td>Applicant was truly Admitted and predicted as Admitted.</td>
            <td><strong>23</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3 class="sub-title">2. Mathematical Derivations of Derived Metrics</h3>
    <div class="grid-2col">
      <div class="formula-block">
        <div class="formula-header">&#128290; Accuracy</div>
        <div class="math-display">Accuracy = (TP + TN) / (TP + TN + FP + FN) = (23 + 21) / 48 = 91.67%</div>
        <p style="font-size: 0.88rem; color: var(--text-secondary);">Measures overall fraction of correct predictions across all classes.</p>
      </div>

      <div class="formula-block">
        <div class="formula-header">&#128290; Precision</div>
        <div class="math-display">Precision = TP / (TP + FP) = 23 / (23 + 3) = 23 / 26 = 88.46%</div>
        <p style="font-size: 0.88rem; color: var(--text-secondary);">Of all applicants the model admitted, 88.5% were genuinely qualified.</p>
      </div>
    </div>

    <div class="grid-2col">
      <div class="formula-block">
        <div class="formula-header">&#128290; Recall (Sensitivity)</div>
        <div class="math-display">Recall = TP / (TP + FN) = 23 / (23 + 1) = 23 / 24 = 95.83%</div>
        <p style="font-size: 0.88rem; color: var(--text-secondary);">Of all genuinely qualified applicants, the model captured 95.8%!</p>
      </div>

      <div class="formula-block">
        <div class="formula-header">&#128290; F1-Score (Harmonic Mean)</div>
        <div class="math-display">F1-Score = 2 × (Precision × Recall) / (Precision + Recall) = 92.00%</div>
        <p style="font-size: 0.88rem; color: var(--text-secondary);">Harmonic balance penalizing extreme imbalances between Precision and Recall.</p>
      </div>
    </div>
  </section>

  <!-- SECTION 18 -->
  <section id="sec-18" class="section-card">
    <div class="section-badge">Section 18</div>
    <h2 class="section-title">Advantages and Limitations of SVM</h2>
    <p class="section-lead">
      No algorithm is a silver bullet. An experienced machine learning practitioner chooses SVM based on a clear-eyed understanding of its unique strengths and practical constraints.
    </p>

    <div class="grid-2col">
      <div>
        <h3 class="sub-title" style="color: #059669; border-color: #A7F3D0;">Key Advantages</h3>
        <ul style="margin-left: 1.25rem; line-height: 1.7; color: var(--text-secondary);">
          <li><strong>Superior High-Dimensional Performance:</strong> SVM excels when the number of features exceeds the number of samples (D &gt; N), such as genomic microarray data and text classification.</li>
          <li><strong>Memory Efficient (Sparse Solution):</strong> Once trained, the model only stores the support vectors; the rest of the dataset can be discarded.</li>
          <li><strong>Maximum Margin Robustness:</strong> Maximizing the margin provides theoretical guarantees against overfitting on moderate-sized data.</li>
          <li><strong>Non-Linear Flexibility:</strong> The kernel trick allows SVM to model complex decision boundaries without computing explicit high-dimensional coordinates.</li>
          <li><strong>Global Convex Optimum:</strong> Because SVM solves a convex quadratic programming problem, it has no local minima (unlike Neural Networks).</li>
        </ul>
      </div>

      <div>
        <h3 class="sub-title" style="color: #DC2626; border-color: #FECACA;">Critical Limitations</h3>
        <ul style="margin-left: 1.25rem; line-height: 1.7; color: var(--text-secondary);">
          <li><strong>Poor Scalability to Massive Datasets:</strong> Training dual SVM scales between O(N²) and O(N³). Training on datasets with N &gt; 100,000 samples becomes prohibitively slow.</li>
          <li><strong>Mandatory Feature Scaling:</strong> Extremely sensitive to feature magnitudes. Forgetting standardization breaks the algorithm.</li>
          <li><strong>Black-Box Non-Linear Kernels:</strong> While a linear SVM provides interpretable weights <code>w</code>, RBF and polynomial kernels obscure the physical meaning of decision boundaries.</li>
          <li><strong>No Native Probabilities:</strong> Standard <code>SVC</code> outputs geometric distances, not calibrated probabilities. Enabling <code>probability=True</code> requires expensive Platt scaling via 5-fold cross-validation.</li>
          <li><strong>Hyperparameter Sensitivity:</strong> Requires careful joint tuning of <code>C</code> and <code>gamma</code> via cross-validation to prevent overfitting.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SECTION 19 -->
  <section id="sec-19" class="section-card">
    <div class="section-badge">Section 19</div>
    <h2 class="section-title">SVM Compared With Other Supervised Algorithms</h2>
    <p class="section-lead">
      How does Support Vector Machine stack up against the other major classifiers in your toolkit? 
      Review this comparative matrix to choose the right tool for each project.
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Comparison Dimension</th>
            <th>Support Vector Machine (SVM)</th>
            <th>Logistic Regression</th>
            <th>K-Nearest Neighbors (KNN)</th>
            <th>Decision Tree</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Core Mechanism</strong></td>
            <td>Finds maximum-margin separating hyperplane via support vectors.</td>
            <td>Models log-odds probability via a linear sigmoid function.</td>
            <td>Computes majority vote among K nearest neighbors in feature space.</td>
            <td>Partitions feature space into orthogonal rectangles using greedy if-else rules.</td>
          </tr>
          <tr>
            <td><strong>Decision Boundary</strong></td>
            <td>Linear (linear kernel) or smooth curved manifolds (RBF / Poly).</td>
            <td>Strictly linear (unless polynomial features are manually engineered).</td>
            <td>Highly irregular, non-linear, locally adaptive contours.</td>
            <td>Orthogonal, step-like axis-aligned rectangular boxes.</td>
          </tr>
          <tr>
            <td><strong>Feature Scaling</strong></td>
            <td><strong>Mandatory:</strong> Euclidean distances and dot products distort unscaled data.</td>
            <td>Recommended for gradient descent convergence and L1/L2 regularization.</td>
            <td><strong>Mandatory:</strong> Distance metrics completely fail without standardization.</td>
            <td><strong>Scale Invariant:</strong> Splitting thresholds are unaffected by monotonic scaling.</td>
          </tr>
          <tr>
            <td><strong>Interpretability</strong></td>
            <td>High for linear kernel; Low (Black Box) for RBF / Poly kernels.</td>
            <td><strong>Very High:</strong> Odds ratios and feature coefficients are easily explained.</td>
            <td>Moderate: Can inspect nearest neighbors, but no global equation.</td>
            <td><strong>Very High:</strong> Visual flowchart readable by non-technical stakeholders.</td>
          </tr>
          <tr>
            <td><strong>Training Speed</strong></td>
            <td>Moderate to Slow: O(N²) to O(N³) with sample count N.</td>
            <td><strong>Very Fast:</strong> Scales linearly with N &times; D.</td>
            <td><strong>Instant (Zero training):</strong> Lazy learner that stores data in memory.</td>
            <td>Fast: O(D &times; N log N) greedy threshold sorting.</td>
          </tr>
          <tr>
            <td><strong>Best Applied When</strong></td>
            <td>Medium-sized complex datasets, high dimensions (text, genomics).</td>
            <td>Baseline classification, calibrated probability output required.</td>
            <td>Small, low-noise datasets where local geometric clustering dominates.</td>
            <td>Tabular business data, categorical features, audit-required workflows.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 20 -->
  <section id="sec-20" class="section-card">
    <div class="section-badge">Section 20</div>
    <h2 class="section-title">Real-Life Case Studies</h2>
    <p class="section-lead">
      Explore four practical case studies demonstrating where SVM thrives in commercial and scientific domains.
    </p>

    <div class="grid-2col">
      <div class="def-box">
        <div class="def-title"><span>&#128231;</span> Case Study 1: Email Spam Filtering</div>
        <p><strong>Scenario:</strong> Classifying incoming emails as Spam (+1) or Ham (-1) based on a vocabulary of 25,000 TF-IDF word frequencies.</p>
        <ul style="margin-left: 1.25rem; font-size: 0.92rem; color: var(--def-card-text);">
          <li><strong>Why Linear SVM:</strong> When feature count is massive (D = 25,000), data is almost always linearly separable. <code>LinearSVC</code> trains in seconds.</li>
          <li><strong>Critical Metric:</strong> <strong>Precision</strong> must be prioritized. A False Positive sends an important job offer to the Spam folder!</li>
        </ul>
      </div>

      <div class="def-box">
        <div class="def-title"><span>&#128065;</span> Case Study 2: Facial Recognition &amp; Image Verification</div>
        <p><strong>Scenario:</strong> Verifying passport holder identity from 128-dimensional facial embedding vectors extracted by deep convolutional networks.</p>
        <ul style="margin-left: 1.25rem; font-size: 0.92rem; color: var(--def-card-text);">
          <li><strong>Why RBF SVM:</strong> Facial embedding spaces contain subtle non-linear manifold relationships. RBF kernel provides high-confidence identity boundaries.</li>
          <li><strong>Critical Metric:</strong> False Accept Rate (FAR) and False Reject Rate (FRR) balanced via threshold tuning.</li>
        </ul>
      </div>
    </div>

    <div class="grid-2col">
      <div class="def-box">
        <div class="def-title"><span>&#128196;</span> Case Study 3: Legal Document Categorization</div>
        <p><strong>Scenario:</strong> Categorizing confidential corporate litigation contracts into regulatory categories (NDAs, Mergers, Compliance).</p>
        <ul style="margin-left: 1.25rem; font-size: 0.92rem; color: var(--def-card-text);">
          <li><strong>Why SVM:</strong> Legal text features high sparsity and high dimensionality. SVM handles sparse matrices natively without dense memory expansion.</li>
          <li><strong>Critical Metric:</strong> Macro F1-Score across imbalanced legal categories.</li>
        </ul>
      </div>

      <div class="warn-box">
        <div class="warn-title"><span>&#9877;&#65039;</span> Case Study 4: Clinical Medical Screening (Hypothetical)</div>
        <p><strong>Scenario:</strong> Screening patients for early-stage diabetic retinopathy based on blood biomarkers and retinal scan features.</p>
        <ul style="margin-left: 1.25rem; font-size: 0.92rem; color: var(--warn-card-text);">
          <li><strong>Why SVM:</strong> High sensitivity and non-linear boundary construction on small-to-medium clinical cohorts.</li>
          <li><strong>Mandatory Governance:</strong> <strong>Recall</strong> is critical (missing a sick patient is catastrophic). <em>Educational disclaimer: Toy SVM models must never replace certified clinical judgment, medical oversight, or FDA-cleared diagnostic software.</em></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SECTION 21 -->
  <section id="sec-21" class="section-card">
    <div class="section-badge">Section 21</div>
    <h2 class="section-title">Required Visual and Diagram Gallery</h2>
    <p class="section-lead">
      Review the 15 hand-crafted vector graphics embedded throughout this chapter, each designed to cement an essential geometric principle.
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Figure #</th>
            <th>Diagram Title</th>
            <th>Section</th>
            <th>Key Practical Takeaway</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fig 13.1</strong></td>
            <td>Two-Class Separating Hyperplane</td>
            <td>Sec 01</td>
            <td>In 2D, the hyperplane is a straight line: <code>w₁x₁ + w₂x₂ + b = 0</code> separating binary classes.</td>
          </tr>
          <tr>
            <td><strong>Fig 13.2</strong></td>
            <td>The Canonical SVM Margin</td>
            <td>Sec 03</td>
            <td>Total margin width is <code>2 / ∥w∥</code>. Maximizing margin equals minimizing <code>½∥w∥²</code>.</td>
          </tr>
          <tr>
            <td><strong>Fig 13.3</strong></td>
            <td>Actual Support Vectors Highlighted</td>
            <td>Sec 04</td>
            <td>Only points on or violating margin boundaries determine hyperplane position (sparse solution).</td>
          </tr>
          <tr>
            <td><strong>Fig 13.4</strong></td>
            <td>Narrow vs. Wide Margin</td>
            <td>Sec 05</td>
            <td>Wide margin boundaries provide vital safety clearance against test-time measurement noise.</td>
          </tr>
          <tr>
            <td><strong>Fig 13.5</strong></td>
            <td>Linear SVM on Separable Data</td>
            <td>Sec 06</td>
            <td>Canonical hard-margin constraints require zero violations: <code>yᵢ(wᵀxᵢ + b) &ge; 1</code>.</td>
          </tr>
          <tr>
            <td><strong>Fig 13.6</strong></td>
            <td>Hard Margin vs. Soft Margin</td>
            <td>Sec 06</td>
            <td>Soft margin introduces slack variables <code>&xi;ᵢ &ge; 0</code> to survive real-world noise without collapsing.</td>
          </tr>
          <tr>
            <td><strong>Fig 13.7</strong></td>
            <td>Decision Boundaries Across C Values</td>
            <td>Sec 07</td>
            <td>Small C gives wide margins (78 SVs); Large C gives narrow margins with strict penalties (23 SVs).</td>
          </tr>
          <tr>
            <td><strong>Fig 13.8</strong></td>
            <td>Kernel Comparison on Non-Linear Data</td>
            <td>Sec 11</td>
            <td>Linear fails (54% acc) on concentric circles; Poly (d=2) and RBF achieve 100% test accuracy.</td>
          </tr>
          <tr>
            <td><strong>Fig 13.9</strong></td>
            <td>RBF Gamma Parameter (&gamma;)</td>
            <td>Sec 12</td>
            <td>Small &gamma; produces smooth contours; Large &gamma; creates isolated island pockets (overfitting).</td>
          </tr>
          <tr>
            <td><strong>Fig 13.10</strong></td>
            <td>Feature Scaling Effect</td>
            <td>Sec 13</td>
            <td>Unscaled features distort Euclidean distance (88% acc); Standardization restores symmetry (100% acc).</td>
          </tr>
          <tr>
            <td><strong>Fig 13.11</strong></td>
            <td>Train vs. Validation Across C Candidates</td>
            <td>Sec 15</td>
            <td>5-Fold CV on train data identifies optimal C = 0.1 to 1.0 (97.4% CV accuracy).</td>
          </tr>
          <tr>
            <td><strong>Fig 13.12</strong></td>
            <td>Class Distribution Bar Chart</td>
            <td>Sec 15</td>
            <td>N = 240 applicant records with a balanced 50/50 target split (120 Admitted vs. 120 Rejected).</td>
          </tr>
          <tr>
            <td><strong>Fig 13.13</strong></td>
            <td>Holdout Test Confusion Matrix</td>
            <td>Sec 17</td>
            <td>N = 48 holdout test evaluations: TN=21, FP=3, FN=1, TP=23 (Accuracy 91.7%, F1 92.0%).</td>
          </tr>
          <tr>
            <td><strong>Fig 13.14</strong></td>
            <td>Support Vector Regression (SVR)</td>
            <td>Sec 16</td>
            <td>SVR ignores errors inside the &epsilon;-tube (width 2&epsilon;); only tube boundary violators become SVs.</td>
          </tr>
          <tr>
            <td><strong>Fig 13.15</strong></td>
            <td>End-to-End SVM Pipeline Flowchart</td>
            <td>Sec 14</td>
            <td>Standardized 11-step protocol preventing data leakage via encapsulated scikit-learn pipelines.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 22 -->
  <section id="sec-22" class="section-card">
    <div class="section-badge">Section 22</div>
    <h2 class="section-title">12 Common Beginner Mistakes and How to Avoid Them</h2>
    <p class="section-lead">
      Learn from the missteps of others. Review these 12 pervasive mistakes made by students and novice practitioners, along with their concrete engineering solutions.
    </p>

    <!-- Mistake 1 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 1: Confusing the Hyperplane with the Margin</div>
      <div class="mistake-body"><strong>The Error:</strong> Using the terms "hyperplane" and "margin" interchangeably.</div>
      <div class="fix-box"><strong>The Fix:</strong> The <em>hyperplane</em> is the zero-decision line (<code>wᵀx + b = 0</code>). The <em>margin</em> is the physical cushion/buffer zone of width <code>2/∥w∥</code> separating the positive and negative margin planes.</div>
    </div>

    <!-- Mistake 2 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 2: Assuming All Training Points Are Support Vectors</div>
      <div class="mistake-body"><strong>The Error:</strong> Believing that every point in the training set contributes to the mathematical boundary equation.</div>
      <div class="fix-box"><strong>The Fix:</strong> Only points lying on or violating the margin boundaries are support vectors (typically 10% to 30% of data). Points far from the margin can be removed without moving the boundary!</div>
    </div>

    <!-- Mistake 3 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 3: Skipping Feature Standardization</div>
      <div class="mistake-body"><strong>The Error:</strong> Feeding raw features with wildly different numerical magnitudes (e.g., Salary $80,000 and Age 25) directly into an SVM.</div>
      <div class="fix-box"><strong>The Fix:</strong> SVM is distance-dependent. Always wrap <code>StandardScaler()</code> and <code>SVC()</code> inside a scikit-learn <code>Pipeline</code> so all features possess zero mean and unit variance.</div>
    </div>

    <!-- Mistake 4 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 4: Fitting the Scaler on the Entire Dataset Before Splitting</div>
      <div class="mistake-body"><strong>The Error:</strong> Calling <code>scaler.fit_transform(X)</code> on the full dataset before calling <code>train_test_split()</code>.</div>
      <div class="fix-box"><strong>The Fix:</strong> This causes severe <em>data leakage</em>. Fit the scaler strictly on <code>X_train</code> only, then use it to transform <code>X_test</code>. Using a Pipeline guarantees zero leakage automatically.</div>
    </div>

    <!-- Mistake 5 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 5: Believing a Larger C Always Improves the Model</div>
      <div class="mistake-body"><strong>The Error:</strong> Cranking <code>C = 10,000</code> because training accuracy reaches 100%.</div>
      <div class="fix-box"><strong>The Fix:</strong> Very large C severely penalizes margin violations, forcing the margin to become razor-thin and memorizing noise/outliers (overfitting). Tune C via cross-validation.</div>
    </div>

    <!-- Mistake 6 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 6: Believing a Larger Gamma Always Improves RBF SVM</div>
      <div class="mistake-body"><strong>The Error:</strong> Setting <code>gamma = 50.0</code> to force the model to capture intricate boundaries.</div>
      <div class="fix-box"><strong>The Fix:</strong> High gamma creates tiny, tight circular "islands" around individual training points. It memorizes training data but fails catastrophically on test observations.</div>
    </div>

    <!-- Mistake 7 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 7: Tuning Hyperparameters on the Final Test Set</div>
      <div class="mistake-body"><strong>The Error:</strong> Testing different combinations of C and gamma on the holdout test set and picking the highest scoring one.</div>
      <div class="fix-box"><strong>The Fix:</strong> This contaminates the test set. Perform hyperparameter tuning strictly on the training partition using K-Fold cross-validation, and evaluate on the test set exactly once.</div>
    </div>

    <!-- Mistake 8 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 8: Treating the Kernel Trick as a Magic Guarantee for All Data</div>
      <div class="mistake-body"><strong>The Error:</strong> Assuming that switching to an RBF kernel guarantees 100% test accuracy on any dataset.</div>
      <div class="fix-box"><strong>The Fix:</strong> Kernels project data into non-linear manifolds, but poor feature engineering, unscaled data, or overlapping distributions will still fail. No kernel cures bad data.</div>
    </div>

    <!-- Mistake 9 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 9: Confusing SVC with SVR</div>
      <div class="mistake-body"><strong>The Error:</strong> Attempting to predict continuous house prices using <code>SVC</code> or class labels with <code>SVR</code>.</div>
      <div class="fix-box"><strong>The Fix:</strong> <code>SVC</code> is for classification (discrete classes). <code>SVR</code> is for regression (continuous targets) utilizing an &epsilon;-insensitive tube.</div>
    </div>

    <!-- Mistake 10 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 10: Assuming SVC Automatically Outputs Calibrated Probabilities</div>
      <div class="mistake-body"><strong>The Error:</strong> Expecting <code>model.predict_proba()</code> to work out of the box with standard <code>SVC()</code>.</div>
      <div class="fix-box"><strong>The Fix:</strong> By default, SVM outputs geometric signed distances via <code>decision_function()</code>. You must explicitly set <code>SVC(probability=True)</code>, which trains an internal logistic regression via 5-fold CV (Platt scaling).</div>
    </div>

    <!-- Mistake 11 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 11: Using Accuracy Alone for Heavily Imbalanced Datasets</div>
      <div class="mistake-body"><strong>The Error:</strong> Celebrating 98% accuracy on a fraud dataset where 98% of transactions are legitimate.</div>
      <div class="fix-box"><strong>The Fix:</strong> A naive model predicting "Not Fraud" achieves 98% accuracy while failing 100% of fraud detections. Use <code>class_weight='balanced'</code> and evaluate Precision, Recall, and F1-Score.</div>
    </div>

    <!-- Mistake 12 -->
    <div class="mistake-card">
      <div class="mistake-header">&#10008; Mistake 12: Treating Synthetic Lab Results as Proof of Production Reliability</div>
      <div class="mistake-body"><strong>The Error:</strong> Assuming a pipeline that achieves 92% accuracy on synthetic Gaussian data will perform identically on messy enterprise data.</div>
      <div class="fix-box"><strong>The Fix:</strong> Real tabular data contains missing records, concept drift, and dirty labels. Always conduct stress testing on live shadow traffic before production rollout.</div>
    </div>
  </section>

  <!-- SECTION 23 -->
  <section id="sec-23" class="section-card">
    <div class="section-badge">Section 23</div>
    <h2 class="section-title">Summary, Comprehensive Glossary &amp; Interactive Revision</h2>
    <p class="section-lead">
      Consolidate everything you have mastered with our chapter summary, a 16-term technical glossary, and 12 interactive revision challenges complete with step-by-step arithmetic and Python solutions.
    </p>

    <h3 class="sub-title">1. Chapter Summary &amp; Deployment Checklist</h3>
    <div class="success-box">
      <div class="success-title">The SVM Production Deployment Checklist</div>
      <ul style="margin-left: 1.25rem; line-height: 1.7; color: var(--success-card-text);">
        <li>&#10003; <strong>Feature Scaling Verified:</strong> Bundled <code>StandardScaler</code> inside a <code>Pipeline</code> so all features possess zero mean and unit variance.</li>
        <li>&#10003; <strong>No Data Leakage:</strong> Scaler and model hyperparameters fitted strictly on <code>X_train</code>; holdout test set quarantined until final evaluation.</li>
        <li>&#10003; <strong>Kernel Selected Strategically:</strong> Used <code>linear</code> for high-dimensional/text data; used <code>rbf</code> for general non-linear numerical problems.</li>
        <li>&#10003; <strong>Hyperparameters Tuned via CV:</strong> Selected optimal <code>C</code> and <code>gamma</code> via 5-Fold cross-validation on training data.</li>
        <li>&#10003; <strong>Support Vector Sparsity Checked:</strong> Inspected <code>clf.support_vectors_</code> to verify the model is not memorizing the entire dataset.</li>
        <li>&#10003; <strong>Balanced Metrics Evaluated:</strong> Reported Precision, Recall, and F1-Score alongside Accuracy to guard against class imbalance illusions.</li>
      </ul>
    </div>

    <h3 class="sub-title">2. Master Glossary of 16 Technical Terms</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Term</th>
            <th>Rigorous Engineering Definition</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Hyperplane</strong></td>
            <td>A flat geometric subspace of dimension (D - 1) separating a D-dimensional feature space: <code>wᵀx + b = 0</code>.</td>
          </tr>
          <tr>
            <td><strong>Margin</strong></td>
            <td>The perpendicular distance between the decision hyperplane and the closest training points of either class (width <code>2/∥w∥</code>).</td>
          </tr>
          <tr>
            <td><strong>Support Vector</strong></td>
            <td>A training observation that lies on or violates the margin boundaries, physically defining the hyperplane position.</td>
          </tr>
          <tr>
            <td><strong>Hard Margin</strong></td>
            <td>An SVM formulation requiring 100% perfect linear separation with zero margin violations (<code>&xi;ᵢ = 0</code>).</td>
          </tr>
          <tr>
            <td><strong>Soft Margin</strong></td>
            <td>An SVM formulation allowing controlled margin violations via slack variables to handle noise and overlapping data.</td>
          </tr>
          <tr>
            <td><strong>Slack Variable (&xi;ᵢ)</strong></td>
            <td>A non-negative penalty measuring the distance by which training observation <code>x_i</code> penetrates or violates the margin boundary.</td>
          </tr>
          <tr>
            <td><strong>C Parameter</strong></td>
            <td>Regularization hyperparameter governing the trade-off between margin width (small C) and training violation penalties (large C).</td>
          </tr>
          <tr>
            <td><strong>Kernel Trick</strong></td>
            <td>Computing high-dimensional dot products <code>⟨&phi;(x), &phi;(z)⟩</code> directly in original coordinates via kernel function <code>K(x, z)</code> without explicit mapping.</td>
          </tr>
          <tr>
            <td><strong>Linear Kernel</strong></td>
            <td>Standard Euclidean inner product <code>K(x, z) = xᵀz</code> constructing a linear decision boundary.</td>
          </tr>
          <tr>
            <td><strong>Polynomial Kernel</strong></td>
            <td>Kernel <code>K(x, z) = (&gamma; xᵀz + r)^d</code> constructing curved, polynomial interaction manifolds of degree d.</td>
          </tr>
          <tr>
            <td><strong>RBF (Gaussian) Kernel</strong></td>
            <td>Kernel <code>K(x, z) = exp(-&gamma; ∥x - z∥²)</code> measuring localized similarity in an infinite-dimensional Hilbert space.</td>
          </tr>
          <tr>
            <td><strong>Gamma (&gamma;)</strong></td>
            <td>The inverse radius of influence in the RBF kernel. High &gamma; yields tight, localized pockets; low &gamma; yields smooth, broad boundaries.</td>
          </tr>
          <tr>
            <td><strong>Standardization</strong></td>
            <td>Z-score transformation <code>z = (x - &mu;) / &sigma;</code> scaling features to zero mean and unit variance.</td>
          </tr>
          <tr>
            <td><strong>Support Vector Regression (SVR)</strong></td>
            <td>Continuous prediction algorithm fitting a regression function inside an &epsilon;-insensitive tube.</td>
          </tr>
          <tr>
            <td><strong>Epsilon Tube (&epsilon;)</strong></td>
            <td>The error-free corridor in SVR where deviations <code>|y - f(x)| &le; &epsilon;</code> incur zero mathematical penalty.</td>
          </tr>
          <tr>
            <td><strong>Sparse Solution</strong></td>
            <td>A property of SVM where only a small subset of training data (support vectors) is required to evaluate future predictions.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3 class="sub-title">3. Interactive Revision Challenges (12 Exercises)</h3>
    <p>Test your understanding by attempting each question before expanding the solution drawer.</p>

    <!-- Q1 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q1: Intuition &bull; How does SVM differ fundamentally from a simple Perceptron?</summary>
      <div class="accordion-content">
        <p><strong>Answer:</strong> A simple Perceptron stops training the instant it finds <em>any</em> line that separates the training classes, even if the line passes fractions of a millimeter away from a data point. In contrast, an SVM explicitly searches for the unique hyperplane that maximizes the <strong>margin</strong> (clearance) between the boundary and the closest training points on both sides.</p>
      </div>
    </details>

    <!-- Q2 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q2: Geometry &bull; What is the dimensionality of a hyperplane in 4-dimensional feature space?</summary>
      <div class="accordion-content">
        <p><strong>Answer:</strong> A hyperplane in any D-dimensional space always has dimension <code>D - 1</code>. In 4D space, the hyperplane is a <strong>3-dimensional flat subspace</strong>.</p>
      </div>
    </details>

    <!-- Q3 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q3: Margin Arithmetic &bull; Calculate the margin width for weight vector w = [3.0, 4.0]ᵀ.</summary>
      <div class="accordion-content">
        <p><strong>Step-by-Step Solution:</strong></p>
        <ol style="margin-left: 1.5rem;">
          <li>Compute Euclidean norm: <code>∥w∥ = √(3.0² + 4.0²) = √(9 + 16) = √(25) = 5.0</code>.</li>
          <li>Apply total margin width formula: <code>Margin Width = 2 / ∥w∥ = 2 / 5.0 = 0.4000 units</code>.</li>
        </ol>
      </div>
    </details>

    <!-- Q4 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q4: Support Vectors &bull; What happens to the hyperplane if you delete 80% of non-support vector training points?</summary>
      <div class="accordion-content">
        <p><strong>Answer:</strong> <strong>Nothing happens! The hyperplane remains 100% identical.</strong> Only support vectors exert mathematical pull on the boundary. Points outside the margin corridor have zero dual lagrange multiplier weights (<code>&alpha;ᵢ = 0</code>).</p>
      </div>
    </details>

    <!-- Q5 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q5: Hard vs. Soft Margin &bull; Why is hard-margin SVM rarely used in real-world engineering?</summary>
      <div class="accordion-content">
        <p><strong>Answer:</strong> Hard-margin SVM requires 100% linear separability. If even a single outlier or noisy sample overlaps into the other class, the optimization solver crashes with an infeasible error. Soft-margin SVM introduces slack variables (&xi;ᵢ) to tolerate noise gracefully.</p>
      </div>
    </details>

    <!-- Q6 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q6: C Parameter &bull; If an SVM model is severely overfitting the training data, should you increase or decrease C?</summary>
      <div class="accordion-content">
        <p><strong>Answer:</strong> You should <strong>decrease C</strong>. A smaller C places less penalty on training violations and forces the algorithm to prioritize a wider, smoother margin corridor, reducing model variance.</p>
      </div>
    </details>

    <!-- Q7 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q7: Kernel Trick &bull; Compute the RBF kernel similarity between x = [1, 2]ᵀ and z = [4, 6]ᵀ with &gamma; = 0.05.</summary>
      <div class="accordion-content">
        <p><strong>Step-by-Step Solution:</strong></p>
        <ol style="margin-left: 1.5rem;">
          <li>Squared Euclidean distance: <code>∥x - z∥² = (1 - 4)² + (2 - 6)² = (-3)² + (-4)² = 9 + 16 = 25.0</code>.</li>
          <li>RBF Formula: <code>K(x, z) = exp(-&gamma; ∥x - z∥²) = exp(-0.05 &times; 25.0) = exp(-1.25) &approx; 0.2865</code>.</li>
        </ol>
      </div>
    </details>

    <!-- Q8 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q8: Gamma Parameter &bull; What visual effect does setting an excessively large gamma have on an RBF SVM?</summary>
      <div class="accordion-content">
        <p><strong>Answer:</strong> High gamma shrinks each point's radius of influence. The model draws tight, isolated circular "islands" around individual positive points. Training accuracy reaches 100%, but test accuracy collapses (catastrophic overfitting).</p>
      </div>
    </details>

    <!-- Q9 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q9: Data Leakage &bull; Explain why StandardScaler must be fitted on training data only.</summary>
      <div class="accordion-content">
        <p><strong>Answer:</strong> Fitting the scaler on the entire dataset incorporates the mean (&mu;) and standard deviation (&sigma;) of the test partition into the training transformation. This leaks future test statistics into model weights, producing over-optimistic, invalid evaluation metrics.</p>
      </div>
    </details>

    <!-- Q10 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q10: SVR &bull; In Support Vector Regression, what does the &epsilon; parameter control?</summary>
      <div class="accordion-content">
        <p><strong>Answer:</strong> <code>&epsilon;</code> controls the half-width of the <strong>&epsilon;-insensitive tube</strong> centered around the regression curve. Any data point whose residual error is less than or equal to &epsilon; incurs zero loss and is not a support vector.</p>
      </div>
    </details>

    <!-- Q11 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q11: Imbalanced Data &bull; Why is accuracy a dangerous metric for evaluating SVM on fraud detection?</summary>
      <div class="accordion-content">
        <p><strong>Answer:</strong> If only 1% of transactions are fraud, an SVM that labels every transaction as legitimate achieves 99% accuracy while detecting 0 fraudulent events! Practitioners must inspect <strong>Recall</strong> and <strong>F1-Score</strong>, and configure <code>class_weight='balanced'</code>.</p>
      </div>
    </details>

    <!-- Q12 -->
    <details class="accordion-item">
      <summary class="accordion-header">Q12: Python Implementation &bull; Write a 4-line snippet creating a leak-free Scaler + RBF SVM pipeline.</summary>
      <div class="accordion-content">
        <p><strong>Python Solution:</strong></p>
        <div class="code-container">
          <pre><code>from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Create encapsulated leak-free pipeline
pipe = Pipeline([('scaler', StandardScaler()), ('svm', SVC(kernel='rbf', C=1.0, gamma='scale'))])
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)</code></pre>
        </div>
      </div>
    </details>
  </section>
"""
