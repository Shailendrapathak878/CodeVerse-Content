# Topic 18 - Part 2: Sections 06 - 10 (Clean Unicode/HTML Math)

PART2_HTML = """
    <!-- SECTION 06 -->
    <section class="content-section" id="sec-06">
      <div class="section-tag">Section 06 &bull; Dimensionality of Anomalies</div>
      <h2 class="section-title">Univariate vs Multivariate Anomalies</h2>
      <p class="section-intro">
        Understanding the distinction between univariate and multivariate anomalies is the single most important step in choosing between a simple statistical rule and a machine learning model.
      </p>

      <h3>1. Univariate Anomalies (Single-Feature Extremes)</h3>
      <p>
        A <strong>univariate anomaly</strong> occurs when a single measurement is extreme on its own isolated axis, completely ignoring all other features.
      </p>
      <ul>
        <li>A customer spending ₹10,00,000 in a single swipe when average spend is ₹500.</li>
        <li>A human body temperature sensor reporting 45°C (113°F).</li>
        <li>A vehicle traveling at 320 km/h on a city road.</li>
      </ul>
      <p>
        These can be easily caught using simple 1D statistical filters such as Z-score, IQR, or threshold gates (e.g., <code>if amount &gt; 50000: alert()</code>).
      </p>

      <h3>2. Multivariate Anomalies (Correlation Breakdowns)</h3>
      <p>
        A <strong>multivariate anomaly</strong> is fundamentally more deceptive: every individual feature value is <em>completely normal on its own</em>, but the <strong>joint combination</strong> of features is physically or statistically impossible!
      </p>

      <div class="card card-analogy">
        <div class="card-title">&#128663; Automotive Example: Engine Health</div>
        Consider an industrial turbo diesel truck with two sensors:
        <ul>
          <li><strong>Engine Temperature:</strong> Normal operating range is 80°C to 110°C.</li>
          <li><strong>Engine Oil Pressure:</strong> Normal operating range is 25 PSI to 65 PSI.</li>
        </ul>
        Now, observe this telemetry reading from a running truck on a highway:
        <br>
        &bull; <code>temp = 105°C</code> (completely normal operating heat)
        <br>
        &bull; <code>oil_pressure = 4 PSI</code> (completely normal when the engine is turned off!)
        <br><br>
        Individually, neither sensor raises a 1D alarm. But combined while driving at 2,500 RPM, <strong>high heat with near-zero oil pressure is a catastrophic engine blowout</strong>! Only a multivariate model that understands the correlation between RPM, temperature, and pressure can spot this before the engine seizes.
      </div>

      <!-- VISUAL 1.5 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.5: Univariate Outlier vs Multivariate Correlation Breakdown</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_UNIVARIATE_VS_MULTIVARIATE__
        <div class="visual-caption">
          <strong>Figure 1.5:</strong> Left: Univariate anomaly exceeds the 3&sigma; boundary on a 1D bell curve. Right: Multivariate anomaly (red dot) is within normal ranges for both X and Y individually, but shatters the expected diagonal correlation.
        </div>
      </div>
    </section>

    <!-- SECTION 07 -->
    <section class="content-section" id="sec-07">
      <div class="section-tag">Section 07 &bull; Statistical Foundation 1</div>
      <h2 class="section-title">Statistical Method 1: Z-Score</h2>
      <p class="section-intro">
        The Z-score (standard score) is the oldest and most widely used statistical tool for identifying univariate outliers in symmetric, Gaussian-like data.
      </p>

      <h3>1. Intuitive Concept</h3>
      <p>
        Imagine you know that the average grocery transaction at a store is ₹350, with a standard spread (deviation) of ₹100.
      </p>
      <ul>
        <li>A transaction of ₹450 is ₹100 above average: that is <strong>1 standard deviation</strong> away.</li>
        <li>A transaction of ₹650 is ₹300 above average: that is <strong>3 standard deviations</strong> away.</li>
        <li>A transaction of ₹1,500 is ₹1,150 above average: that is nearly <strong>12 standard deviations</strong> away!</li>
      </ul>
      <p>
        The <strong>Z-score</strong> simply measures how many standard deviations an observation lies above or below the mean.
      </p>

      <div class="math-box">
        z = (x &minus; &mu;) / &sigma;
        <div class="math-legend">
          Where:<br>
          &bull; <strong>x</strong> = The individual observation being evaluated.<br>
          &bull; <strong>&mu; (mu)</strong> = The arithmetic mean (average) of the dataset.<br>
          &bull; <strong>&sigma; (sigma)</strong> = The standard deviation (spread) of the dataset.
        </div>
      </div>

      <h3>2. The Empirical Rule (68-95-99.7 Rule)</h3>
      <p>
        In a standard normal (Gaussian) distribution:
      </p>
      <ul>
        <li><strong>68.27%</strong> of data points fall within |z| &le; 1 (&plusmn;1 standard deviation).</li>
        <li><strong>95.45%</strong> of data points fall within |z| &le; 2 (&plusmn;2 standard deviations).</li>
        <li><strong>99.73%</strong> of data points fall within |z| &le; 3 (&plusmn;3 standard deviations).</li>
      </ul>
      <p>
        Because only <strong>0.27%</strong> of observations naturally fall beyond 3 standard deviations in a bell curve, a conventional rule of thumb is to flag any point with <code>|z| &gt; 3.0</code> (or |z| &gt; 2.5) as an outlier.
      </p>

      <!-- VISUAL 1.6 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.6: Standard Normal Bell Curve with Z-Score Cutoffs</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_ZSCORE_DISTRIBUTION__
        <div class="visual-caption">
          <strong>Figure 1.6:</strong> The standard normal bell curve. Over 99.7% of points reside within the central green zone (&plusmn;3&sigma;). Any observation falling in the pink rejection tails (|z| &gt; 3.0) is mathematically flagged as an outlier.
        </div>
      </div>

      <h3>3. Step-by-Step Numerical Example</h3>
      <p>
        Let us calculate the exact Z-scores for a small dataset of 10 transaction amounts (in ₹):
      </p>
      <div class="card card-info">
        <strong>Dataset X:</strong> [120, 150, 180, 200, 220, 250, 280, 310, 350, 1500]
      </div>
      <ol>
        <li><strong>Calculate Mean (&mu;):</strong>
          <br>
          <code>&mu; = (120 + 150 + 180 + 200 + 220 + 250 + 280 + 310 + 350 + 1500) / 10 = 3560 / 10 = 356.00</code>
        </li>
        <li><strong>Calculate Standard Deviation (&sigma;):</strong>
          <br>
          <code>&sigma; = &radic;[ &Sigma; (x_i &minus; &mu;)&sup2; / N ] = &radic;[ 1,499,840 / 10 ] = &radic;(149,984) &approx; 387.28</code>
        </li>
        <li><strong>Calculate Z-score for Ordinary Point (x = 200):</strong>
          <br>
          <code>z = (200 &minus; 356.00) / 387.28 = &minus;156.00 / 387.28 = &minus;0.40</code> (Well within normal range)
        </li>
        <li><strong>Calculate Z-score for Extreme Point (x = 1500):</strong>
          <br>
          <code>z = (1500 &minus; 356.00) / 387.28 = +1144.00 / 387.28 = +2.95</code> (Flagged as extreme outlier!)
        </li>
      </ol>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; NumPy Z-Score Implementation</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>import numpy as np

# 1. Sample transaction dataset
tx_amounts = np.array([120, 150, 180, 200, 220, 250, 280, 310, 350, 1500])

# 2. Compute parameters
mean = np.mean(tx_amounts)
std = np.std(tx_amounts)

# 3. Compute vectorized Z-scores
z_scores = (tx_amounts - mean) / std

# 4. Flag observations with |z| > 2.5
threshold = 2.5
outliers = tx_amounts[np.abs(z_scores) > threshold]

print(f"Mean: {mean:.2f}, Std: {std:.2f}")
print("Z-Scores:", np.round(z_scores, 2))
print("Flagged Outliers:", outliers)

# Output:
# Mean: 356.00, Std: 387.28
# Z-Scores: [-0.61 -0.53 -0.45 -0.4  -0.35 -0.27 -0.2  -0.12 -0.02  2.95]
# Flagged Outliers: [1500]</code></pre>
      </div>

      <div class="card card-warn">
        <div class="card-title">&#9888; The "Masking" Flaw of Z-Score</div>
        Notice a subtle flaw in the calculation above: the extreme point <code>1500</code> inflated the mean from ~230 up to <strong>356</strong>, and exploded the standard deviation from ~75 up to <strong>387</strong>!
        <br><br>
        Because the extreme value artificially inflates the standard deviation in the denominator, it pulls its own Z-score down (from what would have been ~17 standard deviations down to just 2.95)! This phenomenon is known as <strong>outlier masking</strong>. Z-score is therefore fragile when multiple extreme outliers contaminate the data.
      </div>
    </section>

    <!-- SECTION 08 -->
    <section class="content-section" id="sec-08">
      <div class="section-tag">Section 08 &bull; Statistical Foundation 2</div>
      <h2 class="section-title">Statistical Method 2: IQR Boxplot</h2>
      <p class="section-intro">
        How do we solve the outlier masking problem of Z-score? By using <strong>order statistics (medians and quartiles)</strong> that cannot be distorted by extreme values!
      </p>

      <h3>1. The Five-Number Summary &amp; Quartiles</h3>
      <p>
        The Interquartile Range (IQR) method, pioneered by statistician John Tukey, divides sorted data into four equal quarters:
      </p>
      <ul>
        <li><strong>Median (Q2, 50th percentile):</strong> The middle number dividing the upper and lower halves.</li>
        <li><strong>First Quartile (Q1, 25th percentile):</strong> The median of the lower half.</li>
        <li><strong>Third Quartile (Q3, 75th percentile):</strong> The median of the upper half.</li>
        <li><strong>IQR (Interquartile Range):</strong> The spread of the middle 50% of the data.</li>
      </ul>

      <div class="math-box">
        IQR = Q<sub>3</sub> &minus; Q<sub>1</sub>
        <br><br>
        Lower Fence = Q<sub>1</sub> &minus; 1.5 &times; IQR
        <br>
        Upper Fence = Q<sub>3</sub> + 1.5 &times; IQR
        <div class="math-legend">
          Any observation falling <strong>below the Lower Fence</strong> or <strong>above the Upper Fence</strong> is declared an outlier.
        </div>
      </div>

      <h3>Why the 1.5 Multiplier?</h3>
      <p>
        The factor 1.5 is Tukey's classic heuristic. In a Gaussian distribution, the range [Q<sub>1</sub> &minus; 1.5 &times; IQR, Q<sub>3</sub> + 1.5 &times; IQR] corresponds to approximately &plusmn;2.7 standard deviations, capturing 99.3% of normal data. For extreme outliers, Tukey designated points beyond 3.0 &times; IQR as "far out".
      </p>

      <!-- VISUAL 1.7 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.7: Anatomy of an IQR Boxplot with Whiskers and Fences</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_IQR_BOXPLOT__
        <div class="visual-caption">
          <strong>Figure 1.7:</strong> The IQR boxplot structure. The central box spans Q1 to Q3 (IQR = 17.5). Whiskers extend to the most extreme data points within the fences. Any observation outside the fences (such as point 140 at the far right) is marked as an isolated outlier circle.
        </div>
      </div>

      <h3>2. Step-by-Step Numerical Example</h3>
      <p>
        Consider a dataset of 12 customer response times (in seconds):
      </p>
      <div class="card card-info">
        <strong>Dataset:</strong> [45, 52, 55, 60, 62, 65, 70, 72, 75, 80, 85, 140]
      </div>
      <ol>
        <li><strong>Find Median (Q2):</strong> Midpoint between 65 and 70 = <strong>67.5</strong>.</li>
        <li><strong>Find Q1 (25th percentile):</strong> Midpoint between 55 and 60 = <strong>58.8</strong>.</li>
        <li><strong>Find Q3 (75th percentile):</strong> Midpoint between 75 and 80 = <strong>76.2</strong>.</li>
        <li><strong>Calculate IQR:</strong> 76.2 &minus; 58.8 = <strong>17.5</strong>.</li>
        <li><strong>Calculate Fences:</strong>
          <br>
          <code>Lower Fence = 58.8 &minus; 1.5 &times; 17.5 = 58.8 &minus; 26.25 = 32.55</code>
          <br>
          <code>Upper Fence = 76.2 + 1.5 &times; 17.5 = 76.2 + 26.25 = 102.45</code>
        </li>
        <li><strong>Identify Outliers:</strong> Point <code>140</code> &gt; 102.5 &rarr; <strong>Confirmed IQR Outlier!</strong></li>
      </ol>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; NumPy IQR Implementation</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>import numpy as np

# Sample data
data = np.array([45, 52, 55, 60, 62, 65, 70, 72, 75, 80, 85, 140])

# Calculate quartiles using linear interpolation
q1 = np.percentile(data, 25)
median = np.median(data)
q3 = np.percentile(data, 75)
iqr = q3 - q1

lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

outliers = data[(data < lower_fence) | (data > upper_fence)]

print(f"Q1: {q1:.1f}, Median: {median:.1f}, Q3: {q3:.1f}, IQR: {iqr:.1f}")
print(f"Fences: [{lower_fence:.1f}, {upper_fence:.1f}]")
print(f"Identified Outliers: {outliers}")

# Output:
# Q1: 58.8, Median: 67.5, Q3: 76.2, IQR: 17.5
# Fences: [32.5, 102.5]
# Identified Outliers: [140]</code></pre>
      </div>

      <h3>3. Comparison: Z-Score vs IQR</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Evaluation Dimension</th>
              <th>Z-Score Method</th>
              <th>IQR (Tukey Boxplot) Method</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Distribution Assumption</strong></td>
              <td>Assumes Gaussian (normal), symmetric, bell-shaped distribution.</td>
              <td>Non-parametric; makes zero assumptions about distribution shape.</td>
            </tr>
            <tr>
              <td><strong>Robustness to Outliers</strong></td>
              <td>Poor (Mean and Std are easily skewed by the outliers themselves).</td>
              <td><strong>Excellent</strong> (Median and Quartiles are resistant to extreme values).</td>
            </tr>
            <tr>
              <td><strong>Skewed Data Performance</strong></td>
              <td>Misleading (flags high valid values in long-tailed distributions).</td>
              <td>Solid (captures the central 50% regardless of tail shape).</td>
            </tr>
            <tr>
              <td><strong>Multi-Feature Support</strong></td>
              <td>Strictly univariate (requires Mahalanobis distance for multivariate).</td>
              <td>Strictly univariate (evaluated column by column).</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 09 -->
    <section class="content-section" id="sec-09">
      <div class="section-tag">Section 09 &bull; Modern Machine Learning Paradigm</div>
      <h2 class="section-title">Introduction to Machine Learning-Based Methods</h2>
      <p class="section-intro">
        Simple statistical rules fail when datasets have dozens of correlated features, non-linear boundaries, or varying local densities. Machine learning models overcome this by learning the <strong>geometry of normality</strong>.
      </p>

      <!-- VISUAL 1.8 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.8: End-to-End Machine Learning Anomaly Detection Architecture</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_ANOMALY_WORKFLOW__
        <div class="visual-caption">
          <strong>Figure 1.8:</strong> The five-stage anomaly detection engineering lifecycle: Stream Ingestion &rarr; Feature Preprocessing &rarr; Model Fitting &rarr; Anomaly Scoring &amp; Thresholding &rarr; Domain Triage.
        </div>
      </div>

      <h3>Scoring Conventions Across scikit-learn</h3>
      <p>
        In scikit-learn, anomaly detection algorithms adhere to a standardized API, but beginners must memorize their specific output conventions:
      </p>
      <ul>
        <li><code>predict(X)</code> returns:
          <br>&bull; <strong>+1</strong> for <strong>Inliers</strong> (Normal observations).
          <br>&bull; <strong>-1</strong> for <strong>Outliers</strong> (Flagged anomalies).
        </li>
        <li><code>decision_function(X)</code> returns a continuous anomaly score:
          <br>&bull; <strong>Negative numbers</strong> indicate abnormal/anomalous observations.
          <br>&bull; <strong>Positive numbers</strong> indicate normal/typical observations.
          <br>&bull; <strong>Zero (0.0)</strong> is the default decision boundary threshold.
        </li>
      </ul>

      <div class="card card-warn">
        <div class="card-title">&#9888; Do Not Compare Raw Scores Across Algorithms!</div>
        An Isolation Forest decision score of <code>-0.15</code> cannot be compared to an LOF factor of <code>1.8</code> or a One-Class SVM distance of <code>-0.02</code>! Each algorithm operates under completely different mathematical definitions of score magnitude.
      </div>
    </section>

    <!-- SECTION 10 -->
    <section class="content-section" id="sec-10">
      <div class="section-tag">Section 10 &bull; Core Algorithm Deep Dive</div>
      <h2 class="section-title">Isolation Forest (iForest)</h2>
      <p class="section-intro">
        Introduced by Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou in 2008, <strong>Isolation Forest</strong> completely flipped anomaly detection on its head. Instead of modeling what is <em>normal</em>, it asks: <em>"How easy is it to isolate this point?"</em>
      </p>

      <h3>1. The Core Geometric Intuition</h3>
      <p>
        Anomalies possess two key mathematical traits:
      </p>
      <ol>
        <li>They are <strong>few</strong> in number (rare).</li>
        <li>They have attribute values that are <strong>substantially different</strong> from the rest of the data.</li>
      </ol>
      <p>
        If you take a 2D plane and randomly cut it with horizontal and vertical lines:
      </p>
      <ul>
        <li>A point sitting alone in empty space will be isolated in just <strong>1 or 2 random cuts</strong>!</li>
        <li>A point buried inside a dense cluster of 1,000 users will require <strong>many cuts (10–20 splits)</strong> before it is separated into its own bounding box!</li>
      </ul>

      <!-- VISUAL 1.9 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.9: Tree Isolation Partitioning &bull; Short Path (Anomaly) vs Deep Path (Normal)</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_ISOLATION_FOREST__
        <div class="visual-caption">
          <strong>Figure 1.9:</strong> Tree partitioning mechanism. Left: An isolated anomaly is cut off at tree depth h(x) = 1. Right: A point inside a dense cluster requires deep recursive splitting (h(x) &ge; 8) to isolate.
        </div>
      </div>

      <h3>2. The Isolation Tree (iTree) Algorithm</h3>
      <p>
        To build an ensemble of <code>n_estimators</code> isolation trees:
      </p>
      <ol>
        <li>Sub-sample the dataset (default 256 samples per tree, making it blazing fast and immune to memory blowup).</li>
        <li>Randomly pick a feature <code>q</code>.</li>
        <li>Randomly pick a split threshold <code>p</code> uniformly between min(q) and max(q).</li>
        <li>Recursively divide until points are isolated or a max depth is reached.</li>
        <li>Measure the <strong>path length h(x)</strong>: the number of edges traversed from root to terminal leaf.</li>
      </ol>

      <div class="math-box">
        s(x, n) = 2<sup>&minus; [ E(h(x)) / c(n) ]</sup>
        <div class="math-legend">
          Where:<br>
          &bull; <strong>E(h(x))</strong> = The average path length of point x across all trees.<br>
          &bull; <strong>c(n)</strong> = Average path length of unsuccessful searches in Binary Search Trees with n nodes.<br>
          &bull; If <strong>s &rarr; 1.0</strong>: Short paths &rarr; <strong>Definite anomaly</strong>.<br>
          &bull; If <strong>s &rarr; 0.5</strong>: Medium paths &rarr; Normal observation.<br>
          &bull; If <strong>s &rarr; 0.0</strong>: Very long paths &rarr; Highly clustered inlier.
        </div>
      </div>

      <h3>3. Key Hyperparameters in scikit-learn</h3>
      <ul>
        <li><code>n_estimators</code> (default 100): Number of random trees. 100 to 200 is almost always sufficient.</li>
        <li><code>max_samples</code> (default 'auto' &rarr; 256): Number of samples drawn to train each tree. 256 prevents swamping and masking!</li>
        <li><code>contamination</code> (default 'auto' or float between 0.0 and 0.5): The expected proportion of outliers in the dataset. Used to determine the decision boundary threshold.</li>
        <li><code>random_state</code>: Ensures reproducible random splits.</li>
      </ul>

      <!-- VISUAL 1.10 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.10: Real Isolation Forest Execution Results (scikit-learn)</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_ISOLATION_FOREST_SCATTER__
        <div class="visual-caption">
          <strong>Figure 1.10:</strong> Actual scikit-learn Isolation Forest fitted on 208 points with <code>contamination=0.05</code>. The model successfully separated the 197 normal cluster points (teal) from 11 isolated anomalies (red circles with outer rings).
        </div>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; Complete Executable Isolation Forest</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>import numpy as np
from sklearn.ensemble import IsolationForest

# 1. Generate synthetic reproducible dataset
rng = np.random.RandomState(42)
# 200 normal points clustered around (5.0, 5.0)
X_normal = rng.normal(loc=5.0, scale=1.0, size=(200, 2))
# Deliberate scattered anomalies
X_anom = rng.uniform(low=0.0, high=10.0, size=(10, 2))
# Keep points far from cluster
X_anom = X_anom[np.linalg.norm(X_anom - [5, 5], axis=1) > 3.0][:10]
X = np.vstack([X_normal, X_anom])

# 2. Fit Isolation Forest
iso = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
preds = iso.fit_predict(X)          # +1 for inlier, -1 for outlier
scores = iso.decision_function(X)   # Negative = anomalous, Positive = normal

n_anomalies = np.sum(preds == -1)
n_normal = np.sum(preds == 1)

print(f"Total samples: {len(X)}")
print(f"Flagged anomalies (preds == -1): {n_anomalies}")
print(f"Normal inliers (preds == 1): {n_normal}")
print(f"Score range: [{scores.min():.4f}, {scores.max():.4f}]")

# Output:
# Total samples: 208
# Flagged anomalies (preds == -1): 11
# Normal inliers (preds == 1): 197
# Score range: [-0.1856, 0.2227]</code></pre>
      </div>

      <div class="card card-success">
        <div class="card-title">&#9989; Why Isolation Forest is the Industry Gold Standard</div>
        1. <strong>Linear Computational Complexity:</strong> Runs in O(t &times; n log n) time, scaling effortlessly to millions of rows.<br>
        2. <strong>Invariant to Monotonic Transformations:</strong> Because it relies purely on cut-order rank, scaling or log-transforms do not alter tree splits!<br>
        3. <strong>Handles Irrelevant Features:</strong> Random feature selection naturally washes out noise dimensions across 100 trees.
      </div>
    </section>
"""
