"""
Module: topic10_part2.py
Contains Sections 6 to 10 for Topic 10: Logistic Regression.
"""

from scratch.topic10_svgs import (
    SVG_ODDS_PROB_MAPPING,
    SVG_THRESHOLD_VARIATION,
    SVG_DECISION_BOUNDARY_1D_2D,
    SVG_LOG_LOSS_CURVES
)

PART2_HTML = f"""
    <!-- SECTION 06: ODDS, LOG-ODDS AND LOGITS -->
    <section id="sec-06" class="section-card">
      <span class="section-badge">Section 06</span>
      <h2 class="section-title">Understanding Odds, Log-Odds and Logits</h2>
      <p class="section-lead">
        To truly understand how Logistic Regression connects linear algebra to probability, we must explore the mathematical bridge that links probabilities, odds, and log-odds (logits).
      </p>

      <h3 class="sub-title">1. What Are Odds? (Probability vs. Odds)</h3>
      <p>
        In everyday conversation, people often treat the words &ldquo;probability&rdquo; and &ldquo;odds&rdquo; as interchangeable synonyms. In statistics and machine learning, they are strictly distinct mathematical quantities:
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; Probability vs. Odds Formulation</div>
        <div class="formula-math">
          Probability (p) = Successes / Total Trials &isin; [0, 1]
        </div>
        <div class="formula-math" style="margin-top:0.75rem;">
          Odds = p / (1 - p) = Successes / Failures &isin; [0, +&infin;)
        </div>
      </div>

      <p>
        Consider a student with an <strong>80% probability</strong> of passing an exam (<code>p = 0.80</code>):
      </p>
      <ul>
        <li><strong>Probability:</strong> <code>p = 0.80</code> (out of 10 attempts, 8 are passes and 2 are fails).</li>
        <li><strong>Odds:</strong> <code>Odds = 0.80 / (1 - 0.80) = 0.80 / 0.20 = 4.0</code> (or &ldquo;4 to 1&rdquo; in favor of passing).</li>
      </ul>

      <h3 class="sub-title">2. What Are Log-Odds (The Logit Function)?</h3>
      <p>
        Notice that Odds are bounded on the left at 0.0 (an impossible event has <code>Odds = 0.0</code>), but stretch infinitely to the right towards +&infin;. This asymmetry makes odds awkward for standard linear modeling.
      </p>
      <p>
        To solve this asymmetry, we take the <strong>natural logarithm</strong> (ln) of the odds. This transformation is called the <strong>Logit Function</strong>:
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; The Logit (Log-Odds) Equation</div>
        <div class="formula-math">
          logit(p) = ln(Odds) = ln(p / (1 - p)) &isin; (-&infin;, +&infin;)
        </div>
      </div>

      <p>
        Taking the log of odds maps the probability range <code>(0, 1)</code> onto the entire continuous real number line from <code>-&infin;</code> to <code>+&infin;</code>!
      </p>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_ODDS_PROB_MAPPING}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.4: The Three Representations of Likelihood.</strong> Probability <code>p</code> is bounded between 0 and 1; Odds range from 0 to +&infin;; Log-Odds (logit) are symmetric across the real line (-&infin;, +&infin;).
        </div>
        <div class="svg-takeaway">
          &#10004; The Core Insight: Logistic regression performs standard linear regression directly on the <strong>Log-Odds</strong> of the target event.
        </div>
      </div>

      <h3 class="sub-title">3. Interpreting Model Coefficients via the Odds Ratio (OR)</h3>
      <p>
        Because the model equation is:
        <br>
        <code>ln(Odds) = &beta;<sub>0</sub> + &beta;<sub>1</sub>x<sub>1</sub> + ... + &beta;<sub>p</sub>x<sub>p</sub></code>
      </p>
      <p>
        If feature <code>x<sub>1</sub></code> increases by <strong>1 unit</strong> while all other features remain constant:
      </p>
      <div class="formula-card">
        <div class="formula-title">&#128290; The Odds Ratio (OR) Formula</div>
        <div class="formula-math">
          Odds Ratio (OR) = e<sup>&beta;<sub>j</sub></sup>
        </div>
        <div class="formula-legend">
          <div class="formula-legend-item"><code>OR &gt; 1.0</code>: Feature increases the odds of the outcome (positive coefficient).</div>
          <div class="formula-legend-item"><code>OR = 1.0</code>: Feature has zero effect on the odds (&beta;<sub>j</sub> = 0).</div>
          <div class="formula-legend-item"><code>OR &lt; 1.0</code>: Feature decreases the odds of the outcome (negative coefficient).</div>
        </div>
      </div>

      <p>
        <strong>Concrete Example:</strong> In our student exam model, the coefficient for completed assignments was <code>&beta; = +1.20</code>.
        <br>
        The Odds Ratio is: <code>e<sup>1.20</sup> = 3.3201</code>.
        <br>
        <em>Interpretation:</em> Each additional assignment completed is associated with a <strong>3.32-fold increase in the odds</strong> of passing the exam, assuming all other factors remain constant.
      </p>

      <div class="callout card-warning">
        <div class="callout-title">&#9888; Critical Caution: Do Not Confuse Odds with Probability or Causality!</div>
        <p>
          An odds ratio of 3.32 does <strong>NOT</strong> mean the student&rsquo;s probability increased by 332%! Odds and probabilities scale differently.
        </p>
        <p>
          Furthermore, learned coefficients represent <strong>statistical associations in observational training data</strong>, not proven causal mechanisms. A high coefficient does not prove that forcing a metric to change will automatically cause the outcome.
        </p>
      </div>
    </section>

    <!-- SECTION 07: DECISION THRESHOLD AND PREDICTED CLASS -->
    <section id="sec-07" class="section-card">
      <span class="section-badge">Section 07</span>
      <h2 class="section-title">Decision Threshold (&tau;) and Predicted Class</h2>
      <p class="section-lead">
        Logistic regression outputs a continuous probability <code>p &isin; (0, 1)</code>. To turn that probability into an actionable binary classification decision (Class 0 or Class 1), we apply a <strong>Decision Threshold (&tau;)</strong>.
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; Threshold Decision Rule</div>
        <div class="formula-math">
          &#375; = 1 &nbsp; if &nbsp; p &ge; &tau; &emsp; | &emsp; &#375; = 0 &nbsp; if &nbsp; p &lt; &tau;
        </div>
      </div>

      <p>
        The universal default threshold across software libraries (including scikit-learn) is <strong>&tau; = 0.50</strong>:
      </p>
      <ul>
        <li>If <code>P(y = 1 | x) &ge; 0.50</code>, predict Class 1.</li>
        <li>If <code>P(y = 1 | x) &lt; 0.50</code>, predict Class 0.</li>
      </ul>

      <h3 class="sub-title">Why 0.50 Is Not Always the Right Threshold</h3>
      <p>
        A threshold of 0.50 assumes that false positives and false negatives carry exactly identical costs. In the real world, this is rarely true!
      </p>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_THRESHOLD_VARIATION}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.5: Shifting Decision Thresholds Across 6 Sample Probabilities.</strong> Lowering the threshold to &tau;=0.30 classifies 5 samples as positive. Raising it to &tau;=0.70 classifies only 2 samples as positive.
        </div>
        <div class="svg-takeaway">
          &#10004; Trade-off Rule: Lowering &tau; increases Recall (catches more positive cases); Raising &tau; increases Precision (fewer false alarms).
        </div>
      </div>

      <h3 class="sub-title">Verified Numerical Comparison Across 6 Sample Probabilities</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Observation</th>
              <th>Estimated Probability (p)</th>
              <th>Default (&tau; = 0.50)</th>
              <th>Sensitive (&tau; = 0.30)</th>
              <th>Conservative (&tau; = 0.70)</th>
              <th>Real-World Context</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Sample A</strong></td>
              <td>0.15 (15%)</td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Neg)</span></td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Neg)</span></td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Neg)</span></td>
              <td>Clear negative across all rules</td>
            </tr>
            <tr>
              <td><strong>Sample B</strong></td>
              <td>0.35 (35%)</td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Neg)</span></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pos)</span></td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Neg)</span></td>
              <td>Flagged positive only by sensitive rule</td>
            </tr>
            <tr>
              <td><strong>Sample C</strong></td>
              <td>0.48 (48%)</td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Neg)</span></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pos)</span></td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Neg)</span></td>
              <td>Borderline point; caught by &tau; = 0.30</td>
            </tr>
            <tr>
              <td><strong>Sample D</strong></td>
              <td>0.52 (52%)</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pos)</span></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pos)</span></td>
              <td><span class="badge" style="background:#FEE2E2;color:#991B1B;">0 (Neg)</span></td>
              <td>Filtered out by conservative rule</td>
            </tr>
            <tr>
              <td><strong>Sample E</strong></td>
              <td>0.75 (75%)</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pos)</span></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pos)</span></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pos)</span></td>
              <td>Robust positive</td>
            </tr>
            <tr>
              <td><strong>Sample F</strong></td>
              <td>0.92 (92%)</td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pos)</span></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pos)</span></td>
              <td><span class="badge" style="background:#DCFCE7;color:#166534;">1 (Pos)</span></td>
              <td>Clear positive across all rules</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout card-concept">
        <div class="callout-title">&#127919; Selecting the Right Operating Threshold</div>
        <p>
          <strong>Scenario 1: Medical Cancer Screening (High Cost of False Negative)</strong><br>
          Missing a malignant tumor (False Negative) can be fatal, while a false alarm (False Positive) is verified with a follow-up biopsy. Doctors intentionally lower the threshold to <code>&tau; = 0.20</code> or <code>0.30</code> to maximize Recall.
        </p>
        <p>
          <strong>Scenario 2: Email Spam Filter (High Cost of False Positive)</strong><br>
          Accidentally sending an urgent job offer or court notice to the spam folder (False Positive) is unacceptable. Engineers raise the threshold to <code>&tau; = 0.85</code> or <code>0.90</code> so only emails that are overwhelmingly likely to be junk are diverted.
        </p>
      </div>
    </section>

    <!-- SECTION 08: DECISION BOUNDARY -->
    <section id="sec-08" class="section-card">
      <span class="section-badge">Section 08</span>
      <h2 class="section-title">The Decision Boundary</h2>
      <p class="section-lead">
        A <strong>Decision Boundary</strong> is the geometric surface in feature space where the model&rsquo;s estimated probability exactly equals the decision threshold: <code>P(y = 1 | x) = &tau;</code>.
      </p>

      <p>
        Under the standard threshold <code>&tau; = 0.50</code>, the decision boundary occurs exactly when the linear score equals zero:
        <br>
        <code>&sigma;(z) = 0.50 &hArr; z = 0</code>
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; Decision Boundary Equation (&tau; = 0.50)</div>
        <div class="formula-math">
          &beta;<sub>0</sub> + &beta;<sub>1</sub>x<sub>1</sub> + &beta;<sub>2</sub>x<sub>2</sub> + ... + &beta;<sub>p</sub>x<sub>p</sub> = 0
        </div>
      </div>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_DECISION_BOUNDARY_1D_2D}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.6: Geometric Decision Boundaries.</strong> In 1D feature space (left), the boundary is a single cutoff point <code>x* = -&beta;<sub>0</sub> / &beta;<sub>1</sub></code>. In 2D feature space (right), the boundary is a straight dividing line separating Class 0 and Class 1.
        </div>
        <div class="svg-takeaway">
          &#10004; Crucial Principle: Standard Logistic Regression creates a <strong>linear decision boundary</strong> in the original feature space.
        </div>
      </div>

      <h3 class="sub-title">How Feature Transformations Create Non-Linear Boundaries</h3>
      <p>
        Beginners often mistakenly believe that Logistic Regression can only ever separate linearly separable data. While the decision boundary is linear with respect to the input features, you can engineer <strong>polynomial or interaction terms</strong>:
      </p>
      <div class="callout card-analogy">
        <div class="callout-title">&#129514; Engineering Non-Linear Boundaries</div>
        <p>
          If you add quadratic terms to the model:
          <br>
          <code>z = &beta;<sub>0</sub> + &beta;<sub>1</sub>x<sub>1</sub><sup>2</sup> + &beta;<sub>2</sub>x<sub>2</sub><sup>2</sup> = 0</code>
        </p>
        <p>
          The decision boundary in the original <code>(x<sub>1</sub>, x<sub>2</sub>)</code> plane becomes an ellipse or circle! The model remains linear in its parameters (&beta;), but its boundary in the raw input space curves around complex data patterns.
        </p>
      </div>
    </section>

    <!-- SECTION 09: HOW DOES LOGISTIC REGRESSION LEARN? -->
    <section id="sec-09" class="section-card">
      <span class="section-badge">Section 09</span>
      <h2 class="section-title">How Does Logistic Regression Learn? (Maximum Likelihood Estimation)</h2>
      <p class="section-lead">
        In Linear Regression, we found optimal parameters using the closed-form Ordinary Least Squares (OLS) formula <code>&beta; = (X<sup>T</sup>X)<sup>-1</sup>X<sup>T</sup>y</code>. In Logistic Regression, the presence of the non-linear sigmoid function makes a closed-form analytical solution impossible.
      </p>

      <p>
        Instead, Logistic Regression learns its weights through an iterative optimization procedure grounded in <strong>Maximum Likelihood Estimation (MLE)</strong>.
      </p>

      <h3 class="sub-title">The 7-Step Training Lifecycle</h3>
      <div class="step-list">
        <div class="step-card">
          <div class="step-number">1</div>
          <div class="step-body">
            <h4>Initialize Coefficients</h4>
            <p>Start with initial coefficient guesses (typically all zeros or small random weights).</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">2</div>
          <div class="step-body">
            <h4>Calculate Linear Scores</h4>
            <p>For each training observation <code>i</code>, compute <code>z<sub>i</sub> = &beta;<sub>0</sub> + &sum; &beta;<sub>j</sub>x<sub>ij</sub></code>.</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">3</div>
          <div class="step-body">
            <h4>Apply Sigmoid Transformation</h4>
            <p>Compute estimated probabilities: <code>p<sub>i</sub> = 1 / (1 + e<sup>-z<sub>i</sub></sup>)</code>.</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">4</div>
          <div class="step-body">
            <h4>Evaluate Training Loss</h4>
            <p>Compare predicted probabilities <code>p<sub>i</sub></code> against true binary labels <code>y<sub>i</sub></code> using Binary Cross-Entropy (Log Loss).</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">5</div>
          <div class="step-body">
            <h4>Calculate the Gradient Error</h4>
            <p>Compute the gradient vector: <code>&nabla;J = (1 / n) &times; X<sup>T</sup>(p - y)</code>. Notice how clean this gradient is: the error is simply the probability residual <code>(p<sub>i</sub> - y<sub>i</sub>)</code>!</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">6</div>
          <div class="step-body">
            <h4>Update Parameters via Numerical Solvers</h4>
            <p>Update weights to decrease loss. Production libraries (like scikit-learn) use second-order quasi-Newton algorithms (such as <code>lbfgs</code> or <code>newton-cg</code>) rather than basic gradient descent for rapid convergence.</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">7</div>
          <div class="step-body">
            <h4>Check Convergence Criteria</h4>
            <p>Repeat steps 2 through 6 until the gradient reaches near zero (tolerance <code>tol = 1e-4</code>) or maximum iterations are exhausted.</p>
          </div>
        </div>
      </div>

      <div class="callout card-concept">
        <div class="callout-title">&#128269; What Is Maximum Likelihood Estimation (MLE)?</div>
        <p>
          Maximum Likelihood asks: <em>&ldquo;Out of all possible coefficient combinations (&beta;), which specific set of weights makes the true training outcomes we actually observed most statistically probable?&rdquo;</em>
        </p>
        <p>
          Because multiplying hundreds of probabilities between 0 and 1 causes floating-point underflow (approaching zero), mathematicians take the log of the likelihood function. Maximizing log-likelihood is mathematically equivalent to <strong>minimizing negative log-likelihood (Log Loss)</strong>.
        </p>
      </div>
    </section>

    <!-- SECTION 10: LOG LOSS / BINARY CROSS-ENTROPY -->
    <section id="sec-10" class="section-card">
      <span class="section-badge">Section 10</span>
      <h2 class="section-title">Log Loss / Binary Cross-Entropy</h2>
      <p class="section-lead">
        The loss function that Logistic Regression minimizes during training is <strong>Binary Cross-Entropy</strong>, commonly referred to as <strong>Log Loss</strong>.
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; The Average Binary Log Loss Formula</div>
        <div class="formula-math">
          J(&beta;) = - (1 / n) &sum;<sub>i=1</sub><sup>n</sup> [ y<sub>i</sub> ln(p<sub>i</sub>) + (1 - y<sub>i</sub>) ln(1 - p<sub>i</sub>) ]
        </div>
        <div class="formula-legend">
          <div class="formula-legend-item"><code>n</code>: Number of training samples.</div>
          <div class="formula-legend-item"><code>y<sub>i</sub></code>: Actual binary ground truth (0 or 1).</div>
          <div class="formula-legend-item"><code>p<sub>i</sub></code>: Model&rsquo;s predicted probability for Class 1 (between 0 and 1).</div>
          <div class="formula-legend-item"><code>ln</code>: Natural logarithm (base e).</div>
          <div class="formula-legend-item"><code>J(&beta;)</code>: Total average log loss (always &ge; 0). Lower is better!</div>
        </div>
      </div>

      <h3 class="sub-title">How the Formula Adapts to Each Class</h3>
      <p>
        The beauty of the formula is how its two terms activate conditionally based on true label <code>y<sub>i</sub></code>:
      </p>
      <ul>
        <li>
          <strong>When actual label y = 1:</strong> The second term <code>(1 - y) &times; ln(1 - p)</code> becomes zero. The loss simplifies to:
          <br>
          <code>Loss = -ln(p)</code>
        </li>
        <li>
          <strong>When actual label y = 0:</strong> The first term <code>y &times; ln(p)</code> becomes zero. The loss simplifies to:
          <br>
          <code>Loss = -ln(1 - p)</code>
        </li>
      </ul>

      <div class="svg-card">
        <div class="svg-container">
          {SVG_LOG_LOSS_CURVES}
        </div>
        <div class="svg-caption">
          <strong>Figure 10.7: Log Loss Curves for Positive (Left) and Negative (Right) Examples.</strong> Notice how predicting <code>p = 0.10</code> when true <code>y = 1</code> triggers a 2.303 penalty, compared to just 0.105 when predicting <code>p = 0.90</code> (a 21.8&times; penalty!).
        </div>
        <div class="svg-takeaway">
          &#10004; Core Mechanism: Log Loss severely punishes confident, arrogant mistakes far more harshly than modest uncertainty.
        </div>
      </div>

      <h3 class="sub-title">Worked Numerical Examples (Python Verified)</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Actual Label (y)</th>
              <th>Predicted Probability (p)</th>
              <th>Confidence Assessment</th>
              <th>Log Loss Calculation</th>
              <th>Calculated Loss Value</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>y = 1</strong></td>
              <td>p = 0.90 (90%)</td>
              <td>Confident &amp; Correct</td>
              <td>-ln(0.90)</td>
              <td><strong>0.1054</strong> (Low loss)</td>
            </tr>
            <tr>
              <td><strong>y = 1</strong></td>
              <td>p = 0.50 (50%)</td>
              <td>Completely Uncertain</td>
              <td>-ln(0.50)</td>
              <td><strong>0.6931</strong> (Moderate loss)</td>
            </tr>
            <tr>
              <td><strong>y = 1</strong></td>
              <td>p = 0.10 (10%)</td>
              <td>Confident &amp; WRONG!</td>
              <td>-ln(0.10)</td>
              <td><strong>2.3026</strong> (21.8&times; penalty!)</td>
            </tr>
            <tr>
              <td><strong>y = 0</strong></td>
              <td>p = 0.10 (10%)</td>
              <td>Confident &amp; Correct</td>
              <td>-ln(1 - 0.10) = -ln(0.90)</td>
              <td><strong>0.1054</strong> (Low loss)</td>
            </tr>
            <tr>
              <td><strong>y = 0</strong></td>
              <td>p = 0.90 (90%)</td>
              <td>Confident &amp; WRONG!</td>
              <td>-ln(1 - 0.90) = -ln(0.10)</td>
              <td><strong>2.3026</strong> (21.8&times; penalty!)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout card-amber">
        <div class="callout-title">&#128295; Practical Numerical Handling: Epsilon Probability Clipping</div>
        <p>
          In pure mathematics, <code>ln(0) = -&infin;</code>. If a model predicted exactly <code>p = 0.0</code> on an observation whose true label was <code>y = 1</code>, the loss would evaluate to infinity, crashing numerical software.
        </p>
        <p>
          To prevent this, production libraries like scikit-learn clip probabilities internally into a safe floating-point range: <code>p = np.clip(p, 1e-15, 1 - 1e-15)</code> before computing log loss.
        </p>
      </div>
    </section>
"""
