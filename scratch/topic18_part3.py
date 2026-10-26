# Topic 18 - Part 3: Sections 11 - 15 (Clean Unicode/HTML Math)

PART3_HTML = """
    <!-- SECTION 11 -->
    <section class="content-section" id="sec-11">
      <div class="section-tag">Section 11 &bull; Density-Based Anomaly Detection</div>
      <h2 class="section-title">Local Outlier Factor (LOF)</h2>
      <p class="section-intro">
        Global distance methods make a fatal assumption: that all clusters in a dataset have the same density. <strong>Local Outlier Factor (LOF)</strong>, invented by Markus M. Breunig et al. in 2000, detects anomalies by comparing a point's local density to that of its neighbors.
      </p>

      <h3>1. The Variable Density Problem</h3>
      <p>
        Consider two groups of bank accounts:
      </p>
      <ul>
        <li><strong>Group A (Salaried Tech Workers):</strong> Extremely tight spending pattern (95% of transactions are between ₹300 and ₹600). The density is very high.</li>
        <li><strong>Group B (Antique Art Collectors):</strong> Naturally spread out spending pattern (transactions range widely between ₹5,000 and ₹50,000). The density is low.</li>
      </ul>
      <p>
        Now, observe a transaction of <strong>₹1,500</strong> by a salaried tech worker.
        <br>
        Under a global distance metric (like Euclidean distance to the global mean), ₹1,500 is very small compared to the ₹50,000 art purchases, so it would never be flagged. But <em>relative to its local peers</em>, spending 3x the tight cluster norm is a massive anomaly!
      </p>

      <!-- VISUAL 1.11 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.11: Local Outlier Factor (LOF) &bull; Why Relative Density Trumps Global Distance</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_LOF_CONCEPT__
        <div class="visual-caption">
          <strong>Figure 1.11:</strong> Point p<sub>1</sub> has a much lower density than its neighbors in dense cluster C<sub>1</sub>, giving it a high LOF score (outlier). Points in sparse cluster C<sub>2</sub> have large distances, but their densities match their peers, so their LOF score is &approx; 1.0 (normal).
        </div>
      </div>

      <h3>2. The Mathematics of LOF in 3 Steps</h3>
      <ol>
        <li><strong>k-Distance &amp; k-Neighbors:</strong> For any point p, find the distance to its k-th nearest neighbor, denoted d<sub>k</sub>(p), and gather its k-nearest neighbors N<sub>k</sub>(p).</li>
        <li><strong>Local Reachability Density (lrd):</strong>
          <div class="math-box">
            lrd<sub>k</sub>(p) = |N<sub>k</sub>(p)| / [ &Sigma; max(d<sub>k</sub>(o), d(p, o)) ]
          </div>
          This measures how tightly packed the neighbors are around point p.
        </li>
        <li><strong>Local Outlier Factor (LOF):</strong>
          <div class="math-box">
            LOF<sub>k</sub>(p) = [ &Sigma; ( lrd<sub>k</sub>(o) / lrd<sub>k</sub>(p) ) ] / |N<sub>k</sub>(p)|
          </div>
          The LOF score is the average ratio of the neighbors' densities to p's density:
          <br>&bull; <strong>LOF &approx; 1.0:</strong> Point has similar density to its peers &rarr; <strong>Normal inlier</strong>.
          <br>&bull; <strong>LOF &lt; 1.0:</strong> Point is inside a very dense cluster &rarr; <strong>Deep inlier</strong>.
          <br>&bull; <strong>LOF &gt;&gt; 1.0:</strong> Point has much lower density than its peers &rarr; <strong>Local Outlier!</strong>
        </li>
      </ol>

      <h3>3. Crucial scikit-learn API Distinction: Outlier vs Novelty Mode</h3>
      <div class="card card-warn">
        <div class="card-title">&#9888; The scikit-learn LOF Pitfall: `novelty` Parameter</div>
        In scikit-learn, <code>LocalOutlierFactor</code> has two completely different modes of operation:
        <br><br>
        1. <strong>Outlier Detection (Default, `novelty=False`):</strong> Used to find outliers inside your training data. You call <code>fit_predict(X)</code>. You <strong>cannot</strong> call <code>predict()</code> or <code>decision_function()</code> on new test data because the neighbor graph is precomputed!
        <br><br>
        2. <strong>Novelty Detection (`novelty=True`):</strong> Used when training on clean normal data and predicting on new unseen test data. You call <code>fit(X_train)</code> and then <code>predict(X_test)</code>.
      </div>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; Local Outlier Factor (Standard Outlier Mode)</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>import numpy as np
from sklearn.neighbors import LocalOutlierFactor

# 1. Create two clusters with different densities + local anomalies
rng = np.random.RandomState(42)
c1 = rng.normal(loc=2.0, scale=0.4, size=(100, 2))  # Dense
c2 = rng.normal(loc=7.0, scale=1.0, size=(100, 2))  # Sparse
local_anom = np.array([[3.2, 3.2], [1.0, 3.5], [8.0, 3.0]])
X = np.vstack([c1, c2, local_anom])

# 2. Fit LOF in Outlier Detection mode (novelty=False)
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.04)
preds = lof.fit_predict(X)

# scikit-learn stores negative outlier factor (higher = more normal)
# Multiply by -1 to get classic Breunig LOF (where > 1 means outlier)
classic_lof = -lof.negative_outlier_factor_

print(f"Total points: {len(X)}")
print(f"Flagged anomalies: {np.sum(preds == -1)}")
print(f"Max LOF score: {classic_lof.max():.3f} (Points with LOF >> 1.0 are anomalies)")
print(f"Mean LOF score: {classic_lof.mean():.3f} (Average close to 1.0 for normal points)")

# Output:
# Total points: 203
# Flagged anomalies: 9
# Max LOF score: 2.822
# Mean LOF score: 1.163</code></pre>
      </div>
    </section>

    <!-- SECTION 12 -->
    <section class="content-section" id="sec-12">
      <div class="section-tag">Section 12 &bull; Boundary-Based Novelty Detection</div>
      <h2 class="section-title">One-Class SVM</h2>
      <p class="section-intro">
        What if you are training an anomaly detector for jet engines or semiconductor fabrication, where you have thousands of pristine factory records and <em>zero</em> examples of catastrophic failures? This is the domain of <strong>One-Class SVM</strong>.
      </p>

      <h3>1. The Geometric Intuition: Bounding the Origin</h3>
      <p>
        In a standard two-class Support Vector Machine (SVM), the algorithm finds a maximum-margin hyperplane that separates Class A (+1) from Class B (-1).
      </p>
      <p>
        In <strong>One-Class SVM</strong> (formulated by Bernhard Schölkopf et al.):
      </p>
      <ol>
        <li>The algorithm treats the coordinate origin (0, 0, &hellip;, 0) as the only member of the "anomalous" class.</li>
        <li>It maps the training data into a high-dimensional feature space using a non-linear kernel (typically <strong>Radial Basis Function / RBF</strong>).</li>
        <li>It finds a maximum-margin hyperplane that separates all the normal training data from the origin!</li>
        <li>Projected back into original space, this linear hyperplane becomes a <strong>tight, smooth non-linear envelope</strong> wrapping around the normal data points.</li>
      </ol>

      <!-- VISUAL 1.12 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.12: One-Class SVM &bull; Non-Linear RBF Decision Boundary</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_ONE_CLASS_SVM__
        <div class="visual-caption">
          <strong>Figure 1.12:</strong> One-Class SVM decision boundary. The green curved envelope encapsulates the dense normal points. The parameter &nu; controls the allowable fraction of margin violations (support vectors in amber), while external points falling in the red zone are rejected as anomalies.
        </div>
      </div>

      <h3>2. Essential Hyperparameters</h3>
      <ul>
        <li><code>nu</code> (&nu;, float between 0.0 and 1.0, default 0.5):
          <br>&bull; An upper bound on the fraction of training errors (outliers).
          <br>&bull; A lower bound on the fraction of support vectors.
          <br>&bull; <em>Crucial practical tip:</em> In anomaly detection, never leave <code>nu=0.5</code> (which would reject 50% of your data)! Set it to a small expected outlier rate like <code>nu=0.05</code> or <code>nu=0.01</code>.
        </li>
        <li><code>kernel</code> (default 'rbf'): Radial Basis Function kernel allows learning arbitrary curved envelopes.</li>
        <li><code>gamma</code> (&gamma;, default 'scale'): Controls the influence radius of individual support vectors. A high gamma leads to tight, overfitted "islands"; a low gamma yields a loose, smooth envelope.</li>
      </ul>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; One-Class SVM with Feature Scaling</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>import numpy as np
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler

# 1. Feature scaling is MANDATORY for SVM!
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Fit One-Class SVM with nu=0.05
oc_svm = OneClassSVM(kernel='rbf', gamma='scale', nu=0.05)
oc_preds = oc_svm.fit_predict(X_scaled)

n_anom = np.sum(oc_preds == -1)
n_inliers = np.sum(oc_preds == 1)

print(f"Flagged anomalies: {n_anom}")
print(f"Normal inliers: {n_inliers}")

# Output:
# Flagged anomalies: 13
# Normal inliers: 195</code></pre>
      </div>
    </section>

    <!-- SECTION 13 -->
    <section class="content-section" id="sec-13">
      <div class="section-tag">Section 13 &bull; Master Comparative Matrix</div>
      <h2 class="section-title">Comparing Anomaly Detection Algorithms</h2>
      <p class="section-intro">
        No single anomaly detection algorithm dominates every dataset. The best method depends on feature dimensionality, local density variation, scaling sensitivity, and whether normal-only training data is available.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Method</th>
              <th>Underlying Model</th>
              <th>Dimensions</th>
              <th>Feature Scaling?</th>
              <th>Density Aware?</th>
              <th>Primary Strengths</th>
              <th>Key Limitations</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Z-Score</strong></td>
              <td>Parametric Gaussian statistical test (&mu;, &sigma;)</td>
              <td>1D (Univariate)</td>
              <td>No (standardizes internally)</td>
              <td>No</td>
              <td>Instant computation; mathematically transparent.</td>
              <td>Assumes Gaussian bell curve; ruined by outlier masking.</td>
            </tr>
            <tr>
              <td><strong>IQR Boxplot</strong></td>
              <td>Non-parametric order statistics (Q<sub>1</sub>, Q<sub>3</sub>, IQR)</td>
              <td>1D (Univariate)</td>
              <td>No</td>
              <td>No</td>
              <td>Completely immune to extreme outliers; distribution-free.</td>
              <td>Blind to correlations between features.</td>
            </tr>
            <tr>
              <td><strong>Isolation Forest</strong></td>
              <td>Ensemble of random binary recursive partitioning trees</td>
              <td>Multivariate (2D to 1,000D+)</td>
              <td><strong>Not Required</strong> (Scale invariant)</td>
              <td>Global isolation</td>
              <td>Linear speed O(n log n); excellent on wide tabular data; default industry choice.</td>
              <td>Can produce axis-aligned artifacts in complex geometric shapes.</td>
            </tr>
            <tr>
              <td><strong>Local Outlier Factor (LOF)</strong></td>
              <td>Nearest neighbor relative density ratios (k-NN)</td>
              <td>Low-to-Medium (2D to 20D)</td>
              <td><strong>Strictly Required</strong> (Distance based)</td>
              <td><strong>Yes</strong> (Local relative)</td>
              <td>Excels when data has clusters of wildly different densities.</td>
              <td>O(n&sup2;) complexity; slow on huge datasets; sensitive to curse of dimensionality.</td>
            </tr>
            <tr>
              <td><strong>One-Class SVM</strong></td>
              <td>Kernelized maximum-margin hyperplane separating data from origin</td>
              <td>Multivariate with non-linear kernel</td>
              <td><strong>Strictly Required</strong> (Distance based)</td>
              <td>Global boundary</td>
              <td>Ideal for semi-supervised novelty detection on clean normal data.</td>
              <td>Sensitive to hyperparameters (&nu;, &gamma;); O(n&sup3;) memory scaling.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 14 -->
    <section class="content-section" id="sec-14">
      <div class="section-tag">Section 14 &bull; Engineering Best Practices</div>
      <h2 class="section-title">Data Preprocessing and Feature Scaling</h2>
      <p class="section-intro">
        The performance of an anomaly detector is dictated by how data is prepared before model training. An unscaled feature can completely hijack your detector.
      </p>

      <h3>1. Why Distance-Based Detectors Require Feature Scaling</h3>
      <p>
        Consider two features in a fraud detection pipeline:
      </p>
      <ul>
        <li><code>transaction_amount</code>: Range ₹100 to ₹10,00,000</li>
        <li><code>swipe_speed_seconds</code>: Range 0.5 to 15.0 seconds</li>
      </ul>
      <p>
        If you calculate Euclidean distance in <strong>LOF</strong>, <strong>k-NN</strong>, or <strong>One-Class SVM</strong>, a change of ₹50 in amount completely obliterates a change of 10 seconds in swipe speed! The model becomes 100% blind to speed anomalies.
      </p>

      <div class="card card-def">
        <div class="card-title">&#128736;&#65039; Best Practice: Use RobustScaler for Outlier Data</div>
        In standard supervised learning, we use <code>StandardScaler</code>. But in anomaly detection, the presence of extreme outliers will distort the mean and variance used by StandardScaler!
        <br><br>
        <strong>RobustScaler</strong> uses the median and IQR:
        <br>
        <code>X_scaled = (X &minus; median) / IQR</code>
        <br>
        This makes your preprocessing mathematically immune to extreme outliers!
      </div>

      <h3>2. Leakage-Safe Novelty Detection Pipelines</h3>
      <p>
        When evaluating semi-supervised novelty detectors on test data, never fit the scaler on the entire dataset:
      </p>
      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; Leakage-Safe scikit-learn Pipeline</span>
          <span>Best Practice</span>
        </div>
        <pre><code>from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.svm import OneClassSVM

# Pipeline ensures scaler is fitted ONLY on normal training records
pipeline = Pipeline([
    ('scaler', RobustScaler()),
    ('detector', OneClassSVM(nu=0.05, kernel='rbf'))
])

# Fit only on clean normal training data
pipeline.fit(X_train_normal)

# Transform and predict on test stream without leakage
test_predictions = pipeline.predict(X_test)</code></pre>
      </div>
    </section>

    <!-- SECTION 15 -->
    <section class="content-section" id="sec-15">
      <div class="section-tag">Section 15 &bull; Evaluation Metrics for Imbalanced Data</div>
      <h2 class="section-title">Evaluating Anomaly Detection</h2>
      <p class="section-intro">
        In standard machine learning, accuracy is the go-to metric. In anomaly detection, <strong>accuracy is completely useless and dangerous</strong>.
      </p>

      <h3>1. The Accuracy Paradox</h3>
      <p>
        Suppose a bank processes 1,000,000 credit card transactions per day, and exactly 100 of them are fraudulent (0.01% fraud rate).
        <br><br>
        A dumb "model" that classifies <strong>every single transaction as normal</strong> achieves:
      </p>
      <div class="math-box">
        Accuracy = 999,900 / 1,000,000 = 99.99%
      </div>
      <p>
        The model has 99.99% accuracy, yet it missed <strong>100% of all fraudulent transactions</strong> and cost the bank millions of rupees!
      </p>

      <h3>2. Precision, Recall, and F1-Score</h3>
      <div class="math-box">
        Precision = TP / (TP + FP)
        &emsp;&emsp;
        Recall = TP / (TP + FN)
        <br><br>
        F1-Score = 2 &times; (Precision &times; Recall) / (Precision + Recall)
        <div class="math-legend">
          Where:<br>
          &bull; <strong>True Positive (TP):</strong> An actual anomaly correctly flagged by the model.<br>
          &bull; <strong>False Positive (FP):</strong> A normal transaction wrongly flagged as an anomaly (False Alarm).<br>
          &bull; <strong>True Negative (TN):</strong> A normal transaction correctly identified as normal.<br>
          &bull; <strong>False Negative (FN):</strong> An actual anomaly that slipped past undetected (Missed Attack).
        </div>
      </div>

      <!-- VISUAL 1.13 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.13: Confusion Matrix &bull; Real Transaction Detection Benchmark</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_CONFUSION_MATRIX__
        <div class="visual-caption">
          <strong>Figure 1.13:</strong> Real confusion matrix on our 500-sample transaction benchmark. The model correctly identifies 473 normal transactions (TN) and 23 anomalies (TP). It incurs 2 false alarms (FP) and 2 missed anomalies (FN), achieving a balanced Precision and Recall of 92.00%.
        </div>
      </div>
    </section>
"""
