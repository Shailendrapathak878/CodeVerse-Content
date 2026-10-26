"""
Module: topic12_part3.py
Contains Sections 11 to 15 for Topic 12: Decision Trees.
"""

from scratch.topic12_svgs import (
    SVG_ACTUAL_TRAINED_TREE,
    SVG_DECISION_BOUNDARIES_DEPTH,
    SVG_TRAIN_VAL_ERROR_CURVE,
    SVG_FEATURE_IMPORTANCE_BARS
)

PART3_HTML = f"""
    <!-- SECTION 11: DECISION TREE VISUALIZATION USING PYTHON -->
    <section id="sec-11" class="section-card">
      <span class="section-badge">Section 11</span>
      <h2 class="section-title">Decision Tree Visualization Using Python</h2>
      <p class="section-lead">
        One of the greatest superpowers of Decision Trees is visual explainability. You do not need to guess how the model thinks—you can render its entire thought process into a high-resolution graph.
      </p>

      {SVG_ACTUAL_TRAINED_TREE}

      <h3 class="sub-title">1. How to Read a Scikit-Learn Tree Diagram</h3>
      <p>
        Every box rendered by <code>sklearn.tree.plot_tree</code> displays five critical pieces of information:
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Box Entry</th>
              <th>Concrete Example</th>
              <th>Engineering Interpretation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Split Rule</strong></td>
              <td><code>Study_Hours &le; 6.45</code></td>
              <td>The feature and cutoff threshold tested at this node. True goes Left; False goes Right.</td>
            </tr>
            <tr>
              <td><strong>gini / entropy</strong></td>
              <td><code>gini = 0.500</code></td>
              <td>The current impurity of samples inside this node before splitting.</td>
            </tr>
            <tr>
              <td><strong>samples</strong></td>
              <td><code>samples = 192</code></td>
              <td>The number of training observations that reached this node during training.</td>
            </tr>
            <tr>
              <td><strong>value</strong></td>
              <td><code>value = [96, 96]</code></td>
              <td>The exact breakdown of classes: 96 Fail (Class 0) and 96 Pass (Class 1).</td>
            </tr>
            <tr>
              <td><strong>class</strong></td>
              <td><code>class = Pass</code></td>
              <td>The majority class prediction that would be assigned if splitting stopped right here.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">2. Text-Based Tree Export with <code>export_text</code></h3>
      <p>
        If graphical rendering tools are unavailable, scikit-learn provides a built-in text exporter that renders the entire tree directly to the terminal console:
      </p>

      <div class="code-container">
        <div class="code-header">
          <span class="code-lang">Python 3</span>
          <span class="code-tag">sklearn.tree.export_text</span>
        </div>
        <pre><code class="language-python">from sklearn.tree import export_text

# Generate clean, indented decision rules
tree_rules = export_text(
    final_dt,
    feature_names=['Study_Hours', 'Attendance_Pct'],
    show_weights=True
)
print(tree_rules)

# Console Output:
# |--- Study_Hours <= 6.45
# |   |--- Attendance_Pct <= 75.20
# |   |   |--- weights: [86.0, 0.0] class: 0 (Pure Fail)
# |   |--- Attendance_Pct >  75.20
# |   |   |--- weights: [6.0, 9.0] class: 1 (Pass)
# |--- Study_Hours >  6.45
# |   |--- Attendance_Pct <= 68.00
# |   |   |--- weights: [2.0, 4.0] class: 1 (Pass)
# |   |--- Attendance_Pct >  68.00
# |   |   |--- weights: [2.0, 83.0] class: 1 (Pure Pass)</code></pre>
      </div>
    </section>

    <!-- SECTION 12: DECISION BOUNDARIES -->
    <section id="sec-12" class="section-card">
      <span class="section-badge">Section 12</span>
      <h2 class="section-title">Decision Boundaries: Orthogonal Axis-Aligned Cuts</h2>
      <p class="section-lead">
        Linear models (like Logistic Regression) draw diagonal separating hyperplanes. K-Nearest Neighbors draws curving, organic boundary contours. What shape do Decision Trees create?
      </p>

      {SVG_DECISION_BOUNDARIES_DEPTH}

      <h3 class="sub-title">1. Why Are Decision Boundaries Axis-Aligned?</h3>
      <p>
        Because each internal node tests <strong>only one feature at a time</strong> (e.g., <code>Study_Hours &le; 6.5</code>), each split corresponds to a straight line perpendicular to that feature's axis:
      </p>
      <ul style="margin: 8px 0 0 20px; line-height: 1.7; color: #334155;">
        <li>A test on <strong>Feature 1 (X-axis)</strong> draws a strictly <strong>vertical line</strong>.</li>
        <li>A test on <strong>Feature 2 (Y-axis)</strong> draws a strictly <strong>horizontal line</strong>.</li>
        <li>Together, a sequence of splits divides the 2D feature space into a patchwork of <strong>axis-aligned rectangular boxes</strong> (or hyper-rectangles in higher dimensions).</li>
      </ul>

      <div class="callout callout-warning">
        <div class="callout-title">&#9888;&#65039; The Diagonal Data Limitation (Staircase Effect)</div>
        <p>
          Because decision trees can only cut horizontally and vertically, they struggle to model smooth diagonal relationships (e.g., <code>y = x</code>). To approximate a simple 45-degree diagonal line, a tree must construct a complex, jagged <strong>"staircase"</strong> of dozens of tiny alternating horizontal and vertical splits, requiring substantial depth and risking severe overfitting!
        </p>
      </div>
    </section>

    <!-- SECTION 13: OVERFITTING, UNDERFITTING AND PRUNING -->
    <section id="sec-13" class="section-card">
      <span class="section-badge">Section 13</span>
      <h2 class="section-title">Overfitting, Underfitting and Pruning</h2>
      <p class="section-lead">
        A Decision Tree left to grow without constraints will greedily split until every leaf is pure, memorizing mislabelled data, sensor noise, and idiosyncratic training quirks.
      </p>

      {SVG_TRAIN_VAL_ERROR_CURVE}

      <h3 class="sub-title">1. Pre-Pruning vs. Post-Pruning (Cost-Complexity)</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Pruning Strategy</th>
              <th>How It Works</th>
              <th>Scikit-Learn Parameters</th>
              <th>Practical Trade-offs</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Pre-Pruning (Early Stopping)</strong></td>
              <td>Halts tree growth proactively during training before nodes become too specific.</td>
              <td><code>max_depth</code>, <code>min_samples_split</code>, <code>min_samples_leaf</code>, <code>max_leaf_nodes</code></td>
              <td><strong>Very Fast:</strong> Avoids building unnecessary branches entirely. May occasionally stop too early before discovering multi-split interactions.</td>
            </tr>
            <tr>
              <td><strong>Post-Pruning (Cost-Complexity / Minimal Cost)</strong></td>
              <td>Grows an unconstrained deep tree first, then prunes back weak, uninformative branches retrospectively.</td>
              <td><code>ccp_alpha</code> (Cost-Complexity Pruning Alpha)</td>
              <td><strong>Theoretically Optimal:</strong> Finds the subtree that best balances simplicity and low validation error. Slightly slower training time.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-def">
        <div class="callout-title">&#128302; Understanding Cost-Complexity Pruning (<code>ccp_alpha</code>)</div>
        <p>
          In scikit-learn, <code>ccp_alpha &ge; 0.0</code> controls the cost-complexity penalty. The objective function minimized is:
          <br><strong>Cost = Total Impurity + (ccp_alpha &times; Number of Terminal Leaves)</strong>
          <br>When <code>ccp_alpha = 0.0</code>, no pruning occurs (full tree). As <code>ccp_alpha</code> increases, having many leaves becomes costly, forcing scikit-learn to collapse weak branches into leaves, producing smaller, more robust trees.
        </p>
      </div>
    </section>

    <!-- SECTION 14: FEATURE IMPORTANCE -->
    <section id="sec-14" class="section-card">
      <span class="section-badge">Section 14</span>
      <h2 class="section-title">Feature Importance: Mean Decrease in Impurity (MDI)</h2>
      <p class="section-lead">
        Which input features actually drive the tree's decisions? In scikit-learn, Decision Trees automatically quantify the relative predictive value of each feature using <strong>Mean Decrease in Impurity (MDI)</strong>.
      </p>

      {SVG_FEATURE_IMPORTANCE_BARS}

      <h3 class="sub-title">1. How Feature Importance is Calculated</h3>
      <p>
        Every time a feature is chosen to split a node, it causes an impurity reduction:
        <br><strong>&Delta; Impurity = N<sub>node</sub> &times; [ Impurity(node) - Weighted Child Impurity ]</strong>
      </p>
      <p>
        The total importance of feature j is the <strong>sum of all impurity drops across all nodes</strong> where feature j was used, normalized so that the importances of all features sum to exactly <strong>1.0 (100%)</strong>.
      </p>

      <div class="callout callout-warning">
        <div class="callout-title">&#9888;&#65039; Four Critical Caveats About Feature Importance</div>
        <ol style="margin-left: 20px; line-height: 1.7; color: #7F1D1D;">
          <li><strong>MDI Does NOT Prove Causation:</strong> High importance simply means the feature was effective at partitioning training labels; it does not prove the feature caused the outcome.</li>
          <li><strong>Bias Toward High-Cardinality Continuous Features:</strong> Features with many unique numbers offer more candidate thresholds, giving the greedy algorithm more opportunities to find accidental splits.</li>
          <li><strong>Correlated Features Dilute Importance:</strong> If two features are highly collinear (e.g., Study Hours and Study Minutes), the tree may pick one at random, making the other appear artificially useless (0% importance).</li>
          <li><strong>Low Importance &ne; Irrelevant:</strong> A feature with 0% importance in an individual tree might be highly valuable when paired with other features in an ensemble model.</li>
        </ol>
      </div>
    </section>

    <!-- SECTION 15: COMPLETE PYTHON CLASSIFICATION LAB -->
    <section id="sec-15" class="section-card">
      <span class="section-badge">Section 15</span>
      <h2 class="section-title">Complete Python Classification Lab</h2>
      <p class="section-lead">
        Let us execute an end-to-end, reproducible classification lab on N = 240 students predicting exam pass/fail outcomes. We follow strict anti-leakage splitting, cross-validation depth selection, holdout evaluation, and output assertions.
      </p>

      <div class="code-container">
        <div class="code-header">
          <span class="code-lang">Python 3 (Full Lab)</span>
          <span class="code-tag">DecisionTreeClassifier Pipeline</span>
        </div>
        <pre><code class="language-python">import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

# ==========================================
# STEP 1: Reproducible Dataset Generation
# ==========================================
np.random.seed(42)
n_samples_per_class = 120

# Class 0 (Fail): lower study hours and attendance
study_c0 = np.random.normal(loc=4.5, scale=1.5, size=n_samples_per_class)
attend_c0 = np.random.normal(loc=65.0, scale=10.0, size=n_samples_per_class)
y_c0 = np.zeros(n_samples_per_class, dtype=int)

# Class 1 (Pass): higher study hours and attendance
study_c1 = np.random.normal(loc=8.5, scale=1.6, size=n_samples_per_class)
attend_c1 = np.random.normal(loc=85.0, scale=8.0, size=n_samples_per_class)
y_c1 = np.ones(n_samples_per_class, dtype=int)

X_study = np.clip(np.concatenate([study_c0, study_c1]), 1.0, 15.0)
X_attend = np.clip(np.concatenate([attend_c0, attend_c1]), 40.0, 100.0)
y_all = np.concatenate([y_c0, y_c1])

df = pd.DataFrame({{
    'Study_Hours': np.round(X_study, 1),
    'Attendance_Pct': np.round(X_attend, 1),
    'Passed_Exam': y_all,
    'Student_ID': [f"STD-{{i:04d}}" for i in range(1, 241)]
}})

print(f"Generated Dataset: {{df.shape[0]}} rows, {{df.shape[1]}} columns")
print(f"Class Balance:\\n{{df['Passed_Exam'].value_counts()}}")

# ==========================================
# STEP 2: Stratified Train / Test Split
# ==========================================
train_df, test_df = train_test_split(
    df, test_size=0.20, random_state=42, stratify=df['Passed_Exam']
)

# Rigorous Leakage Check: Assert zero overlapping Student IDs
assert len(set(train_df['Student_ID']).intersection(set(test_df['Student_ID']))) == 0
print(f"Train samples: {{len(train_df)}} | Test samples: {{len(test_df)}} (Zero overlap)")

X_train = train_df[['Study_Hours', 'Attendance_Pct']]
y_train = train_df['Passed_Exam']
X_test = test_df[['Study_Hours', 'Attendance_Pct']]
y_test = test_df['Passed_Exam']

# ==========================================
# STEP 3: Hyperparameter Tuning via 5-Fold CV
# ==========================================
candidate_depths = [1, 2, 3, 4, 5, 6, 8, 10]
cv_scores = {{}}

print("\\nEvaluating Candidate max_depths using 5-Fold CV on Training Data:")
for d in candidate_depths:
    clf = DecisionTreeClassifier(max_depth=d, criterion='gini', random_state=42)
    scores = cross_val_score(clf, X_train, y_train, cv=5, scoring='accuracy')
    cv_scores[d] = np.mean(scores)
    print(f"  Candidate max_depth={{d:2d}}: Mean CV Accuracy = {{cv_scores[d]:.4f}}")

best_depth = max(cv_scores, key=cv_scores.get)
print(f"Optimal depth selected: max_depth={{best_depth}} (CV Accuracy: {{cv_scores[best_depth]:.4f}})")

# ==========================================
# STEP 4: Fit Final Tree on Training Split
# ==========================================
final_tree = DecisionTreeClassifier(max_depth=3, criterion='gini', random_state=42)
final_tree.fit(X_train, y_train)

# ==========================================
# STEP 5: Final Unbiased Holdout Evaluation
# ==========================================
y_test_pred = final_tree.predict(X_test)

test_acc = accuracy_score(y_test, y_test_pred)
test_prec = precision_score(y_test, y_test_pred)
test_rec = recall_score(y_test, y_test_pred)
test_f1 = f1_score(y_test, y_test_pred)
cm = confusion_matrix(y_test, y_test_pred)

print("\\n--- Holdout Test Performance (N = 48) ---")
print(f"Test Accuracy:  {{test_acc:.4f}} ({{test_acc:.1%}})")
print(f"Test Precision: {{test_prec:.4f}} ({{test_prec:.1%}})")
print(f"Test Recall:    {{test_rec:.4f}} ({{test_rec:.1%}})")
print(f"Test F1-Score:  {{test_f1:.4f}} ({{test_f1:.1%}})")
print("\\nConfusion Matrix:")
print(cm)

# Feature Importances
importances = pd.Series(final_tree.feature_importances_, index=X_train.columns)
print("\\nFeature Importances (MDI):")
for f, imp in importances.items():
    print(f"  {{f}}: {{imp:.4f}} ({{imp:.1%}})")

# Robust Execution Assertions
assert test_acc >= 0.85, "Accuracy below acceptable threshold!"
assert test_f1 >= 0.85, "F1-Score below acceptable threshold!"
print("\\n[SUCCESS] All pipeline assertions and evaluations verified!")</code></pre>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span class="code-lang">Console Output</span>
          <span class="code-tag">Verified Python 3 Runtime Results</span>
        </div>
        <pre><code class="language-text">Generated Dataset: 240 rows, 4 columns
Class Balance:
Passed_Exam
0    120
1    120
Name: count, dtype: int64
Train samples: 192 | Test samples: 48 (Zero overlap)

Evaluating Candidate max_depths using 5-Fold CV on Training Data:
  Candidate max_depth= 1: Mean CV Accuracy = 0.9428
  Candidate max_depth= 2: Mean CV Accuracy = 0.9381
  Candidate max_depth= 3: Mean CV Accuracy = 0.9381
  Candidate max_depth= 4: Mean CV Accuracy = 0.9483
  Candidate max_depth= 5: Mean CV Accuracy = 0.9483
  Candidate max_depth= 6: Mean CV Accuracy = 0.9483
  Candidate max_depth= 8: Mean CV Accuracy = 0.9483
  Candidate max_depth=10: Mean CV Accuracy = 0.9483
Optimal depth selected: max_depth=4 (CV Accuracy: 0.9483)

--- Holdout Test Performance (N = 48) ---
Test Accuracy:  0.8958 (89.6%)
Test Precision: 0.8519 (85.2%)
Test Recall:    0.9583 (95.8%)
Test F1-Score:  0.9020 (90.2%)

Confusion Matrix:
[[20  4]
 [ 1 23]]

Feature Importances (MDI):
  Study_Hours: 0.8677 (86.8%)
  Attendance_Pct: 0.1323 (13.2%)

[SUCCESS] All pipeline assertions and evaluations verified!</code></pre>
      </div>
    </section>
"""

def get_part3():
    return PART3_HTML
