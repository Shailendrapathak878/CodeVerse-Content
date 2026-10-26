# Topic 20 Content - Part 1: Sections 01 to 05
# Strict Light Mode Only, Native HTML Math, Verified Numerical Examples

TOPIC20_PART1 = """
    <!-- HERO HEADER -->
    <header class="hero-header">
      <div class="hero-badge">Topic 20 &bull; Validation &amp; Generalization</div>
      <h1 class="hero-title">Cross-Validation and Model Validation</h1>
      <p class="hero-subtitle">
        A comprehensive, beginner-friendly masterclass on validating machine learning models. Master train/validation/test partitioning, K-Fold and Stratified K-Fold, LOOCV, Group K-Fold, Time-Series validation, hyperparameter tuning with GridSearchCV and RandomizedSearchCV, learning curves, validation curves, and leakage-safe pipelines.
      </p>
      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <span class="hero-meta-label">Prerequisites</span>
          <span class="hero-meta-val">Basic Python, ML Metrics</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Core Focus</span>
          <span class="hero-meta-val">Generalization &amp; Model Selection</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Tools</span>
          <span class="hero-meta-val">scikit-learn, Pipelines, NumPy</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Design Mode</span>
          <span class="hero-meta-val">Strict Light Mode &bull; Accessible</span>
        </div>
      </div>
    </header>

    <!-- TABLE OF CONTENTS -->
    <nav class="toc-card" aria-label="Table of Contents">
      <div class="toc-title">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
        Master Curriculum &bull; 23 Sections
      </div>
      <ul class="toc-grid">
        <li><a class="toc-link" href="#sec-01"><span class="toc-num">01</span> Intro to Model Validation</a></li>
        <li><a class="toc-link" href="#sec-02"><span class="toc-num">02</span> Train, Val, and Test Splits</a></li>
        <li><a class="toc-link" href="#sec-03"><span class="toc-num">03</span> Why Training Accuracy Fails</a></li>
        <li><a class="toc-link" href="#sec-04"><span class="toc-num">04</span> Underfitting vs Overfitting</a></li>
        <li><a class="toc-link" href="#sec-05"><span class="toc-num">05</span> Introduction to Cross-Validation</a></li>
        <li><a class="toc-link" href="#sec-06"><span class="toc-num">06</span> K-Fold CV Step by Step</a></li>
        <li><a class="toc-link" href="#sec-07"><span class="toc-num">07</span> Choosing Number of Folds</a></li>
        <li><a class="toc-link" href="#sec-08"><span class="toc-num">08</span> Stratified K-Fold Cross-Val</a></li>
        <li><a class="toc-link" href="#sec-09"><span class="toc-num">09</span> Other CV Strategies (LOOCV, Group)</a></li>
        <li><a class="toc-link" href="#sec-10"><span class="toc-num">10</span> Time-Series Split &amp; Leakage</a></li>
        <li><a class="toc-link" href="#sec-11"><span class="toc-num">11</span> Cross-Validation in scikit-learn</a></li>
        <li><a class="toc-link" href="#sec-12"><span class="toc-num">12</span> Visualizing Fold Scores</a></li>
        <li><a class="toc-link" href="#sec-13"><span class="toc-num">13</span> Hyperparameter Tuning Basics</a></li>
        <li><a class="toc-link" href="#sec-14"><span class="toc-num">14</span> Exhaustive GridSearchCV</a></li>
        <li><a class="toc-link" href="#sec-15"><span class="toc-num">15</span> Budgeted RandomizedSearchCV</a></li>
        <li><a class="toc-link" href="#sec-16"><span class="toc-num">16</span> Diagnosing with Learning Curves</a></li>
        <li><a class="toc-link" href="#sec-17"><span class="toc-num">17</span> Diagnosing with Validation Curves</a></li>
        <li><a class="toc-link" href="#sec-18"><span class="toc-num">18</span> Data Leakage Anatomy &amp; Prevention</a></li>
        <li><a class="toc-link" href="#sec-19"><span class="toc-num">19</span> Leakage-Safe Pipelines</a></li>
        <li><a class="toc-link" href="#sec-20"><span class="toc-num">20</span> 15 Common Validation Pitfalls</a></li>
        <li><a class="toc-link" href="#sec-21"><span class="toc-num">21</span> Complete Python Practical</a></li>
        <li><a class="toc-link" href="#sec-22"><span class="toc-num">22</span> Quick Revision &amp; Formula Sheet</a></li>
        <li><a class="toc-link" href="#sec-23"><span class="toc-num">23</span> Self-Check Quiz &amp; Technical Q&amp;A</a></li>
      </ul>
    </nav>

    <!-- SECTION 01 -->
    <section id="sec-01" class="content-section">
      <span class="section-tag">Section 01</span>
      <h2 class="section-title">Introduction to Model Validation</h2>
      <p class="section-intro">
        In machine learning, fitting an algorithm to historical data is only the initial step. The fundamental question every engineer must answer is: <em>Will this model actually work when deployed on unseen real-world data?</em>
      </p>

      <h3>What Does Model Training Mean?</h3>
      <p>
        <strong>Model Training</strong> (also called <em>fitting</em>) is the mathematical process where an algorithm examines historical input features (<strong>X</strong>) and known target labels (<strong>y</strong>) to optimize its internal parameters &mdash; such as finding the optimal slopes and intercept in linear regression, splitting thresholds in decision trees, or synaptic weights in neural networks.
      </p>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Technical Definition: Model Validation &amp; Generalization
        </div>
        <p>
          <strong>Model Validation</strong> is the quantitative procedure of assessing how well an estimator performs on independent data that was <em>never used</em> during the fitting process.
          <br><br>
          <strong>Generalization</strong> is the ultimate goal of machine learning: the ability of a trained algorithm to make accurate, reliable predictions on brand-new, previously unseen observations drawn from the same real-world distribution.
        </p>
      </div>

      <div class="card card-analogy">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 1 0 10 10"/></svg>
          Everyday Analogy: The Homework vs The Final Exam
        </div>
        <p>
          Suppose a student prepares for a physics exam by memorizing the answers to a 50-question practice assignment. If the teacher tests them by asking those exact same 50 questions, the student scores 100%. Does that mean the student understands physics? Not necessarily! They may have simply memorized the specific answers.
          <br><br>
          To truly test whether the student learned universal physics principles, the teacher must administer a <strong>final examination with completely new questions</strong>. In machine learning, <strong>training performance</strong> measures how well the model memorized the homework; <strong>validation and test performance</strong> measure whether it actually understands the subject.
        </p>
      </div>

      <h3>Why Training Performance Alone Can Be Fatal</h3>
      <p>
        If you judge a model based on how well it fits its training data, complex models like deep decision trees or unregularized neural networks will always appear superior &mdash; they can easily achieve 100% training accuracy by memorizing random noise, typos, and outliers. But in production, they fail catastrophically. This failure mode is known as <strong>overfitting</strong>.
      </p>

      <!-- FIGURE 1.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 1.1 &bull; End-to-End Model Validation and Selection Workflow</span>
          <span class="visual-tag">System Architecture</span>
        </div>
        __SVG_VAL_WORKFLOW__
        <div class="visual-caption">
          Figure 1.1: The standard 3-stage validation lifecycle. Training data fits parameters; Validation data guides hyperparameter selection and candidate comparison; The final Test Set remains sealed in an untouched vault until the very end.
        </div>
      </div>
    </section>

    <!-- SECTION 02 -->
    <section id="sec-02" class="content-section">
      <span class="section-tag">Section 02</span>
      <h2 class="section-title">Training, Validation, and Test Sets</h2>
      <p class="section-intro">
        To properly validate a machine learning system, the available data must be partitioned into three distinct subsets, each serving a strict, mutually exclusive operational purpose.
      </p>

      <h3>The Three Golden Subsets Explained</h3>
      <ol>
        <li>
          <strong>Training Set (Typically 60% &ndash; 80%):</strong>
          <br>Used exclusively to update the model's learned parameters (e.g., weights, coefficients, tree split criteria). The learning algorithm sees both inputs and labels.
        </li>
        <li>
          <strong>Validation Set (Typically 10% &ndash; 20%):</strong>
          <br>Used during the iterative engineering process to compare candidate algorithms (e.g., Logistic Regression vs Random Forest vs SVM), tune hyperparameters (e.g., tree depth, regularization strength), and calibrate decision thresholds.
        </li>
        <li>
          <strong>Test Set (Typically 10% &ndash; 20%):</strong>
          <br>Kept locked in an untouchable cryptographic vault. It is evaluated <strong>exactly once</strong> at the end of the project to estimate how the chosen model will perform in the real world.
        </li>
      </ol>

      <!-- FIGURE 1.2 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 1.2 &bull; Dataset Splitting Protocol: 70/15/15 on 1,000 Observations</span>
          <span class="visual-tag">Data Partitioning</span>
        </div>
        __SVG_SPLIT_RATIOS__
        <div class="visual-caption">
          Figure 1.2: Proportional breakdown of a 1,000-sample dataset into 700 training samples (70%), 150 validation samples (15%), and 150 held-out test samples (15%).
        </div>
      </div>

      <h3>Comparison Matrix: What Can and Cannot Happen with Each Split</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Dataset Split</th>
              <th>Proportion</th>
              <th>Primary Purpose</th>
              <th>Allowed Actions (&check;)</th>
              <th>Prohibited Actions (&#10006;)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Training Set</strong></td>
              <td>70% &ndash; 80%</td>
              <td>Fit model parameters and optimize objective loss</td>
              <td>Fit scalers, update weights, compute gradients, grow trees</td>
              <td>Do not report training score as final expected accuracy</td>
            </tr>
            <tr>
              <td><strong>Validation Set</strong></td>
              <td>10% &ndash; 20%</td>
              <td>Guide hyperparameter choices and model selection</td>
              <td>Evaluate candidate models, tune thresholds, run CV folds</td>
              <td>Do not fit model parameters or scalers directly on validation data</td>
            </tr>
            <tr>
              <td><strong>Test Set</strong></td>
              <td>10% &ndash; 20%</td>
              <td>Provide unbiased final generalization assessment</td>
              <td>Score the single chosen model exactly once before deployment</td>
              <td><strong>Never</strong> tune parameters, select models, or iterate based on test scores!</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Why a 70/15/15 Split is Not a Universal Law
        </div>
        <p>
          The optimal split ratio depends heavily on the total volume of data:
          <br>&bull; <strong>Small Datasets (N &lt; 1,000):</strong> A fixed 15% validation split contains only 150 samples &mdash; a single lucky or unlucky split can distort your validation score. In small datasets, <strong>K-Fold Cross-Validation replaces the single validation split</strong> to maximize statistical power.
          <br>&bull; <strong>Massive Datasets (N &gt; 1,000,000):</strong> A 98/1/1 split is standard! 1% provides 10,000 validation samples and 10,000 test samples, which is more than enough for high statistical precision while leaving 980,000 samples for training.
        </p>
      </div>
    </section>

    <!-- SECTION 03 -->
    <section id="sec-03" class="content-section">
      <span class="section-tag">Section 03</span>
      <h2 class="section-title">Why Training Accuracy Is Not Enough</h2>
      <p class="section-intro">
        A model that achieves 100% training accuracy may be a triumph of memorization, not learning. Understanding the Generalization Gap is the first step toward building robust models.
      </p>

      <h3>Memorization vs Generalization</h3>
      <p>
        Consider a decision tree allowed to split indefinitely until every single training observation sits in its own isolated leaf node. In this state:
      </p>
      <ul>
        <li><strong>Training Accuracy:</strong> Exactly 100.0%. The tree has a dedicated rule for every past sample.</li>
        <li><strong>Unseen Test Accuracy:</strong> Often drops to 65% or lower! The tree captured idiosyncratic noise, camera glare, or data entry typos that will never appear again.</li>
      </ul>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Technical Definition: The Generalization Gap
        </div>
        <p>
          The <strong>Generalization Gap</strong> is the difference between a model's performance on the training data and its performance on unseen validation/test data:
          <br>
          <div class="math-box">
            Generalization Gap = Training Performance &minus; Validation Performance
          </div>
          A small generalization gap means the model generalizes well. A large, widening generalization gap is the primary quantitative signature of <strong>overfitting</strong>.
        </p>
      </div>

      <!-- FIGURE 1.3 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 1.3 &bull; Training vs Validation Performance &bull; The Generalization Gap</span>
          <span class="visual-tag">Error Curves</span>
        </div>
        __SVG_GENERALIZATION_GAP__
        <div class="visual-caption">
          Figure 1.3: As model complexity increases, training error continues to decrease toward zero. However, validation error reaches a minimum at the optimal sweet spot and then climbs steeply &mdash; creating the Generalization Gap.
        </div>
      </div>
    </section>

    <!-- SECTION 04 -->
    <section id="sec-04" class="content-section">
      <span class="section-tag">Section 04</span>
      <h2 class="section-title">Underfitting, Good Fit, and Overfitting</h2>
      <p class="section-intro">
        Every machine learning algorithm navigates the classic Bias-Variance trade-off. Recognizing where your model sits on the fitting spectrum is essential for applying the correct remedy.
      </p>

      <!-- FIGURE 1.4 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 1.4 &bull; The Fitting Spectrum: Underfitting vs Good Fit vs Overfitting</span>
          <span class="visual-tag">Model Diagnostics</span>
        </div>
        __SVG_FIT_SPECTRUM__
        <div class="visual-caption">
          Figure 1.4: Left: Underfitting (model too rigid to capture true curvature). Center: Good Fit (captures underlying signal while ignoring random noise). Right: Overfitting (erratic decision boundary contorted around individual noise points).
        </div>
      </div>

      <h3>Diagnostic Symptoms and Corrective Actions</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Diagnostic State</th>
              <th>Training Score</th>
              <th>Validation Score</th>
              <th>Root Cause</th>
              <th>Corrective Action (Remedy)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Underfitting (High Bias)</strong></td>
              <td>Low (e.g., 65%)</td>
              <td>Low (e.g., 63%)</td>
              <td>Model lacks mathematical capacity to express the real pattern (e.g., fitting a straight line to quadratic data).</td>
              <td>
                &bull; Increase model complexity (e.g., increase tree depth, add polynomial features)<br>
                &bull; Engineer more informative features<br>
                &bull; Decrease regularization penalty
              </td>
            </tr>
            <tr>
              <td><strong>Good Fit (Optimal Generalization)</strong></td>
              <td>High (e.g., 97%)</td>
              <td>High (e.g., 96%)</td>
              <td>Model captures fundamental underlying relationships without fitting noise.</td>
              <td>
                &bull; Ready for deployment<br>
                &bull; Validate on final sealed test set<br>
                &bull; Monitor for production data drift
              </td>
            </tr>
            <tr>
              <td><strong>Overfitting (High Variance)</strong></td>
              <td>Near Perfect (e.g., 100%)</td>
              <td>Substantially Lower (e.g., 78%)</td>
              <td>Model is excessively flexible and memorized random idiosyncrasies of training samples.</td>
              <td>
                &bull; Apply regularization (L1 Lasso, L2 Ridge)<br>
                &bull; Prune trees (limit <code>max_depth</code>, increase <code>min_samples_split</code>)<br>
                &bull; Collect more training observations<br>
                &bull; Use feature selection / dimensionality reduction
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 05 -->
    <section id="sec-05" class="content-section">
      <span class="section-tag">Section 05</span>
      <h2 class="section-title">Introduction to Cross-Validation</h2>
      <p class="section-intro">
        A single train/validation split is vulnerable to sample selection noise. Cross-validation provides a mathematically robust, variance-reduced evaluation framework.
      </p>

      <h3>The Vulnerability of a Single Split</h3>
      <p>
        Imagine you evaluate a model using a single 80/20 train/validation split. By pure chance:
      </p>
      <ul>
        <li>The 20% validation set happens to contain an unusually high proportion of difficult, noisy outliers &rarr; The reported validation score is <strong>88%</strong> (artificially pessimistic).</li>
        <li>If you reshuffle with a different random seed, the validation set receives only clean, easy samples &rarr; The reported score jumps to <strong>98%</strong> (artificially optimistic).</li>
      </ul>
      <p>
        Which score reflects reality? Neither! Depending on one arbitrary split is like judging a sports team based on a single quarter of a single game.
      </p>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Technical Definition: K-Fold Cross-Validation
        </div>
        <p>
          <strong>K-Fold Cross-Validation</strong> is a resampling technique where the training dataset is partitioned into <strong>K equal-sized subsets (called folds)</strong>. The model is trained and evaluated K separate times: in each iteration, exactly <strong>one fold is reserved for validation</strong> while the remaining <strong>K &minus; 1 folds are pooled together for training</strong>.
        </p>
      </div>

      <!-- FIGURE 1.5 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 1.5 &bull; 5-Fold Cross-Validation Architecture</span>
          <span class="visual-tag">Resampling Architecture</span>
        </div>
        __SVG_KFOLD_5FOLD__
        <div class="visual-caption">
          Figure 1.5: The 5-fold cross-validation architecture. Every observation in the dataset belongs to training in 4 iterations and validation in exactly 1 iteration. No sample is wasted.
        </div>
      </div>
    </section>
"""
