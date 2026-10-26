"""
Module: topic11_part2.py
Contains Sections 6 to 10 for Topic 11: K-Nearest Neighbors (KNN).
"""

from scratch.topic11_svgs import (
    SVG_MANUAL_DISTANCE_RANKING,
    SVG_WEIGHTED_VS_UNWEIGHTED,
    SVG_FEATURE_SCALING_EFFECT,
    SVG_DECISION_BOUNDARIES_K,
    SVG_TRAIN_VAL_ERROR_CURVE
)

PART2_HTML = f"""
    <!-- SECTION 06: COMPLETE MANUAL WORKED EXAMPLE -->
    <section id="sec-06" class="section-card">
      <span class="section-badge">Section 06</span>
      <h2 class="section-title">Complete Manual KNN Worked Example</h2>
      <p class="section-lead">
        To build complete confidence in the algorithm, let us calculate a full KNN prediction entirely by hand using a small 6-point training dataset and verify every arithmetic step with Python.
      </p>

      <h3 class="sub-title">1. The Known Training Dataset</h3>
      <p>
        Suppose an agricultural lab tests 6 pieces of fruit using two numerical features: <strong>Sweetness (x<sub>1</sub>)</strong> and <strong>Crispness (x<sub>2</sub>)</strong> on a 1-to-10 scale. The true class labels are <strong>Apple (Class 0)</strong> and <strong>Orange (Class 1)</strong>:
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Point ID</th>
              <th>Sweetness (x<sub>1</sub>)</th>
              <th>Crispness (x<sub>2</sub>)</th>
              <th>Class Label</th>
              <th>Binary Target (y)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>T1</strong></td>
              <td>4.0</td>
              <td>6.0</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">Apple</span></td>
              <td>0</td>
            </tr>
            <tr>
              <td><strong>T2</strong></td>
              <td>6.0</td>
              <td>5.0</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">Apple</span></td>
              <td>0</td>
            </tr>
            <tr>
              <td><strong>T3</strong></td>
              <td>5.0</td>
              <td>3.0</td>
              <td><span class="badge" style="background:#FFF7ED;color:#C2410C;">Orange</span></td>
              <td>1</td>
            </tr>
            <tr>
              <td><strong>T4</strong></td>
              <td>7.0</td>
              <td>6.0</td>
              <td><span class="badge" style="background:#FFF7ED;color:#C2410C;">Orange</span></td>
              <td>1</td>
            </tr>
            <tr>
              <td><strong>T5</strong></td>
              <td>3.0</td>
              <td>3.0</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">Apple</span></td>
              <td>0</td>
            </tr>
            <tr>
              <td><strong>T6</strong></td>
              <td>8.0</td>
              <td>4.0</td>
              <td><span class="badge" style="background:#FFF7ED;color:#C2410C;">Orange</span></td>
              <td>1</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">2. Arrival of the Unknown Query Point (Q)</h3>
      <p>
        A mystery fruit arrives with coordinates: <strong>Sweetness = 5.0, Crispness = 5.0</strong> &rarr; <code>Q(5.0, 5.0)</code>.
      </p>

      <h3 class="sub-title">3. Distance Calculations to Every Training Point</h3>
      <p>
        Using the Euclidean distance formula: <code>d = &radic;((x<sub>1</sub> - 5.0)&sup2; + (x<sub>2</sub> - 5.0)&sup2;)</code>:
      </p>
      <ul>
        <li><strong>Distance to T1 (4, 6):</strong> <code>&radic;((4-5)&sup2; + (6-5)&sup2;) = &radic;((-1)&sup2; + 1&sup2;) = &radic;(1 + 1) = &radic;2 &approx; <strong>1.4142</strong></code></li>
        <li><strong>Distance to T2 (6, 5):</strong> <code>&radic;((6-5)&sup2; + (5-5)&sup2;) = &radic;(1&sup2; + 0&sup2;) = &radic;1 = <strong>1.0000</strong></code></li>
        <li><strong>Distance to T3 (5, 3):</strong> <code>&radic;((5-5)&sup2; + (3-5)&sup2;) = &radic;(0&sup2; + (-2)&sup2;) = &radic;4 = <strong>2.0000</strong></code></li>
        <li><strong>Distance to T4 (7, 6):</strong> <code>&radic;((7-5)&sup2; + (6-5)&sup2;) = &radic;(2&sup2; + 1&sup2;) = &radic;(4 + 1) = &radic;5 &approx; <strong>2.2361</strong></code></li>
        <li><strong>Distance to T5 (3, 3):</strong> <code>&radic;((3-5)&sup2; + (3-5)&sup2;) = &radic;((-2)&sup2; + (-2)&sup2;) = &radic;(4 + 4) = &radic;8 &approx; <strong>2.8284</strong></code></li>
        <li><strong>Distance to T6 (8, 4):</strong> <code>&radic;((8-5)&sup2; + (4-5)&sup2;) = &radic;(3&sup2; + (-1)&sup2;) = &radic;(9 + 1) = &radic;10 &approx; <strong>3.1623</strong></code></li>
      </ul>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_MANUAL_DISTANCE_RANKING}
        </div>
        <div class="svg-caption">
          <strong>Figure 11.6: Ranked Training Points by Euclidean Distance to Query Q(5, 5).</strong> T2 is the closest neighbor (1.000), followed by T1 (1.414), T3 (2.000), T4 (2.236), T5 (2.828), and T6 (3.162).
        </div>
      </div>

      <h3 class="sub-title">4. Predictions Across Different K Values</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Value of K</th>
              <th>Selected Neighbors (Ranked)</th>
              <th>Class Votes</th>
              <th>Majority Winner</th>
              <th>Predicted Class</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>K = 1</strong></td>
              <td>T2 (Apple, d=1.0000)</td>
              <td>Apple: 1 &bull; Orange: 0</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">Apple</span></td>
              <td><strong>Class 0 (Apple)</strong></td>
            </tr>
            <tr>
              <td><strong>K = 3</strong></td>
              <td>T2 (Apple), T1 (Apple), T3 (Orange)</td>
              <td>Apple: 2 &bull; Orange: 1</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">Apple</span></td>
              <td><strong>Class 0 (Apple)</strong></td>
            </tr>
            <tr>
              <td><strong>K = 5</strong></td>
              <td>T2 (Apple), T1 (Apple), T3 (Orange), T4 (Orange), T5 (Apple)</td>
              <td>Apple: 3 &bull; Orange: 2</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">Apple</span></td>
              <td><strong>Class 0 (Apple)</strong></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="code-block">
        <div class="code-header">
          <span class="code-title">&#128013; manual_knn_validation.py &bull; NumPy Verification</span>
          <span class="code-lang">Python 3</span>
        </div>
        <pre><code>import numpy as np
import pandas as pd

# Training dataset
X_train = np.array([
    [4.0, 6.0], [6.0, 5.0], [5.0, 3.0],
    [7.0, 6.0], [3.0, 3.0], [8.0, 4.0]
])
y_train = np.array([0, 0, 1, 1, 0, 1])  # 0=Apple, 1=Orange
labels = ['Apple', 'Apple', 'Orange', 'Orange', 'Apple', 'Orange']

query = np.array([5.0, 5.0])

# Compute Euclidean distances
distances = np.sqrt(np.sum((X_train - query)**2, axis=1))

# Sort ascending
sorted_indices = np.argsort(distances)

print("Ranked Neighbor Distances:")
for rank, idx in enumerate(sorted_indices, 1):
    print(f"  Rank #{{rank}}: Point T{{idx+1}} {{labels[idx]}} -> Dist = {{distances[idx]:.4f}}")

# Assert K=3 prediction
top_3_labels = y_train[sorted_indices[:3]]
winner_k3 = int(np.bincount(top_3_labels).argmax())
print(f"\\nK=3 Prediction: Class {{winner_k3}} ({{'Apple' if winner_k3 == 0 else 'Orange'}})")
assert winner_k3 == 0, "K=3 must predict Class 0 (Apple) by 2 votes to 1!"</code></pre>
      </div>
    </section>

    <!-- SECTION 07: MAJORITY VS DISTANCE-WEIGHTED VOTING -->
    <section id="sec-07" class="section-card">
      <span class="section-badge">Section 07</span>
      <h2 class="section-title">Majority Voting vs. Distance-Weighted Voting</h2>
      <p class="section-lead">
        In standard unweighted KNN, every neighbor in the top-K receives <strong>exactly one equal vote</strong>, regardless of whether a neighbor is 0.01 units away or 5.0 units away.
      </p>

      <p>
        In many real-world scenarios, an extraordinarily close neighbor should hold greater influence than distant neighbors on the perimeter. This motivation gives rise to <strong>Distance-Weighted Voting</strong>.
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; Inverse-Distance Weighting Formula</div>
        <div class="formula-math">
          w<sub>i</sub> = 1 / d(x<sub>(i)</sub>, q)
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          Where <code>d(x<sub>(i)</sub>, q)</code> is the distance to neighbor <code>i</code>. If a training point lands exactly on the query point (<code>d = 0</code>), software implementations assign <code>w = 1.0</code> to prevent division-by-zero errors.
        </p>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_WEIGHTED_VS_UNWEIGHTED}
        </div>
        <div class="svg-caption">
          <strong>Figure 11.7: A Concrete Divergent Scenario (Apple vs. Orange).</strong> Under unweighted majority voting (left), Apple wins 2-to-1 because count dominates. Under distance-weighted voting (right), Orange flips the victory (1.000 vs. 0.667) because it is 3&times; closer than either Apple!
        </div>
        <div class="svg-takeaway">
          &#10004; Architectural Rule: Distance-weighting allows very close neighbors to override a crowd of distant, borderline points.
        </div>
      </div>

      <h3 class="sub-title">Step-by-Step Numerical Verification</h3>
      <p>
        Suppose an unknown query point <code>Q</code> has three nearest neighbors (<code>K = 3</code>):
      </p>
      <ul>
        <li><strong>Neighbor 1:</strong> Distance = 1.0, Class = Orange (Class 1)</li>
        <li><strong>Neighbor 2:</strong> Distance = 3.0, Class = Apple (Class 0)</li>
        <li><strong>Neighbor 3:</strong> Distance = 3.0, Class = Apple (Class 0)</li>
      </ul>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Voting Strategy</th>
              <th>Class 0 (Apple) Score</th>
              <th>Class 1 (Orange) Score</th>
              <th>Winning Prediction</th>
              <th>Why the Decision Flipped</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Unweighted Majority</strong></td>
              <td>1 + 1 = <strong>2 votes</strong></td>
              <td>1 = <strong>1 vote</strong></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">Class 0 (Apple)</span></td>
              <td>Equal votes: 2 Apples overpower 1 Orange.</td>
            </tr>
            <tr>
              <td><strong>Distance-Weighted (w = 1/d)</strong></td>
              <td>1/3.0 + 1/3.0 = <strong>0.6667</strong></td>
              <td>1/1.0 = <strong>1.0000</strong></td>
              <td><span class="badge" style="background:#FFF7ED;color:#C2410C;">Class 1 (Orange)</span></td>
              <td>Proximity: Orange is 3&times; closer (weight 1.0 &gt; 0.667).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout card-concept">
        <div class="callout-title">&#128736; Setting Weights in Scikit-Learn</div>
        <p>
          In scikit-learn&rsquo;s <code>KNeighborsClassifier(weights='...')</code>:
        </p>
        <ul>
          <li><strong><code>weights='uniform'</code></strong> (Default): Standard unweighted majority voting.</li>
          <li><strong><code>weights='distance'</code></strong>: Inversely weights points by their distance. Often performs better when data has high local density variation.</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 08: THE MANDATORY ROLE OF FEATURE SCALING -->
    <section id="sec-08" class="section-card">
      <span class="section-badge">Section 08</span>
      <h2 class="section-title">The Mandatory Role of Feature Scaling</h2>
      <p class="section-lead">
        Because KNN is entirely distance-based, <strong>feature scaling is not merely an optional optimization; it is mandatory</strong>. Failing to scale features measured on different numeric ranges destroys the integrity of the distance metric.
      </p>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_FEATURE_SCALING_EFFECT}
        </div>
        <div class="svg-caption">
          <strong>Figure 11.8: Feature Scaling Disproportion.</strong> In raw units (left), Annual Income ($20k-$150k) spans thousands of units, completely washing out Age (20-60 years). Person B (20 years older!) is falsely picked as closest. After standard scaling (right), both dimensions contribute isotropically, correctly identifying Person C as the genuine neighbor.
        </div>
      </div>

      <h3 class="sub-title">Two Standard Preprocessing Scalers Explained</h3>
      <div class="formula-card">
        <div class="formula-title">&#128290; 1. Standardization (Z-Score &bull; StandardScaler)</div>
        <div class="formula-math">
          z = (x - &mu;) / &sigma;
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          Centers data around zero mean (<code>&mu; = 0</code>) with unit variance (<code>&sigma; = 1</code>). Recommended for general Gaussian-distributed tabular data and features with outliers.
        </p>
      </div>

      <div class="formula-card">
        <div class="formula-title">&#128290; 2. Min-Max Normalization (MinMaxScaler)</div>
        <div class="formula-math">
          x&prime; = (x - x<sub>min</sub>) / (x<sub>max</sub> - x<sub>min</sub>)
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          Rescales feature values strictly into the bounded interval <code>[0, 1]</code>. Highly effective for pixel intensities (0 to 255) and bounded sensor signals.
        </p>
      </div>

      <h3 class="sub-title">Strict Anti-Leakage Rule: Fit Scalers on Training Data Only</h3>
      <div class="callout card-warning">
        <div class="callout-title">&#9888; Critical Data Leakage Pitfall: Never Fit Scalers Before Splitting!</div>
        <p>
          A catastrophic mistake made by beginners is calling <code>scaler.fit(df)</code> on the entire dataset before calling <code>train_test_split()</code>.
        </p>
        <p>
          This leaks the test set&rsquo;s mean, minimum, and maximum into the training phase, giving your model an unrealistic, biased performance advantage that collapses in production!
        </p>
        <p>
          <strong>The Production Remedy:</strong> Always nest the scaler and classifier inside a scikit-learn <code>Pipeline</code>.
        </p>
      </div>
    </section>

    <!-- SECTION 09: KNN DECISION BOUNDARIES ACROSS K -->
    <section id="sec-09" class="section-card">
      <span class="section-badge">Section 09</span>
      <h2 class="section-title">KNN Decision Boundaries Across K</h2>
      <p class="section-lead">
        In parametric models like Logistic Regression, the decision boundary is restricted to a straight hyperplane. In contrast, KNN is <strong>non-parametric</strong>: its decision boundaries can bend, curve, and wrap around complex non-linear cluster topologies.
      </p>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_DECISION_BOUNDARIES_K}
        </div>
        <div class="svg-caption">
          <strong>Figure 11.9: Real Fitted KNN Decision Boundaries for K = 1, K = 5, and K = 15.</strong> At <code>K = 1</code>, the model produces fragmented &ldquo;island&rdquo; boundaries around individual noise points. At <code>K = 5</code>, the boundary becomes smooth and natural. At <code>K = 15</code>, the boundary oversmooths, flattening fine-grained local separation.
        </div>
        <div class="svg-takeaway">
          &#10004; Visual Rule: Increasing K transforms sharp, jagged local boundaries into smooth, generalized macroscopic curves.
        </div>
      </div>

      <h3 class="sub-title">Why K=1 Memorizes Noise</h3>
      <p>
        When <code>K = 1</code>, the model queries only the single closest point. If your dataset contains an anomalous outlier (e.g., a mislabeled observation or corrupted sensor read), <code>K = 1</code> creates a tight circular decision pocket around that single outlier. This guarantees <strong>100% training accuracy</strong>, but results in poor test generalization.
      </p>
    </section>

    <!-- SECTION 10: UNDERFITTING AND OVERFITTING -->
    <section id="sec-10" class="section-card">
      <span class="section-badge">Section 10</span>
      <h2 class="section-title">Underfitting and Overfitting in KNN</h2>
      <p class="section-lead">
        In KNN, hyperparameter <strong>K acts as an inverse complexity knob</strong>: small K means high complexity (overfitting), while large K means low complexity (underfitting).
      </p>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_TRAIN_VAL_ERROR_CURVE}
        </div>
        <div class="svg-caption">
          <strong>Figure 11.10: Training vs. 5-Fold Cross-Validation Accuracy Across K (1 to 21).</strong> Notice that training accuracy (red line) is perfect (100%) at K=1 and drops steadily. In contrast, 5-Fold CV accuracy (purple line) peaks at K=3 (95.0%) before declining due to underfitting.
        </div>
        <div class="svg-takeaway">
          &#10004; Golden Rule of Model Selection: Never select K based on training accuracy! Always select K at the peak of the <strong>cross-validation accuracy curve</strong>.
        </div>
      </div>

      <h3 class="sub-title">The Inverted Complexity Continuum</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Model State</th>
              <th>K Value</th>
              <th>Training Score</th>
              <th>Validation Score</th>
              <th>Diagnosis</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Overfitting (High Variance)</strong></td>
              <td>K = 1</td>
              <td>100.0% (Perfect)</td>
              <td>92.5% (Degraded)</td>
              <td>Model memorized random noise and local quirks.</td>
            </tr>
            <tr>
              <td><strong>Sweet Spot (Optimal Generalization)</strong></td>
              <td>K = 3 to 5</td>
              <td>95.5% (Realistic)</td>
              <td><strong>95.0% (Peak)</strong></td>
              <td>Ignores outliers while capturing true underlying structure.</td>
            </tr>
            <tr>
              <td><strong>Underfitting (High Bias)</strong></td>
              <td>K &ge; 21</td>
              <td>90.0% (Poor)</td>
              <td>91.5% (Poor)</td>
              <td>Neighborhood is too broad; washes out local patterns.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
