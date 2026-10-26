# Topic 23 Content Module — Part 1: Sections 01 to 06
# High quality, beginner-friendly, Light Mode only, accessible HTML entities for math.

PART_1_HTML = """
    <!-- ========================================== -->
    <!-- SECTION 01: INTRODUCTION TO FEATURES & FE -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-01">
      <div class="section-header">
        <span class="section-tag">Module 01 • Conceptual Foundation</span>
        <h2 class="section-title"><a href="#sec-01">1. Introduction to Features and Feature Engineering</a></h2>
      </div>

      <div class="callout callout-important">
        <div class="callout-title">🍳 The Everyday Analogy: Preparing Ingredients Before Cooking</div>
        <p>
          Imagine you are a chef preparing an gourmet dinner. You do not dump whole unwashed potatoes, unpeeled onions, and raw unmeasured spices directly into a hot pan. If you do, the soup will be bitter, gritty, and unevenly cooked regardless of how expensive your stove is. Instead, you systematically <strong>wash, peel, dice, measure, and season</strong> the ingredients beforehand.
        </p>
        <p style="margin-bottom:0;">
          In Machine Learning, your learning algorithm is the stove, and your raw data consists of the raw, unwashed ingredients. <strong>Feature Engineering</strong> is the deliberate culinary art of cleaning, reshaping, scaling, and combining raw data attributes so that your machine learning model can extract patterns cleanly, accurately, and reliably.
        </p>
      </div>

      <h3>1.1 What Is a Feature and What Is a Target?</h3>
      <p>
        Before writing a single line of pipeline code, we must clearly define the fundamental terminology of tabular machine learning:
      </p>
      <ul>
        <li>
          <strong>Feature (Predictor / Input Variable, denoted <em>X</em>):</strong> An individual measurable property, characteristic, or attribute of the phenomenon being observed. In a real estate dataset, features might include <code>square_feet</code>, <code>num_bedrooms</code>, <code>zip_code</code>, and <code>year_built</code>.
        </li>
        <li>
          <strong>Target (Label / Ground Truth / Dependent Variable, denoted <em>y</em>):</strong> The actual outcome or quantity we wish to predict. For housing, this is <code>sale_price</code> (regression). For credit cards, this is <code>is_fraudulent</code> (binary classification: 0 or 1).
        </li>
        <li>
          <strong>Raw Data:</strong> The unprocessed form in which data naturally arrives from operational databases, web scrapers, log files, or APIs. Raw data is messy: it contains missing values (<code>NaN</code>), mixed text strings, timestamps formatted in multiple ways, extreme outliers, and non-predictive tracking identifiers.
        </li>
        <li>
          <strong>Model-Ready Data:</strong> A sanitized, strictly numerical, fully imputed, and appropriately scaled 2D matrix (shape <em>N &times; M</em>) where every value is a finite floating-point number that mathematical optimization algorithms can compute derivatives and distance metrics over.
        </li>
      </ul>

      <h3>1.2 What Does Feature Engineering Actually Do?</h3>
      <p>
        Machine learning algorithms do not possess human common sense. A linear regression model or neural network cannot look at a column containing <code>"2023-10-24 14:30:00"</code> and instinctively know that it represents a Tuesday afternoon during the autumn shopping quarter.
      </p>
      <p>
        <strong>Feature Engineering</strong> is the process of applying domain knowledge and statistical transformations to create new features or reshape existing ones. It bridges the semantic gap between human business logic and matrix algebra:
      </p>

      <div class="diagram-container">
        __SVG_WORKFLOW__
        <div class="diagram-caption">Figure 1.1: The End-to-End Feature Engineering &amp; ML Pipeline Lifecycle. Raw data is systematically refined through exploration, imputation, domain synthesis, scaling, and leak-free pipeline estimation.</div>
      </div>

      <h3>1.3 The Golden Rule: Feature Quality vs. Feature Quantity</h3>
      <div class="callout callout-warning">
        <div class="callout-title">⚠️ Common Beginner Fallacy: "More Features Always Mean a Better Model"</div>
        <p style="margin-bottom:0;">
          Adding dozens of noisy, highly correlated, or irrelevant features does <strong>not</strong> make a model smarter. In fact, it triggers the <em>Curse of Dimensionality</em>: as the number of features grows, the volume of the feature space increases exponentially, making the available data sparse. Models become prone to memorizing random noise (overfitting) and training times explode. High-quality, thoughtfully engineered features beat brute-force feature dumps every single time.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 02: UNDERSTANDING FEATURE TYPES   -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-02">
      <div class="section-header">
        <span class="section-tag">Module 02 • Data Categorization</span>
        <h2 class="section-title"><a href="#sec-02">2. Understanding Feature Types</a></h2>
      </div>

      <p>
        Every column in your raw dataset belongs to a distinct statistical data type. Applying the wrong transformation to a feature type—such as treating a telephone country code as an arithmetic number—will severely corrupt your model's decision boundaries.
      </p>

      <div class="diagram-container">
        __SVG_FEATURE_TYPES__
        <div class="diagram-caption">Figure 2.1: The Comprehensive Taxonomy of Machine Learning Feature Types, detailing their mathematical properties and standard pipeline actions.</div>
      </div>

      <h3>2.1 Comprehensive Feature Types Taxonomy</h3>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Feature Category</th>
              <th>Subtype</th>
              <th>Concrete Examples</th>
              <th>Mathematical Property</th>
              <th>Standard Pipeline Handling</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Numerical</strong></td>
              <td>Continuous</td>
              <td><code>annual_income</code> ($64,250.80), <code>body_temp</code> (98.6°F)</td>
              <td>Infinite possible values along a real continuum</td>
              <td>Median Imputation + <code>StandardScaler</code> / <code>RobustScaler</code></td>
            </tr>
            <tr>
              <td><strong>Numerical</strong></td>
              <td>Discrete / Count</td>
              <td><code>num_bedrooms</code> (3), <code>support_tickets</code> (12)</td>
              <td>Countable non-negative integers (0, 1, 2, ...)</td>
              <td>Imputation + Scaling; optional binning if highly skewed</td>
            </tr>
            <tr>
              <td><strong>Categorical</strong></td>
              <td>Nominal</td>
              <td><code>city</code> ("Tokyo", "Paris"), <code>color</code> ("Red")</td>
              <td>Mutually exclusive labels with NO natural ordering</td>
              <td><code>OneHotEncoder(handle_unknown='ignore')</code></td>
            </tr>
            <tr>
              <td><strong>Categorical</strong></td>
              <td>Ordinal</td>
              <td><code>education</code> ("HS" &lt; "BS" &lt; "MS" &lt; "PhD"), rating (1★–5★)</td>
              <td>Labels possess a meaningful intrinsic hierarchy</td>
              <td><code>OrdinalEncoder(categories=[ordered_list])</code></td>
            </tr>
            <tr>
              <td><strong>Binary / Boolean</strong></td>
              <td>Indicator</td>
              <td><code>is_vip_member</code> (True/False), <code>has_mortgage</code> (1/0)</td>
              <td>Only two mutually exclusive states</td>
              <td>Cast to binary integer 0 or 1; no further scaling required</td>
            </tr>
            <tr>
              <td><strong>Temporal</strong></td>
              <td>Date / Time</td>
              <td><code>signup_date</code> ("2023-10-24 14:30:00")</td>
              <td>Sequential timestamps with cyclical periodicity</td>
              <td>Decompose into Year, Month, Day, IsWeekend, or Cyclical Sine/Cosine</td>
            </tr>
            <tr>
              <td><strong>Unstructured</strong></td>
              <td>Free Text</td>
              <td><code>user_review</code> ("The service was swift and helpful")</td>
              <td>Unstructured sequences of natural language tokens</td>
              <td><code>TfidfVectorizer</code> or Word Embeddings within Pipeline</td>
            </tr>
            <tr>
              <td><strong>Identifier</strong></td>
              <td>System Key</td>
              <td><code>customer_id</code> ("#98214"), <code>ssn</code>, <code>row_uuid</code></td>
              <td>Unique arbitrary keys with zero generalizable pattern</td>
              <td><strong>DROP IMMEDIATELY!</strong> Never feed IDs into models</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-caution">
        <div class="callout-title">🛑 Crucial Distinction: The Identifier Column Trap</div>
        <p style="margin-bottom:0;">
          Beginners frequently feed columns like <code>user_id</code> or <code>transaction_id</code> into a Random Forest or Neural Network because they appear numeric. The model happily memorizes these IDs, achieving near 100% training accuracy! But on new unseen customers, the model fails completely because new customer IDs were never observed. Identifiers must always be dropped or used solely as tracking keys.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 03: RAW DATA VS MODEL-READY DATA  -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-03">
      <div class="section-header">
        <span class="section-tag">Module 03 • Structural Transformation</span>
        <h2 class="section-title"><a href="#sec-03">3. Raw Data vs Model-Ready Data</a></h2>
      </div>

      <p>
        Let us inspect a concrete side-by-side example comparing a raw operational customer table against its corresponding model-ready mathematical array.
      </p>

      <div class="diagram-container">
        __SVG_RAW_VS_READY__
        <div class="diagram-caption">Figure 3.1: Side-by-side comparison of a raw, messy dataset containing missing values, strings, and disparate scales versus a model-ready, float32 feature matrix.</div>
      </div>

      <h3>3.1 Walkthrough of Required Transformations</h3>
      <p>
        Notice what happens to each column in the raw table during pipeline execution:
      </p>
      <ol>
        <li>
          <strong>Age (Numerical):</strong> Scaled from raw ages (20–65) into standardized z-scores centered around 0 with unit variance. A raw age of 52 becomes <code>+1.16</code> standard deviations above the mean.
        </li>
        <li>
          <strong>Income (Numerical with NaNs):</strong> Missing income cells are imputed with the training median ($48,000), then transformed using <code>StandardScaler</code>. An imputed median value translates to a standardized z-score of <code>0.00</code>.
        </li>
        <li>
          <strong>City (Nominal Categorical):</strong> Transformed via One-Hot Encoding into separate binary columns: <code>City_Tokyo</code>, <code>City_Paris</code>, and <code>City_NewYork</code>. A row with "Tokyo" becomes <code>[1.0, 0.0, 0.0]</code>.
        </li>
        <li>
          <strong>Education (Ordinal Categorical):</strong> Transformed via Ordinal Encoding into numeric ranks respecting academic progression: <code>High School &rarr; 0</code>, <code>Bachelor &rarr; 1</code>, <code>Master &rarr; 2</code>, and <code>PhD &rarr; 3</code>.
        </li>
      </ol>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 04: HANDLING MISSING VALUES       -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-04">
      <div class="section-header">
        <span class="section-tag">Module 04 • Data Cleaning</span>
        <h2 class="section-title"><a href="#sec-04">4. Handling Missing Values</a></h2>
      </div>

      <p>
        Missing data occurs in almost every real-world project. Sensors fail, survey participants skip optional questions, database migrations drop fields, and users refuse to provide their household income.
      </p>

      <h3>4.1 Why Missing Values Break Machine Learning</h3>
      <p>
        Standard scikit-learn models like Linear Regression, Logistic Regression, Support Vector Machines (SVM), and standard K-Nearest Neighbors (KNN) calculate matrix multiplications and dot products. If a single value in a row is <code>NaN</code> (Not a Number), IEEE 754 floating-point arithmetic dictates that any operation involving <code>NaN</code> yields <code>NaN</code>:
      </p>
      <div class="formula-card">
        <div class="formula-math">w₁ · x₁ + w₂ · NaN = NaN</div>
        <div class="formula-desc">Loss functions and gradient updates immediately collapse when NaNs are encountered.</div>
      </div>

      <h3>4.2 Imputation Strategies</h3>
      <ul>
        <li>
          <strong>Mean Imputation:</strong> Replaces missing values with the arithmetic average (&mu;) of the observed training values. Fast, but <em>highly vulnerable to extreme outliers</em>.
        </li>
        <li>
          <strong>Median Imputation:</strong> Replaces missing values with the 50th percentile (middle value) of the observed training values. <strong>Highly recommended for skewed numerical data (e.g., income, house prices).</strong>
        </li>
        <li>
          <strong>Most Frequent (Mode) Imputation:</strong> Replaces missing values with the most frequently occurring category. Standard for categorical features.
        </li>
        <li>
          <strong>Constant Value Imputation:</strong> Replaces missing values with a fixed domain constant (e.g., <code>"Missing"</code> for text, or <code>-1</code> / <code>0</code> for specific numeric sensors).
        </li>
        <li>
          <strong>Missing Indicator:</strong> Adds a new binary feature column (e.g., <code>income_was_missing &isin; {0, 1}</code>). This preserves the critical business signal that a value was missing, which is often highly predictive of churn or fraud.
        </li>
      </ul>

      <div class="diagram-container">
        __SVG_IMPUTATION__
        <div class="diagram-caption">Figure 4.1: Comparing Mean vs. Median Imputation on skewed income data containing an extreme $2.5M outlier. The mean is dragged to $535k, while the median remains stable at $48k.</div>
      </div>

      <h3>4.3 Executable Python: Scikit-Learn SimpleImputer</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python 3.10+ • Scikit-Learn SimpleImputer</span>
          <span class="code-lang">python</span>
        </div>
        <pre><code>import numpy as np
from sklearn.impute import SimpleImputer

# Realistic income sample with extreme outlier and missing NaN
X_raw = np.array([
    [35000.0],
    [42000.0],
    [np.nan],    # Missing value to impute
    [48000.0],
    [52000.0],
    [2500000.0]  # Millionaire outlier
])

# Strategy 1: Mean Imputer (Skewed by outlier)
mean_imputer = SimpleImputer(strategy='mean')
X_mean_imputed = mean_imputer.fit_transform(X_raw)

# Strategy 2: Median Imputer (Robust to outlier)
median_imputer = SimpleImputer(strategy='median')
X_median_imputed = median_imputer.fit_transform(X_raw)

print(f"Mean Imputer substituted:   ${X_mean_imputed[2, 0]:,.2f}")
print(f"Median Imputer substituted: ${X_median_imputed[2, 0]:,.2f}")
# Output:
# Mean Imputer substituted:   $535,400.00 (Distorted!)
# Median Imputer substituted: $48,000.00  (True representative central tendency!)</code></pre>
      </div>

      <div class="callout callout-important">
        <div class="callout-title">🔒 The Zero-Leakage Imputation Rule</div>
        <p style="margin-bottom:0;">
          Imputation statistics (the training mean, median, or mode) <strong>must strictly be computed from the training split only</strong>. Calling <code>imputer.fit(X_all)</code> before splitting leaks the test set's distribution into the training set, producing over-optimistic validation scores that degrade in production.
        </p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 05: ENCODING CATEGORICAL FEATURES -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-05">
      <div class="section-header">
        <span class="section-tag">Module 05 • Categorical Transformation</span>
        <h2 class="section-title"><a href="#sec-05">5. Encoding Categorical Features</a></h2>
      </div>

      <p>
        Because machine learning algorithms operate in vector spaces using dot products and linear combinations, text strings like <code>"Tokyo"</code> or <code>"Bachelor's"</code> must be mapped into numeric coordinates. Choosing the correct encoding method is vital.
      </p>

      <h3>5.1 One-Hot Encoding (OHE) for Nominal Data</h3>
      <p>
        For categories that possess no inherent ranking (like cities, colors, or product departments), <strong>One-Hot Encoding</strong> creates a dedicated binary column (0 or 1) for each unique category.
      </p>

      <div class="diagram-container">
        __SVG_ONE_HOT_ENCODING__
        <div class="diagram-caption">Figure 5.1: One-Hot Encoding expansion. Setting <code>handle_unknown='ignore'</code> ensures that unseen categories at test time produce an all-zero vector rather than an application crash.</div>
      </div>

      <div class="callout callout-tip">
        <div class="callout-title">💡 Production Essential: handle_unknown='ignore'</div>
        <p style="margin-bottom:0;">
          In real-world applications, your test data or live web requests will inevitably encounter a category never seen during training (e.g., a customer registering from "Sydney" when training data only had "Tokyo", "Paris", and "New York"). By default, <code>OneHotEncoder</code> throws a <code>ValueError</code>. Setting <code>OneHotEncoder(handle_unknown='ignore')</code> tells scikit-learn to gracefully output all zeros for unseen categories, keeping your production API online.
        </p>
      </div>

      <h3>5.2 Ordinal Encoding for Hierarchical Data</h3>
      <p>
        When categories have a true mathematical order—such as education level, company hierarchy, or satisfaction ratings—One-Hot Encoding discards this valuable monotonic information. <strong>Ordinal Encoding</strong> maps categories to sequential integers while preserving the order:
      </p>

      <div class="diagram-container">
        __SVG_ORDINAL_ENCODING__
        <div class="diagram-caption">Figure 5.2: Ordinal Encoding structure. Education levels map to 0 &lt; 1 &lt; 2 &lt; 3, correctly reflecting academic progression without creating arbitrary distances.</div>
      </div>

      <h3>5.3 Executable Python: OneHotEncoder &amp; OrdinalEncoder</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python 3.10+ • Scikit-Learn Categorical Encoders</span>
          <span class="code-lang">python</span>
        </div>
        <pre><code>import numpy as np
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

# 1. One-Hot Encoding with handle_unknown='ignore'
cities_train = np.array([['Tokyo'], ['Paris'], ['New York'], ['London']])
ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
ohe.fit(cities_train)

# Transform new test samples, including unseen 'Sydney'
cities_test = np.array([['Sydney'], ['Paris']])
ohe_transformed = ohe.transform(cities_test)
print("Categories learned:", ohe.categories_[0].tolist())
print("Test Transform (Sydney, Paris):\n", ohe_transformed)
# Output:
# Categories learned: ['London', 'New York', 'Paris', 'Tokyo']
# Test Transform:
# [[0. 0. 0. 0.]  <- Sydney: Gracefully encoded as all zeros!
#  [0. 0. 1. 0.]] <- Paris: Exact match at index 2

# 2. Ordinal Encoding with explicit hierarchy
edu_train = np.array([['High School'], ['Bachelor'], ['Master'], ['PhD']])
oe = OrdinalEncoder(categories=[['High School', 'Bachelor', 'Master', 'PhD']])
edu_encoded = oe.fit_transform(edu_train)

for name, code in zip(edu_train.flatten(), edu_encoded.flatten()):
    print(f"  {name:12s} -> {int(code)}")
# Output:
#   High School  -> 0
#   Bachelor     -> 1
#   Master       -> 2
#   PhD          -> 3</code></pre>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 06: FEATURE SCALING & TRANSFORMS  -->
    <!-- ========================================== -->
    <section class="section-card" id="sec-06">
      <div class="section-header">
        <span class="section-tag">Module 06 • Mathematical Scaling</span>
        <h2 class="section-title"><a href="#sec-06">6. Feature Scaling and Transformation</a></h2>
      </div>

      <p>
        Features naturally arrive on wildly different numerical scales. In our loan dataset, <code>applicant_age</code> ranges from 21 to 65, while <code>annual_income</code> ranges from $20,000 to $250,000. Without scaling, distance-based and gradient-based algorithms fail catastrophically.
      </p>

      <div class="diagram-container">
        __SVG_FEATURE_SCALING__
        <div class="diagram-caption">Figure 6.1: Geometry of feature scaling. Unscaled coordinate spaces form severely elongated ellipses that distort Euclidean distances and cause gradient descent to oscillate. Standardized spaces form isotropic circles with balanced feature influence.</div>
      </div>

      <h3>6.1 Mathematical Formulations of Major Scalers</h3>

      <div class="formula-card">
        <div class="formula-math">z = (x - &mu;) / &sigma;</div>
        <div class="formula-desc">
          <strong>Standardization (StandardScaler):</strong> Centers data around mean &mu; = 0 with standard deviation &sigma; = 1. Retains outlier information without compressing normal variance.
        </div>
      </div>

      <div class="formula-card">
        <div class="formula-math">x' = (x - x_min) / (x_max - x_min)</div>
        <div class="formula-desc">
          <strong>Min-Max Scaling (MinMaxScaler):</strong> Compresses all values strictly into the bounded interval [0, 1]. Best for neural networks and image pixels, but highly sensitive to extreme outliers.
        </div>
      </div>

      <div class="formula-card">
        <div class="formula-math">x_robust = (x - Q₂) / (Q₃ - Q₁) = (x - Median) / IQR</div>
        <div class="formula-desc">
          <strong>Robust Scaling (RobustScaler):</strong> Centers using the median (Q₂) and scales by the Interquartile Range (IQR = Q₃ - Q₁). Unaffected by extreme outliers.
        </div>
      </div>

      <h3>6.2 Algorithm Sensitivity to Feature Scaling</h3>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Algorithm Family</th>
              <th>Requires Scaling?</th>
              <th>Underlying Mathematical Reason</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>KNN &amp; K-Means</strong></td>
              <td><span style="color:#B91C1C;font-weight:700;">MANDATORY</span></td>
              <td>Computes Euclidean distance &radic;(&sum;(x_i - y_i)&sup2;). Larger scales completely dominate the distance calculation.</td>
            </tr>
            <tr>
              <td><strong>Support Vector Machines (SVM)</strong></td>
              <td><span style="color:#B91C1C;font-weight:700;">MANDATORY</span></td>
              <td>RBF kernels exp(-&gamma;||x - y||&sup2;) and margin boundaries assume all dimensions have comparable variance.</td>
            </tr>
            <tr>
              <td><strong>Linear &amp; Logistic Regression (Regularized)</strong></td>
              <td><span style="color:#B91C1C;font-weight:700;">MANDATORY</span></td>
              <td>L1/L2 penalties penalize large weights &beta;_j. Unscaled features with tiny coefficients escape regularization!</td>
            </tr>
            <tr>
              <td><strong>Neural Networks / Deep Learning</strong></td>
              <td><span style="color:#B91C1C;font-weight:700;">MANDATORY</span></td>
              <td>Gradient descent updates oscillate wildly when features have disparate gradient magnitudes; causes exploding/vanishing gradients.</td>
            </tr>
            <tr>
              <td><strong>Decision Trees &amp; Random Forests</strong></td>
              <td><span style="color:#047857;font-weight:700;">NOT REQUIRED</span></td>
              <td>Trees make orthogonal splits (x_j &ge; threshold) one feature at a time. Monotonic scaling does not alter split points.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>6.3 Executable Python: Scaling Comparison</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python 3.10+ • Scikit-Learn Scalers</span>
          <span class="code-lang">python</span>
        </div>
        <pre><code>import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Sample dataset with one prominent outlier
X_demo = np.array([[10.0], [20.0], [30.0], [40.0], [100.0]])

ss = StandardScaler().fit(X_demo)
mm = MinMaxScaler().fit(X_demo)
rs = RobustScaler().fit(X_demo)

print(f"Original values: {X_demo.flatten().tolist()}")
print(f"StandardScaler:  {ss.transform(X_demo).flatten().round(2).tolist()}")
print(f"MinMaxScaler:    {mm.transform(X_demo).flatten().round(2).tolist()}")
print(f"RobustScaler:    {rs.transform(X_demo).flatten().round(2).tolist()}")
# Output:
# Original values: [10.0, 20.0, 30.0, 40.0, 100.0]
# StandardScaler:  [-0.95, -0.63, -0.32, 0.0, 1.9]   <- Zero mean
# MinMaxScaler:    [0.0, 0.11, 0.22, 0.33, 1.0]      <- Tightly bounded in [0, 1]
# RobustScaler:    [-1.0, -0.5, 0.0, 0.5, 3.5]       <- Centered on median (30.0)</code></pre>
      </div>
    </section>
"""
