"""
Module: topic12_part4.py
Contains Sections 16 to 23 for Topic 12: Decision Trees.
"""

from scratch.topic12_svgs import (
    SVG_CONFUSION_MATRIX_HEATMAP,
    SVG_REGRESSION_TREE_CURVE
)

PART4_HTML = f"""
    <!-- SECTION 16: DECISION TREE REGRESSION LAB -->
    <section id="sec-16" class="section-card">
      <span class="section-badge">Section 16</span>
      <h2 class="section-title">Decision Tree Regression Lab</h2>
      <p class="section-lead">
        When the target variable is continuous—such as house prices, stock volumes, or vehicle fuel efficiency—<code>DecisionTreeRegressor</code> partitions the continuous feature space into discrete segments and assigns the arithmetic mean of each leaf's training observations as the prediction.
      </p>

      {SVG_REGRESSION_TREE_CURVE}

      <h3 class="sub-title">1. Executable Python Regression Script</h3>
      <div class="code-container">
        <div class="code-header">
          <span class="code-lang">Python 3</span>
          <span class="code-tag">DecisionTreeRegressor Implementation</span>
        </div>
        <pre><code class="language-python">import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. Generate Synthetic Real Estate Dataset: House Size (100 sq ft) -> Price ($k)
np.random.seed(42)
n_homes = 100
sqft = np.random.uniform(8.0, 32.0, n_homes)  # 800 to 3,200 sq ft
noise = np.random.normal(0, 18.0, n_homes)
price = 50.0 + (11.5 * sqft) + noise

df_reg = pd.DataFrame({{
    'Living_Area_100sqft': np.round(sqft, 1),
    'Price_kUSD': np.round(price, 1)
}})

X_r = df_reg[['Living_Area_100sqft']]
y_r = df_reg['Price_kUSD']

# 2. Train / Test Split (75% Train, 25% Test)
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_r, y_r, test_size=0.25, random_state=42
)

# 3. Instantiate & Fit DecisionTreeRegressor with max_depth=3
reg_tree = DecisionTreeRegressor(max_depth=3, random_state=42)
reg_tree.fit(X_train_r, y_train_r)

# 4. Predict on Holdout Test Homes
y_r_pred = reg_tree.predict(X_test_r)

# 5. Evaluate Error Metrics
mae = mean_absolute_error(y_test_r, y_r_pred)
rmse = np.sqrt(mean_squared_error(y_test_r, y_r_pred))

print(f"Regression Tree (max_depth=3) Holdout MAE:  ${{mae:.2f}}k USD")
print(f"Regression Tree (max_depth=3) Holdout RMSE: ${{rmse:.2f}}k USD")

# Example Single Prediction: 2,000 sq ft home (sqft = 20.0)
sample_home = pd.DataFrame({{'Living_Area_100sqft': [20.0]}})
predicted_price = reg_tree.predict(sample_home)[0]
print(f"Predicted price for 2,000 sq ft home: ${{predicted_price:.2f}}k USD")</code></pre>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span class="code-lang">Console Output</span>
          <span class="code-tag">Regression Runtime Verification</span>
        </div>
        <pre><code class="language-text">Regression Tree (max_depth=3) Holdout MAE:  $14.64k USD
Regression Tree (max_depth=3) Holdout RMSE: $17.01k USD
Predicted price for 2,000 sq ft home: $265.52k USD</code></pre>
      </div>

      <div class="callout callout-warning">
        <div class="callout-title">&#9888;&#65039; Critical Limitation: Extrapolation Failure in Regression Trees</div>
        <p>
          Notice how regression trees predict using flat piece-wise constant steps. If a test home arrives with <strong>10,000 sq ft</strong> (far larger than any home in the training data), a linear regression model would extrapolate upward to $1.2M. In stark contrast, a Decision Tree will route the mansion into its rightmost leaf and predict <strong>$380k (the training maximum mean)</strong>! Regression trees <strong>cannot extrapolate</strong> outside the min/max boundaries of their training features.
        </p>
      </div>
    </section>

    <!-- SECTION 17: EVALUATING CLASSIFICATION TREES -->
    <section id="sec-17" class="section-card">
      <span class="section-badge">Section 17</span>
      <h2 class="section-title">Evaluating Classification Trees: Confusion Matrix &amp; Metrics</h2>
      <p class="section-lead">
        To properly judge how well a tree classifier performs, we dissect its correct and incorrect predictions using a 2&times;2 Confusion Matrix and compute standardized quantitative metrics.
      </p>

      {SVG_CONFUSION_MATRIX_HEATMAP}

      <h3 class="sub-title">1. The Four Fundamental Quadrants</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Quadrant</th>
              <th>Full Name</th>
              <th>Actual Class</th>
              <th>Predicted Class</th>
              <th>Intuitive Meaning in Exam Lab</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="badge-tag badge-tag-c0">TN</span></td>
              <td><strong>True Negative</strong></td>
              <td>Fail (0)</td>
              <td>Fail (0)</td>
              <td>Correctly predicted as failing (20 students).</td>
            </tr>
            <tr>
              <td><span class="badge-tag" style="background:#FEE2E2;color:#991B1B;">FP</span></td>
              <td><strong>False Positive</strong></td>
              <td>Fail (0)</td>
              <td>Pass (1)</td>
              <td>Type I Error: False alarm. Predicted to pass, but actually failed (4 students).</td>
            </tr>
            <tr>
              <td><span class="badge-tag" style="background:#FEF3C7;color:#92400E;">FN</span></td>
              <td><strong>False Negative</strong></td>
              <td>Pass (1)</td>
              <td>Fail (0)</td>
              <td>Type II Error: Missed success. Predicted to fail, but actually passed (1 student).</td>
            </tr>
            <tr>
              <td><span class="badge-tag badge-tag-c1">TP</span></td>
              <td><strong>True Positive</strong></td>
              <td>Pass (1)</td>
              <td>Pass (1)</td>
              <td>Correctly predicted as passing (23 students).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">2. Metric Mathematical Formulas and Worked Example</h3>
      <p>
        Let us compute every metric step by step using the exact holdout test set counts from our Classification Lab (N = 48 students: 24 Fail, 24 Pass):
      </p>
      <div style="display: flex; gap: 12px; margin-bottom: 16px; flex-wrap: wrap;">
        <span class="badge-tag badge-tag-c0">TN = 20</span>
        <span class="badge-tag" style="background:#FEE2E2;color:#991B1B;">FP = 4</span>
        <span class="badge-tag" style="background:#FEF3C7;color:#92400E;">FN = 1</span>
        <span class="badge-tag badge-tag-c1">TP = 23</span>
        <span class="badge-tag" style="background:#F1F5F9;color:#0F172A;">Total = 48</span>
      </div>

      <div class="calc-box">
        <h4 style="margin: 0 0 10px 0; font-size: 1.05rem; color: #0284C7;">1. Accuracy (Overall Correct Fraction)</h4>
        <div class="formula-block">
          Accuracy = (TP + TN) / (TP + TN + FP + FN)
        </div>
        <p style="margin: 8px 0 0 0; font-size: 0.92rem; color: #334155;">
          <strong>Calculation:</strong> (23 + 20) / (23 + 20 + 4 + 1) = 43 / 48 &approx; <strong>0.8958 (89.6%)</strong>.<br>
          <em>Interpretation:</em> The tree made the correct classification on 43 out of 48 holdout test students.
        </p>
      </div>

      <div class="calc-box">
        <h4 style="margin: 0 0 10px 0; font-size: 1.05rem; color: #0284C7;">2. Precision (Purity of Positive Alarms)</h4>
        <div class="formula-block">
          Precision = TP / (TP + FP)
        </div>
        <p style="margin: 8px 0 0 0; font-size: 0.92rem; color: #334155;">
          <strong>Calculation:</strong> 23 / (23 + 4) = 23 / 27 &approx; <strong>0.8519 (85.2%)</strong>.<br>
          <em>Interpretation:</em> When the model predicted that a student would Pass, it was correct 85.2% of the time (4 false alarms).
        </p>
      </div>

      <div class="calc-box">
        <h4 style="margin: 0 0 10px 0; font-size: 1.05rem; color: #0284C7;">3. Recall or Sensitivity (Positive Coverage)</h4>
        <div class="formula-block">
          Recall = TP / (TP + FN)
        </div>
        <p style="margin: 8px 0 0 0; font-size: 0.92rem; color: #334155;">
          <strong>Calculation:</strong> 23 / (23 + 1) = 23 / 24 &approx; <strong>0.9583 (95.8%)</strong>.<br>
          <em>Interpretation:</em> Out of 24 actual passing students, the tree successfully caught 23 and missed only 1!
        </p>
      </div>

      <div class="calc-box">
        <h4 style="margin: 0 0 10px 0; font-size: 1.05rem; color: #0284C7;">4. F1-Score (Harmonic Mean of Precision and Recall)</h4>
        <div class="formula-block">
          F1 = 2 &times; (Precision &times; Recall) / (Precision + Recall)
        </div>
        <p style="margin: 8px 0 0 0; font-size: 0.92rem; color: #334155;">
          <strong>Calculation:</strong> 2 &times; (0.8519 &times; 0.9583) / (0.8519 + 0.9583) = 1.6327 / 1.8102 &approx; <strong>0.9020 (90.2%)</strong>.<br>
          <em>Interpretation:</em> Harmonizes high precision and exceptional recall into a single robust performance indicator.
        </p>
      </div>
    </section>

    <!-- SECTION 18: ADVANTAGES AND LIMITATIONS -->
    <section id="sec-18" class="section-card">
      <span class="section-badge">Section 18</span>
      <h2 class="section-title">Advantages and Limitations of Decision Trees</h2>
      <p class="section-lead">
        Decision Trees are immensely popular in applied machine learning, but they are not silver bullets. Understanding their operational boundaries is essential for professional system design.
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
                  <li><strong>White-Box Interpretability:</strong> Decisions can be directly traced as transparent if-else rules.</li>
                  <li><strong>Zero Feature Scaling Required:</strong> Completely invariant to monotonic transformations. Works identically whether features are scaled or raw!</li>
                  <li><strong>Non-Linear Flexibility:</strong> Naturally captures non-linear relationships and complex feature interactions.</li>
                  <li><strong>Fast Inference Speed:</strong> Classifying a query requires only &Oscr;(Tree Depth) comparisons (sub-millisecond!).</li>
                  <li><strong>Handles Mixed Types:</strong> Gracefully processes numerical and categorical features within appropriate pipelines.</li>
                </ul>
              </td>
              <td>
                <ul style="margin: 0; padding-left: 18px; line-height: 1.6;">
                  <li><strong>High Variance &amp; Instability:</strong> Adding or removing a handful of training samples can result in a completely different tree.</li>
                  <li><strong>Greedy Splitting:</strong> Makes locally optimal splits at each step, which may miss the globally optimal tree.</li>
                  <li><strong>Axis-Aligned Restriction:</strong> Struggles to capture smooth diagonal or circular decision boundaries efficiently.</li>
                  <li><strong>Extrapolation Failure:</strong> In regression, cannot predict values outside the min/max range of training data.</li>
                  <li><strong>Overfitting Tendency:</strong> Unconstrained trees memorize noise rapidly without careful pre-pruning or ensembles.</li>
                </ul>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 19: TREES VS OTHER ALGORITHMS -->
    <section id="sec-19" class="section-card">
      <span class="section-badge">Section 19</span>
      <h2 class="section-title">Decision Trees Compared With Other Algorithms</h2>
      <p class="section-lead">
        To architect effective machine learning systems, you must know when to deploy a single Decision Tree versus a Linear Model, KNN, or an Ensemble method.
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Evaluation Dimension</th>
              <th>Decision Tree</th>
              <th>Logistic Regression</th>
              <th>K-Nearest Neighbors (KNN)</th>
              <th>Random Forest</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Model Paradigm</strong></td>
              <td>Non-parametric, eager learner</td>
              <td>Parametric, eager learner</td>
              <td>Non-parametric, lazy learner</td>
              <td>Ensemble of de-correlated trees (Bagging)</td>
            </tr>
            <tr>
              <td><strong>Interpretability</strong></td>
              <td><strong>High:</strong> Visual if-then tree diagram</td>
              <td><strong>High:</strong> Odds ratios and weight coefficients</td>
              <td><strong>Local:</strong> Inspect nearest neighbors</td>
              <td><strong>Low:</strong> Black-box combination of hundreds of trees</td>
            </tr>
            <tr>
              <td><strong>Boundary Shape</strong></td>
              <td>Axis-aligned orthogonal rectangles</td>
              <td>Strictly linear hyperplane</td>
              <td>Arbitrary non-linear, locally curving</td>
              <td>Smooth, complex non-linear contours</td>
            </tr>
            <tr>
              <td><strong>Feature Scaling</strong></td>
              <td><strong>Not Required</strong> (Scale invariant)</td>
              <td>Required when regularized (L1/L2)</td>
              <td><strong>Mandatory</strong> (Euclidean distances)</td>
              <td><strong>Not Required</strong> (Scale invariant)</td>
            </tr>
            <tr>
              <td><strong>Variance &amp; Overfitting</strong></td>
              <td>High variance; prone to deep memorization</td>
              <td>Low variance; high bias on non-linear data</td>
              <td>High variance for small K (K=1)</td>
              <td><strong>Very Low:</strong> Averaging 100+ trees cancels variance!</td>
            </tr>
            <tr>
              <td><strong>Query Latency</strong></td>
              <td>Ultra-Fast: &Oscr;(Tree Depth)</td>
              <td>Ultra-Fast: &Oscr;(D) dot product</td>
              <td>Slow: &Oscr;(N &times; D) distance checks</td>
              <td>Moderate: &Oscr;(Trees &times; Depth)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 20: REAL-LIFE CASE STUDIES -->
    <section id="sec-20" class="section-card">
      <span class="section-badge">Section 20</span>
      <h2 class="section-title">Real-Life Case Studies</h2>
      <p class="section-lead">
        Explore four realistic case studies across education, financial banking, real estate, and clinical healthcare to see where decision trees excel and where governance is required.
      </p>

      <div class="grid-2col">
        <div class="calc-box">
          <h4 style="margin: 0 0 10px 0; color: #0284C7; font-size: 1.1rem;">Case 1: Student Pass/Fail Early Warning</h4>
          <p style="font-size: 0.92rem; line-height: 1.6; color: #334155;">
            <strong>Features:</strong> Weekly Study Hours, Lecture Attendance %, Midterm Exam Score.<br>
            <strong>Target:</strong> Course Outcome (Pass vs. Remedial Mentorship Needed).<br>
            <strong>Why Trees Excel:</strong> Academic advisors need transparent rules they can explain to students: <em>"If your attendance drops below 75% and study hours are under 6, our historical data indicates a 91% risk of course failure."</em><br>
            <strong>Limitation:</strong> Grading standard shifts between professors can reduce historical tree accuracy.
          </p>
        </div>

        <div class="calc-box">
          <h4 style="margin: 0 0 10px 0; color: #0284C7; font-size: 1.1rem;">Case 2: Consumer Loan Credit-Risk Assessment</h4>
          <p style="font-size: 0.92rem; line-height: 1.6; color: #334155;">
            <strong>Features:</strong> Debt-to-Income Ratio (DTI), Credit Score, Annual Income, Delinquent Accounts.<br>
            <strong>Target:</strong> Credit Risk (Approved vs. Denied).<br>
            <strong>Why Trees Excel:</strong> Financial regulatory frameworks (e.g. Equal Credit Opportunity Act) mandate adverse action notices explaining the exact reason an applicant was denied.<br>
            <strong>Fairness &amp; Governance Disclaimer:</strong> <em>Real credit decisions require validated models, algorithmic auditing, and strict prevention of disparate impact against protected classes.</em>
          </p>
        </div>

        <div class="calc-box">
          <h4 style="margin: 0 0 10px 0; color: #0284C7; font-size: 1.1rem;">Case 3: Residential Property Value Estimation</h4>
          <p style="font-size: 0.92rem; line-height: 1.6; color: #334155;">
            <strong>Features:</strong> Living Area (sq ft), Bedroom Count, Zip Code, Lot Size.<br>
            <strong>Target:</strong> House Sale Price ($k USD).<br>
            <strong>Why Trees Excel:</strong> Captures categorical neighborhood boundaries and non-linear lot size premiums.<br>
            <strong>Limitation:</strong> As demonstrated in Section 16, regression trees cannot extrapolate prices for luxury mansions larger than any home in the training dataset.
          </p>
        </div>

        <div class="calc-box">
          <h4 style="margin: 0 0 10px 0; color: #0284C7; font-size: 1.1rem;">Case 4: Emergency Department Triage Screening</h4>
          <p style="font-size: 0.92rem; line-height: 1.6; color: #334155;">
            <strong>Features:</strong> Systolic BP, Heart Rate, Oxygen Saturation (SpO2), Age.<br>
            <strong>Target:</strong> Triage Acuity (High Priority vs. Stable).<br>
            <strong>Why Trees Excel:</strong> Resembles clinical clinical pathways: emergency nurses can verify that SpO2 &lt; 90% immediately triggers high-priority triage.<br>
            <strong>Clinical Disclaimer:</strong> <em>Educational models are not certified clinical diagnostic tools and must never replace qualified clinical judgment by licensed medical personnel.</em>
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 21: KEY VISUALIZATIONS GALLERY -->
    <section id="sec-21" class="section-card">
      <span class="section-badge">Section 21</span>
      <h2 class="section-title">Required Graphics &amp; Visual Gallery</h2>
      <p class="section-lead">
        Visual intuition is the bedrock of machine learning mastery. Below is the complete catalogue of all 15 hand-crafted vector diagrams embedded throughout this chapter, along with their core architectural takeaways.
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
              <td><strong>Fig 12.1</strong></td>
              <td>Decision Tree Architecture Hero</td>
              <td>Visualizes the 4-stage pipeline from unpartitioned data to recursive greedy binary splitting.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.2</strong></td>
              <td>Anatomy of a Decision Tree</td>
              <td>Highlights depth levels (0, 1, 2), root, branches, internal nodes, and terminal leaves.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.3</strong></td>
              <td>Prediction Traversal Walkthrough</td>
              <td>Follows student Alex step by step through root and internal decisions to predict PASS.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.4</strong></td>
              <td>Classification vs. Regression Comparison</td>
              <td>Contrasts categorical mode predictions with continuous arithmetic mean step outputs.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.5</strong></td>
              <td>Homogeneity Increase via Split</td>
              <td>Shows parent impurity (Gini=0.50) dropping to weighted child Gini of 0.3125.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.6</strong></td>
              <td>Gini Impurity Function Curve</td>
              <td>Inverted parabola peaking at 0.50 for balanced binary splits and reaching 0.0 at pure nodes.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.7</strong></td>
              <td>Shannon Entropy Function Curve</td>
              <td>Bell curve measuring impurity in bits, peaking at 1.00 bit for 50/50 uncertainty.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.8</strong></td>
              <td>Entropy vs. Gini Comparison</td>
              <td>Proves scaled Gini (2 &times; Gini) closely mirrors Entropy, explaining &gt;98% split parity.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.9</strong></td>
              <td>Information Gain Arithmetic</td>
              <td>Step-by-step arithmetic verifying an Information Gain of 0.2958 bits.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.10</strong></td>
              <td>Fitted Scikit-Learn Decision Tree</td>
              <td>Visualizes the actual trained tree with thresholds, sample counts, and value arrays.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.11</strong></td>
              <td>Orthogonal Decision Boundaries</td>
              <td>Contrasts underfitting stump (depth 1), optimal sweet spot (depth 3), and overfit noise boxes (depth 8).</td>
            </tr>
            <tr>
              <td><strong>Fig 12.12</strong></td>
              <td>Complexity Curve Across Depths</td>
              <td>Demonstrates training accuracy reaching 100% while validation accuracy peaks at depth 4.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.13</strong></td>
              <td>Feature Importance Bar Chart</td>
              <td>Shows Study_Hours accounting for 86.8% of MDI reduction vs. 13.2% for Attendance_Pct.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.14</strong></td>
              <td>Holdout Confusion Matrix Heatmap</td>
              <td>Displays holdout evaluation (20 TN, 4 FP, 1 FN, 23 TP), yielding 89.6% Accuracy and 95.8% Recall.</td>
            </tr>
            <tr>
              <td><strong>Fig 12.15</strong></td>
              <td>Regression Tree Step Curve</td>
              <td>Illustrates piece-wise constant plateaus and highlights the extrapolation failure outside training bounds.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 22: COMMON BEGINNER MISTAKES -->
    <section id="sec-22" class="section-card">
      <span class="section-badge">Section 22</span>
      <h2 class="section-title">12 Common Beginner Mistakes and How to Avoid Them</h2>
      <p class="section-lead">
        Learn from the missteps of others. Review these 12 pervasive mistakes made by students and novice practitioners, along with their concrete solutions.
      </p>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 1: Confusing a Decision Branch with a Terminal Leaf</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Assuming that every box in a tree diagram makes a final prediction.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Internal nodes only ask questions and route data down branches. Only <em>terminal leaf nodes</em> (nodes with no children) produce final predictions.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 2: Assuming Every Decision Tree Must Be Binary</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Believing all decision tree algorithms split into exactly two branches.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> While scikit-learn's CART algorithm uses binary splits, other historical algorithms (such as ID3 and C4.5) support multi-way splits for categorical attributes.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 3: Confusing Entropy with Information Gain</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Stating that a good split has "high entropy".</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Entropy measures <em>impurity/disorder</em> (you want child nodes to have <strong>low entropy</strong>). Information Gain measures <em>entropy reduction</em> (you want <strong>high Information Gain</strong>).</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 4: Treating Gini Impurity as the Same Formula as Entropy</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Using Gini and Entropy interchangeably in mathematical calculations.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Gini is polynomial: <code>1 - &sum; p&#7522;&sup2;</code> (max 0.50). Entropy is logarithmic: <code>- &sum; p&#7522; log&#8322;(p&#7522;)</code> (max 1.00 bit).</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 5: Assuming Deeper Trees Are Always Superior</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Allowing trees to grow unconstrained because training accuracy reaches 100%.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Unconstrained trees memorize noise and outliers. Always tune <code>max_depth</code> and <code>min_samples_leaf</code> via cross-validation.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 6: Tuning Hyperparameters on the Test Set</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Trying different <code>max_depth</code> values on the test set and picking the best one.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> This causes severe data leakage. Tune depth using K-fold cross-validation strictly on training data, and evaluate on the test set exactly once.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 7: Assuming Feature Importance Proves Real-World Causality</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Concluding that increasing a high-importance feature will cause business outcomes to improve.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Feature importance measures predictive correlation in split criteria, not physical causality. Conduct randomized controlled trials for causal claims.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 8: Relying Exclusively on Accuracy for Imbalanced Classes</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Celebrating 95% accuracy when 95% of samples belong to the majority class.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> A naive tree predicting only majority class achieves 95% accuracy while completely failing to detect the minority class. Inspect Precision, Recall, and F1-Score.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 9: Reporting Training Accuracy as Final Generalization Performance</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Showing stakeholders the 99% accuracy measured on the data used to train the tree.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Training performance reflects memorization. Only report metrics evaluated on an independent, held-out test set.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 10: Assuming Scaling is Mandatory for Decision Trees</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Spending hours fine-tuning StandardScaler for a Decision Tree.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Decision Trees are scale-invariant: a split on <code>Hours &le; 6.5</code> operates identically whether hours are raw or standardized. Scaling is optional for trees!</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 11: Expecting a Single Tree to Extrapolate in Regression</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Predicting house prices for living areas far larger than any training home and expecting continuous scaling.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Regression trees predict leaf means and cannot extrapolate outside training boundaries. Use Linear Regression or Splines if extrapolation is required.</p>
      </div>

      <div class="mistake-card">
        <div class="mistake-header">
          <span class="mistake-icon">&times;</span>
          <span class="mistake-title">Mistake 12: Treating Synthetic Lab Results as Proof of Production Reliability</span>
        </div>
        <p class="mistake-text"><strong>The Error:</strong> Assuming 90% accuracy on synthetic Gaussian data guarantees identical enterprise performance.</p>
        <p class="mistake-fix"><strong>The Fix:</strong> Real tabular data contains missing records, concept drift, and multi-modal distributions. Test thoroughly on live shadow traffic.</p>
      </div>
    </section>

    <!-- SECTION 23: SUMMARY, GLOSSARY AND REVISION -->
    <section id="sec-23" class="section-card">
      <span class="section-badge">Section 23</span>
      <h2 class="section-title">Summary, Comprehensive Glossary &amp; Interactive Revision</h2>
      <p class="section-lead">
        Consolidate everything you have mastered with our chapter summary, a 16-term technical glossary, and 12 interactive revision challenges complete with step-by-step arithmetic and Python solutions.
      </p>

      <h3 class="sub-title">1. Chapter Summary &amp; Deployment Checklist</h3>
      <div class="callout callout-info">
        <div class="callout-title">The Decision Tree Production Deployment Checklist</div>
        <ul style="margin: 8px 0 0 20px; line-height: 1.7;">
          <li>&check; <strong>Problem Type Identified:</strong> Confirmed discrete target (ClassificationTree) or continuous target (RegressionTree).</li>
          <li>&check; <strong>Pre-Pruning Configured:</strong> Set sensible constraints on <code>max_depth</code>, <code>min_samples_split</code>, and <code>min_samples_leaf</code> to curb overfitting.</li>
          <li>&check; <strong>Hyperparameter Validation:</strong> Tuned tree depth via K-fold cross-validation exclusively on the training partition.</li>
          <li>&check; <strong>Criterion Selected:</strong> Configured <code>criterion='gini'</code> for fast training or <code>criterion='entropy'</code> for information-theoretic consistency.</li>
          <li>&check; <strong>Extrapolation Verified:</strong> For regression tasks, confirmed that production query features stay within the training feature domain.</li>
          <li>&check; <strong>Class Imbalance Addressed:</strong> Applied <code>class_weight='balanced'</code> if minority classes are heavily outnumbered.</li>
          <li>&check; <strong>Holdout Evaluation:</strong> Evaluated final model on the held-out test set reporting Precision, Recall, and F1-Score alongside Accuracy.</li>
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
              <td><strong>Root Node</strong></td>
              <td>The topmost entry node of a decision tree containing the complete, unpartitioned training dataset.</td>
            </tr>
            <tr>
              <td><strong>Internal Node</strong></td>
              <td>A decision node that evaluates an input feature against a cutoff threshold and forks into child branches.</td>
            </tr>
            <tr>
              <td><strong>Leaf Node</strong></td>
              <td>A terminal node with no outgoing branches that assigns the final class (mode) or numerical value (mean).</td>
            </tr>
            <tr>
              <td><strong>Branch (Edge)</strong></td>
              <td>A directed link representing the outcome of a decision rule connecting a parent node to a child node.</td>
            </tr>
            <tr>
              <td><strong>Tree Depth</strong></td>
              <td>The length of the longest path from the root node to any terminal leaf node.</td>
            </tr>
            <tr>
              <td><strong>Impurity</strong></td>
              <td>A mathematical metric quantifying how mixed or heterogeneous class labels are inside a node.</td>
            </tr>
            <tr>
              <td><strong>Gini Impurity</strong></td>
              <td>A polynomial impurity measure: 1 - &sum; p&#7522;&sup2;. Equals 0 for pure nodes and 0.50 for balanced binary nodes.</td>
            </tr>
            <tr>
              <td><strong>Shannon Entropy</strong></td>
              <td>A logarithmic measure of uncertainty: - &sum; p&#7522; log&#8322;(p&#7522;), measured in units of binary bits.</td>
            </tr>
            <tr>
              <td><strong>Information Gain</strong></td>
              <td>The reduction in entropy achieved by partitioning a parent node into child subsets.</td>
            </tr>
            <tr>
              <td><strong>CART Algorithm</strong></td>
              <td>Classification and Regression Trees: a greedy recursive algorithm utilizing binary splits and Gini/MSE criteria.</td>
            </tr>
            <tr>
              <td><strong>Pre-Pruning</strong></td>
              <td>Early stopping techniques that halt tree expansion during training before nodes become overfit.</td>
            </tr>
            <tr>
              <td><strong>Cost-Complexity Pruning</strong></td>
              <td>A post-pruning technique (via <code>ccp_alpha</code>) that penalizes tree size to find the optimal subtree.</td>
            </tr>
            <tr>
              <td><strong>Feature Importance (MDI)</strong></td>
              <td>Mean Decrease in Impurity: the total weighted impurity reduction brought by a feature across all splits.</td>
            </tr>
            <tr>
              <td><strong>Decision Stump</strong></td>
              <td>A 1-level decision tree (<code>max_depth=1</code>) making predictions using exactly one single split rule.</td>
            </tr>
            <tr>
              <td><strong>Axis-Aligned Cut</strong></td>
              <td>A split perpendicular to a single feature axis, restricting decision regions to orthogonal rectangles.</td>
            </tr>
            <tr>
              <td><strong>Piece-Wise Constant</strong></td>
              <td>A step-like function predicting a constant flat numerical plateau for all inputs landing in the same leaf.</td>
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
          <span>Q1: Intuition — How does a Decision Tree make a classification decision?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> A Decision Tree routes an unlabelled observation from the top Root Node down through a sequence of internal nodes. At each node, it tests a single feature against a numerical threshold (e.g., <code>Study_Hours &le; 6.5</code>) and branches left or right based on the answer until it hits a terminal Leaf Node, which outputs the majority class of training points in that leaf.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q2: Anatomy — Name and define the four primary visual components of a Decision Tree.</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong></p>
          <ul style="margin-left: 20px; line-height: 1.6;">
            <li><strong>Root Node:</strong> The single top entry node containing the full unpartitioned dataset.</li>
            <li><strong>Internal / Decision Nodes:</strong> Intermediate nodes testing feature conditions and splitting into children.</li>
            <li><strong>Branches / Edges:</strong> Directed arrows representing the True/False outcomes of tests.</li>
            <li><strong>Leaf / Terminal Nodes:</strong> Endpoints with no children that assign final predictions.</li>
          </ul>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q3: Gini Arithmetic — Calculate Gini Impurity for a node with 14 Pass and 6 Fail.</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong></p>
          <p>Total N = 14 + 6 = 20.</p>
          <ul>
            <li>Proportions: p<sub>pass</sub> = 14/20 = 0.7, p<sub>fail</sub> = 6/20 = 0.3.</li>
            <li>Sum of squared proportions: (0.7)&sup2; + (0.3)&sup2; = 0.49 + 0.09 = 0.58.</li>
            <li><strong>Gini Impurity = 1 - 0.58 = 0.4200</strong>.</li>
          </ul>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q4: Entropy Arithmetic — Calculate Entropy for a balanced node with 10 Pass and 10 Fail.</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong></p>
          <p>p<sub>pass</sub> = 10/20 = 0.5, p<sub>fail</sub> = 10/20 = 0.5.</p>
          <ul>
            <li>Recall that log<sub>2</sub>(0.5) = -1.0.</li>
            <li>Entropy = - [ 0.5 &times; log<sub>2</sub>(0.5) + 0.5 &times; log<sub>2</sub>(0.5) ]</li>
            <li>Entropy = - [ 0.5 &times; (-1.0) + 0.5 &times; (-1.0) ] = - [ -0.5 - 0.5 ] = <strong>1.0000 bit</strong>.</li>
          </ul>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q5: Information Gain — Explain the difference between Entropy and Information Gain.</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> <strong>Entropy</strong> measures the <em>amount of disorder or uncertainty</em> inside a single node (0 bits is pure, 1 bit is complete chaos). <strong>Information Gain</strong> measures the <em>reduction in entropy</em> achieved by splitting a parent node into child subsets: <code>IG = H(parent) - Weighted_Child_Entropy</code>. A decision tree chooses the split that maximizes Information Gain.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q6: Gini vs. Entropy — Why is Gini Impurity generally preferred as the default in production?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> Gini Impurity involves only simple multiplication and subtraction (<code>1 - &sum; p&#7522;&sup2;</code>), whereas Entropy requires calculating base-2 logarithms for every candidate split. Avoiding logarithms makes Gini significantly faster to compute, and in over 98% of cases, both criteria select identical splits.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q7: Decision Boundaries — Why are Decision Tree decision boundaries strictly axis-aligned?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> Standard decision trees test only one feature at a time per node (e.g., <code>x&#8321; &le; 5.0</code>). In 2D space, a threshold on x&#8321; draws a vertical line, and a threshold on x&#8322; draws a horizontal line. This constrains the decision regions to a grid of orthogonal, axis-aligned rectangular boxes.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q8: Overfitting — What happens to training and test accuracy when a tree grows without depth limits?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> Training accuracy reaches <strong>100%</strong> because the tree creates tiny isolated leaf nodes around every single training point (including noise and outliers). However, test accuracy collapses (high variance, severe overfitting) because the complex, jagged rules fail to generalize to unseen data.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q9: Pruning — What is the difference between pre-pruning and cost-complexity pruning?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> <strong>Pre-pruning</strong> halts tree growth early during training using stopping criteria like <code>max_depth</code> or <code>min_samples_leaf</code>. <strong>Cost-complexity pruning</strong> (post-pruning via <code>ccp_alpha</code>) grows an unconstrained deep tree first, then prunes away branches that contribute little impurity reduction relative to the penalty parameter.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q10: Feature Importance — Why does high feature importance not prove real-world causality?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> Mean Decrease in Impurity (MDI) importance only measures how effectively a feature was used to separate training labels in that specific dataset. It can be biased toward continuous features with many split points, and it cannot distinguish between correlation and genuine physical causation.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q11: Regression Trees — How does DecisionTreeRegressor predict target values, and why can it not extrapolate?</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <p><strong>Answer:</strong> <code>DecisionTreeRegressor</code> predicts the <strong>arithmetic mean</strong> of the target values of all training observations landing in a leaf, resulting in a piece-wise constant step function. Because predictions are bounded by the leaf means of training data, any test sample far beyond the training feature range simply receives the prediction of the nearest boundary leaf, making extrapolation impossible.</p>
        </div>
      </details>

      <details class="accordion">
        <summary class="accordion-summary">
          <span>Q12: Python Implementation — Write a 4-line snippet to train a pre-pruned tree classifier.</span>
          <span class="accordion-icon">+</span>
        </summary>
        <div class="accordion-content">
          <div class="code-container" style="margin-top: 8px;">
            <pre><code class="language-python">from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)</code></pre>
          </div>
        </div>
      </details>
    </section>
"""

def get_part4():
    return PART4_HTML
