"""
Module: topic8_part2.py
Contains HTML for Sections 6 to 9 of Topic 8: Train, Validation & Test Sets.
"""

from scratch.topic8_svgs import (
    SVG_SPLIT_RATIOS_COMPARISON,
    SVG_SAMPLE_COUNT_CALCULATION,
    SVG_RANDOM_SPLITTING_MECHANICS,
    SVG_STRATIFIED_SPLITTING_PRESERVATION
)

PART2_HTML = f"""
  <!-- SECTION 6: UNDERSTANDING DATASET SPLIT RATIOS -->
  <section id="sec-06" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 06</span>
      <h2 class="section-title">Understanding Dataset Split Ratios</h2>
    </div>
    <p class="section-intro">
      Choosing how to partition your dataset between training, validation, and testing depends on the total sample size, the complexity of the learning algorithm, and the validation strategy being employed.
    </p>

    <!-- FIGURE 8.3: SPLIT RATIOS COMPARISON -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_SPLIT_RATIOS_COMPARISON}
      </div>
      <div class="diagram-caption">Figure 8.3: Comparing the standard 2-Way Split (80/20 with Cross-Validation) and 3-Way Split (70/15/15 dedicated sets).</div>
    </div>

    <h3>Standard Split Archetypes</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Split Archetype</th>
            <th>Proportions</th>
            <th>Best Suited For</th>
            <th>Primary Advantages &amp; Trade-offs</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Classic 2-Way Split</strong></td>
            <td><code>80% Train / 20% Test</code></td>
            <td>Small to medium datasets (N &lt; 50,000) using <strong>K-Fold Cross-Validation</strong> on the training set.</td>
            <td>Maximizes training data; validation is handled dynamically via rotating cross-validation folds.</td>
          </tr>
          <tr>
            <td><strong>Classic 3-Way Split</strong></td>
            <td><code>70% Train / 15% Val / 15% Test</code></td>
            <td>Medium datasets (50,000 &le; N &le; 500,000) where a dedicated validation set is desired for rapid tuning.</td>
            <td>Clean separation of roles; fast tuning without retraining K models per hyperparameter.</td>
          </tr>
          <tr>
            <td><strong>Deep Learning Split</strong></td>
            <td><code>98% Train / 1% Val / 1% Test</code></td>
            <td>Massive "Big Data" collections (N &gt; 1,000,000 observations / images / text tokens).</td>
            <td>1% of 1,000,000 is <strong>10,000 samples</strong>&mdash;statistically abundant to measure generalization precision!</td>
          </tr>
          <tr>
            <td><strong>Conservative Split</strong></td>
            <td><code>60% Train / 20% Val / 20% Test</code></td>
            <td>High-stakes domains (medical diagnostics, avionics) where high evaluation confidence is paramount.</td>
            <td>Provides large validation and test buffers at the cost of reduced training sample size.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-concept">
      <div class="card-title"><span>&#9777;</span> The "Big Data" Myth: Fixed Percentage Rules are Obsolete</div>
      <p>
        In legacy machine learning textbooks from the 1990s, rules like <em>"Always use 70/30"</em> were standard because datasets were small (often only a few hundred samples).
      </p>
      <p>
        If your modern database contains <strong>10,000,000 customer records</strong>, setting aside 30% for testing means locking away <strong>3,000,000 observations</strong>! That is a massive waste of precious training information. In modern deep learning and large-scale tabular modeling, a <code>98% / 1% / 1%</code> split gives you 9,800,000 training rows and 100,000 test rows, which provides extraordinary statistical precision for evaluation.
      </p>
    </div>
  </section>

  <!-- SECTION 7: CALCULATING THE NUMBER OF SAMPLES -->
  <section id="sec-07" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 07</span>
      <h2 class="section-title">Calculating the Number of Samples</h2>
    </div>
    <p class="section-intro">
      Understanding the exact arithmetic of sample allocation ensures that subsets contain enough observations to evaluate metrics with statistical confidence.
    </p>

    <div class="formula-card">
      <div class="formula-title">Mathematical Formulation: Sample Partition Arithmetic</div>
      <div class="formula-box">r<sub>train</sub> + r<sub>validation</sub> + r<sub>test</sub> = 1.0 &emsp; (100%)</div>
      <br>
      <div class="formula-box">N<sub>i</sub> = &lfloor; N &times; r<sub>i</sub> &rfloor;</div>
      <div class="formula-desc">
        Where:
        <ul>
          <li><strong>N:</strong> Total number of observations in the dataset.</li>
          <li><strong>r<sub>i</sub>:</strong> Proportion allocated to subset i (e.g. 0.70 for 70%).</li>
          <li><strong>N<sub>i</sub>:</strong> Integer count of samples assigned to subset i.</li>
        </ul>
      </div>
    </div>

    <!-- FIGURE 8.4: SAMPLE COUNT CALCULATION -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_SAMPLE_COUNT_CALCULATION}
      </div>
      <div class="diagram-caption">Figure 8.4: Mathematical step-by-step sample count calculation for N = 1,000 across a 70/15/15 partition.</div>
    </div>

    <h3>Worked Step-by-Step Numerical Example</h3>
    <p>
      Consider an enterprise fraud detection dataset with <code>N = 1,000</code> transactions:
    </p>
    <ol>
      <li><strong>Target Proportions:</strong> <code>r<sub>train</sub> = 0.70</code>, <code>r<sub>val</sub> = 0.15</code>, <code>r<sub>test</sub> = 0.15</code>.</li>
      <li><strong>Check Sum:</strong> <code>0.70 + 0.15 + 0.15 = 1.00 (100.0%) &check;</code></li>
      <li><strong>Compute Training Count:</strong> <code>N<sub>train</sub> = 1,000 &times; 0.70 = <strong>700 samples</strong></code></li>
      <li><strong>Compute Validation Count:</strong> <code>N<sub>val</sub> = 1,000 &times; 0.15 = <strong>150 samples</strong></code></li>
      <li><strong>Compute Test Count:</strong> <code>N<sub>test</sub> = 1,000 &times; 0.15 = <strong>150 samples</strong></code></li>
      <li><strong>Verify Total:</strong> <code>700 + 150 + 150 = 1,000 samples &check;</code></li>
    </ol>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> The Small Sample Volatility Trap</div>
      <p>
        What happens if your total dataset contains only <strong>100 samples</strong>?
      </p>
      <p>
        A 15% test set contains only <code>15 samples</code>. In a classification problem, if your model makes just <strong>one single mistake</strong>, your test accuracy drops by:
      </p>
      <div class="formula-box">1 / 15 &approx; 6.67% Swing in Accuracy!</div>
      <p>
        Evaluating a model on only 15 samples produces immense statistical noise&mdash;a model that scores 86% might easily score 73% or 93% on a slightly different 15-sample split!
        <br><strong>Safer Engineering Rule:</strong> When total <code>N &lt; 1,000</code>, avoid dedicated 3-way splits. Instead, use an 80/20 split and perform <strong>Repeated Stratified K-Fold Cross-Validation</strong> on the 80% development set to average out variance.
      </p>
    </div>
  </section>

  <!-- SECTION 8: RANDOM SPLITTING AND REPRODUCIBILITY -->
  <section id="sec-08" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 08</span>
      <h2 class="section-title">Random Splitting and Reproducibility</h2>
    </div>
    <p class="section-intro">
      Raw datasets are frequently collected or stored in systematic orders&mdash;sorted by timestamp, customer ID, or target class. Partitioning an unsorted table sequentially introduces fatal selection bias.
    </p>

    <!-- FIGURE 8.5: RANDOM SPLITTING MECHANICS -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_RANDOM_SPLITTING_MECHANICS}
      </div>
      <div class="diagram-caption">Figure 8.5: How pseudo-random shuffling breaks raw sorting bias and generates uniform sample partitions.</div>
    </div>

    <h3>The Critical Role of random_state</h3>
    <div class="card card-def">
      <div class="card-title"><span>&#128214;</span> What is random_state?</div>
      <p>
        Computers cannot generate truly random numbers; they generate <strong>pseudo-random</strong> numbers using mathematical algorithms initialized by an integer seed value (the <code>random_state</code>).
      </p>
      <ul>
        <li>When <code>random_state=42</code> is fixed, the exact same sequence of pseudo-random numbers is produced every time the code runs.</li>
        <li>This ensures that your train, validation, and test sets contain the <strong>exact same observations</strong> across multiple experimental runs, team members, and CI/CD testing pipelines.</li>
      </ul>
    </div>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> Reproducibility &ne; Representativeness</div>
      <p>
        Setting <code>random_state=42</code> makes your experiment reproducible, but it does <strong>not</strong> guarantee that the split is a good, unbiased representation of reality!
      </p>
      <p>
        By pure bad luck, a specific random seed might allocate an unusual cluster of outliers into the test set or starve the validation set of rare classes. This is why stratified splitting (for classification) and cross-validation are essential safeguards.
      </p>
    </div>

    <h3>Scikit-Learn Implementation: 2-Stage Train/Val/Test Split</h3>
    <div class="code-block">
      <div class="code-header">
        <span class="code-title">python_two_stage_split.py</span>
        <span class="code-lang">python</span>
      </div>
      <pre><code>import numpy as np
from sklearn.model_selection import train_test_split

# Generate synthetic dataset of 1,000 samples
X = np.random.randn(1000, 10)
y = np.random.randint(0, 2, size=1000)

# STAGE 1: Split into 70% Train and 30% Temp (Val + Test)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42, shuffle=True
)

# STAGE 2: Split 30% Temp equally (50/50) into 15% Val and 15% Test
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42, shuffle=True
)

print(f"Total:      {{len(X)}}")
print(f"Train Set:  {{len(X_train)}} ({{len(X_train)/len(X):.1%}})")  # 700 (70.0%)
print(f"Val Set:    {{len(X_val)}} ({{len(X_val)/len(X):.1%}})")      # 150 (15.0%)
print(f"Test Set:   {{len(X_test)}} ({{len(X_test)/len(X):.1%}})")    # 150 (15.0%)</code></pre>
    </div>
  </section>

  <!-- SECTION 9: STRATIFIED SPLITTING FOR CLASSIFICATION -->
  <section id="sec-09" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 09</span>
      <h2 class="section-title">Stratified Splitting for Imbalanced Data</h2>
    </div>
    <p class="section-intro">
      In classification problems, real-world target classes are rarely distributed 50/50. Fraud detection, medical diagnosis, and ad click prediction frequently exhibit severe <strong>class imbalance</strong>.
    </p>

    <!-- FIGURE 8.6: STRATIFIED SPLITTING PRESERVATION -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_STRATIFIED_SPLITTING_PRESERVATION}
      </div>
      <div class="diagram-caption">Figure 8.6: Stratified splitting guarantees that minority class proportions (20%) are preserved identically across Train, Val, and Test subsets.</div>
    </div>

    <h3>The Class Starvation Disaster</h3>
    <p>
      Imagine a cancer screening dataset with 1,000 patients where only <strong>10 patients (1.0%)</strong> have a malignant tumor (Class 1) and 990 are benign (Class 0).
    </p>
    <p>
      If you perform an ordinary random split into 70% train and 30% test without stratification, pure probabilistic variance can easily allocate 9 or 10 malignant cases to the training set, leaving only <strong>0 or 1 cancer patient in the test set!</strong>
    </p>
    <p>
      A test set with 1 positive sample cannot compute a meaningful Recall, Precision, or ROC-AUC score! The model could predict "Benign" for every single patient and achieve 99.7% test accuracy while failing 100% of real cancer patients.
    </p>

    <div class="formula-card">
      <div class="formula-title">Mathematical Goal of Stratification</div>
      <div class="formula-box">p<sub>c</sub>(Train) &approx; p<sub>c</sub>(Val) &approx; p<sub>c</sub>(Test) &approx; N<sub>c</sub> / N</div>
      <div class="formula-desc">
        Where <code>p<sub>c</sub></code> is the proportion of class <code>c</code>, <code>N<sub>c</sub></code> is the count of class <code>c</code> samples in the full dataset, and <code>N</code> is total sample size.
      </div>
    </div>

    <h3>Verified Numerical Counts from Executed Python Code</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Subset Name</th>
            <th>Total Samples</th>
            <th>Class 0 Count (Benign)</th>
            <th>Class 1 Count (Malignant)</th>
            <th>Minority Class %</th>
            <th>Stratification Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Full Dataset</strong></td>
            <td>200</td>
            <td>160</td>
            <td>40</td>
            <td><strong>20.0%</strong></td>
            <td>Original Baseline Population</td>
          </tr>
          <tr>
            <td><strong>Training Set (70%)</strong></td>
            <td>140</td>
            <td>112</td>
            <td>28</td>
            <td><strong>20.0%</strong></td>
            <td><span class="key-badge badge-train">&check; Exact Preservation</span></td>
          </tr>
          <tr>
            <td><strong>Validation Set (15%)</strong></td>
            <td>30</td>
            <td>24</td>
            <td>6</td>
            <td><strong>20.0%</strong></td>
            <td><span class="key-badge badge-val">&check; Exact Preservation</span></td>
          </tr>
          <tr>
            <td><strong>Test Set (15%)</strong></td>
            <td>30</td>
            <td>24</td>
            <td>6</td>
            <td><strong>20.0%</strong></td>
            <td><span class="key-badge badge-test">&check; Exact Preservation</span></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-concept">
      <div class="card-title"><span>&#9777;</span> What Stratification Does NOT Do</div>
      <ul>
        <li><strong>It does NOT fix class imbalance:</strong> If your training data has 80% negative and 20% positive, the training set still has 80% negative and 20% positive. To balance training, you must apply re-weighting or sampling techniques (like SMOTE).</li>
        <li><strong>It is NOT suitable for Time-Series data:</strong> Stratification randomly pulls observations from across the entire timeline, causing catastrophic lookahead leakage!</li>
      </ul>
    </div>
  </section>
"""
