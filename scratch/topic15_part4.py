"""
Topic 15: Ensemble Learning - Part 4
Sections:
- Section 21: Overfitting, Underfitting and Generalization
- Section 22: Feature Importance and Interpretability
- Section 23: Real-Life Applications
- Section 24: Common Beginner Mistakes & Fixes
- Section 25: Required Visualizations System
- Section 26: Quick Reference & Formulas
- Section 27: Interactive Knowledge Checks & FAQs
- Notes Footer
"""

TOPIC_15_PART4 = """
    <!-- SECTION 21 -->
    <section id="sec-21" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 21</span>
        <h2 class="section-title">Overfitting, Underfitting, and Generalization</h2>
        <p class="section-subtitle">Understanding how ensembles behave across the complexity spectrum and managing the generalization gap.</p>
      </div>

      <p>
        A widespread myth among beginners is that ensemble models are immune to overfitting. While it is true that Bagging algorithms like Random Forest are exceptionally resistant to overfitting as more trees are added, <strong>ensemble models can and do overfit under specific conditions</strong>.
      </p>

      <h3>How Overfitting Manifests in Different Ensemble Families</h3>
      <ul>
        <li><strong>Overfitting in Boosting:</strong> Because each boosting stage sequentially targets remaining residual errors, boosting will eventually begin fitting to random noise, label errors, and outliers if allowed to run for too many stages without regularization. Training loss will reach 0.0, while validation error spikes.</li>
        <li><strong>Overfitting in Bagging:</strong> While increasing <code>n_estimators</code> in Random Forest does <em>not</em> cause overfitting, setting individual trees to infinite depth with <code>min_samples_split=2</code> on a small, noisy dataset can cause the entire forest to memorize noise.</li>
        <li><strong>Overfitting in Stacking:</strong> If the Level-1 meta-model is overly complex (e.g., a deep neural network or unconstrained tree) or if base predictions leak into the meta-model training split, severe overfitting is guaranteed.</li>
      </ul>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_TRAIN_VS_VAL_OVERFIT__
        </div>
        <div class="visual-caption">
          <strong>Figure 21.1: Training Error vs. Validation Error Across Model Complexity.</strong> Underfitting occurs when trees are too shallow or too few stages are run. As complexity increases, validation error hits a sweet spot (Zone of Optimal Generalization). Beyond this point, training error continues declining while validation error climbs, widening the Generalization Gap.
        </div>
      </div>

      <div class="callout-card def-card">
        <div class="def-title">The Generalization Gap</div>
        <p>
          The <strong>Generalization Gap</strong> is defined as the difference between a model's performance on the training data versus its performance on unseen validation/test data:
          <br><br>
          <code>Generalization Gap = Error_{validation} &minus; Error_{train}</code>
          <br><br>
          A small gap indicates healthy generalization. A massive gap (e.g., 99.9% training accuracy vs. 78% validation accuracy) is the unmistakable fingerprint of overfitting.
        </p>
      </div>
    </section>

    <!-- SECTION 22 -->
    <section id="sec-22" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 22</span>
        <h2 class="section-title">Feature Importance and Model Interpretability</h2>
        <p class="section-subtitle">Inspecting tree ensemble mechanics: Mean Decrease in Impurity vs. Permutation Importance.</p>
      </div>

      <p>
        One of the greatest advantages of tree ensembles over black-box deep neural networks is their native ability to calculate <strong>Feature Importances</strong>. These scores reveal which input attributes had the greatest influence on the ensemble's predictions.
      </p>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_FEATURE_IMPORTANCE__
        </div>
        <div class="visual-caption">
          <strong>Figure 22.1: Random Forest Feature Importance (Mean Decrease in Impurity).</strong> Feature 1 contributed 54.85% of total impurity reduction, while Feature 0 contributed 45.15%. In high-dimensional datasets, this ranking guides dimensionality reduction and business decisions.
        </div>
      </div>

      <h3>Mean Decrease in Impurity (MDI) vs. Permutation Importance</h3>
      <p>
        Scikit-learn's default <code>feature_importances_</code> attribute uses <strong>Mean Decrease in Impurity (MDI)</strong>. While fast to compute, MDI has two known flaws:
      </p>
      <ol>
        <li><strong>Cardinality Bias:</strong> MDI artificially inflates the importance of continuous numerical features and high-cardinality categorical variables because they offer more potential threshold split points.</li>
        <li><strong>In-Sample Evaluation:</strong> MDI is computed on training data splits, meaning an overfitted feature that memorizes noise may appear deceptively important.</li>
      </ol>

      <div class="callout-card success-card">
        <div class="success-title">The Solution: Permutation Feature Importance</div>
        <p>
          To measure true generalization importance, use <code>sklearn.inspection.permutation_importance</code> on held-out validation data.
          <br><br>
          <strong>How it works:</strong>
          <br>1. Evaluate the ensemble's baseline accuracy on the validation set.
          <br>2. For feature j, randomly shuffle its values across the validation rows, destroying its relationship with the target while preserving the distribution.
          <br>3. Re-evaluate validation accuracy. The drop in performance directly quantifies feature j's true importance!
        </p>
      </div>

      <div class="callout-card warn-card">
        <div class="warn-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#DC2626" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
            <line x1="12" y1="9" x2="12" y2="13"></line>
            <line x1="12" y1="17" x2="12.01" y2="17"></line>
          </svg>
          Critical Caution: Feature Importance &ne; Causation
        </div>
        <p>
          A high feature importance score proves that a variable is statistically useful for prediction within the training distribution. It does <em>not</em> prove physical causality. For example, in hospital admission data, "hospital bed number" might strongly correlate with patient mortality because ICU rooms have specific bed numbers. Changing the patient's bed number will not cure their illness!
        </p>
      </div>
    </section>

    <!-- SECTION 23 -->
    <section id="sec-23" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 23</span>
        <h2 class="section-title">Real-Life Applications</h2>
        <p class="section-subtitle">Five comprehensive production architectures demonstrating ensemble learning in mission-critical industries.</p>
      </div>

      <p>
        Ensemble methods power mission-critical software systems across industries. Below are five real-world case studies detailing problem formulation, feature engineering, ensemble selection, and evaluation criteria:
      </p>

      <div class="calc-box">
        <div class="calc-title">1. Financial Fraud Detection (Banking &amp; Fintech)</div>
        <p>
          <strong>Problem:</strong> Detect fraudulent credit card transactions in real-time (&lt; 50ms) where fraudulent events account for less than 0.1% of volume (extreme class imbalance).
          <br><strong>Input Features:</strong> Transaction amount, geographical distance from previous charge, merchant category code, device fingerprint velocity, historical average spend.
          <br><strong>Target:</strong> Binary label (0 = Legitimate, 1 = Fraudulent).
          <br><strong>Optimal Ensemble:</strong> LightGBM or XGBoost with scale_pos_weight adjustment, paired with a high-speed Decision Stump cascade.
          <br><strong>Evaluation:</strong> Precision-Recall AUC (PR-AUC) and False Positive Rate at 95% Recall.
          <br><strong>Operational Risk:</strong> High False Positives cause customer friction (declined legitimate transactions), while False Negatives cause immediate financial loss.
        </p>
      </div>

      <div class="calc-box">
        <div class="calc-title">2. Enterprise Email Spam &amp; Phishing Classification</div>
        <p>
          <strong>Problem:</strong> Intercept phishing links, malicious payloads, and marketing spam before delivery to employee inboxes.
          <br><strong>Input Features:</strong> TF-IDF n-grams of body text, SPF/DKIM authentication flags, sender domain age, URL redirect count, attachment MIME types.
          <br><strong>Target:</strong> Multi-class (0 = Inbox, 1 = Suspicious / Quarantine, 2 = Phishing / Block).
          <br><strong>Optimal Ensemble:</strong> Soft Voting Classifier combining Multinomial Naive Bayes, Linear SVM, and a 100-tree Random Forest.
          <br><strong>Evaluation:</strong> Strict Precision for Class 1 and Class 2 (&gt; 99.5%) to prevent vital communications from being quarantined.
          <br><strong>Operational Risk:</strong> Sophisticated spear-phishing campaigns adapt text patterns to evade keyword filters.
        </p>
      </div>

      <div class="calc-box">
        <div class="calc-title">3. Credit Risk Assessment and Loan Default Prediction</div>
        <p>
          <strong>Problem:</strong> Predict whether a loan applicant will default within 24 months to inform lending interest rates.
          <br><strong>Input Features:</strong> Debt-to-income ratio, credit bureau score, employment duration, revolving credit utilization, loan purpose.
          <br><strong>Target:</strong> Binary (0 = Repaid, 1 = Defaulted).
          <br><strong>Optimal Ensemble:</strong> Stacking Classifier with Monotonic Constraints, using Logistic Regression as the Level-1 meta-model.
          <br><strong>Evaluation:</strong> Brier Score (probability calibration) and ROC-AUC.
          <br><strong>Regulatory Mandate:</strong> Regulators require adverse action notices; the model must provide auditable SHAP explanations showing why an applicant was denied.
        </p>
      </div>

      <div class="calc-box">
        <div class="calc-title">4. SaaS Customer Churn Prediction</div>
        <p>
          <strong>Problem:</strong> Identify enterprise software accounts likely to cancel their subscription 60 days before contract renewal.
          <br><strong>Input Features:</strong> Weekly active user logins, support ticket frequency, license utilization percentage, executive sponsor turnover.
          <br><strong>Target:</strong> Binary (0 = Retained, 1 = Churned).
          <br><strong>Optimal Ensemble:</strong> Random Forest Classifier.
          <br><strong>Evaluation:</strong> Top-Decile Lift and Recall at 20% alert threshold.
          <br><strong>Business Action:</strong> Feature importance guides customer success teams to offer tailored training interventions to disengaged accounts.
        </p>
      </div>

      <div class="calc-box">
        <div class="calc-title">5. Clinical Sepsis Early Warning in Intensive Care Units</div>
        <p>
          <strong>Problem:</strong> Predict the onset of severe sepsis 4 to 6 hours before clinical manifestation using ICU telemetry.
          <br><strong>Input Features:</strong> Heart rate variability, arterial blood pressure, white blood cell count, lactate concentration, respiratory rate.
          <br><strong>Target:</strong> Binary (0 = Stable, 1 = Sepsis Imminent).
          <br><strong>Optimal Ensemble:</strong> Gradient Boosted Decision Trees with early stopping.
          <br><strong>Evaluation:</strong> Sensitivity (Recall) &ge; 90% with low False Alarms per patient-bed-day.
          <br><strong>Critical Warning:</strong> Educational models must never be deployed clinically without multi-center randomized clinical trials, ethical board approval, and human-in-the-loop clinician oversight!
        </p>
      </div>
    </section>

    <!-- SECTION 24 -->
    <section id="sec-24" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 24</span>
        <h2 class="section-title">Common Beginner Mistakes &amp; How to Fix Them</h2>
        <p class="section-subtitle">Thirteen common traps that derail machine learning practitioners and their professional solutions.</p>
      </div>

      <!-- Mistake 1 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 1: Assuming Ensembles Always Outperform Single Models
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> "If I build a Random Forest or Stacking ensemble, it is guaranteed to beat my baseline Logistic Regression on every dataset."
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> If the true underlying data-generating process is purely linear, an ensemble of non-linear trees will overcomplicate the fit and underperform a simple regularized linear model. Always establish a single simple baseline first!
          </div>
        </div>
      </div>

      <!-- Mistake 2 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 2: Confusing Bagging with Boosting
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Treating Bagging and Boosting as interchangeable, or believing that AdaBoost trains trees in parallel across bootstrap samples.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> Bagging trains independent high-capacity models in parallel to reduce variance. Boosting trains small models sequentially on previous residual errors to reduce bias.
          </div>
        </div>
      </div>

      <!-- Mistake 3 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 3: Assuming All Boosting Algorithms Update Weights Identically
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Believing Gradient Boosting and XGBoost reweight samples like AdaBoost does.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> AdaBoost reweights training samples based on classification errors. Gradient Boosting and XGBoost leave sample weights alone and fit subsequent trees to the negative gradient (residuals) of a loss function.
          </div>
        </div>
      </div>

      <!-- Mistake 4 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 4: Confusing Voting and Stacking
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Believing that Stacking is just taking a vote among different models.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> Voting uses a hardcoded heuristic (majority vote or average). Stacking trains a dedicated secondary machine learning algorithm (meta-model) that learns how to weigh and blend the base predictions.
          </div>
        </div>
      </div>

      <!-- Mistake 5 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 5: Training Stacking Meta-Models on In-Sample Base Predictions
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Fitting base models on the training set, generating predictions on that same training set, and feeding them to the meta-model.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> This causes fatal data leakage! Always generate Level-1 training features using K-fold out-of-fold cross-validation (as handled automatically by <code>StackingClassifier(..., cv=5)</code>).
          </div>
        </div>
      </div>

      <!-- Mistake 6 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 6: Repeatedly Tuning Hyperparameters on the Final Test Set
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Tweaking <code>n_estimators</code> and <code>learning_rate</code> until the test set score reaches its highest value.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> This leaks test information into your model selection. Always split data into Train, Validation, and Test. Tune hyperparameters exclusively on the Validation set; evaluate the final winner on the Test set once.
          </div>
        </div>
      </div>

      <!-- Mistake 7 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 7: Comparing Models Evaluated on Different Data Splits
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Evaluating Random Forest with <code>train_test_split(..., random_state=42)</code> and Gradient Boosting with <code>random_state=123</code>.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> Benchmark comparisons are only scientifically valid when all competing models are trained and tested on the exact same identical split.
          </div>
        </div>
      </div>

      <!-- Mistake 8 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 8: Ignoring Extreme Class Imbalance
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Training a standard Random Forest on a dataset with 99% Class 0 and 1% Class 1 without adjustments.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> The forest will prioritize the majority class. Use <code>class_weight='balanced'</code>, <code>BalancedRandomForestClassifier</code>, or tune decision thresholds using precision-recall curves.
          </div>
        </div>
      </div>

      <!-- Mistake 9 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 9: Reporting Only Accuracy for Unbalanced Tasks
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Celebrating a 99% accuracy score when the dataset is 99% negative.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> Report Precision, Recall, F1-Score, and ROC-AUC alongside the full Confusion Matrix.
          </div>
        </div>
      </div>

      <!-- Mistake 10 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 10: Misinterpreting Feature Importance as Real-World Causation
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Telling business leaders that increasing feature X will cause target Y to increase because feature X had high Gini importance.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> Gini importance reflects statistical predictive utility within the fitted model, not real-world causal mechanisms.
          </div>
        </div>
      </div>

      <!-- Mistake 11 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 11: Using Deprecated or Incompatible scikit-learn Parameter Names
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Writing <code>BaggingClassifier(base_estimator=...)</code> or <code>AdaBoostClassifier(base_estimator=...)</code> in modern code.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> In scikit-learn &ge; 1.2, <code>base_estimator</code> is deprecated and replaced by <code>estimator</code>. Using modern parameter names ensures future-proof compatibility.
          </div>
        </div>
      </div>

      <!-- Mistake 12 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 12: Assuming XGBoost Is Installed Without Checking
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Writing scripts that fail with <code>ModuleNotFoundError: No module named 'xgboost'</code>.
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> Always check environment availability via <code>try: import xgboost ... except ImportError: ...</code> and provide fallback instructions.
          </div>
        </div>
      </div>

      <!-- Mistake 13 -->
      <div class="mistake-card">
        <div class="mistake-header">
          <span style="font-size:1.1rem;">&#10060;</span> Mistake 13: Reporting Fabricated Metrics or Unexecuted Examples
        </div>
        <div class="mistake-body">
          <div class="mistake-error">
            <strong>The Misconception:</strong> Writing made-up accuracy numbers (like claiming 99.99% without running code).
          </div>
          <div class="mistake-fix">
            <strong>The Solution:</strong> Always execute the Python pipeline with fixed seeds and report actual, verified numbers (e.g., AdaBoost: 97.92%, Random Forest: 93.75%).
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 25 -->
    <section id="sec-25" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 25</span>
        <h2 class="section-title">Required Visualizations System &amp; Visual Guide</h2>
        <p class="section-subtitle">Catalog of all 17 custom vector diagrams, curves, and architectures implemented in this chapter.</p>
      </div>

      <p>
        Every diagram in this masterclass is an XML-valid, responsive SVG vector asset designed strictly for Light Mode. Below is the systematic index of all 17 figures:
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Figure ID</th>
              <th>Diagram Title &amp; Topic</th>
              <th>Visual Type</th>
              <th>Core Concept Taught</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Fig 1.1</strong></td>
              <td>Universal Ensemble Learning Pipeline</td>
              <td>Architecture Flowchart</td>
              <td>Data &rarr; Diverse Models &rarr; Aggregation &rarr; Final Prediction</td>
            </tr>
            <tr>
              <td><strong>Fig 3.1</strong></td>
              <td>Single Model vs. Ensemble Comparison</td>
              <td>Comparative Diagram</td>
              <td>Single fragile tree vs. diverse consensus forest</td>
            </tr>
            <tr>
              <td><strong>Fig 4.1</strong></td>
              <td>Hard Voting vs. Soft Voting Mechanics</td>
              <td>Decision Matrix</td>
              <td>Majority counting vs. weighted probability averaging</td>
            </tr>
            <tr>
              <td><strong>Fig 6.1</strong></td>
              <td>Bootstrap Sampling with Replacement</td>
              <td>Sampling Grid</td>
              <td>How replacement creates duplicate rows and ~36.8% OOB samples</td>
            </tr>
            <tr>
              <td><strong>Fig 7.1</strong></td>
              <td>Single Tree vs. Bagging Decision Boundary</td>
              <td>Coordinate Frontier</td>
              <td>How averaging 50 trees smoothes erratic orthogonal steps</td>
            </tr>
            <tr>
              <td><strong>Fig 8.1</strong></td>
              <td>Random Forest Dual Randomization Architecture</td>
              <td>Structural Pipeline</td>
              <td>Row bootstrap sampling + random split feature subsets (&radic;p)</td>
            </tr>
            <tr>
              <td><strong>Fig 9.1</strong></td>
              <td>Single Tree vs. Random Forest Boundaries</td>
              <td>Coordinate Comparison</td>
              <td>Rigid high-variance partitions vs. robust contour boundaries</td>
            </tr>
            <tr>
              <td><strong>Fig 9.2</strong></td>
              <td>Random Forest Accuracy vs. Number of Trees</td>
              <td>Metric Curve</td>
              <td>Diminishing returns and asymptotic plateau beyond 100 trees</td>
            </tr>
            <tr>
              <td><strong>Fig 11.1</strong></td>
              <td>Bagging vs. Boosting Process Architecture</td>
              <td>Comparative Flowchart</td>
              <td>Parallel independent models vs. sequential corrective models</td>
            </tr>
            <tr>
              <td><strong>Fig 12.1</strong></td>
              <td>AdaBoost Sequential Sample Reweighting</td>
              <td>Multi-Stage Plot</td>
              <td>Misclassified points magnified; decision stumps combined with &alpha;_t</td>
            </tr>
            <tr>
              <td><strong>Fig 13.1</strong></td>
              <td>Additive Gradient Boosting Progression</td>
              <td>Curve Approximation</td>
              <td>Base mean + tree on residuals + tree on residual shrinkage</td>
            </tr>
            <tr>
              <td><strong>Fig 14.1</strong></td>
              <td>Boosting Stages: Train vs. Validation Loss</td>
              <td>Overfitting Curve</td>
              <td>Optimal early stopping point vs. late-stage noise memorization</td>
            </tr>
            <tr>
              <td><strong>Fig 16.1</strong></td>
              <td>Stacking Generalization Architecture</td>
              <td>2-Level Hierarchy</td>
              <td>Level-0 diverse base models feeding Level-1 meta-model via K-Fold CV</td>
            </tr>
            <tr>
              <td><strong>Fig 18.1</strong></td>
              <td>Unified Classification Benchmark</td>
              <td>Bar Chart Benchmark</td>
              <td>8-model side-by-side test accuracy comparison</td>
            </tr>
            <tr>
              <td><strong>Fig 19.1</strong></td>
              <td>Regression Actual vs. Predicted Trajectories</td>
              <td>Continuous Scatter Plot</td>
              <td>Single Tree vs. Random Forest vs. Gradient Boosting vs. Ground Truth</td>
            </tr>
            <tr>
              <td><strong>Fig 22.1</strong></td>
              <td>Random Forest Feature Importance</td>
              <td>Horizontal Bar Chart</td>
              <td>Relative Mean Decrease in Impurity across input dimensions</td>
            </tr>
            <tr>
              <td><strong>Fig 21.1</strong></td>
              <td>Training vs. Validation Overfitting Dynamics</td>
              <td>Complexity Curve</td>
              <td>Underfitting, sweet spot, and widening Generalization Gap</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 26 -->
    <section id="sec-26" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 26</span>
        <h2 class="section-title">Quick Reference, Formulas, and Summary Matrix</h2>
        <p class="section-subtitle">Mathematical cheat sheet and algorithm selection flowchart for practical engineering.</p>
      </div>

      <div class="calc-box">
        <div class="calc-title">Ensemble Learning Formula Cheat Sheet</div>
        <p>
          &bull; <strong>Hard Voting:</strong> <code>y&#770; = mode( C₁(x), C₂(x), &hellip;, C_M(x) )</code>
          <br>&bull; <strong>Soft Voting:</strong> <code>y&#770; = argmax_c [ (1 / M) &times; &sum;_{m=1}^{M} P_m(y = c | x) ]</code>
          <br>&bull; <strong>Regression Averaging:</strong> <code>y&#770; = (1 / M) &times; &sum;_{m=1}^{M} y&#770;_m(x)</code>
          <br>&bull; <strong>Weighted Regression:</strong> <code>y&#770; = &sum;_{m=1}^{M} w_m &times; y&#770;_m(x), &nbsp; &sum; w_m = 1</code>
          <br>&bull; <strong>Out-of-Bag Probability Limit:</strong> <code>lim_{N &rarr; &infin;} ( 1 &minus; 1/N )^N = 1 / e &approx; 0.3679 (36.8%)</code>
          <br>&bull; <strong>AdaBoost Estimator Weight:</strong> <code>&alpha;_t = (1 / 2) &times; ln( (1 &minus; &epsilon;_t) / &epsilon;_t )</code>
          <br>&bull; <strong>AdaBoost Sample Weight Update:</strong> <code>w_i^{(t+1)} = [ w_i^{(t)} &times; exp( &minus;&alpha;_t &times; y_i &times; h_t(x_i) ) ] / Z_t</code>
          <br>&bull; <strong>Additive Gradient Boosting:</strong> <code>F_m(x) = F_{m-1}(x) + &eta; &times; h_m(x)</code>
          <br>&bull; <strong>Pseudo-Residual (Squared Error):</strong> <code>r_i^{(m)} = y_i &minus; F_{m-1}(x_i)</code>
        </p>
      </div>

      <h3>Which Ensemble Algorithm Should You Pick?</h3>
      <ul>
        <li><strong>Need a quick, reliable, out-of-the-box model with minimal tuning?</strong> &rarr; <strong>Random Forest</strong>. Highly resistant to overfitting, handles tabular non-linearities effortlessly, gives quick feature importances.</li>
        <li><strong>Need maximum possible predictive accuracy on structured/tabular data?</strong> &rarr; <strong>XGBoost, LightGBM, or CatBoost</strong>. Tuned with low learning rate and early stopping.</li>
        <li><strong>Have three already-tuned diverse models (e.g., Logistic Regression, SVM, and Random Forest)?</strong> &rarr; <strong>Soft Voting Classifier</strong> or <strong>Averaging Regressor</strong>.</li>
        <li><strong>Competing in a high-stakes Kaggle competition seeking the final 0.1% edge?</strong> &rarr; <strong>Stacking Classifier</strong> with K-fold cross-validation and a simple linear meta-model.</li>
      </ul>
    </section>

    <!-- SECTION 27 -->
    <section id="sec-27" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 27</span>
        <h2 class="section-title">Interactive Knowledge Checks &amp; FAQs</h2>
        <p class="section-subtitle">Test your understanding with twelve comprehensive technical interview and concept questions.</p>
      </div>

      <!-- Accordion 1 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          1. Why does an ensemble of identical decision trees fail to improve accuracy?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          Ensemble variance reduction depends directly on the <em>uncorrelatedness</em> of individual estimators. If all trees are trained on identical data with identical features, their correlation &rho; = 1. According to the ensemble variance equation <code>Var = &rho;&sigma;&sup2; + ((1 &minus; &rho;) / B)&sigma;&sup2;</code>, when &rho; = 1, the variance remains &sigma;&sup2; regardless of how many trees you add. The ensemble makes the exact same errors as a single tree.
        </div>
      </details>

      <!-- Accordion 2 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          2. What is the fundamental difference between Bagging and Pasting?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          Both methods train models in parallel on random subsets of the training data. However, <strong>Bagging</strong> samples observations <em>with replacement</em> (bootstrap sampling), meaning individual rows can appear multiple times and ~36.8% are omitted. <strong>Pasting</strong> samples observations <em>without replacement</em>, meaning every sampled row is unique in that subset. Bagging generally introduces slightly more diversity and lower variance.
        </div>
      </details>

      <!-- Accordion 3 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          3. How does Random Forest decorrelate trees compared to standard Bagging?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          Standard Bagging only randomizes training rows. If one feature is overwhelmingly predictive, every tree will split on that feature at the root. Random Forest introduces a second layer of randomization: at <em>every individual split</em>, it considers only a random subset of m &approx; &radic;p features. This forces trees to explore alternative features and branching structures, dramatically lowering tree correlation &rho;.
        </div>
      </details>

      <!-- Accordion 4 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          4. When would Soft Voting produce a different outcome than Hard Voting?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          Soft Voting differs when one model has high confidence in one class while two other models have weak, borderline confidence in the opposite class. As proved in Section 4, two models predicting Class 1 with 55% and 60% confidence are overruled in soft voting by a single model predicting Class 0 with 70% confidence, because the average probability for Class 0 (51.67%) exceeds that of Class 1 (48.33%).
        </div>
      </details>

      <!-- Accordion 5 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          5. What is the Out-of-Bag (OOB) score and why does it approximate cross-validation?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          Because each bootstrap sample omits approximately 36.8% of training rows, every training row x_i is completely unseen by ~37% of the trees in a forest. Evaluating x_i exclusively using those unseen trees and aggregating their votes provides an internal out-of-sample performance estimate that closely mirrors 3-fold cross-validation, without requiring separate validation splits.
        </div>
      </details>

      <!-- Accordion 6 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          6. How does AdaBoost decide how much weight (&alpha;_t) to assign to an estimator?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          AdaBoost sets <code>&alpha;_t = (1 / 2) &times; ln( (1 &minus; &epsilon;_t) / &epsilon;_t )</code>, where &epsilon;_t is the weighted error rate. If an estimator achieves 50% error (coin flip), &alpha;_t = 0 (zero vote). If &epsilon;_t &lt; 0.5, &alpha;_t is positive and grows logarithmically as error approaches zero. If an estimator performs worse than random guessing (&epsilon;_t &gt; 0.5), &alpha;_t becomes negative, effectively inverting its prediction!
        </div>
      </details>

      <!-- Accordion 7 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          7. What are pseudo-residuals in Gradient Boosting?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          Pseudo-residuals are the negative gradients of the chosen loss function with respect to current ensemble predictions: <code>r_i^{(m)} = &minus;[ &part;L(y_i, F(x_i)) / &part;F(x_i) ]_{F=F_{m-1}}</code>. For mean squared error L = (1/2)(y &minus; F)&sup2;, the pseudo-residual is exactly y &minus; F(x) (the true residual). For binary log-loss, the pseudo-residual is y_i &minus; p_i, representing the probability error.
        </div>
      </details>

      <!-- Accordion 8 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          8. Why is Early Stopping mandatory when training Gradient Boosting models?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          Unlike Random Forest, where adding more trees never causes overfitting, Gradient Boosting sequentially fits trees to remaining residual errors. Eventually, real patterns are exhausted, and the algorithm begins fitting to random noise, outliers, and dataset artifacts. Early stopping monitors a validation set and halts training the moment validation loss ceases to improve.
        </div>
      </details>

      <!-- Accordion 9 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          9. What is data leakage in Stacking and how does K-Fold CV prevent it?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          If base models generate predictions on the same training set they learned from, their predictions will be unrealistically overconfident (memorized). A meta-model trained on these predictions will overfit. K-Fold CV divides the training data into K folds: each fold is predicted by base models trained strictly on the other K&minus;1 folds, ensuring all meta-training features represent genuine out-of-fold generalization.
        </div>
      </details>

      <!-- Accordion 10 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          10. What are the key advantages of XGBoost over classical Gradient Boosting?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          XGBoost introduces second-order Taylor expansions (gradients + Hessians) for faster optimization, built-in L₁ and L₂ regularization on leaf weights to control tree complexity, automatic sparsity-aware handling for missing values, cache-aware memory block storage, and parallelized column-split finding.
        </div>
      </details>

      <!-- Accordion 11 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          11. Why can Gini-based feature importance be misleading?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          Gini impurity decrease (MDI) is biased toward continuous numerical features and categorical variables with many unique levels (high cardinality), because they offer more opportunities for split creation. Furthermore, MDI is evaluated on training data. Permutation Importance on held-out validation data provides a far more trustworthy metric.
        </div>
      </details>

      <!-- Accordion 12 -->
      <details class="accordion-item">
        <summary class="accordion-summary">
          12. Can an ensemble model be deployed to low-power edge microcontrollers?
          <span style="color:var(--primary-accent); font-size:1.1rem;">&#9662;</span>
        </summary>
        <div class="accordion-content">
          Ensembles of hundreds of deep decision trees consume significant RAM and require traversing multiple trees per inference, which can strain microcontrollers (e.g., ARM Cortex-M with 64KB RAM). In such edge environments, practitioners often train a large ensemble, and then use <strong>Knowledge Distillation</strong> to train a single compact student model (or small neural network) to mimic the ensemble's predictions.
        </div>
      </details>
    </section>

    <!-- FOOTER -->
    <footer class="notes-footer">
      <p>
        <strong>CodeVerse Interactive Machine Learning Curriculum</strong> &bull; Topic 15: Ensemble Learning
        <br>
        Crafted with strict Light Mode aesthetics, mathematically validated algorithms, and reproducible scikit-learn &amp; XGBoost pipelines.
      </p>
    </footer>
"""
