"""
Module: topic7_part2.py
Contains HTML for Sections 5 to 8 of Topic 7: Feature Scaling & Normalization.
"""

from scratch.topic7_svgs import (
    SVG_Z_SCORE_NORMAL_BELL,
    SVG_GRAPH_3_STANDARDIZATION_BEFORE_AFTER,
    SVG_GRAPH_4_OUTLIER_IMPACT,
    SVG_ROW_VS_COLUMN_OPERATIONS,
    SVG_GRAPH_6_VECTOR_NORMALIZATION,
    SVG_GRAPH_7_L1_VS_L2_NORM
)

PART2_HTML = f"""
  <!-- SECTION 5: STANDARDIZATION AND Z-SCORE SCALING -->
  <section id="sec-05" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 05</span>
      <h2 class="section-title">Standardization and Z-Score Scaling</h2>
    </div>
    <p class="section-intro">
      Standardization (also known as <em>Z-score normalization</em>) rescales a numerical feature so that its distribution is centered around a <strong>mean of 0</strong> with a <strong>standard deviation of 1</strong>.
    </p>

    <div class="formula-card">
      <div class="formula-title">Mathematical Formula: Z-Score Standardization</div>
      <div class="formula-box">z = (x - &mu;) / &sigma;</div>
      <div class="formula-desc">
        Where:
        <ul>
          <li><strong>x:</strong> Original raw observation value.</li>
          <li><strong>&mu; (Mu):</strong> Arithmetic mean of the feature fitted on the training split.</li>
          <li><strong>&sigma; (Sigma):</strong> Population standard deviation of the feature fitted on the training split.</li>
          <li><strong>z:</strong> Standardized score (Z-score) representing how many standard deviations x lies away from the mean.</li>
        </ul>
      </div>
    </div>

    <!-- FIGURE 7.5: Z-SCORE NORMAL BELL -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_Z_SCORE_NORMAL_BELL}
      </div>
      <div class="diagram-caption">Figure 7.5: The standard normal bell curve (&mu; = 0, &sigma; = 1) showing empirical Z-score intervals.</div>
    </div>

    <!-- GRAPH 3: STANDARDIZATION BEFORE AND AFTER -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GRAPH_3_STANDARDIZATION_BEFORE_AFTER}
      </div>
      <div class="diagram-caption">Figure 7.6 (Graph 3): Numerical transformation of raw values [10, 20, 30] to Z-scores [-1.225, 0.000, +1.225].</div>
      <div class="how-to-read">
        <div class="how-to-read-title"><span>&#128269;</span> Interpreting Z-Scores:</div>
        <ul>
          <li><strong>z = 0:</strong> The observation is <em>identical</em> to the average (mean) value.</li>
          <li><strong>z &gt; 0 (Positive):</strong> The observation is <em>above average</em>. For example, <code>z = +1.5</code> means 1.5 standard deviations above the mean.</li>
          <li><strong>z &lt; 0 (Negative):</strong> The observation is <em>below average</em>. For example, <code>z = -1.225</code> means 1.225 standard deviations below the mean.</li>
        </ul>
      </div>
    </div>

    <h3>Step-by-Step Worked Numerical Example</h3>
    <p>
      Consider the same feature: <code>X = [10, 20, 30]</code>.
    </p>
    <ol>
      <li><strong>Calculate Mean (&mu;):</strong>
        <br><code>&mu; = (10 + 20 + 30) / 3 = 60 / 3 = <strong>20.0</strong></code>
      </li>
      <li><strong>Calculate Deviations from Mean:</strong>
        <br><code>(10 - 20) = -10</code>, <code>(20 - 20) = 0</code>, <code>(30 - 20) = +10</code>
      </li>
      <li><strong>Calculate Squared Deviations &amp; Variance (&sigma;<sup>2</sup>, ddof = 0):</strong>
        <br><code>&sigma;<sup>2</sup> = [(-10)<sup>2</sup> + 0<sup>2</sup> + 10<sup>2</sup>] / 3 = [100 + 0 + 100] / 3 = 200 / 3 &approx; <strong>66.667</strong></code>
      </li>
      <li><strong>Calculate Population Standard Deviation (&sigma;):</strong>
        <br><code>&sigma; = &radic;(66.6667) &approx; <strong>8.1649658</strong></code>
      </li>
      <li><strong>Transform Each Observation:</strong>
        <ul>
          <li>Observation 1: <code>z<sub>1</sub> = (10 - 20) / 8.16497 = -10 / 8.16497 &approx; <strong>-1.2247</strong></code></li>
          <li>Observation 2: <code>z<sub>2</sub> = (20 - 20) / 8.16497 = 0 / 8.16497 = <strong>0.0000</strong></code></li>
          <li>Observation 3: <code>z<sub>3</sub> = (30 - 20) / 8.16497 = +10 / 8.16497 &approx; <strong>+1.2247</strong></code></li>
        </ul>
      </li>
    </ol>
    <p>
      <strong>Verification:</strong> The mean of the Z-scores is <code>(-1.2247 + 0.0 + 1.2247) / 3 = 0.0</code>, and their standard deviation is exactly <code>1.0</code>!
    </p>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> Two Dangerous Misconceptions About Standardization</div>
      <p>
        <strong>Myth 1: "Standardization makes data normal." &times; FALSE!</strong>
        <br>Standardization is a <em>linear transformation</em>. It shifts the center and stretches/shrinks the axis, but it <strong>never alters the shape</strong> of the distribution. If your raw data is bimodal, uniform, or heavily right-skewed, the standardized data will remain equally bimodal, uniform, or right-skewed!
      </p>
      <p>
        <strong>Myth 2: "Standardized values must fall between 0 and 1." &times; FALSE!</strong>
        <br>Z-scores are unbounded. They typically span from <code>-3</code> to <code>+3</code> for roughly bell-shaped data, but extreme outliers can easily have Z-scores of <code>+15.0</code> or <code>-20.0</code>.
      </p>
    </div>

    <h3>Scikit-Learn StandardScaler Implementation</h3>
    <div class="code-block">
      <div class="code-header">
        <span class="code-title">python_standard_scaler.py</span>
        <span class="code-lang">python</span>
      </div>
      <pre><code>import numpy as np
from sklearn.preprocessing import StandardScaler

X_train = np.array([[10.0], [20.0], [30.0]])

scaler = StandardScaler()
X_train_z = scaler.fit_transform(X_train)

print("Fitted Mean (&mu;):", scaler.mean_)           # Output: [20.]
print("Fitted Std (&sigma;):", scaler.scale_)          # Output: [8.16496581]
print("Standardized Z-Scores:\n", X_train_z.flatten())
# Output: [-1.22474487  0.          1.22474487]

# Constant feature defense
X_const = np.array([[50.0], [50.0], [50.0]])
scaler_const = StandardScaler()
print("Constant Feature Z-Scores:\n", scaler_const.fit_transform(X_const).flatten())
# Output: [0. 0. 0.] (Defensively handled without ZeroDivisionError!)</code></pre>
    </div>
  </section>

  <!-- SECTION 6: ROBUST SCALING -->
  <section id="sec-06" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 06</span>
      <h2 class="section-title">Robust Scaling (Outlier-Resistant)</h2>
    </div>
    <p class="section-intro">
      Both Min-Max Scaling and Standardization suffer from an acute vulnerability: <strong>extreme outliers</strong>. Because <code>x<sub>min</sub></code>, <code>x<sub>max</sub></code>, <code>&mu;</code>, and <code>&sigma;</code> are calculated using all observations, a single astronomical value can distort the entire scaling parameter set.
    </p>

    <div class="formula-card">
      <div class="formula-title">Mathematical Formula: Robust Scaling</div>
      <div class="formula-box">x&apos; = (x - Median) / (Q3 - Q1) = (x - Median) / IQR</div>
      <div class="formula-desc">
        Where:
        <ul>
          <li><strong>x:</strong> Original raw observation value.</li>
          <li><strong>Median (Q2):</strong> 50th percentile of the training data (center of distribution).</li>
          <li><strong>Q1:</strong> 25th percentile (first quartile).</li>
          <li><strong>Q3:</strong> 75th percentile (third quartile).</li>
          <li><strong>IQR (Interquartile Range):</strong> <code>Q3 - Q1</code>, representing the spread of the central 50% of observations.</li>
        </ul>
      </div>
    </div>

    <!-- FIGURE 7.7 / GRAPH 4: OUTLIER IMPACT -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GRAPH_4_OUTLIER_IMPACT}
      </div>
      <div class="diagram-caption">Figure 7.7 (Graph 4): Comparative performance of MinMaxScaler, StandardScaler, and RobustScaler on a dataset with an extreme outlier (500).</div>
      <div class="how-to-read">
        <div class="how-to-read-title"><span>&#128269;</span> What Graph 4 Proves:</div>
        <ul>
          <li><strong>MinMaxScaler Fails:</strong> Points <code>[20 &ndash; 55]</code> are compressed into an unreadable sliver <code>[0.00 &ndash; 0.07]</code>. 93% of the numerical range is wasted on a single outlier!</li>
          <li><strong>StandardScaler Distorts:</strong> The outlier drags the mean up to 88.9, forcing normal data points into negative Z-scores and shrinking their resolution.</li>
          <li><strong>RobustScaler Triumphs:</strong> The median (40) and IQR (20) ignore the outlier completely. The normal points expand comfortably across <code>[-1.00, +0.75]</code>, preserving full feature resolution for the ML algorithm!</li>
        </ul>
      </div>
    </div>

    <h3>Step-by-Step Worked Outlier Calculation</h3>
    <p>
      Consider a 9-observation dataset containing one severe anomaly:
      <br><code>X = [20, 25, 30, 35, 40, 45, 50, 55, 500]</code>
    </p>
    <ol>
      <li><strong>Find Median (50th percentile, index 4):</strong> <code>Median = <strong>40.0</strong></code></li>
      <li><strong>Find Q1 (25th percentile, index 2):</strong> <code>Q1 = <strong>30.0</strong></code></li>
      <li><strong>Find Q3 (75th percentile, index 6):</strong> <code>Q3 = <strong>50.0</strong></code></li>
      <li><strong>Calculate IQR:</strong> <code>IQR = 50.0 - 30.0 = <strong>20.0</strong></code></li>
      <li><strong>Transform Inlier (x = 20):</strong> <code>x&apos; = (20 - 40) / 20 = -20 / 20 = <strong>-1.00</strong></code></li>
      <li><strong>Transform Median (x = 40):</strong> <code>x&apos; = (40 - 40) / 20 = 0 / 20 = <strong>0.00</strong></code></li>
      <li><strong>Transform Inlier (x = 55):</strong> <code>x&apos; = (55 - 40) / 20 = 15 / 20 = <strong>+0.75</strong></code></li>
      <li><strong>Transform Outlier (x = 500):</strong> <code>x&apos; = (500 - 40) / 20 = 460 / 20 = <strong>+23.00</strong></code></li>
    </ol>

    <div class="card card-concept">
      <div class="card-title"><span>&#9777;</span> Does RobustScaler Delete Outliers?</div>
      <p>
        <strong>No!</strong> RobustScaler does <em>not</em> filter, trim, or remove outliers from your dataset. It simply calculates centering and scaling parameters from the median and IQR so that the outliers <strong>cannot corrupt the transformation of regular data points</strong>. The outlier 500 remains in the dataset as <code>+23.00</code>, allowing anomaly detection models to still detect it.
      </p>
    </div>

    <h3>Scikit-Learn RobustScaler Implementation</h3>
    <div class="code-block">
      <div class="code-header">
        <span class="code-title">python_robust_scaler.py</span>
        <span class="code-lang">python</span>
      </div>
      <pre><code>import numpy as np
from sklearn.preprocessing import RobustScaler

X_with_outlier = np.array([[20], [25], [30], [35], [40], [45], [50], [55], [500]])

robust = RobustScaler()
X_robust = robust.fit_transform(X_with_outlier)

print("Robust Center (Median):", robust.center_)  # Output: [40.]
print("Robust Scale (IQR):", robust.scale_)        # Output: [20.]
print("Robust Scaled Values:\n", X_robust.flatten())
# Output: [-1.   -0.75 -0.5  -0.25  0.    0.25  0.5   0.75 23.  ]</code></pre>
    </div>
  </section>

  <!-- SECTION 7: NORMALIZATION: WHAT DOES IT MEAN? -->
  <section id="sec-07" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 07</span>
      <h2 class="section-title">Normalization: What Does It Mean?</h2>
    </div>
    <p class="section-intro">
      The word &ldquo;normalization&rdquo; is one of the most overloaded terms in machine learning. Beginners frequently make catastrophic engineering mistakes by confusing <em>feature-level scaling</em> with <em>sample-level vector normalization</em>.
    </p>

    <!-- FIGURE 7.8: ROW VS COLUMN OPERATIONS -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_ROW_VS_COLUMN_OPERATIONS}
      </div>
      <div class="diagram-caption">Figure 7.8: Column-wise Feature Scaling (vertical across samples) vs Row-wise Vector Normalization (horizontal across features within each sample).</div>
    </div>

    <h3>Two Conflicting Meanings of "Normalization"</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Concept</th>
            <th>Primary Direction</th>
            <th>What is Being Scaled?</th>
            <th>Standard Scikit-Learn Class</th>
            <th>Typical Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Meaning A: Range Scaling</strong></td>
            <td><strong>Column-wise (Vertical)</strong></td>
            <td>Scales an entire feature column across all dataset samples into a fixed range [0, 1].</td>
            <td><code>MinMaxScaler</code></td>
            <td>Tabular data with bounded physical quantities (e.g. image pixels, percentages).</td>
          </tr>
          <tr>
            <td><strong>Meaning B: Vector Normalization</strong></td>
            <td><strong>Row-wise (Horizontal)</strong></td>
            <td>Scales each individual sample row so that its vector length equals 1.0 (Unit Norm).</td>
            <td><code>Normalizer(norm='l2')</code></td>
            <td>Natural Language Processing (TF-IDF vectors), Document Cosine Similarity, Embeddings.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3>Vector Norms: L1 Norm vs L2 Norm</h3>
    <p>
      In linear algebra, a sample with <code>n</code> numerical features is treated as a vector <strong>x</strong> = [x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>] in n-dimensional space.
    </p>

    <div class="formula-card">
      <div class="formula-title">Mathematical Formulations: L2 and L1 Vector Norms</div>
      <div class="formula-box">||x||<sub>2</sub> = &radic;[ &Sigma;<sub>i=1</sub><sup>n</sup> x<sub>i</sub><sup>2</sup> ] &emsp;&emsp; (L2 Euclidean Norm)</div>
      <br>
      <div class="formula-box">||x||<sub>1</sub> = &Sigma;<sub>i=1</sub><sup>n</sup> |x<sub>i</sub>| &emsp;&emsp; (L1 Manhattan Norm)</div>
      <div class="formula-desc">
        <strong>L2 Vector Normalization:</strong> <code>x&apos; = x / ||x||<sub>2</sub></code> (Forces Euclidean distance from origin to equal exactly 1.0).
        <br>
        <strong>L1 Vector Normalization:</strong> <code>x&apos; = x / ||x||<sub>1</sub></code> (Forces the sum of absolute values to equal exactly 1.0, creating a discrete probability distribution).
      </div>
    </div>

    <!-- GRAPH 6 & GRAPH 7 -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GRAPH_6_VECTOR_NORMALIZATION}
      </div>
      <div class="diagram-caption">Figure 7.9 (Graph 6): L2 Vector Normalization projects a vector onto the 2D Unit Circle (r = 1.0) while preserving its exact directional angle &theta;.</div>
    </div>

    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GRAPH_7_L1_VS_L2_NORM}
      </div>
      <div class="diagram-caption">Figure 7.10 (Graph 7): Geometric constraint shapes: L1 Diamond (|x| + |y| = 1) vs L2 Sphere (x&sup2; + y&sup2; = 1).</div>
    </div>

    <h3>Step-by-Step Worked Vector Normalization Example</h3>
    <p>
      Consider a single text document represented by two word counts: <code>v = [3, 4]</code>.
    </p>
    <ol>
      <li><strong>L2 Euclidean Normalization:</strong>
        <ul>
          <li>Calculate L2 Norm: <code>||v||<sub>2</sub> = &radic;(3<sup>2</sup> + 4<sup>2</sup>) = &radic;(9 + 16) = &radic;25 = <strong>5.0</strong></code></li>
          <li>Normalize components: <code>v&apos;<sub>L2</sub> = [3/5, 4/5] = <strong>[0.60, 0.80]</strong></code></li>
          <li>Verify resulting length: <code>&radic;(0.6<sup>2</sup> + 0.8<sup>2</sup>) = &radic;(0.36 + 0.64) = &radic;1.0 = <strong>1.000</strong> &check;</code></li>
        </ul>
      </li>
      <li><strong>L1 Manhattan Normalization:</strong>
        <ul>
          <li>Calculate L1 Norm: <code>||v||<sub>1</sub> = |3| + |4| = <strong>7.0</strong></code></li>
          <li>Normalize components: <code>v&apos;<sub>L1</sub> = [3/7, 4/7] &approx; <strong>[0.4286, 0.5714]</strong></code></li>
          <li>Verify resulting sum: <code>3/7 + 4/7 = 7/7 = <strong>1.000</strong> &check;</code></li>
        </ul>
      </li>
    </ol>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> The Zero-Vector Edge Case in Normalizer</div>
      <p>
        What happens if an observation has all zeros (e.g. <code>[0.0, 0.0, 0.0]</code>)?
        <br>Its L2 norm is <code>||v|| = 0</code>. Dividing by zero is undefined!
      </p>
      <p>
        Scikit-Learn&apos;s <code>Normalizer</code> defensively checks for zero norms: if a row vector has length zero, it bypasses division and outputs all zeros, avoiding <code>NaN</code> values.
      </p>
    </div>

    <h3>Scikit-Learn Normalizer Implementation</h3>
    <div class="code-block">
      <div class="code-header">
        <span class="code-title">python_normalizer.py</span>
        <span class="code-lang">python</span>
      </div>
      <pre><code>import numpy as np
from sklearn.preprocessing import Normalizer

# Matrix of 2 text sample rows across 2 vocabulary word features
X_samples = np.array([
    [3.0, 4.0],   # Sample 1 (Norm = 5.0)
    [1.0, 1.0]    # Sample 2 (Norm = &radic;2 &approx; 1.414)
])

# L2 Unit Normalization (Default)
normalizer_l2 = Normalizer(norm='l2')
X_l2 = normalizer_l2.fit_transform(X_samples)

print("L2 Normalized Matrix:\n", np.round(X_l2, 3))
# Output:
# [[0.6   0.8  ]
#  [0.707 0.707]]

# Verify row norms equal 1.0
print("Sample 1 L2 Length:", np.linalg.norm(X_l2[0]))  # 1.0
print("Sample 2 L2 Length:", np.linalg.norm(X_l2[1]))  # 1.0</code></pre>
    </div>
  </section>

  <!-- SECTION 8: FEATURE SCALING VERSUS NORMALIZATION VERSUS STANDARDIZATION -->
  <section id="sec-08" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 08</span>
      <h2 class="section-title">Feature Scaling vs Normalization vs Standardization</h2>
    </div>
    <p class="section-intro">
      Below is the comprehensive architectural comparison matrix contrasting all five primary scaling and normalization methods.
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Method</th>
            <th>Primary Direction</th>
            <th>Quantities Used</th>
            <th>Output Range</th>
            <th>Outlier Sensitivity</th>
            <th>Best Suited For</th>
            <th>Main Limitations</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Min-Max Scaling</strong></td>
            <td>Column-wise (Features)</td>
            <td><code>x<sub>min</sub></code>, <code>x<sub>max</sub></code></td>
            <td>Strictly <code>[0, 1]</code> (training)</td>
            <td><span class="key-badge badge-high">High</span></td>
            <td>Neural networks (bounded activation functions), Image RGB pixels, algorithms requiring positive inputs.</td>
            <td>Extreme outliers crush non-outliers into a narrow band; unseen test data can exceed bounds.</td>
          </tr>
          <tr>
            <td><strong>Standardization (Z-Score)</strong></td>
            <td>Column-wise (Features)</td>
            <td>Mean <code>&mu;</code>, Std <code>&sigma;</code></td>
            <td>Unbounded (Centered at 0, &sigma;=1)</td>
            <td><span class="key-badge badge-high">High</span></td>
            <td><strong>Default choice</strong> for KNN, SVM, Logistic Regression, PCA, Ridge/Lasso, and Gradient Descent.</td>
            <td>Outliers distort mean and variance; does not bound data into [0, 1]; does not make skewed data normal.</td>
          </tr>
          <tr>
            <td><strong>Robust Scaling</strong></td>
            <td>Column-wise (Features)</td>
            <td>Median, IQR (Q3 - Q1)</td>
            <td>Unbounded (Centered at 0)</td>
            <td><span class="key-badge badge-robust">Very Low (Resistant)</span></td>
            <td>Datasets with severe outliers, financial transactions with fraud spikes, heavy-tailed data.</td>
            <td>Does not guarantee fixed bounds; does not remove outliers; less intuitive than Z-scores.</td>
          </tr>
          <tr>
            <td><strong>L1 Normalization</strong></td>
            <td>Row-wise (Samples)</td>
            <td>Sum of absolute values <code>&Sigma;|x<sub>i</sub>|</code></td>
            <td>Unit Sum <code>&Sigma;|x&apos;<sub>i</sub>| = 1.0</code></td>
            <td><span class="key-badge badge-std">Moderate</span></td>
            <td>Converting feature counts into probability distributions; sparse frequency models.</td>
            <td>Discards overall magnitude/volume information of the sample row entirely.</td>
          </tr>
          <tr>
            <td><strong>L2 Normalization</strong></td>
            <td>Row-wise (Samples)</td>
            <td>Euclidean Norm <code>&radic;&Sigma;x<sub>i</sub><sup>2</sup></code></td>
            <td>Unit Length <code>||x&apos;||<sub>2</sub> = 1.0</code></td>
            <td><span class="key-badge badge-std">Moderate</span></td>
            <td>Cosine similarity, text mining (TF-IDF), vector embeddings, search ranking.</td>
            <td>Discards sample magnitude; meaningless for general tabular columns with mixed units.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3>The 5-Step Beginner Decision Guide</h3>
    <ol>
      <li><strong>Step 1: Check your model family.</strong>
        <br>If using pure tree-based models (Random Forest, Gradient Boosting, XGBoost), scaling is <em>optional and usually unnecessary</em>. If using KNN, SVM, K-Means, PCA, Linear/Logistic regression with regularization, or Neural Networks, scaling is <strong>mandatory</strong>.
      </li>
      <li><strong>Step 2: Check for extreme outliers.</strong>
        <br>If your dataset contains massive outliers (e.g. billionaire salaries, viral click bursts), use <strong>RobustScaler</strong> to prevent parameter corruption.
      </li>
      <li><strong>Step 3: Check if bounded intervals are required.</strong>
        <br>If your model requires non-negative inputs or strictly bounded values in <code>[0, 1]</code> (e.g. neural network sigmoid layers or image RGB channels), use <strong>MinMaxScaler</strong>.
      </li>
      <li><strong>Step 4: Use StandardScaler as the universal default.</strong>
        <br>For general tabular datasets without extreme outliers, <strong>StandardScaler</strong> provides the most numerically stable gradients and isotropic distances for distance-based estimators.
      </li>
      <li><strong>Step 5: Use Normalizer only for row-wise vector direction.</strong>
        <br>Never apply <code>Normalizer</code> across tabular features with mixed physical units. Reserve it for document vectors, embeddings, and cosine similarity tasks.
      </li>
    </ol>
  </section>
"""
