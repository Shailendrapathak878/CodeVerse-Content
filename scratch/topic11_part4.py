"""
Module: topic11_part4.py
Contains Sections 16 to 21 for Topic 11: K-Nearest Neighbors (KNN).
"""

from scratch.topic11_svgs import (
    SVG_CURSE_OF_DIMENSIONALITY
)

PART4_HTML = f"""
    <!-- SECTION 16: ADVANTAGES, LIMITATIONS AND COMPUTATIONAL COST -->
    <section id="sec-16" class="section-card">
      <span class="section-badge">Section 16</span>
      <h2 class="section-title">Advantages, Limitations and Computational Cost</h2>
      <p class="section-lead">
        K-Nearest Neighbors is delightfully simple, highly intuitive, and remarkably flexible. However, its simplicity conceals significant computational costs and severe vulnerabilities in high-dimensional feature spaces.
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th style="width: 50%;">Major Advantages</th>
              <th style="width: 50%;">Practical Limitations</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <ul style="margin: 0; padding-left: 18px; line-height: 1.6;">
                  <li><strong>Zero Training Phase:</strong> As a lazy learner, training simply requires storing or indexing data (&Oscr;(1) or &Oscr;(N log N) tree build).</li>
                  <li><strong>Nonlinear Flexibility:</strong> Makes no assumptions about linear separability. Naturally models intricate, curving boundaries.</li>
                  <li><strong>Dual Capability:</strong> Handles both classification (voting) and regression (local averaging) seamlessly.</li>
                  <li><strong>High Local Interpretability:</strong> You can show stakeholders exactly which training examples caused the prediction.</li>
                  <li><strong>Naturally Multiclass:</strong> No complex one-vs-rest workarounds needed; votes accumulate across any number of classes.</li>
                </ul>
              </td>
              <td>
                <ul style="margin: 0; padding-left: 18px; line-height: 1.6;">
                  <li><strong>Expensive Query Latency:</strong> Scoring an unknown query requires distance checks across N stored training points (&Oscr;(N &times; D)).</li>
                  <li><strong>Substantial RAM Consumption:</strong> The complete training dataset must reside in memory for real-time inference.</li>
                  <li><strong>Scale Sensitivity:</strong> Unscaled features with large numerical magnitudes completely distort neighbor rankings.</li>
                  <li><strong>Irrelevant Feature Distortion:</strong> Noise features widen Euclidean distance, washing out informative patterns.</li>
                  <li><strong>Curse of Dimensionality:</strong> Distance contrast vanishes exponentially in high dimensions.</li>
                </ul>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">1. The Computational Cost of Lazy Learning</h3>
      <p>
        Beginners often think that because KNN is a "lazy learner" with no gradient descent or backpropagation, it is computationally cheap. In truth, <strong>KNN simply shifts the computational burden from training time to inference time</strong>!
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Operation</th>
              <th>Brute-Force KNN</th>
              <th>KD-Tree / Ball-Tree (Low D &le; 20)</th>
              <th>Traditional Eager Model (e.g. Logistic Regression)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Training Time</strong></td>
              <td>&Oscr;(1) — Instantaneous storage</td>
              <td>&Oscr;(D &times; N log N) — Spatial tree construction</td>
              <td>&Oscr;(Iterations &times; N &times; D) — Gradient descent optimization</td>
            </tr>
            <tr>
              <td><strong>Query Time (per sample)</strong></td>
              <td>&Oscr;(N &times; D) — Evaluates all distances</td>
              <td>&Oscr;(D &times; log N) — Traverses spatial branches</td>
              <td>&Oscr;(D) — Single dot product (w<sup>T</sup>x + b) &rarr; Sub-millisecond!</td>
            </tr>
            <tr>
              <td><strong>Memory Footprint</strong></td>
              <td>&Oscr;(N &times; D) — Stored training matrix</td>
              <td>&Oscr;(N &times; D) + tree pointers</td>
              <td>&Oscr;(D) — Only weights and bias vector!</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>
        If your company serves 10,000 real-time API requests per second against a historical database of 1,000,000 users, brute-force KNN requires calculating <strong>10 billion distance operations every second</strong>! In contrast, a trained linear model requires only a single vector multiplication per request.
      </p>

      <h3 class="sub-title">2. The Curse of Dimensionality</h3>
      <p>
        As the number of features (dimensions, D) increases, the volume of the feature space expands exponentially. Data points become isolated in vast empty space, and the ratio between the distance to the nearest neighbor and the distance to the farthest neighbor approaches 1!
      </p>

      {SVG_CURSE_OF_DIMENSIONALITY}

      <div class="callout callout-info">
        <div class="callout-title">Geometric Intuition: The Empty Space Phenomenon</div>
        <p>
          In 1D (a line segment of length 10), 10 points spaced 1 unit apart provide dense coverage. In 2D (a 10&times;10 square), you need 100 points for the same density. In 10D, you need 10<sup>10</sup> = 10,000,000,000 points! Without trillions of data points, high-dimensional spaces are virtually empty, making the very concept of "nearby neighbors" statistically meaningless.
        </p>
      </div>
    </section>

    <!-- SECTION 17: KNN COMPARED WITH OTHER ALGORITHMS -->
    <section id="sec-17" class="section-card">
      <span class="section-badge">Section 17</span>
      <h2 class="section-title">KNN Compared With Other Machine Learning Algorithms</h2>
      <p class="section-lead">
        To select the right algorithm for a project, you must understand how KNN compares against other fundamental classification and clustering techniques.
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Dimension</th>
              <th>K-Nearest Neighbors (KNN)</th>
              <th>Logistic Regression</th>
              <th>Decision Tree</th>
              <th>K-Means Clustering</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Learning Paradigm</strong></td>
              <td>Supervised (Instance-Based / Lazy)</td>
              <td>Supervised (Parametric / Eager)</td>
              <td>Supervised (Non-Parametric / Eager)</td>
              <td><strong>Unsupervised</strong> (Centroid-Based)</td>
            </tr>
            <tr>
              <td><strong>Target Labels Needed?</strong></td>
              <td>Yes (Labels required during voting)</td>
              <td>Yes (Labels train weights)</td>
              <td>Yes (Labels compute split purity)</td>
              <td><strong>No (Discovers hidden clusters in unlabelled data)</strong></td>
            </tr>
            <tr>
              <td><strong>Decision Boundary Shape</strong></td>
              <td>Arbitrary nonlinear, locally adaptive</td>
              <td>Strictly linear (hyperplane)</td>
              <td>Axis-aligned orthogonal rectangles</td>
              <td>Voronoi convex polyhedral cells</td>
            </tr>
            <tr>
              <td><strong>Interpretability</strong></td>
              <td>High local (inspect closest points)</td>
              <td>High global (feature weights / odds)</td>
              <td>High transparent (if-then flowchart)</td>
              <td>Moderate (cluster centroid coordinates)</td>
            </tr>
            <tr>
              <td><strong>Inference Speed</strong></td>
              <td>Slow (&Oscr;(N &times; D))</td>
              <td>Ultra-Fast (&Oscr;(D))</td>
              <td>Fast (&Oscr;(Tree Depth))</td>
              <td>Fast (&Oscr;(K &times; D) vs centroids)</td>
            </tr>
            <tr>
              <td><strong>Scale Sensitivity</strong></td>
              <td><strong>Extreme</strong> (Scaling mandatory)</td>
              <td>High when regularized (L1/L2)</td>
              <td><strong>Zero</strong> (Invariant to scaling)</td>
              <td><strong>Extreme</strong> (Euclidean to centroids)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-warning">
        <div class="callout-title">Critical Distinction: KNN vs. K-Means</div>
        <p>
          Never confuse <strong>KNN</strong> with <strong>K-Means</strong> in an interview or technical discussion! 
          <strong>KNN</strong> is a <em>supervised classification and regression algorithm</em> that predicts known target labels by consulting nearby training examples. 
          <strong>K-Means</strong> is an <em>unsupervised clustering algorithm</em> that groups unlabelled observations into K distinct clusters by iteratively updating geometric cluster centers.
        </p>
      </div>
    </section>

    <!-- SECTION 18: REAL-WORLD CASE STUDIES -->
    <section id="sec-18" class="section-card">
      <span class="section-badge">Section 18</span>
      <h2 class="section-title">Real-World Case Studies</h2>
      <p class="section-lead">
        To understand where KNN shines and where it encounters roadblocks in industry, examine four diverse educational case studies across agriculture, education, healthcare, and retail.
      </p>

      <div class="grid-2col">
        <div class="calc-box">
          <h4 style="margin: 0 0 10px 0; color: #0284C7; font-size: 1.1rem;">Case 1: Automated Fruit Sorting on a Conveyor</h4>
          <p style="font-size: 0.92rem; line-height: 1.6; color: #334155;">
            <strong>Features:</strong> Surface Sweetness (Brix sensor), Firmness (penetrometer), Weight (grams).<br>
            <strong>Target:</strong> Fruit Category (Apple vs. Orange vs. Peach).<br>
            <strong>Workflow:</strong> Optical and physical sensors capture measurements as fruit passes on a conveyor belt. KNN with K = 5 and StandardScaler classifies fruit into distribution crates.<br>
            <strong>Key Metrics:</strong> Precision (avoid mixing sour apples into premium sweet crates) and low latency (&lt; 20 ms).<br>
            <strong>Limitation:</strong> If the sensor lens gets dirty, sensor drift adds noise, misranking neighbors.
          </p>
        </div>

        <div class="calc-box">
          <h4 style="margin: 0 0 10px 0; color: #0284C7; font-size: 1.1rem;">Case 2: Early Warning Academic Intervention</h4>
          <p style="font-size: 0.92rem; line-height: 1.6; color: #334155;">
            <strong>Features:</strong> Weekly Lecture Attendance %, Homework Submission %, Midterm Exam Score.<br>
            <strong>Target:</strong> Academic Outcome (Pass vs. Needs Remedial Mentorship).<br>
            <strong>Workflow:</strong> Instructors run student records through a KNN model trained on previous semesters to flag struggling students by Week 4.<br>
            <strong>Key Metrics:</strong> <strong>Recall</strong> is paramount: failing to identify an at-risk student (False Negative) prevents timely tutoring.<br>
            <strong>Limitation:</strong> Historical grading shifts or curriculum updates can make past training cohorts unrepresentative.
          </p>
        </div>

        <div class="calc-box">
          <h4 style="margin: 0 0 10px 0; color: #0284C7; font-size: 1.1rem;">Case 3: Hypothetical Diabetes Screening Risk</h4>
          <p style="font-size: 0.92rem; line-height: 1.6; color: #334155;">
            <strong>Features:</strong> Fasting Blood Glucose (mg/dL), Body Mass Index (BMI), Age, Systolic BP.<br>
            <strong>Target:</strong> Screening Risk Category (High Risk vs. Low Risk).<br>
            <strong>Workflow:</strong> Clinic intake kiosk flags potential high-risk patients for priority lab tests.<br>
            <strong>Key Metrics:</strong> High Recall (&gt; 95%) and strict zero-leakage training.<br>
            <strong>Limitation &amp; Disclaimer:</strong> <em>Educational models are not certified clinical diagnostic tools and must never replace qualified medical judgment by licensed physicians.</em>
          </p>
        </div>

        <div class="calc-box">
          <h4 style="margin: 0 0 10px 0; color: #0284C7; font-size: 1.1rem;">Case 4: E-Commerce Customer Loyalty Tiers</h4>
          <p style="font-size: 0.92rem; line-height: 1.6; color: #334155;">
            <strong>Features:</strong> Purchase Frequency (orders/year), Average Order Value ($), Days Since Last Visit.<br>
            <strong>Target:</strong> VIP Loyalty Tier (Bronze, Silver, Gold).<br>
            <strong>Workflow:</strong> Distance-weighted KNN assigns new customers to tiers based on behavioral proximity to established VIP profiles.<br>
            <strong>Key Metrics:</strong> F1-Score and distance-weighted stability.<br>
            <strong>Limitation:</strong> Extreme outliers (e.g., a single corporate bulk purchase of $50,000) can distort Euclidean distances without robust scaling or winsorization.
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 19: KEY VISUALIZATIONS AND GRAPHIC GALLERY -->
    <section id="sec-19" class="section-card">
      <span class="section-badge">Section 19</span>
      <h2 class="section-title">Required Graphics &amp; Visual Gallery</h2>
      <p class="section-lead">
        Visual intuition is the bedrock of machine learning mastery. Below is the complete catalogue of all 14 hand-crafted vector diagrams embedded throughout this chapter, along with their core architectural takeaways.
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Figure</th>
              <th>Diagram Name</th>
              <th>Core Educational Takeaway</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Fig 11.1</strong></td>
              <td>KNN Prediction Flowchart</td>
              <td>Visualizes the complete 7-step prediction pipeline from training storage to vote aggregation.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.2</strong></td>
              <td>Query Point with Nearest Neighbors</td>
              <td>Contrasts a local query point against concentric neighborhood radii in 2D space.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.3</strong></td>
              <td>Voting Comparison across K = 1, 3, 5</td>
              <td>Demonstrates how expanding the radius from K=1 to K=5 shifts majority vote tallies.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.4</strong></td>
              <td>Euclidean vs. Manhattan Distance Grid</td>
              <td>Contrasts straight-line diagonal Euclidean distance (5.00) with grid-bound Manhattan distance (7.00).</td>
            </tr>
            <tr>
              <td><strong>Fig 11.5</strong></td>
              <td>Manual Distance Ranking Chart</td>
              <td>Bar chart ordering all 6 training points by proximity to query point Q(5, 5).</td>
            </tr>
            <tr>
              <td><strong>Fig 11.6</strong></td>
              <td>Weighted vs. Unweighted Voting</td>
              <td>Proves how distance weighting (w = 1/d) can overturn an unweighted 2-to-1 majority vote.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.7</strong></td>
              <td>Feature Scaling Before and After</td>
              <td>Shows how unscaled salary ($50k) eclipses age (30), and how standardization restores balance.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.8</strong></td>
              <td>Fitted Decision Boundaries across K</td>
              <td>Shows K=1 creating noisy decision islands while K=15 produces smooth, generalized boundaries.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.9</strong></td>
              <td>Train vs. Validation Performance Across K</td>
              <td>Illustrates the classic U-shaped error curve and identifies optimal K without data leakage.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.10</strong></td>
              <td>Synthetic Dataset Class Distribution</td>
              <td>Displays the 200-sample balanced Gaussian clusters used in our Python Classification Lab.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.11</strong></td>
              <td>Confusion Matrix Heatmap</td>
              <td>Breakdown of holdout predictions: 20 TN, 0 FP, 1 FN, 19 TP, yielding 97.5% accuracy.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.12</strong></td>
              <td>KNN Regression Prediction Curve</td>
              <td>Contrasts K=1 noisy step functions with K=5 balanced fit and K=20 flat over-smoothing.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.13</strong></td>
              <td>Curse of Dimensionality</td>
              <td>Geometric visualization of exponential volume expansion and data sparsity across 1D, 2D, and 3D.</td>
            </tr>
            <tr>
              <td><strong>Fig 11.14</strong></td>
              <td>KNN Concept Architecture Hero</td>
              <td>High-level infographic encapsulating the core principles of instance-based machine learning.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 20: 15 COMMON BEGINNER MISTAKES -->
    <section id="sec-20" class="section-card">
      <span class="section-badge">Section 20</span>
      <h2 class="section-title">15 Common Beginner Mistakes and How to Avoid Them</h2>
      <p class="section-lead">
        Learn from the missteps of others. Review these 15 pervasive mistakes made by students and novice practitioners, along with their concrete solutions.
      </p>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 1: Confusing KNN with K-Means Clustering</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Using KNN when you have unlabelled data, or calling K-Means a classification algorithm.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> KNN is supervised classification/regression requiring ground-truth labels. K-Means is unsupervised clustering that groups unlabelled data into centroids.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 2: Believing K Represents the Number of Target Classes</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Setting K = 2 because you have two classes (e.g., Apple and Orange).</p>
        <p class="mistake-fix"><strong>The Fix:</strong> K is the count of neighboring points to consult. You can choose K = 7 for a 2-class problem, or K = 5 for a 10-class problem.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 3: Assuming K = 1 is Always Best Because Training Accuracy is 100%</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Observing 100% accuracy on training data with K=1 and assuming the model is flawless.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> With K=1, every training point is its own nearest neighbor (distance = 0), memorizing all noise and outlier errors. Always evaluate on unseen validation data.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 4: Tuning Hyperparameter K on the Test Set</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Testing K=1, 3, 5, 7 on the test set and reporting the best test accuracy.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> This is severe data leakage. Tune K using K-fold cross-validation strictly on the training set. Evaluate on the test set exactly once.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 5: Forgetting to Scale Numerical Features</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Running KNN directly on raw features like Age (18&ndash;80) and Annual Income ($20,000&ndash;$200,000).</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Income's large numerical spread will dominate Euclidean distance, rendering Age completely irrelevant. Always apply <code>StandardScaler</code> or <code>MinMaxScaler</code>.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 6: Fitting Feature Scalers Before Splitting Data</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Calling <code>scaler.fit_transform(X)</code> on the full dataset before calling <code>train_test_split</code>.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> The test set's mean and variance leak into the training features. Use a scikit-learn <code>Pipeline</code> so the scaler is fitted solely on training data.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 7: Miscalculating Distance Arithmetic</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Forgetting to take the square root in Euclidean distance, or omitting absolute values in Manhattan distance.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Euclidean distance is &radic;(&sum;(x<sub>i</sub> &minus; y<sub>i</sub>)<sup>2</sup>). Manhattan distance is &sum;|x<sub>i</sub> &minus; y<sub>i</sub>|.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 8: Confusing Distance-Weighted Voting with Simple Majority</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Counting raw votes when <code>weights='distance'</code> was configured, or vice versa.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Simple majority counts tally 1 vote per neighbor. Distance weighting sums 1/d<sub>i</sub> weights, giving much greater authority to immediate neighbors.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 9: Believing an Odd K Guarantees Zero Voting Ties</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Choosing K = 3 for a 3-class problem and assuming ties are mathematically impossible.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> If 3 classes each receive exactly 1 vote among the 3 neighbors (a 1-1-1 deadlock), an odd K still produces an unresolvable tie!</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 10: Relying Exclusively on Accuracy for Imbalanced Data</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Celebrating 95% accuracy when the dataset has a 95:5 class imbalance.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> A naive model predicting majority class achieves 95% accuracy while completely failing to detect the minority class. Inspect Precision, Recall, and F1-Score.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 11: Retaining Irrelevant Noise Features</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Feeding dozens of uninformative columns (e.g., User ID, Timestamp) into KNN.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Irrelevant features add random noise to Euclidean distance, pushing true informative neighbors farther apart. Apply feature selection or PCA before KNN.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 12: Ignoring the Curse of Dimensionality</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Deploying KNN directly on raw text TF-IDF matrices or image pixel arrays with 10,000 dimensions.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> In high dimensions, all pairwise distances converge to nearly identical values. Reduce dimensionality using PCA, UMAP, or autoencoders first.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 13: Assuming a "Lazy Learner" Has Zero Computational Cost</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Deploying brute-force KNN into a real-time, low-latency microservice with 5 million historical records.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Inference requires &Oscr;(N &times; D) calculations per request. Use KD-Trees, Ball-Trees, or approximate nearest neighbor libraries (such as FAISS or Annoy) for high-volume production.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 14: Confusing Classification Majority Voting with Regression Averaging</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Attempting to take the statistical mode of continuous floating-point numbers in regression.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Classification uses discrete mode (majority voting). Regression takes the continuous arithmetic mean: y_pred = (1/K) &sum; y<sub>i</sub>.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 15: Treating Synthetic Benchmark Success as Proof of Enterprise Readiness</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Expecting 98% accuracy on messy production logs because your synthetic Gaussian lab achieved 97.5%.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Real-world tabular data contains missing fields, covariate shift, concept drift, and multi-modal distributions. Validate rigorously on authentic production shadow traffic.</p>
      </div>
    </section>

    <!-- SECTION 21: SUMMARY, GLOSSARY AND REVISION -->
    <section id="sec-21" class="section-card">
      <span class="section-badge">Section 21</span>
      <h2 class="section-title">Summary, Comprehensive Glossary &amp; Interactive Revision</h2>
      <p class="section-lead">
        Consolidate everything you have mastered with our chapter summary, a 16-term technical glossary, and 12 interactive revision challenges complete with step-by-step arithmetic and Python solutions.
      </p>

      <h3 class="sub-title">1. Chapter Summary &amp; Deployment Checklist</h3>
      <div class="callout callout-info">
        <div class="callout-title">The KNN Production Deployment Checklist</div>
        <ul style="margin: 8px 0 0 20px; line-height: 1.7;">
          <li>&check; <strong>Supervised Objective:</strong> Verified that the problem is supervised (labels exist) and that target is discrete (Classifier) or continuous (Regressor).</li>
          <li>&check; <strong>Feature Preprocessing:</strong> Handled missing values, eliminated non-predictive IDs, and standardized numerical features via <code>StandardScaler</code>.</li>
          <li>&check; <strong>Leak-Free Pipeline:</strong> Wrapped scalers and KNN inside a <code>Pipeline</code> so preprocessing is fitted exclusively on training splits.</li>
          <li>&check; <strong>Hyperparameter Selection:</strong> Evaluated candidate K values using K-fold cross-validation on training data rather than peeking at the test set.</li>
          <li>&check; <strong>Distance Metric Selected:</strong> Configured appropriate distance metric (Euclidean for isotropic continuous space, Manhattan for grid/taxicab features).</li>
          <li>&check; <strong>Dimensionality Check:</strong> Confirmed feature count is manageable (D &le; 20) or applied dimensionality reduction (PCA) to avoid the Curse of Dimensionality.</li>
          <li>&check; <strong>Production Latency Budget:</strong> Benchmarked inference latency against SLA requirements to ensure &Oscr;(N &times; D) query cost is acceptable.</li>
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
              <td><strong>Data Point</strong></td>
              <td>A single discrete sample, instance, or observation represented as a feature vector in a multi-dimensional mathematical space.</td>
            </tr>
            <tr>
              <td><strong>Feature</strong></td>
              <td>An individual measurable property, attribute, or characteristic of an observed phenomenon (e.g., Sweetness, Weight, Income).</td>
            </tr>
            <tr>
              <td><strong>Label / Target</strong></td>
              <td>The true ground-truth outcome, category, or numerical value assigned to a data point that a supervised model seeks to predict.</td>
            </tr>
            <tr>
              <td><strong>Neighbor</strong></td>
              <td>A stored training data point whose geometric distance to an unknown query point is among the smallest in the dataset.</td>
            </tr>
            <tr>
              <td><strong>Distance Metric</strong></td>
              <td>A formal mathematical function d(x, y) satisfying non-negativity, identity of indiscernibles, symmetry, and triangle inequality.</td>
            </tr>
            <tr>
              <td><strong>Euclidean Distance</strong></td>
              <td>The straight-line geometric distance between two vectors: &radic;(&sum;(x<sub>j</sub> &minus; y<sub>j</sub>)<sup>2</sup>), equivalent to the L2 norm.</td>
            </tr>
            <tr>
              <td><strong>Manhattan Distance</strong></td>
              <td>The rectilinear, grid-aligned distance: &sum;|x<sub>j</sub> &minus; y<sub>j</sub>|, equivalent to the L1 norm or taxicab metric.</td>
            </tr>
            <tr>
              <td><strong>Minkowski Distance</strong></td>
              <td>The generalized Lp metric: (&sum;|x<sub>j</sub> &minus; y<sub>j</sub>|<sup>p</sup>)<sup>1/p</sup>. Reduces to Manhattan at p=1 and Euclidean at p=2.</td>
            </tr>
            <tr>
              <td><strong>Majority Voting</strong></td>
              <td>A decision rule where each of the K nearest neighbors casts one unweighted vote, and the class with the most votes wins.</td>
            </tr>
            <tr>
              <td><strong>Distance-Weighted Voting</strong></td>
              <td>A voting variant where a neighbor's influence is inversely proportional to its distance (w = 1/d), favoring closer points.</td>
            </tr>
            <tr>
              <td><strong>Standardization (Z-score)</strong></td>
              <td>A scaling transformation z = (x &minus; &mu;) / &sigma; shifting the feature distribution to zero mean and unit variance.</td>
            </tr>
            <tr>
              <td><strong>Min-Max Normalization</strong></td>
              <td>A bounding transformation x' = (x &minus; x<sub>min</sub>) / (x<sub>max</sub> &minus; x<sub>min</sub>) compressing values into [0, 1].</td>
            </tr>
            <tr>
              <td><strong>Lazy Learner</strong></td>
              <td>An algorithm that defers generalization until inference time by storing training examples rather than learning explicit parameters.</td>
            </tr>
            <tr>
              <td><strong>Curse of Dimensionality</strong></td>
              <td>The phenomenon where high-dimensional feature spaces become exponentially sparse and all pairwise distances become nearly equal.</td>
            </tr>
            <tr>
              <td><strong>Confusion Matrix</strong></td>
              <td>A 2&times;2 contingency table cross-tabulating true class labels against model predictions (TN, FP, FN, TP).</td>
            </tr>
            <tr>
              <td><strong>F1-Score</strong></td>
              <td>The harmonic mean of precision and recall: 2 &times; (Precision &times; Recall) / (Precision + Recall).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">3. Interactive Revision Challenges (12 Exercises)</h3>
      <p>
        Test your understanding by attempting each question before expanding the solution drawer.
      </p>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q1: Intuition — How does KNN predict the category of an unknown fruit?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> KNN compares the unknown fruit's measured features (e.g., sweetness and crispness) to all stored labelled fruits in its memory. It calculates the geometric distance to every stored fruit, identifies the K closest fruits (neighbors), and assigns the unknown fruit to the majority category among those K neighbors.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q2: Prediction Process — Name the 7 sequential steps of a KNN prediction.</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong></p>
          <ol style="margin-left: 20px; line-height: 1.6;">
            <li>Store the labelled training feature vectors and target labels.</li>
            <li>Choose a value for the hyperparameter K and a distance metric.</li>
            <li>Receive an unlabelled query data point.</li>
            <li>Calculate the distance from the query point to every training point.</li>
            <li>Sort all training points by ascending distance and select the top K closest neighbors.</li>
            <li>Collect the target values or classes of those K neighbors.</li>
            <li>Compute the prediction via majority vote (classification) or mean average (regression).</li>
          </ol>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q3: Distance Arithmetic — Calculate Euclidean and Manhattan distance between (2, 3) and (6, 6).</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong></p>
          <p>Given x = (2, 3) and y = (6, 6):</p>
          <ul>
            <li><strong>Coordinate Differences:</strong> &Delta;x<sub>1</sub> = 6 &minus; 2 = 4, &Delta;x<sub>2</sub> = 6 &minus; 3 = 3.</li>
            <li><strong>Euclidean Distance:</strong> d = &radic;(4<sup>2</sup> + 3<sup>2</sup>) = &radic;(16 + 9) = &radic;25 = <strong>5.0000</strong>.</li>
            <li><strong>Manhattan Distance:</strong> d = |4| + |3| = 4 + 3 = <strong>7.0000</strong>.</li>
          </ul>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q4: Tie Breaking — Why does an odd K not guarantee a tie-break in a 3-class problem?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> An odd K (such as K = 3) prevents ties only when there are exactly <strong>two classes</strong> (since 3 votes cannot be split 50/50). In a 3-class problem (e.g., Apple, Orange, Banana), the 3 neighbors can each belong to a distinct class (1 vote for Apple, 1 vote for Orange, 1 vote for Banana), creating an unbreakable 1-1-1 tie!</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q5: Weighted Voting — When two Class 0 points have distance 3.0 and one Class 1 point has distance 1.0, who wins?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li><strong>Simple Majority:</strong> Class 0 has 2 votes, Class 1 has 1 vote &rarr; <strong>Class 0 wins (2 vs 1)</strong>.</li>
            <li><strong>Distance-Weighted (w = 1/d):</strong>
              <br>Weight for Class 1: w = 1 / 1.0 = <strong>1.0000</strong>.
              <br>Weight for Class 0: w = (1 / 3.0) + (1 / 3.0) = 0.3333 + 0.3333 = <strong>0.6667</strong>.
              <br>Since 1.0000 &gt; 0.6667, <strong>Class 1 wins</strong>! Distance weighting overturns the majority because the single Class 1 neighbor is much closer.
            </li>
          </ul>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q6: Feature Scaling — Why is fitting a scaler on the entire dataset before splitting considered data leakage?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> When you fit a scaler (such as <code>StandardScaler</code>) on the full dataset, the mean (&mu;) and standard deviation (&sigma;) are computed using test observations. This contaminates the training feature distribution with information from the holdout set, giving overly optimistic test evaluations and risking real-world deployment failure.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q7: Decision Boundaries — Describe how the decision boundary changes as K increases from 1 to 15.</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> At <strong>K = 1</strong>, the decision boundary is jagged, complex, and filled with isolated decision islands surrounding noisy outlier training points (high variance, overfitting). As K increases to <strong>K = 5</strong>, boundaries become smoother and ignore isolated anomalies. At <strong>K = 15</strong>, boundaries become highly generalized, broad curves; if K is made excessively large, it oversmooths and underfits subtle class distinctions.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q8: Performance Metrics — Given TP = 19, FP = 0, FN = 1, TN = 20, calculate Accuracy, Precision, Recall, and F1.</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li>Total = 19 + 0 + 1 + 20 = 40.</li>
            <li><strong>Accuracy:</strong> (19 + 20) / 40 = 39 / 40 = <strong>0.9750 (97.5%)</strong>.</li>
            <li><strong>Precision:</strong> 19 / (19 + 0) = 19 / 19 = <strong>1.0000 (100.0%)</strong>.</li>
            <li><strong>Recall:</strong> 19 / (19 + 1) = 19 / 20 = <strong>0.9500 (95.0%)</strong>.</li>
            <li><strong>F1-Score:</strong> 2 &times; (1.0 &times; 0.95) / (1.0 + 0.95) = 1.90 / 1.95 &approx; <strong>0.9744 (97.4%)</strong>.</li>
          </ul>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q9: Curse of Dimensionality — Why does Euclidean distance fail when the feature count reaches 1,000?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> In 1,000-dimensional space, the volume of the space grows exponentially, making data points exceedingly sparse. Due to the concentration of distances phenomenon, the Euclidean distance between any pair of points converges to nearly the same value (distance to closest point &approx; distance to farthest point). When all points are equidistant, nearest-neighbor rankings become meaningless.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q10: Computational Complexity — What is the query time complexity of brute-force KNN for N training points and D features?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> For each test query, brute-force KNN must calculate the distance to all N training vectors (each taking &Oscr;(D) operations) and find the top K smallest distances. This yields an inference time complexity of <strong>&Oscr;(N &times; D)</strong>. Unlike parametric models with &Oscr;(D) query speed, KNN becomes very slow when N is large.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q11: Regression Averaging — How does KNeighborsRegressor predict the target price for a 2,000 sq ft house?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> Instead of tallying votes, <code>KNeighborsRegressor</code> identifies the K nearest homes in feature space (e.g., the 5 homes with sizes closest to 2,000 sq ft) and computes the <strong>arithmetic mean</strong> of their actual sale prices: y_pred = (1/K) &sum; y<sub>i</sub> (or a distance-weighted average).</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q12: Python Implementation Challenge — Write a 5-line leak-free KNN classification pipeline.</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <div class="code-container" style="margin-top: 8px;">
            <pre><code class="language-python">from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

pipe = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_neighbors=5))])
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)</code></pre>
          </div>
        </div>
      </details>
    </section>
"""

def get_part4():
    return PART4_HTML
