"""
Topic 15: Ensemble Learning - Part 3
Sections:
- Section 14: Learning Rate and Number of Estimators
- Section 15: XGBoost Introduction
- Section 16: Stacking (Stacked Generalization)
- Section 17: Bagging vs Boosting vs Stacking vs Voting
- Section 18: Complete Python Classification Lab
- Section 19: Regression Ensemble Lab
- Section 20: Evaluation Metrics
"""

TOPIC_15_PART3 = """
    <!-- SECTION 14 -->
    <section id="sec-14" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 14</span>
        <h2 class="section-title">Learning Rate and Number of Estimators</h2>
        <p class="section-subtitle">Balancing shrinkage and iteration count: avoiding both premature underfitting and catastrophic overfitting.</p>
      </div>

      <p>
        In gradient boosting algorithms, two hyperparameters are intimately coupled: the <strong>learning rate &eta;</strong> (often termed <em>shrinkage</em>) and the <strong>number of estimators M</strong> (<code>n_estimators</code>). Understanding their interaction is essential to tuning state-of-the-art boosting pipelines.
      </p>

      <h3>The Shrinkage Principle</h3>
      <p>
        Recall the additive model: <code>F_m(x) = F_{m-1}(x) + &eta; &times; h_m(x)</code>. If &eta; = 1.0, each tree adds 100% of its fitted residual prediction. While this leads to rapid initial training loss reduction, it often overshoots the minimum and quickly begins fitting to training noise.
      </p>
      <p>
        Setting &eta; to a small value (such as 0.05 or 0.10) scales down each tree's contribution. This forces the algorithm to take conservative, graceful steps along the loss gradient. Individual trees cannot dominate the ensemble, which leaves ample margin for future trees to capture subtle residual patterns.
      </p>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_BOOSTING_STAGES_CURVE__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.1: Training Loss vs. Validation Loss Across Boosting Stages.</strong> While training loss steadily drops toward zero, validation loss reaches an optimal minimum at stage 42. Continuing training beyond this point leads to overfitting as the model memorizes idiosyncratic training noise.
        </div>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Hyperparameter Configuration</th>
              <th>Training Convergence</th>
              <th>Overfitting Vulnerability</th>
              <th>Recommended Production Strategy</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>High &eta; (&ge; 0.30), Low M (&lt; 30)</strong></td>
              <td>Very Fast</td>
              <td>High: Prone to oscillation and poor generalization</td>
              <td>Quick baseline prototyping; rarely optimal for production</td>
            </tr>
            <tr>
              <td><strong>Medium &eta; (0.10), Medium M (50&ndash;100)</strong></td>
              <td>Moderate</td>
              <td>Balanced: Standard starting point</td>
              <td>Default exploration range for tabular benchmarks</td>
            </tr>
            <tr>
              <td><strong>Low &eta; (0.01&ndash;0.05), High M (200&ndash;1,000)</strong></td>
              <td>Slow (Requires compute)</td>
              <td>Lowest (When paired with Early Stopping)</td>
              <td><strong>Gold Standard:</strong> Pair low &eta; with <code>early_stopping_rounds</code></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout-card success-card">
        <div class="success-title">The Early Stopping Rule</div>
        <p>
          Never guess the exact number of boosting stages! In production, set <code>n_estimators</code> to a large number (e.g., <code>1000</code>), set a small learning rate (<code>learning_rate=0.03</code>), and enable early stopping (e.g., <code>n_iter_no_change=10</code> in scikit-learn or <code>early_stopping_rounds=15</code> in XGBoost). Training terminates automatically when validation loss fails to improve for 10 consecutive iterations, saving compute and guaranteeing optimal generalization!
        </p>
      </div>
    </section>

    <!-- SECTION 15 -->
    <section id="sec-15" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 15</span>
        <h2 class="section-title">XGBoost Introduction: Extreme Gradient Boosting</h2>
        <p class="section-subtitle">Second-order Taylor approximations, hardware-level optimizations, and algorithmic regularization.</p>
      </div>

      <p>
        Developed in 2014 by Tianqi Chen at the University of Washington, <strong>XGBoost</strong> (e<strong>X</strong>treme <strong>G</strong>radient <strong>Boost</strong>ing) transformed competitive data science. XGBoost implements the gradient-boosted decision tree framework, but incorporates dramatic mathematical and systems engineering enhancements:
      </p>

      <h3>Key Architectural Breakthroughs of XGBoost</h3>
      <ol>
        <li><strong>Second-Order Taylor Expansion:</strong> While classical gradient boosting relies only on the first-order gradient g_i = &part;L / &part;y&#770;_i, XGBoost calculates both the first-order gradient g_i and the second-order Hessian h_i = &part;&sup2;L / &part;y&#770;_i&sup2;. This provides curvature information, enabling much faster and more accurate Newton-Raphson optimization steps.</li>
        <li><strong>Built-In Regularization (&Omega;(f)):</strong> The objective function explicitly penalizes tree complexity:
          <br><br>
          <code>L_XGB = &sum;_{i=1}^N L(y_i, y&#770;_i) + &sum;_{k=1}^M [ &gamma;&middot;T_k + (1/2)&lambda;&middot;&sum;_{j=1}^{T_k} w_{kj}&sup2; + &alpha;&middot;&sum;_{j=1}^{T_k} |w_{kj}| ]</code>
          <br><br>
          Where T_k is the number of leaves in tree k, &gamma; penalizes adding new leaves, &lambda; is L₂ leaf weight regularization, and &alpha; is L₁ leaf regularization.</li>
        <li><strong>Sparsity-Aware Split Finding:</strong> Missing values are automatically assigned to an optimal default branch learned from the data, eliminating the need for manual imputation.</li>
        <li><strong>Hardware-Level Optimizations:</strong> Utilizes cache-aware pre-fetching, compressed column blocks, and multi-threaded parallel split finding across CPU and GPU cores.</li>
      </ol>

      <h3>Python Implementation: Verified XGBClassifier Demo</h3>
      <div class="code-container">
        <div class="code-header">
          <span class="code-lang-badge">Python &bull; XGBoost 3.4</span>
          <span style="color:#94A3B8; font-size:0.75rem;">xgboost_classifier_demo.py</span>
        </div>
        <pre class="code-body">import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

# 1. Generate reproducible dataset
X, y = make_classification(n_samples=240, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 2. Instantiate and fit XGBClassifier
xgb_clf = xgb.XGBClassifier(
    n_estimators=50,
    learning_rate=0.1,
    max_depth=3,
    reg_lambda=1.0,
    random_state=42,
    eval_metric='logloss'
)
xgb_clf.fit(X_train, y_train)

# 3. Evaluate performance
xgb_preds = xgb_clf.predict(X_test)
print(f"XGBoost Test Accuracy: {accuracy_score(y_test, xgb_preds):.4f} ({accuracy_score(y_test, xgb_preds) * 100:.2f}%)")
print(f"XGBoost Test F1 Score: {f1_score(y_test, xgb_preds):.4f}")</pre>
      </div>

      <div class="code-output">
        <div class="code-output-title">Verified Execution Output</div>XGBoost Test Accuracy: 0.9583 (95.83%)
XGBoost Test F1 Score: 0.9583</div>
    </section>

    <!-- SECTION 16 -->
    <section id="sec-16" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 16</span>
        <h2 class="section-title">Stacking (Stacked Generalization)</h2>
        <p class="section-subtitle">Hierarchical learning: using out-of-fold base predictions to train a secondary meta-model.</p>
      </div>

      <p>
        Introduced by David Wolpert in 1992, <strong>Stacking</strong> (or <em>Stacked Generalization</em>) takes model aggregation to the next level. Instead of using fixed analytical rules like voting or averaging, Stacking trains an entirely separate machine learning model&mdash;known as a <strong>meta-model</strong> or <strong>blender</strong>&mdash;to learn the optimal way to combine base models.
      </p>

      <h3>The 2-Level Stacking Architecture</h3>
      <ul>
        <li><strong>Level-0 (Base Learners):</strong> Several diverse models (e.g., Logistic Regression, Random Forest, Support Vector Machine, and Gradient Boosting) are trained on the training features X.</li>
        <li><strong>Level-1 (Meta-Learner):</strong> A simple, highly interpretable model (typically Logistic Regression for classification or Ridge Regression for regression) takes the <em>predictions</em> of the Level-0 models as its input features, and learns to predict the true target y.</li>
      </ul>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_STACKING_ARCHITECTURE__
        </div>
        <div class="visual-caption">
          <strong>Figure 16.1: The Stacking Generalization Architecture.</strong> Level-0 estimators generate out-of-fold prediction columns. These columns are concatenated into a meta-feature matrix, which serves as the input training data for the Level-1 Meta-Learner.
        </div>
      </div>

      <div class="callout-card warn-card">
        <div class="warn-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#DC2626" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
            <line x1="12" y1="9" x2="12" y2="13"></line>
            <line x1="12" y1="17" x2="12.01" y2="17"></line>
          </svg>
          The Catastrophic Danger of In-Sample Meta-Training (Data Leakage)
        </div>
        <p>
          If you train the Level-0 base models on the training set, generate predictions on that <em>exact same</em> training set, and feed those predictions to the meta-model, your pipeline will fail.
          <br><br>
          Why? Because complex base models (like deep Random Forests) memorize training data and output overconfident 99.9% probability estimates. The meta-model will learn to blindly trust these overfitted predictions. When evaluated on unseen test data, the base models make normal errors, but the meta-model is completely unprepared, resulting in catastrophic generalization failure!
          <br><br>
          <strong>The Solution:</strong> Level-1 training features must <em>always</em> be generated using <strong>K-Fold Out-of-Fold Cross-Validation</strong>. Each training slice is predicted by a base model that was trained exclusively on the other K&minus;1 folds!
        </p>
      </div>

      <h3>Python Implementation: scikit-learn StackingClassifier</h3>
      <div class="code-container">
        <div class="code-header">
          <span class="code-lang-badge">Python &bull; StackingClassifier</span>
          <span style="color:#94A3B8; font-size:0.75rem;">stacking_classifier_demo.py</span>
        </div>
        <pre class="code-body">from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

X, y = make_classification(n_samples=240, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Level-0 Base Estimators
base_estimators = [
    ('rf', RandomForestClassifier(n_estimators=40, random_state=42)),
    ('svc', SVC(probability=True, random_state=42)),
    ('lr', LogisticRegression(random_state=42))
]

# Level-1 Meta-Learner (cv=5 prevents in-sample leakage)
stacking_clf = StackingClassifier(
    estimators=base_estimators,
    final_estimator=LogisticRegression(random_state=42),
    cv=5,
    n_jobs=-1
)
stacking_clf.fit(X_train, y_train)

stack_preds = stacking_clf.predict(X_test)
print(f"Stacking Test Accuracy: {accuracy_score(y_test, stack_preds):.4f} ({accuracy_score(y_test, stack_preds) * 100:.2f}%)")
print(f"Stacking Test F1 Score: {f1_score(y_test, stack_preds):.4f}")</pre>
      </div>

      <div class="code-output">
        <div class="code-output-title">Verified Execution Output</div>Stacking Test Accuracy: 0.8958 (89.58%)
Stacking Test F1 Score: 0.9057</div>
    </section>

    <!-- SECTION 17 -->
    <section id="sec-17" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 17</span>
        <h2 class="section-title">Bagging vs. Boosting vs. Stacking vs. Voting: The Master Comparison</h2>
        <p class="section-subtitle">Side-by-side architectural and practical synthesis of the four major ensemble families.</p>
      </div>

      <p>
        To help you select the exact right architecture for your dataset, this master comparison table summarizes the operational principles, algorithms, and practical trade-offs:
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Voting &amp; Averaging</th>
              <th>Bagging (e.g., Random Forest)</th>
              <th>Boosting (AdaBoost, Gradient Boosting, XGBoost)</th>
              <th>Stacking (Stacked Generalization)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Core Principle</strong></td>
              <td>Democratic majority vote or probability average</td>
              <td>Parallel training on bootstrap row &amp; feature samples</td>
              <td>Sequential additive training to correct prior residuals</td>
              <td>Hierarchical blending via a secondary meta-model</td>
            </tr>
            <tr>
              <td><strong>Training Order</strong></td>
              <td>Independent / Parallel</td>
              <td>Independent / Highly Parallel</td>
              <td>Sequential / Iterative</td>
              <td>2-Stage (Base models parallel, then Meta-model)</td>
            </tr>
            <tr>
              <td><strong>Prediction Combination</strong></td>
              <td>Mode or Mean</td>
              <td>Majority class vote or Mean average</td>
              <td>Weighted sum / Shrinkage additions</td>
              <td>Learned prediction from Meta-estimator</td>
            </tr>
            <tr>
              <td><strong>Targeted Error Component</strong></td>
              <td>Variance &amp; Minor Bias</td>
              <td><strong>Variance Reduction</strong></td>
              <td><strong>Bias Reduction</strong></td>
              <td>Both Bias &amp; Variance</td>
            </tr>
            <tr>
              <td><strong>Base Model Types</strong></td>
              <td>Heterogeneous (Diverse algorithms)</td>
              <td>Homogeneous (Deep unpruned trees)</td>
              <td>Homogeneous (Shallow decision stumps/trees)</td>
              <td>Heterogeneous (Diverse algorithms)</td>
            </tr>
            <tr>
              <td><strong>Overfitting Risk</strong></td>
              <td>Low</td>
              <td>Very Low (Robust to increasing tree count)</td>
              <td>Moderate to High (Requires early stopping)</td>
              <td>Moderate (Prevent with K-fold CV)</td>
            </tr>
            <tr>
              <td><strong>Hyperparameter Sensitivity</strong></td>
              <td>Low</td>
              <td>Low (Works well out-of-the-box)</td>
              <td>High (Requires tuning &eta;, depth, subsample)</td>
              <td>High (Must tune base models + meta-model)</td>
            </tr>
            <tr>
              <td><strong>Ideal Use Case</strong></td>
              <td>Quick baseline blending of 3 tuned models</td>
              <td>Tabular data with noisy features and high variance</td>
              <td>Competitive tabular ML demanding maximum accuracy</td>
              <td>Kaggle competitions pushing for the top 0.1% score</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 18 -->
    <section id="sec-18" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 18</span>
        <h2 class="section-title">Complete Python Classification Lab</h2>
        <p class="section-subtitle">Rigorous, multi-model benchmark evaluating 9 distinct classifiers on a unified 60/20/20 train/val/test split.</p>
      </div>

      <p>
        In this end-to-end laboratory, we evaluate 9 distinct classification models on identical data splits. We use a 3-way split: 60% Training (for fitting), 20% Validation (for hyperparameter tuning and model selection), and 20% Test (held out completely until final reporting).
      </p>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_CLASSIFICATION_BENCHMARK__
        </div>
        <div class="visual-caption">
          <strong>Figure 18.1: Unified Classification Model Benchmark.</strong> Side-by-side test accuracy comparison across 9 estimators. Ensemble methods (AdaBoost, Gradient Boosting, XGBoost, Soft Voting, and Random Forest) clearly outperform the baseline Logistic Regression and Single Decision Tree.
        </div>
      </div>

      <h3>Benchmark Evaluation Results Table</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Model Architecture</th>
              <th>Validation Accuracy</th>
              <th>Held-Out Test Accuracy</th>
              <th>Held-Out Test F1 Score</th>
              <th>Relative Performance Rank</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>AdaBoost (50 Stumps)</strong></td>
              <td>0.8750</td>
              <td><span style="color:#059669; font-weight:700;">0.9792 (97.92%)</span></td>
              <td><span style="color:#059669; font-weight:700;">0.9796</span></td>
              <td><strong>Rank 1 (Tie)</strong></td>
            </tr>
            <tr>
              <td><strong>Gradient Boosting (60 Trees)</strong></td>
              <td>0.8958</td>
              <td><span style="color:#059669; font-weight:700;">0.9792 (97.92%)</span></td>
              <td><span style="color:#059669; font-weight:700;">0.9796</span></td>
              <td><strong>Rank 1 (Tie)</strong></td>
            </tr>
            <tr>
              <td><strong>XGBoost (50 Trees)</strong></td>
              <td>0.8542</td>
              <td><span style="color:#0284C7; font-weight:700;">0.9583 (95.83%)</span></td>
              <td><span style="color:#0284C7; font-weight:700;">0.9583</span></td>
              <td>Rank 3</td>
            </tr>
            <tr>
              <td><strong>Random Forest (100 Trees)</strong></td>
              <td>0.8958</td>
              <td>0.9375 (93.75%)</td>
              <td>0.9412</td>
              <td>Rank 4 (Tie)</td>
            </tr>
            <tr>
              <td><strong>Soft Voting Ensemble</strong></td>
              <td>0.9167</td>
              <td>0.9375 (93.75%)</td>
              <td>0.9412</td>
              <td>Rank 4 (Tie)</td>
            </tr>
            <tr>
              <td><strong>Stacking Classifier</strong></td>
              <td>0.9167</td>
              <td>0.8958 (89.58%)</td>
              <td>0.9057</td>
              <td>Rank 6</td>
            </tr>
            <tr>
              <td><strong>Bagging Classifier (50 Trees)</strong></td>
              <td>0.9167</td>
              <td>0.8542 (85.42%)</td>
              <td>0.8627</td>
              <td>Rank 7 (Tie)</td>
            </tr>
            <tr>
              <td><strong>Single Decision Tree</strong></td>
              <td>0.8958</td>
              <td>0.8542 (85.42%)</td>
              <td>0.8727</td>
              <td>Rank 7 (Tie)</td>
            </tr>
            <tr>
              <td><strong>Logistic Regression (Baseline)</strong></td>
              <td>0.9167</td>
              <td>0.8125 (81.25%)</td>
              <td>0.8163</td>
              <td>Rank 9 (Baseline)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Labelled Confusion Matrix: Gradient Boosting Classifier</h3>
      <p>
        Evaluating the confusion matrix of our top-performing Gradient Boosting Classifier on the held-out test split of 48 instances:
      </p>
      <div class="table-wrapper" style="max-width: 480px; margin: 18px auto;">
        <table>
          <thead>
            <tr>
              <th></th>
              <th>Predicted Negative (Class 0)</th>
              <th>Predicted Positive (Class 1)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Actual Negative (Class 0)</strong></td>
              <td><span style="color:#059669; font-weight:800; font-size:1.1rem;">23</span> (True Negative)</td>
              <td><span style="color:#DC2626; font-weight:800; font-size:1.1rem;">1</span> (False Positive)</td>
            </tr>
            <tr>
              <td><strong>Actual Positive (Class 1)</strong></td>
              <td><span style="color:#DC2626; font-weight:800; font-size:1.1rem;">0</span> (False Negative)</td>
              <td><span style="color:#059669; font-weight:800; font-size:1.1rem;">24</span> (True Positive)</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p style="text-align:center; font-size:0.9rem; color:var(--text-muted);">
        Out of 48 held-out test samples, Gradient Boosting achieved 47 correct classifications (97.92% accuracy) and produced 0 False Negatives!
      </p>
    </section>

    <!-- SECTION 19 -->
    <section id="sec-19" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 19</span>
        <h2 class="section-title">Regression Ensemble Lab</h2>
        <p class="section-subtitle">Comparing Single Tree, Random Forest, Gradient Boosting, and Averaging on continuous targets.</p>
      </div>

      <p>
        To evaluate regression performance, we fit four regressors on a synthetic continuous dataset of 160 samples (120 training, 40 held-out test) and evaluate Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the coefficient of determination (R&sup2;):
      </p>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_REGRESSION_ACTUAL_PRED__
        </div>
        <div class="visual-caption">
          <strong>Figure 19.1: Regression Actual vs. Predicted Trajectories.</strong> The Single Decision Tree outputs blocky, step-like predictions. Random Forest, Gradient Boosting, and the Averaging Ensemble track the actual ground truth line with high fidelity and lower residual dispersion.
        </div>
      </div>

      <h3>Regression Evaluation Benchmark Results</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Regression Estimator</th>
              <th>MAE (Mean Absolute Error)</th>
              <th>RMSE (Root Mean Squared Error)</th>
              <th>R&sup2; Score</th>
              <th>Verdict</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Random Forest Regressor (50 Trees)</strong></td>
              <td><span style="color:#059669; font-weight:700;">0.1694</span></td>
              <td><span style="color:#059669; font-weight:700;">0.2185</span></td>
              <td><span style="color:#059669; font-weight:700;">0.9668 (96.68%)</span></td>
              <td><strong>Lowest Error &amp; Highest R&sup2;</strong></td>
            </tr>
            <tr>
              <td><strong>Averaging Ensemble</strong></td>
              <td>0.1786</td>
              <td>0.2218</td>
              <td>0.9658 (96.58%)</td>
              <td>Highly competitive &amp; robust</td>
            </tr>
            <tr>
              <td><strong>Gradient Boosting Regressor</strong></td>
              <td>0.1763</td>
              <td>0.2295</td>
              <td>0.9633 (96.33%)</td>
              <td>Strong fit; slightly higher dispersion</td>
            </tr>
            <tr>
              <td><strong>Single Decision Tree Regressor</strong></td>
              <td>0.2052</td>
              <td>0.2394</td>
              <td>0.9601 (96.01%)</td>
              <td>Highest error; rigid step artifacts</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p>
        Notice that the Random Forest Regressor achieves a <strong>17.4% reduction in Mean Absolute Error</strong> compared to the Single Decision Tree (0.1694 vs. 0.2052), illustrating how averaging multiple randomized trees eliminates jagged prediction discontinuities.
      </p>
    </section>

    <!-- SECTION 20 -->
    <section id="sec-20" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 20</span>
        <h2 class="section-title">Evaluation Metrics for Ensembles</h2>
        <p class="section-subtitle">Selecting the right metric: why accuracy alone is treacherous in real-world ML engineering.</p>
      </div>

      <p>
        A machine learning model is only as good as the metric used to judge it. Depending on the task and business consequences of errors, different metrics must be chosen:
      </p>

      <h3>Classification Metrics</h3>
      <ul>
        <li><strong>Accuracy:</strong> <code>(TP + TN) / (TP + TN + FP + FN)</code>. The percentage of correct predictions. <em>Dangerous when classes are imbalanced!</em> In a dataset where 99% of transactions are legitimate, a useless model that always predicts "Legitimate" achieves 99% accuracy.</li>
        <li><strong>Precision:</strong> <code>TP / (TP + FP)</code>. Out of all instances the model flagged as positive, how many were actually positive? Crucial when False Positives are expensive (e.g., spam filtering, where marking an important work email as spam is unacceptable).</li>
        <li><strong>Recall / Sensitivity:</strong> <code>TP / (TP + FN)</code>. Out of all actual positive cases in the wild, how many did the model find? Crucial when False Negatives are dangerous (e.g., cancer detection or fraud screening, where missing a disease or fraudulent charge is catastrophic).</li>
        <li><strong>F1-Score:</strong> <code>2 &times; (Precision &times; Recall) / (Precision + Recall)</code>. The harmonic mean of Precision and Recall. Balances both concerns.</li>
        <li><strong>ROC-AUC (Area Under the ROC Curve):</strong> Measures the model's ability to rank positive instances higher than negative instances across all possible probability thresholds. Insensitive to class imbalance.</li>
      </ul>

      <h3>Regression Metrics</h3>
      <ul>
        <li><strong>MAE (Mean Absolute Error):</strong> <code>(1 / N) &times; &sum; |y_i &minus; y&#770;_i|</code>. Measures average magnitude of error in original units. Resilient to outliers.</li>
        <li><strong>RMSE (Root Mean Squared Error):</strong> <code>&radic;[ (1 / N) &times; &sum; (y_i &minus; y&#770;_i)&sup2; ]</code>. Heavily penalizes large errors because individual errors are squared before averaging. Use when a single large prediction miss is disastrous.</li>
        <li><strong>R&sup2; (Coefficient of Determination):</strong> <code>1 &minus; [ &sum; (y_i &minus; y&#770;_i)&sup2; ] / [ &sum; (y_i &minus; y&#772;)&sup2; ]</code>. Represents the fraction of target variance explained by the model (1.0 is perfect; 0.0 means the model is no better than predicting the mean y&#772;).</li>
      </ul>
    </section>
"""
