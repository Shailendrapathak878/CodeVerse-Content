"""
Module: topic8_part1.py
Contains HTML for Header, Hero Card, Table of Contents, and Sections 1 to 5.
"""

from scratch.topic8_svgs import (
    SVG_HERO_SPLIT_OVERVIEW,
    SVG_TRAIN_VAL_TEST_ROLES
)

PART1_HTML = f"""
  <!-- HERO CARD -->
  <div class="hero-card">
    <div class="hero-badge">Machine Learning &bull; Topic 8 &bull; Light Mode</div>
    <h1 class="hero-title">Train, Validation &amp; Test Sets</h1>
    <p class="hero-subtitle">
      Master the fundamental principles of dataset partitioning. Learn why models must never be evaluated on their training data, how to divide datasets into independent subsets, how to perform stratified and group-aware splits, how to eliminate data leakage during model selection, and how to conduct true unbiased evaluations.
    </p>
    <div class="hero-meta">
      <span class="meta-tag"><strong>Difficulty:</strong> Beginner &rarr; Production</span>
      <span class="meta-tag"><strong>Focus:</strong> Experimental Design &amp; MLOps</span>
      <span class="meta-tag"><strong>Tooling:</strong> Scikit-Learn 1.9+ &bull; Pandas 2.3+ &bull; NumPy 2.5+</span>
      <span class="meta-tag"><strong>Theme:</strong> Strict Light Mode</span>
    </div>
  </div>

  <!-- TABLE OF CONTENTS -->
  <div class="toc-container">
    <div class="toc-title">
      <span>&#128218;</span> Chapter Table of Contents
    </div>
    <div class="toc-grid">
      <ul class="toc-list">
        <li class="toc-item"><a href="#sec-01"><span class="toc-number">01</span> Introduction: Why Split a Dataset?</a></li>
        <li class="toc-item"><a href="#sec-02"><span class="toc-number">02</span> The Training Set: Learning Parameters</a></li>
        <li class="toc-item"><a href="#sec-03"><span class="toc-number">03</span> The Validation Set: Model Selection</a></li>
        <li class="toc-item"><a href="#sec-04"><span class="toc-number">04</span> The Test Set: Final Unbiased Audit</a></li>
        <li class="toc-item"><a href="#sec-05"><span class="toc-number">05</span> Training vs Validation vs Test</a></li>
        <li class="toc-item"><a href="#sec-06"><span class="toc-number">06</span> Understanding Dataset Split Ratios</a></li>
        <li class="toc-item"><a href="#sec-07"><span class="toc-number">07</span> Calculating Number of Samples</a></li>
        <li class="toc-item"><a href="#sec-08"><span class="toc-number">08</span> Random Splitting &amp; Reproducibility</a></li>
        <li class="toc-item"><a href="#sec-09"><span class="toc-number">09</span> Stratified Splitting for Imbalanced Data</a></li>
      </ul>
      <ul class="toc-list">
        <li class="toc-item"><a href="#sec-10"><span class="toc-number">10</span> Splitting Strategies by Data Type</a></li>
        <li class="toc-item"><a href="#sec-11"><span class="toc-number">11</span> Data Leakage During Splitting</a></li>
        <li class="toc-item"><a href="#sec-12"><span class="toc-number">12</span> Complete Preprocessing Workflow</a></li>
        <li class="toc-item"><a href="#sec-13"><span class="toc-number">13</span> Cross-Validation: How It Fits In</a></li>
        <li class="toc-item"><a href="#sec-14"><span class="toc-number">14</span> Complete Hands-On Python Lab</a></li>
        <li class="toc-item"><a href="#sec-15"><span class="toc-number">15</span> Real-Life Industry Case Studies</a></li>
        <li class="toc-item"><a href="#sec-16"><span class="toc-number">16</span> 14 Common Beginner Mistakes &amp; Fixes</a></li>
        <li class="toc-item"><a href="#sec-17"><span class="toc-number">17</span> Checklist, Glossary, Q&amp;A &amp; Final Challenge</a></li>
      </ul>
    </div>
  </div>

  <!-- SECTION 1: INTRODUCTION: WHY SPLIT A DATASET? -->
  <section id="sec-01" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 01</span>
      <h2 class="section-title">Introduction: Why Split a Dataset?</h2>
    </div>
    <p class="section-intro">
      The ultimate objective of any machine learning model is <strong>generalization</strong>&mdash;the ability to make accurate, reliable predictions on completely new, unseen observations that were never encountered during training.
    </p>

    <div class="card card-def">
      <div class="card-title"><span>&#128214;</span> Core Concept: Memorization vs Generalization</div>
      <p>
        <strong>Memorization (Rote Learning):</strong> A model simply stores the exact training examples in memory. When presented with an identical input, it produces the stored answer with 100% accuracy. However, when presented with a slightly modified input, it fails completely.
      </p>
      <p>
        <strong>Generalization:</strong> A model discovers the true underlying patterns, mathematical relationships, and decision boundaries governing the phenomenon. When presented with unseen data, it correctly deduces the target value.
      </p>
    </div>

    <h3>The Exam Analogy: Why Evaluating on Training Data Fails</h3>
    <p>
      To understand why evaluating an algorithm on the data it trained on produces a false sense of competence, consider a high-school student preparing for a national mathematics examination:
    </p>

    <div class="card card-analogy">
      <div class="card-title"><span>&#128161;</span> The High-School Mathematics Exam Analogy</div>
      <ul>
        <li><strong>Practice Homework Problems (Training Set):</strong> The student solves 500 practice algebra questions from the textbook. The student has access to both the questions and the answers in the back of the book, studying the formulas until they can answer all 500 questions with 100% accuracy.</li>
        <li><strong>Mock Practice Tests (Validation Set):</strong> Before the real exam, the student takes 3 simulated practice tests to decide which strategy works best (e.g. solving equations algebraically vs graphing). The teacher gives feedback on which approach works better.</li>
        <li><strong>The Official Final Exam (Test Set):</strong> On exam day, the student sits in a proctored room and receives brand-new questions that have never been seen before. This exam provides an <em>unbiased measure</em> of whether the student truly understands algebra or simply memorized the textbook questions!</li>
      </ul>
      <p>
        <strong>The Machine Learning Moral:</strong> If the teacher tested the student using the exact same 500 homework problems, a student who merely memorized the answer keys would score 100%, masking their total inability to solve new math problems! In machine learning, evaluating a model on its training data produces this exact delusion.
      </p>
    </div>

    <!-- FIGURE 8.1: HERO SPLIT OVERVIEW -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_HERO_SPLIT_OVERVIEW}
      </div>
      <div class="diagram-caption">Figure 8.1: The Golden Triad of Dataset Partitioning: Dividing raw data into independent Training (70%), Validation (15%), and Test (15%) subsets.</div>
      <div class="how-to-read">
        <div class="how-to-read-title"><span>&#128269;</span> How to Read This Architectural Diagram:</div>
        <ul>
          <li><strong>Top Bar:</strong> The full collected dataset (100% of samples) contains all available observations.</li>
          <li><strong>Training Partition (70%):</strong> Dedicated exclusively to fitting internal model parameters (weights, biases, tree splits) and fitting preprocessing scalers/encoders.</li>
          <li><strong>Validation Partition (15%):</strong> Dedicated to comparing candidate models, tuning hyperparameters, and deciding model complexity.</li>
          <li><strong>Test Partition (15%):</strong> Kept in a strictly sealed vault until all development decisions are finalized, providing the single unbiased audit of production readiness.</li>
        </ul>
      </div>
      <div class="diagram-takeaway">
        <strong>Key Takeaway:</strong> Dataset splitting enforces a strict wall of separation between <em>learning</em>, <em>decision-making</em>, and <em>evaluation</em>.
      </div>
    </div>
  </section>

  <!-- SECTION 2: THE TRAINING SET -->
  <section id="sec-02" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 02</span>
      <h2 class="section-title">The Training Set: Learning Parameters</h2>
    </div>
    <p class="section-intro">
      The <strong>training set</strong> is the portion of the dataset directly ingested by the machine learning algorithm during the fitting process. It constitutes the primary knowledge base from which the model constructs its mathematical mapping from features (X) to targets (y).
    </p>

    <div class="card card-def">
      <div class="card-title"><span>&#128214;</span> What Are Model Parameters?</div>
      <p>
        <strong>Model Parameters</strong> are the internal numerical variables that the algorithm learns directly from the training data during optimization:
      </p>
      <ul>
        <li>In <strong>Linear &amp; Logistic Regression:</strong> The weights (coefficients) <code>w<sub>1</sub>, w<sub>2</sub>, ...</code> and intercept (bias) <code>b</code>.</li>
        <li>In <strong>Neural Networks:</strong> The connection weights and node biases across all hidden layers.</li>
        <li>In <strong>Decision Trees:</strong> The exact feature thresholds selected at each split node (e.g. <code>Age &le; 35.5</code>).</li>
      </ul>
      <p>
        These parameters are adjusted iteratively to minimize the training loss function (such as Mean Squared Error or Cross-Entropy).
      </p>
    </div>

    <h3>A Concrete Tabular Example</h3>
    <p>
      Consider 5 sample records from a real-estate dataset predicting home selling prices:
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Sample ID</th>
            <th>Square Footage (X<sub>1</sub>)</th>
            <th>Bedrooms (X<sub>2</sub>)</th>
            <th>Sale Price (y)</th>
            <th>Assigned Partition</th>
            <th>How It Is Used</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>REC-001</code></td>
            <td>1,450</td>
            <td>3</td>
            <td>$285,000</td>
            <td><span class="key-badge badge-train">Training Set</span></td>
            <td>Model views X and y to compute weight updates.</td>
          </tr>
          <tr>
            <td><code>REC-002</code></td>
            <td>2,100</td>
            <td>4</td>
            <td>$395,000</td>
            <td><span class="key-badge badge-train">Training Set</span></td>
            <td>Model views X and y to compute weight updates.</td>
          </tr>
          <tr>
            <td><code>REC-003</code></td>
            <td>1,200</td>
            <td>2</td>
            <td>$230,000</td>
            <td><span class="key-badge badge-val">Validation Set</span></td>
            <td>Used to compare model architectures; weights never updated on this.</td>
          </tr>
          <tr>
            <td><code>REC-004</code></td>
            <td>2,800</td>
            <td>5</td>
            <td>$510,000</td>
            <td><span class="key-badge badge-train">Training Set</span></td>
            <td>Model views X and y to compute weight updates.</td>
          </tr>
          <tr>
            <td><code>REC-005</code></td>
            <td>1,750</td>
            <td>3</td>
            <td>$320,000</td>
            <td><span class="key-badge badge-test">Test Set</span></td>
            <td>Locked in vault until final audit. Never seen during training!</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> Why Training Accuracy Can Be a Complete Lie</div>
      <p>
        A 1-Nearest Neighbor classifier (KNN with <code>k=1</code>) or an unconstrained Decision Tree with infinite depth will achieve <strong>100.0% training accuracy</strong> on almost any classification problem!
      </p>
      <p>
        Does this mean the model is a genius? No! It simply means the model memorized every training row. If the training data contains noise, typos, or outliers, the model memorized the noise as well (<em>overfitting</em>). Training performance indicates how well the model fit historical samples; it provides <strong>zero statistical evidence</strong> of whether the model will succeed on future samples.
      </p>
    </div>
  </section>

  <!-- SECTION 3: THE VALIDATION SET -->
  <section id="sec-03" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 03</span>
      <h2 class="section-title">The Validation Set: Model Selection</h2>
    </div>
    <p class="section-intro">
      The <strong>validation set</strong> (sometimes called the <em>development set</em> or <em>dev set</em>) is an independent subset used exclusively during the development phase to evaluate competing model architectures, tune hyperparameters, and prevent overfitting.
    </p>

    <div class="card card-def">
      <div class="card-title"><span>&#128214;</span> Parameters vs Hyperparameters: The Core Distinction</div>
      <p>
        Beginners often confuse parameters with hyperparameters. Here is the definitive distinction:
      </p>
      <ul>
        <li><strong>Parameters:</strong> Learned <em>automatically</em> by the algorithm from the training data (e.g. weights <code>w</code>, intercept <code>b</code>). The engineer does not set these manually.</li>
        <li><strong>Hyperparameters:</strong> Configured <em>manually</em> by the machine learning engineer <strong>before</strong> training begins. They control the learning process, model capacity, and regularization strength (e.g. <code>k</code> in KNN, tree <code>max_depth</code>, learning rate <code>&alpha;</code>, regularization penalty <code>&lambda;</code>).</li>
      </ul>
    </div>

    <h3>How the Validation Set Guides Engineering Decisions</h3>
    <p>
      Suppose you are building a customer churn predictor and want to determine the optimal neighbor count <code>k</code> for a KNN model:
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Candidate Model</th>
            <th>Hyperparameter Setting</th>
            <th>Training Accuracy</th>
            <th>Validation Accuracy</th>
            <th>Engineering Conclusion</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Model A</strong></td>
            <td><code>k = 1</code> (High Complexity)</td>
            <td><strong>100.0%</strong></td>
            <td>71.4%</td>
            <td><span class="key-badge badge-leak">Severely Overfitted</span> (Memorized noise)</td>
          </tr>
          <tr>
            <td><strong>Model B</strong></td>
            <td><code>k = 7</code> (Balanced Complexity)</td>
            <td>86.5%</td>
            <td><strong>83.3%</strong></td>
            <td><span class="key-badge badge-test">&check; Optimal Winner</span> (Best generalization)</td>
          </tr>
          <tr>
            <td><strong>Model C</strong></td>
            <td><code>k = 45</code> (Low Complexity)</td>
            <td>74.0%</td>
            <td>73.1%</td>
            <td><span class="key-badge badge-val">Underfitted</span> (Oversmoothed boundary)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-concept">
      <div class="card-title"><span>&#9777;</span> The Subtle Feedback Loop: Validation "Snoop" Leakage</div>
      <p>
        Notice what happened in the table above: we tried three different values of <code>k</code> and selected <strong>Model B</strong> because it had the highest score on the validation set.
      </p>
      <p>
        Because our human decisions were guided by the validation score, information from the validation set indirectly influenced the final model selection! If an engineer tries 500 different hyperparameter combinations, they will eventually find one that performs exceptionally well on that specific validation set purely by random chance.
      </p>
      <p>
        This is why <strong>a validation set cannot serve as the final unbiased test set</strong>. We need a completely separate, pristine dataset that was never involved in any training or tuning decisions whatsoever.
      </p>
    </div>
  </section>

  <!-- SECTION 4: THE TEST SET -->
  <section id="sec-04" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 04</span>
      <h2 class="section-title">The Test Set: Final Unbiased Audit</h2>
    </div>
    <p class="section-intro">
      The <strong>test set</strong> (often called the <em>holdout set</em> or <em>golden evaluation set</em>) is the final, untouched partition of data. Its sole purpose is to provide a realistic, statistically valid estimate of how the final selected model will perform in the live production environment.
    </p>

    <!-- FIGURE 8.6: EXAM ANALOGY -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_TRAIN_VAL_TEST_ROLES}
      </div>
      <div class="diagram-caption">Figure 8.2: The distinct functional roles of Training (parameter learning), Validation (hyperparameter selection), and Test (final unbiased audit).</div>
    </div>

    <h3>The Cardinal Rules of the Test Set</h3>
    <ol>
      <li><strong>Rule 1: Evaluate ONLY ONCE.</strong> The test set should only be evaluated after all model architectures, feature choices, and hyperparameters have been finalized.</li>
      <li><strong>Rule 2: NEVER Tune Based on Test Scores.</strong> If a model achieves 82% on the test set, you must NOT go back, adjust your learning rate or tree depth, and test again! The moment you tune hyperparameters based on test results, your test set becomes a validation set, and its unbiased integrity is permanently destroyed.</li>
      <li><strong>Rule 3: NEVER Fit Preprocessing on Test Data.</strong> Imputers, scalers, and categorical encoders must be fitted on training data only. Test features are transformed using the parameters learned from the training set.</li>
      <li><strong>Rule 4: Test Scores are Estimates, Not Absolute Guarantees.</strong> A test score is a point estimate of expected performance. If live production data experiences concept drift (changes in user behavior, seasonal shifts, macroeconomic shocks), real-world performance will diverge from test metrics.</li>
    </ol>
  </section>

  <!-- SECTION 5: TRAINING VS VALIDATION VS TEST -->
  <section id="sec-05" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 05</span>
      <h2 class="section-title">Training vs Validation vs Test: The Definitive Comparison</h2>
    </div>
    <p class="section-intro">
      Below is the comprehensive comparison matrix contrasting the three fundamental dataset subsets.
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Attribute</th>
            <th>Training Set</th>
            <th>Validation Set</th>
            <th>Test Set</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Main Purpose</strong></td>
            <td>Learn model parameters (weights, biases, tree splits).</td>
            <td>Guide model selection, hyperparameter tuning, and early stopping.</td>
            <td>Provide an unbiased evaluation of the final selected model.</td>
          </tr>
          <tr>
            <td><strong>Exam Analogy</strong></td>
            <td>Textbook chapters and worked practice exercises.</td>
            <td>Mock practice tests and strategy quizzes.</td>
            <td>The official final certification examination.</td>
          </tr>
          <tr>
            <td><strong>Model Parameters Fitted?</strong></td>
            <td><span class="key-badge badge-train">YES</span> (Backpropagation / OLS)</td>
            <td><span class="key-badge badge-leak">NO</span> (Never used in fit)</td>
            <td><span class="key-badge badge-leak">NO</span> (Never used in fit)</td>
          </tr>
          <tr>
            <td><strong>Hyperparameters Tuned?</strong></td>
            <td><span class="key-badge badge-leak">NO</span> (Causes severe overfitting)</td>
            <td><span class="key-badge badge-val">YES</span> (Primary purpose)</td>
            <td><span class="key-badge badge-leak">NO</span> (Destroys test integrity)</td>
          </tr>
          <tr>
            <td><strong>Preprocessing Fitted?</strong></td>
            <td><span class="key-badge badge-train">YES</span> (fit_transform)</td>
            <td><span class="key-badge badge-leak">NO</span> (transform only)</td>
            <td><span class="key-badge badge-leak">NO</span> (transform only)</td>
          </tr>
          <tr>
            <td><strong>Evaluation Frequency</strong></td>
            <td>Every epoch / iteration during training.</td>
            <td>Every candidate model / epoch for tuning.</td>
            <td><strong>Exactly ONCE</strong> at project completion.</td>
          </tr>
          <tr>
            <td><strong>Consequence of Misuse</strong></td>
            <td>Underfitting if too small; noise memorization if too complex.</td>
            <td>Overfitting to validation set if tuned excessively.</td>
            <td>Overly optimistic metric; silent failure in production.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-success">
      <div class="card-title"><span>&#10003;</span> The Memorable Summary Formula</div>
      <p style="font-size: 1.1rem; line-height: 1.8;">
        &bull; <strong>TRAIN:</strong> Learn what the data says.
        <br>&bull; <strong>VALIDATE:</strong> Decide which model learned best.
        <br>&bull; <strong>TEST:</strong> Verify what the model will do in the real world.
      </p>
    </div>
  </section>
"""
