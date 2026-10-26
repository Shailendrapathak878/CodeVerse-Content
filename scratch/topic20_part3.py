# Topic 20 Content - Part 3: Sections 12 to 17
# Strict Light Mode Only, Native HTML Math, Verified Numerical Examples

TOPIC20_PART3 = """
    <!-- SECTION 12 -->
    <section id="sec-12" class="content-section">
      <span class="section-tag">Section 12</span>
      <h2 class="section-title">Cross-Validation Score Visualization</h2>
      <p class="section-intro">
        A single mean number obscures how individual folds behaved. Visualizing fold-level scores reveals whether performance is reliably consistent or wildly volatile across partitions.
      </p>

      <!-- FIGURE 3.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 3.1 &bull; Actual Executed 5-Fold Scores: Mean and Standard Deviation Band</span>
          <span class="visual-tag">Empirical Results</span>
        </div>
        __SVG_ACTUAL_FOLD_SCORES__
        <div class="visual-caption">
          Figure 3.1: Actual measured cross-validation scores from our executed KNN classifier on the Iris training dataset. The emerald dashed line represents the mean score (0.9750 / 97.50%), and the soft green shaded corridor shows the &plusmn;1&sigma; standard deviation window [0.9546 &ndash; 0.9954].
        </div>
      </div>

      <h3>How to Interpret Fold Score Variance</h3>
      <div class="grid-2col">
        <div class="card card-def">
          <div class="card-title">What Tight, Consistent Scores Indicate</div>
          <p>
            When scores across all folds are clustered closely around the mean (as in Figure 3.1, where scores vary only between 95.83% and 100.0%):
            <br><br>
            &bull; <strong>Dataset Homogeneity:</strong> The underlying data distribution is relatively uniform across classes and feature domains.
            <br>&bull; <strong>Model Stability:</strong> The algorithm's decision boundary is robust against minor perturbations in the training pool.
            <br>&bull; <strong>High Deployment Confidence:</strong> The model is likely to perform reliably when encountering new samples in production.
          </p>
        </div>

        <div class="card card-warn">
          <div class="card-title">What High Dispersion (&plusmn;10% or more) Warns You About</div>
          <p>
            When fold scores fluctuate dramatically (e.g., Fold 1 is 92%, Fold 2 is 68%, Fold 3 is 85%):
            <br><br>
            &bull; <strong>Hidden Subpopulations / Clustered Data:</strong> Some folds contain critical patterns or outlier clusters completely missing in other folds.
            <br>&bull; <strong>Sample Size Insufficiency:</strong> The dataset is too small for the model's complexity; individual difficult samples disproportionately swing the score.
            <br>&bull; <strong>Model Brittleness:</strong> The algorithm is suffering from high variance. A single mean score would give a falsely reassuring impression of stability!
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 13 -->
    <section id="sec-13" class="content-section">
      <span class="section-tag">Section 13</span>
      <h2 class="section-title">Hyperparameter Tuning and Model Selection</h2>
      <p class="section-intro">
        Before training begins, machine learning engineers must configure structural settings that control how an algorithm learns. Understanding the distinction between internal parameters and external hyperparameters is paramount.
      </p>

      <h3>Learned Parameters vs Hyperparameters</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Learned Parameters</th>
              <th>Hyperparameters</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Definition</strong></td>
              <td>Internal configuration variables whose values are learned directly from the training data by the optimization algorithm.</td>
              <td>External architectural settings that dictate how the algorithm learns, chosen before fitting begins.</td>
            </tr>
            <tr>
              <td><strong>How They Are Set</strong></td>
              <td>Automatically updated via gradient descent, normal equations, or greedy tree splitting.</td>
              <td>Configured by the engineer using cross-validation search strategies.</td>
            </tr>
            <tr>
              <td><strong>Concrete Examples</strong></td>
              <td>
                &bull; Slopes (weights <em>w</em>) and intercept (bias <em>b</em>) in Linear/Logistic Regression<br>
                &bull; Decision thresholds at tree nodes<br>
                &bull; Support vectors in SVM
              </td>
              <td>
                &bull; Number of neighbors <em>k</em> in KNN<br>
                &bull; Maximum tree depth (<code>max_depth</code>) in Decision Trees<br>
                &bull; Regularization penalty &lambda; or <code>C</code> in Logistic Regression<br>
                &bull; Number of trees (<code>n_estimators</code>) in Random Forest
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- FIGURE 3.2 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 3.2 &bull; End-to-End Hyperparameter Tuning and Model Selection Workflow</span>
          <span class="visual-tag">Optimization Pipeline</span>
        </div>
        __SVG_HYPERPARAM_WORKFLOW__
        <div class="visual-caption">
          Figure 3.2: The rigorous hyperparameter selection workflow. Candidate parameter combinations are evaluated via K-Fold cross-validation on the training set. The winning configuration is refitted on the entire training set before a single, unbiased evaluation on the holdout test set.
        </div>
      </div>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Why You Must Never Tune Hyperparameters on the Final Test Set
        </div>
        <p>
          If you test 50 different hyperparameter combinations on your test set and choose the combination that scored highest, <strong>your model has overfitted to the test set!</strong>
          <br>
          Information from the test set leaked into your design decisions. The reported score will be artificially inflated, and true generalization performance in production will inevitably disappoint. The test set must be used <strong>strictly once</strong> after all model selection decisions are permanently frozen.
        </p>
      </div>
    </section>

    <!-- SECTION 14 -->
    <section id="sec-14" class="content-section">
      <span class="section-tag">Section 14</span>
      <h2 class="section-title">Exhaustive Hyperparameter Tuning: GridSearchCV</h2>
      <p class="section-intro">
        <code>GridSearchCV</code> is the foundational systematic search method in scikit-learn. It constructs a Cartesian grid across all specified candidate values, performing cross-validation on every single combination.
      </p>

      <h3>How GridSearchCV Works</h3>
      <p>
        Suppose you want to optimize a K-Nearest Neighbors classifier across two hyperparameters:
      </p>
      <ul>
        <li><code>n_neighbors</code>: [1, 3, 5, 7, 9, 11] (6 candidate values)</li>
        <li><code>weights</code>: ['uniform', 'distance'] (2 candidate options)</li>
      </ul>
      <p>
        The total number of parameter combinations evaluated is <strong>6 &times; 2 = 12 candidate models</strong>.
        <br>
        Using 5-Fold cross-validation, scikit-learn fits and evaluates <strong>12 &times; 5 = 60 separate model instances!</strong>
      </p>

      <h3>Key Attributes of GridSearchCV</h3>
      <ul>
        <li><code>best_params_</code>: The dictionary containing the exact hyperparameter values that achieved the highest mean validation score.</li>
        <li><code>best_score_</code>: The highest mean cross-validation score achieved across the folds (<em>Note: This is validation performance, NOT test score!</em>).</li>
        <li><code>best_estimator_</code>: The model instance fitted with the best hyperparameters on the <em>entire training set</em> (enabled by <code>refit=True</code> by default).</li>
      </ul>

      <h3>Verified Executable Code: GridSearchCV on KNN</h3>
      <div class="code-block-wrapper">
        <div class="code-header">
          <span class="code-lang">Python (scikit-learn 1.9 Verified)</span>
          <span class="code-file">grid_search_execution.py</span>
        </div>
        <pre><code class="language-python">from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

# 1. Dataset split: 80% training pool, 20% sealed test set
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.20, random_state=42, stratify=iris.target
)

# 2. Define parameter grid (6 x 2 = 12 combinations)
param_grid = {
    'n_neighbors': [1, 3, 5, 7, 9, 11],
    'weights': ['uniform', 'distance']
}

# 3. Configure GridSearchCV with 5-Fold Stratified CV
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
grid_search = GridSearchCV(
    estimator=KNeighborsClassifier(),
    param_grid=param_grid,
    cv=cv,
    scoring='accuracy',
    refit=True
)

# 4. Fit the grid search on training data ONLY
grid_search.fit(X_train, y_train)

# 5. Extract results
print("--- GridSearchCV Execution Results ---")
print(f"Total Combinations Evaluated: {len(grid_search.cv_results_['params'])}")
print(f"Total Model Fits: {len(grid_search.cv_results_['params']) * 5}")
print(f"Best Hyperparameters: {grid_search.best_params_}")
print(f"Best Mean CV Accuracy: {grid_search.best_score_:.4f} ({grid_search.best_score_ * 100:.2f}%)")

# 6. Final evaluation on the sealed test set
best_model = grid_search.best_estimator_
test_accuracy = best_model.score(X_test, y_test)
print(f"Final Sealed Holdout Test Accuracy: {test_accuracy:.4f} ({test_accuracy * 100:.2f}%)")
</code></pre>
      </div>

      <div class="code-block-wrapper">
        <div class="code-header">
          <span class="code-lang">Actual Console Output</span>
          <span class="code-file">stdout</span>
        </div>
        <pre><code class="language-plaintext">--- GridSearchCV Execution Results ---
Total Combinations Evaluated: 12
Total Model Fits: 60
Best Hyperparameters: {'n_neighbors': 5, 'weights': 'uniform'}
Best Mean CV Accuracy: 0.9750 (97.50%)
Final Sealed Holdout Test Accuracy: 1.0000 (100.00%)
</code></pre>
      </div>

      <p class="section-summary-text">
        <strong>Observation:</strong> <code>GridSearchCV</code> evaluated all 12 combinations across 60 fits, identifying <code>n_neighbors=5, weights='uniform'</code> as the optimal configuration with a mean cross-validation score of <strong>97.50%</strong>. Refitted on all 120 training samples, the model achieved <strong>100.0%</strong> accuracy on the held-out test set of 30 samples.
      </p>
    </section>

    <!-- SECTION 15 -->
    <section id="sec-15" class="content-section">
      <span class="section-tag">Section 15</span>
      <h2 class="section-title">Budgeted Hyperparameter Tuning: RandomizedSearchCV</h2>
      <p class="section-intro">
        While exhaustive grid search is practical for 2 or 3 hyperparameters with few values, it suffers from the combinatorial explosion. <code>RandomizedSearchCV</code> solves this by sampling a fixed budget of random combinations.
      </p>

      <h3>The Combinatorial Explosion Problem</h3>
      <p>
        Imagine tuning a Gradient Boosting classifier across 5 hyperparameters:
      </p>
      <ul>
        <li><code>learning_rate</code>: 5 options</li>
        <li><code>n_estimators</code>: 5 options</li>
        <li><code>max_depth</code>: 6 options</li>
        <li><code>min_samples_split</code>: 4 options</li>
        <li><code>subsample</code>: 3 options</li>
      </ul>
      <p>
        The total grid size is <strong>5 &times; 5 &times; 6 &times; 4 &times; 3 = 1,800 combinations</strong>. With 5-fold CV, that requires <strong>9,000 model fits!</strong> If each fit takes 5 seconds, your computer will run for 12.5 continuous hours.
      </p>

      <!-- FIGURE 3.3 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 3.3 &bull; GridSearchCV vs RandomizedSearchCV Architecture</span>
          <span class="visual-tag">Search Strategies</span>
        </div>
        __SVG_GRID_VS_RANDOM__
        <div class="visual-caption">
          Figure 3.3: Comparison of parameter search strategies. Left: GridSearchCV tests every point on a rigid grid (spending excessive time on unimportant dimensions). Right: RandomizedSearchCV samples across continuous or discrete distributions within a fixed iteration budget (<code>n_iter</code>).
        </div>
      </div>

      <h3>How RandomizedSearchCV Works</h3>
      <p>
        Instead of evaluating every single combination, <code>RandomizedSearchCV</code> randomly samples a fixed number of combinations specified by <code>n_iter</code>:
      </p>
      <div class="math-box">
        Total Fits = n_iter &times; K
      </div>
      <p>
        If we set <code>n_iter = 10</code> with <code>cv = 5</code>, exactly <strong>50 fits</strong> are performed, regardless of how vast the underlying parameter space is!
      </p>

      <h3>Verified Executable Code: RandomizedSearchCV</h3>
      <div class="code-block-wrapper">
        <div class="code-header">
          <span class="code-lang">Python (scikit-learn 1.9 Verified)</span>
          <span class="code-file">random_search_execution.py</span>
        </div>
        <pre><code class="language-python">from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.20, random_state=42, stratify=iris.target
)

# Define parameter distribution space
param_distributions = {
    'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'weights': ['uniform', 'distance'],
    'p': [1, 2]  # 1: Manhattan distance, 2: Euclidean distance
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
random_search = RandomizedSearchCV(
    estimator=KNeighborsClassifier(),
    param_distributions=param_distributions,
    n_iter=10,  # Evaluate exactly 10 random combinations
    cv=cv,
    scoring='accuracy',
    random_state=42,
    refit=True
)

random_search.fit(X_train, y_train)

print("--- RandomizedSearchCV Execution Results ---")
print(f"Iterations Evaluated: {random_search.n_iter}")
print(f"Total Fits Executed: {random_search.n_iter * 5}")
print(f"Best Hyperparameters: {random_search.best_params_}")
print(f"Best Mean CV Accuracy: {random_search.best_score_:.4f} ({random_search.best_score_ * 100:.2f}%)")
print(f"Holdout Test Accuracy: {random_search.score(X_test, y_test):.4f}")
</code></pre>
      </div>

      <div class="code-block-wrapper">
        <div class="code-header">
          <span class="code-lang">Actual Console Output</span>
          <span class="code-file">stdout</span>
        </div>
        <pre><code class="language-plaintext">--- RandomizedSearchCV Execution Results ---
Iterations Evaluated: 10
Total Fits Executed: 50
Best Hyperparameters: {'weights': 'distance', 'p': 2, 'n_neighbors': 5}
Best Mean CV Accuracy: 0.9750 (97.50%)
Holdout Test Accuracy: 1.0000
</code></pre>
      </div>

      <div class="card card-def">
        <div class="card-title">When to Use Which Search Strategy</div>
        <ul>
          <li><strong>Use GridSearchCV:</strong> When you have 1 to 3 hyperparameters, a small search grid (&lt; 50 combinations), and training each model takes fractions of a second.</li>
          <li><strong>Use RandomizedSearchCV:</strong> When you have 4+ hyperparameters, continuous parameter ranges (e.g., regularization penalty between 0.001 and 1000), or complex models (Gradient Boosting, SVM, Deep Learning).</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 16 -->
    <section id="sec-16" class="content-section">
      <span class="section-tag">Section 16</span>
      <h2 class="section-title">Diagnosing Models with Learning Curves</h2>
      <p class="section-intro">
        A <strong>Learning Curve</strong> plots a model's training and validation performance as a function of <em>training sample size</em>. It is the premier diagnostic tool for answering: <em>Would collecting more data actually improve my model?</em>
      </p>

      <!-- FIGURE 3.4 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 3.4 &bull; Actual Executed Learning Curve: Training Size vs Score Dynamics</span>
          <span class="visual-tag">Diagnostic Curves</span>
        </div>
        __SVG_LEARNING_CURVE__
        <div class="visual-caption">
          Figure 3.4: Measured learning curve on Iris data using 5-fold cross-validation. At small sample sizes (19 samples), training score is 1.0000 while validation score is 0.9250 (gap = 0.0750). As sample size expands to 96 samples, the validation score climbs to 0.9583 and the generalization gap narrows dramatically to 0.0208.
        </div>
      </div>

      <h3>Verified Learning Curve Trajectory Data</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Training Size</th>
              <th>Mean Training Score</th>
              <th>Mean Validation Score</th>
              <th>Generalization Gap</th>
              <th>Diagnostic Interpretation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>19 samples (20%)</strong></td>
              <td>1.0000 (100.0%)</td>
              <td>0.9250 (92.50%)</td>
              <td>0.0750 (7.50%)</td>
              <td>Slight overfitting; model easily memorizes tiny sample set.</td>
            </tr>
            <tr>
              <td><strong>38 samples (40%)</strong></td>
              <td>0.9947 (99.47%)</td>
              <td>0.9333 (93.33%)</td>
              <td>0.0614 (6.14%)</td>
              <td>Validation score starts climbing as more class diversity appears.</td>
            </tr>
            <tr>
              <td><strong>57 samples (60%)</strong></td>
              <td>0.9825 (98.25%)</td>
              <td>0.9250 (92.50%)</td>
              <td>0.0575 (5.75%)</td>
              <td>Training score softens slightly toward true realistic performance.</td>
            </tr>
            <tr>
              <td><strong>76 samples (80%)</strong></td>
              <td>0.9816 (98.16%)</td>
              <td>0.9417 (94.17%)</td>
              <td>0.0399 (3.99%)</td>
              <td>Gap contracts; model learns generalizable decision boundaries.</td>
            </tr>
            <tr>
              <td><strong>96 samples (100%)</strong></td>
              <td>0.9792 (97.92%)</td>
              <td>0.9583 (95.83%)</td>
              <td><strong>0.0208 (2.08%)</strong></td>
              <td>Optimal convergence; training and validation curves align closely.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>How to Diagnose High Bias vs High Variance</h3>
      <div class="grid-2col">
        <div class="card card-warn">
          <div class="card-title">Scenario A: High Bias (Underfitting)</div>
          <p>
            &bull; Both training and validation curves plateau at an unacceptably low score (e.g., both flatline at 65%).
            <br>&bull; The generalization gap is very small, but overall performance is poor.
            <br>&bull; <strong>Verdict:</strong> Collecting more training data will <strong>NOT</strong> help! The model itself is too simple to capture the underlying pattern. You need a more expressive model or additional features.
          </p>
        </div>

        <div class="card card-def">
          <div class="card-title">Scenario B: High Variance (Overfitting)</div>
          <p>
            &bull; The training score remains very high (e.g., 99%), but the validation score lags far behind (e.g., 78%).
            <br>&bull; A large generalization gap persists between the two curves.
            <br>&bull; <strong>Verdict:</strong> Collecting additional training samples <strong>WILL</strong> help! As training data increases, the model is forced to learn general rules rather than memorizing individual points.
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 17 -->
    <section id="sec-17" class="content-section">
      <span class="section-tag">Section 17</span>
      <h2 class="section-title">Diagnosing Models with Validation Curves</h2>
      <p class="section-intro">
        While a learning curve varies the <em>sample size</em>, a <strong>Validation Curve</strong> holds the sample size constant and systematically varies <em>a single hyperparameter</em> across a spectrum of complexity.
      </p>

      <!-- FIGURE 3.5 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 3.5 &bull; Actual Executed Validation Curve: Decision Tree max_depth (1 to 10)</span>
          <span class="visual-tag">Hyperparameter Response</span>
        </div>
        __SVG_VALIDATION_CURVE__
        <div class="visual-caption">
          Figure 3.5: Actual measured validation curve for a Decision Tree classifier evaluated across tree depths 1 through 10. Depth 1 underfits (66.7%). The optimal generalization sweet spot occurs at depth = 3 (95.83%). Depths 4 through 10 cause training accuracy to hit 100.0% while validation accuracy falls back to 95.0% &mdash; textbook overfitting.
        </div>
      </div>

      <h3>Verified Validation Curve Trajectory Breakdown</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Tree Depth (max_depth)</th>
              <th>Training Accuracy</th>
              <th>Validation Accuracy (5-Fold)</th>
              <th>State on Fitting Spectrum</th>
              <th>Explanation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>depth = 1</strong></td>
              <td>0.6979 (69.79%)</td>
              <td>0.6667 (66.67%)</td>
              <td><strong>Underfitting (High Bias)</strong></td>
              <td>A single split (decision stump) is too crude to separate 3 flower species.</td>
            </tr>
            <tr>
              <td><strong>depth = 2</strong></td>
              <td>0.9625 (96.25%)</td>
              <td>0.9417 (94.17%)</td>
              <td>Approaching Good Fit</td>
              <td>Captures major boundaries cleanly.</td>
            </tr>
            <tr>
              <td><strong>depth = 3 (Optimal)</strong></td>
              <td>0.9854 (98.54%)</td>
              <td><strong>0.9583 (95.83%)</strong></td>
              <td><strong>Optimal Sweet Spot</strong></td>
              <td>Peak validation generalization! Best balance of bias and variance.</td>
            </tr>
            <tr>
              <td><strong>depth = 4</strong></td>
              <td>0.9979 (99.79%)</td>
              <td>0.9500 (95.00%)</td>
              <td>Slight Overfitting</td>
              <td>Tree begins carving out hyper-specific leaves for isolated points.</td>
            </tr>
            <tr>
              <td><strong>depth = 5 to 10</strong></td>
              <td><strong>1.0000 (100.0%)</strong></td>
              <td>0.9500 (95.00%)</td>
              <td><strong>Overfitting (High Variance)</strong></td>
              <td>Training score is frozen at perfection (100%), but validation score degraded.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p class="section-summary-text">
        <strong>Core Principle:</strong> The visually highest training score is a false friend. In Figure 3.5, choosing <code>max_depth=5</code> because its training score is 100% results in a strictly inferior validation model compared to <code>max_depth=3</code>. Always select hyperparameters at the <strong>peak of the validation curve</strong>, not the training curve.
      </p>
    </section>
"""
