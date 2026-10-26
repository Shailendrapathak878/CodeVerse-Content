"""
Topic 14: Naive Bayes - Content Part 4
Covers Sections 16 through 23, plus Footer.
Uses literal UTF-8 characters and structured Light Mode cards.
"""

TOPIC14_PART4 = """
    <!-- Section 16 -->
    <section id="sec-16" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 16</span>
        <h2 class="section-title">Model Evaluation &amp; Error Cost Tradeoffs</h2>
        <p class="section-subtitle">Evaluating classification performance and asymmetric real-world error costs</p>
      </div>

      <p>A machine learning model cannot be judged by accuracy alone. In spam filtering and medical diagnostics, different types of errors carry drastically different consequences.</p>

      <h3>The Confusion Matrix Components</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Matrix Term</th>
              <th>Technical Meaning</th>
              <th>Spam Filter Reality</th>
              <th>Real-World Impact</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>True Positive (TP)</strong></td>
              <td>Actual Positive correctly predicted as Positive.</td>
              <td>Actual spam email correctly sent to the spam folder.</td>
              <td>Success: Clean inbox.</td>
            </tr>
            <tr>
              <td><strong>True Negative (TN)</strong></td>
              <td>Actual Negative correctly predicted as Negative.</td>
              <td>Actual legitimate email delivered to the main inbox.</td>
              <td>Success: Work continues normally.</td>
            </tr>
            <tr>
              <td><strong>False Positive (FP)</strong></td>
              <td>Actual Negative incorrectly predicted as Positive.</td>
              <td>Legitimate email mistakenly blocked or sent to spam!</td>
              <td><span style="color:#DC2626;font-weight:700;">Severe Cost:</span> Missed job offers, invoices, or emergency alerts.</td>
            </tr>
            <tr>
              <td><strong>False Negative (FN)</strong></td>
              <td>Actual Positive incorrectly predicted as Negative.</td>
              <td>Spam email mistakenly allowed into the inbox.</td>
              <td><span style="color:#D97706;font-weight:700;">Minor Inconvenience:</span> User clicks delete.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Standard Evaluation Metrics</h3>
      <div class="formula-block">
        <div class="formula-title">Classification Metric Mathematical Formulas</div>
        &bull; Accuracy = (TP + TN) / (TP + TN + FP + FN)<br>
        &bull; Precision = TP / (TP + FP)   [Of all flagged as spam, what fraction is truly spam?]<br>
        &bull; Recall = TP / (TP + FN)      [Of all actual spam, what fraction did we catch?]<br>
        &bull; F1-Score = 2 &times; (Precision &times; Recall) / (Precision + Recall)
      </div>

      <div class="callout-card warn-card">
        <div class="warn-title">The Asymmetric Cost of False Positives</div>
        <p>In spam classification, <strong>Precision is far more critical than Recall</strong>. Users will tolerate an occasional spam message slipping into their inbox (False Negative), but they will abandon an email service if an urgent flight ticket, job interview invitation, or bank password reset email is incorrectly classified as spam (False Positive). Therefore, production spam filters often set higher classification probability thresholds (e.g., P(Spam) &gt; 0.90) to minimize False Positives.</p>
      </div>
    </section>

    <!-- Section 17 -->
    <section id="sec-17" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 17</span>
        <h2 class="section-title">Advantages &amp; Fundamental Limitations</h2>
        <p class="section-subtitle">A balanced, objective engineering assessment of Naive Bayes classifiers</p>
      </div>

      <h3>Key Advantages</h3>
      <ul>
        <li><strong>Blazing Fast Training and Inference:</strong> Training requires only a single pass over the training data to aggregate frequency counts. It trains in O(N &times; D) time, making it significantly faster than gradient descent or kernel SVMs.</li>
        <li><strong>Low Computational and Memory Footprint:</strong> Requires storing only small count tables or mean/variance vectors per class. Ideal for edge devices and resource-constrained microcontrollers.</li>
        <li><strong>Effective Baseline for High-Dimensional Text:</strong> In document classification with vocabularies of 20,000+ words, Naive Bayes often performs on par with or better than complex neural networks, especially when training samples are limited.</li>
        <li><strong>Naturally Handles Missing Values:</strong> If a test email does not contain a particular word, that feature is simply skipped in the product chain during likelihood evaluation.</li>
        <li><strong>Multiple Specialized Variants:</strong> Supports text counts (MultinomialNB), binary flags (BernoulliNB), continuous metrics (GaussianNB), and categories (CategoricalNB).</li>
      </ul>

      <h3>Fundamental Limitations</h3>
      <ul>
        <li><strong>The Independence Assumption is Rarely True:</strong> In real datasets, features often exhibit strong correlations. While classification order often survives, correlated features cause overcounting of evidence.</li>
        <li><strong>Poor Probability Calibration:</strong> Because feature likelihoods are multiplied independently, posterior probabilities tend to cluster excessively near 0.0 or 1.0. A predicted probability of 0.999 does not mean the model has true 99.9% empirical calibration.</li>
        <li><strong>Zero-Frequency Hazard:</strong> Without Laplace smoothing (&alpha; &gt; 0), any previously unseen feature value in a class forces the entire class score to zero.</li>
        <li><strong>Continuous Normality Assumption in GaussianNB:</strong> If continuous numeric features exhibit multi-modal distributions, heavy tails, or power laws, GaussianNB's single bell curve model will mischaracterize the feature density.</li>
      </ul>
    </section>

    <!-- Section 18 -->
    <section id="sec-18" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 18</span>
        <h2 class="section-title">Naive Bayes vs. Other ML Classifiers</h2>
        <p class="section-subtitle">Comparing algorithmic strengths, training speed, interpretability, and boundary shapes</p>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Algorithm</th>
              <th>Decision Paradigm</th>
              <th>Training Speed</th>
              <th>Inference Speed</th>
              <th>Handling of Correlated Features</th>
              <th>Primary Limitation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Naive Bayes</strong></td>
              <td>Probabilistic factorization (Bayes' Theorem)</td>
              <td>Extremely Fast (O(N &times; D) single pass)</td>
              <td>Extremely Fast (linear vector product)</td>
              <td>Poor (assumes conditional independence)</td>
              <td>Poorly calibrated probabilities; sensitive to correlations.</td>
            </tr>
            <tr>
              <td><strong>Logistic Regression</strong></td>
              <td>Linear weighted sum passed through sigmoid</td>
              <td>Fast (iterative convex optimization)</td>
              <td>Very Fast (dot product)</td>
              <td>Good (learns joint weights; handles co-occurrence)</td>
              <td>Linear decision boundary only unless polynomial features added.</td>
            </tr>
            <tr>
              <td><strong>K-Nearest Neighbors</strong></td>
              <td>Geometric distance to local neighbors</td>
              <td>Zero training (lazy learner)</td>
              <td>Slow (scans all training instances)</td>
              <td>Moderate (degrades under curse of dimensionality)</td>
              <td>High inference latency and memory requirements on large datasets.</td>
            </tr>
            <tr>
              <td><strong>Decision Trees</strong></td>
              <td>Hierarchical axis-aligned feature splits</td>
              <td>Moderate (evaluates information gain / Gini)</td>
              <td>Fast (branch traversal)</td>
              <td>Good (evaluates features sequentially in context)</td>
              <td>High risk of overfitting without pruning or ensemble methods.</td>
            </tr>
            <tr>
              <td><strong>Support Vector Machines</strong></td>
              <td>Maximum margin separating hyperplane</td>
              <td>Slow on large N (O(N² to N³))</td>
              <td>Moderate (computes kernel to support vectors)</td>
              <td>Excellent (finds optimal separating margin)</td>
              <td>Computationally heavy on massive text corpora; requires careful scaling.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Section 19 -->
    <section id="sec-19" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 19</span>
        <h2 class="section-title">Real-Life Production Case Studies</h2>
        <p class="section-subtitle">Four practical production scenarios where Naive Bayes is successfully deployed</p>
      </div>

      <h3>Case Study 1: Production Email Spam Filtering</h3>
      <p><strong>Problem:</strong> An email service provider processes 50 million incoming emails daily and must classify each message within 2 milliseconds.</p>
      <p><strong>Feature Representation:</strong> Bag-of-words token counts extracted using <code>CountVectorizer</code> with an established vocabulary of 50,000 words.</p>
      <p><strong>Model Variant:</strong> <code>MultinomialNB(alpha=1.0)</code>.</p>
      <p><strong>Why it Works:</strong> Count tables are precomputed in RAM. Classifying an incoming email involves looking up the word counts, taking log additions, and checking if log P(Spam|X) &minus; log P(Ham|X) exceeds a conservative threshold. Inference takes less than 0.5 milliseconds.</p>

      <h3>Case Study 2: News-Topic &amp; Article Categorization</h3>
      <p><strong>Problem:</strong> A digital media aggregator ingests articles from hundreds of RSS feeds and classifies them into categories: <em>Politics, Sports, Technology, Business, Entertainment</em>.</p>
      <p><strong>Feature Representation:</strong> TF-IDF or normalized word frequencies across article headlines and lead paragraphs.</p>
      <p><strong>Model Variant:</strong> <code>MultinomialNB(alpha=0.5)</code>.</p>
      <p><strong>Why it Works:</strong> MultinomialNB handles multi-class classification natively by computing scores for all five classes and selecting the highest argmax class. Strong domain-specific keywords ("touchdown", "semiconductor", "legislation") provide decisive class signals.</p>

      <h3>Case Study 3: Customer Sentiment Analysis</h3>
      <p><strong>Problem:</strong> An e-commerce platform monitors product reviews to flag negative feedback for immediate customer support follow-up.</p>
      <p><strong>Feature Representation:</strong> Binary presence of positive/negative sentiment tokens, negation phrases ("not clean", "never arrived"), and emoji markers.</p>
      <p><strong>Model Variant:</strong> <code>BernoulliNB(alpha=1.0)</code>.</p>
      <p><strong>Why it Works:</strong> For short customer reviews (1&ndash;2 sentences), word presence/absence is often more informative than raw repetition. BernoulliNB models the absence of positive terms as an indicator of negative sentiment.</p>

      <h3>Case Study 4: Preliminary Health Symptom Screening</h3>
      <p><strong>Problem:</strong> A telehealth triage intake chatbot analyzes patient symptom checklists to recommend appropriate medical specialties.</p>
      <p><strong>Feature Representation:</strong> Combination of binary symptom indicators (fever: yes/no, cough: yes/no) and continuous vital signs (body temperature, pulse rate).</p>
      <p><strong>Model Variant:</strong> Mixed setup or <code>GaussianNB</code> for continuous vitals alongside <code>CategoricalNB</code> for symptom checklists.</p>
      <p><strong>Why it Works:</strong> Provides rapid probabilistic ranking of possible conditions while transparently allowing clinicians to inspect individual likelihood contributions.</p>
    </section>

    <!-- Section 20 -->
    <section id="sec-20" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 20</span>
        <h2 class="section-title">Common Beginner Mistakes &amp; Fixes</h2>
        <p class="section-subtitle">Twelve critical conceptual, mathematical, and coding errors and how to avoid them</p>
      </div>

      <!-- Mistake 1 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 01 &bull; Confusing P(A | B) with P(B | A)</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Assuming that P(Free | Spam) is the same as P(Spam | Free). Thinking that because 80% of spam contains "free", any email with "free" has an 80% chance of being spam.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> Always identify the reference denominator! P(Free | Spam) divides by the Spam count (16/20 = 80%). P(Spam | Free) divides by the total count of emails containing "free" (16/24 = 66.7%). They are fundamentally different quantities.</div>
        </div>
      </div>

      <!-- Mistake 2 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 02 &bull; Confusing Likelihood with Posterior Probability</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Treating the likelihood P(X | C) as the final prediction probability without multiplying by the class prior P(C).</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> Likelihood tells you how well the class hypothesis explains the evidence. Posterior tells you the probability of the class given the evidence. You MUST multiply likelihood by the prior P(C) to account for base rates.</div>
        </div>
      </div>

      <!-- Mistake 3 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 03 &bull; Forgetting Class Prior Probabilities P(C)</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Assuming all classes are equally likely (e.g., 50/50) in an imbalanced dataset where spam is only 5% of all traffic.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> Include the empirical or domain prior P(C). In rare disease screening (0.1% base rate), ignoring the prior results in massive false-positive rates.</div>
        </div>
      </div>

      <!-- Mistake 4 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 04 &bull; Multiplying Raw Probabilities Without Laplace Smoothing</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Calculating Naive Bayes likelihoods with raw counts, causing a single unseen word in training data to force the entire class score to 0.0.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> Always use Laplace smoothing (&alpha; = 1.0) or Lidstone smoothing (&alpha; &gt; 0) in categorical and multinomial models: P = (Count + &alpha;) / (Total + &alpha;&times;K).</div>
        </div>
      </div>

      <!-- Mistake 5 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 05 &bull; Applying the Wrong Denominator in Laplace Smoothing</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Adding |V| (vocabulary size) to a binary presence model, or adding K = 2 to a full multinomial text dictionary.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> In binary Bernoulli models, K = 2 (present/absent) &rarr; denominator is N<sub>C</sub> + 2&alpha;. In multinomial word-count models, denominator is the total word count in class C plus &alpha;&times;|V|, where |V| is the total vocabulary dimension.</div>
        </div>
      </div>

      <!-- Mistake 6 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 06 &bull; Using GaussianNB on Count Data or MultinomialNB on Negative Numbers</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Passing word counts into GaussianNB, or passing standardized negative features (from StandardScaler) into MultinomialNB.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> Match model to representation! Use MultinomialNB for non-negative word counts, BernoulliNB for binary {0, 1} flags, and GaussianNB for continuous real numbers. Never use StandardScaler with MultinomialNB.</div>
        </div>
      </div>

      <!-- Mistake 7 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 07 &bull; Confusing Word Presence with Word Frequency</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Expecting BernoulliNB to give higher weight to a word that appears 10 times compared to a word that appears once.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> BernoulliNB checks only binary presence (0 or 1). If repetition frequency matters (e.g., in long documents), use MultinomialNB with CountVectorizer or TfidfVectorizer.</div>
        </div>
      </div>

      <!-- Mistake 8 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 08 &bull; Fitting CountVectorizer on the Entire Dataset Before Train/Test Split</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Running <code>vectorizer.fit(all_data)</code> before calling <code>train_test_split</code>, leaking test set vocabulary into the training stage.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> Always use a scikit-learn <code>Pipeline([('vec', CountVectorizer()), ('nb', MultinomialNB())])</code>. The pipeline automatically fits the vocabulary strictly on training data and transforms test data safely.</div>
        </div>
      </div>

      <!-- Mistake 9 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 09 &bull; Tuning Hyperparameters Directly on the Test Set</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Testing multiple &alpha; values on the test set and reporting the best test accuracy.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> Use K-Fold Cross-Validation on the training split only to select the optimal &alpha;, reserving the held-out test set strictly for final unbiased evaluation.</div>
        </div>
      </div>

      <!-- Mistake 10 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 10 &bull; Assuming predict_proba Output is Perfectly Calibrated</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Believing that a predicted probability of 0.9999 means the model has a true 99.99% accuracy on that sample.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> Naive Bayes multiplies correlated feature evidence, causing probability estimates to be pushed aggressively toward 0 or 1. Use <code>CalibratedClassifierCV</code> if well-calibrated probabilities are required.</div>
        </div>
      </div>

      <!-- Mistake 11 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 11 &bull; Claiming Toy/Synthetic Results Prove Real-World Production Readiness</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Stating that 100% accuracy on a small synthetic dataset of 80 messages proves the filter can stop global spam.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> Always explicitly label educational datasets as synthetic. Production spam filters face adversarial misspelling ("F.R.E.E"), image-based spam, and massive conceptual drift.</div>
        </div>
      </div>

      <!-- Mistake 12 -->
      <div class="mistake-card">
        <div class="mistake-header">Mistake 12 &bull; Reporting Fabricated or Unexecuted Code Results</div>
        <div class="mistake-body">
          <div class="mistake-error"><strong>Error:</strong> Inventing performance metrics, confusion matrices, or probabilities without actually running the code.</div>
          <div class="mistake-fix"><strong>Correct Fix:</strong> Always run Python verification scripts and verify all reported numbers against actual execution outputs.</div>
        </div>
      </div>
    </section>

    <!-- Section 21 -->
    <section id="sec-21" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 21</span>
        <h2 class="section-title">Required Visualizations System &amp; Visual Guide</h2>
        <p class="section-subtitle">Complete gallery and architectural catalog of all 15 custom vector diagrams in Topic 14</p>
      </div>

      <p>This chapter includes 15 bespoke, XML-valid vector diagrams engineered to illustrate every theoretical, mathematical, and practical facet of Naive Bayes classification:</p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Figure #</th>
              <th>Diagram Title</th>
              <th>Section Located</th>
              <th>Educational Concept Illustrated</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Figure 14.1</strong></td>
              <td>Naive Bayes Classification Pipeline</td>
              <td>Section 01</td>
              <td>End-to-end pipeline from email to tokens, scores, and argmax prediction.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.2</strong></td>
              <td>Class Prior Probabilities Bar Chart</td>
              <td>Section 02</td>
              <td>Visual comparison of baseline class rates P(Spam) = 0.20 vs. P(Ham) = 0.80.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.3</strong></td>
              <td>Contingency Table &amp; Restricted Denominator</td>
              <td>Section 03</td>
              <td>2&times;2 joint count matrix illustrating conditioning universe restrictions.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.4</strong></td>
              <td>Bayes' Theorem Belief Update</td>
              <td>Section 04</td>
              <td>Prior belief (20%) updating to posterior belief (66.7%) upon observing "free".</td>
            </tr>
            <tr>
              <td><strong>Figure 14.5</strong></td>
              <td>Spam Vocabulary Feature Likelihoods</td>
              <td>Section 05</td>
              <td>Likelihood ratios for keywords "free", "offer", and "prize" across classes.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.6</strong></td>
              <td>Naive Independence Assumption Graph</td>
              <td>Section 07</td>
              <td>Interdependent feature network vs. simplified Naive Bayes star topology.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.7</strong></td>
              <td>Step-by-Step Score Comparison</td>
              <td>Section 08</td>
              <td>Unnormalized raw scores converted into normalized posterior probabilities.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.8</strong></td>
              <td>Zero-Frequency Product Collapse</td>
              <td>Section 09</td>
              <td>Illustration of how a single zero count annihilates all other evidence.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.9</strong></td>
              <td>Laplace Smoothing Before-and-After</td>
              <td>Section 10</td>
              <td>Additive pseudocount (&alpha; = 1.0) converting 0% into safe 1.22% probability.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.10</strong></td>
              <td>Naive Bayes Four Variants Visual</td>
              <td>Section 11</td>
              <td>Card grid comparing Gaussian, Multinomial, Bernoulli, and Categorical NB.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.11</strong></td>
              <td>Multinomial Document-Term Heatmap</td>
              <td>Section 12</td>
              <td>Non-negative integer term frequency matrix capturing repetition intensity.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.12</strong></td>
              <td>Bernoulli Binary Word-Presence Matrix</td>
              <td>Section 12</td>
              <td>Strict binary {0, 1} matrix modeling word presence versus absence.</td>
            </tr>
            <tr>
              <td><strong>Figure 14.13</strong></td>
              <td>Gaussian Class Bell Curves</td>
              <td>Section 12 &amp; 14</td>
              <td>Continuous normal distributions with learned means &mu; and variances &sigma;².</td>
            </tr>
            <tr>
              <td><strong>Figure 14.14</strong></td>
              <td>Spam Classifier Confusion Matrix</td>
              <td>Section 13</td>
              <td>Held-out test evaluation matrix (TN=9, FP=1, FN=0, TP=10).</td>
            </tr>
            <tr>
              <td><strong>Figure 14.15</strong></td>
              <td>Predicted Class Probabilities</td>
              <td>Section 15</td>
              <td>Breakdown of <code>predict_proba</code> outputs across test messages.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Section 22 -->
    <section id="sec-22" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 22</span>
        <h2 class="section-title">Quick Reference, Formulas &amp; Summary Matrix</h2>
        <p class="section-subtitle">A concise cheatsheet of essential mathematical equations and scikit-learn code patterns</p>
      </div>

      <h3>Mathematical Cheat Sheet</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Concept</th>
              <th>Formula</th>
              <th>Key Implementation Note</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Bayes' Theorem</strong></td>
              <td>P(C | X) = [ P(X | C) &times; P(C) ] / P(X)</td>
              <td>Inverts conditional probabilities; updates prior P(C) using likelihood P(X|C).</td>
            </tr>
            <tr>
              <td><strong>Naive Bayes Rule</strong></td>
              <td>P(C | X) &prop; P(C) &times; &prod;<sub>i=1</sub><sup>n</sup> P(x<sub>i</sub> | C)</td>
              <td>Multiplies individual conditional feature probabilities under independence assumption.</td>
            </tr>
            <tr>
              <td><strong>Log-Space Rule</strong></td>
              <td>log P(C | X) &prop; log P(C) + &sum;<sub>i=1</sub><sup>n</sup> log P(x<sub>i</sub> | C)</td>
              <td>Converts tiny probability multiplications into stable additions, preventing underflow.</td>
            </tr>
            <tr>
              <td><strong>Laplace Smoothing</strong></td>
              <td>P(x<sub>i</sub> | C) = [ Count + &alpha; ] / [ Total + &alpha;&times;K ]</td>
              <td>Adds pseudocount &alpha; = 1.0 to eliminate zero-frequency probabilities.</td>
            </tr>
            <tr>
              <td><strong>Gaussian Likelihood</strong></td>
              <td>P(x | C) = [ 1 / &radic;(2&pi;&sigma;²) ] &times; exp( &minus;(x&minus;&mu;)² / (2&sigma;²) )</td>
              <td>Evaluates continuous density using class mean &mu; and variance &sigma;².</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Scikit-Learn Implementation Quick Reference</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python 3 &bull; Naive Bayes API Quick Reference</span>
          <span class="code-lang-badge">Python</span>
        </div>
        <pre class="code-body"><code># Text Classification Pipeline (MultinomialNB)
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

text_pipe = Pipeline([
    ('vec', CountVectorizer(stop_words='english')),
    ('nb', MultinomialNB(alpha=1.0))
])
text_pipe.fit(X_train, y_train)
y_pred = text_pipe.predict(X_test)
y_prob = text_pipe.predict_proba(X_test)

# Continuous Numerical Classification (GaussianNB)
from sklearn.naive_bayes import GaussianNB

gauss_model = GaussianNB()
gauss_model.fit(X_num_train, y_train)
means = gauss_model.theta_     # Class means per feature
variances = gauss_model.var_   # Class variances per feature</code></pre>
      </div>
    </section>

    <!-- Section 23 -->
    <section id="sec-23" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 23</span>
        <h2 class="section-title">Interactive Knowledge Checks &amp; FAQs</h2>
        <p class="section-subtitle">Test and consolidate your understanding with interactive concept checks and detailed explanations</p>
      </div>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>1. Why is Naive Bayes called "Naive"?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>It is called "Naive" because it makes the simplifying assumption that all input features are conditionally independent of each other given the class label. In human language, words frequently correlate (e.g., "credit" and "card"), but assuming independence reduces exponential combinations down to simple 1D multiplications while retaining accurate classification boundaries.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>2. Why can we drop the denominator P(X) when predicting the class?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>For any given input example X, P(X) is an identical constant across all candidate classes. Since dividing all scores by the same positive number scales them proportionally without changing their relative ranking, the class that maximizes the numerator also maximizes the full posterior probability.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>3. What is the Zero-Frequency Problem, and how does Laplace smoothing resolve it?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>If a feature never appears in a particular class in the training data, its unsmoothed likelihood is 0.0. Multiplying this zero into the Naive Bayes product chain annihilates all other evidence, forcing the entire class score to 0. Laplace smoothing adds a small pseudocount &alpha; (typically &alpha; = 1.0) to every feature count, guaranteeing that every probability remains strictly positive.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>4. What is the fundamental difference between MultinomialNB and BernoulliNB?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>MultinomialNB uses integer frequency counts, so repeating a word multiple times increases its evidence weight. BernoulliNB uses strictly binary indicators (0 or 1), focusing solely on whether a word is present or absent, and explicitly penalizes classes for missing expected vocabulary tokens.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>5. When should I choose GaussianNB over MultinomialNB?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>Choose GaussianNB when your features are continuous real-valued numbers (e.g., temperature, blood pressure, sensor voltage) that approximately follow a normal distribution. Choose MultinomialNB when features represent non-negative discrete counts, such as word frequencies in text classification.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>6. Why do Naive Bayes implementations compute log-probabilities instead of raw probabilities?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>Multiplying hundreds of fractional probabilities together results in floating-point underflow (numbers smaller than 10<sup>&minus;308</sup> collapsing to zero). Taking logarithms transforms multiplications into additions of negative numbers, which are numerically stable and computationally fast.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>7. Are the output values from predict_proba well-calibrated true probabilities?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>No. Because features often correlate in reality, multiplying their probabilities violates independence and pushes posterior estimates aggressively toward 0.0 or 1.0. While the predicted class ranking is usually correct, the raw probability values should not be interpreted as exact statistical confidence unless calibrated using isotonic regression or Platt scaling.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>8. Why is a False Positive considered more harmful than a False Negative in spam filtering?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>A False Positive occurs when a legitimate email (e.g., a job offer, invoice, or urgent medical alert) is mistakenly blocked or routed to the spam folder, causing severe disruption. A False Negative merely means a junk email appears in the inbox, which the user can quickly delete. Spam filters therefore prioritize high Precision over Recall.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>9. Why should you never use StandardScaler with MultinomialNB?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>StandardScaler centers features to zero mean, producing negative z-scores. MultinomialNB models multinomial count distributions and strictly requires non-negative values. Passing negative values to MultinomialNB will cause an immediate ValueError.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>10. How does Naive Bayes handle missing feature values during inference?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>Because features are assumed to be conditionally independent, any missing feature can simply be omitted from the likelihood product calculation without invalidating the remaining terms. The model calculates the posterior using whatever features are present.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>11. What happens if you fit a CountVectorizer on the entire dataset before train_test_split?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>This introduces data leakage: the vocabulary from the test set is learned by the vectorizer during the training phase, giving the model unrealistic prior knowledge of test vocabulary and producing falsely optimistic evaluation metrics.</p>
        </div>
      </details>

      <details class="accordion-item">
        <summary class="accordion-summary">
          <span>12. How does tuning the alpha hyperparameter influence model variance and bias?</span>
          <span style="color:#7C3AED;font-weight:700;">+</span>
        </summary>
        <div class="accordion-content">
          <p>Setting &alpha; near zero reduces smoothing, making the model fit training counts tightly (higher variance, risk of zero probabilities). Setting &alpha; very large adds heavy smoothing, pulling all probabilities toward uniform distribution (higher bias, softer predictions). &alpha; = 1.0 typically provides the optimal balance.</p>
        </div>
      </details>
    </section>

    <!-- Footer -->
    <footer class="notes-footer">
      <p>CodeVerse Machine Learning &bull; Topic 14: Naive Bayes Classifiers &bull; Light Mode Only</p>
      <p style="margin-top: 6px; font-size: 12px; color: #94A3B8;">Verified Scikit-Learn 1.9.1 Implementation &bull; 15 Custom Vector Visualizations &bull; Leak-Free Pipelines</p>
    </footer>
  </div>
"""
