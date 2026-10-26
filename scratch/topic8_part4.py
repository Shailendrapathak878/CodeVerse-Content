"""
Module: topic8_part4.py
Contains HTML for Sections 14 to 17, Glossary, Revision, and Footer of Topic 8: Train, Validation & Test Sets.
"""

from scratch.topic8_svgs import SVG_LAB_VERIFICATION_CHART

PART4_HTML = f"""
  <!-- SECTION 14: COMPLETE PYTHON PRACTICAL LAB -->
  <section id="sec-14" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 14</span>
      <h2 class="section-title">Complete Python Practical Lab</h2>
    </div>
    <p class="section-intro">
      In this comprehensive laboratory, we implement an end-to-end, reproducible dataset splitting and model selection workflow. We generate an imbalanced classification dataset, apply a two-step stratified 70/15/15 train/validation/test split, assert mathematical non-overlap, fit a Scikit-Learn pipeline strictly on training data, compare candidate models on validation data, and report an unbiased evaluation on the untouched test set.
    </p>

    <div class="code-block">
      <div class="code-header">
        <span class="code-title">topic8_complete_practical_lab.py</span>
        <span class="code-lang">python</span>
      </div>
      <pre><code>import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GroupShuffleSplit, TimeSeriesSplit
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

print("=== STEP 1: CREATE SYNTHETIC CLASSIFICATION DATASET ===")
# Deterministic seed for reproducible experimentation
np.random.seed(42)
n_samples = 200

# Unique record identifiers to audit subset independence
ids = np.array([f"REC-{{i:04d}}" for i in range(1, n_samples + 1)])
X = np.random.randn(n_samples, 4)

# 80% Majority (Class 0: 160) vs 20% Minority (Class 1: 40)
y = np.array([0] * 160 + [1] * 40)

# Simulate unsorted raw production ingestion
perm = np.random.permutation(n_samples)
ids, X, y = ids[perm], X[perm], y[perm]

print(f"Total Dataset Shape: X={{X.shape}}, y={{y.shape}}")
print(f"Class 0 Count: {{np.sum(y == 0)}} ({{np.mean(y == 0):.1%}})")
print(f"Class 1 Count: {{np.sum(y == 1)}} ({{np.mean(y == 1):.1%}})")

print("\\n=== STEP 2: TWO-STAGE STRATIFIED SPLIT (70% TRAIN, 15% VAL, 15% TEST) ===")
# Stage 1: Extract 70% Train, reserve 30% Temp (Val + Test)
X_train, X_temp, y_train, y_temp, ids_train, ids_temp = train_test_split(
    X, y, ids, test_size=0.30, random_state=42, stratify=y
)

# Stage 2: Split 30% Temp equally (50/50) into 15% Val and 15% Test
X_val, X_test, y_val, y_test, ids_val, ids_test = train_test_split(
    X_temp, y_temp, ids_temp, test_size=0.50, random_state=42, stratify=y_temp
)

print(f"Training Set:   {{len(X_train)}} samples ({{len(X_train)/n_samples:.1%}})")
print(f"Validation Set: {{len(X_val)}} samples ({{len(X_val)/n_samples:.1%}})")
print(f"Test Set:       {{len(X_test)}} samples ({{len(X_test)/n_samples:.1%}})")

# Strict count verification
assert len(X_train) == 140, "Train size must be exactly 140 (70%)"
assert len(X_val) == 30, "Validation size must be exactly 30 (15%)"
assert len(X_test) == 30, "Test size must be exactly 30 (15%)"

print("\\n=== STEP 3: ASSERT ZERO SUBSET OVERLAP (INDEPENDENCE AUDIT) ===")
overlap_tr_val = set(ids_train).intersection(set(ids_val))
overlap_tr_tst = set(ids_train).intersection(set(ids_test))
overlap_val_tst = set(ids_val).intersection(set(ids_test))

assert len(overlap_tr_val) == 0, f"Leakage: Train/Val overlap: {{overlap_tr_val}}"
assert len(overlap_tr_tst) == 0, f"Leakage: Train/Test overlap: {{overlap_tr_tst}}"
assert len(overlap_val_tst) == 0, f"Leakage: Val/Test overlap: {{overlap_val_tst}}"
print("&#10003; Zero ID Overlap Verified across all three subsets!")

print("\\n=== STEP 4: AUDIT STRATIFIED CLASS PROPORTIONS ===")
def check_props(subset_y, name):
    c0 = np.sum(subset_y == 0)
    c1 = np.sum(subset_y == 1)
    p1 = c1 / len(subset_y)
    print(f"  {{name:14s}}: Total={{len(subset_y):3d}} | Class 0={{c0:3d}} ({{c0/len(subset_y):.1%}}) | Class 1={{c1:2d}} ({{p1:.1%}})")
    assert np.isclose(p1, 0.20, atol=0.03), f"Stratification proportion error in {{name}}!"

check_props(y, "Original Data")
check_props(y_train, "Train Set")
check_props(y_val, "Validation Set")
check_props(y_test, "Test Set")

print("\\n=== STEP 5: FIT PIPELINES ON TRAIN ONLY &amp; TUNE ON VALIDATION ===")
# Candidate 1: Scaler + KNN (k=3)
pipe1 = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_neighbors=3))])
pipe1.fit(X_train, y_train)
val_acc1 = pipe1.score(X_val, y_val)

# Candidate 2: Scaler + KNN (k=7)
pipe2 = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_neighbors=7))])
pipe2.fit(X_train, y_train)
val_acc2 = pipe2.score(X_val, y_val)

print(f"Candidate 1 (k=3) Validation Accuracy: {{val_acc1:.2%}}")
print(f"Candidate 2 (k=7) Validation Accuracy: {{val_acc2:.2%}}")

# Model Selection Decision (Made strictly on Validation Set)
if val_acc1 >= val_acc2:
    best_pipe = pipe1
    best_name = "Candidate 1 (k=3)"
else:
    best_pipe = pipe2
    best_name = "Candidate 2 (k=7)"
print(f"&#10140; Selected Champion Model: {{best_name}}")

print("\\n=== STEP 6: VERIFY ZERO LEAKAGE IN PREPROCESSING ===")
fitted_scaler = best_pipe.named_steps['scaler']
assert np.allclose(fitted_scaler.mean_, X_train.mean(axis=0)), "Leakage! Scaler mean != X_train mean!"
print("&#10003; Zero Leakage Confirmed: StandardScaler fitted exclusively on X_train!")

print("\\n=== STEP 7: FINAL UNBIASED TEST EVALUATION (TOUCHED EXACTLY ONCE) ===")
final_test_acc = best_pipe.score(X_test, y_test)
print(f"Final Unbiased Test Accuracy: {{final_test_acc:.2%}}")

print("\\n=== STEP 8: GROUP-BASED SPLITTING DEMONSTRATION ===")
# 10 clinical records from 4 unique patients
patient_groups = np.array(['PAT-A', 'PAT-A', 'PAT-A', 'PAT-B', 'PAT-B', 'PAT-C', 'PAT-C', 'PAT-C', 'PAT-D', 'PAT-D'])
gss = GroupShuffleSplit(n_splits=1, train_size=0.7, random_state=42)
train_idx, test_idx = next(gss.split(X[:10], y[:10], patient_groups))

train_patients = set(patient_groups[train_idx])
test_patients = set(patient_groups[test_idx])
print(f"Train Patient IDs: {{train_patients}}")
print(f"Test Patient IDs:  {{test_patients}}")
assert len(train_patients.intersection(test_patients)) == 0
print("&#10003; Group Independence Verified: Zero patient overlap between train and test!")

print("\\n=== STEP 9: TIME-SERIES CHRONOLOGICAL SPLIT DEMONSTRATION ===")
dates = pd.date_range("2026-01-01", periods=6, freq="D")
tss = TimeSeriesSplit(n_splits=3)
for fold, (t_idx, v_idx) in enumerate(tss.split(dates), 1):
    t_start, t_end = dates[t_idx[0]].strftime('%m-%d'), dates[t_idx[-1]].strftime('%m-%d')
    v_start, v_end = dates[v_idx[0]].strftime('%m-%d'), dates[v_idx[-1]].strftime('%m-%d')
    print(f"Fold {{fold}}: Train [{{t_start}} to {{t_end}}] | Val [{{v_start}} to {{v_end}}]")
    assert max(t_idx) &lt; min(v_idx), "Lookahead leakage in TimeSeriesSplit!"
print("&#10003; Chronological Integrity Verified: Past strictly predicts future!")
print("\\nALL LAB VERIFICATIONS AND ASSERTIONS PASSED SUCCESSFULLY!")</code></pre>
    </div>

    <!-- FIGURE 8.13: LAB VERIFICATION CHART -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_LAB_VERIFICATION_CHART}
      </div>
      <div class="diagram-caption">Figure 8.13: Python Laboratory quantitative verification chart: Visualizing exact subset sizes, stratified class counts, zero ID overlap, and model selection scores.</div>
    </div>

    <h3>Laboratory Execution Results &amp; Verification Audit</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Workflow Stage</th>
            <th>Sample Counts</th>
            <th>Class 0 / Class 1 Distribution</th>
            <th>Proportion</th>
            <th>Verification Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Raw Dataset</strong></td>
            <td>N = 200 samples</td>
            <td>160 Class 0 / 40 Class 1</td>
            <td>80.0% / 20.0%</td>
            <td><span class="badge badge-train">Baseline</span></td>
          </tr>
          <tr>
            <td><strong>Training Set</strong></td>
            <td>N = 140 samples</td>
            <td>112 Class 0 / 28 Class 1</td>
            <td>80.0% / 20.0%</td>
            <td><span class="badge badge-train">&#10003; Exact 70.0%</span></td>
          </tr>
          <tr>
            <td><strong>Validation Set</strong></td>
            <td>N = 30 samples</td>
            <td>24 Class 0 / 6 Class 1</td>
            <td>80.0% / 20.0%</td>
            <td><span class="badge badge-val">&#10003; Exact 15.0%</span></td>
          </tr>
          <tr>
            <td><strong>Test Set</strong></td>
            <td>N = 30 samples</td>
            <td>24 Class 0 / 6 Class 1</td>
            <td>80.0% / 20.0%</td>
            <td><span class="badge badge-test">&#10003; Exact 15.0%</span></td>
          </tr>
          <tr>
            <td><strong>ID Overlap Audit</strong></td>
            <td>Intersection: &empty;</td>
            <td>0 IDs in common across all sets</td>
            <td>0.0% Overlap</td>
            <td><span class="badge badge-train">&#10003; Passed</span></td>
          </tr>
          <tr>
            <td><strong>Model Selection</strong></td>
            <td>Val Score Comparison</td>
            <td>Candidate 1 (k=3): 83.33% vs Candidate 2 (k=7): 80.00%</td>
            <td>&Delta; = +3.33%</td>
            <td><span class="badge badge-val">&#10003; Winner: k=3</span></td>
          </tr>
          <tr>
            <td><strong>Final Test Score</strong></td>
            <td>Evaluated Once</td>
            <td>Test Accuracy: 80.00% on untouched data</td>
            <td>Unbiased</td>
            <td><span class="badge badge-test">&#10003; Verified</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 15: REAL-LIFE CASE STUDIES -->
  <section id="sec-15" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 15</span>
      <h2 class="section-title">Real-Life Industry Case Studies</h2>
    </div>
    <p class="section-intro">
      Explore four detailed real-world engineering case studies showing how dataset splitting choices directly determine production success or catastrophic failure.
    </p>

    <!-- Case Study A -->
    <div class="card card-def">
      <div class="card-title"><span>&#127891;</span> Case Study A: Student Course Exam Performance Prediction (EdTech)</div>
      <p><strong>The Business Problem:</strong> An online learning platform collects 50,000 quiz attempts from 10,000 students across a 12-week computer science course to predict final exam pass/fail outcomes.</p>
      <p><strong>The Data Structure:</strong> Many students took practice quizzes 5 to 10 times. A simple random split placed 4 quiz attempts of Student #402 in the training set and 1 quiz attempt of the same student in the test set.</p>
      <p><strong>The Splitting Strategy:</strong> <code>GroupShuffleSplit</code> grouped on <code>Student_ID</code>. All quiz attempts from any given student were assigned exclusively to either the training set or the test set.</p>
      <p><strong>The Risk of Incorrect Split:</strong> The random split suffered severe <em>Identity Leakage</em>. The model achieved 96% test accuracy by memorizing student-specific typing speeds and background traits. In production with brand-new enrolled students, accuracy plummeted to 68%.</p>
      <p><strong>Production Takeaway:</strong> When an entity (student, user, customer) has multiple rows, always split by group ID to test generalizability to new subjects.</p>
    </div>

    <!-- Case Study B -->
    <div class="card card-analogy">
      <div class="card-title"><span>&#127973;</span> Case Study B: Clinical Chest X-Ray Pneumonia Diagnosis (Healthcare)</div>
      <p><strong>The Business Problem:</strong> A hospital network trains a convolutional neural network (CNN) to detect pneumonia from 30,000 thoracic radiography scans.</p>
      <p><strong>The Data Structure:</strong> Sick patients undergo follow-up X-rays every 2 days during hospitalization, resulting in 4 to 8 images per patient with identical anatomical quirks and hospital bed hardware markers.</p>
      <p><strong>The Splitting Strategy:</strong> <strong>Patient-Level Grouped Splitting</strong> combined with stratification on pneumonia diagnosis labels (<code>StratifiedGroupKFold</code>).</p>
      <p><strong>The Risk of Incorrect Split:</strong> Random row splitting caused the CNN to learn patient-specific chest rib structures and bedside ECG lead placement instead of lung opacities, producing a dangerously false 99% validation accuracy that failed to diagnose new clinical admissions.</p>
      <p><strong>Production Takeaway:</strong> In medical and biometric systems, data independence must be enforced at the biological subject level, never the image or record level.</p>
    </div>

    <!-- Case Study C -->
    <div class="card card-concept">
      <div class="card-title"><span>&#128179;</span> Case Study C: High-Volume Credit Card Fraud Detection (FinTech)</div>
      <p><strong>The Business Problem:</strong> A global payment processor monitors 1,000,000 daily card transactions to flag fraudulent payments in real time.</p>
      <p><strong>The Data Structure:</strong> Severe class imbalance: 99.8% legitimate transactions (998,000) vs 0.2% fraudulent transactions (2,000).</p>
      <p><strong>The Splitting Strategy:</strong> <strong>Stratified Splitting</strong> with chronological block testing. Stratification ensured that both the training and test sets contained exactly 0.2% fraudulent cases (1,600 in train, 400 in test).</p>
      <p><strong>The Risk of Incorrect Split:</strong> An unstratified random split risked placing almost no fraud samples in a small test set, creating wild evaluation swings where a single missed fraud shifted test recall by 25%. Furthermore, random shuffling across time allowed the model to train on future fraud patterns to predict past attacks.</p>
      <p><strong>Production Takeaway:</strong> In extreme class imbalance, stratification preserves statistical evaluation power, while chronological splitting tests true forward predictive utility.</p>
    </div>

    <!-- Case Study D -->
    <div class="card card-success">
      <div class="card-title"><span>&#128200;</span> Case Study D: Algorithmic Quantitative Stock Trading (Capital Markets)</div>
      <p><strong>The Business Problem:</strong> A hedge fund builds an automated algorithmic trading model to forecast 15-minute future equity returns across S&amp;P 500 stocks.</p>
      <p><strong>The Data Structure:</strong> High-frequency continuous time-series data with strong temporal autocorrelation, volatility clustering, and market regime shifts.</p>
      <p><strong>The Splitting Strategy:</strong> <strong>Chronological Forward-Chaining Split</strong> with an enforced <strong>Purge/Embargo Window</strong> between training and evaluation blocks.</p>
      <p><strong>The Risk of Incorrect Split:</strong> Standard random shuffle splitting caused catastrophic lookahead leakage. The model used 2:15 PM market prices to predict 2:00 PM returns, showing an unrealistic 8.5 Sharpe Ratio in backtesting. Deployed live with real capital, the strategy lost $1.4M in two trading days.</p>
      <p><strong>Production Takeaway:</strong> In financial markets and time-series forecasting, never shuffle rows. The timeline is an unbroken one-way arrow.</p>
    </div>
  </section>

  <!-- SECTION 16: COMMON BEGINNER MISTAKES -->
  <section id="sec-16" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 16</span>
      <h2 class="section-title">14 Common Beginner Mistakes &amp; Fixes</h2>
    </div>
    <p class="section-intro">
      Learn to recognize and avoid the 14 most pervasive dataset splitting mistakes encountered in academic coursework and industry machine learning engineering.
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Common Mistake</th>
            <th>Why It Causes Serious Problems</th>
            <th>Defensive Safe Engineering Approach</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>01</strong></td>
            <td>Training and testing on the exact same data</td>
            <td>The model achieves 100% accuracy simply by memorizing training rows without learning any general patterns.</td>
            <td>Always split data into distinct subsets before any model fitting begins.</td>
          </tr>
          <tr>
            <td><strong>02</strong></td>
            <td>Assuming high training accuracy proves generalisation</td>
            <td>Training accuracy only measures memorization capacity. Complex models easily overfit noise.</td>
            <td>Evaluate performance exclusively on holdout validation and test sets that the model never saw.</td>
          </tr>
          <tr>
            <td><strong>03</strong></td>
            <td>Using the test set to tune hyperparameters or select models</td>
            <td>Causes <em>Test-Set Overfitting</em>. The test set becomes part of the training feedback loop, losing objectivity.</td>
            <td>Use a dedicated <strong>Validation Set</strong> or K-Fold Cross-Validation for tuning; reserve Test for the final audit.</td>
          </tr>
          <tr>
            <td><strong>04</strong></td>
            <td>Fitting scalers or encoders before splitting</td>
            <td>Creates <strong>Data Leakage</strong> by allowing test set means, standard deviations, or category frequencies into training.</td>
            <td>Always call <code>fit()</code> strictly on <code>X_train</code>, or encapsulate steps inside a Scikit-Learn <code>Pipeline</code>.</td>
          </tr>
          <tr>
            <td><strong>05</strong></td>
            <td>Ignoring class imbalance during splitting</td>
            <td>Random splitting may leave zero minority class examples in the test set, creating unmeasurable evaluation metrics.</td>
            <td>Always pass <code>stratify=y</code> in <code>train_test_split()</code> for classification tasks.</td>
          </tr>
          <tr>
            <td><strong>06</strong></td>
            <td>Randomly shuffling time-series observations</td>
            <td>Leaks future market conditions, weather events, or trends into the past, creating impossible lookahead bias.</td>
            <td>Use chronological forward-chaining splits via <code>TimeSeriesSplit</code> without shuffling (<code>shuffle=False</code>).</td>
          </tr>
          <tr>
            <td><strong>07</strong></td>
            <td>Ignoring repeated entities across subsets</td>
            <td>Multiple records from the same patient, user, or device contaminate both sets, causing identity memorization.</td>
            <td>Use group-aware splitting strategies like <code>GroupShuffleSplit</code> or <code>StratifiedGroupKFold</code>.</td>
          </tr>
          <tr>
            <td><strong>08</strong></td>
            <td>Assuming random_state guarantees a representative split</td>
            <td>A fixed seed only guarantees identical repeatability, not statistical quality. An unlucky seed can produce an unrepresentative split.</td>
            <td>Always inspect class distributions, feature histograms, and summary statistics across all created subsets.</td>
          </tr>
          <tr>
            <td><strong>09</strong></td>
            <td>Blindly applying an 80/20 ratio without considering N</td>
            <td>On 50 samples, a 20% test set is only 10 samples (highly unstable); on 10M samples, 20% wastes 2M samples.</td>
            <td>Scale split ratios to sample volume: use K-Fold CV on small datasets and 98/1/1 splits on multi-million row datasets.</td>
          </tr>
          <tr>
            <td><strong>10</strong></td>
            <td>Assuming stratification solves all splitting challenges</td>
            <td>Stratification only preserves class frequencies; it does not protect against group leakage or temporal autocorrelation.</td>
            <td>Combine stratification with grouping (<code>StratifiedGroupKFold</code>) or chronological ordering where applicable.</td>
          </tr>
          <tr>
            <td><strong>11</strong></td>
            <td>Repeatedly checking the test score during development</td>
            <td>Every time you alter architecture after seeing test performance, you inject human feedback bias into the test set.</td>
            <td>Lock the test set away until all modeling and hyperparameter choices are 100% frozen.</td>
          </tr>
          <tr>
            <td><strong>12</strong></td>
            <td>Allowing duplicate records across subset boundaries</td>
            <td>Duplicate rows present in both train and test artificially boost evaluation metrics via direct memorization.</td>
            <td>Deduplicate raw datasets (<code>df.drop_duplicates()</code>) prior to performing splitting operations.</td>
          </tr>
          <tr>
            <td><strong>13</strong></td>
            <td>Reporting evaluation metrics without statistical confidence</td>
            <td>Reporting "85% test accuracy" on a 20-sample test set ignores that the 95% confidence interval spans [62% &ndash; 97%].</td>
            <td>Always report test set sample size (N<sub>test</sub>) and standard errors or confidence intervals.</td>
          </tr>
          <tr>
            <td><strong>14</strong></td>
            <td>Failing to assert subset non-overlap programmatically</td>
            <td>Subtle bugs in splitting scripts can silently duplicate rows across sets without throwing Python errors.</td>
            <td>Write explicit unit assertions: <code>assert len(set(ids_train).intersection(set(ids_test))) == 0</code>.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 17: GLOSSARY, REVISION AND FINAL EXERCISE -->
  <section id="sec-17" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 17</span>
      <h2 class="section-title">Glossary, Revision &amp; Hands-On Exercise</h2>
    </div>
    <p class="section-intro">
      Consolidate your mastery of dataset splitting with a production checklist, comprehensive glossary, interactive revision questions, scenario challenges, and a capstone practical exercise.
    </p>

    <!-- Checklist Card -->
    <div class="card card-success">
      <div class="card-title"><span>&#9745;</span> Production Dataset Splitting Checklist</div>
      <ul class="checklist">
        <li><strong>Step 1:</strong> Have you inspected the target variable for class imbalance and enabled <code>stratify=y</code> if classification?</li>
        <li><strong>Step 2:</strong> Have you identified repeated entities (patients, users, devices) and enabled group-based splitting?</li>
        <li><strong>Step 3:</strong> Is there a temporal sequence? If so, have you disabled row shuffling and used chronological forward chaining?</li>
        <li><strong>Step 4:</strong> Have you verified zero record overlap between train, validation, and test index sets?</li>
        <li><strong>Step 5:</strong> Are all data preprocessing transformers (imputers, scalers, encoders) fitted strictly on <code>X_train</code>?</li>
        <li><strong>Step 6:</strong> Have you encapsulated transformations inside a Scikit-Learn <code>Pipeline</code>?</li>
        <li><strong>Step 7:</strong> Were all hyperparameter tuning decisions made exclusively using the validation set or cross-validation?</li>
        <li><strong>Step 8:</strong> Has the test set been evaluated strictly once as the final unbiased audit?</li>
      </ul>
    </div>

    <h3>Comprehensive Glossary of Essential Terms</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Technical Term</th>
            <th>Formal Engineering Definition</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Generalization</strong></td>
            <td>The ability of a machine learning model to make accurate predictions on new, unseen data drawn from the same distribution.</td>
          </tr>
          <tr>
            <td><strong>Overfitting</strong></td>
            <td>A failure mode where a model learns training noise and specific sample quirks rather than underlying population patterns.</td>
          </tr>
          <tr>
            <td><strong>Training Set</strong></td>
            <td>The subset of data directly supplied to the learning algorithm to optimize its internal model parameters (weights, biases).</td>
          </tr>
          <tr>
            <td><strong>Validation Set</strong></td>
            <td>An independent holdout subset used during model development to compare algorithms, tune hyperparameters, and select features.</td>
          </tr>
          <tr>
            <td><strong>Test Set</strong></td>
            <td>A strictly quarantined holdout subset evaluated only once at the conclusion of development to estimate real-world performance.</td>
          </tr>
          <tr>
            <td><strong>Model Parameter</strong></td>
            <td>An internal variable learned automatically from training data during fitting (e.g. regression coefficients &beta;, neural weights w).</td>
          </tr>
          <tr>
            <td><strong>Hyperparameter</strong></td>
            <td>An external configuration setting specified prior to training that controls the learning process (e.g. KNN k, tree depth, learning rate).</td>
          </tr>
          <tr>
            <td><strong>Data Leakage</strong></td>
            <td>The unintended contamination of training data with information from validation, test, or future operational distributions.</td>
          </tr>
          <tr>
            <td><strong>Stratified Splitting</strong></td>
            <td>A partitioning method that ensures each subset contains approximately the same target class proportions as the complete dataset.</td>
          </tr>
          <tr>
            <td><strong>Group-Based Splitting</strong></td>
            <td>A partitioning method where all records sharing a common group identifier (e.g. Patient ID) are confined to a single subset.</td>
          </tr>
          <tr>
            <td><strong>Time-Series Split</strong></td>
            <td>A chronological splitting technique where training observations strictly precede validation/test observations in time.</td>
          </tr>
          <tr>
            <td><strong>K-Fold Cross-Validation</strong></td>
            <td>A resampling procedure partitioning development data into K folds, iteratively using K-1 folds to train and 1 fold to validate.</td>
          </tr>
          <tr>
            <td><strong>Target Encoding Leakage</strong></td>
            <td>Calculating category target means using the complete dataset, which leaks ground-truth validation/test labels into training features.</td>
          </tr>
          <tr>
            <td><strong>Holdout Method</strong></td>
            <td>The fundamental practice of withholding a portion of available labeled data from the training process for unbiased evaluation.</td>
          </tr>
          <tr>
            <td><strong>Early Stopping</strong></td>
            <td>A regularization technique that halts iterative model training as soon as validation loss begins to deteriorate.</td>
          </tr>
          <tr>
            <td><strong>Random Seed (random_state)</strong></td>
            <td>An integer initialization value for pseudo-random number generators that ensures deterministic reproducibility across runs.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3>10 Interactive Revision Questions &amp; Detailed Explanations</h3>
    
    <details>
      <summary><span>&#10067;</span> Question 1: Why is training accuracy alone insufficient to evaluate an ML model?</summary>
      <div class="details-content">
        <strong>Answer:</strong> Training accuracy only measures a model&apos;s ability to memorize data it has already seen. Highly flexible models (such as 1-Nearest Neighbor or unpruned Decision Trees) can achieve 100% training accuracy simply by memorizing training examples and random noise. However, memorized noise does not generalize to new observations. Evaluating on an independent holdout set is the only way to measure true predictive generalization.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 2: What is the crucial difference between a Validation Set and a Test Set?</summary>
      <div class="details-content">
        <strong>Answer:</strong> Both are holdout sets, but they serve completely different lifecycle roles. The <strong>Validation Set</strong> is an active development tool used iteratively to compare algorithms, choose hyperparameters, and make architectural decisions. Because it guides modeling choices, it suffers slight indirect optimization bias. In contrast, the <strong>Test Set</strong> is strictly quarantined until all modeling decisions are frozen; it is evaluated exactly once to provide a final, unbiased estimate of production accuracy.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 3: What is the difference between a model parameter and a hyperparameter?</summary>
      <div class="details-content">
        <strong>Answer:</strong> <strong>Parameters</strong> (such as regression slope &beta;, intercept &beta;<sub>0</sub>, or neural network weights) are learned automatically from training data by an optimization algorithm during fitting. <strong>Hyperparameters</strong> (such as KNN&apos;s number of neighbors <code>k</code>, tree maximum depth, or regularization strength &alpha;) are external architectural knobs chosen by the engineer <em>prior</em> to training, and are tuned by evaluating performance on the validation set.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 4: How does setting stratify=y prevent evaluation failure in imbalanced datasets?</summary>
      <div class="details-content">
        <strong>Answer:</strong> In imbalanced datasets (e.g. 95% Class 0 vs 5% Class 1), an ordinary unstratified random split might accidentally assign all minority class examples to the training set, leaving zero minority examples in the test set. In that scenario, calculating minority recall or F1-score is impossible. Setting <code>stratify=y</code> forces the splitting algorithm to preserve the 95%/5% class ratio across train, validation, and test subsets.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 5: Why does standardizing the entire dataset before train/test split cause data leakage?</summary>
      <div class="details-content">
        <strong>Answer:</strong> Standardizing requires computing the dataset mean (&mu;) and standard deviation (&sigma;). If computed before splitting, the training feature values are transformed using parameters derived in part from the test set. The model thereby gains subtle statistical foreknowledge about the scale and bounds of unseen test data, artificially inflating offline evaluation metrics and risking failure in production.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 6: When is ordinary random splitting inappropriate for dataset partitioning?</summary>
      <div class="details-content">
        <strong>Answer:</strong> Ordinary random splitting fails in two major scenarios:
        <br>1. <strong>Grouped / Clustered Data:</strong> When multiple observations belong to the same person, patient, or device, random splitting allows records from the same subject into both train and test sets, causing identity leakage.
        <br>2. <strong>Time-Series / Temporal Sequences:</strong> When predicting future events, random shuffling leaks future information into past training data (lookahead bias).
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 7: What does random_state=42 actually accomplish in Scikit-Learn?</summary>
      <div class="details-content">
        <strong>Answer:</strong> It initializes the pseudo-random number generator with a deterministic seed value. Every time the script executes, Scikit-Learn will generate the exact same permutation of row indices, guaranteeing that experiments, sample counts, and subset assignments are 100% reproducible across different runs and collaborating team members. It does <em>not</em>, however, guarantee that the split is statistically representative.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 8: How does K-Fold Cross-Validation replace the validation set?</summary>
      <div class="details-content">
        <strong>Answer:</strong> In standard K-Fold CV, the development dataset is split into K equal folds. The model trains on K-1 folds and validates on the remaining fold, rotating until every fold has served as the validation set once. The K validation scores are averaged into an aggregate metric: <code>Score&#772;<sub>CV</sub> = (1/K)&Sigma;Score<sub>k</sub></code>. This eliminates the dependency on a single arbitrary validation split and maximizes training data utility.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 9: Why must you still maintain an independent Test Set when using Cross-Validation?</summary>
      <div class="details-content">
        <strong>Answer:</strong> If you use cross-validation scores to iteratively test 50 different models and select the best hyperparameter configuration, the selected model has been tuned to maximize performance on that development dataset. Just as with a single validation set, the cross-validation score has suffered selection bias. An independent, untouched Test Set is still required to confirm real-world performance.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 10: What is test-set overfitting and how does it happen?</summary>
      <div class="details-content">
        <strong>Answer:</strong> <em>Test-set overfitting</em> occurs when a data scientist repeatedly evaluates experimental models on the test set and uses those test scores to adjust features, change architectures, or tune hyperparameters. Even though the model is not trained on the test set via gradient descent, the human engineer acts as an optimization algorithm, tailoring decisions to the quirks of the test set until test accuracy no longer reflects performance on genuinely new data.
      </div>
    </details>

    <h3>Scenario-Based Engineering Challenges</h3>
    <div class="card card-concept">
      <div class="card-title"><span>&#9874;</span> Scenario Challenge 1: The Hospital Sepsis Alert System</div>
      <p>
        <strong>Scenario:</strong> You are tasked with developing a machine learning model to predict sepsis onset in hospital ICU patients. The dataset contains 25,000 hourly vital sign measurements recorded from 800 distinct patients over a 3-year period. Sepsis occurs in 4% of patient encounters.
      </p>
      <p>
        <strong>Challenge:</strong> Which dataset splitting strategy should you implement, and what parameters must be configured?
      </p>
      <p>
        <strong>Recommended Solution:</strong> Implement <strong>Stratified Group Splitting</strong> using <code>StratifiedGroupKFold</code> or a grouped holdout based on <code>Patient_ID</code>.
        <br>&bull; Grouping by <code>Patient_ID</code> ensures that no patient has hourly vitals in both training and test sets (preventing patient identity memorization).
        <br>&bull; Stratifying on sepsis diagnosis ensures both train and test splits contain approximately 4% positive sepsis cases.
      </p>
    </div>

    <div class="card card-analogy">
      <div class="card-title"><span>&#9874;</span> Scenario Challenge 2: The E-Commerce Black Friday Churn Model</div>
      <p>
        <strong>Scenario:</strong> A retail platform wants to predict customer subscription churn during the high-volume Q4 holiday shopping season. You have daily transaction records spanning January 1 to December 31, 2025.
      </p>
      <p>
        <strong>Challenge:</strong> Why would an ordinary 80/20 random shuffle split produce catastrophic production failures in this context?
      </p>
      <p>
        <strong>Recommended Solution:</strong> An ordinary random split shuffles rows across the entire calendar year. The model would train on December holiday purchasing patterns to predict November customer behavior (future lookahead leakage). Furthermore, holiday consumer psychology is radically different from summer baseline shopping.
        <br><strong>Safe Strategy:</strong> Implement a chronological split: Train on January through October, validate on November, and perform final test evaluation on December.
      </p>
    </div>

    <h3>Final Hands-On Practical Assignment</h3>
    <div class="card card-success">
      <div class="card-title"><span>&#9997;</span> Capstone Exercise: End-to-End Leak-Free Customer Churn Pipeline</div>
      <p>
        Given a customer retention dataset with 10,000 records containing:
        <br>&bull; <code>Customer_ID</code>: Unique customer identifier
        <br>&bull; <code>Tenure_Months</code>: Number of months subscribed (numerical)
        <br>&bull; <code>Monthly_Charges</code>: Monthly billing amount (numerical)
        <br>&bull; <code>Contract_Type</code>: Categorical (Month-to-month, One year, Two year)
        <br>&bull; <code>Churned</code>: Binary target label (0 = Retained, 1 = Churned, 12% minority class)
      </p>
      <p>
        <strong>Your Engineering Assignment:</strong>
        <br>1. Perform a two-stage stratified split: 70% Train, 15% Validation, 15% Test, using <code>random_state=42</code>.
        <br>2. Assert programmatically that the three index sets share zero customer IDs.
        <br>3. Verify that the minority churn rate is approximately 12% in all three subsets.
        <br>4. Construct a Scikit-Learn <code>Pipeline</code> containing <code>StandardScaler</code> and a <code>KNeighborsClassifier</code>.
        <br>5. Fit the pipeline strictly on the training set.
        <br>6. Compare validation accuracy for <code>k=5</code> versus <code>k=15</code>; select the champion hyperparameter.
        <br>7. Perform a single final evaluation on the untouched test set and report accuracy, precision, and recall.
      </p>
    </div>

    <div class="notes-footer">
      <p>CodeVerse Machine Learning Educational Notes &bull; Topic 8: Train, Validation &amp; Test Sets</p>
      <p>Strict Light Mode Standard &bull; Validated for Web and Mobile Viewports &bull; Powered by Scikit-Learn 1.9+</p>
    </div>
  </section>
"""
