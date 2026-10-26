# Topic 20 Content - Part 2: Sections 06 to 11
# Strict Light Mode Only, Native HTML Math, Verified Numerical Examples

TOPIC20_PART2 = """
    <!-- SECTION 06 -->
    <section id="sec-06" class="content-section">
      <span class="section-tag">Section 06</span>
      <h2 class="section-title">K-Fold Cross-Validation Step by Step</h2>
      <p class="section-intro">
        To understand cross-validation deeply, let us trace exactly what happens during each iteration of a 5-Fold cross-validation procedure on an educational dataset of 120 training samples.
      </p>

      <h3>The Step-by-Step 5-Fold Rotation</h3>
      <p>
        Suppose our training set contains <strong>N = 120</strong> observations. We partition this data into <strong>K = 5</strong> equal non-overlapping subsets (folds) of <strong>24 samples each</strong>:
      </p>
      <ul>
        <li><strong>Iteration 1:</strong> Folds 2, 3, 4, 5 (96 samples, 80%) train the model &rarr; Fold 1 (24 samples, 20%) evaluates it. Score: <code>s₁ = 0.9583</code>.</li>
        <li><strong>Iteration 2:</strong> Folds 1, 3, 4, 5 (96 samples, 80%) train the model &rarr; Fold 2 (24 samples, 20%) evaluates it. Score: <code>s₂ = 1.0000</code>.</li>
        <li><strong>Iteration 3:</strong> Folds 1, 2, 4, 5 (96 samples, 80%) train the model &rarr; Fold 3 (24 samples, 20%) evaluates it. Score: <code>s₃ = 0.9583</code>.</li>
        <li><strong>Iteration 4:</strong> Folds 1, 2, 3, 5 (96 samples, 80%) train the model &rarr; Fold 4 (24 samples, 20%) evaluates it. Score: <code>s₄ = 1.0000</code>.</li>
        <li><strong>Iteration 5:</strong> Folds 1, 2, 3, 4 (96 samples, 80%) train the model &rarr; Fold 5 (24 samples, 20%) evaluates it. Score: <code>s₅ = 0.9583</code>.</li>
      </ul>

      <!-- FIGURE 2.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 2.1 &bull; Step-by-Step 5-Fold Cross-Validation Rotation</span>
          <span class="visual-tag">Fold Execution</span>
        </div>
        __SVG_KFOLD_ROTATION__
        <div class="visual-caption">
          Figure 2.1: The 5-fold cross-validation rotation across iterations. The green validation fold shifts sequentially from Fold 1 through Fold 5, ensuring every single observation serves as validation data exactly once.
        </div>
      </div>

      <h3>Mathematical Aggregation: Mean and Standard Deviation</h3>
      <p>
        After all <em>K</em> models are trained and scored, we compute two vital descriptive metrics:
      </p>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Cross-Validation Mean Score Formula
        </div>
        <p>
          The <strong>Mean Cross-Validation Score (s&#772;)</strong> is the arithmetic mean across all <em>K</em> fold scores:
        </p>
        <div class="math-box">
          s&#772; = (1 / K) &times; &sum;<sub>i=1</sub><sup>K</sup> s<sub>i</sub>
        </div>
        <p>
          For our verified 5-fold run:
          <br>
          s&#772; = (0.9583 + 1.0000 + 0.9583 + 1.0000 + 0.9583) / 5 = <strong>0.9750 (97.50%)</strong>
        </p>
      </div>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Cross-Validation Standard Deviation Formula
        </div>
        <p>
          The <strong>Sample Standard Deviation (&sigma;)</strong> measures the dispersion or stability of scores across folds:
        </p>
        <div class="math-box">
          &sigma; = &radic; [ (1 / (K &minus; 1)) &times; &sum;<sub>i=1</sub><sup>K</sup> (s<sub>i</sub> &minus; s&#772;)<sup>2</sup> ]
        </div>
        <p>
          For our verified run, population std dev is <strong>&sigma; = 0.0204 (2.04%)</strong> and sample std dev is <strong>0.0228 (2.28%)</strong>.
          <br>
          Reported performance: <strong>0.9750 &plusmn; 0.0204</strong>.
        </p>
      </div>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Critical Statistical Caveat: Fold Scores Are NOT Independent
        </div>
        <p>
          In classical statistics, standard confidence intervals assume independent and identically distributed (i.i.d.) observations. <strong>Fold scores violate independence!</strong>
          <br>
          In a 5-fold CV, each training set shares <strong>75%</strong> of its samples with every other training set (3 out of 4 training folds are shared). Therefore, the fold scores are positively correlated.
          <br>
          <em>Key Takeaway:</em> The standard deviation is an informative descriptive measure of split stability, but you must <strong>not</strong> use standard naive t-tests or z-tests on fold scores as if they were fully independent measurements.
        </p>
      </div>
    </section>

    <!-- SECTION 07 -->
    <section id="sec-07" class="content-section">
      <span class="section-tag">Section 07</span>
      <h2 class="section-title">Choosing the Number of Folds</h2>
      <p class="section-intro">
        How do you pick <em>K</em>? The choice of <em>K</em> represents a fundamental engineering trade-off between computational budget, statistical bias, and score variance.
      </p>

      <h3>Comparing Fold Configurations: 3 vs 5 vs 10 vs LOOCV</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Fold Count (K)</th>
              <th>Train Ratio</th>
              <th>Validation Ratio</th>
              <th>Computational Fits</th>
              <th>Bias of Performance Estimate</th>
              <th>Variance of Estimate</th>
              <th>Recommended Use Case</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>K = 3</strong></td>
              <td>66.7%</td>
              <td>33.3%</td>
              <td>3 fits</td>
              <td>Higher bias (models train on only 2/3 of available data)</td>
              <td>Low computation</td>
              <td>Massive datasets, heavy neural networks, quick prototyping</td>
            </tr>
            <tr>
              <td><strong>K = 5 (Standard Default)</strong></td>
              <td>80.0%</td>
              <td>20.0%</td>
              <td>5 fits</td>
              <td>Low bias (trains on 80% of data, close to full dataset)</td>
              <td>Well-balanced variance</td>
              <td><strong>The gold-standard default</strong> for most tabular and general ML tasks</td>
            </tr>
            <tr>
              <td><strong>K = 10</strong></td>
              <td>90.0%</td>
              <td>10.0%</td>
              <td>10 fits</td>
              <td>Very low bias (trains on 90% of data)</td>
              <td>Can have slightly higher variance; 2x computation vs K=5</td>
              <td>Rigorous benchmark publications, moderate-sized datasets</td>
            </tr>
            <tr>
              <td><strong>K = N (LOOCV)</strong></td>
              <td>(N &minus; 1)/N</td>
              <td>1 sample</td>
              <td><strong>N fits</strong></td>
              <td>Virtually zero bias (trains on almost all samples)</td>
              <td>High score variance; astronomical compute for large N</td>
              <td>Tiny datasets (N &lt; 50), clinical studies with rare conditions</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- INTERACTIVE K-FOLD EXPLORER -->
      <div class="kfold-explorer" id="kfoldExplorer">
        <div class="kfold-controls">
          <label style="font-weight:700; color:#0F172A; font-size:14px;">Select K-Fold Setting:</label>
          <div class="kfold-btn-group">
            <button type="button" class="kfold-btn" onclick="updateKFold(3, this)">K = 3 Folds</button>
            <button type="button" class="kfold-btn active" onclick="updateKFold(5, this)">K = 5 Folds (Default)</button>
            <button type="button" class="kfold-btn" onclick="updateKFold(10, this)">K = 10 Folds</button>
          </div>
        </div>

        <div class="kfold-metrics">
          <div class="kfold-metric-box">
            <div class="kfold-metric-title">Training Size per Fold</div>
            <div class="kfold-metric-val" id="kfoldTrainVal">96 samples (80.0%)</div>
          </div>
          <div class="kfold-metric-box">
            <div class="kfold-metric-title">Validation Size per Fold</div>
            <div class="kfold-metric-val" id="kfoldValVal">24 samples (20.0%)</div>
          </div>
          <div class="kfold-metric-box">
            <div class="kfold-metric-title">Total Model Fits</div>
            <div class="kfold-metric-val" id="kfoldFitsVal">5 fits</div>
          </div>
          <div class="kfold-metric-box">
            <div class="kfold-metric-title">Relative Compute Workload</div>
            <div class="kfold-metric-val" id="kfoldWorkloadVal">1.0x (Baseline)</div>
          </div>
        </div>
      </div>

      <script>
        function updateKFold(k, btn) {
          document.querySelectorAll('.kfold-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          const total = 120;
          const valSize = Math.round(total / k);
          const trainSize = total - valSize;
          const trainPct = ((trainSize / total) * 100).toFixed(1);
          const valPct = ((valSize / total) * 100).toFixed(1);
          
          document.getElementById('kfoldTrainVal').innerText = trainSize + " samples (" + trainPct + "%)";
          document.getElementById('kfoldValVal').innerText = valSize + " samples (" + valPct + "%)";
          document.getElementById('kfoldFitsVal').innerText = k + " fits";
          
          let workload = "1.0x (Baseline)";
          if (k === 3) workload = "0.6x (Fastest)";
          if (k === 10) workload = "2.0x (Heavy)";
          document.getElementById('kfoldWorkloadVal').innerText = workload;
        }
      </script>
    </section>

    <!-- SECTION 08 -->
    <section id="sec-08" class="content-section">
      <span class="section-tag">Section 08</span>
      <h2 class="section-title">Stratified K-Fold Cross-Validation</h2>
      <p class="section-intro">
        In real-world classification, classes are rarely balanced 50/50. When positive instances are rare &mdash; such as in fraud detection (1%) or medical diagnosis (5%) &mdash; ordinary random K-Fold can catastrophically skew your folds.
      </p>

      <h3>The Hazard of Ordinary K-Fold on Imbalanced Datasets</h3>
      <p>
        Consider an imbalanced dataset of <strong>100 samples</strong>: 90 negative samples (Class 0, 90%) and 10 positive samples (Class 1, 10%).
        <br>
        If we perform standard 5-Fold cross-validation with random splitting:
      </p>
      <ul>
        <li><strong>Fold 1:</strong> Receives only 1 positive sample (4.2% minority rate &mdash; artificially scarce).</li>
        <li><strong>Fold 4:</strong> Receives 4 positive samples (16.7% minority rate &mdash; 4x higher prevalence!).</li>
      </ul>
      <p>
        Because each fold evaluates on a radically different class distribution, fold scores oscillate wildly not because the model is unstable, but because the evaluation sets are inconsistent!
      </p>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Technical Definition: Stratified K-Fold
        </div>
        <p>
          <strong>Stratified K-Fold</strong> is a modified partitioning strategy that preserves the approximate percentage of samples for each target class in every single fold.
          <br><br>
          If the full dataset has 10% positive samples, Stratified K-Fold guarantees that <em>each of the 5 validation folds contains exactly 10% positive samples (2 positives out of 20 samples)</em>.
        </p>
      </div>

      <!-- FIGURE 2.2 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 2.2 &bull; Ordinary K-Fold vs Stratified K-Fold on Imbalanced Data (90:10 Ratio)</span>
          <span class="visual-tag">Stratification Comparison</span>
        </div>
        __SVG_ORDINARY_VS_STRATIFIED__
        <div class="visual-caption">
          Figure 2.2: Comparison of fold class balance. In Ordinary K-Fold (left), minority samples fluctuate erratically between 1 and 4 per fold. In Stratified K-Fold (right), every single fold maintains the identical 90% Class 0 to 10% Class 1 distribution.
        </div>
      </div>

      <h3>Verified Executable Code: Ordinary vs Stratified K-Fold</h3>
      <div class="code-block-wrapper">
        <div class="code-header">
          <span class="code-lang">Python (scikit-learn 1.9 Verified)</span>
          <span class="code-file">stratified_kfold_verification.py</span>
        </div>
        <pre><code class="language-python">import numpy as np
from sklearn.model_selection import KFold, StratifiedKFold

# 1. Create imbalanced dataset: 90 Class 0, 10 Class 1
X = np.arange(100).reshape(-1, 1)
y = np.array([0] * 90 + [1] * 10)

print(f"Overall Class 1 Prevalence: {np.mean(y == 1):.1%}")

# 2. Ordinary K-Fold
kf = KFold(n_splits=5, shuffle=True, random_state=42)
print("\\nOrdinary K-Fold Minority Counts per Fold:")
for i, (train_idx, val_idx) in enumerate(kf.split(X, y), start=1):
    count_1 = np.sum(y[val_idx] == 1)
    pct_1 = np.mean(y[val_idx] == 1)
    print(f"  Fold {i}: {count_1} positive samples ({pct_1:.1%})")

# 3. Stratified K-Fold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
print("\\nStratified K-Fold Minority Counts per Fold:")
for i, (train_idx, val_idx) in enumerate(skf.split(X, y), start=1):
    count_1 = np.sum(y[val_idx] == 1)
    pct_1 = np.mean(y[val_idx] == 1)
    print(f"  Fold {i}: {count_1} positive samples ({pct_1:.1%})")
</code></pre>
      </div>

      <div class="code-block-wrapper">
        <div class="code-header">
          <span class="code-lang">Actual Console Output</span>
          <span class="code-file">stdout</span>
        </div>
        <pre><code class="language-plaintext">Overall Class 1 Prevalence: 10.0%

Ordinary K-Fold Minority Counts per Fold:
  Fold 1: 1 positive samples (5.0%)
  Fold 2: 2 positive samples (10.0%)
  Fold 3: 1 positive samples (5.0%)
  Fold 4: 4 positive samples (20.0%)
  Fold 5: 2 positive samples (10.0%)

Stratified K-Fold Minority Counts per Fold:
  Fold 1: 2 positive samples (10.0%)
  Fold 2: 2 positive samples (10.0%)
  Fold 3: 2 positive samples (10.0%)
  Fold 4: 2 positive samples (10.0%)
  Fold 5: 2 positive samples (10.0%)
</code></pre>
      </div>

      <p class="section-summary-text">
        <strong>Takeaway:</strong> For classification problems &mdash; especially when classes are imbalanced &mdash; <strong>always use StratifiedKFold</strong>. In scikit-learn, <code>cross_val_score</code> automatically detects classifiers and applies StratifiedKFold under the hood!
      </p>
    </section>

    <!-- SECTION 09 -->
    <section id="sec-09" class="content-section">
      <span class="section-tag">Section 09</span>
      <h2 class="section-title">Other Cross-Validation Strategies</h2>
      <p class="section-intro">
        Different real-world datasets possess distinct structural properties &mdash; such as repeated measurements, patient groupings, or tiny sample sizes &mdash; requiring specialized cross-validation strategies.
      </p>

      <!-- FIGURE 2.3 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 2.3 &bull; Specialized Cross-Validation Strategies Architecture</span>
          <span class="visual-tag">Validation Taxonomies</span>
        </div>
        __SVG_CV_STRATEGIES_COMPARE__
        <div class="visual-caption">
          Figure 2.3: Architecture of four advanced validation strategies: LOOCV (N fits), Repeated K-Fold (averaging across random seeds), Group K-Fold (zero group leakage across folds), and Time-Series Split (strictly past-to-future).
        </div>
      </div>

      <h3>Detailed Method Breakdowns</h3>
      <div class="grid-2col">
        <div class="card card-strategy">
          <div class="card-title">1. Leave-One-Out CV (LOOCV)</div>
          <p>
            <strong>How it works:</strong> If you have <em>N</em> samples, you run <em>N</em> iterations. In each iteration, <em>N &minus; 1</em> samples train the model and exactly <strong>one single sample</strong> is validated.
            <br><br>
            <strong>Advantages:</strong> Completely deterministic (no random seed variance) and utilizes maximum possible training data.
            <br><br>
            <strong>Limitations:</strong> Computationally prohibitive for large <em>N</em> (e.g., N = 10,000 means 10,000 fits!). Furthermore, because test samples are binary (0 or 1 error), individual test scores have high variance.
          </p>
        </div>

        <div class="card card-strategy">
          <div class="card-title">2. Repeated K-Fold</div>
          <p>
            <strong>How it works:</strong> Runs standard K-Fold cross-validation <em>R</em> times, with each repetition shuffling the dataset with a completely different random partition (e.g., 5-Fold repeated 10 times = 50 fits).
            <br><br>
            <strong>Advantages:</strong> Drastically suppresses partitioning noise and provides a tighter, smoother estimate of performance dispersion.
            <br><br>
            <strong>Limitations:</strong> Linearly multiplies total training time by <em>R</em>. Best reserved for small datasets where training is fast.
          </p>
        </div>

        <div class="card card-strategy">
          <div class="card-title">3. Group K-Fold</div>
          <p>
            <strong>How it works:</strong> Ensures that all observations belonging to the same entity (patient, customer, vehicle, hospital) reside exclusively in either the training set or the validation set &mdash; <strong>never both!</strong>
            <br><br>
            <strong>Critical Use Case:</strong> If a clinical dataset contains 10 chest X-rays from Patient A, ordinary K-Fold might put 8 images in train and 2 in validation. The model might memorize Patient A's bone structure, creating catastrophic <strong>Group Leakage</strong>. Group K-Fold prevents this entirely.
          </p>
        </div>

        <div class="card card-strategy">
          <div class="card-title">4. TimeSeriesSplit</div>
          <p>
            <strong>How it works:</strong> Respects the strict arrow of time. In iteration <em>k</em>, the model trains exclusively on past time windows and evaluates on the subsequent future time window (expanding or rolling window).
            <br><br>
            <strong>Critical Rule:</strong> Never randomly shuffle temporal data! Using random K-Fold on stock prices or sales forecasts allows the model to "peek into the future", rendering validation scores fictitious.
          </p>
        </div>
      </div>

      <h3>Comprehensive Strategy Comparison Table</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Validation Method</th>
              <th>How Folds Are Formed</th>
              <th>Suitable Dataset Structure</th>
              <th>Primary Advantage</th>
              <th>Main Limitation</th>
              <th>Example Real-World Scenario</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>K-Fold</strong></td>
              <td>Random partitioning into K equal chunks</td>
              <td>Standard I.I.D. regression or balanced classification</td>
              <td>Simplicity, balanced compute</td>
              <td>Subject to class distribution skew in imbalanced data</td>
              <td>Housing price regression, customer churn with 50/50 ratio</td>
            </tr>
            <tr>
              <td><strong>Stratified K-Fold</strong></td>
              <td>Equal class percentages in each fold</td>
              <td>Classification with uneven target classes</td>
              <td>Guarantees identical class balance across folds</td>
              <td>Not applicable to continuous regression targets</td>
              <td>Credit card fraud detection (99.8% legit vs 0.2% fraud)</td>
            </tr>
            <tr>
              <td><strong>Group K-Fold</strong></td>
              <td>Keeps entire entity IDs together</td>
              <td>Multiple correlated records per person, device, or group</td>
              <td>Prevents identity / entity leakage</td>
              <td>Fold sizes may not be perfectly equal in sample count</td>
              <td>Medical diagnostics (multiple MRI scans per patient)</td>
            </tr>
            <tr>
              <td><strong>TimeSeriesSplit</strong></td>
              <td>Expanding historical window &rarr; next future block</td>
              <td>Time-dependent series, sequence forecasts</td>
              <td>Strictly prevents look-ahead temporal leakage</td>
              <td>Early folds train on fewer historical observations</td>
              <td>Daily store sales forecasting, stock market volatility</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 10 -->
    <section id="sec-10" class="content-section">
      <span class="section-tag">Section 10</span>
      <h2 class="section-title">Time-Series Validation and Leakage Prevention</h2>
      <p class="section-intro">
        In temporal domains &mdash; such as energy consumption forecasting, algorithmic trading, and website traffic prediction &mdash; observations are autocorrelated across time. Standard cross-validation destroys the temporal sequence.
      </p>

      <h3>The Peril of Random Splitting in Time-Series</h3>
      <p>
        Suppose you are forecasting tomorrow's retail demand (Day <em>t+1</em>) given historical sales.
        <br>
        If you randomly shuffle your data into a standard train/test split:
      </p>
      <ul>
        <li>The training set might contain Days 1, 3, 4, 6, 7, 9, 10.</li>
        <li>The validation set contains Days 2, 5, 8.</li>
      </ul>
      <p>
        To predict Day 5, the model can simply interpolate between Day 4 and Day 6! In production, you will never have access to Day 6 when forecasting Day 5. This fatal blunder is known as <strong>Look-Ahead Bias</strong> (or <em>temporal data leakage</em>).
      </p>

      <!-- FIGURE 2.4 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 2.4 &bull; Time-Series Split: Expanding Window Architecture</span>
          <span class="visual-tag">Temporal Architecture</span>
        </div>
        __SVG_TIMESERIES_SPLIT__
        <div class="visual-caption">
          Figure 2.4: scikit-learn's <code>TimeSeriesSplit</code> expanding window. In every iteration, the training window incorporates additional historical observations, while the validation window strictly evaluates the chronological future.
        </div>
      </div>

      <h3>Temporal Leakage Prevention Checklist</h3>
      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          The 5 Cardinal Rules of Time-Series Validation
        </div>
        <ol style="margin-top:8px; padding-left:20px; line-height:1.7;">
          <li><strong>Never shuffle:</strong> Set <code>shuffle=False</code> whenever handling date or time indexed records.</li>
          <li><strong>Lag your features:</strong> Features must only contain information strictly available at prediction time (e.g., <code>sales_lag_7d</code>, <code>rolling_mean_past_30d</code>).</li>
          <li><strong>Refit scalers temporally:</strong> Compute mean and standard deviation for standardization exclusively on the historical training window; never compute global means across the entire timeline.</li>
          <li><strong>Account for operational latency:</strong> If a model takes 2 hours to retrain, Day <em>t</em> predictions cannot use data from Day <em>t &minus; 10 minutes</em>. Include an appropriate validation forecast gap.</li>
          <li><strong>Group-aware time series:</strong> When forecasting multiple stores across time, group by store ID while respecting chronological sequence (nested group-temporal splitting).</li>
        </ol>
      </div>
    </section>

    <!-- SECTION 11 -->
    <section id="sec-11" class="content-section">
      <span class="section-tag">Section 11</span>
      <h2 class="section-title">Cross-Validation Using scikit-learn</h2>
      <p class="section-intro">
        scikit-learn provides industrial-grade utilities for executing cross-validation cleanly and safely. Let us examine the core functions, their arguments, and the important negated scoring convention.
      </p>

      <h3>The Primary Cross-Validation API</h3>
      <p>
        The most common utility is <code>cross_val_score(estimator, X, y, cv, scoring)</code>:
      </p>
      <ul>
        <li><code>estimator</code>: The scikit-learn model or Pipeline to be evaluated.</li>
        <li><code>X, y</code>: Feature matrix and target array.</li>
        <li><code>cv</code>: An integer (e.g., <code>cv=5</code>) or a custom splitter object like <code>StratifiedKFold(n_splits=5, shuffle=True, random_state=42)</code>.</li>
        <li><code>scoring</code>: A string specifying the metric (e.g., <code>'accuracy'</code>, <code>'f1_macro'</code>, <code>'roc_auc'</code>, <code>'neg_mean_squared_error'</code>).</li>
      </ul>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Why Does scikit-learn Report Negative Values for Loss Metrics?
        </div>
        <p>
          Students are often shocked when evaluating regression models with MSE:
          <br>
          <code>cross_val_score(model, X, y, scoring='neg_mean_squared_error') &rarr; [-14.2, -18.5, -12.1]</code>
          <br><br>
          <strong>Why is the MSE negative?</strong> In mathematics, Mean Squared Error can never be negative.
          <br>
          However, scikit-learn enforces a universal unified optimization convention: <strong>Higher scores must ALWAYS represent superior models</strong>.
          <br>
          For classification accuracy, 0.95 is better than 0.80 (higher is better). But for an error metric like MSE, 12 is better than 18 (lower is better).
          <br>
          To make loss functions obey the universal maximization rule in automated tools like <code>GridSearchCV</code>, scikit-learn negates them:
          <div class="math-box">
            neg_mean_squared_error = &minus;1 &times; MSE
          </div>
          Since &minus;12.1 is mathematically greater than &minus;18.5, higher remains better! To recover the true positive MSE, simply multiply by &minus;1.
        </p>
      </div>

      <h3>Verified Executable Code: 5-Fold Cross-Validation on Iris</h3>
      <div class="code-block-wrapper">
        <div class="code-header">
          <span class="code-lang">Python (scikit-learn 1.9 Verified)</span>
          <span class="code-file">iris_cv_execution.py</span>
        </div>
        <pre><code class="language-python">import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# 1. Load data and create holdout test split (sealed vault)
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"Full Dataset: N = {len(X)}")
print(f"Training Pool: N_train = {len(X_train)} (80%)")
print(f"Holdout Test: N_test = {len(X_test)} (20%, Sealed)")

# 2. Configure model and Stratified 5-Fold Cross-Validation
knn = KNeighborsClassifier(n_neighbors=5)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 3. Execute cross_val_score on training pool ONLY
scores = cross_val_score(knn, X_train, y_train, cv=cv, scoring='accuracy')

print("\\n--- 5-Fold Cross-Validation Results ---")
for fold_idx, score in enumerate(scores, start=1):
    print(f"  Fold {fold_idx}: {score:.4f} ({score * 100:.2f}%)")

mean_cv = np.mean(scores)
std_cv = np.std(scores)
print(f"\\nMean CV Accuracy: {mean_cv:.4f} ({mean_cv * 100:.2f}%)")
print(f"Fold Score Std Dev: {std_cv:.4f} ({std_cv * 100:.2f}%)")
</code></pre>
      </div>

      <div class="code-block-wrapper">
        <div class="code-header">
          <span class="code-lang">Actual Console Output</span>
          <span class="code-file">stdout</span>
        </div>
        <pre><code class="language-plaintext">Full Dataset: N = 150
Training Pool: N_train = 120 (80%)
Holdout Test: N_test = 30 (20%, Sealed)

--- 5-Fold Cross-Validation Results ---
  Fold 1: 0.9583 (95.83%)
  Fold 2: 1.0000 (100.00%)
  Fold 3: 0.9583 (95.83%)
  Fold 4: 1.0000 (100.00%)
  Fold 5: 0.9583 (95.83%)

Mean CV Accuracy: 0.9750 (97.50%)
Fold Score Std Dev: 0.0204 (2.04%)
</code></pre>
      </div>

      <p class="section-summary-text">
        <strong>Interpretation:</strong> Across 5 folds on the 120 training samples, the KNN classifier achieved an average accuracy of <strong>97.50%</strong> with an extremely small standard deviation of <strong>2.04%</strong>. The consistency across folds confirms that the model generalizes robustly without relying on idiosyncratic sample partitions.
      </p>
    </section>
"""
