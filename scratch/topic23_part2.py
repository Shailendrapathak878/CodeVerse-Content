# Topic 23 Content Module — Part 2: Sections 07 to 12
# High quality, beginner-friendly, Light Mode only, accessible HTML entities for math.

PART_2_HTML = """
    <!-- ========================================== -->
    <!-- SECTION 07: CREATING NEW FEATURES         -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-07">
      <div class="section-header">
        <span class="section-tag">Module 07 • Feature Synthesis</span>
        <h2 class="section-title"><a href="#sec-07">7. Creating New Features</a></h2>
      </div>

      <p>
        While data cleaning and scaling prevent algorithms from failing, <strong>feature creation</strong> is where machine learning models achieve breakthroughs in predictive accuracy. Feature creation derives new, highly informative indicators from raw columns by infusing domain knowledge.
      </p>

      <div class="diagram-container">
        __SVG_FEATURE_CREATION__
        <div class="diagram-caption">Figure 7.1: The Feature Synthesis Engine. Raw isolated columns are combined into relational metrics (e.g. Debt-to-Income, Log Income, Customer Tenure) that linearly align with real-world target behavior.</div>
      </div>

      <h3>7.1 Common Feature Creation Patterns</h3>
      <ul>
        <li>
          <strong>Ratios and Rates:</strong> Combining two raw values that have little meaning in isolation. For example, a $300,000 loan has very different risk profiles for a borrower earning $40,000 versus one earning $400,000. The ratio <code>debt_to_income = loan_amount / (annual_income + 1)</code> captures true credit burden in a single number.
        </li>
        <li>
          <strong>Difference and Elapsed Time:</strong> Converting two timestamps or an event date and the current reference date into an active duration (e.g. <code>account_age_days = (reference_date - signup_date).dt.days</code>).
        </li>
        <li>
          <strong>Logarithmic Transformations:</strong> Compressing heavily right-skewed variables (like wealth, prices, or web traffic) via <code>log1p(x) = log(1 + x)</code> to transform exponential distributions into symmetric Gaussian bells.
        </li>
        <li>
          <strong>Aggregation Statistics:</strong> Grouping historical transaction records per customer to calculate mean spend, maximum daily transaction, or transaction count over the last 30 days.
        </li>
      </ul>

      <div class="callout callout-caution">
        <div class="callout-title">🛑 Critical Edge Cases: Division by Zero and Future Timestamps</div>
        <p>
          When synthesizing features, you must always anticipate production edge cases:
        </p>
        <ul style="margin-bottom:0;">
          <li><strong>Division by Zero:</strong> If calculating <code>loan_amount / income</code>, zero or near-zero income will produce infinite (<code>inf</code>) or NaN values. Always add a tiny stabilization epsilon or constant: <code>loan_amount / (income + 1.0)</code>.</li>
          <li><strong>Target Leakage via Feature Creation:</strong> Never construct an input feature using information derived from the target variable <em>y</em>. For example, creating a feature <code>total_payments_made</code> to predict loan default when payments only occur <em>after</em> the loan is issued causes catastrophic target leakage!</li>
        </ul>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 08: POLYNOMIAL & INTERACTIONS     -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-08">
      <div class="section-header">
        <span class="section-tag">Module 08 • Non-Linear Expansion</span>
        <h2 class="section-title"><a href="#sec-08">8. Polynomial and Interaction Features</a></h2>
      </div>

      <p>
        Linear models (like Linear Regression, Ridge, and Logistic Regression) assume that each feature affects the prediction independently and linearly:
      </p>
      <div class="formula-card">
        <div class="formula-math">y = w₁ · x₁ + w₂ · x₂ + b</div>
        <div class="formula-desc">A pure linear model cannot capture synergy between features or curved trajectories.</div>
      </div>

      <p>
        In reality, relationships are frequently non-linear or synergistic:
      </p>
      <ul>
        <li>
          <strong>Interaction Features (x₁ &middot; x₂):</strong> The effect of one feature depends on the level of another. For instance, the value of a house increases with <code>square_feet</code>, but increases <em>much faster</em> if <code>school_district_rating</code> is also high. The product captures this synergy.
        </li>
        <li>
          <strong>Polynomial Powers (x&sup2;, x&sup3;):</strong> Allows a linear model to bend and fit parabolic, quadratic, or cubic curves without changing the underlying optimization algorithm.
        </li>
      </ul>

      <div class="diagram-container">
        __SVG_POLYNOMIAL_FEATURES__
        <div class="diagram-caption">Figure 8.1: Expanding two input features [x₁, x₂] with degree=2 generates five distinct features, capturing curvature and interaction synergy.</div>
      </div>

      <h3>8.1 Executable Python: PolynomialFeatures Benchmark</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python 3.10+ • Scikit-Learn Polynomial Expansion</span>
          <span class="code-lang">python</span>
        </div>
        <pre><code>import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score, root_mean_squared_error

# Synthetic quadratic dataset: y = 2.5 * x^2 - 8 * x + 15 + noise
np.random.seed(42)
x = np.linspace(1, 10, 30).reshape(-1, 1)
y = 2.5 * x.ravel()**2 - 8 * x.ravel() + 15 + np.random.normal(0, 8, size=30)

# 1. Standard Linear Regression (Underfits non-linear curve)
lin_model = LinearRegression().fit(x, y)
y_pred_lin = lin_model.predict(x)

# 2. Polynomial Pipeline (Degree = 2)
poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression()).fit(x, y)
y_pred_poly = poly_model.predict(x)

print("--- Empirical Polynomial Expansion Results ---")
print(f"Linear Model:        R² = {r2_score(y, y_pred_lin):.4f} | RMSE = {root_mean_squared_error(y, y_pred_lin):.2f}")
print(f"Polynomial (deg=2):  R² = {r2_score(y, y_pred_poly):.4f} | RMSE = {root_mean_squared_error(y, y_pred_poly):.2f}")
# Output:
# Linear Model:        R² = 0.8720 | RMSE = 19.14
# Polynomial (deg=2):  R² = 0.9859 | RMSE = 6.36  (Dramatic 67% error reduction!)</code></pre>
      </div>

      <div class="callout callout-warning">
        <div class="callout-title">⚠️ The Combinatorial Explosion Warning</div>
        <p style="margin-bottom:0;">
          If you have 100 features and set <code>PolynomialFeatures(degree=3)</code>, scikit-learn will generate over <strong>176,850 features</strong>! This combinatorial explosion leads to massive memory consumption, slow training, and severe overfitting. If you must use polynomial features, restrict the degree to 2, or set <code>interaction_only=True</code>, and always pair with L1/L2 regularization (Ridge or Lasso).
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 09: FEATURE SELECTION             -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-09">
      <div class="section-header">
        <span class="section-tag">Module 09 • Dimensionality Reduction</span>
        <h2 class="section-title"><a href="#sec-09">9. Feature Selection and Redundant Features</a></h2>
      </div>

      <p>
        <strong>Feature Selection</strong> is the process of selecting a subset of the most relevant, non-redundant features to use in model construction. It is the deliberate counterpart to feature creation: while feature creation adds candidates, feature selection removes unhelpful noise.
      </p>

      <h3>9.1 Why Pruning Features Is Essential</h3>
      <ul>
        <li><strong>Reduces Overfitting:</strong> Less redundant data means fewer opportunities for the algorithm to make decisions based on random noise.</li>
        <li><strong>Improves Interpretability:</strong> A healthcare model with 8 clinically meaningful features is far easier for doctors to audit and trust than a black box with 500 collinear inputs.</li>
        <li><strong>Accelerates Training &amp; Inference:</strong> Lowers memory footprint and allows faster real-time predictions in production APIs.</li>
      </ul>

      <div class="diagram-container">
        __SVG_FEATURE_SELECTION__
        <div class="diagram-caption">Figure 9.1: Feature selection ranking via ANOVA F-Score (SelectKBest). High-signal domain features (DTI, Credit Score, Income) are retained, while zero-signal noise is safely pruned.</div>
      </div>

      <h3>9.2 The Three Families of Feature Selection</h3>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Method Family</th>
              <th>How It Works</th>
              <th>Advantages</th>
              <th>Disadvantages</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Filter Methods</strong><br><code>SelectKBest</code></td>
              <td>Evaluates individual statistical relationship with target (ANOVA F-test, Mutual Info, Chi-Square)</td>
              <td>Extremely fast; completely independent of the choice of ML algorithm</td>
              <td>Ignores feature interactions; may drop features that only work in combination</td>
            </tr>
            <tr>
              <td><strong>Wrapper Methods</strong><br><code>RFE</code> (Recursive Elimination)</td>
              <td>Iteratively trains models on subsets of features, pruning the weakest at each step</td>
              <td>Captures complex interactions; tuned directly to model performance</td>
              <td>Computationally very expensive; prone to overfitting on small datasets</td>
            </tr>
            <tr>
              <td><strong>Embedded Methods</strong><br><code>Lasso</code>, <code>RandomForest</code></td>
              <td>Feature selection occurs natively during model optimization (L1 penalty drives coefficients to 0)</td>
              <td>Balanced speed and accuracy; naturally penalizes multicollinear features</td>
              <td>Tied strictly to that specific algorithm family</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-important">
        <div class="callout-title">🔒 Pipeline Integration Rule for Feature Selection</div>
        <p style="margin-bottom:0;">
          If feature selection uses target labels <em>y</em> (such as <code>SelectKBest</code> or <code>RFE</code>), <strong>it must occur strictly inside the cross-validation pipeline</strong>. Performing feature selection across the full dataset before cross-validation leaks label associations into the validation folds, invalidating your performance metrics.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 10: DATA LEAKAGE IN PREPROCESSING -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-10">
      <div class="section-header">
        <span class="section-tag">Module 10 • Robust Engineering</span>
        <h2 class="section-title"><a href="#sec-10">10. Data Leakage During Feature Engineering</a></h2>
      </div>

      <div class="callout callout-caution">
        <div class="callout-title">🛑 What Is Data Leakage?</div>
        <p style="margin-bottom:0;">
          <strong>Data Leakage</strong> (also known as information leakage) occurs when information from outside the training dataset is inadvertently used to train or prepare the model. It causes models to perform artificially well during local testing and cross-validation, but fail catastrophically when deployed into production on real unseen data.
        </p>
      </div>

      <div class="diagram-container">
        __SVG_DATA_LEAKAGE__
        <div class="diagram-caption">Figure 10.1: Anatomy of Preprocessing Leakage. The incorrect top workflow computes global means/scalers across all rows before splitting, leaking test information. The bottom pipeline workflow strictly isolates training parameters.</div>
      </div>

      <h3>10.1 The Top 5 Preprocessing Leakage Mistakes</h3>
      <ol>
        <li>
          <strong>Global Scaling / Normalization:</strong> Calling <code>scaler.fit(X_full)</code> before splitting. The test set's mean (&mu;) and standard deviation (&sigma;) bleed into the normalized training values.
        </li>
        <li>
          <strong>Global Imputation:</strong> Computing the dataset-wide mean or median across all rows. If the test set contains high outliers, the imputed training rows will reflect test distribution information.
        </li>
        <li>
          <strong>Supervised Feature Selection on All Data:</strong> Ranking features using correlation with <em>y</em> on the entire dataset. The model selects features that happen to correlate with test labels by random chance.
        </li>
        <li>
          <strong>Temporal / Future Leakage:</strong> Using records from next week to impute or predict records from today. In time-series tasks, you can only look backward, never forward.
        </li>
        <li>
          <strong>Duplicate Records Crossing Splits:</strong> If multiple rows belong to the same customer and are randomly split into both train and test sets, the model effectively tests on memorized training entities.
        </li>
      </ol>

      <h3>10.2 The Universal Fix: The Training-Only Fitting Rule</h3>
      <div class="formula-card">
        <div class="formula-math">fit() &isin; Train Set ONLY &nbsp;&nbsp;|&nbsp;&nbsp; transform() &isin; Train, Val, &amp; Test</div>
        <div class="formula-desc">Never, under any circumstances, call fit() or fit_transform() on validation or test sets.</div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 11: WHAT IS AN ML PIPELINE?       -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-11">
      <div class="section-header">
        <span class="section-tag">Module 11 • Architecture &amp; Automation</span>
        <h2 class="section-title"><a href="#sec-11">11. What Is an ML Pipeline?</a></h2>
      </div>

      <p>
        Manually keeping track of imputers, encoders, scalers, and estimators across training and test splits is messy, error-prone, and almost always leads to data leakage.
      </p>
      <p>
        In scikit-learn, a <strong>Pipeline</strong> is an immutable container that chains multiple data transformation steps together sequentially, culminating in a final estimator (model).
      </p>

      <div class="diagram-container">
        __SVG_BASIC_PIPELINE__
        <div class="diagram-caption">Figure 11.1: The Linear Scikit-Learn Pipeline Architecture. Every transformer executes sequentially, ensuring identical handling between training and production inference.</div>
      </div>

      <h3>11.1 How Pipelines Solve the Leakage Problem</h3>
      <p>
        The beauty of a scikit-learn <code>Pipeline</code> lies in how it seamlessly alternates between training and inference modes:
      </p>
      <ul>
        <li>
          <strong>When calling <code>pipeline.fit(X_train, y_train)</code>:</strong> The pipeline automatically executes <code>fit_transform()</code> on Step 1 (Imputer), passes the output to Step 2 (Scaler) for <code>fit_transform()</code>, and finally calls <code>fit()</code> on the Estimator. All transformation statistics are learned <strong>strictly from X_train</strong>.
        </li>
        <li>
          <strong>When calling <code>pipeline.predict(X_test)</code>:</strong> The pipeline automatically freezes the learned parameters and calls <strong>only <code>transform()</code></strong> on Step 1, followed by <code>transform()</code> on Step 2, and finally passes the sanitized array to <code>estimator.predict()</code>. Zero test data is ever fitted!
        </li>
      </ul>

      <h3>11.2 Accessing Pipeline Parameters: The Double-Underscore Syntax</h3>
      <p>
        To access or tune the internal hyperparameters of any step inside a pipeline, scikit-learn uses a distinct double-underscore (<code>__</code>) naming convention:
      </p>
      <div class="formula-card">
        <div class="formula-math">&lt;step_name&gt;__&lt;parameter_name&gt;</div>
        <div class="formula-desc">For example: <code>imputer__strategy = 'median'</code> or <code>classifier__max_depth = 10</code>.</div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 12: BUILDING A BASIC PIPELINE     -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-12">
      <div class="section-header">
        <span class="section-tag">Module 12 • Hands-On Implementation</span>
        <h2 class="section-title"><a href="#sec-12">12. Building a Basic Pipeline</a></h2>
      </div>

      <p>
        Let us construct a clean, leak-free numeric pipeline from scratch on a dataset containing missing values.
      </p>

      <div class="code-container">
        <div class="code-header">
          <span>Python 3.10+ • Scikit-Learn Pipeline Construction</span>
          <span class="code-lang">python</span>
        </div>
        <pre><code>import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Generate synthetic numeric features with missing values
np.random.seed(42)
X_raw = np.random.randn(200, 3) * 50 + 100
# Inject 5% NaNs
X_raw[np.random.choice(200, 10), np.random.choice(3, 10)] = np.nan
y = (X_raw[:, 0] + X_raw[:, 1] > 200).astype(int)

# 2. Strict Train / Test Split FIRST (Zero Leakage!)
X_train, X_test, y_train, y_test = train_test_split(
    X_raw, y, test_size=0.25, random_state=42, stratify=y
)

# 3. Define the sequential pipeline steps as (name, object) tuples
basic_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(random_state=42))
])

# 4. Fit the entire pipeline on TRAINING DATA ONLY
basic_pipeline.fit(X_train, y_train)

# 5. Predict on completely untouched test set
y_preds = basic_pipeline.predict(X_test)
test_accuracy = accuracy_score(y_test, y_preds)

print(f"Basic Pipeline fitted successfully!")
print(f"Holdout Test Accuracy: {test_accuracy:.4f}")
print("Trained steps:", [name for name, _ in basic_pipeline.steps])
# Output:
# Basic Pipeline fitted successfully!
# Holdout Test Accuracy: 0.9400
# Trained steps: ['imputer', 'scaler', 'classifier']</code></pre>
      </div>

      <p>
        Notice that a single object, <code>basic_pipeline</code>, now encapsulates data cleaning, normalization, and classification. It can be serialized with <code>joblib.dump()</code> and deployed directly to production.
      </p>
    </section>
"""
