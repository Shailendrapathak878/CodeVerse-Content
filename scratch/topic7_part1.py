"""
Module: topic7_part1.py
Contains HTML for Header, Hero Card, Table of Contents, and Sections 1 to 4.
"""

from scratch.topic7_svgs import (
    SVG_HERO_SCALING_OVERVIEW,
    SVG_WHY_SCALE_DISTANCE_DOMINANCE,
    SVG_STATISTICAL_SPREAD_ANATOMY,
    SVG_GRAPH_2_MINMAX_BEFORE_AFTER
)

PART1_HTML = f"""
  <!-- HERO CARD -->
  <div class="hero-card">
    <div class="hero-badge">Machine Learning &bull; Topic 7 &bull; Light Mode</div>
    <h1 class="hero-title">Feature Scaling &amp; Normalization</h1>
    <p class="hero-subtitle">
      Master the mathematical art of numerical calibration. Learn why machine learning algorithms fail on unscaled data, how to balance heterogeneous feature magnitudes, the critical differences between Min-Max Scaling, Standardization, Robust Scaling, and Vector Normalization, and how to build leak-free production pipelines.
    </p>
    <div class="hero-meta">
      <span class="meta-tag"><strong>Difficulty:</strong> Beginner &rarr; Production</span>
      <span class="meta-tag"><strong>Focus:</strong> Numerical Preprocessing &amp; MLOps</span>
      <span class="meta-tag"><strong>Tooling:</strong> Scikit-Learn 1.9+ &bull; Pandas 2.3+ &bull; NumPy 2.5+</span>
      <span class="meta-tag"><strong>Theme:</strong> Strict Light Mode</span>
    </div>
  </div>

  <!-- TABLE OF CONTENTS -->
  <div class="toc-container">
    <div class="toc-title">
      <span>&#128218;</span> Chapter Table of Contents
    </div>
    <div class="toc-grid">
      <ul class="toc-list">
        <li class="toc-item"><a href="#sec-01"><span class="toc-number">01</span> Introduction to Feature Scaling</a></li>
        <li class="toc-item"><a href="#sec-02"><span class="toc-number">02</span> Why Do We Need Feature Scaling?</a></li>
        <li class="toc-item"><a href="#sec-03"><span class="toc-number">03</span> Important Statistical Foundations</a></li>
        <li class="toc-item"><a href="#sec-04"><span class="toc-number">04</span> Min-Max Scaling (0 to 1 Normalization)</a></li>
        <li class="toc-item"><a href="#sec-05"><span class="toc-number">05</span> Standardization and Z-Score Scaling</a></li>
        <li class="toc-item"><a href="#sec-06"><span class="toc-number">06</span> Robust Scaling (Outlier-Resistant)</a></li>
        <li class="toc-item"><a href="#sec-07"><span class="toc-number">07</span> Normalization: What Does It Mean?</a></li>
        <li class="toc-item"><a href="#sec-08"><span class="toc-number">08</span> Grand Comparison &amp; Decision Framework</a></li>
      </ul>
      <ul class="toc-list">
        <li class="toc-item"><a href="#sec-09"><span class="toc-number">09</span> Visual Exploratory Graphs (Graphs 1 to 9)</a></li>
        <li class="toc-item"><a href="#sec-10"><span class="toc-number">10</span> Which Algorithms Need Scaling?</a></li>
        <li class="toc-item"><a href="#sec-11"><span class="toc-number">11</span> Data Leakage &amp; Preprocessing Pipelines</a></li>
        <li class="toc-item"><a href="#sec-12"><span class="toc-number">12</span> Handling Edge Cases &amp; Special Features</a></li>
        <li class="toc-item"><a href="#sec-13"><span class="toc-number">13</span> Complete Hands-On Python Lab</a></li>
        <li class="toc-item"><a href="#sec-14"><span class="toc-number">14</span> Real-World Industry Case Studies</a></li>
        <li class="toc-item"><a href="#sec-15"><span class="toc-number">15</span> 14 Common Beginner Mistakes &amp; Fixes</a></li>
        <li class="toc-item"><a href="#sec-16"><span class="toc-number">16</span> Checklist, Glossary, Q&amp;A &amp; Final Challenge</a></li>
      </ul>
    </div>
  </div>

  <!-- SECTION 1: INTRODUCTION TO FEATURE SCALING -->
  <section id="sec-01" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 01</span>
      <h2 class="section-title">Introduction to Feature Scaling</h2>
    </div>
    <p class="section-intro">
      In machine learning, real-world data arrives as a mixture of different physical units, measurement conventions, and numerical magnitudes. A single dataset describing customers might record a person&apos;s age in tens of years, their annual income in hundreds of thousands of dollars, and their number of store visits as single digits.
    </p>

    <div class="card card-def">
      <div class="card-title"><span>&#128214;</span> Formal Definition: Feature Scale</div>
      <p>
        A <strong>numerical feature</strong> is an individual measurable property or characteristic of a phenomenon being observed. The <strong>scale</strong> or <strong>magnitude</strong> of a feature refers to the range of numerical values it spans across observations in the dataset.
      </p>
      <p>
        <strong>Feature Scaling</strong> is a data preprocessing technique used to transform numerical features of varying ranges and units into a common, proportional numerical scale so that mathematical algorithms treat them equitably.
      </p>
    </div>

    <h3>The Magnitude Disparity Problem</h3>
    <p>
      Consider three typical customer attributes recorded in an e-commerce credit evaluation database:
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Feature Name</th>
            <th>Physical Unit</th>
            <th>Typical Numerical Range</th>
            <th>Approximate Span</th>
            <th>Order of Magnitude</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Age</strong></td>
            <td>Years</td>
            <td><code>18 &ndash; 65</code></td>
            <td><code>47</code></td>
            <td>~ 10<sup>1</sup> (Tens)</td>
          </tr>
          <tr>
            <td><strong>Annual Income</strong></td>
            <td>US Dollars ($)</td>
            <td><code>$30,000 &ndash; $850,000</code></td>
            <td><code>$820,000</code></td>
            <td>~ 10<sup>5</sup> &ndash; 10<sup>6</sup> (Hundreds of Thousands)</td>
          </tr>
          <tr>
            <td><strong>Years of Experience</strong></td>
            <td>Years</td>
            <td><code>0 &ndash; 30</code></td>
            <td><code>30</code></td>
            <td>~ 10<sup>1</sup> (Tens)</td>
          </tr>
          <tr>
            <td><strong>App Purchases / Month</strong></td>
            <td>Count</td>
            <td><code>1 &ndash; 15</code></td>
            <td><code>14</code></td>
            <td>~ 10<sup>0</sup> (Units)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> The Fundamental Trap: Big Numbers &ne; More Important</div>
      <p>
        Beginners often intuitively assume that an annual income of <code>$85,000</code> is mathematically "more significant" than an age of <code>35</code> because 85,000 is over 2,400 times larger than 35. <strong>This is completely false!</strong>
      </p>
      <p>
        The size of a number is simply an arbitrary artifact of its measurement unit. If we measure income in thousands of dollars (<code>$85k</code>), or if we measure age in minutes (<code>18,396,000 minutes</code>), the relative magnitudes reverse entirely without changing any real-world information! A mathematical equation that calculates Euclidean distances or matrix multiplications does not know what a "dollar" or a "year" is&mdash;it sees only raw float numbers.
      </p>
    </div>

    <div class="card card-analogy">
      <div class="card-title"><span>&#128161;</span> Everyday Analogy: The Currency &amp; Distance Exchange</div>
      <p>
        Imagine you are competing in a fitness triathlon where your overall score is the sum of your race distance and your registration fee. If your running distance is measured in kilometers (<code>10 km</code>) and your fee is paid in Japanese Yen (<code>50,000 &yen;</code>), adding them directly (<code>10 + 50,000 = 50,010</code>) means your running effort contributes less than 0.02% of your score! A runner who ran twice as far (<code>20 km</code>) would see almost zero difference.
      </p>
      <p>
        To make a fair athletic competition, both metrics must be converted into standard, normalized points (such as percentiles from 0 to 100). Feature scaling does exactly this for machine learning models.
      </p>
    </div>

    <!-- FIGURE 7.1: HERO SCALING OVERVIEW -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_HERO_SCALING_OVERVIEW}
      </div>
      <div class="diagram-caption">Figure 7.1: Multi-scale raw features entering a Feature Scaling engine and emerging in harmonized, equitable numerical intervals.</div>
      <div class="how-to-read">
        <div class="how-to-read-title"><span>&#128269;</span> How to Read This Architectural Diagram:</div>
        <ul>
          <li><strong>Left Box:</strong> Raw features possess radically different spans (Age spans 47 units; Income spans 820,000 units). On an uncalibrated plane, Income completely dwarfs Age.</li>
          <li><strong>Center Engine:</strong> Mathematical scalers (MinMaxScaler, StandardScaler, RobustScaler) apply deterministic transformations to calibrate scales.</li>
          <li><strong>Right Box:</strong> Scaled features occupy uniform numerical intervals (typically centered at 0 with standard deviation 1, or bounded between 0 and 1), allowing algorithms to evaluate all dimensions proportionally.</li>
        </ul>
      </div>
      <div class="diagram-takeaway">
        <strong>Key Takeaway:</strong> Feature scaling alters the <em>numerical representation</em> of data; it does <em>not</em> create new information or automatically guarantee superior model performance. Its purpose is to remove artificial scale distortions.
      </div>
    </div>
  </section>

  <!-- SECTION 2: WHY DO WE NEED FEATURE SCALING? -->
  <section id="sec-02" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 02</span>
      <h2 class="section-title">Why Do We Need Feature Scaling?</h2>
    </div>
    <p class="section-intro">
      Not all machine learning algorithms require feature scaling. Understanding <em>why</em> scaling is essential requires examining the internal mathematical machinery of different algorithm families.
    </p>

    <!-- FIGURE 7.2: DISTANCE DOMINANCE -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_WHY_SCALE_DISTANCE_DOMINANCE}
      </div>
      <div class="diagram-caption">Figure 7.2: Mathematical proof showing how an unscaled feature with large magnitude completely hijacks Euclidean distance calculations.</div>
      <div class="how-to-read">
        <div class="how-to-read-title"><span>&#128269;</span> Step-by-Step Distance Breakdown:</div>
        <p>
          Let observation A have <code>Age = 25</code>, <code>Income = $40,000</code>. Let observation B have <code>Age = 26</code>, <code>Income = $120,000</code>. Let observation C have <code>Age = 65</code>, <code>Income = $40,000</code>.
        </p>
        <p>
          <strong>Between A and B:</strong> The age difference is tiny (1 year), but the income difference is huge ($80,000). The Euclidean distance is &radic;(1<sup>2</sup> + 80,000<sup>2</sup>) = &radic;(1 + 6,400,000,000) &approx; <strong>80,000.000006</strong>.
        </p>
        <p>
          <strong>Between A and C:</strong> The income difference is $0, but the age difference is 40 years! The Euclidean distance is &radic;(40<sup>2</sup> + 0<sup>2</sup>) = <strong>40.0</strong>.
        </p>
        <p>
          Because 80,000 is dramatically larger than 40, the model declares A and C to be "almost identical" and A and B to be "infinitely far apart," completely ignoring that C is a senior citizen and A is a young adult!
        </p>
      </div>
    </div>

    <h3>Mathematical Reasons Across Algorithm Families</h3>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Algorithm Family</th>
            <th>Primary Mathematical Mechanism</th>
            <th>Scale Sensitivity</th>
            <th>Exact Impact of Unscaled Data</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>K-Nearest Neighbors (KNN)</strong></td>
            <td>Euclidean / Manhattan Distance metric: &radic;(&Sigma;(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup>)</td>
            <td><span class="key-badge badge-high">Extremely Sensitive</span></td>
            <td>Features with large spans dominate distance; features with small spans are effectively ignored.</td>
          </tr>
          <tr>
            <td><strong>K-Means Clustering</strong></td>
            <td>Distance between sample points and cluster centroids</td>
            <td><span class="key-badge badge-high">Extremely Sensitive</span></td>
            <td>Clusters form long, distorted ellipsoids aligned only with the feature having the largest variance.</td>
          </tr>
          <tr>
            <td><strong>Support Vector Machines (SVM)</strong></td>
            <td>Margin maximization and RBF Kernel: exp(-&gamma;||x<sub>1</sub> - x<sub>2</sub>||<sup>2</sup>)</td>
            <td><span class="key-badge badge-high">Extremely Sensitive</span></td>
            <td>RBF kernel bandwidth (&gamma;) collapses along the dominant feature, degrading classification boundaries.</td>
          </tr>
          <tr>
            <td><strong>Principal Component Analysis (PCA)</strong></td>
            <td>Orthogonal projection maximizing variance: Covariance matrix &Sigma;</td>
            <td><span class="key-badge badge-high">Extremely Sensitive</span></td>
            <td>PCA identifies the first principal component solely as the unscaled feature with the largest raw numerical variance.</td>
          </tr>
          <tr>
            <td><strong>Regularized Linear Models (Ridge / Lasso)</strong></td>
            <td>Loss + &lambda;&Sigma;w<sub>j</sub><sup>2</sup> or Loss + &lambda;&Sigma;|w<sub>j</sub>|</td>
            <td><span class="key-badge badge-high">Extremely Sensitive</span></td>
            <td>Features with small raw scales require massive weights (w) to impact prediction, causing regularization to unfairly penalize and zero them out!</td>
          </tr>
          <tr>
            <td><strong>Gradient Descent (Logistic Reg / Neural Nets)</strong></td>
            <td>Iterative weight updates: w &larr; w - &alpha; &nabla;L(w)</td>
            <td><span class="key-badge badge-std">Moderately Sensitive</span></td>
            <td>Loss surface forms an elongated canyon. Gradient oscillates wildly perpendicular to the valley, slowing convergence down by orders of magnitude.</td>
          </tr>
          <tr>
            <td><strong>Decision Trees &amp; Ensembles (Random Forest / XGBoost)</strong></td>
            <td>Orthogonal axis-aligned threshold splits: (feature &le; threshold)</td>
            <td><span class="key-badge badge-robust">Scale Invariant</span></td>
            <td>Trees evaluate ordering, not distances. Monotonic transformations preserve rank order; splits remain mathematically identical.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-concept">
      <div class="card-title"><span>&#9777;</span> The Regularization Paradox in Linear Regression</div>
      <p>
        Consider a linear model predicting house prices: <code>Price = w<sub>1</sub> &times; Area_sqft + w<sub>2</sub> &times; Bathrooms</code>.
      </p>
      <p>
        If <code>Area_sqft</code> spans <code>[500 &ndash; 5,000]</code> and <code>Bathrooms</code> spans <code>[1 &ndash; 4]</code>, each additional bathroom might increase house price by $20,000. To achieve this, the model requires <code>w<sub>2</sub> &approx; 20,000</code>. But for square footage, an extra square foot increases price by $100, requiring <code>w<sub>1</sub> &approx; 100</code>.
      </p>
      <p>
        When you apply <strong>L2 Regularization (Ridge)</strong>, the penalty is <code>&lambda;(w<sub>1</sub><sup>2</sup> + w<sub>2</sub><sup>2</sup>)</code>. Notice that <code>w<sub>2</sub><sup>2</sup> = 20,000<sup>2</sup> = 400,000,000</code>, while <code>w<sub>1</sub><sup>2</sup> = 10,000</code>! The penalty will mercilessly crush <code>w<sub>2</sub></code> towards zero simply because its physical unit is small. Standardizing both features beforehand ensures all weights are penalized equitably.
      </p>
    </div>
  </section>

  <!-- SECTION 3: IMPORTANT STATISTICAL FOUNDATIONS -->
  <section id="sec-03" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 03</span>
      <h2 class="section-title">Important Statistical Foundations</h2>
    </div>
    <p class="section-intro">
      Every feature scaler is fundamentally a statistical transformation. Before choosing a scaling formula, we must understand the core summary statistics used to measure location (center) and dispersion (spread).
    </p>

    <!-- FIGURE 7.3: SPREAD ANATOMY -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_STATISTICAL_SPREAD_ANATOMY}
      </div>
      <div class="diagram-caption">Figure 7.3: Anatomy of statistical spread: Minimum, Q1 (25th percentile), Median (50th percentile), Q3 (75th percentile), Interquartile Range (IQR), and Outliers.</div>
      <div class="how-to-read">
        <div class="how-to-read-title"><span>&#128269;</span> Key Statistical Measures Defined:</div>
        <ul>
          <li><strong>Minimum (x<sub>min</sub>):</strong> The smallest observed value in the sample. Highly sensitive to extreme negative outliers.</li>
          <li><strong>Maximum (x<sub>max</sub>):</strong> The largest observed value in the sample. Highly sensitive to extreme positive outliers.</li>
          <li><strong>Range (Span):</strong> <code>Range = x<sub>max</sub> - x<sub>min</sub></code>. The total numerical span of the feature.</li>
          <li><strong>Arithmetic Mean (&mu; or x&#772;):</strong> The sum of all observations divided by sample count: &mu; = (1/N) &Sigma; x<sub>i</sub>. Vulnerable to outlier distortion.</li>
          <li><strong>Median (Q2):</strong> The middle value when sorted in ascending order. Highly robust to outliers.</li>
          <li><strong>First Quartile (Q1):</strong> The 25th percentile; 25% of data falls below this value.</li>
          <li><strong>Third Quartile (Q3):</strong> The 75th percentile; 75% of data falls below this value.</li>
          <li><strong>Interquartile Range (IQR):</strong> <code>IQR = Q3 - Q1</code>. The central 50% span of the distribution. Completely immune to extreme outlier corruption.</li>
        </ul>
      </div>
    </div>

    <h3>Standard Deviation: Population (&sigma;) vs Sample (s)</h3>
    <p>
      A common source of confusion for beginners is the discrepancy between Pandas and Scikit-Learn when calculating standard deviation.
    </p>

    <div class="card card-amber">
      <div class="card-title"><span>&#128269;</span> The Degrees of Freedom (ddof) Convention</div>
      <p>
        <strong>Population Standard Deviation (&sigma;, ddof = 0):</strong> Divides the sum of squared differences by <code>N</code>. Used when data is treated as the complete population.
      </p>
      <div class="formula-box">&sigma; = &radic;[ (1 / N) &times; &Sigma; (x<sub>i</sub> - &mu;)<sup>2</sup> ]</div>
      <p>
        <strong>Sample Standard Deviation (s, ddof = 1):</strong> Divides by <code>N - 1</code> (Bessel&apos;s correction) to provide an unbiased estimator of population variance when sampling.
      </p>
      <div class="formula-box">s = &radic;[ (1 / (N - 1)) &times; &Sigma; (x<sub>i</sub> - x&#772;)<sup>2</sup> ]</div>
      <p>
        <strong>Critical Engineering Rule:</strong> Scikit-Learn&apos;s <code>StandardScaler</code> and NumPy&apos;s <code>np.std()</code> default to <strong>ddof = 0</strong> (&sigma;). Pandas&apos; <code>df['col'].std()</code> defaults to <strong>ddof = 1</strong> (s). Always use <code>ddof=0</code> when verifying Scikit-Learn calculations!
      </p>
    </div>
  </section>

  <!-- SECTION 4: MIN-MAX SCALING -->
  <section id="sec-04" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 04</span>
      <h2 class="section-title">Min-Max Scaling (0 to 1 Normalization)</h2>
    </div>
    <p class="section-intro">
      Min-Max Scaling (often called <em>Min-Max Normalization</em>) linearly maps all values of a feature into a fixed, user-defined closed interval&mdash;most commonly between <strong>0.0</strong> and <strong>1.0</strong>.
    </p>

    <div class="formula-card">
      <div class="formula-title">Mathematical Formula: Min-Max Scaling</div>
      <div class="formula-box">x&apos; = (x - x<sub>min</sub>) / (x<sub>max</sub> - x<sub>min</sub>)</div>
      <div class="formula-desc">
        Where:
        <ul>
          <li><strong>x:</strong> Original raw observation value.</li>
          <li><strong>x<sub>min</sub>:</strong> Minimum value of the feature observed in the training set.</li>
          <li><strong>x<sub>max</sub>:</strong> Maximum value of the feature observed in the training set.</li>
          <li><strong>(x<sub>max</sub> - x<sub>min</sub>):</strong> Total range (span) of the feature.</li>
          <li><strong>x&apos;:</strong> Scaled output value (strictly in [0, 1] for in-range training samples).</li>
        </ul>
      </div>
    </div>

    <!-- FIGURE 7.7 / GRAPH 2: MINMAX BEFORE AND AFTER -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GRAPH_2_MINMAX_BEFORE_AFTER}
      </div>
      <div class="diagram-caption">Figure 7.4 (Graph 2): Linear mapping of raw values [10, 20, 30] to [0.0, 0.5, 1.0], and how an unseen value (40) extends beyond 1.0.</div>
    </div>

    <h3>Step-by-Step Worked Numerical Example</h3>
    <p>
      Consider a simple feature with three training observations: <code>X = [10, 20, 30]</code>.
    </p>
    <ol>
      <li><strong>Find Minimum &amp; Maximum:</strong> <code>x<sub>min</sub> = 10</code>, <code>x<sub>max</sub> = 30</code>.</li>
      <li><strong>Calculate Span:</strong> <code>Span = 30 - 10 = 20</code>.</li>
      <li><strong>Transform Observation 1 (x = 10):</strong>
        <br><code>x&apos;<sub>1</sub> = (10 - 10) / 20 = 0 / 20 = <strong>0.0</strong></code>
      </li>
      <li><strong>Transform Observation 2 (x = 20):</strong>
        <br><code>x&apos;<sub>2</sub> = (20 - 10) / 20 = 10 / 20 = <strong>0.5</strong></code>
      </li>
      <li><strong>Transform Observation 3 (x = 30):</strong>
        <br><code>x&apos;<sub>3</sub> = (30 - 10) / 20 = 20 / 20 = <strong>1.0</strong></code>
      </li>
    </ol>
    <p>
      <strong>Verification:</strong> The minimum value maps to 0.0, the maximum maps to 1.0, and the midpoint 20 maps exactly to 0.5. The relative distance ratios between points are perfectly preserved!
    </p>

    <h3>Edge Cases &amp; Unseen Test Data</h3>
    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> What Happens When Test Data Exceeds Training Bounds?</div>
      <p>
        Suppose an unseen customer appears in the production test set with <code>x<sub>test</sub> = 40</code>.
      </p>
      <p>
        Because the scaler was fitted on training data where <code>x<sub>min</sub> = 10</code> and <code>x<sub>max</sub> = 30</code>:
      </p>
      <div class="formula-box">x&apos;<sub>test</sub> = (40 - 10) / (30 - 10) = 30 / 20 = <strong>1.5</strong></div>
      <p>
        Notice that <code>1.5</code> lies <strong>outside the [0, 1] range!</strong> Min-Max Scaling does <em>not</em> clip unseen test values by default unless explicitly configured via <code>MinMaxScaler(clip=True)</code> in Scikit-Learn.
      </p>
    </div>

    <div class="card card-def">
      <div class="card-title"><span>&#128214;</span> Constant Feature Behavior (Variance = 0)</div>
      <p>
        If all training values in a column are identical (e.g. <code>[20, 20, 20]</code>), then <code>x<sub>max</sub> - x<sub>min</sub> = 20 - 20 = 0</code>. Direct mathematical division by zero is undefined!
      </p>
      <p>
        Scikit-Learn&apos;s <code>MinMaxScaler</code> defensively handles this: if <code>x<sub>max</sub> == x<sub>min</sub></code>, it sets the scale factor to 1.0 and outputs <code>0.0</code> for all samples, preventing runtime crashes.
      </p>
    </div>

    <h3>Runnable Scikit-Learn Implementation</h3>
    <div class="code-block">
      <div class="code-header">
        <span class="code-title">python_minmax_scaler.py</span>
        <span class="code-lang">python</span>
      </div>
      <pre><code>import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 1. Training feature array (must be 2D matrix of shape [n_samples, n_features])
X_train = np.array([[10.0], [20.0], [30.0]])

# 2. Instantiate and fit scaler
scaler = MinMaxScaler(feature_range=(0, 1))
X_train_scaled = scaler.fit_transform(X_train)

print("Fitted Training Minimum:", scaler.data_min_)   # Output: [10.]
print("Fitted Training Maximum:", scaler.data_max_)   # Output: [30.]
print("Scaled Training Array:\n", X_train_scaled.flatten())
# Output: [0.  0.5 1. ]

# 3. Transform unseen test data using training statistics
X_test = np.array([[5.0], [25.0], [40.0]])
X_test_scaled = scaler.transform(X_test)
print("Scaled Test Array:\n", X_test_scaled.flatten())
# Output: [-0.25  0.75  1.5 ] (Demonstrates values outside [0, 1]!)</code></pre>
    </div>
  </section>
"""
