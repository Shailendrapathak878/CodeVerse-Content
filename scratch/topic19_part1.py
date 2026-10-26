# Topic 19 Content - Part 1: Sections 01 to 06
# Strict Light Mode Only, Native HTML Math, Verified Numerical Examples

TOPIC19_PART1 = """
    <!-- HERO HEADER -->
    <header class="hero-header">
      <div class="hero-badge">Topic 19 &bull; Evaluation &amp; Metrics</div>
      <h1 class="hero-title">Classification and Regression Metrics</h1>
      <p class="hero-subtitle">
        A complete, beginner-friendly masterclass on evaluating machine learning models. Master confusion matrices, accuracy, precision, recall, specificity, F1, ROC-AUC, Precision-Recall curves, MAE, MSE, RMSE, R-squared, residuals, and leakage-safe validation workflows with Python and scikit-learn.
      </p>
      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <span class="hero-meta-label">Prerequisites</span>
          <span class="hero-meta-val">Basic Python, Intro to ML</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Core Focus</span>
          <span class="hero-meta-val">Model Evaluation &amp; Diagnostics</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Tools</span>
          <span class="hero-meta-val">scikit-learn, NumPy, Matplotlib</span>
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
        Master Curriculum &bull; 27 Sections
      </div>
      <ul class="toc-grid">
        <li><a class="toc-link" href="#sec-01"><span class="toc-num">01</span> Intro to Model Evaluation</a></li>
        <li><a class="toc-link" href="#sec-02"><span class="toc-num">02</span> Actual vs Predicted Values</a></li>
        <li><a class="toc-link" href="#sec-03"><span class="toc-num">03</span> Classification Basics (Spam)</a></li>
        <li><a class="toc-link" href="#sec-04"><span class="toc-num">04</span> Confusion Matrix Anatomy</a></li>
        <li><a class="toc-link" href="#sec-05"><span class="toc-num">05</span> Accuracy &amp; The Paradox</a></li>
        <li><a class="toc-link" href="#sec-06"><span class="toc-num">06</span> Precision &amp; False Alarms</a></li>
        <li><a class="toc-link" href="#sec-07"><span class="toc-num">07</span> Recall &amp; Missed Positives</a></li>
        <li><a class="toc-link" href="#sec-08"><span class="toc-num">08</span> Specificity, FPR &amp; FNR</a></li>
        <li><a class="toc-link" href="#sec-09"><span class="toc-num">09</span> F1-Score &amp; F-Beta Score</a></li>
        <li><a class="toc-link" href="#sec-10"><span class="toc-num">10</span> Classification Thresholds</a></li>
        <li><a class="toc-link" href="#sec-11"><span class="toc-num">11</span> Interactive Threshold Demo</a></li>
        <li><a class="toc-link" href="#sec-12"><span class="toc-num">12</span> ROC Curve &amp; ROC-AUC</a></li>
        <li><a class="toc-link" href="#sec-13"><span class="toc-num">13</span> PR Curve &amp; Average Precision</a></li>
        <li><a class="toc-link" href="#sec-14"><span class="toc-num">14</span> Multiclass Metrics &amp; Averaging</a></li>
        <li><a class="toc-link" href="#sec-15"><span class="toc-num">15</span> Regression Evaluation Basics</a></li>
        <li><a class="toc-link" href="#sec-16"><span class="toc-num">16</span> Mean Absolute Error (MAE)</a></li>
        <li><a class="toc-link" href="#sec-17"><span class="toc-num">17</span> Mean Squared Error (MSE)</a></li>
        <li><a class="toc-link" href="#sec-18"><span class="toc-num">18</span> Root Mean Squared Error (RMSE)</a></li>
        <li><a class="toc-link" href="#sec-19"><span class="toc-num">19</span> MAE vs MSE vs RMSE Comparison</a></li>
        <li><a class="toc-link" href="#sec-20"><span class="toc-num">20</span> Coefficient of Determination (R&sup2;)</a></li>
        <li><a class="toc-link" href="#sec-21"><span class="toc-num">21</span> Residuals &amp; Residual Plots</a></li>
        <li><a class="toc-link" href="#sec-22"><span class="toc-num">22</span> Train, Val, Test Splits &amp; Leakage</a></li>
        <li><a class="toc-link" href="#sec-23"><span class="toc-num">23</span> Selecting the Right Metric</a></li>
        <li><a class="toc-link" href="#sec-24"><span class="toc-num">24</span> Common Mistakes &amp; Pitfalls</a></li>
        <li><a class="toc-link" href="#sec-25"><span class="toc-num">25</span> Complete Python Practical</a></li>
        <li><a class="toc-link" href="#sec-26"><span class="toc-num">26</span> Quick Revision &amp; Formula Sheet</a></li>
        <li><a class="toc-link" href="#sec-27"><span class="toc-num">27</span> Self-Check Quiz &amp; Interview Q&amp;A</a></li>
      </ul>
    </nav>

    <!-- SECTION 01 -->
    <section id="sec-01" class="content-section">
      <span class="section-tag">Section 01</span>
      <h2 class="section-title">Introduction to Model Evaluation</h2>
      <p class="section-intro">
        Building a Machine Learning model is only half the journey. The real test is knowing whether your model's predictions are accurate, reliable, and practically useful on unseen real-world data.
      </p>

      <h3>What Does a Machine Learning Model Predict?</h3>
      <p>
        In supervised machine learning, an algorithm learns patterns from historical input features (denoted as <strong>X</strong>) to predict an outcome target (denoted as <strong>y</strong>). For any given data sample, the model outputs a prediction, conventionally written with a hat symbol: <strong>&#375;</strong> (pronounced <em>"y-hat"</em>).
      </p>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Technical Definition: Model Evaluation
        </div>
        <p>
          <strong>Model Evaluation</strong> is the formal quantitative process of assessing how well an algorithm's predictions (<strong>&#375;</strong>) align with true, ground-truth outcomes (<strong>y</strong>) on a strictly held-out test dataset that the model was never trained on.
        </p>
      </div>

      <h3>Why Good-Looking Training Predictions Are Not Enough</h3>
      <p>
        A common trap for beginners is measuring performance solely on the data used to train the model. A complex model (like an unconstrained Decision Tree or a deep Neural Network) can simply memorize every single training example, achieving 100% training accuracy. However, when deployed in production, this memorized model often fails miserably because it captured random noise rather than real generalizable patterns. This failure mode is called <strong>overfitting</strong>.
      </p>

      <div class="card card-analogy">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 1 0 10 10"/></svg>
          Intuitive Analogy: The Practice Exam vs The Real Final
        </div>
        <p>
          Imagine a student preparing for a mathematics exam by memorizing the answer key to a 50-question practice test. On that practice test, they score a perfect 100%. But on the final examination, where numbers and questions are completely new, they fail because they learned specific answers instead of problem-solving principles. <strong>Training metrics</strong> measure practice test recall; <strong>test evaluation metrics</strong> measure true problem-solving mastery.
        </p>
      </div>

      <h3>Classification vs. Regression: Two Distinct Evaluation Worlds</h3>
      <p>
        The mathematical nature of the target variable dictates how performance must be evaluated:
      </p>
      <ul>
        <li><strong>Classification:</strong> The target <em>y</em> is a <strong>discrete category or class label</strong> (e.g., Spam vs. Not Spam, Fraud vs. Legitimate, Cat vs. Dog vs. Bird). We measure <em>label matches, misclassification counts, and probabilistic calibration</em>.</li>
        <li><strong>Regression:</strong> The target <em>y</em> is a <strong>continuous numerical quantity</strong> (e.g., house price in thousands of dollars, temperature in degrees Celsius, student test score from 0 to 100). We measure the <em>numerical distance (error) between predicted values and actual values</em>.</li>
      </ul>

      <!-- FIGURE 1.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 1.1 &bull; Classification vs Regression Evaluation Overview</span>
          <span class="visual-tag">Conceptual Architecture</span>
        </div>
        __SVG_CLS_VS_REG__
        <div class="visual-caption">
          Figure 1.1: Structural comparison between classification evaluation (discrete matching, confusion matrix, thresholding) and regression evaluation (continuous residuals, numerical distance, variance explained).
        </div>
      </div>
    </section>

    <!-- SECTION 02 -->
    <section id="sec-02" class="content-section">
      <span class="section-tag">Section 02</span>
      <h2 class="section-title">Actual Values, Predicted Values, and Prediction Scores</h2>
      <p class="section-intro">
        Before computing any mathematical metric, you must clearly distinguish between ground truth labels, model probabilities, decision thresholds, and continuous numerical estimates.
      </p>

      <h3>Ground-Truth vs. Model Outputs</h3>
      <p>
        When evaluating models, every observation in our test dataset has two key pieces of information:
      </p>
      <ol>
        <li><strong>Actual Value (y):</strong> The verified true outcome (e.g., this email was confirmed spam; this house sold for $350,000). Also called the <em>ground truth</em> or <em>target</em>.</li>
        <li><strong>Predicted Output (&#375;):</strong> What the machine learning model generated after examining the sample's features.</li>
      </ol>

      <div class="card card-info">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Important Distinction: Predicted Probabilities vs Predicted Classes
        </div>
        <p>
          Most modern classification algorithms (such as Logistic Regression, Random Forests, and Gradient Boosting) do not directly output a hard label like "Spam" or "Not Spam". Instead, they output a continuous <strong>predicted probability score</strong> between 0.0 and 1.0 (e.g., P(y=1|X) = 0.82). A <strong>decision threshold</strong> (typically default $0.50) is applied to convert this continuous score into a final categorical class label.
        </p>
      </div>

      <h3>Concrete Educational Sample: 5 Observations</h3>
      <p>
        Let us observe five sample test records to see both classification and regression targets side by side:
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Sample ID</th>
              <th>Classification Actual (y)</th>
              <th>Predicted Prob P(y=1)</th>
              <th>Predicted Class (&#375;) [Threshold 0.50]</th>
              <th>Regression Actual (y)</th>
              <th>Regression Predicted (&#375;)</th>
              <th>Residual Error (y - &#375;)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Sample #1</strong></td>
              <td>1 (Spam)</td>
              <td>0.92</td>
              <td><span style="color:#15803D; font-weight:700;">1 (Spam) &check;</span></td>
              <td>200,000</td>
              <td>210,000</td>
              <td>-$10,000 (Overpredicted)</td>
            </tr>
            <tr>
              <td><strong>Sample #2</strong></td>
              <td>1 (Spam)</td>
              <td>0.85</td>
              <td><span style="color:#15803D; font-weight:700;">1 (Spam) &check;</span></td>
              <td>250,000</td>
              <td>240,000</td>
              <td>+$10,000 (Underpredicted)</td>
            </tr>
            <tr>
              <td><strong>Sample #3</strong></td>
              <td>0 (Not Spam)</td>
              <td>0.60</td>
              <td><span style="color:#DC2626; font-weight:700;">1 (Spam) &#10006;</span></td>
              <td>300,000</td>
              <td>320,000</td>
              <td>-$20,000 (Overpredicted)</td>
            </tr>
            <tr>
              <td><strong>Sample #4</strong></td>
              <td>0 (Not Spam)</td>
              <td>0.30</td>
              <td><span style="color:#15803D; font-weight:700;">0 (Not Spam) &check;</span></td>
              <td>350,000</td>
              <td>340,000</td>
              <td>+$10,000 (Underpredicted)</td>
            </tr>
            <tr>
              <td><strong>Sample #5</strong></td>
              <td>1 (Spam)</td>
              <td>0.35</td>
              <td><span style="color:#DC2626; font-weight:700;">0 (Not Spam) &#10006;</span></td>
              <td>400,000</td>
              <td>420,000</td>
              <td>-$20,000 (Overpredicted)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- FIGURE 2.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 2.1 &bull; Continuous Probabilities to Discrete Class Labels</span>
          <span class="visual-tag">Decision Logic</span>
        </div>
        __SVG_PROB_THRESHOLD__
        <div class="visual-caption">
          Figure 2.1: Mapping continuous probability estimates along a [0.0, 1.0] spectrum into binary predictions via a decision threshold. Notice how points near the boundary shift classification if the threshold changes.
        </div>
      </div>
    </section>

    <!-- SECTION 03 -->
    <section id="sec-03" class="content-section">
      <span class="section-tag">Section 03</span>
      <h2 class="section-title">Classification Evaluation Basics</h2>
      <p class="section-intro">
        In binary classification, the outcome belongs to one of two mutually exclusive categories: Positive (Class 1) or Negative (Class 0). Every single prediction falls into one of four possible outcomes.
      </p>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          Critical Rule: "Positive" Does Not Mean "Good"
        </div>
        <p>
          In machine learning terminology, the label <strong>"Positive" (Class 1)</strong> simply denotes the specific target condition being investigated or flagged (e.g., spam email, fraudulent transaction, defective component). The label <strong>"Negative" (Class 0)</strong> denotes the default or baseline state (e.g., normal email, legitimate payment, defect-free part). Detecting a severe defect is mathematically a "Positive" detection!
        </p>
      </div>

      <h3>The Four Fundamental Outcomes</h3>
      <p>
        Comparing a model's prediction against reality yields four distinct possibilities:
      </p>
      <ol>
        <li>
          <strong>True Positive (TP):</strong> The actual condition was <em>Positive</em>, and the model correctly predicted <em>Positive</em>.
          <br><em>Spam Example:</em> A real spam email arrives, and the filter correctly sends it to the Spam folder.
        </li>
        <li>
          <strong>True Negative (TN):</strong> The actual condition was <em>Negative</em>, and the model correctly predicted <em>Negative</em>.
          <br><em>Spam Example:</em> A normal email from your colleague arrives, and the filter delivers it to your Inbox.
        </li>
        <li>
          <strong>False Positive (FP) &mdash; Type I Error:</strong> The actual condition was <em>Negative</em>, but the model incorrectly predicted <em>Positive</em>.
          <br><em>Spam Example:</em> A legitimate job offer email is mistakenly flagged and sent to Spam (a <strong>False Alarm</strong>).
        </li>
        <li>
          <strong>False Negative (FN) &mdash; Type II Error:</strong> The actual condition was <em>Positive</em>, but the model incorrectly predicted <em>Negative</em>.
          <br><em>Spam Example:</em> A dangerous phishing spam email slips past the filter and lands in your Inbox (a <strong>Missed Detection</strong>).
        </li>
      </ol>

      <h3>Complete Worked Example: 10 Evaluated Emails</h3>
      <p>
        Consider an evaluation set of 10 emails where 5 are actually Spam (1) and 5 are actually Legitimate (0):
      </p>
      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; 10 Sample Binary Dataset</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>import numpy as np
from sklearn.metrics import confusion_matrix

# True ground-truth labels (1 = Spam, 0 = Legitimate)
y_true = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

# Model predicted probabilities
y_prob = np.array([0.92, 0.85, 0.78, 0.65, 0.35, 0.60, 0.40, 0.30, 0.20, 0.10])

# Convert probabilities to class labels using threshold 0.50
y_pred = (y_prob >= 0.50).astype(int)
# y_pred: [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]

# Calculate confusion matrix components
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

print(f"True Negatives  (TN): {tn}")  # Output: 4
print(f"False Positives (FP): {fp}")  # Output: 1
print(f"False Negatives (FN): {fn}")  # Output: 1
print(f"True Positives  (TP): {tp}")  # Output: 4</code></pre>
      </div>

      <p>
        Let us manually inspect every sample to confirm the counts:
      </p>
      <ul>
        <li>Emails #1, #2, #3, #4: Actual = 1, Predicted = 1 &rarr; <strong>4 True Positives (TP = 4)</strong></li>
        <li>Email #5: Actual = 1, Predicted = 0 &rarr; <strong>1 False Negative (FN = 1)</strong></li>
        <li>Email #6: Actual = 0, Predicted = 1 &rarr; <strong>1 False Positive (FP = 1)</strong></li>
        <li>Emails #7, #8, #9, #10: Actual = 0, Predicted = 0 &rarr; <strong>4 True Negatives (TN = 4)</strong></li>
      </ul>
      <p>
        Total samples = TP + TN + FP + FN = 4 + 4 + 1 + 1 = 10. Everything matches perfectly.
      </p>
    </section>

    <!-- SECTION 04 -->
    <section id="sec-04" class="content-section">
      <span class="section-tag">Section 04</span>
      <h2 class="section-title">Confusion Matrix Anatomy</h2>
      <p class="section-intro">
        A Confusion Matrix is a 2&times;2 grid (for binary tasks) that displays the exact counts of True Positives, False Positives, True Negatives, and False Negatives in one unified visual layout.
      </p>

      <h3>Orientation and Conventions</h3>
      <p>
        In scikit-learn and standard data science practice:
      </p>
      <ul>
        <li><strong>Rows represent Actual (Ground Truth) classes:</strong> Row 0 is Actual Negative (0), Row 1 is Actual Positive (1).</li>
        <li><strong>Columns represent Predicted classes:</strong> Column 0 is Predicted Negative (0), Column 1 is Predicted Positive (1).</li>
      </ul>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
          Scikit-Learn Matrix Layout
        </div>
        <p>
          When calling <code>confusion_matrix(y_true, y_pred)</code>, the returned 2D array has the following structure:
          <br>
          <code>[[TN, FP], [FN, TP]]</code>
          <br>
          Top-left is TN, top-right is FP, bottom-left is FN, bottom-right is TP. Always state your orientation explicitly!
        </p>
      </div>

      <!-- FIGURE 4.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 4.1 &bull; Fully Labelled Confusion Matrix Anatomy</span>
          <span class="visual-tag">Heatmap &amp; Metrics</span>
        </div>
        __SVG_CONFUSION_MATRIX_ANATOMY__
        <div class="visual-caption">
          Figure 4.1: The four quadrants of a binary confusion matrix with exact counts from our 10-sample spam dataset (TN=4, FP=1, FN=1, TP=4). The main diagonal represents correct predictions; off-diagonal cells represent errors.
        </div>
      </div>

      <h3>Generating a Confusion Matrix Heatmap in Python</h3>
      <p>
        Scikit-learn provides <code>ConfusionMatrixDisplay</code> to easily plot beautiful, high-contrast confusion matrices:
      </p>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; Confusion Matrix Heatmap Plotting</span>
          <span>Executable Code</span>
        </div>
        <pre><code>import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Compute matrix
cm = confusion_matrix(y_true, y_pred)

# Display with crisp Light-Mode styling
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Legitimate (0)", "Spam (1)"])
fig, ax = plt.subplots(figsize=(5, 4))
disp.plot(cmap="Blues", ax=ax, values_format="d")
plt.title("Confusion Matrix (10 Sample Email Test)", fontsize=12, fontweight="bold", pad=12)
plt.tight_layout()
# plt.show()</code></pre>
      </div>

      <p>
        <strong>What this matrix reveals:</strong> The model correctly classified 8 out of 10 emails. However, it made one False Alarm (misclassifying 1 legitimate email as spam) and one Missed Detection (letting 1 spam email through). A confusion matrix exposes the <em>types</em> of errors, which a single summary score can easily hide.
      </p>
    </section>

    <!-- SECTION 05 -->
    <section id="sec-05" class="content-section">
      <span class="section-tag">Section 05</span>
      <h2 class="section-title">Accuracy and The Accuracy Paradox</h2>
      <p class="section-intro">
        Accuracy is the most intuitive classification metric: what proportion of all predictions did the model get right? However, on imbalanced datasets, accuracy can be dangerously deceptive.
      </p>

      <h3>Formula and Technical Definition</h3>
      <div class="math-box">
        Accuracy = (TP + TN) / (TP + TN + FP + FN)
        <div class="math-legend">
          &bull; <strong>TP:</strong> True Positives &nbsp;|&nbsp; 
          &bull; <strong>TN:</strong> True Negatives &nbsp;|&nbsp; 
          &bull; <strong>FP:</strong> False Positives &nbsp;|&nbsp; 
          &bull; <strong>FN:</strong> False Negatives &nbsp;|&nbsp; 
          &bull; <strong>Denominator:</strong> Total number of evaluated observations (N)
        </div>
      </div>

      <p>
        <strong>Worked Example:</strong> Using our 10-sample spam dataset:
      </p>
      <div class="math-box">
        Accuracy = (4 + 4) / (4 + 4 + 1 + 1) = 8 / 10 = 0.8000 &nbsp;(80.0%)
      </div>

      <h3>When Is Accuracy Useful?</h3>
      <p>
        Accuracy is a valid, reliable metric <strong>only when two conditions are met simultaneously:</strong>
      </p>
      <ol>
        <li>The dataset has roughly <strong>balanced class distributions</strong> (e.g., 50% Positive, 50% Negative).</li>
        <li>The real-world <strong>cost of a False Positive is approximately equal</strong> to the cost of a False Negative.</li>
      </ol>

      <h3>The Accuracy Paradox on Imbalanced Datasets</h3>
      <p>
        In many real-world machine learning problems, the positive class is extremely rare:
      </p>
      <ul>
        <li>Credit card fraud: 99.8% legitimate transactions, 0.2% fraudulent.</li>
        <li>Factory defect inspection: 99.0% defect-free parts, 1.0% defective.</li>
        <li>Rare disease screening: 99.5% healthy patients, 0.5% positive.</li>
      </ul>

      <p>
        Suppose an email inbox contains <strong>1,000 emails: 990 legitimate and 10 spam</strong>.
        Consider a "dummy model" that has zero intelligence and simply predicts <em>"Legitimate (0)"</em> for every single email:
      </p>
      <ul>
        <li>True Negatives (TN): 990</li>
        <li>False Negatives (FN): 10</li>
        <li>True Positives (TP): 0</li>
        <li>False Positives (FP): 0</li>
      </ul>
      <div class="math-box">
        Dummy Accuracy = (0 + 990) / 1000 = 990 / 1000 = 0.9900 &nbsp;(99.0% Accuracy!)
      </div>

      <p>
        This completely useless model claims <strong>99% accuracy</strong> despite catching <strong>zero spam emails</strong>! If an engineering team evaluates this model by accuracy alone, they might deploy an algorithm that fails 100% of its intended purpose.
      </p>

      <!-- FIGURE 5.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 5.1 &bull; Balanced Dataset vs Imbalanced Dataset Accuracy Paradox</span>
          <span class="visual-tag">Evaluation Risk</span>
        </div>
        __SVG_ACCURACY_PARADOX__
        <div class="visual-caption">
          Figure 5.1: Demonstrating the Accuracy Paradox. On a 99:1 imbalanced dataset, a dummy classifier predicting only the majority class achieves 99% accuracy while detecting 0% of the actual positive cases.
        </div>
      </div>
    </section>

    <!-- SECTION 06 -->
    <section id="sec-06" class="content-section">
      <span class="section-tag">Section 06</span>
      <h2 class="section-title">Precision and The Cost of False Alarms</h2>
      <p class="section-intro">
        When your model sounds an alarm and predicts "Positive", how often is it actually right? That is the essence of Precision.
      </p>

      <h3>Formula and Technical Definition</h3>
      <div class="math-box">
        Precision = TP / (TP + FP)
        <div class="math-legend">
          &bull; <strong>TP:</strong> True Positives (correctly flagged positives)<br>
          &bull; <strong>FP:</strong> False Positives (legitimate items wrongly flagged as positive)<br>
          &bull; <strong>Denominator (TP + FP):</strong> Total number of samples predicted as Positive by the model
        </div>
      </div>

      <p>
        <strong>Worked Example:</strong> In our 10-sample spam dataset, the model predicted 5 emails as spam (TP=4, FP=1):
      </p>
      <div class="math-box">
        Precision = 4 / (4 + 1) = 4 / 5 = 0.8000 &nbsp;(80.0%)
      </div>
      <p>
        This means: <em>"When this model flags an email as Spam, it is correct 80% of the time. 20% of flagged emails are false alarms."</em>
      </p>

      <h3>When Does Precision Matter Most?</h3>
      <p>
        Prioritize <strong>high Precision</strong> when a <strong>False Positive carries high cost, disruption, or harm:</strong>
      </p>
      <ul>
        <li><strong>Spam Filtering:</strong> Sending a legitimate email from a key client or recruiter to Spam is catastrophic. You want high precision so that anything placed in Spam is almost certainly spam.</li>
        <li><strong>Fraud Transaction Freezing:</strong> Inconveniently blocking a customer's debit card at a grocery checkout causes extreme customer dissatisfaction.</li>
        <li><strong>Automated YouTube Copyright Strikes:</strong> Wrongfully penalizing an innocent creator's channel damages creator trust and brand reputation.</li>
      </ul>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Implementation Nuance: Zero Denominator Handling
        </div>
        <p>
          If a conservative model predicts <strong>zero positive samples</strong> (TP = 0 and FP = 0), the formula becomes $0 / 0, which is mathematically undefined. In scikit-learn, this generates a warning unless you explicitly define the parameter <code>zero_division=0</code> (or <code>zero_division=1</code>). Always pass <code>zero_division=0</code> in production evaluation scripts to avoid silent crashes!
        </p>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; Precision Calculation with scikit-learn</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>from sklearn.metrics import precision_score

# Compute precision with safe zero division
prec = precision_score(y_true, y_pred, zero_division=0)
print(f"Precision: {prec:.4f}")  # Output: 0.8000 (80.0%)</code></pre>
      </div>
    </section>
"""
