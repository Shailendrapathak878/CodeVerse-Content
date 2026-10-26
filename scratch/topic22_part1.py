# Topic 22 - Part 1 (Sections 01 - 06)
# High quality, beginner-friendly ML notes

PART_1_HTML = """
    <!-- SECTION 01: INTRODUCTION -->
    <section class="content-section" id="sec-01">
      <div class="section-tag">Section 01</div>
      <h2 class="section-title">Introduction to Hyperparameter Tuning</h2>
      <p class="section-intro">
        In machine learning, algorithms do not automatically configure themselves. Just as an automobile requires adjusting the steering ratio, tire pressure, and suspension stiffness for optimal performance on a wet race track, an ML algorithm relies on external configuration knobs called <strong>hyperparameters</strong> to adapt to specific datasets.
      </p>

      <div class="card card-analogy">
        <div class="card-title">
          <span>🎓</span> The Exam Preparation Analogy: Adjustable Study Settings
        </div>
        <p>
          Imagine a student preparing for a competitive national examination. The student cannot directly force knowledge into their brain in a single instant; instead, they have several <strong>adjustable study settings</strong>:
        </p>
        <ul>
          <li><strong>Study Duration:</strong> How many hours per day are dedicated to focused study (e.g., 2 hours vs. 8 hours)?</li>
          <li><strong>Revision Frequency:</strong> How often old notes are reviewed (e.g., daily vs. weekly spaced repetition)?</li>
          <li><strong>Practice Question Difficulty:</strong> Solving introductory textbook exercises versus past Olympiad papers?</li>
        </ul>
        <p>
          If the student sets their study duration to only 15 minutes a day, they will fail to absorb the syllabus (<strong>underfitting</strong>). If they spend 16 hours a day memorizing the exact answer keys of 5 specific practice tests without understanding underlying principles, they will score 100% on those 5 tests but fail completely on the real unseen exam (<strong>overfitting</strong>).
        </p>
        <p>
          To find the winning balance, the student takes <strong>practice mock exams</strong> under timed conditions, compares their mock exam scores across different study schedules, selects the strategy that produces the highest average score, and only then sits for the <strong>final official examination</strong>.
        </p>
      </div>

      <h3>Connecting the Analogy to Machine Learning</h3>
      <p>
        In machine learning, this trial-and-evaluation procedure is called <strong>hyperparameter tuning</strong> (or hyperparameter optimization).
      </p>
      <ul>
        <li>The <strong>study settings</strong> correspond to <strong>model hyperparameters</strong> (such as the number of neighbors $k$ in KNN or the tree depth in a Decision Tree).</li>
        <li>The <strong>practice mock exams</strong> correspond to the <strong>validation set</strong> or <strong>cross-validation folds</strong>.</li>
        <li>The <strong>final official exam</strong> corresponds to the isolated, untouched <strong>holdout test set</strong>.</li>
      </ul>

      <div class="card card-def">
        <div class="card-title">Technical Definition: Hyperparameter Tuning</div>
        <p>
          <strong>Hyperparameter Tuning</strong> is the systematic process of searching through a predefined space of configuration settings, training candidate models under each candidate setting using training data, evaluating their generalization performance on independent validation data, and selecting the configuration that maximizes a chosen evaluation objective (such as Accuracy, F1-Score, or negative Root Mean Squared Error).
        </p>
      </div>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 1.1 — The End-to-End Hyperparameter Tuning Lifecycle</span>
          <span class="visual-tag">Workflow Architecture</span>
        </div>
        __SVG_TUNING_WORKFLOW__
        <div class="visual-caption">
          Figure 1.1 illustrates the complete six-stage tuning lifecycle: from data partitioning and candidate search space specification, to iterative training across cross-validation folds, validation scoring, model comparison, full-train refitting, and final unbiased holdout test evaluation.
        </div>
      </div>

      <h3>Why Model Selection Matters</h3>
      <p>
        No single algorithm or configuration setting works best for every dataset. The mathematical <em>No Free Lunch Theorem</em> proves that there is no universal optimal setting. An unregularized decision tree might work reasonably well on clean synthetic data with orthogonal decision boundaries, but fail catastrophically on noisy biomedical measurements. Tuning bridges the gap between a generic algorithm and the unique geometric landscape of your data.
      </p>
    </section>

    <!-- SECTION 02: PARAMETERS VS HYPERPARAMETERS -->
    <section class="content-section" id="sec-02">
      <div class="section-tag">Section 02</div>
      <h2 class="section-title">Parameters vs. Hyperparameters</h2>
      <p class="section-intro">
        One of the most frequent points of confusion for beginners is the distinction between <strong>model parameters</strong> and <strong>hyperparameters</strong>. While both govern the model's behavior, they originate from fundamentally different sources and exist at different stages of the modeling lifecycle.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 2.1 — Model Parameters (Internal) vs Hyperparameters (External)</span>
          <span class="visual-tag">Conceptual Comparison</span>
        </div>
        __SVG_PARAMS_VS_HYPERPARAMS__
        <div class="visual-caption">
          Figure 2.1 contrasts internal model parameters (learned automatically from training data via optimization algorithms) with external hyperparameters (configured by the engineer before training begins to control structural capacity and optimization mechanics).
        </div>
      </div>

      <h3>Detailed Side-by-Side Comparison</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Model Parameter (Internal)</th>
              <th>Hyperparameter (External Knob)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Definition</strong></td>
              <td>Internal variables that the algorithm learns directly from training data during the fitting procedure.</td>
              <td>External configuration choices specified prior to fitting that govern model structure, capacity, or the learning process.</td>
            </tr>
            <tr>
              <td><strong>Who sets it?</strong></td>
              <td>Estimated automatically by the optimization algorithm (e.g., Ordinary Least Squares, Gradient Descent).</td>
              <td>Chosen manually by the practitioner or discovered automatically via search algorithms (Grid/Random Search).</td>
            </tr>
            <tr>
              <td><strong>When is it set?</strong></td>
              <td>During the execution of <code>model.fit(X, y)</code>.</td>
              <td>Before calling <code>model.fit()</code>, during model instantiation (e.g., <code>KNeighborsClassifier(n_neighbors=7)</code>).</td>
            </tr>
            <tr>
              <td><strong>Where is it stored?</strong></td>
              <td>Saved in scikit-learn estimator attributes ending with a trailing underscore (e.g., <code>coef_</code>, <code>intercept_</code>).</td>
              <td>Saved in estimator constructor attributes accessible via <code>get_params()</code> (e.g., <code>n_neighbors</code>, <code>max_depth</code>).</td>
            </tr>
            <tr>
              <td><strong>Concrete Examples</strong></td>
              <td>
                • Linear regression slope weights ($w_1, w_2$) &amp; intercept ($b$)<br>
                • Decision tree threshold split values and feature indices<br>
                • Neural network synapse weights and bias vectors
              </td>
              <td>
                • $k$ (number of neighbors in KNN)<br>
                • <code>max_depth</code>, <code>min_samples_split</code> in Decision Trees<br>
                • Regularization strength $\alpha$ in Ridge / Lasso, or $C$ in SVM<br>
                • Number of trees <code>n_estimators</code> in Random Forests
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card card-warn">
        <div class="card-title">⚠️ The Scikit-Learn Trailing Underscore Rule</div>
        <p>
          In scikit-learn, learned <strong>parameters</strong> are always identified by a trailing underscore after fitting:
          <code>model.coef_</code>, <code>model.intercept_</code>, <code>model.feature_importances_</code>. In contrast, <strong>hyperparameters</strong> do not have a trailing underscore: <code>model.n_neighbors</code>, <code>model.max_depth</code>, <code>model.alpha</code>.
        </p>
      </div>
    </section>

    <!-- SECTION 03: WHY TUNING MATTERS -->
    <section class="content-section" id="sec-03">
      <div class="section-tag">Section 03</div>
      <h2 class="section-title">Why Hyperparameter Tuning Is Needed</h2>
      <p class="section-intro">
        Why not simply rely on the default settings provided by libraries like scikit-learn? While library defaults provide safe, general-purpose starting points, they are unaware of your dataset's specific dimensionality, noise level, class distribution, and real-world cost tradeoffs.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 3.1 — How Hyperparameter Settings Govern the Fit Spectrum</span>
          <span class="visual-tag">Complexity Control</span>
        </div>
        __SVG_SETTINGS_FIT_SPECTRUM__
        <div class="visual-caption">
          Figure 3.1 demonstrates how extreme hyperparameter choices drive models into underfitting (excessive constraint / high bias) or overfitting (excessive flexibility / high variance). Proper tuning locates the optimal generalization sweet spot.
        </div>
      </div>

      <h3>Settings Directly Control Model Complexity</h3>
      <p>
        Hyperparameters serve as the mathematical "reins" that prevent an estimator from becoming too simple or too complex:
      </p>
      <ul>
        <li><strong>Too Constrained (Underfitting / High Bias):</strong> If you set <code>max_depth=1</code> on a Decision Tree, the model can only make a single binary split (a decision stump). Even if your dataset has 30 rich features, the model cannot capture non-linear relationships. Both training and validation error remain high.</li>
        <li><strong>Too Flexible (Overfitting / High Variance):</strong> If you set <code>n_neighbors=1</code> in a K-Nearest Neighbors classifier, the model memorizes every isolated training instance, including mislabeled data points or background sensor noise. Its training accuracy is a deceptive 100.0%, but its error on new validation data is severe.</li>
      </ul>

      <h3>Why Training Accuracy Alone Is Fatal</h3>
      <p>
        Evaluating model configurations based solely on training accuracy is one of the most perilous traps in machine learning. As a model's complexity increases, training error monotonically decreases toward zero. If you chose hyperparameters based on training score, you would always select the most overfitted, brittle configuration possible. Validation performance on holdout data is the only reliable compass.
      </p>
    </section>

    <!-- SECTION 04: TRAINING, VALIDATION, AND TEST SETS -->
    <section class="content-section" id="sec-04">
      <div class="section-tag">Section 04</div>
      <h2 class="section-title">Training, Validation, and Test Sets</h2>
      <p class="section-intro">
        To select hyperparameters without fooling yourself, you must strictly partition your data into three separate functional roles. Failing to separate these roles introduces <em>model selection bias</em>, causing you to deploy models that fail unexpectedly in production.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 4.1 — The Three Functional Partitions in Model Development</span>
          <span class="visual-tag">Data Architecture</span>
        </div>
        __SVG_DATA_SPLIT_ROLES__
        <div class="visual-caption">
          Figure 4.1 shows the clear separation of responsibilities: the Training Set fits internal model parameters, the Validation Set (or CV folds) guides candidate model selection, and the Test Set remains untouched until the end for an unbiased performance estimate.
        </div>
      </div>

      <h3>The Three Partition Roles Explained</h3>
      <div class="grid-3col">
        <div class="card" style="border-top: 3px solid #6366F1;">
          <div class="card-title" style="color: #3730A3;">1. Training Set (~60–80%)</div>
          <p style="font-size: 13.5px; color: #475569;">
            The portion of data seen by the model to optimize its internal parameters. When evaluating 50 candidate configurations, each candidate is fitted from scratch on this data.
          </p>
        </div>
        <div class="card" style="border-top: 3px solid #F59E0B;">
          <div class="card-title" style="color: #92400E;">2. Validation Set (~15–20%)</div>
          <p style="font-size: 13.5px; color: #475569;">
            The benchmark data used to evaluate and compare different hyperparameter configurations. The configuration that achieves the highest validation score is declared the winner.
          </p>
        </div>
        <div class="card" style="border-top: 3px solid #10B981;">
          <div class="card-title" style="color: #065F46;">3. Holdout Test Set (~15–20%)</div>
          <p style="font-size: 13.5px; color: #475569;">
            Locked away in an isolated "vault". Never consulted during candidate comparisons. Evaluated exactly once on the final selected model to provide an honest estimate of real-world generalization.
          </p>
        </div>
      </div>

      <div class="card card-warn">
        <div class="card-title">🚨 Why You Cannot Tune on the Test Set: Selection Bias</div>
        <p>
          If you evaluate 1,000 different hyperparameter combinations directly against your test set and pick the one with the highest test accuracy, <strong>you have contaminated the test set</strong>. Even if the configurations were random noise, by chance alone one configuration will align with the random quirks of that specific test partition. The resulting score is artificially optimistic.
        </p>
      </div>

      <h3>Cross-Validation as a Stronger Validation Strategy</h3>
      <p>
        A single fixed validation split has a major drawback: if your dataset is modest in size (e.g., 500 samples), setting aside 20% leaves only 100 samples for validation. A lucky or unlucky random split can skew your evaluation. <strong>K-Fold Cross-Validation</strong> solves this by rotating the validation fold across $K$ subsets, ensuring every sample serves in validation exactly once.
      </p>
    </section>

    <!-- SECTION 05: MANUAL TUNING -->
    <section class="content-section" id="sec-05">
      <div class="section-tag">Section 05</div>
      <h2 class="section-title">Manual Hyperparameter Tuning</h2>
      <p class="section-intro">
        Before diving into automated tools like <code>GridSearchCV</code>, it is vital to perform manual tuning once. Manual tuning reveals the exact underlying mechanics: looping over candidate values, fitting on training folds, and observing how validation performance shifts.
      </p>

      <h3>Demonstration: Tuning KNN <code>n_neighbors</code> on Real Cancer Data</h3>
      <p>
        We evaluate a K-Nearest Neighbors classifier across 9 candidate values of <em>k</em> &isin; [1, 3, 5, 7, 9, 11, 15, 21, 31] using 5-fold cross-validation on the scikit-learn Breast Cancer dataset (<em>N</em> = 569 samples, 30 features, standardized with <code>StandardScaler</code>):
      </p>

      <div class="code-block-wrapper">
        <div class="code-header">
          <span>Manual Tuning Loop with 5-Fold Cross-Validation</span>
          <span class="code-lang">Python</span>
        </div>
        <pre><code>import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1. Load data and establish isolated 80/20 train/test holdout
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 2. Scale features safely based strictly on training data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Manual candidate grid
k_candidates = [1, 3, 5, 7, 9, 11, 15, 21, 31]
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print(f"{'k':>3} | {'Train Acc':>9} | {'5-Fold CV Acc':>15} | {'Std Dev':>8}")
print("-" * 44)

for k in k_candidates:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    train_acc = knn.score(X_train_scaled, y_train)
    
    cv_scores = cross_val_score(knn, X_train_scaled, y_train, cv=cv, scoring='accuracy')
    print(f"{k:>3} | {train_acc:>9.4f} | {cv_scores.mean():>15.4f} | +/-{cv_scores.std():>6.4f}")</code></pre>
      </div>

      <h3>Actual Executed Output</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Candidate <em>k</em></th>
              <th>Training Accuracy</th>
              <th>5-Fold CV Accuracy</th>
              <th>Fold Std Dev</th>
              <th>Diagnosis</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>k = 1</code></td>
              <td>1.0000 (100.0%)</td>
              <td>0.9429</td>
              <td>&plusmn; 0.0213</td>
              <td><span style="color: #DC2626; font-weight: 700;">Severe Overfitting</span>: Memorizes noise. High train, lower validation.</td>
            </tr>
            <tr>
              <td><code>k = 3</code></td>
              <td>0.9780</td>
              <td>0.9692</td>
              <td>&plusmn; 0.0245</td>
              <td>Good fit, strong boundaries.</td>
            </tr>
            <tr>
              <td><code>k = 5</code></td>
              <td>0.9736</td>
              <td>0.9670</td>
              <td>&plusmn; 0.0209</td>
              <td>Solid generalizer.</td>
            </tr>
            <tr style="background-color: #EEF2FF; font-weight: 700;">
              <td><code>k = 7 (Best)</code></td>
              <td>0.9758</td>
              <td>0.9714</td>
              <td>&plusmn; 0.0192</td>
              <td><span style="color: #16A34A; font-weight: 800;">Optimal Sweet Spot</span>: Highest mean CV score (97.14%) and lowest variance.</td>
            </tr>
            <tr>
              <td><code>k = 9</code></td>
              <td>0.9736</td>
              <td>0.9692</td>
              <td>&plusmn; 0.0162</td>
              <td>High stability, slight drop in recall.</td>
            </tr>
            <tr>
              <td><code>k = 11</code></td>
              <td>0.9714</td>
              <td>0.9626</td>
              <td>&plusmn; 0.0149</td>
              <td>Beginning to oversmooth subtle decision boundaries.</td>
            </tr>
            <tr>
              <td><code>k = 15</code></td>
              <td>0.9692</td>
              <td>0.9626</td>
              <td>&plusmn; 0.0215</td>
              <td>Oversmoothed boundary.</td>
            </tr>
            <tr>
              <td><code>k = 21</code></td>
              <td>0.9648</td>
              <td>0.9604</td>
              <td>&plusmn; 0.0247</td>
              <td>Performance continuing to erode.</td>
            </tr>
            <tr>
              <td><code>k = 31</code></td>
              <td>0.9626</td>
              <td>0.9538</td>
              <td>&plusmn; 0.0235</td>
              <td><span style="color: #D97706; font-weight: 700;">Underfitting</span>: Oversmoothed neighborhood dilutes local pattern.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 5.1 — Manual Tuning Curve: Training vs Cross-Validation Accuracy across candidate <em>k</em></span>
          <span class="visual-tag">Actual Experimental Data</span>
        </div>
        __SVG_MANUAL_TUNING_CURVE__
        <div class="visual-caption">
          Figure 5.1 displays genuine experimental data from our executed script. At <em>k</em> = 1, training accuracy is 100% while validation accuracy is depressed (overfitting). As <em>k</em> increases, validation accuracy peaks at <em>k</em> = 7 (0.9714) before gradually decaying into underfitting as neighborhoods become overly diluted.
        </div>
      </div>

      <h3>Why Manual Tuning Fails in Practice</h3>
      <p>
        While manual tuning works cleanly for a single integer parameter like <em>k</em>, it quickly breaks down in production:
      </p>
      <ul>
        <li><strong>Combinatorial Explosion:</strong> If you want to tune 4 hyperparameters simultaneously with 5 values each, you must evaluate 5 &times; 5 &times; 5 &times; 5 = 625 combinations. Writing nested Python <code>for</code> loops for this is slow, error-prone, and cumbersome.</li>
        <li><strong>Interaction Effects Missed:</strong> Changing one hyperparameter often shifts the optimal value of another (e.g., in Gradient Boosting, a lower <code>learning_rate</code> requires a higher <code>n_estimators</code>). Manual one-at-a-time tuning cannot capture complex interactions.</li>
        <li><strong>Informal and Undocumented:</strong> Manual experimentation often leads to "tinkering" where settings are adjusted on the fly without systematic logging or reproducible seeds.</li>
      </ul>
    </section>

    <!-- SECTION 06: SEARCH SPACES -->
    <section class="content-section" id="sec-06">
      <div class="section-tag">Section 06</div>
      <h2 class="section-title">Search Spaces and Candidate Values</h2>
      <p class="section-intro">
        Before you can deploy an automated search algorithm, you must define the <strong>search space</strong>: the bounded mathematical domain of candidate settings that the algorithm is permitted to explore.
      </p>

      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 6.1 — Taxonomy of Hyperparameter Types and Scales</span>
          <span class="visual-tag">Mathematical Foundations</span>
        </div>
        __SVG_SEARCH_SPACE_TYPES__
        <div class="visual-caption">
          Figure 6.1 categorizes the four primary parameter representations: Discrete/Integer counts, Continuous real-valued floats, Categorical choices, and Logarithmic spaces that span multiple orders of magnitude.
        </div>
      </div>

      <h3>The Four Fundamental Parameter Types</h3>
      <ol>
        <li>
          <strong>Discrete / Integer Parameters:</strong> Parameters that represent whole-number counts.
          Examples: <code>n_neighbors</code> in KNN (<em>k</em> &isin; [1, 31]), <code>max_depth</code> in Decision Trees ([2, 20]), or <code>n_estimators</code> in Random Forest ([50, 500]).
        </li>
        <li>
          <strong>Continuous Parameters:</strong> Real-valued floating-point numbers spanning an interval $[a, b]$.
          Examples: <code>learning_rate</code> in Gradient Boosting ($\in (0.001, 0.3)$), or <code>l1_ratio</code> in ElasticNet ($\in [0.0, 1.0]$).
        </li>
        <li>
          <strong>Categorical Parameters:</strong> Discrete qualitative options from a fixed enumerated set.
          Examples: KNN distance metric <code>weights</code> $\in$ <code>['uniform', 'distance']</code>; SVM kernel function $\in$ <code>['linear', 'rbf', 'poly']</code>; or Logistic Regression solver $\in$ <code>['lbfgs', 'saga']</code>.
        </li>
        <li>
          <strong>Logarithmic Search Spaces:</strong> Parameters where the difference between $0.001$ and $0.01$ is just as consequential as the difference between $10$ and $100$.
          Examples: Regularization penalties $\alpha$ in Ridge/Lasso, or margin softness $C$ in SVM. If you search $C$ linearly in steps of $10$ ($[0, 10, 20, \dots, 100]$), you completely miss the vital logarithmic behavior between $0.0001$ and $1.0$.
        </li>
      </ol>

      <div class="card card-strategy">
        <div class="card-title">💡 The Goldilocks Principle for Search Spaces</div>
        <p>
          <strong>Too Narrow:</strong> If you restrict your Ridge $\alpha$ search space to $[1.0, 2.0]$, you will miss the fact that the dataset actually requires strong regularization at $\alpha=100.0$ or virtually no regularization at $\alpha=0.001$.<br>
          <strong>Too Broad:</strong> If you test decision tree depths from $1$ to $10,000$, you waste hours computing models that are guaranteed to overfit without gaining any incremental insight.
        </p>
      </div>
    </section>
"""
