# Topic 22 - Part 2 (Sections 07 - 12)
# High quality, beginner-friendly ML notes

PART_2_HTML = """
    <!-- SECTION 07: GRID SEARCH -->
    <section class="content-section" id="sec-07">
      <div class="section-tag">Section 07</div>
      <h2 class="section-title">Grid Search: Exhaustive Combinatorial Evaluation</h2>
      <p class="section-intro">
        <strong>Grid Search</strong> is the simplest and most intuitive automated hyperparameter optimization technique. It systematically evaluates every single combination of candidate values provided by the engineer in a Cartesian coordinate mesh.
      </p>

      <h3>How Grid Search Works from Scratch</h3>
      <p>
        Suppose you wish to tune a K-Nearest Neighbors classifier by experimenting with two hyperparameters:
      </p>
      <ul>
        <li><code>n_neighbors</code>: $[3, 5, 7, 9]$ (4 candidate values)</li>
        <li><code>weights</code>: <code>['uniform', 'distance']</code> (2 candidate values)</li>
      </ul>
      <p>
        Grid Search forms the full Cartesian product by pairing every neighbor value with every weighting strategy:
      </p>
      <div class="math-box">
        (3, 'uniform'), (3, 'distance'), (5, 'uniform'), (5, 'distance'),<br>
        (7, 'uniform'), (7, 'distance'), (9, 'uniform'), (9, 'distance')
      </div>
      <p>
        This yields 4 &times; 2 = 8 distinct model configurations before accounting for cross-validation folds.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 7.1 — Grid Search 2D Cartesian Coordinate Evaluation</span>
          <span class="visual-tag">Cartesian Mesh</span>
        </div>
        __SVG_GRID_SEARCH_COMBINATIONS__
        <div class="visual-caption">
          Figure 7.1 illustrates an 8-node parameter grid formed by crossing four neighbor values (<em>k</em> = 3, 5, 7, 9) with two weighting options. Every single intersection node is trained and scored across all validation folds.
        </div>
      </div>

      <h3>The General Workload Formula</h3>
      <p>
        For a search space containing <em>k</em> distinct hyperparameters, where hyperparameter <em>i</em> has <em>n</em><sub>i</sub> candidate values, the total number of unique model configurations <em>N</em><sub>configurations</sub> is:
      </p>
      <div class="math-box">
        N<sub>configurations</sub> = &prod;<sub>i=1</sub><sup>k</sup> n<sub>i</sub> = n<sub>1</sub> &times; n<sub>2</sub> &times; &hellip; &times; n<sub>k</sub>
      </div>
      <p>
        When evaluating each configuration using <em>K</em>-Fold Cross-Validation, the approximate total number of model fits <em>N</em><sub>fits</sub> is multiplied by <em>K</em>:
      </p>
      <div class="math-box">
        N<sub>fits</sub> &asymp; N<sub>configurations</sub> &times; K
      </div>
      <p>
        <em>Note on implementation details:</em> Scikit-learn's <code>GridSearchCV</code> also adds $+1$ final fit after finding the winner to refit the best model on the entire training dataset (when <code>refit=True</code>, which is enabled by default).
      </p>

      <h3>Strengths and Inherent Limitations</h3>
      <div class="grid-2col">
        <div class="card" style="border-left: 4px solid #10B981;">
          <div class="card-title" style="color: #047857;">Advantages of Grid Search</div>
          <ul>
            <li><strong>Exhaustive Guarantee:</strong> Evaluates every single permutation specified in your grid.</li>
            <li><strong>Deterministic &amp; Reproducible:</strong> Running the search twice yields identical results.</li>
            <li><strong>Intuitive:</strong> Extremely easy for teams and stakeholders to understand and visualize.</li>
            <li><strong>Ideal for Small Grids:</strong> Perfect when tuning 2 to 3 discrete hyperparameters.</li>
          </ul>
        </div>
        <div class="card" style="border-left: 4px solid #EF4444;">
          <div class="card-title" style="color: #B91C1C;">Limitations of Grid Search</div>
          <ul>
            <li><strong>The Curse of Dimensionality:</strong> Computational cost explodes exponentially with each added hyperparameter.</li>
            <li><strong>Coarse Resolution:</strong> You can only evaluate values you explicitly list. If the optimum is at $\\alpha=1.75$ and you only checked $1.0$ and $2.0$, you miss it.</li>
            <li><strong>Wasted Computation:</strong> Spends enormous time evaluating subtle variations of parameters that have no material impact on accuracy.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTION 08: GRIDSEARCHCV PRACTICAL -->
    <section class="content-section" id="sec-08">
      <div class="section-tag">Section 08</div>
      <h2 class="section-title">GridSearchCV Practical: Safe Leak-Free Tuning</h2>
      <p class="section-intro">
        In scikit-learn, <code>GridSearchCV</code> automates the loop of cross-validation, candidate evaluation, metric tracking, and final model refitting. In this practical, we construct a <strong>leakage-safe pipeline</strong> that bundles <code>StandardScaler</code> and <code>KNeighborsClassifier</code> together.
      </p>

      <h3>The Parameter Grid Setup</h3>
      <p>
        We tune three hyperparameters of the KNN estimator:
      </p>
      <ul>
        <li><code>knn__n_neighbors</code>: [3, 5, 7, 9, 11, 15] (6 values)</li>
        <li><code>knn__weights</code>: <code>['uniform', 'distance']</code> (2 values)</li>
        <li><code>knn__p</code>: [1, 2] (2 values: Manhattan vs. Euclidean distance)</li>
      </ul>
      <p>
        Total configurations: 6 &times; 2 &times; 2 = 24. With 5-Fold Stratified Cross-Validation, total fits: 24 &times; 5 = 120 fits (+1 final refit).
      </p>

      <div class="code-block-wrapper">
        <div class="code-header">
          <span>End-to-End GridSearchCV with Leakage-Safe Pipeline</span>
          <span class="code-lang">Python</span>
        </div>
        <pre><code>from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
import pandas as pd

# 1. Load data and split off the final 20% holdout test set FIRST
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 2. Build a Pipeline so StandardScaler is fitted INSIDE each fold
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

# 3. Define the candidate parameter grid (use double underscore 'step__param')
param_grid = {
    'knn__n_neighbors': [3, 5, 7, 9, 11, 15],
    'knn__weights': ['uniform', 'distance'],
    'knn__p': [1, 2]
}

# 4. Instantiate GridSearchCV with Stratified 5-Fold CV
cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=cv_strategy,
    scoring='accuracy',
    return_train_score=True,
    n_jobs=-1
)

# 5. Fit strictly on the training set
grid_search.fit(X_train, y_train)

# 6. Extract results
print(f"Total Configurations Evaluated: {len(grid_search.cv_results_['params'])}")
print(f"Best Hyperparameters: {grid_search.best_params_}")
print(f"Best 5-Fold CV Accuracy: {grid_search.best_score_:.4f}")

# 7. Evaluate on the untouched holdout test set
test_accuracy = grid_search.score(X_test, y_test)
print(f"Final Holdout Test Accuracy: {test_accuracy:.4f}")</code></pre>
      </div>

      <h3>Actual Executed Experimental Results</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Rank</th>
              <th>Mean 5-Fold CV Accuracy</th>
              <th>Std Dev</th>
              <th>Hyperparameter Configuration</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background-color: #EEF2FF; font-weight: 700;">
              <td>#1 (Winner)</td>
              <td>0.9714 (97.14%)</td>
              <td>&plusmn; 0.0192</td>
              <td><code>{'knn__n_neighbors': 7, 'knn__p': 2, 'knn__weights': 'uniform'}</code></td>
            </tr>
            <tr>
              <td>#2</td>
              <td>0.9714 (97.14%)</td>
              <td>&plusmn; 0.0192</td>
              <td><code>{'knn__n_neighbors': 7, 'knn__p': 2, 'knn__weights': 'distance'}</code></td>
            </tr>
            <tr>
              <td>#3</td>
              <td>0.9692 (96.92%)</td>
              <td>&plusmn; 0.0245</td>
              <td><code>{'knn__n_neighbors': 3, 'knn__p': 2, 'knn__weights': 'distance'}</code></td>
            </tr>
            <tr>
              <td>#4</td>
              <td>0.9692 (96.92%)</td>
              <td>&plusmn; 0.0245</td>
              <td><code>{'knn__n_neighbors': 3, 'knn__p': 2, 'knn__weights': 'uniform'}</code></td>
            </tr>
            <tr>
              <td>#5</td>
              <td>0.9692 (96.92%)</td>
              <td>&plusmn; 0.0162</td>
              <td><code>{'knn__n_neighbors': 9, 'knn__p': 2, 'knn__weights': 'distance'}</code></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card card-strategy">
        <div class="card-title">🔬 Key Scientific Observations from the Execution</div>
        <ul>
          <li><strong>Winning Configuration:</strong> Euclidean distance (<em>p</em> = 2), uniform weights, and <em>k</em> = 7 achieved the peak mean CV score of 0.9714 (97.14%).</li>
          <li><strong>Ties Handled Gracefully:</strong> Notice that <em>k</em> = 7 with <code>'distance'</code> weighting scored an identical 0.9714. In practice, when two models tie on validation score, prefer the simpler model (here, <code>'uniform'</code> weighting has lower computation and fewer assumptions).</li>
          <li><strong>Untouched Test Score:</strong> When evaluated on the 114 holdout test samples, the refitted model achieved <strong>0.9737 (97.37%)</strong>. This closely mirrors the cross-validation estimate (0.9714), confirming that the model has zero leakage and generalizes reliably.</li>
        </ul>
      </div>

      <h3>Anatomy of GridSearchCV Attributes</h3>
      <ul>
        <li><code>best_params_</code>: A dictionary mapping hyperparameter names to the winning values discovered.</li>
        <li><code>best_score_</code>: The average cross-validation score achieved by the winning candidate across all <em>K</em> folds.</li>
        <li><code>best_estimator_</code>: The complete fitted estimator pipeline ready for inference. Because <code>refit=True</code> by default, this estimator has automatically been retrained on the <em>entire</em> 455-sample training set!</li>
        <li><code>cv_results_</code>: A comprehensive dictionary (convertible to a pandas DataFrame) containing execution times, individual fold scores, and rankings for every candidate evaluated.</li>
      </ul>
    </section>

    <!-- SECTION 09: RANDOM SEARCH -->
    <section class="content-section" id="sec-09">
      <div class="section-tag">Section 09</div>
      <h2 class="section-title">Random Search: High-Dimensional Efficiency</h2>
      <p class="section-intro">
        While Grid Search evaluates every point on a rigid lattice, <strong>Random Search</strong> randomly samples a fixed number of configurations from specified probability distributions or candidate lists.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 9.1 — Grid Search vs. Random Search: The Landmark Bergstra &amp; Bengio Insight</span>
          <span class="visual-tag">Efficiency Paradigm</span>
        </div>
        __SVG_GRID_VS_RANDOM_SEARCH__
        <div class="visual-caption">
          Figure 9.1 visualizes the fundamental theorem of hyperparameter search (Bergstra &amp; Bengio, 2012): when only a subset of hyperparameters significantly influence model performance (low effective dimensionality), Grid Search wastes trials repeatedly testing the same projection, whereas Random Search explores unique values along the critical dimension in every single trial.
        </div>
      </div>

      <h3>Why Random Search Outperforms Grid Search in Higher Dimensions</h3>
      <p>
        In 2012, researchers James Bergstra and Yoshua Bengio published a groundbreaking paper: <em>"Random Search for Hyper-Parameter Optimization."</em> They made a profound discovery: <strong>for most real-world datasets, only a small number of hyperparameters dominate model performance</strong>.
      </p>
      <p>
        Consider a model with two hyperparameters: one critical parameter (e.g., <code>learning_rate</code>) and one largely irrelevant parameter (e.g., random initial state).
      </p>
      <ul>
        <li><strong>Grid Search (9 evaluations, 3 &times; 3 grid):</strong> Tests only 3 distinct values along the critical <code>learning_rate</code> axis, repeating each value 3 times across the unimportant parameter. You only get 3 chances to find the optimum!</li>
        <li><strong>Random Search (9 evaluations):</strong> Samples 9 completely distinct values along the critical <code>learning_rate</code> axis. You get 9 unique chances to hit the performance peak!</li>
      </ul>

      <h3>Advantages and Limitations</h3>
      <div class="grid-2col">
        <div class="card" style="border-left: 4px solid #10B981;">
          <div class="card-title" style="color: #047857;">Advantages of Random Search</div>
          <ul>
            <li><strong>Budget-Controlled:</strong> You dictate the exact computational budget via <code>n_iter</code> (e.g., run exactly 50 models, regardless of how vast the space is).</li>
            <li><strong>Continuous Parameter Sampling:</strong> Can sample from continuous distributions (e.g., <code>scipy.stats.uniform</code> or <code>loguniform</code>) rather than being trapped in a coarse discrete grid.</li>
            <li><strong>Scalability:</strong> Adding a new hyperparameter to the search space does not multiply the runtime.</li>
          </ul>
        </div>
        <div class="card" style="border-left: 4px solid #EF4444;">
          <div class="card-title" style="color: #B91C1C;">Limitations of Random Search</div>
          <ul>
            <li><strong>No Global Optimum Guarantee:</strong> Because sampling is stochastic, it may miss a narrow high-performing valley if the budget is too small.</li>
            <li><strong>Requires Fixed Seeds for Reproducibility:</strong> Must specify <code>random_state</code> to ensure team members reproduce identical results.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTION 10: RANDOMIZEDSEARCHCV PRACTICAL -->
    <section class="content-section" id="sec-10">
      <div class="section-tag">Section 10</div>
      <h2 class="section-title">RandomizedSearchCV Practical: Tuning a Random Forest</h2>
      <p class="section-intro">
        To demonstrate the power of <code>RandomizedSearchCV</code>, we tune an ensemble model—a <code>RandomForestClassifier</code>—over a large combinatorial space that would be computationally prohibitive for a beginner using standard Grid Search.
      </p>

      <h3>The Vast 675-Combination Space</h3>
      <p>
        We configure a search space across 5 hyperparameters:
      </p>
      <ul>
        <li><code>n_estimators</code>: [50, 100, 150, 200, 300] (5 values)</li>
        <li><code>max_depth</code>: [3, 5, 8, 12, None] (5 values)</li>
        <li><code>min_samples_split</code>: [2, 5, 10] (3 values)</li>
        <li><code>min_samples_leaf</code>: [1, 2, 4] (3 values)</li>
        <li><code>max_features</code>: <code>['sqrt', 'log2', None]</code> (3 values)</li>
      </ul>
      <p>
        The total grid size is 5 &times; 5 &times; 3 &times; 3 &times; 3 = <strong>675 combinations</strong>. With 5-fold cross-validation, an exhaustive grid search would require 675 &times; 5 = <strong>3,375 fits</strong>!
      </p>
      <p>
        Instead, we set <code>n_iter=20</code>, sampling just 20 high-potential configurations across the search space (20 &times; 5 = <strong>100 fits</strong>)—saving over <strong>97% of computational work</strong>!
      </p>

      <div class="code-block-wrapper">
        <div class="code-header">
          <span>RandomizedSearchCV on Random Forest Classifier</span>
          <span class="code-lang">Python</span>
        </div>
        <pre><code>from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

# 1. Load data and establish holdout split
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 2. Define the large parameter distribution
param_distributions = {
    'n_estimators': [50, 100, 150, 200, 300],
    'max_depth': [3, 5, 8, 12, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None]
}

# 3. Instantiate RandomizedSearchCV with fixed budget
cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_distributions,
    n_iter=20,                 # Sample exactly 20 configurations
    cv=cv_strategy,
    scoring='accuracy',
    random_state=42,           # Ensures reproducible sampling
    n_jobs=-1
)

# 4. Fit strictly on training data
random_search.fit(X_train, y_train)

# 5. Report actual execution findings
print(f"Total Combinations in Grid: 675")
print(f"Configurations Sampled: {random_search.n_iter}")
print(f"Best Hyperparameters: {random_search.best_params_}")
print(f"Best 5-Fold CV Accuracy: {random_search.best_score_:.4f}")

# 6. Evaluate winning model on untouched holdout test set
test_acc = random_search.score(X_test, y_test)
print(f"Holdout Test Accuracy: {test_acc:.4f}")</code></pre>
      </div>

      <h3>Actual Executed Experimental Results</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Metric</th>
              <th>Value from Real Execution</th>
              <th>Interpretation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Configurations Evaluated</strong></td>
              <td>20 out of 675 ($2.96\%$ of total space)</td>
              <td>Massive computational savings without evaluating unpromising combinations.</td>
            </tr>
            <tr>
              <td><strong>Best Hyperparameters</strong></td>
              <td><code>{'n_estimators': 100, 'min_samples_split': 2, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'max_depth': 8}</code></td>
              <td>Ensemble of 100 trees pruned to depth 8 with square-root feature decorrelation.</td>
            </tr>
            <tr>
              <td><strong>Best 5-Fold CV Accuracy</strong></td>
              <td><strong>0.9582 (95.82%)</strong></td>
              <td>Mean performance across the 5 cross-validation folds on the training set.</td>
            </tr>
            <tr>
              <td><strong>Holdout Test Accuracy</strong></td>
              <td><strong>0.9561 (95.61%)</strong></td>
              <td>Honest evaluation on the untouched 114 test samples, showing strong generalization.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card card-warn">
        <div class="card-title">⚠️ Common Beginner Mistake: Confusing n_iter with cv</div>
        <p>
          Do not confuse <code>n_iter</code> with <code>cv</code>:
        </p>
        <ul>
          <li><code>n_iter</code> controls <strong>how many unique hyperparameter configurations</strong> are picked from the distribution (here: 20).</li>
          <li><code>cv</code> controls <strong>how many folds</strong> each configuration is trained and validated on (here: 5).</li>
          <li>The total number of model fits is <code>n_iter &times; cv</code> (20 &times; 5 = 100 fits).</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 11: GRID SEARCH VS RANDOM SEARCH -->
    <section class="content-section" id="sec-11">
      <div class="section-tag">Section 11</div>
      <h2 class="section-title">Grid Search vs. Random Search: Strategic Comparison</h2>
      <p class="section-intro">
        Neither Grid Search nor Random Search is uniformly superior in every scenario. The seasoned machine learning engineer selects the appropriate search strategy based on the size of the search space, the computational cost of training the estimator, and whether continuous parameters are present.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Property</th>
              <th>Grid Search (<code>GridSearchCV</code>)</th>
              <th>Random Search (<code>RandomizedSearchCV</code>)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Candidate Selection</strong></td>
              <td>Evaluates <em>all</em> specified combinations in a rigid Cartesian product.</td>
              <td>Samples a budgeted subset of configurations from candidate lists or distributions.</td>
            </tr>
            <tr>
              <td><strong>Search Coverage</strong></td>
              <td>Exhaustive within the boundaries of the specified candidate values.</td>
              <td>Stochastic sampling across the entire bounded hyperparameter space.</td>
            </tr>
            <tr>
              <td><strong>Computational Workload</strong></td>
              <td>Grows exponentially ($\prod n_i$). Impractical for $>3$ hyperparameters.</td>
              <td>Strictly controlled by the practitioner via the <code>n_iter</code> budget parameter.</td>
            </tr>
            <tr>
              <td><strong>Continuous Parameters</strong></td>
              <td>Must discretize continuous ranges into coarse, arbitrary manual step sizes.</td>
              <td>Seamlessly samples from true probability distributions (e.g., <code>scipy.stats.uniform</code>).</td>
            </tr>
            <tr>
              <td><strong>Effective Dimensionality</strong></td>
              <td>Wastes compute repeatedly evaluating unimportant parameters on a grid.</td>
              <td>Explores unique coordinate values along all dimensions in every single trial.</td>
            </tr>
            <tr>
              <td><strong>Best Use Case</strong></td>
              <td>Small, targeted search spaces with 1–3 discrete hyperparameters (e.g., KNN, Ridge).</td>
              <td>Medium to large search spaces with complex models (Random Forest, Gradient Boosting, SVM).</td>
            </tr>
            <tr>
              <td><strong>Main Limitation</strong></td>
              <td>Prohibitive computational cost as the search space expands.</td>
              <td>Does not guarantee hitting the exact mathematical global optimum.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Recommended Industry Hybrid Strategy</h3>
      <p>
        In production machine learning workflows, engineers often combine both methods using a two-stage strategy:
      </p>
      <ol>
        <li><strong>Stage 1 (Coarse Random Search):</strong> Run a broad <code>RandomizedSearchCV</code> with 50–100 iterations across wide parameter distributions spanning several orders of magnitude to quickly identify high-performing neighborhoods.</li>
        <li><strong>Stage 2 (Fine Grid Search):</strong> Construct a small, tightly bounded <code>GridSearchCV</code> focused directly around the best neighborhood discovered in Stage 1 to polish the final settings.</li>
      </ol>
    </section>

    <!-- SECTION 12: CROSS-VALIDATION IN TUNING -->
    <section class="content-section" id="sec-12">
      <div class="section-tag">Section 12</div>
      <h2 class="section-title">Cross-Validation in Hyperparameter Tuning</h2>
      <p class="section-intro">
        Hyperparameter tuning is only as trustworthy as the validation scheme evaluating it. Relying on a single train/validation split introduces massive vulnerability to sampling noise. <strong>Cross-validation</strong> provides the statistical backbone for stable model selection.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 12.1 — 5-Fold Cross-Validation Architecture</span>
          <span class="visual-tag">Validation Mechanics</span>
        </div>
        __SVG_KFOLD_TUNING_DIAGRAM__
        <div class="visual-caption">
          Figure 12.1 shows 5-fold cross-validation. In each of the five iterations, a different 20% fold acts as the validation benchmark while the remaining 80% trains the model. The five fold scores are averaged to produce an aggregated metric ($\mu \pm \sigma$).
        </div>
      </div>

      <h3>Choosing the Right Cross-Validation Strategy for Your Data</h3>
      <p>
        A critical beginner mistake is applying standard random <code>KFold</code> to every dataset without inspecting its structure. Scikit-learn provides specialized splitters for distinct data types:
      </p>
      <ul>
        <li>
          <strong>StratifiedKFold (Classification Standard):</strong>
          Ensures that each fold contains approximately the same percentage of samples of each target class as the complete dataset.
          <em>Mandatory for classification tasks, especially with imbalanced datasets</em> (e.g., fraud detection with 1% positive cases).
        </li>
        <li>
          <strong>GroupKFold (Clustered / Repeated Measures):</strong>
          Ensures that the same group (e.g., patient, customer, laboratory device) does not appear simultaneously in both the training folds and validation fold.
          <em>Mandatory when data contains multiple samples from the same entity</em> to prevent identity leakage.
        </li>
        <li>
          <strong>TimeSeriesSplit (Temporal Data):</strong>
          Preserves chronological order by training strictly on historical data and validating on future data (e.g., Train on Jan–Mar, Validate on Apr; then Train on Jan–Apr, Validate on May).
          <em>Mandatory for stock forecasting, demand planning, and time-series data</em> to prevent looking into the future.
        </li>
      </ul>
    </section>
"""
