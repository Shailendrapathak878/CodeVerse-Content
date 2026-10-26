# Topic 22 - Part 3 (Sections 13 - 18)
# High quality, beginner-friendly ML notes

PART_3_HTML = """
    <!-- SECTION 13: INTERPRETING CV SCORES -->
    <section class="content-section" id="sec-13">
      <div class="section-tag">Section 13</div>
      <h2 class="section-title">Interpreting Cross-Validation Scores and Variance</h2>
      <p class="section-intro">
        When evaluating model configurations, beginners often focus solely on the <code>mean_test_score</code>, declaring whatever candidate scored 0.001 higher as the undisputed champion. In reality, a candidate's <strong>score variability (standard deviation across folds)</strong> is just as vital as its mean.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 13.1 — Candidate Configurations with Cross-Validation Error Bars</span>
          <span class="visual-tag">Variance Analysis</span>
        </div>
        __SVG_CV_SCORE_VARIABILITY__
        <div class="visual-caption">
          Figure 13.1 displays mean accuracy alongside &plusmn; 1 standard deviation error bars for candidate configurations from our KNN experiment. While <em>k</em> = 7 achieves the highest mean (0.9714), notice that its error bar overlaps significantly with <em>k</em> = 9 (0.9692 &plusmn; 0.0162), which exhibits even tighter stability.
        </div>
      </div>

      <h3>Mean Score vs. Fold-to-Fold Stability</h3>
      <p>
        Consider two hypothetical candidate models evaluated across 5 folds:
      </p>
      <ul>
        <li><strong>Candidate A:</strong> Fold scores [0.99, 0.98, 0.90, 0.99, 0.94] &rarr; Mean = 0.960, Std = <strong>0.034</strong></li>
        <li><strong>Candidate B:</strong> Fold scores [0.95, 0.96, 0.95, 0.96, 0.95] &rarr; Mean = 0.954, Std = <strong>0.005</strong></li>
      </ul>
      <p>
        Although Candidate A has a slightly higher mean score (0.960 vs. 0.954), Candidate B is vastly more stable and reliable. Candidate A's high standard deviation indicates that its performance is sensitive to the specific training sample—a warning sign of subtle overfitting. In mission-critical systems, an engineer will often prefer Candidate B.
      </p>

      <div class="card card-strategy">
        <div class="card-title">📐 The "One Standard Error Rule" (Hastie et al.)</div>
        <p>
          A widely respected heuristic in statistical learning is the <em>One Standard Error Rule</em>: when selecting among multiple competing hyperparameter settings, identify the candidate with the highest numerical score, and then <strong>select the simplest or most regularized model whose score falls within 1 standard error of that peak</strong>. This intentionally protects your project against selecting overly complex models due to random sampling fluctuations.
        </p>
      </div>
    </section>

    <!-- SECTION 14: ALGORITHM HYPERPARAMETERS -->
    <section class="content-section" id="sec-14">
      <div class="section-tag">Section 14</div>
      <h2 class="section-title">Hyperparameters of Common ML Algorithms</h2>
      <p class="section-intro">
        Every machine learning family has its own distinct set of architectural and regularization hyperparameters. Understanding the mechanical purpose of each knob enables you to define sensible, targeted search spaces rather than guessing blindly.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 14.1 — Hyperparameter Map Across Core Machine Learning Algorithms</span>
          <span class="visual-tag">Architectural Cheat Sheet</span>
        </div>
        __SVG_ALGORITHM_HYPERPARAMS_MAP__
        <div class="visual-caption">
          Figure 14.1 maps out the primary external hyperparameters governing KNN, Decision Trees, Random Forests, Support Vector Machines, Linear Regularized Models, and Gradient Boosting.
        </div>
      </div>

      <h3>Comprehensive Hyperparameter Reference Guide</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Algorithm Family</th>
              <th>Key Hyperparameter</th>
              <th>Typical Search Range</th>
              <th>Low Value Effect</th>
              <th>High Value Effect</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td rowspan="3"><strong>KNN</strong></td>
              <td><code>n_neighbors</code> (<em>k</em>)</td>
              <td>3 to 31 (prefer odd integers)</td>
              <td>Complex boundaries, high variance, overfits noise.</td>
              <td>Oversmoothed boundaries, high bias, dilutes local patterns.</td>
            </tr>
            <tr>
              <td><code>weights</code></td>
              <td><code>['uniform', 'distance']</code></td>
              <td>All <em>k</em> neighbors vote equally.</td>
              <td>Closer neighbors exert higher voting weight.</td>
            </tr>
            <tr>
              <td><code>p</code> (Minkowski metric)</td>
              <td>1 (Manhattan) or 2 (Euclidean)</td>
              <td>Grid-aligned L<sub>1</sub> distance.</td>
              <td>Straight-line Euclidean L<sub>2</sub> distance.</td>
            </tr>
            <tr>
              <td rowspan="3"><strong>Decision Trees</strong></td>
              <td><code>max_depth</code></td>
              <td>2 to 15 or <code>None</code></td>
              <td>Shallow tree, decision stumps, underfitting.</td>
              <td>Deep branches, memorizes training samples, severe overfitting.</td>
            </tr>
            <tr>
              <td><code>min_samples_split</code></td>
              <td>2 to 20 (integer)</td>
              <td>Allows nodes with very few samples to split.</td>
              <td>Constrains tree growth, forcing generalization.</td>
            </tr>
            <tr>
              <td><code>min_samples_leaf</code></td>
              <td>1 to 10 (integer)</td>
              <td>Allows single isolated sample in leaf (overfit).</td>
              <td>Smooths predictions by requiring multi-sample consensus.</td>
            </tr>
            <tr>
              <td rowspan="3"><strong>Random Forest</strong></td>
              <td><code>n_estimators</code></td>
              <td>100 to 500</td>
              <td>Noisier ensemble predictions.</td>
              <td>Stabilizes variance; performance plateaus without overfitting.</td>
            </tr>
            <tr>
              <td><code>max_features</code></td>
              <td><code>['sqrt', 'log2', None]</code></td>
              <td>Strong tree decorrelation, reduces variance.</td>
              <td>Trees become similar, ensemble diversity decreases.</td>
            </tr>
            <tr>
              <td><code>min_samples_leaf</code></td>
              <td>1 to 5</td>
              <td>Allows deep leaves.</td>
              <td>Prunes forest trees, reducing RAM footprint.</td>
            </tr>
            <tr>
              <td rowspan="2"><strong>Support Vector Machine (SVM)</strong></td>
              <td><code>C</code> (Regularization)</td>
              <td>10<sup>-3</sup> to 10<sup>3</sup></td>
              <td>Soft margin, permits misclassifications (high bias).</td>
              <td>Hard margin, strictly penalizes errors (overfitting risk).</td>
            </tr>
            <tr>
              <td><code>gamma</code> (RBF Kernel)</td>
              <td><code>'scale'</code>, <code>'auto'</code>, or 10<sup>-4</sup> to 10<sup>1</sup></td>
              <td>Broad, smooth Gaussian bell; large influence radius.</td>
              <td>Tight, peaked Gaussian spikes; memorizes training points.</td>
            </tr>
            <tr>
              <td><strong>Logistic Regression</strong></td>
              <td><code>C</code> (1/&lambda; inverse penalty)</td>
              <td>10<sup>-4</sup> to 10<sup>2</sup></td>
              <td>Strong shrinkage toward zero weights (prevents overfitting).</td>
              <td>Weak penalty, approaches unregularized Maximum Likelihood.</td>
            </tr>
            <tr>
              <td><strong>Ridge / Lasso</strong></td>
              <td><code>alpha</code> (&lambda; penalty)</td>
              <td>10<sup>-4</sup> to 10<sup>3</sup></td>
              <td>Zero penalty &rarr; Ordinary Least Squares regression.</td>
              <td>Heavy shrinkage; Lasso zeroes out irrelevant coefficients.</td>
            </tr>
            <tr>
              <td rowspan="2"><strong>Gradient Boosting</strong></td>
              <td><code>learning_rate</code></td>
              <td>0.01 to 0.2</td>
              <td>Small updates per tree; requires more <code>n_estimators</code>.</td>
              <td>Aggressive updates; fast convergence but risks overshooting.</td>
            </tr>
            <tr>
              <td><code>max_depth</code></td>
              <td>2 to 6</td>
              <td>Weak learners (decision stumps / shallow trees).</td>
              <td>Overly complex individual trees; rapid overfitting.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card card-warn">
        <div class="card-title">⚠️ Watch Out for Incompatible Solver &amp; Penalty Combinations</div>
        <p>
          In scikit-learn's <code>LogisticRegression</code>, not every solver supports every penalty:
        </p>
        <ul>
          <li>The default solver <code>'lbfgs'</code> supports <code>penalty='l2'</code> and <code>None</code>, but <strong>crashes</strong> if paired with <code>penalty='l1'</code>!</li>
          <li>To tune between L1 and L2 penalties in the same grid, you must configure <code>solver='saga'</code> or <code>'liblinear'</code>. Always verify parameter compatibility before launching a long grid search.</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 15: CHOOSING THE SCORING METRIC -->
    <section class="content-section" id="sec-15">
      <div class="section-tag">Section 15</div>
      <h2 class="section-title">Choosing the Correct Scoring Metric</h2>
      <p class="section-intro">
        Hyperparameter optimization is a mathematical pursuit: the search algorithm is an optimization machine that blindly drives the model toward whatever objective function you provide. If you choose the wrong scoring metric, you will successfully optimize for the wrong outcome.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 15.1 — Scoring Metric Decision Guide</span>
          <span class="visual-tag">Evaluation Framework</span>
        </div>
        __SVG_METRIC_SELECTION_GUIDE__
        <div class="visual-caption">
          Figure 15.1 provides a structured decision path for choosing evaluation metrics across classification (Accuracy, Precision, Recall, F1, ROC-AUC) and regression tasks (MAE, RMSE, R<sup>2</sup>), emphasizing class imbalance considerations.
        </div>
      </div>

      <h3>Why Accuracy Fails on Imbalanced Datasets</h3>
      <p>
        Consider a medical screening dataset where only 1% of patients have a rare malignant condition (99% are healthy). A trivial model that predicts "Healthy" for every single person achieves an astounding <strong>99.0% Accuracy</strong> while completely failing to identify a single sick patient!
      </p>
      <ul>
        <li><strong>Recall (Sensitivity):</strong> TP / (TP + FN). Use when False Negatives are fatal (Cancer diagnosis, fraud detection, structural flaw detection).</li>
        <li><strong>Precision:</strong> TP / (TP + FP). Use when False Positives are expensive (Spam email filtering, loan approvals, automated customer blocking).</li>
        <li><strong>F1-Score:</strong> Harmonic mean of Precision and Recall. Balances both concerns.</li>
        <li><strong>ROC-AUC:</strong> Measures how well the model ranks positive instances higher than negative instances across all possible classification probability thresholds.</li>
      </ul>

      <h3>Actual Multi-Metric Evaluation of Our Tuned KNN Model</h3>
      <p>
        Here is the genuine multi-metric audit for our best tuned KNN model (<em>k</em> = 7) evaluated on the untouched 114-sample holdout test set:
      </p>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Evaluation Metric</th>
              <th>Score on Holdout Test Set</th>
              <th>Practical Interpretation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Accuracy</strong></td>
              <td><strong>0.9737 (97.37%)</strong></td>
              <td>111 out of 114 test samples correctly classified.</td>
            </tr>
            <tr>
              <td><strong>Precision (Benign)</strong></td>
              <td><strong>0.9600 (96.00%)</strong></td>
              <td>When model predicts Benign, it is correct 96.0% of the time.</td>
            </tr>
            <tr style="background-color: #DCFCE7; font-weight: 700;">
              <td><strong>Recall (Benign)</strong></td>
              <td><strong>1.0000 (100.0%)</strong></td>
              <td><span style="color: #15803D;">Flawless:</span> Caught 100% of all Benign tumors with zero misses!</td>
            </tr>
            <tr>
              <td><strong>F1-Score</strong></td>
              <td><strong>0.9796 (97.96%)</strong></td>
              <td>Excellent harmonic balance between precision and recall.</td>
            </tr>
            <tr>
              <td><strong>ROC-AUC</strong></td>
              <td><strong>0.9884 (98.84%)</strong></td>
              <td>Near-perfect rank ordering of class probabilities.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card card-def">
        <div class="card-title">Scikit-Learn Convention: The "Greater Is Better" Rule</div>
        <p>
          In scikit-learn, all search estimators follow the convention that <em>higher scores represent better models</em>. For loss functions where lower is naturally better (such as Mean Squared Error or Mean Absolute Error), scikit-learn negates the values:
          <code>scoring='neg_mean_squared_error'</code> or <code>'neg_mean_absolute_error'</code>. A score of $-0.15$ is better than $-0.45$!
        </p>
      </div>
    </section>

    <!-- SECTION 16: OVERFITTING DURING TUNING -->
    <section class="content-section" id="sec-16">
      <div class="section-tag">Section 16</div>
      <h2 class="section-title">Overfitting During Hyperparameter Tuning: Selection Bias</h2>
      <p class="section-intro">
        Most practitioners know that a model can overfit training data. But few beginners realize that <strong>the hyperparameter tuning process itself can overfit the validation data</strong>!
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 16.1 — Safe vs Unsafe Model Selection Workflows</span>
          <span class="visual-tag">Protocol Integrity</span>
        </div>
        __SVG_SAFE_MODEL_SELECTION__
        <div class="visual-caption">
          Figure 16.1 contrasts an unsafe protocol (evaluating 500 candidates directly on the test set, creating massive selection bias) with the robust protocol (keeping the test set isolated in a vault until a single winning model is selected via cross-validation).
        </div>
      </div>

      <h3>How Validation Snooping Happens</h3>
      <p>
        If you test 10,000 different hyperparameter combinations on a 5-fold cross-validation split, you are effectively running 10,000 distinct statistical hypothesis tests on the same dataset. By sheer random chance, one or two configurations will exploit the idiosyncratic noise of those particular folds and score higher than they deserve.
      </p>
      <p>
        This phenomenon is known as <strong>multiple testing bias</strong> or <strong>model selection bias</strong>:
      </p>
      <ul>
        <li>The <code>best_score_</code> reported by <code>GridSearchCV</code> is often slightly optimistic compared to true future performance.</li>
        <li>This is why an independent, untouched <strong>Holdout Test Set</strong> is mandatory: it serves as the ultimate impartial judge, evaluated exactly once.</li>
      </ul>
    </section>

    <!-- SECTION 17: DATA LEAKAGE AND PIPELINES -->
    <section class="content-section" id="sec-17">
      <div class="section-tag">Section 17</div>
      <h2 class="section-title">Data Leakage and Safe Scikit-Learn Pipelines</h2>
      <p class="section-intro">
        <strong>Data leakage</strong> occurs when information from outside the training partition is inadvertently shared with the model during training or feature engineering. In hyperparameter tuning, naive preprocessing is the #1 culprit of data leakage.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 17.1 — Preprocessing Inside vs. Outside Cross-Validation Folds</span>
          <span class="visual-tag">Data Leakage Architecture</span>
        </div>
        __SVG_DATA_LEAKAGE_COMPARISON__
        <div class="visual-caption">
          Figure 17.1 illustrates why preprocessing must happen inside the cross-validation loop. In the top diagram, calling <code>fit_transform</code> on the entire dataset leaks the global mean and standard deviation of validation samples into the training step. In the bottom diagram, a scikit-learn <code>Pipeline</code> fits the scaler exclusively on training folds.
        </div>
      </div>

      <h3>The Classic Preprocessing Leakage Trap</h3>
      <div class="code-block-wrapper">
        <div class="code-header">
          <span>❌ The Flawed Leaky Approach (Never Do This!)</span>
          <span class="code-lang">Python</span>
        </div>
        <pre><code># FLAWED: Scaler learns mean & std from the ENTIRE dataset (including validation folds!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)   # &lt;-- LEAKAGE OCCURS HERE!

# When cross_val_score splits X_scaled into folds, the training folds
# already contain leaked statistical information about the validation fold!
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid_search.fit(X_scaled, y)         # &lt;-- Optimistic, untrustworthy score</code></pre>
      </div>

      <div class="code-block-wrapper">
        <div class="code-header">
          <span>✅ The Robust Pipeline Approach (Always Do This!)</span>
          <span class="code-lang">Python</span>
        </div>
        <pre><code>from sklearn.pipeline import Pipeline

# ROBUST: Encapsulate scaler and estimator inside a Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

# Pass raw X_train into GridSearchCV.
# During each fold, StandardScaler.fit() is called STRICTLY on the training fold!
grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)    # &lt;-- 100% Leakage-Free and Mathematically Sound</code></pre>
      </div>
    </section>

    <!-- SECTION 18: LEARNING AND VALIDATION CURVES -->
    <section class="content-section" id="sec-18">
      <div class="section-tag">Section 18</div>
      <h2 class="section-title">Diagnostic Curves: Learning Curves vs. Validation Curves</h2>
      <p class="section-intro">
        Diagnostic curves transform hyperparameter tuning from a black-box trial-and-error game into an interpretable scientific study. Two fundamental diagnostic curves reveal whether your model is suffering from high bias or high variance.
      </p>

      <h3>1. Validation Curve: Isolating a Single Hyperparameter</h3>
      <p>
        A <strong>Validation Curve</strong> plots both training performance and validation performance as a function of a <em>single hyperparameter's value</em> (while keeping all other settings fixed).
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 18.2 — Actual Validation Curve: Decision Tree max_depth (1 to 15)</span>
          <span class="visual-tag">Actual Experimental Execution</span>
        </div>
        __SVG_ACTUAL_VALIDATION_CURVE__
        <div class="visual-caption">
          Figure 18.2 displays genuine experimental validation curve data from our executed script. At <code>max_depth=1</code>, the model underfits (validation score 0.8967). Validation score peaks at <code>max_depth=4</code> (0.9385). Beyond depth 4, training accuracy surges to 100.0% while validation accuracy decays to 0.9099, establishing an overfitting gap of 0.0901.
        </div>
      </div>

      <h3>Actual Experimental Values: Decision Tree max_depth</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Tree Depth</th>
              <th>Training Accuracy</th>
              <th>5-Fold Validation Accuracy</th>
              <th>Generalization Gap</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>depth = 1</code></td>
              <td>0.9258</td>
              <td>0.8967</td>
              <td>0.0291</td>
              <td>Underfitting (stump too simple)</td>
            </tr>
            <tr>
              <td><code>depth = 2</code></td>
              <td>0.9571</td>
              <td>0.9187</td>
              <td>0.0385</td>
              <td>Improving fit</td>
            </tr>
            <tr>
              <td><code>depth = 3</code></td>
              <td>0.9802</td>
              <td>0.9253</td>
              <td>0.0549</td>
              <td>Strong fit</td>
            </tr>
            <tr style="background-color: #DCFCE7; font-weight: 700;">
              <td><code>depth = 4 (Peak)</code></td>
              <td>0.9912</td>
              <td>0.9385</td>
              <td>0.0527</td>
              <td><span style="color: #15803D;">Optimal Sweet Spot: Peak Validation Score</span></td>
            </tr>
            <tr>
              <td><code>depth = 5</code></td>
              <td>0.9940</td>
              <td>0.9319</td>
              <td>0.0621</td>
              <td>Slight variance increase</td>
            </tr>
            <tr>
              <td><code>depth = 6</code></td>
              <td>0.9967</td>
              <td>0.9187</td>
              <td>0.0780</td>
              <td>Overfitting emerging</td>
            </tr>
            <tr>
              <td><code>depth = 8 to 15</code></td>
              <td>1.0000 (100.0%)</td>
              <td>0.9099</td>
              <td>0.0901</td>
              <td><span style="color: #DC2626;">Severe Overfitting:</span> Memorizes training set completely</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>2. Learning Curve: Diagnosis Across Dataset Size</h3>
      <p>
        A <strong>Learning Curve</strong> plots training score and validation score as the <em>sample size of the training dataset increases</em> ($N=36$ to $N=364$), evaluating our tuned KNN model ($k=7$).
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 18.1 — Actual Learning Curve: Sample Size vs Performance for Tuned KNN</span>
          <span class="visual-tag">Actual Experimental Execution</span>
        </div>
        __SVG_ACTUAL_LEARNING_CURVE__
        <div class="visual-caption">
          Figure 18.1 plots genuine executed learning curve data. As training data increases from 36 to 364 samples, the training score stabilizes at 0.9742 while the validation score climbs steadily to 0.9714. At $N=364$, the training and validation curves converge with a tiny gap of 0.0027, demonstrating that the tuned model has low variance and high stability.
        </div>
      </div>
    </section>
"""
