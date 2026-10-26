"""
Module: topic10_part3.py
Contains Sections 11 to 15 for Topic 10: Logistic Regression.
"""

from scratch.topic10_svgs import (
    SVG_CONFUSION_MATRIX_HEATMAP,
    SVG_PRECISION_RECALL_TRADEOFF,
    SVG_ROC_AUC_CURVE,
    SVG_CLASS_IMBALANCE_ILLUSION,
    SVG_REGULARIZATION_L2_C
)

PART3_HTML = f"""
    <!-- SECTION 11: SIMPLE AND MULTIPLE LOGISTIC REGRESSION -->
    <section id="sec-11" class="section-card">
      <span class="section-badge">Section 11</span>
      <h2 class="section-title">Simple and Multiple Logistic Regression</h2>
      <p class="section-lead">
        Just like linear models, Logistic Regression expands naturally from a single feature (simple) to multidimensional spaces containing dozens or hundreds of predictors (multiple).
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Dimension Aspect</th>
              <th>Simple Logistic Regression (1 Feature)</th>
              <th>Multiple Logistic Regression (p Features)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Linear Score</strong></td>
              <td><code>z = &beta;<sub>0</sub> + &beta;<sub>1</sub>x</code></td>
              <td><code>z = &beta;<sub>0</sub> + &sum;<sub>j=1</sub><sup>p</sup> &beta;<sub>j</sub>x<sub>j</sub></code></td>
            </tr>
            <tr>
              <td><strong>Geometry</strong></td>
              <td>1D S-curve; decision cutoff is a point on a line.</td>
              <td>Multidimensional sigmoid manifold; decision boundary is a hyperplane.</td>
            </tr>
            <tr>
              <td><strong>Feature Interactions</strong></td>
              <td>None; captures only isolated univariate effect.</td>
              <td>Jointly models multivariate predictors simultaneously.</td>
            </tr>
            <tr>
              <td><strong>Key Hazard</strong></td>
              <td>Omitted variable bias (underfitting).</td>
              <td>Multicollinearity and curse of dimensionality.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">1. Feature Scaling and Coefficient Comparability</h3>
      <p>
        In multiple logistic regression, each coefficient <code>&beta;<sub>j</sub></code> reflects the change in log-odds <strong>per one-unit increase in that feature&rsquo;s specific measurement unit</strong>.
      </p>
      <ul>
        <li>If study hours ranges from 0 to 30, a one-unit change is a 1-hour increase.</li>
        <li>If student family income is measured in dollars (e.g., $10,000 to $150,000), a one-unit change is just a single $1.00 increase! Its raw coefficient might be <code>+0.00004</code>, appearing artificially tiny.</li>
      </ul>
      <div class="callout card-concept">
        <div class="callout-title">&#128736; Best Practice: Standardize Features Before Interpreting Coefficients</div>
        <p>
          Always apply <code>StandardScaler</code> so every feature has zero mean and unit variance (<code>z-score</code>). With standardized inputs, coefficient magnitudes directly reflect relative predictive importance across features!
        </p>
      </div>

      <h3 class="sub-title">2. Multicollinearity: The Problem with Redundant Features</h3>
      <p>
        When two or more predictor features are strongly correlated (e.g., total study hours and total study minutes, or attendance percentage and lectures attended), they contain redundant information.
      </p>
      <p>
        Multicollinearity inflates the standard errors of the coefficients, causing weights to oscillate wildly and making individual coefficient signs unreliable. Regularization provides the primary defense.
      </p>
    </section>

    <!-- SECTION 12: REGULARIZATION AND OVERFITTING -->
    <section id="sec-12" class="section-card">
      <span class="section-badge">Section 12</span>
      <h2 class="section-title">Regularization and Overfitting (The C Parameter)</h2>
      <p class="section-lead">
        When a dataset has many features relative to sample size, or when data is perfectly linearly separable, unconstrained Logistic Regression drives weights toward extreme values to force probabilities close to 0 and 1. This creates severe <strong>overfitting</strong>.
      </p>

      <p>
        <strong>Regularization</strong> solves this by adding a penalty term to the loss function that discourages excessively large coefficients:
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; Regularized Loss Formulations</div>
        <div class="formula-math">
          L2 Regularization (Ridge): J<sub>reg</sub> = J<sub>logloss</sub> + &lambda; &sum;<sub>j=1</sub><sup>p</sup> &beta;<sub>j</sub><sup>2</sup>
        </div>
        <div class="formula-math" style="margin-top:0.75rem;">
          L1 Regularization (Lasso): J<sub>reg</sub> = J<sub>logloss</sub> + &lambda; &sum;<sub>j=1</sub><sup>p</sup> |&beta;<sub>j</sub>|
        </div>
      </div>

      <h3 class="sub-title">Understanding Scikit-Learn&rsquo;s Inverted C Parameter</h3>
      <p>
        In theoretical textbooks, regularization strength is denoted by <strong>&lambda; (lambda)</strong>, where larger &lambda; means stronger penalty.
        <br>
        In <strong>scikit-learn</strong>, the <code>LogisticRegression</code> class uses parameter <strong><code>C</code></strong>, which is the <strong>inverse of regularization strength</strong>:
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; The Scikit-Learn Parameter Relationship</div>
        <div class="formula-math">
          C = 1 / &lambda;
        </div>
        <div class="formula-legend">
          <div class="formula-legend-item">
            <code>Small C (e.g., C = 0.01)</code>: Huge penalty (&lambda;=100). Aggressively shrinks weights towards zero. Fights overfitting.
          </div>
          <div class="formula-legend-item">
            <code>Default C (C = 1.0)</code>: Standard balanced penalty (&lambda;=1). Scikit-learn default.
          </div>
          <div class="formula-legend-item">
            <code>Large C (e.g., C = 100.0)</code>: Tiny penalty (&lambda;=0.01). Weights can grow freely. Risk of overfitting.
          </div>
        </div>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_REGULARIZATION_L2_C}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.8: Weight Shrinkage Under Varying C Values.</strong> In our lab model, setting <code>C = 0.01</code> shrinks the total weight vector norm to <code>0.4443</code>, compared to <code>3.8803</code> at <code>C = 1.0</code> and <code>7.7703</code> at <code>C = 100.0</code>.
        </div>
        <div class="svg-takeaway">
          &#10004; Critical Memory Rule: In scikit-learn, <strong>smaller C = stronger regularization</strong>.
        </div>
      </div>

      <div class="callout card-amber">
        <div class="callout-title">&#128295; Solver and Penalty Compatibility in Scikit-Learn</div>
        <p>
          Not every optimization solver supports every penalty!
        </p>
        <ul>
          <li><strong><code>solver='lbfgs'</code></strong> (default): Supports L2 regularization and None. Extremely fast for dense tabular data.</li>
          <li><strong><code>solver='liblinear'</code></strong>: Supports L1 and L2 penalties. Great for smaller datasets.</li>
          <li><strong><code>solver='saga'</code></strong>: Supports ElasticNet, L1, and L2 penalties. Excellent for large sparse datasets.</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 13: CLASSIFICATION METRICS -->
    <section id="sec-13" class="section-card">
      <span class="section-badge">Section 13</span>
      <h2 class="section-title">Important Classification Metrics &amp; The Confusion Matrix</h2>
      <p class="section-lead">
        In continuous regression, we measured model performance using MAE, MSE, and R<sup>2</sup>. In classification, performance evaluation starts with the <strong>Confusion Matrix</strong>.
      </p>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_CONFUSION_MATRIX_HEATMAP}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.9: The 2&times;2 Confusion Matrix for a 100-Patient Screening Clinic.</strong> The matrix breaks down the four possible outcomes between actual disease status and diagnostic predictions.
        </div>
        <div class="svg-takeaway">
          &#10004; Fundamental Rule: Always inspect the four confusion matrix cells before trusting a single summary number.
        </div>
      </div>

      <h3 class="sub-title">The Four Fundamental Outcomes Defined</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Outcome Name</th>
              <th>Actual Class</th>
              <th>Model Prediction</th>
              <th>Clinic Example (N=100)</th>
              <th>Real-World Meaning</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>True Positive (TP)</strong></td>
              <td>1 (Sick)</td>
              <td>1 (Sick)</td>
              <td><span class="badge badge-tp">18 Patients</span></td>
              <td>Correct detection: Patient has condition and gets treatment.</td>
            </tr>
            <tr>
              <td><strong>False Negative (FN)</strong></td>
              <td>1 (Sick)</td>
              <td>0 (Healthy)</td>
              <td><span class="badge badge-fn">2 Patients</span></td>
              <td><strong>Type II Error:</strong> Missed diagnosis. Patient sent home untreated!</td>
            </tr>
            <tr>
              <td><strong>False Positive (FP)</strong></td>
              <td>0 (Healthy)</td>
              <td>1 (Sick)</td>
              <td><span class="badge badge-fp">6 Patients</span></td>
              <td><strong>Type I Error:</strong> False alarm. Healthy patient receives stress &amp; biopsy.</td>
            </tr>
            <tr>
              <td><strong>True Negative (TN)</strong></td>
              <td>0 (Healthy)</td>
              <td>0 (Healthy)</td>
              <td><span class="badge badge-tn">74 Patients</span></td>
              <td>Correct clearance: Healthy person confirmed healthy.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">The Four Core Classification Metrics</h3>
      <p>
        Using our verified 100-patient medical screening numbers (<code>TP = 18, FN = 2, FP = 6, TN = 74</code>), let us calculate each core metric:
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; 1. Classification Accuracy</div>
        <div class="formula-math">
          Accuracy = (TP + TN) / (TP + TN + FP + FN)
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          <code>Accuracy = (18 + 74) / 100 = 92 / 100 = <strong>92.00%</strong></code>
          <br>
          <em>Meaning:</em> Percentage of all predictions that were correct. Dangerous when classes are imbalanced!
        </p>
      </div>

      <div class="formula-card">
        <div class="formula-title">&#128290; 2. Precision (Positive Predictive Value)</div>
        <div class="formula-math">
          Precision = TP / (TP + FP)
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          <code>Precision = 18 / (18 + 6) = 18 / 24 = <strong>75.00%</strong></code>
          <br>
          <em>Meaning:</em> When the model predicts positive, how often is it actually right? (High precision means few false alarms).
        </p>
      </div>

      <div class="formula-card">
        <div class="formula-title">&#128290; 3. Recall / Sensitivity (True Positive Rate)</div>
        <div class="formula-math">
          Recall = TP / (TP + FN)
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          <code>Recall = 18 / (18 + 2) = 18 / 20 = <strong>90.00%</strong></code>
          <br>
          <em>Meaning:</em> Out of all truly positive cases, what percentage did the model catch? (High recall means few missed diseases).
        </p>
      </div>

      <div class="formula-card">
        <div class="formula-title">&#128290; 4. F1-Score (Harmonic Mean of Precision and Recall)</div>
        <div class="formula-math">
          F1 = 2 &times; (Precision &times; Recall) / (Precision + Recall)
        </div>
        <p style="margin-top:0.5rem;font-size:0.95rem;color:#334155;">
          <code>F1 = 2 &times; (0.75 &times; 0.90) / (0.75 + 0.90) = 2 &times; 0.675 / 1.65 = 1.35 / 1.65 = <strong>81.82%</strong></code>
          <br>
          <em>Meaning:</em> Balanced metric that heavily penalizes extreme asymmetry between precision and recall.
        </p>
      </div>
    </section>

    <!-- SECTION 14: ROC CURVE AND AUC -->
    <section id="sec-14" class="section-card">
      <span class="section-badge">Section 14</span>
      <h2 class="section-title">ROC Curve and AUC (Receiver Operating Characteristic)</h2>
      <p class="section-lead">
        A single confusion matrix only shows performance at <strong>one specific operating threshold</strong> (like &tau;=0.50). To evaluate how well a model discriminates between classes across <em>all possible thresholds simultaneously</em>, machine learning practitioners use the <strong>ROC Curve</strong>.
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; The Two Axes of the ROC Curve</div>
        <div class="formula-math">
          Y-Axis: True Positive Rate (TPR / Recall) = TP / (TP + FN)
        </div>
        <div class="formula-math" style="margin-top:0.75rem;">
          X-Axis: False Positive Rate (FPR) = FP / (FP + TN) = 1 - Specificity
        </div>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_PRECISION_RECALL_TRADEOFF}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.10: The Precision-Recall Trade-off Curve.</strong> As the decision threshold increases from 0.0 to 1.0, Recall decreases monotonically while Precision climbs. The curves intersect near the peak F1-score balance.
        </div>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_ROC_AUC_CURVE}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.11: The Receiver Operating Characteristic (ROC) Curve.</strong> The curve plots TPR vs. FPR across all thresholds. The red diagonal line represents random guessing (AUC = 0.50). Our high-performing model achieves near-perfect discrimination (AUC &approx; 1.00).
        </div>
        <div class="svg-takeaway">
          &#10004; Interpretation: AUC measures <strong>ranking discrimination</strong>: the probability that the model ranks a randomly chosen positive sample higher than a randomly chosen negative sample.
        </div>
      </div>

      <h3 class="sub-title">Benchmark Guide for ROC AUC Values</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>AUC Score Range</th>
              <th>Discrimination Quality</th>
              <th>Diagnostic Utility</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>0.90 &ndash; 1.00</strong></td>
              <td><span class="badge badge-tp">Outstanding</span></td>
              <td>Exceptional separation; model rarely confuses positive and negative cases.</td>
            </tr>
            <tr>
              <td><strong>0.80 &ndash; 0.90</strong></td>
              <td><span class="badge" style="background:#E0F2FE;color:#0369A1;">Good / Strong</span></td>
              <td>Solid production-grade performance for business and engineering.</td>
            </tr>
            <tr>
              <td><strong>0.70 &ndash; 0.80</strong></td>
              <td><span class="badge badge-fp">Fair</span></td>
              <td>Acceptable for exploratory modeling, but requires careful threshold tuning.</td>
            </tr>
            <tr>
              <td><strong>0.50 &ndash; 0.60</strong></td>
              <td><span class="badge badge-fn">Poor / Coin Flip</span></td>
              <td>No better than random guessing. Model has learned no meaningful pattern.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 15: CLASS IMBALANCE AND THRESHOLD SELECTION -->
    <section id="sec-15" class="section-card">
      <span class="section-badge">Section 15</span>
      <h2 class="section-title">Class Imbalance and Threshold Selection</h2>
      <p class="section-lead">
        In real-world applications such as credit card fraud, cybersecurity intrusion detection, and rare disease diagnosis, the classes are severely imbalanced: 95% to 99.9% of samples belong to the negative class.
      </p>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_CLASS_IMBALANCE_ILLUSION}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.12: The 95% Accuracy Trap.</strong> A naive dummy classifier that unconditionally predicts &ldquo;Normal&rdquo; achieves 95% accuracy while completely missing all 5 fraud cases (Recall = 0.0%).
        </div>
        <div class="svg-takeaway">
          &#10004; Golden Rule: Never rely on Accuracy alone when evaluating models on imbalanced datasets!
        </div>
      </div>

      <h3 class="sub-title">Three Practical Techniques to Address Imbalance</h3>
      <div class="step-list">
        <div class="step-card">
          <div class="step-number">1</div>
          <div class="step-body">
            <h4>Use Balanced Class Weights: <code>class_weight='balanced'</code></h4>
            <p>
              In scikit-learn, setting <code>LogisticRegression(class_weight='balanced')</code> automatically weights the loss function inversely proportional to class frequencies. Misclassifying a rare positive sample incurs a much higher penalty than misclassifying an abundant negative sample.
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">2</div>
          <div class="step-body">
            <h4>Optimize Decision Threshold on Validation Data</h4>
            <p>
              Do not stick with the default 0.50 threshold. Lower the threshold to 0.15 or 0.25 on a <strong>validation split</strong> to maximize Recall or F1-score. Never tune the threshold on the final test set!
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">3</div>
          <div class="step-body">
            <h4>Evaluate Precision-Recall Curves (PR-AUC)</h4>
            <p>
              When positive cases are rare (e.g., 0.1%), ROC AUC can remain deceptively high because large true negatives dilute the FPR denominator. In contrast, <strong>Precision-Recall AUC (PR-AUC)</strong> focuses strictly on positive class performance.
            </p>
          </div>
        </div>
      </div>
    </section>
"""
