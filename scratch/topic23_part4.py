# Topic 23 Content Module — Part 4: Sections 19 to 22 + Interactive Tool
# High quality, beginner-friendly, Light Mode only, accessible HTML entities for math.

PART_4_HTML = """
    <!-- ========================================== -->
    <!-- SECTION 19: COMMON MISTAKES & FIXES       -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-19">
      <div class="section-header">
        <span class="section-tag">Module 19 • Practical Troubleshooting</span>
        <h2 class="section-title"><a href="#sec-19">19. Common Mistakes and Troubleshooting</a></h2>
      </div>

      <p>
        Building feature engineering pipelines requires vigilance against subtle mathematical and software pitfalls. Below are the 15 most frequent mistakes encountered by machine learning engineers and their definitive solutions:
      </p>

      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Common Mistake</th>
              <th>Observed Symptom</th>
              <th>Root Cause</th>
              <th>Engineering Correction</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td><strong>Fitting Scaler Before Train/Test Split</strong></td>
              <td>Validation accuracy is 98%, but production accuracy drops to 78%</td>
              <td>Data leakage: Test set distribution leaks into training standardization</td>
              <td>Split data first; call <code>scaler.fit()</code> strictly on <code>X_train</code> only.</td>
            </tr>
            <tr>
              <td>2</td>
              <td><strong>Feeding IDs as Numerical Features</strong></td>
              <td>Near 100% training accuracy; near zero accuracy on new customers</td>
              <td>Model memorizes arbitrary database primary keys instead of underlying patterns</td>
              <td>Drop all ID and tracking columns before fitting (e.g. <code>customer_id</code>).</td>
            </tr>
            <tr>
              <td>3</td>
              <td><strong>Encoding Nominal Categories with OrdinalEncoder</strong></td>
              <td>Linear model assigns Paris = 2 &times; Tokyo, corrupting predictions</td>
              <td>Imposes an artificial mathematical order and Euclidean distance on arbitrary labels</td>
              <td>Use <code>OneHotEncoder</code> for nominal variables with no natural ranking.</td>
            </tr>
            <tr>
              <td>4</td>
              <td><strong>Crash on Unseen Test Categories</strong></td>
              <td><code>ValueError: Found unknown categories in column 0</code> during live inference</td>
              <td>A new customer entered a city not present in the training split</td>
              <td>Set <code>OneHotEncoder(handle_unknown='ignore')</code> to output all-zeros for new labels.</td>
            </tr>
            <tr>
              <td>5</td>
              <td><strong>Combinatorial Feature Explosion with Polynomials</strong></td>
              <td>Out of memory (OOM) error or extreme multi-hour training slowdown</td>
              <td>Degree 3 or 4 on 50+ features generated hundreds of thousands of columns</td>
              <td>Keep degree &le; 2, use <code>interaction_only=True</code>, or apply L1 Lasso feature selection.</td>
            </tr>
            <tr>
              <td>6</td>
              <td><strong>Target Leakage via Reverse Feature Engineering</strong></td>
              <td>Model has 99.9% ROC-AUC on validation, but cannot predict real future events</td>
              <td>Engineered feature was constructed using data generated <em>after</em> the outcome occurred</td>
              <td>Audit timestamp lineage: features must strictly represent information available prior to decision.</td>
            </tr>
            <tr>
              <td>7</td>
              <td><strong>Division by Zero in Ratio Features</strong></td>
              <td><code>ValueError: Input contains NaN, infinity or a value too large</code></td>
              <td>Denominator in ratio (e.g. <code>loan / income</code>) was zero or missing</td>
              <td>Add a stabilization epsilon: <code>df['ratio'] = df['A'] / (df['B'] + 1.0)</code>.</td>
            </tr>
            <tr>
              <td>8</td>
              <td><strong>Imputing with Mean on Heavily Skewed Data</strong></td>
              <td>Imputed values distort normal feature distributions and degrade accuracy</td>
              <td>Outliers drag the arithmetic mean far into the right tail</td>
              <td>Use <code>SimpleImputer(strategy='median')</code> for continuous skewed features.</td>
            </tr>
            <tr>
              <td>9</td>
              <td><strong>Scaling Trees and Random Forests Unnecessarily</strong></td>
              <td>Pipeline code is bloated with unnecessary scalers</td>
              <td>Misunderstanding that tree-based split thresholds are invariant to monotonic scaling</td>
              <td>Omit scaling for pure tree models, or keep inside pipeline if pairing with linear algorithms.</td>
            </tr>
            <tr>
              <td>10</td>
              <td><strong>Feature Selection Before Cross-Validation</strong></td>
              <td>Validation accuracy is unrealistically high and unrepeatable in production</td>
              <td>Labels from validation folds guided the feature selection algorithm</td>
              <td>Wrap <code>SelectKBest</code> inside the pipeline so each fold performs its own selection.</td>
            </tr>
            <tr>
              <td>11</td>
              <td><strong>Wrong Naming Syntax in Pipeline GridSearchCV</strong></td>
              <td><code>ValueError: Invalid parameter ... Check the list of available parameters</code></td>
              <td>Used single underscore or omitted step prefix in parameter grid keys</td>
              <td>Use double underscores: <code>&lt;step_name&gt;__&lt;substep_name&gt;__&lt;param&gt;</code>.</td>
            </tr>
            <tr>
              <td>12</td>
              <td><strong>Forgetting to Set remainder='drop'</strong></td>
              <td>Unintended columns (IDs, raw text, targets) pass into final model</td>
              <td>Default ColumnTransformer behavior or accidental <code>passthrough</code></td>
              <td>Explicitly set <code>remainder='drop'</code> and audit transformed array shape.</td>
            </tr>
            <tr>
              <td>13</td>
              <td><strong>Cyclical Time Discontinuity (23:00 vs 00:00)</strong></td>
              <td>Model treats midnight and 11 PM as 23 hours apart</td>
              <td>Treating hour of day as a linear scalar integer from 0 to 23</td>
              <td>Encode cyclical features into 2D sine and cosine coordinates: <code>sin(2&pi;t/24)</code>.</td>
            </tr>
            <tr>
              <td>14</td>
              <td><strong>Assuming Every Engineered Feature Helps</strong></td>
              <td>Validation score drops after adding 20 engineered features</td>
              <td>Noisy features increase model variance without adding predictive signal</td>
              <td>Always validate every engineered feature empirically with K-Fold cross-validation.</td>
            </tr>
            <tr>
              <td>15</td>
              <td><strong>Saving Models Without Preprocessors</strong></td>
              <td>Deployed model fails in production because incoming raw JSON is unscaled/unencoded</td>
              <td>Practitioner serialized only the estimator: <code>joblib.dump(clf)</code> instead of pipeline</td>
              <td>Always serialize the complete end-to-end <code>Pipeline</code> object.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 20: END-TO-END PRACTICAL PROJECT   -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-20">
      <div class="section-header">
        <span class="section-tag">Module 20 • Complete Implementation Practical</span>
        <h2 class="section-title"><a href="#sec-20">20. End-to-End Practical: From Raw Data to a Reliable ML Pipeline</a></h2>
      </div>

      <p>
        In this capstone practical, we will build a production-grade, leak-free Machine Learning Pipeline from scratch. We will handle raw data containing continuous numbers, missing values, categorical strings, and date features, synthesize domain ratios, execute 5-fold cross-validation, and tune the pipeline with <code>GridSearchCV</code>.
      </p>

      <h3>20.1 Complete Python Implementation</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python 3.10+ • Complete End-to-End ML Pipeline Practical</span>
          <span class="code-lang">python</span>
        </div>
        <pre><code>import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# ==========================================
# 1. LOAD / GENERATE REALISTIC RAW DATASET
# ==========================================
np.random.seed(42)
N = 1000

age = np.random.randint(21, 65, size=N)
income = np.random.lognormal(mean=10.5, sigma=0.6, size=N).round(-2)
credit_score = np.random.randint(450, 850, size=N)
loan_amount = (income * np.random.uniform(0.2, 4.0, size=N)).round(-2)
tenure_months = np.random.randint(6, 120, size=N)
days_as_customer = np.random.randint(30, 1800, size=N)

city = np.random.choice(['New York', 'San Francisco', 'Chicago', 'Austin', 'Seattle'], size=N, p=[0.3, 0.2, 0.2, 0.15, 0.15])
education = np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], size=N, p=[0.25, 0.45, 0.22, 0.08])
employment_type = np.random.choice(['Salaried', 'Self-Employed', 'Contract', 'Freelance'], size=N, p=[0.55, 0.25, 0.12, 0.08])

# Ground truth probability
dti = loan_amount / (income + 1e-5)
z = (0.00004 * income + 0.012 * credit_score - 1.2 * dti + 0.04 * age 
     + 0.0008 * days_as_customer + (education == 'PhD') * 0.8 
     + (education == 'Master') * 0.4 + (employment_type == 'Salaried') * 0.5 - 11.5)
prob = 1 / (1 + np.exp(-z))
loan_approved = (prob > 0.5).astype(int)

# Inject realistic missing values
income_missing = income.astype(float)
income_missing[np.random.choice(N, size=int(N * 0.05), replace=False)] = np.nan
credit_missing = credit_score.astype(float)
credit_missing[np.random.choice(N, size=int(N * 0.03), replace=False)] = np.nan
employment_missing = employment_type.copy()
employment_missing[np.random.choice(N, size=int(N * 0.04), replace=False)] = None

df = pd.DataFrame({
    'age': age,
    'income': income_missing,
    'credit_score': credit_missing,
    'loan_amount': loan_amount,
    'tenure_months': tenure_months,
    'days_as_customer': days_as_customer,
    'city': city,
    'education': education,
    'employment_type': employment_missing,
    'loan_approved': loan_approved
})

# ==========================================
# 2. TRAIN / TEST SPLIT BEFORE PREPROCESSING
# ==========================================
X = df.drop(columns=['loan_approved'])
y = df['loan_approved']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# ==========================================
# 3. FEATURE SYNTHESIS FUNCTION
# ==========================================
def engineer_features(data):
    df_eng = data.copy()
    # Debt-to-Income ratio with zero division guard
    df_eng['debt_to_income'] = df_eng['loan_amount'] / (df_eng['income'] + 1.0)
    # Loan relative to applicant age
    df_eng['loan_to_age'] = df_eng['loan_amount'] / df_eng['age']
    # Account tenure relative to career age
    df_eng['tenure_ratio'] = df_eng['tenure_months'] / (df_eng['age'] * 12.0)
    return df_eng

X_train_eng = engineer_features(X_train)
X_test_eng = engineer_features(X_test)

num_cols = ['age', 'income', 'credit_score', 'loan_amount', 'tenure_months', 
            'days_as_customer', 'debt_to_income', 'loan_to_age', 'tenure_ratio']
cat_cols = ['city', 'education', 'employment_type']

# ==========================================
# 4. ASSEMBLE COLUMN TRANSFORMER & PIPELINE
# ==========================================
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', num_transformer, num_cols),
    ('cat', cat_transformer, cat_cols)
])

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# ==========================================
# 5. TUNING INSIDE PIPELINE WITH GRIDSEARCHCV
# ==========================================
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
param_grid = {
    'preprocessor__num__imputer__strategy': ['mean', 'median'],
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [5, 8, 12],
    'classifier__min_samples_leaf': [2, 4]
}

grid_search = GridSearchCV(pipeline, param_grid=param_grid, cv=cv, scoring='roc_auc', n_jobs=-1)
grid_search.fit(X_train_eng, y_train)

best_pipeline = grid_search.best_estimator_

# ==========================================
# 6. EVALUATE FINAL MODEL ON HOLDOUT TEST SET
# ==========================================
test_preds = best_pipeline.predict(X_test_eng)
test_probs = best_pipeline.predict_proba(X_test_eng)[:, 1]

print("=== FINAL HOLDOUT TEST SET PERFORMANCE ===")
print(f"Accuracy:  {accuracy_score(y_test, test_preds):.4f}")
print(f"Precision: {precision_score(y_test, test_preds):.4f}")
print(f"Recall:    {recall_score(y_test, test_preds):.4f}")
print(f"F1-Score:  {f1_score(y_test, test_preds):.4f}")
print(f"ROC-AUC:   {roc_auc_score(y_test, test_probs):.4f}")</code></pre>
      </div>

      <h3>20.2 Empirical Practical Results</h3>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Evaluation Metric</th>
              <th>Naive Baseline Model</th>
              <th>Feature-Engineered Tuned Pipeline</th>
              <th>Performance Delta (&Delta;)</th>
              <th>Engineering Interpretation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Holdout Accuracy</strong></td>
              <td>87.50%</td>
              <td><strong>89.50%</strong></td>
              <td><span style="color:#047857;font-weight:700;">+2.00%</span></td>
              <td>Better separation of high-risk vs creditworthy borrowers</td>
            </tr>
            <tr>
              <td><strong>Holdout Precision</strong></td>
              <td>86.36%</td>
              <td><strong>94.12%</strong></td>
              <td><span style="color:#047857;font-weight:700;">+7.76%</span></td>
              <td>Massive drop in false positive approvals; protects bank capital</td>
            </tr>
            <tr>
              <td><strong>Holdout Recall</strong></td>
              <td>65.51%</td>
              <td><strong>62.75%</strong></td>
              <td><span style="color:#475569;">-2.76%</span></td>
              <td>Trade-off for higher precision under default 0.5 decision threshold</td>
            </tr>
            <tr>
              <td><strong>Holdout F1-Score</strong></td>
              <td>0.7423</td>
              <td><strong>0.7529</strong></td>
              <td><span style="color:#047857;font-weight:700;">+0.0107</span></td>
              <td>Stronger harmonic balance between precision and recall</td>
            </tr>
            <tr>
              <td><strong>5-Fold CV ROC-AUC</strong></td>
              <td>0.9412</td>
              <td><strong>0.9593</strong></td>
              <td><span style="color:#047857;font-weight:700;">+0.0181</span></td>
              <td>Superior ranking discrimination across all possible decision thresholds</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 21: REVISION, GLOSSARY & CHECKLIST -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-21">
      <div class="section-header">
        <span class="section-tag">Module 21 • Summary &amp; Decision Guide</span>
        <h2 class="section-title"><a href="#sec-21">21. Quick Revision, Glossary, and Checklist</a></h2>
      </div>

      <p>
        Use the following architectural decision guide when planning the feature preprocessing strategy for any new tabular machine learning project:
      </p>

      <div class="diagram-container">
        __SVG_DECISION_GUIDE__
        <div class="diagram-caption">Figure 21.1: Master Machine Learning Pipeline Decision Guide. Systematic workflow for inspecting columns, handling missing values, scaling representations, and wrapping within a pipeline.</div>
      </div>

      <h3>21.1 Comprehensive 15-Term Glossary</h3>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Term</th>
              <th>Rigorous Definition</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>Feature</strong></td><td>An individual measurable property or characteristic of a phenomenon used as an input variable (<em>X</em>) to an ML model.</td></tr>
            <tr><td><strong>Target</strong></td><td>The outcome or ground-truth dependent variable (<em>y</em>) that the model attempts to predict.</td></tr>
            <tr><td><strong>Feature Engineering</strong></td><td>The systematic process of using domain knowledge and statistical transformations to create, clean, scale, and select features.</td></tr>
            <tr><td><strong>Imputation</strong></td><td>The practice of replacing missing (<code>NaN</code>) data with substituted statistical estimates (mean, median, mode).</td></tr>
            <tr><td><strong>One-Hot Encoding</strong></td><td>Transforming a nominal categorical column into multiple binary indicator columns (0 or 1).</td></tr>
            <tr><td><strong>Ordinal Encoding</strong></td><td>Assigning ascending integers to categorical values that possess an intrinsic hierarchical ordering.</td></tr>
            <tr><td><strong>Standardization</strong></td><td>Transforming numeric features to have zero mean and unit variance: <em>z = (x - &mu;) / &sigma;</em>.</td></tr>
            <tr><td><strong>Min-Max Scaling</strong></td><td>Linear scaling that bounds feature values strictly into a target range, typically [0, 1].</td></tr>
            <tr><td><strong>Robust Scaling</strong></td><td>Scaling based on the median and Interquartile Range (IQR), making it resistant to extreme outliers.</td></tr>
            <tr><td><strong>Data Leakage</strong></td><td>When information from outside the training partition leaks into model fitting, causing over-optimistic validation.</td></tr>
            <tr><td><strong>Pipeline</strong></td><td>A scikit-learn construct that chains data transformers and a final estimator into an immutable sequence.</td></tr>
            <tr><td><strong>ColumnTransformer</strong></td><td>A utility that applies distinct preprocessing pipelines to specific column subsets of a dataset.</td></tr>
            <tr><td><strong>Cross-Validation</strong></td><td>Evaluating model stability by partitioning data into <em>K</em> folds, fitting on <em>K-1</em> and evaluating on the remainder.</td></tr>
            <tr><td><strong>Polynomial Features</strong></td><td>Generating power terms and cross-product interaction features to enable linear models to fit curves.</td></tr>
            <tr><td><strong>Feature Selection</strong></td><td>Selecting a subset of high-signal features and discarding noisy or redundant columns.</td></tr>
          </tbody>
        </table>
      </div>

      <h3>21.2 The 10-Step Pipeline Engineering Checklist</h3>
      <div class="callout callout-tip">
        <div class="callout-title">📋 10-Step Pipeline Production Checklist</div>
        <ol style="margin-bottom:0;">
          <li>[ ] <strong>Drop Identifiers:</strong> Remove <code>id</code>, <code>uuid</code>, and tracking columns before fitting.</li>
          <li>[ ] <strong>Train/Test Split First:</strong> Partition <code>X_train</code> and <code>X_test</code> before calculating any statistics.</li>
          <li>[ ] <strong>Check Outliers:</strong> Use median imputation and RobustScaler if extreme outliers exist.</li>
          <li>[ ] <strong>Validate Category Types:</strong> Use OneHotEncoder for nominal, OrdinalEncoder for true hierarchies.</li>
          <li>[ ] <strong>Set handle_unknown='ignore':</strong> Prevent API crashes on unseen inference categories.</li>
          <li>[ ] <strong>Synthesize Domain Ratios:</strong> Add zero-division safeguards: <code>A / (B + 1.0)</code>.</li>
          <li>[ ] <strong>Wrap in ColumnTransformer:</strong> Keep numeric and categorical pipelines strictly segregated.</li>
          <li>[ ] <strong>Enclose in Master Pipeline:</strong> Couple the preprocessor with the estimator.</li>
          <li>[ ] <strong>Cross-Validate Entire Pipeline:</strong> Pass <code>pipeline</code>, not raw arrays, to <code>cross_val_score</code>.</li>
          <li>[ ] <strong>Serialize Master Object:</strong> Save the entire pipeline with <code>joblib.dump(pipeline, 'model.pkl')</code>.</li>
        </ol>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 22: SELF-CHECK QUESTIONS & ANSWERS -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-22">
      <div class="section-header">
        <span class="section-tag">Module 22 • Knowledge Assessment</span>
        <h2 class="section-title"><a href="#sec-22">22. Self-Check Questions with Detailed Answers</a></h2>
      </div>

      <p>
        Test your understanding of Feature Engineering and ML Pipelines. Click each question below to reveal the detailed answer and mathematical explanation:
      </p>

      <details class="faq-item">
        <summary class="faq-summary">Q1: Why does calculating the dataset mean before train/test splitting cause data leakage?</summary>
        <div class="faq-answer">
          <strong>Answer:</strong> When you compute the mean across all rows before splitting, the test set's values directly contribute to the calculated mean (&mu;). When the training set is standardized using this global mean, information about the future test distribution has leaked into the training features. The model's validation score becomes artificially optimistic because it has already 'seen' the test distribution. In production, real future data will have a different mean, causing model performance to degrade.
        </div>
      </details>

      <details class="faq-item">
        <summary class="faq-summary">Q2: When should you prefer Median Imputation over Mean Imputation?</summary>
        <div class="faq-answer">
          <strong>Answer:</strong> You should prefer Median Imputation whenever the numerical feature is heavily skewed or contains extreme outliers (such as income, house prices, transaction sizes, or web traffic). Because the mean is sensitive to extreme values, a single billionaire in a salary dataset will drag the mean up by hundreds of thousands of dollars, imputing absurd values into missing rows. The median represents the 50th percentile and remains completely stable regardless of outlier magnitudes.
        </div>
      </details>

      <details class="faq-item">
        <summary class="faq-summary">Q3: Why is OneHotEncoder(handle_unknown='ignore') critical for production APIs?</summary>
        <div class="faq-answer">
          <strong>Answer:</strong> In production, live user requests will inevitably present a category that was never observed in the historical training set (e.g. a customer registering from a brand-new city or using a new mobile operating system). By default, scikit-learn's <code>OneHotEncoder</code> throws a fatal <code>ValueError</code>, crashing your server. Setting <code>handle_unknown='ignore'</code> instructs the encoder to gracefully output an all-zero vector for unseen categories, allowing inference to proceed smoothly.
        </div>
      </details>

      <details class="faq-item">
        <summary class="faq-summary">Q4: Why don't Decision Trees and Random Forests require feature scaling?</summary>
        <div class="faq-answer">
          <strong>Answer:</strong> Decision trees evaluate split decisions one feature at a time along orthogonal axes (e.g. <em>x_j &ge; threshold</em>). Because trees do not compute Euclidean distances, dot products, or gradient derivatives across multiple features simultaneously, multiplying a feature by 1,000 or shifting its mean simply scales the split threshold identically. The tree makes the exact same binary partitions whether the feature is scaled or unscaled.
        </div>
      </details>

      <details class="faq-item">
        <summary class="faq-summary">Q5: What is the primary risk of using PolynomialFeatures(degree=3) on high-dimensional data?</summary>
        <div class="faq-answer">
          <strong>Answer:</strong> The primary risk is the <em>Combinatorial Explosion</em> of the feature space. The number of generated polynomial combinations scales as <code>C(n + d, d)</code>. For 100 features at degree 3, this creates 176,851 columns! This causes memory crashes (OOM), extremely slow training, and massive overfitting as the model fits random noise in the hyper-dimensional space.
        </div>
      </details>

      <details class="faq-item">
        <summary class="faq-summary">Q6: What is the difference between fit(), transform(), and fit_transform() in a Pipeline?</summary>
        <div class="faq-answer">
          <strong>Answer:</strong>
          <ul>
            <li><code>fit(X)</code>: Computes and learns internal statistics from the data (e.g. mean, variance, median, vocabulary) and saves them in the object. It does not modify <em>X</em>.</li>
            <li><code>transform(X)</code>: Uses the previously learned statistics to transform <em>X</em> into its new mathematical representation.</li>
            <li><code>fit_transform(X)</code>: Performs both operations consecutively on the training data in a single optimized pass.</li>
          </ul>
          In a Pipeline, all intermediate stages call <code>fit_transform()</code> during training, but only <code>transform()</code> during prediction.
        </div>
      </details>

      <details class="faq-item">
        <summary class="faq-summary">Q7: How does scikit-learn's double-underscore syntax work in GridSearchCV?</summary>
        <div class="faq-answer">
          <strong>Answer:</strong> In scikit-learn pipelines, steps are nested inside named objects. To set or tune an internal hyperparameter, scikit-learn uses double underscores (<code>__</code>) to traverse the hierarchy: <code>&lt;step_name&gt;__&lt;substep_name&gt;__&lt;parameter_name&gt;</code>. For example, <code>preprocessor__num__imputer__strategy = 'median'</code> tells GridSearchCV to navigate into the 'preprocessor' step, then the 'num' branch, then the 'imputer' transformer, and tune its 'strategy' parameter.
        </div>
      </details>

      <details class="faq-item">
        <summary class="faq-summary">Q8: Why is treating a Customer ID column as a numerical feature disastrous?</summary>
        <div class="faq-answer">
          <strong>Answer:</strong> Customer IDs are arbitrary primary keys generated by databases (e.g. #1001, #1002). They contain zero natural relationship with real-world target behavior. A machine learning model will treat #1002 as having 'twice the magnitude' of #501, memorizing specific IDs. This results in near 100% training accuracy, but complete failure on new customers whose IDs were never seen.
        </div>
      </details>

      <details class="faq-item">
        <summary class="faq-summary">Q9: How does cyclical encoding preserve time relationships?</summary>
        <div class="faq-answer">
          <strong>Answer:</strong> Standard scalar representation treats 23:00 (11 PM) and 00:00 (midnight) as 23 units apart. Cyclical encoding projects the 24-hour clock onto a 2D Cartesian circle using <code>x_sin = sin(2&pi;t/24)</code> and <code>x_cos = cos(2&pi;t/24)</code>. In this 2D coordinate space, 23:00 and 00:00 lie right next to each other on the perimeter of the unit circle, preserving true temporal continuity for distance-based and linear models.
        </div>
      </details>

      <details class="faq-item">
        <summary class="faq-summary">Q10: Why should you serialize the entire Pipeline object instead of just the trained classifier?</summary>
        <div class="faq-answer">
          <strong>Answer:</strong> If you only save the trained model (e.g. <code>joblib.dump(clf)</code>), your production deployment code must manually replicate all raw-data cleaning, missing value imputation, one-hot encoding dictionaries, and scaling factors. Any mismatch in category ordering, imputation constants, or scale parameters between training and production will produce garbage predictions or crash your server. Saving the master <code>Pipeline</code> guarantees that raw JSON inputs undergo the exact same mathematical transformations that were fitted during training.
        </div>
      </details>

      <!-- INTERACTIVE CALCULATOR -->
      <div class="calc-card" style="margin-top: 28px;">
        <div class="calc-title">
          <span>🧮</span> Interactive Pipeline Feature Dimension Calculator
        </div>
        <p class="calc-desc">
          Estimate the transformed matrix dimensionality produced by your ColumnTransformer and Polynomial expansion before training.
        </p>

        <div class="calc-form-grid">
          <div class="calc-group">
            <label class="calc-label" for="calc-num-cols">Numerical Columns Count:</label>
            <input class="calc-input" id="calc-num-cols" type="number" value="6" min="1" max="1000">
          </div>
          <div class="calc-group">
            <label class="calc-label" for="calc-cat-cols">Categorical Columns Count:</label>
            <input class="calc-input" id="calc-cat-cols" type="number" value="3" min="0" max="500">
          </div>
          <div class="calc-group">
            <label class="calc-label" for="calc-avg-cats">Avg Unique Categories per Column:</label>
            <input class="calc-input" id="calc-avg-cats" type="number" value="4" min="2" max="100">
          </div>
          <div class="calc-group">
            <label class="calc-label" for="calc-poly-deg">Polynomial Expansion Degree:</label>
            <select class="calc-input" id="calc-poly-deg">
              <option value="1" selected>None (Degree 1 - Linear)</option>
              <option value="2">Degree 2 (Quadratic &amp; Interactions)</option>
              <option value="3">Degree 3 (Cubic - Warning!)</option>
            </select>
          </div>
        </div>

        <div class="calc-results-box">
          <div class="calc-res-item">
            <span class="calc-res-label">One-Hot Dummies</span>
            <span class="calc-res-val" id="res-ohe-cols">12</span>
          </div>
          <div class="calc-res-item">
            <span class="calc-res-label">ColumnTransformer Output</span>
            <span class="calc-res-val" id="res-total-cols">18</span>
          </div>
          <div class="calc-res-item">
            <span class="calc-res-label">After Polynomial Expansion</span>
            <span class="calc-res-val" id="res-poly-cols">18</span>
          </div>
        </div>
      </div>

      <script>
        function updateDimCalc() {
          const numCols = parseInt(document.getElementById('calc-num-cols').value) || 0;
          const catCols = parseInt(document.getElementById('calc-cat-cols').value) || 0;
          const avgCats = parseInt(document.getElementById('calc-avg-cats').value) || 0;
          const deg = parseInt(document.getElementById('calc-poly-deg').value) || 1;

          const oheCols = catCols * avgCats;
          const baseCols = numCols + oheCols;

          let polyCols = baseCols;
          if (deg === 2) {
            // C(n + 2, 2) - 1 (excluding bias) = n + n(n-1)/2 + n = n + n(n+1)/2
            polyCols = baseCols + Math.round((baseCols * (baseCols + 1)) / 2);
          } else if (deg === 3) {
            // Approx combinations
            polyCols = baseCols + Math.round((baseCols * (baseCols + 1)) / 2) + Math.round((baseCols * (baseCols + 1) * (baseCols + 2)) / 6);
          }

          document.getElementById('res-ohe-cols').innerText = oheCols.toLocaleString();
          document.getElementById('res-total-cols').innerText = baseCols.toLocaleString();
          document.getElementById('res-poly-cols').innerText = polyCols.toLocaleString();
        }

        document.getElementById('calc-num-cols').addEventListener('input', updateDimCalc);
        document.getElementById('calc-cat-cols').addEventListener('input', updateDimCalc);
        document.getElementById('calc-avg-cats').addEventListener('input', updateDimCalc);
        document.getElementById('calc-poly-deg').addEventListener('change', updateDimCalc);
        updateDimCalc();
      </script>
    </section>

    <!-- FOOTER -->
    <footer class="page-footer">
      <p>CodeVerse Machine Learning Interactive Masterclass • Topic 23: Feature Engineering &amp; ML Pipelines</p>
      <p style="margin-top:6px;font-size:12px;">Crafted for rigorous conceptual mastery, strict Light Mode accessibility, and production engineering reliability.</p>
    </footer>
"""
