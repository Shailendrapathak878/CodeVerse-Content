"""
Module: topic10_part1.py
Contains Hero Header, Table of Contents, and Sections 1 to 5 for Topic 10: Logistic Regression.
"""

from scratch.topic10_svgs import (
    SVG_LOGREG_HERO,
    SVG_LINEAR_VS_SIGMOID,
    SVG_SIGMOID_CURVE
)

PART1_HTML = f"""
    <!-- HERO HEADER -->
    <header class="hero-card">
      <div class="hero-tag">&#9874; Supervised Machine Learning &bull; Topic 10</div>
      <h1 class="hero-title">Logistic Regression: Complete Beginner Guide</h1>
      <p class="hero-subtitle">
        Master binary classification from zero. Learn why classification differs from continuous regression, how the elegant S-shaped sigmoid function compresses unbounded linear scores into true probabilities, and how to calibrate decision boundaries, evaluate confusion matrices, and build leak-free scikit-learn classification pipelines.
      </p>
      <div class="meta-bar">
        <span class="meta-pill">&#128218; 21 Comprehensive Sections</span>
        <span class="meta-pill">&#9889; 14 Interactive Vector Diagrams</span>
        <span class="meta-pill">&#128013; Verified Scikit-Learn Pipeline</span>
        <span class="meta-pill">&#9878; Strict Light Mode Only</span>
        <span class="meta-pill">&#127919; 100% Mobile &amp; Desktop Tested</span>
      </div>
    </header>

    <!-- ARCHITECTURE HERO SVG -->
    <div class="svg-card">
      <div class="svg-container">
        {SVG_LOGREG_HERO}
      </div>
      <div class="svg-caption">
        <strong>Figure 10.1: The Four-Stage Logistic Regression Engine.</strong> Raw input features <code>X</code> are linearly weighted into score <code>z</code>, mapped into bounded probability <code>p &isin; (0, 1)</code> via the sigmoid activation function <code>&sigma;(z)</code>, and converted to discrete class labels <code>&#375; &isin; {{0, 1}}</code> through decision threshold <code>&tau;</code>.
      </div>
      <div class="svg-takeaway">
        &#10004; Core takeaway: Logistic regression does not predict discrete labels directly; it calculates a continuous, calibrated class probability and applies a threshold rule.
      </div>
    </div>

    <!-- TABLE OF CONTENTS -->
    <nav class="toc-card" aria-label="Table of Contents">
      <div class="toc-title">
        <span>&#128203; Chapter Roadmap &bull; Table of Contents</span>
      </div>
      <div class="toc-grid">
        <a href="#sec-01" class="toc-link"><span class="toc-num">01</span> Introduction to Classification</a>
        <a href="#sec-02" class="toc-link"><span class="toc-num">02</span> What Is Logistic Regression?</a>
        <a href="#sec-03" class="toc-link"><span class="toc-num">03</span> Why Not Linear Regression?</a>
        <a href="#sec-04" class="toc-link"><span class="toc-num">04</span> The Sigmoid Function</a>
        <a href="#sec-05" class="toc-link"><span class="toc-num">05</span> The Logistic Regression Equation</a>
        <a href="#sec-06" class="toc-link"><span class="toc-num">06</span> Odds, Log-Odds &amp; Logits</a>
        <a href="#sec-07" class="toc-link"><span class="toc-num">07</span> Decision Thresholds (&tau;)</a>
        <a href="#sec-08" class="toc-link"><span class="toc-num">08</span> The Decision Boundary</a>
        <a href="#sec-09" class="toc-link"><span class="toc-num">09</span> How Logistic Regression Learns (MLE)</a>
        <a href="#sec-10" class="toc-link"><span class="toc-num">10</span> Log Loss &amp; Binary Cross-Entropy</a>
        <a href="#sec-11" class="toc-link"><span class="toc-num">11</span> Simple &amp; Multiple Logistic Regression</a>
        <a href="#sec-12" class="toc-link"><span class="toc-num">12</span> Regularization &amp; Overfitting (C Parameter)</a>
        <a href="#sec-13" class="toc-link"><span class="toc-num">13</span> Classification Metrics &amp; Confusion Matrix</a>
        <a href="#sec-14" class="toc-link"><span class="toc-num">14</span> ROC Curve &amp; AUC Ranking</a>
        <a href="#sec-15" class="toc-link"><span class="toc-num">15</span> Class Imbalance &amp; Threshold Selection</a>
        <a href="#sec-16" class="toc-link"><span class="toc-num">16</span> Probability Calibration &amp; Interpretation</a>
        <a href="#sec-17" class="toc-link"><span class="toc-num">17</span> Complete Python Practical Lab</a>
        <a href="#sec-18" class="toc-link"><span class="toc-num">18</span> Real-Life Case Studies</a>
        <a href="#sec-19" class="toc-link"><span class="toc-num">19</span> Key Visualizations &amp; Graphs</a>
        <a href="#sec-20" class="toc-link"><span class="toc-num">20</span> 18 Common Beginner Mistakes</a>
        <a href="#sec-21" class="toc-link"><span class="toc-num">21</span> Glossary, Checklist &amp; Revision</a>
      </div>
    </nav>

    <!-- SECTION 01: INTRODUCTION TO CLASSIFICATION -->
    <section id="sec-01" class="section-card">
      <span class="section-badge">Section 01</span>
      <h2 class="section-title">Introduction to Classification</h2>
      <p class="section-lead">
        In machine learning, supervised learning tasks split into two primary branches: predicting continuous quantities (regression) and categorizing observations into distinct buckets (classification).
      </p>

      <p>
        Every day, software systems make millions of instantaneous decisions:
      </p>
      <ul>
        <li><strong>Email spam detection:</strong> Does an incoming email belong in your inbox (<em>Not Spam</em>) or should it be diverted to junk (<em>Spam</em>)?</li>
        <li><strong>Financial fraud monitoring:</strong> Is a credit card swipe at 3:00 AM in a foreign city legitimate (<em>Normal</em>) or fraudulent (<em>Fraud</em>)?</li>
        <li><strong>Healthcare screening:</strong> Does an emergency room triage scan indicate a positive pathological abnormality (<em>Positive</em>) or a clear, benign scan (<em>Negative</em>)?</li>
        <li><strong>Customer churn prevention:</strong> Will an active SaaS subscriber renew their contract next month (<em>Retained</em>) or cancel their account (<em>Churn</em>)?</li>
      </ul>

      <div class="callout card-concept">
        <div class="callout-title">&#128161; Regression vs. Classification: Fundamental Contrast</div>
        <p>
          In <strong>Regression</strong> (Topic 9), the target <code>y</code> is a continuous numerical measurement that can take infinitely many values on a real number scale (such as predicting a house selling price of $354,250.00, or a temperature of 24.6 &deg;C).
        </p>
        <p>
          In <strong>Classification</strong>, the target <code>y</code> is a categorical qualitative label. The model chooses between mutually exclusive categories or assigns a probability to each category.
        </p>
      </div>

      <h3 class="sub-title">Comparison Table: Regression vs Classification Tasks</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Task Domain</th>
              <th>Input Features (X)</th>
              <th>Target Type</th>
              <th>Target Output (y)</th>
              <th>Learning Task</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Real Estate</strong></td>
              <td>Square footage, bedrooms, postal code</td>
              <td>Continuous Number</td>
              <td>$425,000.00 USD</td>
              <td><span class="badge" style="background:#EEF2FF;color:#4338CA;">Regression</span></td>
            </tr>
            <tr>
              <td><strong>Email Security</strong></td>
              <td>Keyword frequencies, sender reputation, links</td>
              <td>Categorical Label</td>
              <td>Spam vs. Not Spam</td>
              <td><span class="badge" style="background:#F0FDF4;color:#166534;">Classification</span></td>
            </tr>
            <tr>
              <td><strong>Banking Fraud</strong></td>
              <td>Transaction amount, merchant category, time</td>
              <td>Categorical Label</td>
              <td>Legitimate vs. Fraudulent</td>
              <td><span class="badge" style="background:#F0FDF4;color:#166534;">Classification</span></td>
            </tr>
            <tr>
              <td><strong>Subscription SaaS</strong></td>
              <td>Login frequency, open support tickets, days active</td>
              <td>Categorical Label</td>
              <td>Churn vs. Retained</td>
              <td><span class="badge" style="background:#F0FDF4;color:#166534;">Classification</span></td>
            </tr>
            <tr>
              <td><strong>Automotive</strong></td>
              <td>Engine displacement, vehicle weight, horsepower</td>
              <td>Continuous Number</td>
              <td>32.4 Miles Per Gallon</td>
              <td><span class="badge" style="background:#EEF2FF;color:#4338CA;">Regression</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">What Is Binary Classification?</h3>
      <p>
        When a classification task involves exactly <strong>two possible outcomes</strong>, it is called <strong>binary classification</strong>. By convention, machine learning engineers encode these two classes numerically as:
      </p>
      <ul>
        <li><strong>Class 0 (Negative Class):</strong> The baseline, standard, or unexceptional state (e.g., <em>Not Spam</em>, <em>Legitimate Transaction</em>, <em>Healthy Scan</em>, <em>Retained Customer</em>).</li>
        <li><strong>Class 1 (Positive Class):</strong> The event, alert, or anomaly of interest (e.g., <em>Spam</em>, <em>Fraudulent Charge</em>, <em>Condition Detected</em>, <em>Customer Churned</em>).</li>
      </ul>

      <div class="callout card-warning">
        <div class="callout-title">&#9888; Critical Beginner Pitfall: The Meaning of Numbers 0 and 1</div>
        <p>
          Do not confuse binary class labels <code>0</code> and <code>1</code> with mathematical quantities! A spam email is not &ldquo;one unit greater&rdquo; than a legitimate email. 
        </p>
        <p>
          The numerals <code>0</code> and <code>1</code> are purely discrete category identifiers. They represent qualitative states, not continuous points on a physical number line.
        </p>
      </div>
    </section>

    <!-- SECTION 02: WHAT IS LOGISTIC REGRESSION? -->
    <section id="sec-02" class="section-card">
      <span class="section-badge">Section 02</span>
      <h2 class="section-title">What Is Logistic Regression?</h2>
      <p class="section-lead">
        Despite having the word &ldquo;Regression&rdquo; in its historic name, Logistic Regression is the world&rsquo;s most foundational and widely deployed supervised algorithm for <strong>Classification</strong>.
      </p>

      <p>
        Why is it called &ldquo;regression&rdquo; if it performs classification? The answer lies in its internal mathematical architecture:
      </p>
      <div class="callout card-definition">
        <div class="callout-title">&#128214; The Historic Paradox Explained</div>
        <p>
          Internally, Logistic Regression computes a standard linear regression score:
          <br>
          <code>z = &beta;<sub>0</sub> + &beta;<sub>1</sub>x<sub>1</sub> + &beta;<sub>2</sub>x<sub>2</sub> + ... + &beta;<sub>p</sub>x<sub>p</sub></code>
        </p>
        <p>
          However, instead of outputting this linear score directly as a final continuous quantity, it feeds <code>z</code> into a non-linear mathematical filter called the <strong>Sigmoid Activation Function</strong>. The sigmoid squashes the unbounded score into a strict probability between 0.0 and 1.0. A decision threshold then assigns the final class.
        </p>
      </div>

      <h3 class="sub-title">Foundational Vocabulary: Terms Defined Before Use</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Term</th>
              <th>Plain-English Definition</th>
              <th>Concrete Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Feature (X)</strong></td>
              <td>A measurable property or input attribute used to make a prediction.</td>
              <td>Weekly study hours: <code>x = 18.5</code></td>
            </tr>
            <tr>
              <td><strong>Target / Label (y)</strong></td>
              <td>The true known ground-truth outcome in the dataset.</td>
              <td>Exam passed: <code>y = 1</code>; Exam failed: <code>y = 0</code></td>
            </tr>
            <tr>
              <td><strong>Linear Score (z)</strong></td>
              <td>The raw weighted sum of features plus an intercept bias. Unbounded: (-&infin;, +&infin;).</td>
              <td><code>z = -2.5 + (0.35 &times; 18.5) = +3.975</code></td>
            </tr>
            <tr>
              <td><strong>Class Probability (p)</strong></td>
              <td>The model&rsquo;s estimated likelihood that the observation belongs to Class 1. Bounded: (0, 1).</td>
              <td><code>p = P(y = 1 | x) = 0.9816 (98.16%)</code></td>
            </tr>
            <tr>
              <td><strong>Decision Threshold (&tau;)</strong></td>
              <td>The cutoff probability separating Class 0 from Class 1. Default is 0.50.</td>
              <td>If <code>p &ge; 0.50</code>, predict <code>&#375; = 1</code></td>
            </tr>
            <tr>
              <td><strong>Predicted Class (&#375;)</strong></td>
              <td>The final categorical assignment made after applying the threshold.</td>
              <td><code>&#375; = 1 (Pass)</code></td>
            </tr>
            <tr>
              <td><strong>Model Coefficient (&beta;)</strong></td>
              <td>The learned slope reflecting how much the log-odds change per unit increase in that feature.</td>
              <td><code>&beta;<sub>study</sub> = +0.35</code> (more hours increase pass odds)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">A Relatable Concrete Example: Student Exam Pass/Fail</h3>
      <p>
        Suppose an academic department trains a Logistic Regression model to predict whether university students will pass a rigorous mathematics exam based on two features: weekly study hours and attendance percentage.
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Student ID</th>
              <th>Study Hours</th>
              <th>Attendance</th>
              <th>Calculated Score (z)</th>
              <th>Estimated Probability (p)</th>
              <th>Threshold (&tau;=0.50)</th>
              <th>Predicted Class (&#375;)</th>
              <th>Actual Label (y)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>STU-001</strong></td>
              <td>4.5 hrs</td>
              <td>52.0%</td>
              <td>-2.14</td>
              <td><strong>0.1053 (10.5%)</strong></td>
              <td>p &lt; 0.50</td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Fail)</span></td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Fail)</span> &#10004;</td>
            </tr>
            <tr>
              <td><strong>STU-002</strong></td>
              <td>12.0 hrs</td>
              <td>78.5%</td>
              <td>+0.45</td>
              <td><strong>0.6106 (61.1%)</strong></td>
              <td>p &ge; 0.50</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pass)</span></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pass)</span> &#10004;</td>
            </tr>
            <tr>
              <td><strong>STU-003</strong></td>
              <td>22.5 hrs</td>
              <td>95.0%</td>
              <td>+3.82</td>
              <td><strong>0.9786 (97.9%)</strong></td>
              <td>p &ge; 0.50</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pass)</span></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pass)</span> &#10004;</td>
            </tr>
            <tr>
              <td><strong>STU-004</strong></td>
              <td>8.0 hrs</td>
              <td>68.0%</td>
              <td>-0.08</td>
              <td><strong>0.4800 (48.0%)</strong></td>
              <td>p &lt; 0.50</td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Fail)</span></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pass)</span> &#10008; (FN)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>
        Notice student <code>STU-004</code>: their estimated probability was 48.0%, which is just below the 0.50 cutoff. The model predicted Fail, but the student actually passed. This reveals a vital machine learning principle:
      </p>
      <div class="callout card-amber">
        <div class="callout-title">&#128308; Probabilities Are Model Estimates, Not Guarantees</div>
        <p>
          A predicted probability of <code>p = 0.85</code> does not mean the outcome is 100% guaranteed. It means that under the model&rsquo;s learned parameters, similar students have an estimated 85% statistical likelihood of passing. In the real world, human performance and health outcomes always retain stochastic variability.
        </p>
      </div>
    </section>

    <!-- SECTION 03: WHY NOT LINEAR REGRESSION? -->
    <section id="sec-03" class="section-card">
      <span class="section-badge">Section 03</span>
      <h2 class="section-title">Why Not Use Ordinary Linear Regression for Classification?</h2>
      <p class="section-lead">
        When beginners first encounter binary classification, a natural thought emerges: <em>&ldquo;Since labels are 0 and 1, why not just fit an Ordinary Least Squares (OLS) line through the points and round to the nearest whole number?&rdquo;</em>
      </p>

      <p>
        While mathematically possible to fit an OLS line, doing so introduces severe structural flaws:
      </p>

      <div class="step-list">
        <div class="step-card">
          <div class="step-number">1</div>
          <div class="step-body">
            <h4>Out-of-Bounds Predictions: Probabilities Less Than 0 or Greater Than 1</h4>
            <p>
              An ordinary linear regression equation <code>&#375; = &beta;<sub>0</sub> + &beta;<sub>1</sub>x</code> is a straight, unbounded line. For small or large feature values, the line extends to -&infin; and +&infin;. A model that predicts a student has a <code>-35%</code> or <code>+140%</code> probability of passing violates fundamental probability axioms.
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">2</div>
          <div class="step-body">
            <h4>Extreme Vulnerability to Outliers in Feature Space</h4>
            <p>
              In linear regression, OLS minimizes squared residual errors. If you introduce a student who studied 50 hours and easily passed (a valid extreme positive point), OLS tilts the entire line to minimize the squared error on that far point. This slope tilt changes predictions for ordinary students in the middle, pushing previously passing students into the failing category!
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">3</div>
          <div class="step-body">
            <h4>Severe Heteroscedasticity (Non-Constant Variance)</h4>
            <p>
              In linear regression, residuals are assumed to have constant variance (&sigma;<sup>2</sup>). In binary outcomes, the variance is <code>Var(y | x) = p(x)(1 - p(x))</code>. The variance is near zero when <code>p &approx; 0</code> or <code>p &approx; 1</code>, and peaks at 0.25 when <code>p = 0.5</code>. Fitting a standard linear regression model directly violates Gauss-Markov assumptions, rendering standard OLS hypothesis testing and p-values invalid.
            </p>
          </div>
        </div>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_LINEAR_VS_SIGMOID}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.2: Straight Linear Fit vs. S-Curve Sigmoid Fit.</strong> The linear regression line (left) produces nonsense values below 0.0 and above 1.0. In contrast, Logistic Regression (right) smoothly squashes all predictions into the open interval (0, 1).
        </div>
        <div class="svg-takeaway">
          &#10004; Key takeaway: Logistic regression does not force a straight line through binary labels; it models the underlying probability using a bounded non-linear activation curve.
        </div>
      </div>
    </section>

    <!-- SECTION 04: UNDERSTANDING THE SIGMOID FUNCTION -->
    <section id="sec-04" class="section-card">
      <span class="section-badge">Section 04</span>
      <h2 class="section-title">Understanding the Sigmoid Function</h2>
      <p class="section-lead">
        The mathematical heartbeat of Logistic Regression is the <strong>Standard Logistic Function</strong>, universally known in machine learning as the <strong>Sigmoid Function</strong>.
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; The Standard Sigmoid Activation Formula</div>
        <div class="formula-math">
          &sigma;(z) = 1 / (1 + e<sup>-z</sup>)
        </div>
        <div class="formula-legend">
          <div class="formula-legend-item">
            <code>z</code>: The input linear score (weighted sum &beta;<sub>0</sub> + &sum; &beta;<sub>j</sub>x<sub>j</sub>). Domain: (-&infin;, +&infin;).
          </div>
          <div class="formula-legend-item">
            <code>e</code>: Euler&rsquo;s natural mathematical constant (&approx; 2.7182818).
          </div>
          <div class="formula-legend-item">
            <code>e<sup>-z</sup></code>: Exponential decay term (1 / e<sup>z</sup>).
          </div>
          <div class="formula-legend-item">
            <code>&sigma;(z)</code>: Sigmoid output probability. Range: strictly (0.0, 1.0).
          </div>
        </div>
      </div>

      <h3 class="sub-title">Step-by-Step Numerical Calculations (Python Verified)</h3>
      <p>
        Let us calculate the exact output of the sigmoid function for five critical benchmark values of linear score <code>z</code>:
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Linear Score (z)</th>
              <th>e<sup>-z</sup> Calculation</th>
              <th>Denominator: 1 + e<sup>-z</sup></th>
              <th>Sigmoid &sigma;(z) = 1 / (1 + e<sup>-z</sup>)</th>
              <th>Interpretation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>z = 0.0</strong></td>
              <td>e<sup>-0.0</sup> = 1.0000</td>
              <td>1 + 1.0000 = 2.0000</td>
              <td>1 / 2.0000 = <strong>0.5000 (50.0%)</strong></td>
              <td>Perfect 50/50 uncertainty (boundary center)</td>
            </tr>
            <tr>
              <td><strong>z = +1.8</strong></td>
              <td>e<sup>-1.8</sup> = 0.1653</td>
              <td>1 + 0.1653 = 1.1653</td>
              <td>1 / 1.1653 = <strong>0.8581 (85.81%)</strong></td>
              <td>Moderate positive confidence</td>
            </tr>
            <tr>
              <td><strong>z = -1.8</strong></td>
              <td>e<sup>+1.8</sup> = 6.0496</td>
              <td>1 + 6.0496 = 7.0496</td>
              <td>1 / 7.0496 = <strong>0.1419 (14.19%)</strong></td>
              <td>Moderate negative confidence</td>
            </tr>
            <tr>
              <td><strong>z = +5.0</strong></td>
              <td>e<sup>-5.0</sup> = 0.00674</td>
              <td>1 + 0.00674 = 1.00674</td>
              <td>1 / 1.00674 = <strong>0.9933 (99.33%)</strong></td>
              <td>High positive confidence (near upper asymptote)</td>
            </tr>
            <tr>
              <td><strong>z = -5.0</strong></td>
              <td>e<sup>+5.0</sup> = 148.413</td>
              <td>1 + 148.413 = 149.413</td>
              <td>1 / 149.413 = <strong>0.0067 (0.67%)</strong></td>
              <td>High negative confidence (near lower asymptote)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_SIGMOID_CURVE}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.3: The Sigmoid Curve Geometry and Asymptotes.</strong> The function produces an S-shaped curve centered at (0, 0.5). Notice how values of <code>z = +1.8</code> and <code>z = -1.8</code> sum exactly to 1.0.
        </div>
        <div class="svg-takeaway">
          &#10004; Mathematical Elegance: <code>&sigma;(z) + &sigma;(-z) = 1.0</code> for any real number <code>z</code>.
        </div>
      </div>

      <h3 class="sub-title">Three Architectural Superpowers of the Sigmoid</h3>
      <ol>
        <li>
          <strong>Strict Bounded Range (0, 1):</strong> No matter how enormous a positive score becomes (e.g., <code>z = +100</code>), <code>e<sup>-100</sup> &approx; 0</code>, so <code>&sigma;(100) &approx; 0.999999... &lt; 1.0</code>. Similarly, if <code>z = -100</code>, <code>&sigma;(-100) &approx; 0.00000... &gt; 0.0</code>. Probabilities can never cross 0 or 1.
        </li>
        <li>
          <strong>Maximum Sensitivity in the Center:</strong> The first derivative of the sigmoid is <code>d&sigma;/dz = &sigma;(z) &times; (1 - &sigma;(z))</code>. At <code>z = 0</code>, the slope is <code>0.5 &times; (1 - 0.5) = 0.25</code> (its steepest rate of change). Small changes in input features create decisive shifts when the model is uncertain, but taper off safely when the model is already confident.
        </li>
        <li>
          <strong>Saturated Plateau at the Extremes:</strong> As <code>|z|</code> grows past 4, the curve flattens horizontally into asymptotes. This prevents extreme outliers from exerting disproportionate leverage on the decision boundary.
        </li>
      </ol>
    </section>

    <!-- SECTION 05: THE LOGISTIC REGRESSION EQUATION -->
    <section id="sec-05" class="section-card">
      <span class="section-badge">Section 05</span>
      <h2 class="section-title">The Logistic Regression Equation</h2>
      <p class="section-lead">
        Now that we understand both the linear score and the sigmoid curve, we assemble the complete mathematical formulation for binary logistic regression.
      </p>

      <h3 class="sub-title">1. Single-Feature Formulation (Univariate)</h3>
      <p>
        When making a prediction based on one input feature <code>x</code>:
      </p>
      <div class="formula-card">
        <div class="formula-title">&#128290; Single-Feature Logistic Model</div>
        <div class="formula-math">
          P(y = 1 | x) = &sigma;(&beta;<sub>0</sub> + &beta;<sub>1</sub>x) = 1 / (1 + e<sup>-(&beta;<sub>0</sub> + &beta;<sub>1</sub>x)</sup>)
        </div>
        <div class="formula-legend">
          <div class="formula-legend-item"><code>x</code>: Input feature value (e.g., study hours).</div>
          <div class="formula-legend-item"><code>&beta;<sub>0</sub></code>: Intercept (bias) term. Determines baseline probability when x = 0.</div>
          <div class="formula-legend-item"><code>&beta;<sub>1</sub></code>: Slope coefficient. Controls steepness and direction of the S-curve.</div>
        </div>
      </div>

      <h3 class="sub-title">2. Multiple-Feature Formulation (Multivariate)</h3>
      <p>
        In realistic machine learning applications, we predict outcomes using <code>p</code> input features <code>x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>p</sub></code>:
      </p>
      <div class="formula-card">
        <div class="formula-title">&#128290; Multiple Logistic Regression Model</div>
        <div class="formula-math">
          z = &beta;<sub>0</sub> + &beta;<sub>1</sub>x<sub>1</sub> + &beta;<sub>2</sub>x<sub>2</sub> + ... + &beta;<sub>p</sub>x<sub>p</sub> = &beta;<sub>0</sub> + &sum;<sub>j=1</sub><sup>p</sup> &beta;<sub>j</sub>x<sub>j</sub>
        </div>
        <div class="formula-math" style="margin-top:0.75rem;">
          P(y = 1 | x) = &sigma;(z) = 1 / (1 + e<sup>-z</sup>)
        </div>
      </div>

      <h3 class="sub-title">Complete Worked Arithmetic Walkthrough</h3>
      <p>
        Suppose an ad-tech company trains a multiple logistic regression model to predict whether a website visitor will click on a banner advertisement (<code>y = 1</code>) based on two features:
      </p>
      <ul>
        <li><code>x<sub>1</sub></code>: Time spent on website (minutes).</li>
        <li><code>x<sub>2</sub></code>: Number of previous purchases.</li>
      </ul>
      <p>
        The learned model parameters are:
        <br>
        <code>&beta;<sub>0</sub> = -3.20</code> (Intercept), <code>&beta;<sub>1</sub> = +0.45</code>, <code>&beta;<sub>2</sub> = +0.60</code>.
      </p>
      <p>
        Now consider a visitor who spent <strong>6 minutes</strong> on the site (<code>x<sub>1</sub> = 6.0</code>) and has made <strong>2 previous purchases</strong> (<code>x<sub>2</sub> = 2.0</code>). Let us compute the prediction step-by-step:
      </p>

      <div class="step-list">
        <div class="step-card">
          <div class="step-number">1</div>
          <div class="step-body">
            <h4>Calculate the Linear Score (z)</h4>
            <p>
              <code>z = &beta;<sub>0</sub> + &beta;<sub>1</sub>x<sub>1</sub> + &beta;<sub>2</sub>x<sub>2</sub></code><br>
              <code>z = -3.20 + (0.45 &times; 6.0) + (0.60 &times; 2.0)</code><br>
              <code>z = -3.20 + 2.70 + 1.20 = <strong>+0.70</strong></code>
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">2</div>
          <div class="step-body">
            <h4>Calculate the Exponential Term</h4>
            <p>
              <code>e<sup>-z</sup> = e<sup>-0.70</sup> &approx; <strong>0.496585</strong></code>
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">3</div>
          <div class="step-body">
            <h4>Compute the Sigmoid Probability</h4>
            <p>
              <code>P(Click = 1 | x) = 1 / (1 + 0.496585) = 1 / 1.496585 &approx; <strong>0.6682 (66.82%)</strong></code>
            </p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">4</div>
          <div class="step-body">
            <h4>Apply Decision Threshold and Classify</h4>
            <p>
              Using standard threshold <code>&tau; = 0.50</code>:<br>
              Since <code>0.6682 &ge; 0.50</code>, the model outputs: <strong>Predicted Class &#375; = 1 (Visitor Will Click)</strong>.
            </p>
          </div>
        </div>
      </div>

      <div class="code-block">
        <div class="code-header">
          <span class="code-title">&#128013; python_verification.py &bull; Manual Arithmetic Check</span>
          <span class="code-lang">Python</span>
        </div>
        <pre><code>import numpy as np

# 1. Model parameters
beta_0 = -3.20
beta_1 = 0.45
beta_2 = 0.60

# 2. Input features
x1 = 6.0  # Time on site (minutes)
x2 = 2.0  # Prior purchases

# 3. Calculate linear score z
z = beta_0 + (beta_1 * x1) + (beta_2 * x2)
print(f"Linear score z: {{z:.4f}}")  # Expected: +0.7000

# 4. Apply Sigmoid function
prob = 1.0 / (1.0 + np.exp(-z))
print(f"Estimated Click Probability: {{prob:.4%}}")  # Expected: 66.82%

# 5. Apply threshold tau = 0.50
prediction = 1 if prob >= 0.50 else 0
print(f"Predicted Class: {{prediction}} (Will Click)")

assert np.isclose(z, 0.7000)
assert np.isclose(prob, 0.6682, atol=0.001)
print("[PASS] Manual arithmetic matches NumPy calculation exactly!")</code></pre>
      </div>
    </section>
"""
