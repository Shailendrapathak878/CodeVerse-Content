# Topic 19 Content - Part 3: Sections 14 to 21
# Strict Light Mode Only, Native HTML Math, Verified Numerical Examples

TOPIC19_PART3 = """
    <!-- SECTION 14 -->
    <section id="sec-14" class="content-section">
      <span class="section-tag">Section 14</span>
      <h2 class="section-title">Multiclass Classification Metrics and Averaging</h2>
      <p class="section-intro">
        Real-world problems frequently involve more than two outcomes &mdash; such as classifying images into Cats, Dogs, and Birds. How do Precision, Recall, and F1 adapt when there are K &gt; 2 classes?
      </p>

      <h3>The Multiclass Confusion Matrix</h3>
      <p>
        For a <em>K</em>-class problem, the confusion matrix becomes a K \times K table. Each row represents the true class; each column represents the predicted class. The main diagonal represents correct predictions for each class.
      </p>

      <!-- FIGURE 14.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 14.1 &bull; 3-Class Multiclass Confusion Matrix (Cat, Dog, Bird)</span>
          <span class="visual-tag">Multiclass Diagnostics</span>
        </div>
        __SVG_MULTICLASS_CM__
        <div class="visual-caption">
          Figure 14.1: Multiclass confusion matrix for 15 animal images across 3 balanced classes (5 Cats, 5 Dogs, 5 Birds). Diagonal entries represent True Positives for each individual class; off-diagonal elements show specific class-to-class confusions.
        </div>
      </div>

      <h3>Per-Class Metrics (One-vs-Rest)</h3>
      <p>
        To evaluate each class individually, we treat that class as "Positive" and all other classes collectively as "Negative":
      </p>
      <ul>
        <li>
          <strong>Class 0 (Cat):</strong>
          <br>&bull; TP = 4, FP = 1 (1 Dog predicted as Cat), FN = 1 (1 Cat predicted as Dog)
          <br>&bull; Precision = 4 / (4 + 1) = <strong>0.8000</strong>, Recall = 4 / (4 + 1) = <strong>0.8000</strong>, F1 = <strong>0.8000</strong>
        </li>
        <li>
          <strong>Class 1 (Dog):</strong>
          <br>&bull; TP = 3, FP = 2 (1 Cat + 1 Bird predicted as Dog), FN = 2 (1 Dog predicted as Cat + 1 Dog predicted as Bird)
          <br>&bull; Precision = 3 / (3 + 2) = <strong>0.6000</strong>, Recall = 3 / (3 + 2) = <strong>0.6000</strong>, F1 = <strong>0.6000</strong>
        </li>
        <li>
          <strong>Class 2 (Bird):</strong>
          <br>&bull; TP = 4, FP = 1 (1 Dog predicted as Bird), FN = 1 (1 Bird predicted as Dog)
          <br>&bull; Precision = 4 / (4 + 1) = <strong>0.8000</strong>, Recall = 4 / (4 + 1) = <strong>0.8000</strong>, F1 = <strong>0.8000</strong>
        </li>
      </ul>

      <h3>The Three Averaging Strategies: Macro, Micro, and Weighted</h3>
      <p>
        To summarize per-class scores into a single overall metric, machine learning uses three distinct aggregation strategies:
      </p>

      <!-- FIGURE 14.2 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 14.2 &bull; Macro vs Micro vs Weighted Averaging Mechanisms</span>
          <span class="visual-tag">Aggregation Logic</span>
        </div>
        __SVG_MACRO_MICRO_WEIGHTED__
        <div class="visual-caption">
          Figure 14.2: Comparison of averaging methods. Macro averages treat all classes equally regardless of frequency; Weighted averages weight each class by its support; Micro aggregates global TP, FP, FN counts.
        </div>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Averaging Method</th>
              <th>How It Is Calculated</th>
              <th>Sensitivity to Class Imbalance</th>
              <th>When to Use It</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Macro Average</strong></td>
              <td>Computes the metric independently for each class, then takes the unweighted arithmetic mean: <br><code>(M_1 + M_2 + ... + M_K) / K</code></td>
              <td><strong>High:</strong> Rare minority classes contribute just as much to the final score as massive majority classes.</td>
              <td>When every class is equally important to business goals (e.g., medical diagnoses where rare diseases must not be neglected).</td>
            </tr>
            <tr>
              <td><strong>Weighted Average</strong></td>
              <td>Computes metric per class, then takes an average weighted by the actual number of instances (<strong>support</strong>) in each class.</td>
              <td><strong>Low:</strong> Dominant majority classes heavily influence the final score; minority class drops are diluted.</td>
              <td>When you want an overall population-level metric reflecting real-world encounter frequencies.</td>
            </tr>
            <tr>
              <td><strong>Micro Average</strong></td>
              <td>Sums up total TP, FP, and FN globally across all classes, then computes the metric once.</td>
              <td><strong>Zero:</strong> In multi-class classification where each sample has exactly one label, Micro Precision = Micro Recall = Overall Accuracy!</td>
              <td>When overall sample-level throughput is the primary concern, or in multi-label classification tasks.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; Multiclass Classification Report</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

# 15 evaluated animals across 3 balanced classes (5 of each)
y_multi_true = np.array([0,0,0,0,0, 1,1,1,1,1, 2,2,2,2,2])
y_multi_pred = np.array([0,0,0,0,1, 0,1,1,1,2, 1,2,2,2,2])

# Generate full classification report
report = classification_report(
    y_multi_true, 
    y_multi_pred, 
    target_names=["Cat", "Dog", "Bird"],
    digits=4
)
print(report)</code></pre>
      </div>

      <p>
        <strong>Output Verification:</strong>
        <br>Accuracy = 11 / 15 = <strong>0.7333 (73.33%)</strong>.
        <br>Macro Average F1 = (0.8000 + 0.6000 + 0.8000) / 3 = <strong>0.7333</strong>.
        <br>Weighted Average F1 = (5&times;0.8000 + 5&times;0.6000 + 5&times;0.8000) / 15 = <strong>0.7333</strong> (identical here due to balanced support).
      </p>
    </section>

    <!-- SECTION 15 -->
    <section id="sec-15" class="content-section">
      <span class="section-tag">Section 15</span>
      <h2 class="section-title">Regression Evaluation Basics</h2>
      <p class="section-intro">
        In regression, the model predicts a continuous numerical quantity rather than a class label. A prediction is rarely exactly equal to reality &mdash; what matters is the magnitude and pattern of the errors.
      </p>

      <h3>Continuous Targets vs Predictions</h3>
      <p>
        For observation <em>i</em>:
      </p>
      <ul>
        <li><strong>y<sub>i</sub>:</strong> The actual continuous target value (e.g., $300,000 house price).</li>
        <li><strong>&#375;<sub>i</sub>:</strong> The model's continuous predicted value (e.g., $320,000 estimate).</li>
      </ul>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Technical Definition: Residual and Error Sign Convention
        </div>
        <p>
          In standard statistical and machine learning literature, the <strong>residual</strong> (error) for sample <em>i</em> is defined as:
          <br>
          <strong>e<sub>i</sub> = y<sub>i</sub> &minus; &#375;<sub>i</sub> &nbsp;(Actual &minus; Predicted)</strong>
          <br><br>
          &bull; <strong>e<sub>i</sub> &gt; 0 (Positive Residual):</strong> The model <strong>underpredicted</strong> (actual was higher than predicted).
          <br>
          &bull; <strong>e<sub>i</sub> &lt; 0 (Negative Residual):</strong> The model <strong>overpredicted</strong> (predicted was higher than actual).
          <br>
          &bull; <strong>e<sub>i</sub> = 0:</strong> Perfect exact prediction.
        </p>
      </div>

      <h3>Why We Cannot Simply Sum Raw Errors</h3>
      <p>
        If a model overpredicts one house by $20,000 (e<sub>1</sub> = -$20,000) and underpredicts another by $20,000 (e<sub>2</sub> = +$20,000), the sum of raw errors is:
      </p>
      <div class="math-box">
        (-20,000) + (+20,000) = 0
      </div>
      <p>
        The positive and negative errors cancel out completely, falsely suggesting zero total error! To prevent this cancellation, regression metrics transform errors using either <strong>absolute values (|e|)</strong> or <strong>squares (e&sup2;)</strong>.
      </p>

      <!-- FIGURE 15.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 15.1 &bull; Actual vs Predicted Values and Residual Distance</span>
          <span class="visual-tag">Regression Diagnostics</span>
        </div>
        __SVG_REGRESSION_RESIDUALS__
        <div class="visual-caption">
          Figure 15.1: Regression evaluation geometry on 5 house price samples. Points on the diagonal 45-degree line have zero error; vertical line segments depict positive residuals (underprediction) and negative residuals (overprediction).
        </div>
      </div>

      <h3>Standard Worked Example: 5 Houses</h3>
      <p>
        We will use this exact 5-house valuation dataset to compute and compare MAE, MSE, RMSE, and R&sup2; step by step:
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>House ID</th>
              <th>Actual Price (y)</th>
              <th>Predicted Price (&#375;)</th>
              <th>Residual Error (y &minus; &#375;)</th>
              <th>Absolute Error |y &minus; &#375;|</th>
              <th>Squared Error (y &minus; &#375;)&sup2;</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>House #1</strong></td>
              <td>200k</td>
              <td>210k</td>
              <td>-$10k (Overpredicted)</td>
              <td>10k</td>
              <td>100 (k&sup2;)</td>
            </tr>
            <tr>
              <td><strong>House #2</strong></td>
              <td>250k</td>
              <td>240k</td>
              <td>+$10k (Underpredicted)</td>
              <td>10k</td>
              <td>100 (k&sup2;)</td>
            </tr>
            <tr>
              <td><strong>House #3</strong></td>
              <td>300k</td>
              <td>320k</td>
              <td>-$20k (Overpredicted)</td>
              <td>20k</td>
              <td>400 (k&sup2;)</td>
            </tr>
            <tr>
              <td><strong>House #4</strong></td>
              <td>350k</td>
              <td>340k</td>
              <td>+$10k (Underpredicted)</td>
              <td>10k</td>
              <td>100 (k&sup2;)</td>
            </tr>
            <tr>
              <td><strong>House #5</strong></td>
              <td>400k</td>
              <td>420k</td>
              <td>-$20k (Overpredicted)</td>
              <td>20k</td>
              <td>400 (k&sup2;)</td>
            </tr>
            <tr style="font-weight:700; background:#EEF2FF;">
              <td>Sum (&sum;)</td>
              <td>1,500k</td>
              <td>1,530k</td>
              <td>-$30k</td>
              <td><strong>70k</strong></td>
              <td><strong>1,100 (k&sup2;)</strong></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 16 -->
    <section id="sec-16" class="content-section">
      <span class="section-tag">Section 16</span>
      <h2 class="section-title">Mean Absolute Error (MAE)</h2>
      <p class="section-intro">
        Mean Absolute Error answers the simplest intuitive question: "On average, by how much was the model off in actual real-world units?"
      </p>

      <h3>Formula and Technical Definition</h3>
      <div class="math-box">
        MAE = (1 / n) &times; &sum;<sub>i=1</sub><sup>n</sup> |y<sub>i</sub> &minus; &#375;<sub>i</sub>|
        <div class="math-legend">
          &bull; <strong>n:</strong> Number of evaluated observations (here n = 5)<br>
          &bull; <strong>y<sub>i</sub>:</strong> True actual target value for sample i<br>
          &bull; <strong>&#375;<sub>i</sub>:</strong> Model's predicted target value<br>
          &bull; <strong>|y<sub>i</sub> &minus; &#375;<sub>i</sub>|:</strong> Absolute distance between truth and prediction
        </div>
      </div>

      <p>
        <strong>Step-by-Step Manual Calculation:</strong>
      </p>
      <ol>
        <li>Calculate absolute errors: $|200 - 210| = 10, $|250 - 240| = 10, $|300 - 320| = 20, $|350 - 340| = 10, $|400 - 420| = 20.</li>
        <li>Sum the absolute errors: $10 + 10 + 20 + 10 + 20 = 70.</li>
        <li>Divide by <em>n</em> = 5:</li>
      </ol>
      <div class="math-box">
        MAE = 70 / 5 = 14.00 &nbsp;($14,000)
      </div>

      <h3>Key Characteristics of MAE</h3>
      <ul>
        <li><strong>Directly Interpretable:</strong> MAE is expressed in the <em>exact same physical units</em> as the target variable (dollars, kilograms, Celsius).</li>
        <li><strong>Linear Penalty:</strong> An error of $20,000 is penalized exactly twice as much as an error of $10,000.</li>
        <li><strong>Robust to Outliers:</strong> Because errors are not squared, a single extreme outlier will not unduly distort the overall metric.</li>
      </ul>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; MAE Calculation</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>import numpy as np
from sklearn.metrics import mean_absolute_error

y_reg_true = np.array([200.0, 250.0, 300.0, 350.0, 400.0])
y_reg_pred = np.array([210.0, 240.0, 320.0, 340.0, 420.0])

mae = mean_absolute_error(y_reg_true, y_reg_pred)
print(f"MAE: {mae:.2f} (k)")  # Output: 14.00 ($14,000)</code></pre>
      </div>
    </section>

    <!-- SECTION 17 -->
    <section id="sec-17" class="content-section">
      <span class="section-tag">Section 17</span>
      <h2 class="section-title">Mean Squared Error (MSE)</h2>
      <p class="section-intro">
        Mean Squared Error heavily penalizes large blunders by squaring each residual error before averaging.
      </p>

      <h3>Formula and Technical Definition</h3>
      <div class="math-box">
        MSE = (1 / n) &times; &sum;<sub>i=1</sub><sup>n</sup> (y<sub>i</sub> &minus; &#375;<sub>i</sub>)&sup2;
      </div>

      <p>
        <strong>Step-by-Step Manual Calculation:</strong>
      </p>
      <ol>
        <li>Calculate squared errors: (-10)&sup2; = 100, (+10)&sup2; = 100, (-20)&sup2; = 400, (+10)&sup2; = 100, (-20)&sup2; = 400.</li>
        <li>Sum the squared errors: $100 + 100 + 400 + 100 + 400 = 1,100.</li>
        <li>Divide by <em>n</em> = 5:</li>
      </ol>
      <div class="math-box">
        MSE = 1,100 / 5 = 220.00 &nbsp;(k&sup2;)
      </div>

      <h3>Why Square the Errors?</h3>
      <ul>
        <li><strong>Differentiability:</strong> The quadratic parabola e&sup2;$ is smoothly differentiable everywhere with a continuous gradient, making MSE the standard loss function for Gradient Descent and Ordinary Least Squares (OLS) optimization.</li>
        <li><strong>Harsh Penalty for Big Mistakes:</strong> Doubling the error <em>quadruples</em> the penalty:
          <br>&bull; Error = 10 &rarr; Penalty = 100
          <br>&bull; Error = 20 &rarr; Penalty = 400 (4&times; higher for only 2&times; larger error!)
          <br>&bull; Error = 50 &rarr; Penalty = 2,500 (25&times; higher!)
        </li>
      </ul>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          The Major Limitation of MSE: Squared Units
        </div>
        <p>
          MSE is expressed in <strong>squared units</strong> (e.g., dollars squared, square degrees Celsius). An MSE of "220 million dollars squared" is practically impossible to communicate meaningfully to non-technical stakeholders or executive leadership.
        </p>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; MSE Calculation</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_reg_true, y_reg_pred)
print(f"MSE: {mse:.2f} (k^2)")  # Output: 220.00</code></pre>
      </div>
    </section>

    <!-- SECTION 18 -->
    <section id="sec-18" class="content-section">
      <span class="section-tag">Section 18</span>
      <h2 class="section-title">Root Mean Squared Error (RMSE)</h2>
      <p class="section-intro">
        Root Mean Squared Error provides the best of both worlds: it penalizes large errors disproportionately like MSE, yet expresses the result in original target units like MAE.
      </p>

      <h3>Formula and Technical Definition</h3>
      <div class="math-box">
        RMSE = &radic;(MSE) = &radic;[ (1 / n) &times; &sum;<sub>i=1</sub><sup>n</sup> (y<sub>i</sub> &minus; &#375;<sub>i</sub>)&sup2; ]
      </div>

      <p>
        <strong>Step-by-Step Manual Calculation:</strong>
      </p>
      <div class="math-box">
        RMSE = &radic;(220.00) = 14.8324 &nbsp;($14,832.40)
      </div>

      <h3>Why RMSE &ge; MAE Always Holds</h3>
      <p>
        Notice that in our example, <strong>RMSE ($14.83k) is greater than MAE ($14.00k)</strong>.
        Mathematically, by the Cauchy-Schwarz inequality, <strong>RMSE is always greater than or equal to MAE</strong>:
      </p>
      <div class="math-box">
        RMSE &ge; MAE
      </div>
      <p>
        RMSE equals MAE <em>if and only if all individual errors have the exact same absolute magnitude</em>. The wider the gap between RMSE and MAE, the more variance and extreme outlier errors exist in the model's predictions.
      </p>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; RMSE Calculation</span>
          <span>Verified Execution (scikit-learn 1.4+)</span>
        </div>
        <pre><code>from sklearn.metrics import root_mean_squared_error

# In scikit-learn 1.4+, use root_mean_squared_error directly:
rmse = root_mean_squared_error(y_reg_true, y_reg_pred)
print(f"RMSE: {rmse:.4f} (k)")  # Output: 14.8324 ($14,832.40)

# Alternative compatible with older scikit-learn:
# rmse = np.sqrt(mean_squared_error(y_reg_true, y_reg_pred))</code></pre>
      </div>
    </section>

    <!-- SECTION 19 -->
    <section id="sec-19" class="content-section">
      <span class="section-tag">Section 19</span>
      <h2 class="section-title">MAE vs. MSE vs. RMSE: Complete Comparative Analysis</h2>
      <p class="section-intro">
        Understanding how error magnitude impacts each metric allows you to choose the exact right evaluation metric for your engineering problem.
      </p>

      <!-- FIGURE 19.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 19.1 &bull; Linear vs Quadratic Penalty: Absolute vs Squared Error Growth</span>
          <span class="visual-tag">Penalty Curve Dynamics</span>
        </div>
        __SVG_MAE_VS_MSE_CURVE__
        <div class="visual-caption">
          Figure 19.1: Comparing error penalty growth. Absolute error (MAE) scales linearly with error size (y = |e|). Squared error (MSE) explodes quadratically (y = e&sup2;$), heavily punishing large prediction deviations.
        </div>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Mean Absolute Error (MAE)</th>
              <th>Mean Squared Error (MSE)</th>
              <th>Root Mean Squared Error (RMSE)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Mathematical Formula</strong></td>
              <td><code>(1/n) &sum; |y - &#375;|</code></td>
              <td><code>(1/n) &sum; (y - &#375;)&sup2;</code></td>
              <td><code>&radic;[ (1/n) &sum; (y - &#375;)&sup2; ]</code></td>
            </tr>
            <tr>
              <td><strong>Physical Units</strong></td>
              <td>Same as Target (e.g., $)</td>
              <td>Squared Target Units (e.g., &sup2;)</td>
              <td>Same as Target (e.g., $)</td>
            </tr>
            <tr>
              <td><strong>Penalty Growth</strong></td>
              <td>Linear (constant slope)</td>
              <td>Quadratic (steeply compounding)</td>
              <td>Quadratic before square root</td>
            </tr>
            <tr>
              <td><strong>Sensitivity to Outliers</strong></td>
              <td>Low (robust, median-seeking)</td>
              <td>Extremely High (distorted by blunders)</td>
              <td>High (sensitive to large errors)</td>
            </tr>
            <tr>
              <td><strong>Executive Interpretability</strong></td>
              <td>Highest ("average dollar error")</td>
              <td>Lowest (counter-intuitive units)</td>
              <td>High ("typical root error")</td>
            </tr>
            <tr>
              <td><strong>Mathematical Optimization</strong></td>
              <td>Non-smooth derivative at zero</td>
              <td>Smooth, convex, differentiable</td>
              <td>Smooth, convex, differentiable</td>
            </tr>
            <tr>
              <td><strong>Ideal Application</strong></td>
              <td>Continuous metrics with noisy outliers where typical performance matters</td>
              <td>Model loss training functions in neural networks and linear models</td>
              <td>Evaluation when large prediction errors incur severe financial or safety penalties</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 20 -->
    <section id="sec-20" class="content-section">
      <span class="section-tag">Section 20</span>
      <h2 class="section-title">Coefficient of Determination (R&sup2; Score)</h2>
      <p class="section-intro">
        While MAE and RMSE tell you the absolute scale of errors, the R&sup2; score tells you what proportion of the variance in the target variable is explained by your model compared to a naive baseline.
      </p>

      <h3>Formula and Decomposition of Sum of Squares</h3>
      <div class="math-box">
        R&sup2; = 1 &minus; [ &sum;<sub>i=1</sub><sup>n</sup> (y<sub>i</sub> &minus; &#375;<sub>i</sub>)&sup2; ] / [ &sum;<sub>i=1</sub><sup>n</sup> (y<sub>i</sub> &minus; y&#772;)&sup2; ] = 1 &minus; (SS<sub>res</sub> / SS<sub>tot</sub>)
        <div class="math-legend">
          &bull; <strong>y&#772; (y-bar):</strong> Mean of the actual ground-truth target values<br>
          &bull; <strong>SS<sub>res</sub> (Sum of Squared Residuals):</strong> Unexplained error variance of the model<br>
          &bull; <strong>SS<sub>tot</sub> (Total Sum of Squares):</strong> Total variance inherent in the target data around its mean
        </div>
      </div>

      <!-- FIGURE 20.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 20.1 &bull; R&sup2; Score: Model Residuals vs Mean Baseline Variance</span>
          <span class="visual-tag">Variance Explained Geometry</span>
        </div>
        __SVG_R2_BASELINE__
        <div class="visual-caption">
          Figure 20.1: Visualizing R&sup2;. Total variance SS<sub>tot</sub> measures how points scatter around the horizontal target mean line (y&#772; = 300). Residual variance SS<sub>res</sub> measures scatter around model predictions. R&sup2; measures the percentage reduction in variance.
        </div>
      </div>

      <h3>Step-by-Step Manual Calculation on Our 5 Houses</h3>
      <ol>
        <li>Calculate target mean: y&#772; = (200 + 250 + 300 + 350 + 400) / 5 = 1,500 / 5 = 300.0.</li>
        <li>Compute deviations from mean (y<sub>i</sub> - y&#772;):
          <br>&bull; (200 - 300) = -100 &rarr; squared = $10,000
          <br>&bull; (250 - 300) = -50 &rarr; squared = $2,500
          <br>&bull; (300 - 300) = 0 &rarr; squared = $0
          <br>&bull; (350 - 300) = +50 &rarr; squared = $2,500
          <br>&bull; (400 - 300) = +100 &rarr; squared = $10,000
        </li>
        <li>Sum of total squares: SS<sub>tot</sub> = 10,000 + 2,500 + 0 + 2,500 + 10,000 = 25,000.</li>
        <li>Sum of squared residuals: SS<sub>res</sub> = 1,100 (from Section 17).</li>
        <li>Compute R&sup2;:</li>
      </ol>
      <div class="math-box">
        R&sup2; = 1 &minus; (1,100 / 25,000) = 1 &minus; 0.0440 = 0.9560 &nbsp;(95.60%)
      </div>
      <p>
        <strong>Interpretation:</strong> The model accounts for <strong>95.60% of the variance</strong> in house prices. Only 4.40% of the variance remains unexplained residual error.
      </p>

      <h3>How to Interpret R&sup2; Values</h3>
      <ul>
        <li><strong>R&sup2; = 1.0:</strong> Perfect model. SS<sub>res</sub> = 0. The model predicts every single test observation with 100% precision.</li>
        <li><strong>R&sup2; = 0.0:</strong> The model performs exactly as well as a "dumb" baseline that always predicts the mean value y&#772;$.</li>
        <li><strong>R&sup2; &lt; 0.0 (Negative R&sup2;):</strong> The model performs <strong>worse than predicting the mean!</strong> Its predictions are so wildly erratic that simply guessing the average of historical data would yield lower total squared error.</li>
      </ul>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Common Myth: "R&sup2; Can Never Be Negative"
        </div>
        <p>
          In linear regression on training data with an intercept, $0 &le; R&sup2; &le; 1. However, <strong>on an unseen test set or with nonlinear models, R&sup2; can absolutely be negative!</strong> If your test R&sup2; is negative, your model has severely overfitted or completely failed to generalize.
        </p>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; R&sup2; Score Calculation</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>from sklearn.metrics import r2_score

r2 = r2_score(y_reg_true, y_reg_pred)
print(f"R-squared (R2): {r2:.4f}")  # Output: 0.9560 (95.60%)</code></pre>
      </div>
    </section>

    <!-- SECTION 21 -->
    <section id="sec-21" class="content-section">
      <span class="section-tag">Section 21</span>
      <h2 class="section-title">Residuals and Residual Plots</h2>
      <p class="section-intro">
        Summary metrics like RMSE and R&sup2; condense performance into single numbers. Residual plots expose hidden systematic flaws, curvature, and changing variance that metrics fail to detect.
      </p>

      <h3>Diagnostic Power of Residual Analysis</h3>
      <p>
        A <strong>residual plot</strong> displays the model's residuals (e<sub>i</sub> = y<sub>i</sub> &minus; &#375;<sub>i</sub>) on the vertical Y-axis plotted against the predicted values (&#375;<sub>i</sub>) on the horizontal X-axis, with a reference line at e = 0.
      </p>

      <!-- FIGURE 21.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 21.1 &bull; Residual Plot Patterns: Healthy vs Nonlinear vs Heteroscedastic</span>
          <span class="visual-tag">Regression Model Diagnostics</span>
        </div>
        __SVG_RESIDUAL_PLOTS__
        <div class="visual-caption">
          Figure 21.1: Residual diagnostic patterns. (A) Healthy random scatter around zero (homoscedasticity). (B) U-shaped curved pattern indicating missing nonlinear terms or polynomials. (C) Funnel-shaped fanning indicating non-constant error variance (heteroscedasticity).
        </div>
      </div>

      <h3>Interpreting Residual Patterns</h3>
      <ol>
        <li>
          <strong>Pattern A &mdash; Random Uniform Scatter (Ideal):</strong>
          <br>Residuals form an unstructured cloud symmetrically distributed above and below zero across all predicted ranges. The model has captured all systematic trends; only pure random noise remains.
        </li>
        <li>
          <strong>Pattern B &mdash; Curvature / U-Shape (Nonlinear Underfitting):</strong>
          <br>The residuals bow into an arch or parabola. This proves that the underlying relationship is nonlinear, but the engineer fitted an overly simplistic linear model. <em>Remedy:</em> Add polynomial features or switch to tree-based / nonlinear models.
        </li>
        <li>
          <strong>Pattern C &mdash; Funnel / Fan Shape (Heteroscedasticity):</strong>
          <br>Errors start tiny for small predictions and fan out into huge spreads for large predictions (e.g., predicting prices of multi-million dollar luxury estates has far higher dollar variance than starter apartments). <em>Remedy:</em> Apply a logarithmic or power transformation to the target (<em>y</em>).
        </li>
      </ol>
    </section>
"""
