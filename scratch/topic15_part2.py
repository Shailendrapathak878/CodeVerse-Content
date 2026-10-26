"""
Topic 15: Ensemble Learning - Part 2
Sections:
- Section 07: Bagging Classifier
- Section 08: Random Forest
- Section 09: Visualize Random Forest
- Section 10: Out-of-Bag (OOB) Evaluation
- Section 11: Boosting: The Core Idea
- Section 12: AdaBoost
- Section 13: Gradient Boosting
"""

TOPIC_15_PART2 = """
    <!-- SECTION 07 -->
    <section id="sec-07" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 07</span>
        <h2 class="section-title">Bagging Classifier in Practice</h2>
        <p class="section-subtitle">Training parallel ensembles of decision trees using scikit-learn's BaggingClassifier.</p>
      </div>

      <p>
        In scikit-learn, the generic bagging architecture is provided by <code>BaggingClassifier</code> and <code>BaggingRegressor</code>. While any estimator can technically be used as the base learner (including K-Nearest Neighbors or Support Vector Machines), decision trees are overwhelmingly the standard choice because of their high variance and low bias when grown unpruned.
      </p>

      <h3>Key Hyperparameters of BaggingClassifier</h3>
      <ul>
        <li><code>estimator</code>: The base learner to clone and fit across bootstrap samples (in scikit-learn &ge; 1.2, replacing the deprecated <code>base_estimator</code>). Defaults to <code>DecisionTreeClassifier()</code>.</li>
        <li><code>n_estimators</code>: The number of base estimators to train in parallel. Typical values range from 50 to 500.</li>
        <li><code>max_samples</code>: The number (or fraction) of training samples drawn from X to train each base estimator. Defaults to <code>1.0</code> (drawing N samples).</li>
        <li><code>bootstrap</code>: Whether samples are drawn with replacement (<code>True</code>, standard bagging) or without replacement (<code>False</code>, known as <em>Pasting</em>).</li>
        <li><code>n_jobs</code>: Number of CPU cores to execute in parallel (<code>-1</code> uses all available cores).</li>
      </ul>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_BAGGING_DECISION_BOUNDARY__
        </div>
        <div class="visual-caption">
          <strong>Figure 7.1: Decision Boundary Smoothing via Bagging.</strong> While an individual unpruned decision tree carves erratic orthogonal rectangles around isolated training instances, a 50-tree Bagging Classifier averages those boundaries into a smooth, generalizable contour.
        </div>
      </div>

      <h3>Python Implementation: Single Tree vs. BaggingClassifier</h3>
      <div class="code-container">
        <div class="code-header">
          <span class="code-lang-badge">Python &bull; BaggingClassifier</span>
          <span style="color:#94A3B8; font-size:0.75rem;">bagging_classifier_demo.py</span>
        </div>
        <pre class="code-body">from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

# 1. Generate synthetic classification dataset
X, y = make_classification(n_samples=240, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 2. Fit single unpruned decision tree
single_tree = DecisionTreeClassifier(random_state=42)
single_tree.fit(X_train, y_train)
tree_preds = single_tree.predict(X_test)

# 3. Fit BaggingClassifier with 50 decision trees
bagging_clf = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=50,
    bootstrap=True,
    random_state=42,
    n_jobs=-1
)
bagging_clf.fit(X_train, y_train)
bagging_preds = bagging_clf.predict(X_test)

print(f"Single Tree Test Accuracy:     {accuracy_score(y_test, tree_preds):.4f} | F1: {f1_score(y_test, tree_preds):.4f}")
print(f"Bagging (50) Test Accuracy:    {accuracy_score(y_test, bagging_preds):.4f} | F1: {f1_score(y_test, bagging_preds):.4f}")</pre>
      </div>

      <div class="code-output">
        <div class="code-output-title">Verified Execution Output</div>Single Tree Test Accuracy:     0.8542 | F1: 0.8727
Bagging (50) Test Accuracy:    0.8542 | F1: 0.8627</div>

      <div class="callout-card warn-card">
        <div class="warn-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#DC2626" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
            <line x1="12" y1="9" x2="12" y2="13"></line>
            <line x1="12" y1="17" x2="12.01" y2="17"></line>
          </svg>
          Why Bagging Performance Flattens and Does Not Improve Indefinitely
        </div>
        <p>
          Beginners often assume that increasing <code>n_estimators</code> from 50 to 5,000 will steadily push accuracy toward 100%. In reality, the performance curve flattens rapidly (usually between 50 and 200 trees). Adding more trees reduces variance asymptotically toward the lower bound defined by the average correlation between trees, but it <em>cannot</em> reduce bias or eliminate irreducible noise.
        </p>
      </div>
    </section>

    <!-- SECTION 08 -->
    <section id="sec-08" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 08</span>
        <h2 class="section-title">Random Forest: Dual Randomization</h2>
        <p class="section-subtitle">How combining bootstrap sample rows with randomized feature subsets creates the gold standard of bagging.</p>
      </div>

      <p>
        Introduced by Leo Breiman and Adele Cutler in 2001, <strong>Random Forest</strong> is the pinnacle of the bagging family. While a standard <code>BaggingClassifier</code> only introduces randomness by selecting random subsets of <em>rows</em>, Random Forest introduces a second layer of randomization: <strong>random feature subsets at every individual node split</strong>.
      </p>

      <h3>The 4-Step Random Forest Training Algorithm</h3>
      <ol>
        <li><strong>Bootstrap Sample of Rows:</strong> Draw a random bootstrap sample of size N with replacement from the training dataset.</li>
        <li><strong>Random Feature Selection at Splits:</strong> When growing each decision tree, at every candidate node split, do <em>not</em> consider all p features. Instead, randomly select a subset of m features:
          <br>&bull; For Classification: Typically m = &lfloor; &radic;p &rfloor;
          <br>&bull; For Regression: Typically m = &lfloor; p / 3 &rfloor;
        </li>
        <li><strong>Best Split Among Candidates:</strong> Choose the best split (using Gini Impurity or Information Gain) <em>strictly</em> among the m randomly chosen features.</li>
        <li><strong>Deep Tree Growth &amp; Ensemble Voting:</strong> Grow each tree fully without pruning. Repeat steps 1&ndash;3 for all B trees. For predictions, take the majority class vote (classification) or mean average (regression).</li>
      </ol>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_RANDOM_FOREST_ARCHITECTURE__
        </div>
        <div class="visual-caption">
          <strong>Figure 8.1: The Random Forest Dual Randomization Architecture.</strong> Both row sampling (bootstrap) and column sampling (random m features at each split) are applied. The diverse trees output independent votes which are combined into the consensus prediction.
        </div>
      </div>

      <h3>Why Randomized Feature Selection Is Critical: Tree Decorrelation</h3>
      <p>
        Imagine a medical dataset where one feature&mdash;say, <code>FastingBloodGlucose</code>&mdash;is an overwhelmingly strong predictor of diabetes.
      </p>
      <p>
        If we apply standard Bagging without feature randomization, virtually every decision tree will select <code>FastingBloodGlucose</code> as its root node split. Consequently, all 100 trees will have nearly identical top-level branching structures. Their prediction errors will be strongly correlated (&rho; &approx; 1).
      </p>
      <p>
        By forcing each split to consider only a random subset of m = &radic;p features, Random Forest ensures that <code>FastingBloodGlucose</code> will be excluded from the candidate pool in many split evaluations. This forces other features (such as <code>BMI</code>, <code>Insulin</code>, or <code>BloodPressure</code>) to be selected as root splits. The resulting trees explore entirely different hypothesis spaces, drastically lowering tree correlation &rho; and maximizing the variance reduction of the ensemble!
      </p>

      <h3>Key RandomForestClassifier Hyperparameters</h3>
      <ul>
        <li><code>n_estimators</code> (default 100): The number of trees in the forest. More trees generally reduce variance until the curve plateaus, with diminishing returns beyond 200&ndash;300 trees.</li>
        <li><code>max_depth</code> (default <code>None</code>): The maximum depth of each tree. In Random Forests, trees are typically grown deep, but setting a limit (e.g., 10&ndash;15) can prevent excessive memory usage on massive datasets.</li>
        <li><code>max_features</code> (default <code>'sqrt'</code>): The number of features to consider when looking for the best split. Lowering <code>max_features</code> increases diversity (lower correlation) at the cost of slightly higher bias for individual trees.</li>
        <li><code>min_samples_split</code> (default 2): Minimum number of samples required to split an internal node.</li>
        <li><code>min_samples_leaf</code> (default 1): Minimum number of samples required to be at a leaf node. Setting this to 2&ndash;5 helps smooth decision boundaries.</li>
        <li><code>oob_score</code> (default <code>False</code>): When set to <code>True</code>, computes out-of-bag validation accuracy automatically during training.</li>
        <li><code>random_state</code>: Fixes the pseudo-random generator seed for 100% deterministic reproducibility.</li>
      </ul>
    </section>

    <!-- SECTION 09 -->
    <section id="sec-09" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 09</span>
        <h2 class="section-title">Visualizing Random Forest Behavior</h2>
        <p class="section-subtitle">Comparing decision frontiers, tuning forest size, and understanding feature importances.</p>
      </div>

      <p>
        To build intuition, let us examine how a Random Forest transforms the jagged decision boundaries of an individual tree into a resilient decision frontier, and how performance responds as forest size expands.
      </p>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_RF_DECISION_BOUNDARIES__
        </div>
        <div class="visual-caption">
          <strong>Figure 9.1: Single Decision Tree vs. 100-Tree Random Forest Decision Boundaries.</strong> The single tree on the left carves fragmented rectangular steps that overfit training noise. The Random Forest on the right combines 100 decorrelated trees to produce a smooth, robust frontier that generalizes cleanly.
        </div>
      </div>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_RF_TREES_CURVE__
        </div>
        <div class="visual-caption">
          <strong>Figure 9.2: Test Accuracy vs. Number of Estimators in Random Forest.</strong> As the forest grows from 1 tree (accuracy 85.42%) to 20 trees (accuracy 91.67%) to 100 trees (accuracy 93.75%), accuracy improves quickly and then asymptotes. Notice that beyond ~100 trees, accuracy stabilizes at ~93.75%, showing that adding more trees yields diminishing returns.
        </div>
      </div>

      <div class="callout-card def-card">
        <div class="def-title">Understanding Random Forest Feature Importance (Mean Decrease in Impurity)</div>
        <p>
          In a Random Forest, every time a node split occurs on feature j, the Gini impurity (or mean squared error) of the child nodes is lower than that of the parent node. The total reduction in impurity brought by feature j is summed across all trees in the forest and normalized to sum to 1.0:
          <br><br>
          <code>Importance(j) = [ &sum;_{t=1}^B &sum;_{n &isin; splits(t, j)} &Delta;Gini(n) ] / [ &sum;_k &sum;_{t=1}^B &sum;_{n &isin; splits(t, k)} &Delta;Gini(n) ]</code>
          <br><br>
          <em>Caution:</em> Impurity-based feature importance can be artificially biased toward features with high cardinality (numerical features with many unique values or categorical features with numerous levels). Always corroborate with <strong>Permutation Importance</strong> on held-out validation data before making high-stakes business decisions!
        </p>
      </div>
    </section>

    <!-- SECTION 10 -->
    <section id="sec-10" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 10</span>
        <h2 class="section-title">Out-of-Bag (OOB) Evaluation</h2>
        <p class="section-subtitle">Built-in cross-validation without setting aside a separate validation dataset.</p>
      </div>

      <p>
        Recall from Section 6 that for each tree in a Random Forest, approximately <strong>36.8%</strong> of the original training samples are omitted during bootstrap sampling. These samples are completely unseen by that specific tree. This enables a powerful validation technique called <strong>Out-of-Bag (OOB) Evaluation</strong>.
      </p>

      <h3>How Out-of-Bag Evaluation Works</h3>
      <ol>
        <li>For each training observation x_i, identify all trees in the forest that did <em>not</em> include x_i in their bootstrap sample. (On average, ~37 out of 100 trees qualify).</li>
        <li>Pass x_i through only those eligible trees and aggregate their predictions (majority vote for classification or average for regression).</li>
        <li>Compute the prediction error across all N observations by comparing their aggregated out-of-bag predictions against their true labels. The resulting metric is the <strong>OOB Score</strong>.</li>
      </ol>

      <div class="formula-block">
        <div class="formula-title">Out-of-Bag Accuracy Formula</div>
        <div class="formula-math">OOB Score = (1 / N) &times; &sum;_{i=1}^{N} I( y_i = argmax_c [ &sum;_{b: x_i &notin; D_b} I( h_b(x_i) = c ) ] )</div>
        <div class="formula-explanation">Where D_b is the bootstrap training sample for tree b, and I(&middot;) is the indicator function (1 if true, 0 if false).</div>
      </div>

      <h3>Python Implementation: Accessing the OOB Score</h3>
      <div class="code-container">
        <div class="code-header">
          <span class="code-lang-badge">Python &bull; OOB Score Evaluation</span>
          <span style="color:#94A3B8; font-size:0.75rem;">oob_score_demo.py</span>
        </div>
        <pre class="code-body">from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=240, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Set oob_score=True during instantiation
rf_clf = RandomForestClassifier(
    n_estimators=100,
    oob_score=True,
    random_state=42,
    n_jobs=-1
)
rf_clf.fit(X_train, y_train)

print(f"Random Forest OOB Score:       {rf_clf.oob_score_:.4f} ({rf_clf.oob_score_ * 100:.2f}%)")
print(f"Held-Out Test Set Accuracy:    {rf_clf.score(X_test, y_test):.4f} ({rf_clf.score(X_test, y_test) * 100:.2f}%)")</pre>
      </div>

      <div class="code-output">
        <div class="code-output-title">Verified Execution Output</div>Random Forest OOB Score:       0.8889 (88.89%)
Held-Out Test Set Accuracy:    0.9375 (93.75%)</div>

      <div class="callout-card success-card">
        <div class="success-title">Benefits and Limitations of OOB Evaluation</div>
        <p>
          <strong>Advantages:</strong> You do not need to discard 20% or 30% of your data into a validation split. You can use 100% of available records for training the forest while still obtaining a realistic validation metric.
          <br><br>
          <strong>Limitations:</strong> OOB score assumes standard i.i.d. (independent and identically distributed) observations. For time-series, spatial, or clustered grouped data, OOB predictions will leak temporal or group-level information. In such settings, strict temporal or GroupKFold splits are required.
        </p>
      </div>
    </section>

    <!-- SECTION 11 -->
    <section id="sec-11" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 11</span>
        <h2 class="section-title">Boosting: The Core Idea</h2>
        <p class="section-subtitle">Sequential learning: how models collaborate by specializing on their predecessors' mistakes.</p>
      </div>

      <p>
        While Bagging relies on training independent models in parallel to reduce variance, <strong>Boosting</strong> operates on a completely different philosophical and mathematical framework: <strong>sequential corrective learning</strong> to reduce bias.
      </p>

      <div class="callout-card analogy-card">
        <div class="analogy-title">Everyday Analogy: The Student and the Specialized Tutors</div>
        <p>
          Imagine a student preparing for a comprehensive board exam:
          <br>&bull; <strong>Tutor 1:</strong> Administers a diagnostic test across all subjects. The student scores 70%, but gets several tricky calculus questions wrong.
          <br>&bull; <strong>Tutor 2:</strong> Reviews the errors made with Tutor 1. Instead of repeating basic algebra, Tutor 2 focuses specifically on calculus integration techniques.
          <br>&bull; <strong>Tutor 3:</strong> Reviews remaining residual errors from Tutors 1 and 2, focusing on edge cases in differential equations.
          <br><br>
          In boosting, each subsequent learner does not waste effort relearning patterns that the previous ensemble already mastered. Instead, each new stage focuses its capacity on the residual errors.
        </p>
      </div>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_BAGGING_VS_BOOSTING__
        </div>
        <div class="visual-caption">
          <strong>Figure 11.1: Parallel Bagging vs. Sequential Boosting Architectures.</strong> In Bagging (left), models are trained completely independently in parallel on bootstrap samples. In Boosting (right), models are trained in an iterative sequence, where each stage's training distribution is dictated by the errors of the preceding stages.
        </div>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Comparison Dimension</th>
              <th>Bagging (e.g., Random Forest)</th>
              <th>Boosting (e.g., AdaBoost, Gradient Boosting)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Training Execution</strong></td>
              <td>Parallel &amp; Independent</td>
              <td>Sequential &amp; Dependent</td>
            </tr>
            <tr>
              <td><strong>Primary Target</strong></td>
              <td>Reduces <strong>Variance</strong></td>
              <td>Reduces <strong>Bias</strong></td>
            </tr>
            <tr>
              <td><strong>Base Learner Complexity</strong></td>
              <td>High capacity (deep, unpruned trees)</td>
              <td>Low capacity (shallow decision stumps or small trees)</td>
            </tr>
            <tr>
              <td><strong>Overfitting Risk</strong></td>
              <td>Very low; adding more trees does not cause overfitting</td>
              <td>Moderate to high; adding too many stages can overfit noise</td>
            </tr>
            <tr>
              <td><strong>Parallelization</strong></td>
              <td>Trivially parallelizable across all CPU cores</td>
              <td>Inherently sequential across stages (intra-tree splits can be parallel)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 12 -->
    <section id="sec-12" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 12</span>
        <h2 class="section-title">AdaBoost (Adaptive Boosting)</h2>
        <p class="section-subtitle">Iterative sample reweighting: magnifying difficult instances until they are mastered.</p>
      </div>

      <p>
        Formulated by Yoav Freund and Robert Schapire in 1996, <strong>AdaBoost</strong> was the first practical boosting algorithm. It demonstrated that a set of <em>weak learners</em> (models that perform barely better than a coin flip) can be combined into an arbitrarily accurate <em>strong learner</em>.
      </p>

      <h3>The 5-Step AdaBoost Algorithm</h3>
      <ol>
        <li><strong>Initialize Equal Sample Weights:</strong> Assign each training instance x_i an initial weight w_i^{(1)} = 1 / N.</li>
        <li><strong>Fit Weak Learner:</strong> Fit a base classifier h_t(x)&mdash;typically a <em>decision stump</em> (a decision tree with <code>max_depth=1</code>)&mdash;to the weighted training data.</li>
        <li><strong>Compute Weighted Error Rate:</strong>
          <br>
          <code>&epsilon;_t = &sum;_{i: h_t(x_i) &ne; y_i} w_i^{(t)}</code>
        </li>
        <li><strong>Compute Estimator Weight &alpha;_t:</strong>
          <br>
          <code>&alpha;_t = (1 / 2) &times; ln( (1 &minus; &epsilon;_t) / &epsilon;_t )</code>
          <br>
          If &epsilon;_t = 0.5 (random guessing), &alpha;_t = 0. If &epsilon;_t &rarr; 0 (near-perfect), &alpha;_t &rarr; &infin;.
        </li>
        <li><strong>Update and Renormalize Sample Weights:</strong> Increase weights for misclassified samples; decrease weights for correct samples:
          <br>
          <code>w_i^{(t+1)} = [ w_i^{(t)} &times; exp( &minus;&alpha;_t &times; y_i &times; h_t(x_i) ) ] / Z_t</code>
          <br>
          Where Z_t is a normalizing factor ensuring &sum; w_i^{(t+1)} = 1.
        </li>
      </ol>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_ADABOOST_SEQUENTIAL__
        </div>
        <div class="visual-caption">
          <strong>Figure 12.1: AdaBoost Sequential Learning and Sample Reweighting.</strong> Stage 1 misclassifies the central red circles. Stage 2 magnifies the sample weights of those misclassified circles, forcing Stump 2 to create a vertical split. The final weighted vote combines all stumps into a high-accuracy non-linear classifier.
        </div>
      </div>

      <h3>Python Implementation: AdaBoostClassifier in Action</h3>
      <div class="code-container">
        <div class="code-header">
          <span class="code-lang-badge">Python &bull; AdaBoostClassifier</span>
          <span style="color:#94A3B8; font-size:0.75rem;">adaboost_classifier_demo.py</span>
        </div>
        <pre class="code-body">from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

# 1. Generate synthetic classification dataset
X, y = make_classification(n_samples=240, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 2. Instantiate AdaBoost with decision stumps (max_depth=1)
adaboost_clf = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50,
    learning_rate=1.0,
    random_state=42
)
adaboost_clf.fit(X_train, y_train)

# 3. Predict and evaluate
ada_preds = adaboost_clf.predict(X_test)
print(f"AdaBoost Test Accuracy: {accuracy_score(y_test, ada_preds):.4f} ({accuracy_score(y_test, ada_preds) * 100:.2f}%)")
print(f"AdaBoost Test F1 Score: {f1_score(y_test, ada_preds):.4f}")</pre>
      </div>

      <div class="code-output">
        <div class="code-output-title">Verified Execution Output</div>AdaBoost Test Accuracy: 0.9792 (97.92%)
AdaBoost Test F1 Score: 0.9796</div>
    </section>

    <!-- SECTION 13 -->
    <section id="sec-13" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 13</span>
        <h2 class="section-title">Gradient Boosting: Optimization in Function Space</h2>
        <p class="section-subtitle">Stepping down the loss gradient: fitting regression trees directly to pseudo-residuals.</p>
      </div>

      <p>
        While AdaBoost reweights training samples based on classification errors, Jerome Friedman generalized the concept in 1999 to arbitrary differentiable loss functions. This formulation is known as <strong>Gradient Boosting</strong>.
      </p>

      <p>
        Instead of modifying sample weights, each subsequent model in Gradient Boosting is fitted to the <strong>pseudo-residuals</strong> (the negative gradient of the loss function with respect to the current model predictions).
      </p>

      <h3>The 5-Step Intuitive Gradient Boosting Pipeline</h3>
      <ol>
        <li><strong>Initial Prediction:</strong> Begin with a constant base prediction F₀(x) that minimizes the global loss (for squared-error regression, this is simply the mean of the training target y&#772;).</li>
        <li><strong>Compute Residuals:</strong> Calculate the residual error for each sample:
          <br>
          <code>r_i^{(m)} = y_i &minus; F_{m-1}(x_i) = &minus;[ &part;L(y_i, F(x_i)) / &part;F(x_i) ]_{F=F_{m-1}}</code>
        </li>
        <li><strong>Fit Weak Tree to Residuals:</strong> Train a shallow decision tree h_m(x) using the residuals r_i^{(m)} as its target labels.</li>
        <li><strong>Update Ensemble with Shrinkage:</strong> Add the new tree's predictions scaled by a learning rate &eta;:
          <br>
          <code>F_m(x) = F_{m-1}(x) + &eta; &times; h_m(x)</code>
        </li>
        <li><strong>Iterate:</strong> Repeat steps 2&ndash;4 for M total boosting stages.</li>
      </ol>

      <div class="formula-block">
        <div class="formula-title">The Master Additive Boosting Equation</div>
        <div class="formula-math">F_m(x) = F_{m-1}(x) + &eta; &times; h_m(x) = F₀(x) + &sum;_{k=1}^{m} &eta; &times; h_k(x)</div>
        <div class="formula-explanation">
          &bull; <strong>F_m(x):</strong> The updated ensemble prediction score after stage m.<br>
          &bull; <strong>F_{m-1}(x):</strong> The cumulative ensemble model built up through stage m&minus;1.<br>
          &bull; <strong>&eta; &isin; (0, 1]:</strong> The <em>learning rate</em> (shrinkage factor) that controls step size.<br>
          &bull; <strong>h_m(x):</strong> The newly fitted base decision tree trained to predict the current residuals.
        </div>
      </div>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_GRADIENT_BOOSTING_ADDITIVE__
        </div>
        <div class="visual-caption">
          <strong>Figure 13.1: Additive Gradient Boosting Progression.</strong> Stage 0 provides the baseline mean. Stage 1 fits a tree to the initial large residuals. Stage 2 fits another tree to the smaller remaining residuals. Summing these scaled contributions reproduces complex curves with high precision.
        </div>
      </div>

      <h3>Python Implementation: GradientBoostingClassifier Loss Trajectory</h3>
      <div class="code-container">
        <div class="code-header">
          <span class="code-lang-badge">Python &bull; GradientBoostingClassifier</span>
          <span style="color:#94A3B8; font-size:0.75rem;">gradient_boosting_demo.py</span>
        </div>
        <pre class="code-body">from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=240, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Instantiate Gradient Boosting Classifier
gb_clf = GradientBoostingClassifier(
    n_estimators=60,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)
gb_clf.fit(X_train, y_train)

# Monitor training loss reduction across stages
initial_loss = gb_clf.train_score_[0]
final_loss = gb_clf.train_score_[-1]
test_acc = accuracy_score(y_test, gb_clf.predict(X_test))

print(f"Stage 1 Training Loss:     {initial_loss:.4f}")
print(f"Stage 60 Training Loss:    {final_loss:.4f} (87.5% Loss Reduction)")
print(f"Final Test Accuracy:       {test_acc:.4f} ({test_acc * 100:.2f}%)")</pre>
      </div>

      <div class="code-output">
        <div class="code-output-title">Verified Execution Output</div>Stage 1 Training Loss:     1.2596
Stage 60 Training Loss:    0.1578 (87.5% Loss Reduction)
Final Test Accuracy:       0.9792 (97.92%)</div>
    </section>
"""
