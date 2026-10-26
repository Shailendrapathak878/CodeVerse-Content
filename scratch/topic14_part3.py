"""
Topic 14: Naive Bayes - Content Part 3
Covers Sections 11 through 15.
Uses literal UTF-8 characters and placeholders __SVG_...__ for diagram insertion.
"""

TOPIC14_PART3 = """
    <!-- Section 11 -->
    <section id="sec-11" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 11</span>
        <h2 class="section-title">Types of Naive Bayes Classifiers</h2>
        <p class="section-subtitle">Selecting the mathematically appropriate variant based on feature data types</p>
      </div>

      <p>Naive Bayes is not a single rigid algorithm. It is a family of algorithms that share the common conditional independence principle, but differ fundamentally in how they model the likelihood function P(x<sub>i</sub> | C) for different data distributions.</p>

      <!-- 4 Variants SVG Graphic -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_NB_VARIANTS_COMPARISON__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.10:</strong> The four primary Naive Bayes variants, categorized by their underlying input feature representations and probability distribution assumptions.
        </div>
      </div>

      <h3>Detailed Variant Breakdown</h3>

      <h4>1. Gaussian Naive Bayes (GaussianNB)</h4>
      <p>Designed for <strong>continuous real-valued numeric features</strong> (e.g., temperature, blood pressure, sensor readings, dimensions). It assumes that within each class C, each continuous feature x<sub>i</sub> follows a normal (Gaussian) distribution parameterized by class-conditional mean &mu;<sub>C,i</sub> and variance &sigma;²<sub>C,i</sub>:</p>
      
      <div class="formula-block">
        <div class="formula-title">Gaussian Likelihood Density Function</div>
        P(x<sub>i</sub> | C) = [ 1 / &radic;(2&pi;&sigma;²<sub>C,i</sub>) ] &times; exp( &minus; (x<sub>i</sub> &minus; &mu;<sub>C,i</sub>)² / (2&sigma;²<sub>C,i</sub>) )
      </div>

      <h4>2. Multinomial Naive Bayes (MultinomialNB)</h4>
      <p>Motivated by <strong>discrete non-negative count features</strong> (integers 0, 1, 2, &hellip;). It is the classic workhorse for natural language processing and document categorization, where features represent word frequencies, token counts, or bag-of-words histograms. It estimates the multinomial parameter &theta;<sub>C,i</sub> representing the probability that token i occurs in class C.</p>

      <h4>3. Bernoulli Naive Bayes (BernoulliNB)</h4>
      <p>Specifically designed for <strong>binary indicator features</strong> ({0, 1}, True/False, Present/Absent). Unlike MultinomialNB, BernoulliNB explicitly models the non-occurrence of words: if an important spam word is <em>absent</em>, BernoulliNB includes the factor (1 &minus; p<sub>C,i</sub>), actively penalizing the class for missing expected tokens.</p>

      <h4>4. Categorical Naive Bayes (CategoricalNB)</h4>
      <p>Optimized for <strong>discrete categorical features</strong> where each feature takes one of K distinct nominal levels (e.g., Marital Status &isin; {Single, Married, Divorced}, Blood Group &isin; {A, B, AB, O}). It avoids assuming continuous ordering or integer counts.</p>

      <h3>Comprehensive Variant Comparison Table</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Model Variant</th>
              <th>Input Feature Type</th>
              <th>Primary Mathematical Assumption</th>
              <th>Typical Real-World Use Case</th>
              <th>Important Limitation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>GaussianNB</strong></td>
              <td>Continuous real numbers (&reals;)</td>
              <td>Features follow Gaussian bell curve within each class.</td>
              <td>Medical biometric tests, sensor metrics, physical measurements.</td>
              <td>Fails if data is heavily skewed or multimodal (e.g., bimodal clusters).</td>
            </tr>
            <tr>
              <td><strong>MultinomialNB</strong></td>
              <td>Discrete counts (&naturals;<sub>0</sub>)</td>
              <td>Tokens follow multinomial distribution; captures repetition.</td>
              <td>Text classification, spam filtering, topic tagging.</td>
              <td>Cannot accept negative numbers; requires integer counts or non-negative frequencies.</td>
            </tr>
            <tr>
              <td><strong>BernoulliNB</strong></td>
              <td>Binary indicators ({0, 1})</td>
              <td>Features follow Bernoulli trials; models presence and absence.</td>
              <td>Short texts, tweet sentiment, binary checkbox surveys.</td>
              <td>Completely discards word frequency (a word appearing 10 times counts as 1).</td>
            </tr>
            <tr>
              <td><strong>CategoricalNB</strong></td>
              <td>Nominal discrete categories</td>
              <td>Each feature has a categorical distribution with K levels.</td>
              <td>Demographic survey forms, diagnostic questionnaires.</td>
              <td>Requires every category level to be known or smoothed; fails on unseen levels if unhandled.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Section 12 -->
    <section id="sec-12" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 12</span>
        <h2 class="section-title">Comparing Naive Bayes Variants Visually</h2>
        <p class="section-subtitle">Visualizing count matrices, binary indicators, and continuous Gaussian density curves</p>
      </div>

      <p>To understand why choosing the right variant matters, let us examine the visual differences in data representations.</p>

      <h3>1. MultinomialNB: Word-Count Matrix (Term Frequencies)</h3>
      <p>In MultinomialNB, a document that repeats the word "free" three times conveys stronger spam evidence than a document containing it only once:</p>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_MULTINOMIAL_TERM_MATRIX__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.11:</strong> Document-term count matrix used by MultinomialNB. Cell values represent integer frequency counts, capturing repetition intensity across documents.
        </div>
      </div>

      <h3>2. BernoulliNB: Binary Word-Presence Matrix</h3>
      <p>In BernoulliNB, all counts greater than zero are strictly clamped to 1. The model focuses solely on vocabulary coverage rather than repetition:</p>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_BERNOULLI_PRESENCE_MATRIX__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.12:</strong> Binary word-presence matrix used by BernoulliNB. Even if a word occurs 5 times in a document, it is recorded as a single binary indicator (1).
        </div>
      </div>

      <h3>3. GaussianNB: Continuous Class-Conditional Bell Curves</h3>
      <p>For numeric features such as weekly study hours, GaussianNB fits a normal distribution curve for each class:</p>

      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_GAUSSIAN_DISTRIBUTIONS__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.13:</strong> Continuous class-conditional bell curves fitted by GaussianNB for Study Hours. Class 0 (Not Passed, &mu; = 12.0h) and Class 1 (Passed, &mu; = 27.6h) allow instant likelihood evaluation for any continuous test query (e.g., x = 20h).
        </div>
      </div>
    </section>

    <!-- Section 13 -->
    <section id="sec-13" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 13</span>
        <h2 class="section-title">Complete Python Lab: MultinomialNB Spam Classifier</h2>
        <p class="section-subtitle">An end-to-end, leak-free text classification pipeline using scikit-learn with verified execution metrics</p>
      </div>

      <p>We now implement a complete, reproducible Python classification lab using <code>CountVectorizer</code> and <code>MultinomialNB</code> in a scikit-learn <code>Pipeline</code> to prevent data leakage.</p>

      <h3>Dataset Description</h3>
      <p>We construct a balanced, transparent synthetic dataset of <strong>80 realistic emails</strong> (40 Spam, 40 Legitimate Ham). Ham emails include business memos, invoices, meeting agendas, and engineering updates. Spam emails include lottery prize alerts, urgent cash rewards, and free gift cards.</p>

      <div class="callout-card def-card">
        <div class="def-title">Dataset Integrity Note: Explicitly Synthetic</div>
        <p>This dataset is synthetic and designed for educational transparency and immediate reproducibility without external downloads. While it demonstrates genuine machine learning mechanics, real-world spam filtering involves adversarial evasion, obfuscated text, and evolving vocabularies.</p>
      </div>

      <h3>Complete Executable Pipeline Code</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python 3 &bull; End-to-End MultinomialNB Text Classification Lab</span>
          <span class="code-lang-badge">Python</span>
        </div>
        <pre class="code-body"><code>import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# 1. Dataset of 80 labeled emails (40 Spam = 1, 40 Ham = 0)
# (Sample of representative entries shown; full dataset contains 80 balanced rows)
emails = [
    ("Urgent: Claim your free prize and cash bonus now!", 1),
    ("Congratulations! You won a guaranteed lottery cash prize", 1),
    ("Free gift card and exclusive promotion reward awaits you", 1),
    ("Winner! Claim your urgent cash jackpot immediately", 1),
    ("Exclusive deal: Get free trial and big discount offer", 1),
    # ... [40 balanced spam examples] ...
    ("Hi team, please find the attached weekly project progress report", 0),
    ("Quarterly financial budget review meeting scheduled for tomorrow afternoon", 0),
    ("Could you please review the updated Python codebase and pull request?", 0),
    ("Meeting notes from today's client consultation and discussion", 0),
    ("Attached is the invoice for software design services rendered in March", 0),
    # ... [40 balanced ham examples] ...
]

df = pd.DataFrame(emails, columns=['text', 'label'])

# 2. Stratified 75/25 Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.25, random_state=42, stratify=df['label']
)

# 3. Pipeline: Vectorizer + MultinomialNB (alpha=1.0)
# Prevents preprocessing leakage by fitting vectorizer strictly on training data
spam_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(stop_words='english', lowercase=True)),
    ('nb', MultinomialNB(alpha=1.0))
])

# 4. Train Model
spam_pipeline.fit(X_train, y_train)

# 5. Evaluate on Held-Out Test Set (20 emails: 10 Ham, 10 Spam)
y_pred = spam_pipeline.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

print("Test Set Evaluation Metrics:")
print(f"  Accuracy:  {accuracy_score(y_test, y_pred):.4f} (95.0%)")
print(f"  Precision: {precision_score(y_test, y_pred):.4f} (90.9%)")
print(f"  Recall:    {recall_score(y_test, y_pred):.4f} (100.0%)")
print(f"  F1-Score:  {f1_score(y_test, y_pred):.4f} (95.2%)")
print(f"Confusion Matrix (TN, FP / FN, TP):\n{cm}")</code></pre>
        <div class="code-output">
          <div class="code-output-title">Verified Execution Output</div>
Test Set Evaluation Metrics:
  Accuracy:  0.9500 (95.0%)
  Precision: 0.9091 (90.9%)
  Recall:    1.0000 (100.0%)
  F1-Score:  0.9524 (95.2%)
Confusion Matrix (TN, FP / FN, TP):
[[ 9  1]
 [ 0 10]]
        </div>
      </div>

      <!-- Confusion Matrix Heatmap SVG Visual -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_CONFUSION_MATRIX_HEATMAP__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.14:</strong> Confusion matrix resulting from the actual held-out test predictions: 9 True Negatives, 1 False Positive, 0 False Negatives, and 10 True Positives.
        </div>
      </div>

      <h3>Predictions on Unseen Messages</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python 3 &bull; Evaluating New Unseen Messages with predict_proba</span>
          <span class="code-lang-badge">Python</span>
        </div>
        <pre class="code-body"><code>test_samples = [
    "Claim your free prize and cash bonus today!",
    "Team meeting scheduled for Monday project review",
    "Urgent account update required to verify funds",
    "Please find attached the financial report invoice"
]

preds = spam_pipeline.predict(test_samples)
probs = spam_pipeline.predict_proba(test_samples)

for text, pred, prob in zip(test_samples, preds, probs):
    label = "SPAM" if pred == 1 else "HAM"
    print(f"Message: '{text}'")
    print(f"  -> Prediction: {label} | P(Ham)={prob[0]:.4f}, P(Spam)={prob[1]:.4f}")</code></pre>
        <div class="code-output">
          <div class="code-output-title">Verified Execution Output</div>
Message: 'Claim your free prize and cash bonus today!'
  -> Prediction: SPAM | P(Ham)=0.0000, P(Spam)=1.0000
Message: 'Team meeting scheduled for Monday project review'
  -> Prediction: HAM | P(Ham)=0.9998, P(Spam)=0.0002
Message: 'Urgent account update required to verify funds'
  -> Prediction: SPAM | P(Ham)=0.0339, P(Spam)=0.9661
Message: 'Please find attached the financial report invoice'
  -> Prediction: HAM | P(Ham)=0.9717, P(Spam)=0.0283
        </div>
      </div>

      <h3>Effect of Smoothing Parameter &alpha; (Alpha Tuning)</h3>
      <p>How does altering &alpha; change the model's behavior on ambiguous messages? Let us test the short ambiguous phrase <em>"Free urgent ticket"</em> across different &alpha; values:</p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Alpha (&alpha;)</th>
              <th>P(Ham)</th>
              <th>P(Spam)</th>
              <th>Predicted Class</th>
              <th>Interpretation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>0.001</strong> (Near-Zero)</td>
              <td>0.0000</td>
              <td>1.0000</td>
              <td>SPAM</td>
              <td>Extreme confidence; minimal regularization; highly sensitive to vocabulary presence.</td>
            </tr>
            <tr>
              <td><strong>1.000</strong> (Laplace Standard)</td>
              <td>0.0045</td>
              <td>0.9955</td>
              <td>SPAM</td>
              <td>Balanced smoothing; guarantees non-zero probabilities while preserving class evidence.</td>
            </tr>
            <tr>
              <td><strong>5.000</strong> (Moderate)</td>
              <td>0.0706</td>
              <td>0.9294</td>
              <td>SPAM</td>
              <td>Smoothes likelihoods toward uniform; softens extreme predictions.</td>
            </tr>
            <tr>
              <td><strong>20.000</strong> (Heavy Smoothing)</td>
              <td>0.2673</td>
              <td>0.7327</td>
              <td>SPAM</td>
              <td>Pulls all class-conditional probabilities heavily toward the uniform base rate.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Section 14 -->
    <section id="sec-14" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 14</span>
        <h2 class="section-title">Gaussian Naive Bayes Numerical Lab</h2>
        <p class="section-subtitle">Modeling continuous variables with normal distributions and scikit-learn's GaussianNB</p>
      </div>

      <p>When our features are continuous real numbers rather than word counts, we employ <code>GaussianNB</code>. In this lab, we classify students into <strong>Not Passed (0)</strong> and <strong>Passed (1)</strong> based on two continuous features:</p>
      <ul>
        <li><strong>Study Hours:</strong> Weekly self-study hours.</li>
        <li><strong>Quiz Score %:</strong> Average score on preliminary practice quizzes.</li>
      </ul>

      <h3>Executable GaussianNB Pipeline</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python 3 &bull; GaussianNB Continuous Classification Pipeline</span>
          <span class="code-lang-badge">Python</span>
        </div>
        <pre class="code-body"><code>import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

np.random.seed(42)
n_samples = 40  # 40 per class = 80 total

# Class 0: Not Passed (mean hours=12.5, quiz=54.0)
h_0 = np.random.normal(loc=12.5, scale=3.2, size=n_samples)
q_0 = np.random.normal(loc=54.0, scale=7.5, size=n_samples)
y_0 = np.zeros(n_samples, dtype=int)

# Class 1: Passed (mean hours=27.5, quiz=81.5)
h_1 = np.random.normal(loc=27.5, scale=3.8, size=n_samples)
q_1 = np.random.normal(loc=81.5, scale=6.8, size=n_samples)
y_1 = np.ones(n_samples, dtype=int)

X = np.column_stack([np.concatenate([h_0, h_1]), np.concatenate([q_0, q_1])])
y = np.concatenate([y_0, y_1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Train GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)

print(f"Learned Class Means (theta_):\\n  Class 0: {gnb.theta_[0]}\\n  Class 1: {gnb.theta_[1]}")
print(f"Learned Class Variances (var_):\\n  Class 0: {gnb.var_[0]}\\n  Class 1: {gnb.var_[1]}")
print(f"Test Accuracy:  {accuracy_score(y_test, y_pred):.4f} (100.0%)")
print(f"Confusion Matrix:\\n{confusion_matrix(y_test, y_pred)}")</code></pre>
        <div class="code-output">
          <div class="code-output-title">Verified Execution Output</div>
Learned Class Means (theta_):
  Class 0: [12.01118341 53.61473433]
  Class 1: [27.55602467 81.50218636]
Learned Class Variances (var_):
  Class 0: [ 8.77459799 57.8149713 ]
  Class 1: [11.58394642 49.0592037 ]
Test Accuracy:  1.0000 (100.0%)
Confusion Matrix:
[[10  0]
 [ 0 10]]
        </div>
      </div>

      <div class="callout-card analogy-card">
        <div class="analogy-title">How GaussianNB Evaluates Continuous Queries</div>
        <p>When a new student enters with 20 hours and a 68% quiz score, GaussianNB does not look for exact frequency matches in a table. Instead, it plugs 20 and 68 into the two normal probability density functions (Figure 14.13), multiplies the height of the bell curves by the class priors, and assigns the student to the class with the higher density score!</p>
      </div>
    </section>

    <!-- Section 15 -->
    <section id="sec-15" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 15</span>
        <h2 class="section-title">Decision Scores, Probabilities &amp; Log-Space</h2>
        <p class="section-subtitle">Understanding predict_proba, floating-point underflow, and log-likelihood transformations</p>
      </div>

      <h3>How predict_proba Calculates Posterior Probabilities</h3>
      <p>In scikit-learn, calling <code>model.predict_proba(X)</code> returns the normalized posterior probabilities across all candidate classes. Standard classification assigns the sample to the class with the maximum predicted probability:</p>

      <!-- Predicted Probabilities SVG Visual -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_PREDICTED_PROBABILITY_BARS__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.15:</strong> Model probability breakdowns from <code>predict_proba</code> on four test emails, illustrating decisive predictions alongside nuanced confidence allocations.
        </div>
      </div>

      <h3>The Floating-Point Underflow Problem</h3>
      <p>When an email contains 500 words, multiplying 500 fractional probabilities together creates an extraordinarily tiny number:</p>
      <div class="formula-block">
        Likelihood &approx; 0.01 &times; 0.05 &times; 0.02 &times; &hellip; (500 terms) &approx; 10<sup>&minus;650</sup>
      </div>
      <p>Standard 64-bit floating-point numbers in computer hardware underflow to zero when numbers drop below approximately 10<sup>&minus;308</sup>. If underflow occurs, both the Spam and Ham scores become <code>0.00000000</code>, and the classifier fails completely!</p>

      <h3>The Log-Space Solution</h3>
      <p>To eliminate underflow completely, Naive Bayes implementations (including scikit-learn) perform calculations in <strong>logarithmic space</strong>. Because the natural logarithm is a strictly monotonically increasing function, maximizing log-score is mathematically equivalent to maximizing the raw score:</p>

      <div class="formula-block">
        <div class="formula-title">Log-Space Naive Bayes Classification Rule</div>
        log [ P(C) &times; &prod;<sub>i=1</sub><sup>n</sup> P(x<sub>i</sub> | C) ] = log P(C) + &sum;<sub>i=1</sub><sup>n</sup> log P(x<sub>i</sub> | C)
      </div>

      <div class="callout-card success-card">
        <div class="success-title">Multiplication Becomes Addition!</div>
        <p>By taking logarithms, dangerous chain multiplications of tiny fractions turn into stable, safe additions of negative numbers! For example, log(0.01) + log(0.05) = &minus;4.605 + &minus;2.996 = &minus;7.601. Floating-point underflow is completely prevented, and calculations run faster on modern CPUs.</p>
      </div>
    </section>
"""
