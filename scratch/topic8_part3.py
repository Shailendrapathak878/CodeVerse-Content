"""
Module: topic8_part3.py
Contains HTML for Sections 10 to 13 of Topic 8: Train, Validation & Test Sets.
"""

from scratch.topic8_svgs import (
    SVG_GROUP_BASED_SPLITTING,
    SVG_TIME_SERIES_SPLITTING,
    SVG_DATA_LEAKAGE_COMPARISON,
    SVG_NINE_LEAKAGE_VECTORS,
    SVG_MODEL_SELECTION_FLOWCHART,
    SVG_FIVE_FOLD_CROSS_VALIDATION
)

PART3_HTML = f"""
  <!-- SECTION 10: COMMON SPLITTING STRATEGIES FOR DIFFERENT DATA TYPES -->
  <section id="sec-10" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 10</span>
      <h2 class="section-title">Common Splitting Strategies by Data Type</h2>
    </div>
    <p class="section-intro">
      Standard random splitting relies on a critical assumption in statistics: that all data samples are <strong>Independent and Identically Distributed (I.I.D.)</strong>. When observations are grouped, correlated, or sequential in time, ordinary random splitting produces severe data leakage.
    </p>

    <!-- FIGURE 8.7: GROUP BASED SPLITTING -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GROUP_BASED_SPLITTING}
      </div>
      <div class="diagram-caption">Figure 8.7: Group-based splitting ensures that all observations belonging to the same patient or user identity remain together in the same subset.</div>
    </div>

    <h3>The 5 Core Splitting Strategies</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Strategy Name</th>
            <th>Underlying Assumption</th>
            <th>Scikit-Learn Implementation</th>
            <th>When Mandatory</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Ordinary Random Split</strong></td>
            <td>Observations are completely independent and identically distributed (I.I.D.).</td>
            <td><code>train_test_split(shuffle=True)</code></td>
            <td>Standard tabular regression or balanced classification with unique entities per row.</td>
          </tr>
          <tr>
            <td><strong>Stratified Split</strong></td>
            <td>Class proportions in subsets must match the population to avoid class starvation.</td>
            <td><code>train_test_split(stratify=y)</code></td>
            <td>Any classification problem with moderate to severe class imbalance (e.g. fraud, medical).</td>
          </tr>
          <tr>
            <td><strong>Group-Based Split</strong></td>
            <td>Multiple rows belong to the same entity (person, patient, device, household, hospital).</td>
            <td><code>GroupShuffleSplit</code> or <code>GroupKFold</code></td>
            <td>Medical diagnostic records, user telemetry, customer churn with repeated sessions.</td>
          </tr>
          <tr>
            <td><strong>Chronological Time Split</strong></td>
            <td>Observations have temporal dependency; the past must predict the future.</td>
            <td><code>TimeSeriesSplit</code> or date cutoff</td>
            <td>Stock prices, weather forecasting, demand forecasting, IoT sensor telemetry.</td>
          </tr>
          <tr>
            <td><strong>Stratified Group Split</strong></td>
            <td>Both class balance and subject independence must be preserved simultaneously.</td>
            <td><code>StratifiedGroupKFold</code></td>
            <td>Multi-visit clinical trials with imbalanced rare disease diagnoses across patients.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- FIGURE 8.8: TIME SERIES SPLITTING -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_TIME_SERIES_SPLITTING}
      </div>
      <div class="diagram-caption">Figure 8.8: Chronological Time-Series Splitting: Training sets always strictly precede validation/test sets to eliminate lookahead bias.</div>
    </div>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> The Lookahead Disaster in Time-Series Data</div>
      <p>
        If you randomly shuffle a stock market or weather dataset:
      </p>
      <p>
        Your model will be trained on data from <em>Wednesday</em> and tested on data from <em>Tuesday</em>! The model will learn future trends to "predict" the past, producing near-perfect validation accuracy (e.g. 99.8%). But when deployed live on Thursday morning, future data does not exist, and the trading bot or weather forecast will fail completely.
        <br><strong>Cardinal Rule of Time-Series:</strong> Never shuffle temporal data. Always split chronologically: Past &rarr; Present &rarr; Future.
      </p>
    </div>
  </section>

  <!-- SECTION 11: DATA LEAKAGE DURING DATASET SPLITTING -->
  <section id="sec-11" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 11</span>
      <h2 class="section-title">Data Leakage During Dataset Splitting</h2>
    </div>
    <p class="section-intro">
      <strong>Data Leakage</strong> is the introduction of information about the target or test distribution into the training pipeline. It is the single most common cause of high offline benchmark scores followed by catastrophic production failures.
    </p>

    <!-- FIGURE 8.9: NINE LEAKAGE VECTORS -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_NINE_LEAKAGE_VECTORS}
      </div>
      <div class="diagram-caption">Figure 8.9: The 9 primary data leakage vectors encountered during dataset splitting and preprocessing.</div>
    </div>

    <!-- FIGURE 8.10: LEAKAGE WORKFLOW COMPARISON -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_DATA_LEAKAGE_COMPARISON}
      </div>
      <div class="diagram-caption">Figure 8.10: Architectural comparison of a leaking preprocessing workflow vs a leak-free Scikit-Learn Pipeline.</div>
    </div>

    <h3>Detailed Breakdown of the 9 Leakage Vectors</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Leakage Vector</th>
            <th>The Flawed Mechanism</th>
            <th>The Safe Engineering Fix</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>01</strong></td>
            <td><strong>Scaling Before Splitting</strong></td>
            <td><code>StandardScaler.fit(X_all)</code> calculates global &mu; and &sigma; using test rows.</td>
            <td>Split first: <code>scaler.fit(X_train)</code>, then <code>scaler.transform(X_test)</code>.</td>
          </tr>
          <tr>
            <td><strong>02</strong></td>
            <td><strong>Global Imputation</strong></td>
            <td>Missing values filled with mean/median computed across training + test data.</td>
            <td>Fit <code>SimpleImputer</code> strictly on training data; transform test data.</td>
          </tr>
          <tr>
            <td><strong>03</strong></td>
            <td><strong>Test Feature Selection</strong></td>
            <td>Running ANOVA, Chi2, or correlation on the full dataset before splitting.</td>
            <td>Select features using only training feature-target relationships.</td>
          </tr>
          <tr>
            <td><strong>04</strong></td>
            <td><strong>Global Target Encoding</strong></td>
            <td>Category averages calculated using evaluation targets.</td>
            <td>Compute target statistics within cross-fitting loops or training folds only.</td>
          </tr>
          <tr>
            <td><strong>05</strong></td>
            <td><strong>Oversampling (SMOTE) Before Split</strong></td>
            <td>Synthetic minority points generated using test samples, leaking into training.</td>
            <td>Apply SMOTE exclusively to the training split inside an <code>imblearn.Pipeline</code>.</td>
          </tr>
          <tr>
            <td><strong>06</strong></td>
            <td><strong>Duplicate Records</strong></td>
            <td>Identical or near-identical rows land in both training and testing sets.</td>
            <td>De-duplicate identical rows based on unique entity keys before splitting.</td>
          </tr>
          <tr>
            <td><strong>07</strong></td>
            <td><strong>Subject / Patient Leakage</strong></td>
            <td>Same human or device appears in both sets, memorizing individual traits.</td>
            <td>Use <code>GroupShuffleSplit</code> or <code>GroupKFold</code> keyed on Subject ID.</td>
          </tr>
          <tr>
            <td><strong>08</strong></td>
            <td><strong>Time Lookahead Bias</strong></td>
            <td>Randomly shuffling temporal observations leaks future trends into the past.</td>
            <td>Split chronologically using expanding or rolling time windows.</td>
          </tr>
          <tr>
            <td><strong>09</strong></td>
            <td><strong>Test-Score Hyperparameter Tuning</strong></td>
            <td>Repeatedly adjusting model parameters to improve test set scores.</td>
            <td>Tune hyperparameters strictly on the <strong>validation set</strong>; touch test once!</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 12: TRAIN/VALIDATION/TEST WORKFLOW WITH PREPROCESSING -->
  <section id="sec-12" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 12</span>
      <h2 class="section-title">Train/Val/Test Workflow with Preprocessing</h2>
    </div>
    <p class="section-intro">
      Below is the complete, production-grade 11-step machine learning experimental workflow, showing exactly when preprocessing transformers are fitted, how candidate models are compared, and when the final test audit occurs.
    </p>

    <!-- FIGURE 8.11: MODEL SELECTION FLOWCHART -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_MODEL_SELECTION_FLOWCHART}
      </div>
      <div class="diagram-caption">Figure 8.11: End-to-end model selection flowchart illustrating candidate comparison on validation data followed by a single final test set evaluation.</div>
    </div>

    <h3>The 11-Step Production ML Lifecycle</h3>
    <ol>
      <li><strong>Step 1: Define Problem &amp; Data Structure:</strong> Establish the target variable (y) and verify if data contains groups (subjects) or time ordering.</li>
      <li><strong>Step 2: Clean Raw Data:</strong> Remove corrupted corrupted rows, deduplicate identical entities, and parse date stamps.</li>
      <li><strong>Step 3: PARTITION FIRST (Golden Rule):</strong> Execute <code>train_test_split()</code>, <code>GroupShuffleSplit()</code>, or time cutoff to create Train (70%), Validation (15%), and Test (15%) subsets.</li>
      <li><strong>Step 4: Lock the Test Set in a Vault:</strong> Disconnect the test set from your active coding notebook or pipeline to prevent accidental snoop leakage.</li>
      <li><strong>Step 5: Fit Preprocessing on Train ONLY:</strong> Fit scalers (StandardScaler), imputers (SimpleImputer), and encoders (OneHotEncoder) on <code>X_train</code> only.</li>
      <li><strong>Step 6: Transform Validation Data:</strong> Apply fitted transformers to <code>X_val</code> using <code>transformer.transform(X_val)</code>.</li>
      <li><strong>Step 7: Train Candidate Models:</strong> Fit multiple model architectures (KNN, SVM, Random Forest, XGBoost) on <code>X_train</code>.</li>
      <li><strong>Step 8: Evaluate &amp; Tune on Validation Set:</strong> Compare candidate predictions on <code>X_val</code>. Tune hyperparameters (e.g. <code>k</code> in KNN, tree depth) to optimize validation metric.</li>
      <li><strong>Step 9: Select the Winning Model:</strong> Pick the single best-performing architecture and configuration based strictly on validation performance.</li>
      <li><strong>Step 10: Conduct the Final Unbiased Test Audit:</strong> Evaluate the winning model <strong>exactly once</strong> on <code>X_test</code>. Report final accuracy, precision, recall, and F1-score.</li>
      <li><strong>Step 11: Production Deployment:</strong> Package the fitted preprocessing pipeline and model weights for live inference serving.</li>
    </ol>
  </section>

  <!-- SECTION 13: CROSS-VALIDATION: HOW IT FITS INTO THE PICTURE -->
  <section id="sec-13" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 13</span>
      <h2 class="section-title">Cross-Validation: How It Fits Into the Picture</h2>
    </div>
    <p class="section-intro">
      When a dataset is small or moderately sized, setting aside a dedicated 15% validation set can reduce the amount of training data available, while a small validation set produces noisy evaluation scores. <strong>K-Fold Cross-Validation</strong> solves this dilemma by dynamically rotating the validation role across the training split.
    </p>

    <!-- FIGURE 8.12: FIVE FOLD CROSS VALIDATION -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_FIVE_FOLD_CROSS_VALIDATION}
      </div>
      <div class="diagram-caption">Figure 8.12: 5-Fold Cross-Validation mechanics: The development dataset rotates through 5 training/validation splits, averaging scores into an aggregate performance metric.</div>
    </div>

    <h3>How K-Fold Cross-Validation Works</h3>
    <ol>
      <li>The training/development data is partitioned into <code>K</code> equal-sized chunks called <strong>folds</strong> (typically K = 5 or K = 10).</li>
      <li>In iteration 1, fold 1 is held out as the validation set, and the model is trained on folds 2, 3, 4, 5. Score 1 is recorded.</li>
      <li>In iteration 2, fold 2 is held out, and the model trains on folds 1, 3, 4, 5. Score 2 is recorded.</li>
      <li>This process repeats until every fold has served as the validation set exactly once.</li>
      <li>The overall cross-validation score is the arithmetic mean of all K iterations:</li>
    </ol>

    <div class="formula-card">
      <div class="formula-title">Mathematical Formula: K-Fold Cross-Validation Average Score</div>
      <div class="formula-box">Score&#772;<sub>CV</sub> = (1 / K) &times; &Sigma;<sub>k=1</sub><sup>K</sup> Score<sub>k</sub></div>
    </div>

    <div class="card card-concept">
      <div class="card-title"><span>&#9777;</span> Does Cross-Validation Eliminate the Need for a Test Set?</div>
      <p>
        <strong>No!</strong> Cross-validation replaces the <em>validation set</em>, not the <em>test set</em>.
      </p>
      <p>
        If you tune hyperparameters by maximizing cross-validation scores, your final selected model has still been tuned to that development dataset! To provide a completely unbiased estimate of real-world production performance, you must still maintain a separate, untouched <strong>Test Set</strong> (typically 20%) that was never used inside the cross-validation loop.
      </p>
    </div>
  </section>
"""
