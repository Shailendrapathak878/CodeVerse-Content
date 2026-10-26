"""
Module: topic11_part1.py
Contains Hero Header, Table of Contents, and Sections 1 to 5 for Topic 11: K-Nearest Neighbors (KNN).
"""

from scratch.topic11_svgs import (
    SVG_KNN_HERO,
    SVG_KNN_PREDICTION_FLOWCHART,
    SVG_KNN_QUERY_NEIGHBORS,
    SVG_KNN_K_COMPARISON,
    SVG_EUCLIDEAN_VS_MANHATTAN
)

PART1_HTML = f"""
    <!-- HERO HEADER -->
    <header class="hero-card">
      <div class="hero-tag">&#9874; Supervised Machine Learning &bull; Topic 11</div>
      <h1 class="hero-title">K-Nearest Neighbors (KNN): Complete Beginner Guide</h1>
      <p class="hero-subtitle">
        Master instance-based machine learning from absolute zero. Learn how the intuitive principle of geometric proximity powers both classification and regression, how distance metrics dictate neighborhood boundaries, how feature scaling prevents dimensional distortion, and how to build leak-free scikit-learn KNN pipelines with rigorous cross-validation.
      </p>
      <div class="meta-bar">
        <span class="meta-pill">&#128218; 21 Comprehensive Sections</span>
        <span class="meta-pill">&#9889; 14 Interactive Vector Diagrams</span>
        <span class="meta-pill">&#128013; Verified Scikit-Learn Pipelines</span>
        <span class="meta-pill">&#9878; Strict Light Mode Only</span>
        <span class="meta-pill">&#127919; 100% Mobile &amp; Desktop Tested</span>
      </div>
    </header>

    <!-- ARCHITECTURE HERO SVG -->
    <div class="svg-card">
      <div class="svg-container">
        {SVG_KNN_HERO}
      </div>
      <div class="svg-caption">
        <strong>Figure 11.1: The K-Nearest Neighbors Instance-Based Paradigm.</strong> Unlike parametric models that compute mathematical weights (&beta;) during training, KNN simply memorizes training examples. When an unknown query <code>q</code> arrives, it computes distances across all <code>N</code> points, extracts the <code>K</code> nearest neighbors, and outputs their majority class or average value.
      </div>
      <div class="svg-takeaway">
        &#10004; Core takeaway: KNN is a <strong>lazy learner</strong>: training takes zero compute (O(1)), but prediction requires computing distances to every training example (O(N &times; d)).
      </div>
    </div>

    <!-- TABLE OF CONTENTS -->
    <nav class="toc-card" aria-label="Table of Contents">
      <div class="toc-title">
        <span>&#128203; Chapter Roadmap &bull; Table of Contents</span>
      </div>
      <div class="toc-grid">
        <a href="#sec-01" class="toc-link"><span class="toc-num">01</span> Introduction to KNN</a>
        <a href="#sec-02" class="toc-link"><span class="toc-num">02</span> How KNN Works (7 Steps)</a>
        <a href="#sec-03" class="toc-link"><span class="toc-num">03</span> Classification vs. Regression</a>
        <a href="#sec-04" class="toc-link"><span class="toc-num">04</span> Understanding the Value of K</a>
        <a href="#sec-05" class="toc-link"><span class="toc-num">05</span> Distance Measures (Euclidean &amp; Manhattan)</a>
        <a href="#sec-06" class="toc-link"><span class="toc-num">06</span> Complete Manual Worked Example</a>
        <a href="#sec-07" class="toc-link"><span class="toc-num">07</span> Majority vs. Distance-Weighted Voting</a>
        <a href="#sec-08" class="toc-link"><span class="toc-num">08</span> The Mandatory Role of Feature Scaling</a>
        <a href="#sec-09" class="toc-link"><span class="toc-num">09</span> KNN Decision Boundaries Across K</a>
        <a href="#sec-10" class="toc-link"><span class="toc-num">10</span> Underfitting &amp; Overfitting in KNN</a>
        <a href="#sec-11" class="toc-link"><span class="toc-num">11</span> Selecting the Best K via Validation</a>
        <a href="#sec-12" class="toc-link"><span class="toc-num">12</span> Scikit-Learn Hyperparameters</a>
        <a href="#sec-13" class="toc-link"><span class="toc-num">13</span> Complete Python Classification Lab</a>
        <a href="#sec-14" class="toc-link"><span class="toc-num">14</span> KNN Regression Practical Lab</a>
        <a href="#sec-15" class="toc-link"><span class="toc-num">15</span> Classification Evaluation Metrics</a>
        <a href="#sec-16" class="toc-link"><span class="toc-num">16</span> Advantages &amp; Curse of Dimensionality</a>
        <a href="#sec-17" class="toc-link"><span class="toc-num">17</span> KNN Compared With Other Algorithms</a>
        <a href="#sec-18" class="toc-link"><span class="toc-num">18</span> Real-World Case Studies</a>
        <a href="#sec-19" class="toc-link"><span class="toc-num">19</span> Key Visualizations &amp; Graphic Gallery</a>
        <a href="#sec-20" class="toc-link"><span class="toc-num">20</span> 15 Common Beginner Mistakes</a>
        <a href="#sec-21" class="toc-link"><span class="toc-num">21</span> Glossary, Checklist &amp; Revision</a>
      </div>
    </nav>

    <!-- SECTION 01: INTRODUCTION TO KNN -->
    <section id="sec-01" class="section-card">
      <span class="section-badge">Section 01</span>
      <h2 class="section-title">Introduction to K-Nearest Neighbors (KNN)</h2>
      <p class="section-lead">
        Imagine you visit an unfamiliar fruit market and encounter an exotic, unlabeled piece of fruit. You don&rsquo;t know its biological classification, but you take a small bite and note its measurable physical characteristics: it is moderately sweet (sweetness score: 6 out of 10) and remarkably crisp (crispness score: 7 out of 10).
      </p>

      <p>
        How would your mind naturally deduce what kind of fruit it is? You would intuitively compare it to fruits you have previously tasted:
      </p>
      <ul>
        <li>You recall that apples are consistently crisp and moderately sweet.</li>
        <li>You recall that oranges are juicy and sweet, but soft and not crisp.</li>
        <li>You identify the <em>closest fruits in memory</em> that match these two features and conclude: <em>&ldquo;Because its closest neighbors are apples, this fruit is almost certainly an apple!&rdquo;</em></li>
      </ul>

      <p>
        This universal human intuition forms the foundation of <strong>K-Nearest Neighbors (KNN)</strong>: <em>&ldquo;Show me your closest neighbors, and I will tell you who you are.&rdquo;</em>
      </p>

      <div class="callout card-definition">
        <div class="callout-title">&#128214; Foundational Vocabulary: Terms Defined Before Use</div>
        <p>Before examining equations, let us define the key terminology:</p>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Term</th>
              <th>Plain-English Definition</th>
              <th>Concrete Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Data Point (Sample)</strong></td>
              <td>A single recorded observation or entity within a dataset.</td>
              <td>A single fruit tested in the market.</td>
            </tr>
            <tr>
              <td><strong>Feature (X)</strong></td>
              <td>A measurable attribute or numeric variable describing the sample.</td>
              <td>Sweetness score (<code>x<sub>1</sub> = 6.0</code>), Crispness score (<code>x<sub>2</sub> = 7.0</code>).</td>
            </tr>
            <tr>
              <td><strong>Label / Target (y)</strong></td>
              <td>The known ground-truth outcome or category of a sample.</td>
              <td>Category: <code>Apple (0)</code> vs. <code>Orange (1)</code>.</td>
            </tr>
            <tr>
              <td><strong>Neighbor</strong></td>
              <td>A known training observation that lies close to a query point in feature space.</td>
              <td>A known Honeycrisp apple located nearby at coordinates (6, 7).</td>
            </tr>
            <tr>
              <td><strong>Distance (d)</strong></td>
              <td>A mathematical metric measuring geometric separation between two coordinate vectors.</td>
              <td>Straight-line Euclidean distance: <code>d = 1.0</code>.</td>
            </tr>
            <tr>
              <td><strong>Classification</strong></td>
              <td>Predicting a discrete qualitative category or label.</td>
              <td>Determining if a fruit is an Apple or an Orange.</td>
            </tr>
            <tr>
              <td><strong>Regression</strong></td>
              <td>Predicting a continuous numerical quantity.</td>
              <td>Predicting the price per pound of the fruit ($2.45/lb).</td>
            </tr>
            <tr>
              <td><strong>Supervised Learning</strong></td>
              <td>A machine learning approach where algorithms learn from labeled input-output pairs.</td>
              <td>Training on historical fruits with verified human-labeled categories.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">The Central Intuition and Key Caveats</h3>
      <p>
        The central premise of KNN is simple: <strong>nearby data points in feature space tend to share similar properties and outcomes</strong>.
      </p>
      <div class="callout card-warning">
        <div class="callout-title">&#9888; Critical Beginner Caveat: The Meaning of &ldquo;Nearby&rdquo;</div>
        <p>
          The validity of &ldquo;nearby&rdquo; is not absolute! It depends heavily on:
        </p>
        <ul>
          <li><strong>Feature Quality:</strong> If you include irrelevant features (e.g., the day of the week the fruit was picked), it adds random distance noise.</li>
          <li><strong>Feature Scaling:</strong> If one feature is measured in grams (e.g., 200g) and another in pH (e.g., 3.5), the larger scale will dominate the distance calculation completely unless standardized.</li>
          <li><strong>Distance Metric:</strong> Euclidean vs. Manhattan distance can reorder neighbor rankings.</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 02: HOW KNN WORKS -->
    <section id="sec-02" class="section-card">
      <span class="section-badge">Section 02</span>
      <h2 class="section-title">How KNN Works (The 7-Step Prediction Process)</h2>
      <p class="section-lead">
        KNN is an <strong>instance-based, non-parametric</strong> algorithm. It does not construct an explicit internal mathematical equation during training. Instead, all computation happens on demand when a prediction is requested.
      </p>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_KNN_PREDICTION_FLOWCHART}
        </div>
        <div class="svg-caption">
          <strong>Figure 11.2: The 7-Step KNN Prediction Execution Pipeline.</strong> From initial dataset memorization to local distance calculation, sorting, neighborhood extraction, and aggregation.
        </div>
        <div class="svg-takeaway">
          &#10004; Architectural Rule: KNN skips the training phase entirely, deferring all computational burden to query time.
        </div>
      </div>

      <h3 class="sub-title">Step-by-Step Prediction Workflow</h3>
      <div class="step-list">
        <div class="step-card">
          <div class="step-number">1</div>
          <div class="step-body">
            <h4>Store Labelled Training Data</h4>
            <p>Load and store the <code>N</code> training feature vectors <code>X</code> and corresponding targets <code>y</code> in memory.</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">2</div>
          <div class="step-body">
            <h4>Select the Value of K</h4>
            <p>Determine hyperparameter <code>K</code> (the number of nearest neighbors to consult, e.g., <code>K = 3</code> or <code>K = 5</code>).</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">3</div>
          <div class="step-body">
            <h4>Receive an Unlabelled Query Point (q)</h4>
            <p>A new observation arrives with feature coordinates <code>(q<sub>1</sub>, q<sub>2</sub>, ..., q<sub>p</sub>)</code> but an unknown target.</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">4</div>
          <div class="step-body">
            <h4>Calculate Distances to All Training Points</h4>
            <p>Compute the geometric distance between query <code>q</code> and every single point <code>x<sub>i</sub></code> in the training set.</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">5</div>
          <div class="step-body">
            <h4>Sort Distances and Identify Top-K Nearest Neighbors</h4>
            <p>Sort all <code>N</code> calculated distances in ascending order and select the <code>K</code> points with the smallest distances.</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">6</div>
          <div class="step-body">
            <h4>Gather Neighbor Labels or Numerical Values</h4>
            <p>Retrieve the ground-truth targets <code>{{y<sub>1</sub>, y<sub>2</sub>, ..., y<sub>K</sub>}}</code> corresponding to the chosen <code>K</code> neighbors.</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">7</div>
          <div class="step-body">
            <h4>Aggregate and Output Prediction</h4>
            <p>
              <strong>For Classification:</strong> Take the majority vote (statistical mode) among the <code>K</code> neighbor classes.<br>
              <strong>For Regression:</strong> Compute the arithmetic mean (average) of the <code>K</code> neighbor values.
            </p>
          </div>
        </div>
      </div>

      <h3 class="sub-title">Why Is KNN Called a &ldquo;Lazy Learner&rdquo;?</h3>
      <p>
        In machine learning, algorithms are broadly split into <strong>eager learners</strong> and <strong>lazy learners</strong>:
      </p>
      <ul>
        <li>
          <strong>Eager Learners (e.g., Linear Regression, Logistic Regression, Neural Networks):</strong> Spend significant time and compute during training to compress data into a compact set of model parameters (coefficients &beta; or weights). Once trained, the training dataset can be discarded, and predictions are evaluated in microseconds.
        </li>
        <li>
          <strong>Lazy Learners (e.g., KNN):</strong> Spend <em>zero time</em> learning parameters during training (training time is <code>O(1)</code>). However, because no model was built, the algorithm must retain the complete training dataset in RAM. At query time, it must compare the query point against every stored sample, requiring <code>O(N &times; d)</code> operations per prediction.
        </li>
      </ul>

      <div class="callout card-concept">
        <div class="callout-title">&#128269; KNN vs. K-Means: Do Not Confuse Them!</div>
        <p>
          Beginners frequently mix up <strong>KNN</strong> and <strong>K-Means</strong> because both share the letter &ldquo;K&rdquo;:
        </p>
        <ul>
          <li><strong>KNN (K-Nearest Neighbors):</strong> A <strong>Supervised</strong> algorithm used for classification and regression where <code>K</code> represents the count of nearest training neighbors consulted.</li>
          <li><strong>K-Means:</strong> An <strong>Unsupervised</strong> clustering algorithm used to group unlabelled data into <code>K</code> clusters where <code>K</code> represents the number of centroids.</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 03: CLASSIFICATION VS REGRESSION -->
    <section id="sec-03" class="section-card">
      <span class="section-badge">Section 03</span>
      <h2 class="section-title">Classification and Regression with KNN</h2>
      <p class="section-lead">
        A major strength of KNN is its dual versatility: with slight modification to the final aggregation step, the exact same neighborhood search solves both <strong>Classification</strong> and <strong>Regression</strong> problems.
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Task Dimension</th>
              <th>KNN Classification</th>
              <th>KNN Regression</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Target Type (y)</strong></td>
              <td>Discrete qualitative class / category</td>
              <td>Continuous real numerical measurement</td>
            </tr>
            <tr>
              <td><strong>Aggregation Rule</strong></td>
              <td><strong>Majority Vote (Mode):</strong> Most frequent class label among the K neighbors.</td>
              <td><strong>Arithmetic Average (Mean):</strong> Numerical average of neighbor target values.</td>
            </tr>
            <tr>
              <td><strong>Primary Metric</strong></td>
              <td>Accuracy, Precision, Recall, F1-Score</td>
              <td>Mean Absolute Error (MAE), Root Mean Squared Error (RMSE)</td>
            </tr>
            <tr>
              <td><strong>Concrete Example</strong></td>
              <td>Predicting whether a fruit is an Apple or an Orange based on sweetness and crispness.</td>
              <td>Predicting home selling price ($325,000) based on square footage and neighborhood.</td>
            </tr>
            <tr>
              <td><strong>Tie-Breaking</strong></td>
              <td>Break ties randomly, pick nearest neighbor, or use distance weighting.</td>
              <td>No ties: numerical mean always produces a single continuous average.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">Mathematical Formulations</h3>
      <div class="formula-card">
        <div class="formula-title">&#128290; KNN Classification Decision Rule</div>
        <div class="formula-math">
          &#375; = mode(y<sub>(1)</sub>, y<sub>(2)</sub>, ..., y<sub>(K)</sub>) = argmax<sub>c &isin; C</sub> &sum;<sub>i=1</sub><sup>K</sup> I(y<sub>(i)</sub> = c)
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          Where <code>I(&bull;)</code> is an indicator function returning 1 if neighbor <code>i</code> belongs to class <code>c</code>, and 0 otherwise.
        </p>
      </div>

      <div class="formula-card">
        <div class="formula-title">&#128290; KNN Regression Prediction Formula</div>
        <div class="formula-math">
          &#375; = (1 / K) &sum;<sub>i=1</sub><sup>K</sup> y<sub>(i)</sub>
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          Where <code>y<sub>(i)</sub></code> represents the continuous numerical target value of the <code>i</code>-th nearest neighbor.
        </p>
      </div>
    </section>

    <!-- SECTION 04: UNDERSTANDING THE VALUE OF K -->
    <section id="sec-04" class="section-card">
      <span class="section-badge">Section 04</span>
      <h2 class="section-title">Understanding the Value of K</h2>
      <p class="section-lead">
        The parameter <strong>K</strong> is the central hyperparameter of the algorithm. It controls the size of the neighborhood around the query point and governs the fundamental trade-off between model flexibility and noise resilience.
      </p>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_KNN_QUERY_NEIGHBORS}
        </div>
        <div class="svg-caption">
          <strong>Figure 11.3: Expanding Neighborhood Radii Around Query Q(5, 5).</strong> The innermost circle (blue dashed) captures <code>K = 1</code> (only T2). The middle circle (sky blue dashed) captures <code>K = 3</code> (T2, T1, T3). The outer circle (green dashed) captures <code>K = 5</code>.
        </div>
        <div class="svg-takeaway">
          &#10004; Key Insight: As K increases, the boundary expands outward, incorporating more surrounding consensus while dampening localized noise.
        </div>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_KNN_K_COMPARISON}
        </div>
        <div class="svg-caption">
          <strong>Figure 11.4: Decision Shift Across K = 1, K = 3, and K = 5.</strong> In this dataset, Apple wins consistently across all three neighborhoods, but notice how the vote distribution shifts from unanimous (1-0) to 2-1 and 3-2.
        </div>
      </div>

      <h3 class="sub-title">The Fundamental Trade-Offs of Selecting K</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Choice of K</th>
              <th>Model Flexibility</th>
              <th>Sensitivity to Noise</th>
              <th>Variance vs. Bias</th>
              <th>Risk</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Small K (e.g., K = 1)</strong></td>
              <td>Extremely High</td>
              <td>Extreme (1 outlier flips prediction)</td>
              <td><strong>High Variance, Low Bias</strong></td>
              <td><strong>Overfitting:</strong> Memorizes noisy boundaries and outliers.</td>
            </tr>
            <tr>
              <td><strong>Moderate K (e.g., K = 3 to 7)</strong></td>
              <td>Balanced</td>
              <td>Robust to single mislabeled points</td>
              <td><strong>Balanced Equilibrium</strong></td>
              <td>Optimal sweet spot for clean generalization.</td>
            </tr>
            <tr>
              <td><strong>Excessive K (e.g., K &rarr; N)</strong></td>
              <td>Extremely Low (Rigid)</td>
              <td>Immune to local variations</td>
              <td><strong>Low Variance, High Bias</strong></td>
              <td><strong>Underfitting:</strong> Simply predicts the global majority class.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">Handling Ties and the Myth of Odd K</h3>
      <p>
        In binary classification (2 classes), choosing an <strong>odd value of K</strong> (e.g., K = 3, 5, 7) guarantees that a tie vote is mathematically impossible: there is no way to divide 5 votes evenly between two classes!
      </p>
      <div class="callout card-warning">
        <div class="callout-title">&#9888; Critical Beginner Myth: Odd K Does NOT Prevent Ties in Multi-Class Tasks!</div>
        <p>
          If you have <strong>three classes</strong> (e.g., Apple, Orange, Banana) and set <code>K = 5</code>:
          <br>
          Votes can easily split as: <strong>2 Apples, 2 Oranges, 1 Banana</strong>.
          <br>
          Even though K is odd, a 2-2 tie occurs! In such cases, software libraries break ties by selecting the class whose nearest neighbor is closest, or by falling back to distance-weighted voting.
        </p>
      </div>
    </section>

    <!-- SECTION 05: DISTANCE MEASURES -->
    <section id="sec-05" class="section-card">
      <span class="section-badge">Section 05</span>
      <h2 class="section-title">Distance Measures: Euclidean, Manhattan and Minkowski</h2>
      <p class="section-lead">
        To determine which training points are &ldquo;nearest&rdquo;, KNN requires a mathematical distance function. Let us explore the two most fundamental geometric distance measures.
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; 1. Euclidean Distance (L2 Norm &bull; Straight Line)</div>
        <div class="formula-math">
          d(x, y) = &radic;(&sum;<sub>j=1</sub><sup>p</sup> (x<sub>j</sub> - y<sub>j</sub>)&sup2;)
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          In two dimensions (p = 2): <code>d = &radic;((x<sub>1</sub> - y<sub>1</sub>)&sup2; + (x<sub>2</sub> - y<sub>2</sub>)&sup2;)</code>
        </p>
      </div>

      <div class="formula-card">
        <div class="formula-title">&#128290; 2. Manhattan Distance (L1 Norm &bull; City Block / Taxicab)</div>
        <div class="formula-math">
          d(x, y) = &sum;<sub>j=1</sub><sup>p</sup> |x<sub>j</sub> - y<sub>j</sub>|
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          In two dimensions (p = 2): <code>d = |x<sub>1</sub> - y<sub>1</sub>| + |x<sub>2</sub> - y<sub>2</sub>|</code>
        </p>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_EUCLIDEAN_VS_MANHATTAN}
        </div>
        <div class="svg-caption">
          <strong>Figure 11.5: Euclidean vs. Manhattan Distance Between Point A(2, 3) and Point B(6, 6).</strong> Euclidean distance (solid purple line) takes the direct diagonal hypotenuse (5.0). Manhattan distance (dashed amber path) follows axis-aligned city-block grid steps (4 + 3 = 7.0).
        </div>
        <div class="svg-takeaway">
          &#10004; Geometric Rule: Manhattan distance is always greater than or equal to Euclidean distance: <code>d<sub>Manhattan</sub> &ge; d<sub>Euclidean</sub></code>.
        </div>
      </div>

      <h3 class="sub-title">Step-by-Step Calculation Walkthrough (Python Verified)</h3>
      <p>
        Let us calculate both distances between <strong>Point A(2, 3)</strong> and <strong>Point B(6, 6)</strong>:
      </p>

      <div class="step-list">
        <div class="step-card">
          <div class="step-number">1</div>
          <div class="step-body">
            <h4>Calculate Coordinate Differences</h4>
            <p>
              <code>&Delta;x<sub>1</sub> = 6 - 2 = 4</code><br>
              <code>&Delta;x<sub>2</sub> = 6 - 3 = 3</code>
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">2</div>
          <div class="step-body">
            <h4>Compute Euclidean Distance (L2)</h4>
            <p>
              <code>d<sub>Euc</sub> = &radic;(4&sup2; + 3&sup2;) = &radic;(16 + 9) = &radic;25 = <strong>5.0000</strong></code>
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">3</div>
          <div class="step-body">
            <h4>Compute Manhattan Distance (L1)</h4>
            <p>
              <code>d<sub>Man</sub> = |4| + |3| = 4 + 3 = <strong>7.0000</strong></code>
            </p>
          </div>
        </div>
      </div>

      <h3 class="sub-title">3. Minkowski Distance: The Mathematical Generalization</h3>
      <p>
        Both Euclidean and Manhattan distances are specific instances of the generalized <strong>Minkowski Distance</strong>:
      </p>
      <div class="formula-card">
        <div class="formula-title">&#128290; Minkowski Distance Formula</div>
        <div class="formula-math">
          d(x, y) = (&sum;<sub>j=1</sub><sup>p</sup> |x<sub>j</sub> - y<sub>j</sub>|<sup>p</sup>)<sup>1/p</sup>
        </div>
        <div class="formula-legend">
          <div class="formula-legend-item"><code>p = 1</code>: Exactly equivalent to Manhattan distance.</div>
          <div class="formula-legend-item"><code>p = 2</code>: Exactly equivalent to Euclidean distance (scikit-learn default).</div>
          <div class="formula-legend-item"><code>p &rarr; &infin;</code>: Chebyshev distance (maximum coordinate difference).</div>
        </div>
      </div>
      <p>
        For our example points with <code>p = 3</code>:
        <br>
        <code>d<sub>Mink</sub> = (|4|<sup>3</sup> + |3|<sup>3</sup>)<sup>1/3</sup> = (64 + 27)<sup>1/3</sup> = 91<sup>1/3</sup> &approx; <strong>4.4979</strong></code> (Verified with Python).
      </p>
    </section>
"""
