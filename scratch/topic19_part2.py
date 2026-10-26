# Topic 19 Content - Part 2: Sections 07 to 13
# Strict Light Mode Only, Native HTML Math, Verified Numerical Examples

TOPIC19_PART2 = """
    <!-- SECTION 07 -->
    <section id="sec-07" class="content-section">
      <span class="section-tag">Section 07</span>
      <h2 class="section-title">Recall (Sensitivity) and Missed Detections</h2>
      <p class="section-intro">
        Out of all the actual positive cases existing in reality, what proportion did your model manage to detect? That is Recall.
      </p>

      <h3>Formula and Technical Definition</h3>
      <div class="math-box">
        Recall = TP / (TP + FN)
        <div class="math-legend">
          &bull; <strong>TP:</strong> True Positives (actual positives correctly found)<br>
          &bull; <strong>FN:</strong> False Negatives (actual positives missed by the model)<br>
          &bull; <strong>Denominator (TP + FN):</strong> Total number of actual positive cases in reality
        </div>
      </div>

      <p>
        <strong>Worked Example:</strong> In our 10-sample spam dataset, there were 5 actual spam emails (TP = 4, FN = 1):
      </p>
      <div class="math-box">
        Recall = 4 / (4 + 1) = 4 / 5 = 0.8000 &nbsp;(80.0%)
      </div>
      <p>
        This means: <em>"The model captured 80% of all real spam emails, but missed 20% (1 spam email slipped into the inbox)."</em>
      </p>

      <div class="card card-analogy">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
          Hypothetical Educational Example: Airport Security Scanner
        </div>
        <p>
          Imagine an airport baggage screening scanner detecting prohibited items. An actual weapon slipping past the scanner (a <strong>False Negative</strong>) could lead to a catastrophe. An innocent water bottle triggering a manual bag check (a <strong>False Positive</strong>) is mildly inconvenient. In this scenario, security teams deliberately optimize for <strong>near-100% Recall</strong> &mdash; missing a threat is unacceptable.
          <br><br>
          <em>Educational Note:</em> In medical screening, machine learning models are designed to maximize Recall to ensure no prospective patient is missed during preliminary triage; such screening tools are decision-support aids and do not replace clinical diagnosis.
        </p>
      </div>

      <h3>Precision vs. Recall: The Inevitable Seesaw Trade-Off</h3>
      <p>
        Precision and Recall naturally pull in opposite directions:
      </p>
      <ul>
        <li>To achieve <strong>100% Recall</strong>, a model can simply classify <em>everything</em> as Positive. It will never miss a real positive (FN = 0), but its Precision will plummet because of countless False Positives.</li>
        <li>To achieve <strong>100% Precision</strong>, a model can become extremely timid, flagging only the single sample it is 99.9% confident about. If that sample is positive, Precision is 100%, but Recall collapses because dozens of other real positives are ignored (FN is huge).</li>
      </ul>

      <!-- FIGURE 7.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 7.1 &bull; Precision vs Recall Trade-Off Illustration</span>
          <span class="visual-tag">Conceptual Comparison</span>
        </div>
        __SVG_PRECISION_VS_RECALL__
        <div class="visual-caption">
          Figure 7.1: The Precision vs Recall trade-off. Precision focuses on prediction purity (minimizing False Positives); Recall focuses on ground-truth coverage (minimizing False Negatives).
        </div>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; Recall Calculation with scikit-learn</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>from sklearn.metrics import recall_score

# Compute recall
rec = recall_score(y_true, y_pred)
print(f"Recall: {rec:.4f}")  # Output: 0.8000 (80.0%)</code></pre>
      </div>
    </section>

    <!-- SECTION 08 -->
    <section id="sec-08" class="content-section">
      <span class="section-tag">Section 08</span>
      <h2 class="section-title">Specificity, False Positive Rate, and False Negative Rate</h2>
      <p class="section-intro">
        While Precision and Recall focus primarily on the Positive class, evaluating how the model treats the Negative class is essential for comprehensive diagnostics.
      </p>

      <h3>1. Specificity (True Negative Rate)</h3>
      <p>
        <strong>Specificity</strong> measures the proportion of actual negative cases that were correctly identified as negative:
      </p>
      <div class="math-box">
        Specificity = TN / (TN + FP)
      </div>
      <p>
        In our 10-sample spam dataset, there were 5 actual legitimate emails (TN = 4, FP = 1):
      </p>
      <div class="math-box">
        Specificity = 4 / (4 + 1) = 4 / 5 = 0.8000 &nbsp;(80.0%)
      </div>

      <h3>2. False Positive Rate (FPR)</h3>
      <p>
        <strong>FPR</strong> measures the proportion of actual negative cases that were mistakenly flagged as positive:
      </p>
      <div class="math-box">
        FPR = FP / (FP + TN) = 1 &minus; Specificity
      </div>
      <p>
        In our dataset:
      </p>
      <div class="math-box">
        FPR = 1 / (1 + 4) = 1 / 5 = 0.2000 &nbsp;(20.0%) &nbsp;[or 1 &minus; 0.80 = 0.20]
      </div>

      <h3>3. False Negative Rate (FNR) &mdash; Miss Rate</h3>
      <p>
        <strong>FNR</strong> measures the proportion of actual positive cases that were missed:
      </p>
      <div class="math-box">
        FNR = FN / (FN + TP) = 1 &minus; Recall
      </div>
      <p>
        In our dataset:
      </p>
      <div class="math-box">
        FNR = 1 / (1 + 4) = 1 / 5 = 0.2000 &nbsp;(20.0%) &nbsp;[or 1 &minus; 0.80 = 0.20]
      </div>

      <!-- FIGURE 8.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 8.1 &bull; Rate Relationships: Specificity, FPR, and FNR</span>
          <span class="visual-tag">Mathematical Connections</span>
        </div>
        __SVG_SPECIFICITY_FPR_FNR__
        <div class="visual-caption">
          Figure 8.1: Structural relationships among rates. The actual negative column splits into Specificity (TNR) and FPR (sum = 1.0). The actual positive column splits into Recall (TPR) and FNR (sum = 1.0).
        </div>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Metric Name</th>
              <th>Formula</th>
              <th>Evaluates Condition</th>
              <th>Our 10-Sample Value</th>
              <th>Key Property</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Sensitivity (Recall / TPR)</strong></td>
              <td>TP / (TP + FN)</td>
              <td>Actual Positives</td>
              <td>0.8000 (80.0%)</td>
              <td>Sensitivity + FNR = 1.0</td>
            </tr>
            <tr>
              <td><strong>Specificity (TNR)</strong></td>
              <td>TN / (TN + FP)</td>
              <td>Actual Negatives</td>
              <td>0.8000 (80.0%)</td>
              <td>Specificity + FPR = 1.0</td>
            </tr>
            <tr>
              <td><strong>False Positive Rate (FPR)</strong></td>
              <td>FP / (FP + TN)</td>
              <td>Actual Negatives</td>
              <td>0.2000 (20.0%)</td>
              <td>Plotted on X-axis of ROC Curve</td>
            </tr>
            <tr>
              <td><strong>False Negative Rate (FNR)</strong></td>
              <td>FN / (FN + TP)</td>
              <td>Actual Positives</td>
              <td>0.2000 (20.0%)</td>
              <td>Proportion of missed detections</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 09 -->
    <section id="sec-09" class="content-section">
      <span class="section-tag">Section 09</span>
      <h2 class="section-title">F1-Score and F-Beta Score</h2>
      <p class="section-intro">
        When you need a single summary score that balances both Precision and Recall without being misled by class imbalance, the F1-Score is the industry standard.
      </p>

      <h3>Formula and The Harmonic Mean</h3>
      <p>
        The <strong>F1-Score</strong> is the <strong>harmonic mean</strong> of Precision and Recall:
      </p>
      <div class="math-box">
        F1 = 2 &times; (Precision &times; Recall) / (Precision + Recall)
      </div>

      <p>
        <strong>Worked Example:</strong> With Precision = 0.8000 and Recall = 0.8000:
      </p>
      <div class="math-box">
        F1 = 2 &times; (0.80 &times; 0.80) / (0.80 + 0.80) = 2 &times; 0.64 / 1.60 = 1.28 / 1.60 = 0.8000
      </div>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Why Harmonic Mean Instead of Simple Arithmetic Average?
        </div>
        <p>
          The simple arithmetic average (P + R) / 2 is dangerously forgiving of catastrophic failures. Consider an extreme model with <strong>Precision = 1.0</strong> and <strong>Recall = 0.02</strong> (it made 1 correct prediction and missed 98 others):
          <br>
          &bull; <em>Arithmetic Average:</em> (1.0 + 0.02) / 2 = 0.510 (looks mediocre).
          <br>
          &bull; <em>Harmonic Mean (F1):</em> $2 &times; (1.0 &times; 0.02) / (1.0 + 0.02) = 0.04 / 1.02 = 0.039 (correctly reveals near-total failure!).
          <br>
          The harmonic mean is pulled strongly toward the lower number. If <em>either</em> Precision or Recall is low, the F1-Score collapses.
        </p>
      </div>

      <h3>F-Beta Score (F<sub>&beta;</sub>): Customizing the Trade-Off</h3>
      <p>
        What if your business problem values Recall twice as much as Precision? You can use the generalized <strong>F<sub>&beta;</sub>-Score</strong>:
      </p>
      <div class="math-box">
        F<sub>&beta;</sub> = (1 + &beta;&sup2;) &times; (Precision &times; Recall) / (&beta;&sup2; &times; Precision + Recall)
      </div>
      <ul>
        <li><strong>&beta; = 1.0:</strong> Standard F1-Score (weights Precision and Recall equally).</li>
        <li><strong>&beta; = 2.0 (F2-Score):</strong> Gives <strong>Recall twice the weight</strong> of Precision. Ideal for fraud detection, medical triage, and threat identification where missed cases are intolerable.</li>
        <li><strong>&beta; = 0.5 (F0.5-Score):</strong> Gives <strong>Precision twice the weight</strong> of Recall. Ideal for spam filtering and automated customer communications where false alarms destroy user trust.</li>
      </ul>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Important Caveat: What F1 Ignores
        </div>
        <p>
          Notice that the formula for F1 includes only TP, FP, and FN. <strong>True Negatives (TN) do not appear anywhere in the F1 formula!</strong> While this makes F1 immune to overwhelming majorities of negative samples, it also means F1 does not reward a model for effectively filtering millions of true negatives. It cannot replace a full confusion matrix inspection.
        </p>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; F1 and F-Beta Calculations</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>from sklearn.metrics import f1_score, fbeta_score

# Compute standard F1 score
f1 = f1_score(y_true, y_pred)
print(f"F1-Score: {f1:.4f}")  # Output: 0.8000

# Compute F2 score (Recall priority)
f2 = fbeta_score(y_true, y_pred, beta=2.0)
print(f"F2-Score (Recall emphasis): {f2:.4f}")  # Output: 0.8000

# Compute F0.5 score (Precision priority)
f05 = fbeta_score(y_true, y_pred, beta=0.5)
print(f"F0.5-Score (Precision emphasis): {f05:.4f}")  # Output: 0.8000</code></pre>
      </div>
    </section>

    <!-- SECTION 10 -->
    <section id="sec-10" class="content-section">
      <span class="section-tag">Section 10</span>
      <h2 class="section-title">Classification Thresholds</h2>
      <p class="section-intro">
        A classification model produces continuous confidence scores. The decision threshold determines where you draw the line between Positive and Negative.
      </p>

      <h3>The Default 0.50 Threshold is an Arbitrary Convention</h3>
      <p>
        By default, virtually all machine learning frameworks assign an observation to Class 1 if P(y=1|X) &ge; 0.50, and Class 0 otherwise. However, <strong>0.50 is not an immutable law of nature</strong> &mdash; it is merely an arbitrary default assuming equal penalty for False Positives and False Negatives.
      </p>

      <h3>How Shifting the Threshold Changes Metrics</h3>
      <p>
        Changing the threshold alters the entire confusion matrix:
      </p>
      <ul>
        <li>
          <strong>Lowering the Threshold (e.g., from 0.50 down to 0.20):</strong>
          <br>The model becomes aggressive. It predicts Positive much more readily.
          <br>&bull; <strong>Recall increases:</strong> Fewer positive cases are missed (FN decreases).
          <br>&bull; <strong>Precision decreases:</strong> More innocent samples get falsely flagged (FP increases).
        </li>
        <li>
          <strong>Raising the Threshold (e.g., from 0.50 up to 0.80):</strong>
          <br>The model becomes conservative. It flags Positive only when exceptionally confident.
          <br>&bull; <strong>Precision increases:</strong> Fewer false alarms occur (FP decreases).
          <br>&bull; <strong>Recall decreases:</strong> Many borderline positive cases are overlooked (FN increases).
        </li>
      </ul>

      <!-- FIGURE 10.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 10.1 &bull; Threshold Sweep Effect on Prediction Counts</span>
          <span class="visual-tag">Decision Boundary Dynamics</span>
        </div>
        __SVG_THRESHOLD_SWEEP__
        <div class="visual-caption">
          Figure 10.1: Sweeping the classification threshold across candidate values (0.20, 0.50, 0.80). Shifting left captures more positives (higher recall); shifting right minimizes false alarms (higher precision).
        </div>
      </div>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Golden Rule: Never Tune Thresholds on the Test Set!
        </div>
        <p>
          Selecting an optimal operational threshold must be performed on the <strong>validation set</strong> or via cross-validation. Tuning the threshold on the final test set is a severe form of data snooping (data leakage) that produces unrealistically optimistic performance estimates.
        </p>
      </div>
    </section>

    <!-- SECTION 11 -->
    <section id="sec-11" class="content-section">
      <span class="section-tag">Section 11</span>
      <h2 class="section-title">Interactive Classification Threshold Demonstration</h2>
      <p class="section-intro">
        Experiment with threshold adjustment on our 10-sample dataset below. Adjust the slider to see how predictions, confusion matrix counts, and resulting metrics adapt in real time.
      </p>

      <!-- INTERACTIVE WIDGET -->
      <div class="threshold-widget">
        <div class="widget-controls">
          <label for="threshold-slider" style="font-weight:700; color:#1E1B4B; font-size:1rem;">
            Adjust Classification Decision Threshold:
          </label>
          <div class="slider-row">
            <span style="font-size:0.85rem; font-weight:600; color:#64748B;">0.00</span>
            <input type="range" id="threshold-slider" min="0.05" max="0.95" step="0.05" value="0.50" aria-label="Classification Threshold">
            <span style="font-size:0.85rem; font-weight:600; color:#64748B;">1.00</span>
            <div class="threshold-val-badge" id="threshold-val-display">&theta; = 0.50</div>
          </div>
        </div>

        <div class="widget-metrics-grid">
          <div class="metric-pill">
            <div class="metric-pill-label">True Pos (TP)</div>
            <div class="metric-pill-val" id="val-tp" style="color:#15803D;">4</div>
          </div>
          <div class="metric-pill">
            <div class="metric-pill-label">False Pos (FP)</div>
            <div class="metric-pill-val" id="val-fp" style="color:#DC2626;">1</div>
          </div>
          <div class="metric-pill">
            <div class="metric-pill-label">True Neg (TN)</div>
            <div class="metric-pill-val" id="val-tn" style="color:#15803D;">4</div>
          </div>
          <div class="metric-pill">
            <div class="metric-pill-label">False Neg (FN)</div>
            <div class="metric-pill-val" id="val-fn" style="color:#DC2626;">1</div>
          </div>
          <div class="metric-pill">
            <div class="metric-pill-label">Precision</div>
            <div class="metric-pill-val" id="val-prec" style="color:#4F46E5;">0.80</div>
          </div>
          <div class="metric-pill">
            <div class="metric-pill-label">Recall</div>
            <div class="metric-pill-val" id="val-rec" style="color:#4F46E5;">0.80</div>
          </div>
          <div class="metric-pill">
            <div class="metric-pill-label">F1-Score</div>
            <div class="metric-pill-val" id="val-f1" style="color:#4F46E5;">0.80</div>
          </div>
          <div class="metric-pill">
            <div class="metric-pill-label">Accuracy</div>
            <div class="metric-pill-val" id="val-acc" style="color:#0F172A;">0.80</div>
          </div>
        </div>

        <p style="font-size:0.85rem; color:#64748B; margin-bottom:12px;">
          <em>Live Samples Table:</em> Below are the 10 evaluated samples. Green indicates a correct prediction (&check;); red indicates an error (&#10006;).
        </p>

        <div class="table-container">
          <table id="threshold-samples-table">
            <thead>
              <tr>
                <th>Sample ID</th>
                <th>Actual Label</th>
                <th>Predicted Prob</th>
                <th>Predicted Class (&ge; &theta;)</th>
                <th>Outcome Cell</th>
              </tr>
            </thead>
            <tbody id="samples-tbody">
              <!-- Dynamically populated by JS or fallback -->
              <tr><td>Email #1</td><td>1 (Spam)</td><td>0.92</td><td>1 (Spam)</td><td><span style="color:#15803D; font-weight:700;">TP &check;</span></td></tr>
              <tr><td>Email #2</td><td>1 (Spam)</td><td>0.85</td><td>1 (Spam)</td><td><span style="color:#15803D; font-weight:700;">TP &check;</span></td></tr>
              <tr><td>Email #3</td><td>1 (Spam)</td><td>0.78</td><td>1 (Spam)</td><td><span style="color:#15803D; font-weight:700;">TP &check;</span></td></tr>
              <tr><td>Email #4</td><td>1 (Spam)</td><td>0.65</td><td>1 (Spam)</td><td><span style="color:#15803D; font-weight:700;">TP &check;</span></td></tr>
              <tr><td>Email #5</td><td>1 (Spam)</td><td>0.35</td><td>0 (Not Spam)</td><td><span style="color:#DC2626; font-weight:700;">FN &#10006;</span></td></tr>
              <tr><td>Email #6</td><td>0 (Not Spam)</td><td>0.60</td><td>1 (Spam)</td><td><span style="color:#DC2626; font-weight:700;">FP &#10006;</span></td></tr>
              <tr><td>Email #7</td><td>0 (Not Spam)</td><td>0.40</td><td>0 (Not Spam)</td><td><span style="color:#15803D; font-weight:700;">TN &check;</span></td></tr>
              <tr><td>Email #8</td><td>0 (Not Spam)</td><td>0.30</td><td>0 (Not Spam)</td><td><span style="color:#15803D; font-weight:700;">TN &check;</span></td></tr>
              <tr><td>Email #9</td><td>0 (Not Spam)</td><td>0.20</td><td>0 (Not Spam)</td><td><span style="color:#15803D; font-weight:700;">TN &check;</span></td></tr>
              <tr><td>Email #10</td><td>0 (Not Spam)</td><td>0.10</td><td>0 (Not Spam)</td><td><span style="color:#15803D; font-weight:700;">TN &check;</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- STATIC FALLBACK SEQUENCE -->
      <h3>Static Threshold Progression Reference Table</h3>
      <p>
        For environments without active JavaScript, the exact mathematically calculated outputs across 5 representative thresholds are documented below:
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Threshold (&theta;)</th>
              <th>TP</th>
              <th>FP</th>
              <th>TN</th>
              <th>FN</th>
              <th>Precision</th>
              <th>Recall</th>
              <th>F1-Score</th>
              <th>Accuracy</th>
              <th>Operational Profile</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>0.20</strong></td>
              <td>5</td>
              <td>4</td>
              <td>1</td>
              <td>0</td>
              <td>0.5556</td>
              <td>1.0000</td>
              <td>0.7143</td>
              <td>0.6000</td>
              <td>Aggressive (Zero Missed Positives)</td>
            </tr>
            <tr>
              <td><strong>0.40</strong></td>
              <td>4</td>
              <td>2</td>
              <td>3</td>
              <td>1</td>
              <td>0.6667</td>
              <td>0.8000</td>
              <td>0.7273</td>
              <td>0.7000</td>
              <td>Moderate High-Recall</td>
            </tr>
            <tr>
              <td><strong>0.50 (Default)</strong></td>
              <td>4</td>
              <td>1</td>
              <td>4</td>
              <td>1</td>
              <td>0.8000</td>
              <td>0.8000</td>
              <td>0.8000</td>
              <td>0.8000</td>
              <td>Balanced Operating Point</td>
            </tr>
            <tr>
              <td><strong>0.70</strong></td>
              <td>3</td>
              <td>0</td>
              <td>5</td>
              <td>2</td>
              <td>1.0000</td>
              <td>0.6000</td>
              <td>0.7500</td>
              <td>0.8000</td>
              <td>High Precision (Zero False Alarms)</td>
            </tr>
            <tr>
              <td><strong>0.80</strong></td>
              <td>2</td>
              <td>0</td>
              <td>5</td>
              <td>3</td>
              <td>1.0000</td>
              <td>0.4000</td>
              <td>0.5714</td>
              <td>0.7000</td>
              <td>Very Conservative</td>
            </tr>
          </tbody>
        </table>
      </div>

      <script>
        (function() {
          var slider = document.getElementById('threshold-slider');
          if (!slider) return;

          var samples = [
            { id: "Email #1", actual: 1, prob: 0.92 },
            { id: "Email #2", actual: 1, prob: 0.85 },
            { id: "Email #3", actual: 1, prob: 0.78 },
            { id: "Email #4", actual: 1, prob: 0.65 },
            { id: "Email #5", actual: 1, prob: 0.35 },
            { id: "Email #6", actual: 0, prob: 0.60 },
            { id: "Email #7", actual: 0, prob: 0.40 },
            { id: "Email #8", actual: 0, prob: 0.30 },
            { id: "Email #9", actual: 0, prob: 0.20 },
            { id: "Email #10", actual: 0, prob: 0.10 }
          ];

          function update() {
            var th = parseFloat(slider.value);
            document.getElementById('threshold-val-display').textContent = "\u03B8 = " + th.toFixed(2);

            var tp = 0, fp = 0, tn = 0, fn = 0;
            var tbody = document.getElementById('samples-tbody');
            if (tbody) tbody.innerHTML = '';

            for (var i = 0; i < samples.length; i++) {
              var s = samples[i];
              var pred = (s.prob >= th) ? 1 : 0;
              var outcome = "";
              var outcomeStyle = "";

              if (s.actual === 1 && pred === 1) {
                tp++;
                outcome = "TP \u2713";
                outcomeStyle = "color:#15803D; font-weight:700;";
              } else if (s.actual === 0 && pred === 0) {
                tn++;
                outcome = "TN \u2713";
                outcomeStyle = "color:#15803D; font-weight:700;";
              } else if (s.actual === 0 && pred === 1) {
                fp++;
                outcome = "FP \u2716";
                outcomeStyle = "color:#DC2626; font-weight:700;";
              } else {
                fn++;
                outcome = "FN \u2716";
                outcomeStyle = "color:#DC2626; font-weight:700;";
              }

              if (tbody) {
                var row = document.createElement('tr');
                row.innerHTML = "<td>" + s.id + "</td>" +
                  "<td>" + (s.actual === 1 ? "1 (Spam)" : "0 (Not Spam)") + "</td>" +
                  "<td>" + s.prob.toFixed(2) + "</td>" +
                  "<td>" + (pred === 1 ? "1 (Spam)" : "0 (Not Spam)") + "</td>" +
                  "<td><span style='" + outcomeStyle + "'>" + outcome + "</span></td>";
                tbody.appendChild(row);
              }
            }

            var prec = (tp + fp > 0) ? (tp / (tp + fp)) : 0;
            var rec = (tp + fn > 0) ? (tp / (tp + fn)) : 0;
            var f1 = (prec + rec > 0) ? (2 * prec * rec / (prec + rec)) : 0;
            var acc = (tp + tn + fp + fn > 0) ? ((tp + tn) / (tp + tn + fp + fn)) : 0;

            document.getElementById('val-tp').textContent = tp;
            document.getElementById('val-fp').textContent = fp;
            document.getElementById('val-tn').textContent = tn;
            document.getElementById('val-fn').textContent = fn;
            document.getElementById('val-prec').textContent = prec.toFixed(2);
            document.getElementById('val-rec').textContent = rec.toFixed(2);
            document.getElementById('val-f1').textContent = f1.toFixed(2);
            document.getElementById('val-acc').textContent = acc.toFixed(2);
          }

          slider.addEventListener('input', update);
        })();
      </script>
    </section>

    <!-- SECTION 12 -->
    <section id="sec-12" class="content-section">
      <span class="section-tag">Section 12</span>
      <h2 class="section-title">ROC Curve and ROC-AUC</h2>
      <p class="section-intro">
        How do you evaluate a model's diagnostic power across ALL possible thresholds at once? The Receiver Operating Characteristic (ROC) curve is the industry's answer.
      </p>

      <h3>What Does the ROC Curve Represent?</h3>
      <p>
        The <strong>ROC Curve</strong> plots the <strong>True Positive Rate (TPR / Recall)</strong> on the Y-axis against the <strong>False Positive Rate (FPR)</strong> on the X-axis for every conceivable decision threshold from 0.0 to 1.0.
      </p>
      <ul>
        <li><strong>Y-axis &mdash; True Positive Rate (TPR):</strong> TPR = TP / (TP + FN) (we want this as high as possible).</li>
        <li><strong>X-axis &mdash; False Positive Rate (FPR):</strong> FPR = FP / (FP + TN) (we want this as low as possible).</li>
      </ul>

      <!-- FIGURE 12.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 12.1 &bull; ROC Curve with Random Classifier Reference Line</span>
          <span class="visual-tag">Threshold-Agnostic Ranking</span>
        </div>
        __SVG_ROC_CURVE__
        <div class="visual-caption">
          Figure 12.1: The ROC curve plotted across thresholds. A perfect model passes through (0, 1) with an AUC of 1.0. A completely random guess follows the diagonal 45-degree dashed line with an AUC of 0.50. Our verified 10-sample model achieves an ROC-AUC of 0.9200.
        </div>
      </div>

      <h3>Understanding the Area Under the Curve (ROC-AUC)</h3>
      <p>
        The <strong>ROC-AUC (Area Under the ROC Curve)</strong> collapses the entire curve into a single scalar value between 0.0 and 1.0:
      </p>
      <div class="math-box">
        0.5 &le; ROC-AUC &le; 1.0
      </div>
      <ul>
        <li><strong>AUC = 1.0:</strong> Perfect classifier. There exists a threshold that completely separates positive and negative classes with zero False Positives and zero False Negatives.</li>
        <li><strong>AUC = 0.5:</strong> Random chance. The model has zero discriminative ability (equivalent to flipping an unbiased coin).</li>
        <li><strong>AUC &lt; 0.5:</strong> Worse than random guessing! (Note: Inverting the model's predictions will yield an AUC &gt; 0.5).</li>
      </ul>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Probabilistic Interpretation of ROC-AUC
        </div>
        <p>
          ROC-AUC has a fascinating probabilistic meaning: <strong>It is the exact probability that the model will assign a higher predicted score to a randomly chosen positive sample than to a randomly chosen negative sample.</strong>
          <br>
          For our 10-sample spam dataset, ROC-AUC = 0.9200. This means if you pick one random spam email and one random legitimate email, there is a <strong>92.0% chance</strong> the model scored the spam email higher!
        </p>
      </div>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Common Trap: ROC-AUC Does Not Choose Your Operating Threshold
        </div>
        <p>
          A high ROC-AUC tells you that the model is great at <em>ranking</em> samples. It does <strong>not</strong> tell you what threshold to set in production! You must still inspect the operational trade-offs and select a concrete threshold based on business costs. Furthermore, <strong>never pass hard binary labels (0 and 1)</strong> into <code>roc_curve()</code>; it requires continuous probability scores!
        </p>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; ROC Curve and ROC-AUC Computation</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

# Compute ROC curve coordinates and AUC score
fpr, tpr, thresholds = roc_curve(y_true, y_prob)
auc = roc_auc_score(y_true, y_prob)

print(f"ROC-AUC: {auc:.4f}")  # Output: 0.9200

# Plotting ROC Curve
plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, color="#4F46E5", lw=2.5, label=f"Model ROC (AUC = {auc:.4f})")
plt.plot([0, 1], [0, 1], color="#94A3B8", lw=1.5, linestyle="--", label="Random Chance (AUC = 0.50)")
plt.xlim([-0.02, 1.02])
plt.ylim([-0.02, 1.05])
plt.xlabel("False Positive Rate (FPR)", fontweight="bold")
plt.ylabel("True Positive Rate (Recall / TPR)", fontweight="bold")
plt.title("ROC Curve &bull; Binary Spam Classifier", fontsize=12, fontweight="bold")
plt.legend(loc="lower right")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
# plt.show()</code></pre>
      </div>
    </section>

    <!-- SECTION 13 -->
    <section id="sec-13" class="content-section">
      <span class="section-tag">Section 13</span>
      <h2 class="section-title">Precision–Recall Curve and Average Precision (AP)</h2>
      <p class="section-intro">
        When evaluating heavily imbalanced datasets, the ROC curve can present an overly rosy picture. The Precision–Recall (PR) curve provides an unvarnished view of minority-class performance.
      </p>

      <h3>Why ROC Curves Can Mask Poor Performance on Imbalanced Data</h3>
      <p>
        Recall that the X-axis of the ROC curve is FPR = FP / (TN + FP). If the negative class has 100,000 samples and the model makes 100 False Positives, the FPR is:
      </p>
      <div class="math-box">
        FPR = 100 / (100,000 + 100) = 0.00099 &nbsp;(virtually 0!)
      </div>
      <p>
        The ROC curve barely moves to the right, looking stellar. But if there were only 20 true positive cases in the entire dataset, those 100 False Positives mean that for every 1 real positive found, the model generated 5 false alarms! Precision is an abysmal $20 / (20 + 100) \approx 16.7%$. The ROC curve hides this disaster; the <strong>Precision–Recall curve exposes it immediately</strong>.
      </p>

      <!-- FIGURE 13.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 13.1 &bull; Precision–Recall Curve with Baseline Prevalence</span>
          <span class="visual-tag">Imbalance Diagnostic</span>
        </div>
        __SVG_PR_CURVE__
        <div class="visual-caption">
          Figure 13.1: Precision–Recall curve. The baseline reference line is not 0.50 &mdash; it equals the dataset's positive class prevalence (here 5/10 = 0.50). Average Precision (AP) calculated across step-weighted thresholds is 0.9429.
        </div>
      </div>

      <h3>The PR Baseline: Class Prevalence</h3>
      <p>
        Unlike the ROC curve where random guessing produces a constant diagonal at $0.50, the baseline on a PR curve is a horizontal line equal to the <strong>positive class prevalence</strong>:
      </p>
      <div class="math-box">
        Baseline PR = Positive Cases / Total Samples = P / (P + N)
      </div>
      <p>
        If a fraud dataset contains 0.5% fraud, the random chance baseline is $0.005. A curve staying at $0.005 indicates zero skill.
      </p>

      <h3>Average Precision (AP) vs Area Under the PR Curve</h3>
      <p>
        In scikit-learn, <code>average_precision_score()</code> summarizes the PR curve using a weighted mean of precisions achieved at each threshold, with the increase in recall from the previous threshold used as the weight:
      </p>
      <div class="math-box">
        AP = &sum;<sub>n</sub> (R<sub>n</sub> &minus; R<sub>n&minus;1</sub>) &times; P<sub>n</sub>
      </div>
      <p>
        On our 10-sample spam dataset, the calculated <strong>Average Precision is 0.9429</strong>.
      </p>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; Precision–Recall Curve and Average Precision</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>from sklearn.metrics import precision_recall_curve, average_precision_score

# Compute Precision-Recall curve
precision_pts, recall_pts, pr_thresholds = precision_recall_curve(y_true, y_prob)
ap = average_precision_score(y_true, y_prob)

print(f"Average Precision (AP): {ap:.4f}")  # Output: 0.9429

# Plotting PR Curve
plt.figure(figsize=(6, 5))
plt.plot(recall_pts, precision_pts, color="#7E22CE", lw=2.5, label=f"Model PR (AP = {ap:.4f})")
plt.axhline(y=0.50, color="#94A3B8", linestyle="--", label="Baseline Prevalence (0.50)")
plt.xlim([-0.02, 1.02])
plt.ylim([0.45, 1.05])
plt.xlabel("Recall", fontweight="bold")
plt.ylabel("Precision", fontweight="bold")
plt.title("Precision–Recall Curve &bull; Binary Spam Classifier", fontsize=12, fontweight="bold")
plt.legend(loc="lower left")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
# plt.show()</code></pre>
      </div>
    </section>
"""
