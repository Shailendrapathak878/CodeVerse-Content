"""
Module: topic7_part3.py
Contains HTML for Sections 9 to 12 of Topic 7: Feature Scaling & Normalization.
"""

from scratch.topic7_svgs import (
    SVG_GRAPH_1_ORIGINAL_RANGES,
    SVG_GRAPH_2_MINMAX_BEFORE_AFTER,
    SVG_GRAPH_3_STANDARDIZATION_BEFORE_AFTER,
    SVG_GRAPH_4_OUTLIER_IMPACT,
    SVG_GRAPH_5_DISTRIBUTION_PRESERVATION,
    SVG_GRAPH_6_VECTOR_NORMALIZATION,
    SVG_GRAPH_7_L1_VS_L2_NORM,
    SVG_GRAPH_8_ALGORITHM_SENSITIVITY,
    SVG_GRAPH_9_DECISION_FLOWCHART,
    SVG_LEAKAGE_WORKFLOW_ARCHITECTURE,
    SVG_SPECIAL_CASES_GRID
)

PART3_HTML = f"""
  <!-- SECTION 9: IMPORTANT GRAPHS AND VISUAL EXPLANATIONS -->
  <section id="sec-09" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 09</span>
      <h2 class="section-title">Important Graphs and Visual Explanations</h2>
    </div>
    <p class="section-intro">
      Visualizing numerical data before and after scaling is essential for diagnosing range disparities, validating mathematical transformations, and verifying that distribution shapes remain uncorrupted.
    </p>

    <!-- GRAPH 1: ORIGINAL FEATURE RANGES -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GRAPH_1_ORIGINAL_RANGES}
      </div>
      <div class="diagram-caption">Graph 1: Original feature ranges across Age (years), Annual Income ($), and Experience (years).</div>
      <div class="how-to-read">
        <div class="how-to-read-title"><span>&#128269;</span> Interpreting Range Disparity:</div>
        <p>
          On a shared raw numerical axis, plotting Age (span 38) alongside Annual Income (span 818,000) causes the Age bar to completely disappear. Separate panel plots with clear axis markings allow us to detect the 21,500&times; order-of-magnitude imbalance that breaks distance-based estimators.
        </p>
      </div>
      <div class="diagram-takeaway">
        <strong>Practical Takeaway:</strong> When features span different physical units, always inspect individual column spans and summary statistics prior to modeling.
      </div>
    </div>

    <!-- GRAPH 5: DISTRIBUTION PRESERVATION -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GRAPH_5_DISTRIBUTION_PRESERVATION}
      </div>
      <div class="diagram-caption">Graph 5: Distribution shape preservation under linear standardization.</div>
      <div class="how-to-read">
        <div class="how-to-read-title"><span>&#128269;</span> How to Read This Distribution Comparison:</div>
        <p>
          Notice how the relative bar heights in the raw histogram (left) are <strong>100% identical</strong> to the standardized histogram (right). Linear scaling shifts the origin and scales the grid lines, but it preserves skewness, kurtosis, and multi-modal clustering.
        </p>
      </div>
      <div class="diagram-takeaway">
        <strong>Mathematical Truth:</strong> Standardizing a non-Gaussian feature does <em>not</em> make it Gaussian. It only ensures zero mean and unit variance.
      </div>
    </div>

    <!-- GRAPH 8: ALGORITHM SENSITIVITY -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GRAPH_8_ALGORITHM_SENSITIVITY}
      </div>
      <div class="diagram-caption">Graph 8: Comprehensive algorithm scale sensitivity taxonomy.</div>
      <div class="how-to-read">
        <div class="how-to-read-title"><span>&#128269;</span> Grouping Rationale:</div>
        <ul>
          <li><strong>Red Group (Mandatory):</strong> KNN, K-Means, SVM, PCA calculate raw geometric distances or covariances. Unscaled features guarantee failure.</li>
          <li><strong>Amber Group (Recommended):</strong> Regularized linear models and Neural Networks converge faster and avoid regularizing small-scale weights unfairly.</li>
          <li><strong>Green Group (Invariant):</strong> Decision trees and boosted ensembles evaluate monotonic rank splits; scaling neither improves nor hurts tree splits.</li>
        </ul>
      </div>
    </div>

    <!-- GRAPH 9: DECISION FLOWCHART -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GRAPH_9_DECISION_FLOWCHART}
      </div>
      <div class="diagram-caption">Graph 9: Production Feature Scaling Decision Flowchart.</div>
      <div class="how-to-read">
        <div class="how-to-read-title"><span>&#128269;</span> Using the Flowchart:</div>
        <p>
          Follow the decision nodes sequentially: First confirm if a tree-based model is used (no scaling). Next check for severe outliers (RobustScaler). Next check for strict [0, 1] bounded input constraints (MinMaxScaler). Otherwise, adopt StandardScaler as the standard industry default.
        </p>
      </div>
    </div>
  </section>

  <!-- SECTION 10: WHICH ALGORITHMS NEED SCALING? -->
  <section id="sec-10" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 10</span>
      <h2 class="section-title">Which Algorithms Need Scaling?</h2>
    </div>
    <p class="section-intro">
      Understanding the exact mathematical inner workings of machine learning algorithms explains why some models fail catastrophically on unscaled features while others remain completely indifferent.
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Algorithm</th>
            <th>Needs Scaling?</th>
            <th>Primary Mathematical Reason</th>
            <th>Recommended Scaler</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>K-Nearest Neighbors (KNN)</strong></td>
            <td><span class="key-badge badge-high">MANDATORY</span></td>
            <td>Distance function: <code>d = &radic;&Sigma;(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup></code>. Large features dominate the neighborhood search entirely.</td>
            <td><code>StandardScaler</code> or <code>RobustScaler</code></td>
          </tr>
          <tr>
            <td><strong>K-Means Clustering</strong></td>
            <td><span class="key-badge badge-high">MANDATORY</span></td>
            <td>Minimizes within-cluster sum of squares. Unscaled data stretches clusters into elongated ellipses along the dominant axis.</td>
            <td><code>StandardScaler</code></td>
          </tr>
          <tr>
            <td><strong>Support Vector Machines (SVM)</strong></td>
            <td><span class="key-badge badge-high">MANDATORY</span></td>
            <td>Maximizes margin between support vectors: <code>2 / ||w||</code>. RBF kernel computes <code>exp(-&gamma;||x<sub>1</sub> - x<sub>2</sub>||<sup>2</sup>)</code>.</td>
            <td><code>StandardScaler</code></td>
          </tr>
          <tr>
            <td><strong>Logistic Regression</strong></td>
            <td><span class="key-badge badge-std">RECOMMENDED</span></td>
            <td>Accelerates gradient descent convergence; essential when L1/L2 penalties are active.</td>
            <td><code>StandardScaler</code></td>
          </tr>
          <tr>
            <td><strong>Regularized Linear (Ridge / Lasso)</strong></td>
            <td><span class="key-badge badge-high">MANDATORY</span></td>
            <td>Penalizes weight magnitudes (&Sigma;w<sub>j</sub><sup>2</sup> or &Sigma;|w<sub>j</sub>|). Unscaled small features get unfairly erased by the penalty.</td>
            <td><code>StandardScaler</code></td>
          </tr>
          <tr>
            <td><strong>Deep Neural Networks (MLP / CNN)</strong></td>
            <td><span class="key-badge badge-high">MANDATORY</span></td>
            <td>Prevents vanishing/exploding gradients in backpropagation; matches activation function input sweet spots (tanh, sigmoid, ReLU).</td>
            <td><code>StandardScaler</code> or <code>MinMaxScaler</code></td>
          </tr>
          <tr>
            <td><strong>Principal Component Analysis (PCA)</strong></td>
            <td><span class="key-badge badge-high">MANDATORY</span></td>
            <td>Eigenvalue decomposition of covariance matrix. Unscaled features with huge numbers artificially masquerade as the principal components.</td>
            <td><code>StandardScaler</code></td>
          </tr>
          <tr>
            <td><strong>Decision Trees</strong></td>
            <td><span class="key-badge badge-robust">NO (Invariant)</span></td>
            <td>Evaluates single-feature threshold inequality: <code>x &le; t</code>. Monotonic scaling transforms the threshold into <code>t&apos;</code> with identical split purity!</td>
            <td>None (Raw data)</td>
          </tr>
          <tr>
            <td><strong>Random Forests</strong></td>
            <td><span class="key-badge badge-robust">NO (Invariant)</span></td>
            <td>Ensemble of bagged decision trees. Invariant to any monotonic transformation of individual feature columns.</td>
            <td>None (Raw data)</td>
          </tr>
          <tr>
            <td><strong>Gradient Boosted Trees (XGB / LGBM)</strong></td>
            <td><span class="key-badge badge-robust">NO (Invariant)</span></td>
            <td>Splits on numerical quantile bins. Raw unscaled data is processed directly without performance degradation.</td>
            <td>None (Raw data)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 11: DATA LEAKAGE AND CORRECT SCALING WORKFLOW -->
  <section id="sec-11" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 11</span>
      <h2 class="section-title">Data Leakage and Correct Scaling Workflow</h2>
    </div>
    <p class="section-intro">
      <strong>Data Leakage</strong> in preprocessing occurs when information from outside the training dataset (such as validation or test splits) is inadvertently used to transform training data. This artificially inflates offline validation scores while guaranteeing degraded performance in production.
    </p>

    <!-- FIGURE 7.11: LEAKAGE WORKFLOW ARCHITECTURE -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_LEAKAGE_WORKFLOW_ARCHITECTURE}
      </div>
      <div class="diagram-caption">Figure 7.11: Architecture of preprocessing data leakage vs the leak-free Scikit-Learn Pipeline standard.</div>
    </div>

    <h3>Why Scalers Cause Data Leakage</h3>
    <p>
      Every feature scaler learns statistics from the dataset passed to its <code>fit()</code> method:
    </p>
    <ul>
      <li><code>MinMaxScaler</code> learns: <code>x<sub>min</sub></code> and <code>x<sub>max</sub></code></li>
      <li><code>StandardScaler</code> learns: <code>&mu;</code> (mean) and <code>&sigma;</code> (standard deviation)</li>
      <li><code>RobustScaler</code> learns: <code>Median</code> and <code>IQR</code></li>
    </ul>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> The "Fit Before Split" Disaster</div>
      <p>
        If you run <code>scaler.fit_transform(X)</code> on your entire dataset <strong>before</strong> calling <code>train_test_split()</code>:
      </p>
      <p>
        The computed mean <code>&mu;</code> and standard deviation <code>&sigma;</code> contain the future test observations! Your model learns from a feature space that was calibrated using test distribution parameters. When deployed in production, incoming unseen customers cannot contribute to the training mean, causing the model&apos;s predictions to drift and fail.
      </p>
    </div>

    <div class="card card-concept">
      <div class="card-title"><span>&#9777;</span> The Three Fundamental Preprocessing Methods</div>
      <ul>
        <li><code>fit(X_train)</code>: Computes and stores the summary statistics (&mu;, &sigma;, min, max) from <code>X_train</code> only. Returns the fitted scaler object.</li>
        <li><code>transform(X)</code>: Applies the previously learned statistics to transform <code>X</code> into scaled values. Computes NO new statistics.</li>
        <li><code>fit_transform(X_train)</code>: Combines both steps efficiently for the training split only.</li>
      </ul>
      <p>
        <strong>Production Golden Rule:</strong> NEVER call <code>fit()</code> or <code>fit_transform()</code> on test or validation data! Always use <code>scaler.transform(X_test)</code>.
      </p>
    </div>

    <h3>Building a Leak-Free Pipeline with Scikit-Learn</h3>
    <div class="code-block">
      <div class="code-header">
        <span class="code-title">python_leakfree_pipeline.py</span>
        <span class="code-lang">python</span>
      </div>
      <pre><code>import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

# 1. Create synthetic dataset
X = np.array([[22, 32000], [25, 45000], [45, 95000], [50, 110000], [29, 48000], [38, 78000]])
y = np.array([0, 0, 1, 1, 0, 1])

# 2. SPLIT FIRST (Mandatory Step 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# 3. Encapsulate Scaler and Estimator inside Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', KNeighborsClassifier(n_neighbors=2))
])

# 4. Fit pipeline on X_train ONLY!
# StandardScaler.fit() executes ONLY on X_train internally.
pipeline.fit(X_train, y_train)

# 5. Evaluate on held-out test set
# Internally calls StandardScaler.transform() using X_train statistics!
test_accuracy = pipeline.score(X_test, y_test)
print(f"Leak-Free Test Accuracy: {{test_accuracy:.2f}}")

# Verify fitted statistics match training split only:
fitted_scaler = pipeline.named_steps['scaler']
print("Pipeline Scaler Mean:", fitted_scaler.mean_)
print("Actual X_train Mean:", X_train.mean(axis=0))
assert np.allclose(fitted_scaler.mean_, X_train.mean(axis=0)), "Leakage detected!"</code></pre>
    </div>
  </section>

  <!-- SECTION 12: HANDLING SPECIAL CASES -->
  <section id="sec-12" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 12</span>
      <h2 class="section-title">Handling Special Cases &amp; Edge Features</h2>
    </div>
    <p class="section-intro">
      Real-world tabular datasets contain edge cases, sparse matrices, and mixed feature types that require specialized preprocessing policies.
    </p>

    <!-- FIGURE 7.12: SPECIAL CASES GRID -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_SPECIAL_CASES_GRID}
      </div>
      <div class="diagram-caption">Figure 7.12: Defensive engineering policies for constant features, binary columns, extreme outliers, and sparse matrices.</div>
    </div>

    <h3>10 Defensive Engineering Policies</h3>
    <ol>
      <li><strong>Constant Features (Variance = 0):</strong>
        <br>Columns where all values are identical provide zero predictive signal. Both <code>MinMaxScaler</code> and <code>StandardScaler</code> output zeros. Safest action: Drop zero-variance columns prior to scaling using <code>VarianceThreshold</code>.
      </li>
      <li><strong>Missing Values (NaNs):</strong>
        <br>Scikit-Learn scalers require complete numerical arrays. Always apply numerical imputation (Mean, Median, or IterativeImputer) <strong>before</strong> calling the scaler in your pipeline.
      </li>
      <li><strong>One-Hot Encoded Binary Columns ({0, 1}):</strong>
        <br>Never standardize binary dummy features with <code>StandardScaler</code>! Centering them shifts zeros to negative floats, destroying matrix sparsity and intuitive binary interpretation. Keep them untouched in [0, 1].
      </li>
      <li><strong>Sparse Matrices (Text / Bag-of-Words):</strong>
        <br>High-dimensional sparse matrices (e.g. TF-IDF) contain 99% zeros. Calling <code>StandardScaler(with_mean=True)</code> subtracts the mean from every zero, expanding the sparse matrix into a massive dense array that triggers Out-of-Memory (OOM) crashes. <strong>Always use <code>StandardScaler(with_mean=False)</code></strong> to scale variance without centering zeros!
      </li>
      <li><strong>Extreme Skewness (Log Transformation vs Scaling):</strong>
        <br>Scaling does not resolve extreme right-skewness. For positive quantities like revenue or web visits, apply a logarithmic transform (<code>np.log1p(x) = ln(1 + x)</code>) to compress exponential spreads into normal bell curves before scaling.
      </li>
      <li><strong>Features Already in Comparable Ranges:</strong>
        <br>If all features in your dataset naturally span <code>[0 &ndash; 10]</code> (such as survey ratings), scaling may be optional if units are identical.
      </li>
      <li><strong>Unseen Test Values Outside Training Bounds:</strong>
        <br>When using <code>MinMaxScaler</code>, configure <code>MinMaxScaler(clip=True)</code> if downstream models require strictly bounded inputs.
      </li>
      <li><strong>Mixed Data Types (Numerical + Categorical):</strong>
        <br>Use Scikit-Learn&apos;s <code>ColumnTransformer</code> to apply <code>StandardScaler</code> to continuous columns while routing categorical columns through <code>OneHotEncoder</code> simultaneously.
      </li>
      <li><strong>Outliers in Real Data:</strong>
        <br>Never arbitrarily delete outliers without domain justification. Use <code>RobustScaler</code> to build models that remain resilient against extreme events.
      </li>
      <li><strong>Inverting Transformations for Predictions:</strong>
        <br>When scaling a regression target variable (y), use <code>scaler.inverse_transform(y_pred)</code> to return model predictions back to original physical currency/unit scale for stakeholders.
      </li>
    </ol>
  </section>
"""
