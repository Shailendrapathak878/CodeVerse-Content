"""
Module: topic9_part2.py
Contains HTML for Sections 6 to 10 of Topic 9: Linear Regression.
"""

from scratch.topic9_svgs import (
    SVG_RESIDUAL_LINES,
    SVG_LOSS_FUNCTION_COMPARISON,
    SVG_OLS_CALCULATION_ENGINE,
    SVG_GRADIENT_DESCENT_CURVE
)

PART2_HTML = f"""
  <!-- SECTION 06: ACTUAL VALUES, PREDICTED VALUES AND RESIDUALS -->
  <section id="sec-06" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 06</span>
      <h2 class="section-title">Actual Values, Predicted Values and Residuals</h2>
    </div>
    <p class="section-intro">
      At the heart of regression analysis lies the concept of a <strong>residual</strong>&mdash;the difference between what actually occurred in reality and what our mathematical model estimated.
    </p>

    <div class="formula-card">
      <div class="formula-title">Mathematical Definition: Individual Sample Residual</div>
      <div class="formula-box">e&#7522; = y&#7522; - &#375;&#7522;</div>
      <div class="formula-desc">
        Where <strong>y&#7522;</strong> is the observed ground-truth value, <strong>&#375;&#7522;</strong> is the model's predicted value, and <strong>e&#7522;</strong> is the signed residual error for sample <em>i</em>.
      </div>
    </div>

    <!-- FIGURE 9.6: RESIDUAL LINES -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_RESIDUAL_LINES}
      </div>
      <div class="diagram-caption">Figure 9.6: Visualizing residuals as vertical differences: Dashed red segments show the exact error distance between observed points and the fitted regression model.</div>
    </div>

    <h3>Interpreting the Sign of the Residual</h3>
    <ul>
      <li><strong>Positive Residual (e&#7522; &gt; 0):</strong> The actual observed value lies <em>above</em> the regression line (<code>y&#7522; &gt; &#375;&#7522;</code>). The model <strong>underestimated</strong> reality.</li>
      <li><strong>Negative Residual (e&#7522; &lt; 0):</strong> The actual observed value lies <em>below</em> the regression line (<code>y&#7522; &lt; &#375;&#7522;</code>). The model <strong>overestimated</strong> reality.</li>
      <li><strong>Zero Residual (e&#7522; = 0):</strong> The observation lies exactly on the regression line. The prediction was 100% accurate.</li>
    </ul>

    <h3>Step-by-Step Worked Residual Table (4 Samples)</h3>
    <p>
      Consider four observations where the fitted model equation is <code>&#375; = 2.1x + 0.8</code>:
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Sample #</th>
            <th>Input (x)</th>
            <th>Actual Value (y)</th>
            <th>Predicted (&#375; = 2.1x + 0.8)</th>
            <th>Residual (e = y - &#375;)</th>
            <th>Model Evaluation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Sample 1</strong></td>
            <td><code>x&#8321; = 1.0</code></td>
            <td><code>y&#8321; = 3.0</code></td>
            <td><code>&#375;&#8321; = 2.1(1.0) + 0.8 = 2.90</code></td>
            <td><code>3.0 - 2.90 = +0.10</code></td>
            <td>Underestimated by 0.10 units</td>
          </tr>
          <tr>
            <td><strong>Sample 2</strong></td>
            <td><code>x&#8322; = 2.0</code></td>
            <td><code>y&#8322; = 5.0</code></td>
            <td><code>&#375;&#8322; = 2.1(2.0) + 0.8 = 5.00</code></td>
            <td><code>5.0 - 5.00 = 0.00</code></td>
            <td><strong>Exact perfect hit!</strong></td>
          </tr>
          <tr>
            <td><strong>Sample 3</strong></td>
            <td><code>x&#8323; = 3.0</code></td>
            <td><code>y&#8323; = 8.0</code></td>
            <td><code>&#375;&#8323; = 2.1(3.0) + 0.8 = 7.10</code></td>
            <td><code>8.0 - 7.10 = +0.90</code></td>
            <td>Underestimated by 0.90 units</td>
          </tr>
          <tr>
            <td><strong>Sample 4</strong></td>
            <td><code>x&#8324; = 4.0</code></td>
            <td><code>y&#8324; = 9.0</code></td>
            <td><code>&#375;&#8324; = 2.1(4.0) + 0.8 = 9.20</code></td>
            <td><code>9.0 - 9.20 = -0.20</code></td>
            <td>Overestimated by 0.20 units</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-def">
      <div class="card-title"><span>&#128207;</span> Why Are Residuals Strictly Vertical in Ordinary Least Squares?</div>
      <p>
        In basic geometry, the shortest distance from a point to a line is the perpendicular segment. However, in linear regression, <strong>residuals are strictly vertical</strong> along the y-axis.
      </p>
      <p>
        Why? Because in supervised learning, our objective is to predict target <code>y</code> given a fixed, known feature <code>x</code>. We assume the input <code>x</code> is measured without error; our only uncertainty lies in the output <code>y</code>. Therefore, the algorithm penalizes vertical discrepancy exclusively!
      </p>
    </div>
  </section>

  <!-- SECTION 07: LOSS FUNCTIONS AND MEAN SQUARED ERROR -->
  <section id="sec-07" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 07</span>
      <h2 class="section-title">Loss Functions and Mean Squared Error</h2>
    </div>
    <p class="section-intro">
      To compare millions of candidate lines, an algorithm cannot inspect a list of individual residuals manually. It requires a single mathematical number&mdash;a <strong>Loss Function</strong> (or Cost Function)&mdash;that scores the overall badness of the model's predictions.
    </p>

    <div class="formula-card">
      <div class="formula-title">Core Regression Loss: Mean Squared Error (MSE)</div>
      <div class="formula-box">MSE = (1 / n) &times; &Sigma;&#7522;&#61105;&#8321;&#7519; (y&#7522; - &#375;&#7522;)&#178;</div>
      <div class="formula-desc">
        Where <strong>n</strong> is the number of samples, <strong>y&#7522;</strong> is actual value, and <strong>&#375;&#7522;</strong> is prediction. MSE computes the average squared vertical error.
      </div>
    </div>

    <!-- FIGURE 9.7: LOSS FUNCTION COMPARISON -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_LOSS_FUNCTION_COMPARISON}
      </div>
      <div class="diagram-caption">Figure 9.7: Comparing loss penalties: Mean Squared Error (quadratic) punishes large outlier errors far more aggressively than Mean Absolute Error (linear).</div>
    </div>

    <h3>Step-by-Step Manual Loss Calculation</h3>
    <p>
      Using the 4 observations from Section 6, let us manually calculate the complete error metrics:
    </p>
    <ol>
      <li><strong>Compute individual residuals (e&#7522;):</strong> <code>[+0.10, 0.00, +0.90, -0.20]</code></li>
      <li><strong>Square each residual (e&#7522;&#178;):</strong>
        <ul>
          <li><code>(+0.10)&#178; = 0.0100</code></li>
          <li><code>(0.00)&#178;  = 0.0000</code></li>
          <li><code>(+0.90)&#178; = 0.8100</code></li>
          <li><code>(-0.20)&#178; = 0.0400</code></li>
        </ul>
      </li>
      <li><strong>Sum of Squared Errors (SSE):</strong> <code>0.0100 + 0.0000 + 0.8100 + 0.0400 = 0.8600</code></li>
      <li><strong>Mean Squared Error (MSE):</strong> <code>SSE / n = 0.8600 / 4 = 0.2150</code></li>
      <li><strong>Root Mean Squared Error (RMSE):</strong> <code>&radic;MSE = &radic;0.2150 = 0.4637</code></li>
      <li><strong>Mean Absolute Error (MAE):</strong> <code>(|0.10| + |0.00| + |0.90| + |-0.20|) / 4 = 1.20 / 4 = 0.3000</code></li>
    </ol>

    <!-- Metrics Table -->
    <h3>Why Do We Need Both MSE, RMSE, and MAE?</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Metric</th>
            <th>Formula</th>
            <th>Units</th>
            <th>Key Advantage &amp; Limitation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mean Squared Error (MSE)</strong></td>
            <td><code>(1/n) &Sigma; e&#7522;&#178;</code></td>
            <td>Squared Target Units (e.g. <code>$&#178;</code>)</td>
            <td>Mathematically smooth &amp; differentiable; but units are squared and non-intuitive to explain to non-technical stakeholders.</td>
          </tr>
          <tr>
            <td><strong>Root Mean Squared Error (RMSE)</strong></td>
            <td><code>&radic;MSE</code></td>
            <td>Original Target Units (e.g. <code>$</code>)</td>
            <td>Restores original units for easy business interpretation; still heavily sensitive to extreme outlier errors.</td>
          </tr>
          <tr>
            <td><strong>Mean Absolute Error (MAE)</strong></td>
            <td><code>(1/n) &Sigma; |e&#7522;|</code></td>
            <td>Original Target Units (e.g. <code>$</code>)</td>
            <td>Robust to outliers; measures average absolute distance. Not smooth at e = 0, making calculus optimization slightly harder.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> Why Can't We Just Minimize the Simple Sum of Errors (&Sigma; e&#7522;)?</div>
      <p>
        If we don't square or take the absolute value, positive residuals and negative residuals cancel each other out! A model could make a <code>+1,000</code> error on sample 1 and a <code>-1,000</code> error on sample 2. The simple sum would be <code>+1000 + (-1000) = 0</code>, declaring the model "flawless" despite massive errors on every prediction. Squaring ensures that every mistake contributes a positive penalty.
      </p>
    </div>
  </section>

  <!-- SECTION 08: THE ORDINARY LEAST SQUARES OBJECTIVE -->
  <section id="sec-08" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 08</span>
      <h2 class="section-title">The Ordinary Least Squares Objective</h2>
    </div>
    <p class="section-intro">
      <strong>Ordinary Least Squares (OLS)</strong> is the standard analytical formulation for fitting a linear regression model. It mathematically determines the optimal slope (<code>&beta;&#8321;</code>) and intercept (<code>&beta;&#8320;</code>) by solving for the exact point where the derivative of the squared error loss is zero.
    </p>

    <!-- FIGURE 9.8: OLS CALCULATION ENGINE -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_OLS_CALCULATION_ENGINE}
      </div>
      <div class="diagram-caption">Figure 9.8: The Ordinary Least Squares calculation engine: Closed-form Normal Equations solve directly for the optimal slope and intercept using covariance and variance.</div>
    </div>

    <div class="formula-card">
      <div class="formula-title">Analytical Closed-Form Formulas for Simple Linear Regression</div>
      <div class="formula-box">&beta;&#8321; = &Sigma;(x&#7522; - x&#772;)(y&#7522; - y&#772;) / &Sigma;(x&#7522; - x&#772;)&#178; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &beta;&#8320; = y&#772; - &beta;&#8321; &times; x&#772;</div>
      <div class="formula-desc">
        Where <strong>x&#772;</strong> and <strong>y&#772;</strong> are the sample arithmetic means of feature X and target Y.
      </div>
    </div>

    <h3>Complete Worked Numerical Example from First Principles</h3>
    <p>
      Consider a small dataset with <code>n = 5</code> observations:
      <br><code>X = [1.0, 2.0, 3.0, 4.0, 5.0]</code>
      <br><code>Y = [2.0, 3.0, 5.0, 7.0, 8.0]</code>
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>i</th>
            <th>x&#7522;</th>
            <th>y&#7522;</th>
            <th>(x&#7522; - x&#772;)</th>
            <th>(y&#7522; - y&#772;)</th>
            <th>(x&#7522; - x&#772;)(y&#7522; - y&#772;)</th>
            <th>(x&#7522; - x&#772;)&#178;</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>1.0</td>
            <td>2.0</td>
            <td>1.0 - 3.0 = -2.0</td>
            <td>2.0 - 5.0 = -3.0</td>
            <td>(-2.0)(-3.0) = +6.0</td>
            <td>(-2.0)&#178; = 4.0</td>
          </tr>
          <tr>
            <td>2</td>
            <td>2.0</td>
            <td>3.0</td>
            <td>2.0 - 3.0 = -1.0</td>
            <td>3.0 - 5.0 = -2.0</td>
            <td>(-1.0)(-2.0) = +2.0</td>
            <td>(-1.0)&#178; = 1.0</td>
          </tr>
          <tr>
            <td>3</td>
            <td>3.0</td>
            <td>5.0</td>
            <td>3.0 - 3.0 = 0.0</td>
            <td>5.0 - 5.0 = 0.0</td>
            <td>(0.0)(0.0) = 0.0</td>
            <td>(0.0)&#178; = 0.0</td>
          </tr>
          <tr>
            <td>4</td>
            <td>4.0</td>
            <td>7.0</td>
            <td>4.0 - 3.0 = +1.0</td>
            <td>7.0 - 5.0 = +2.0</td>
            <td>(+1.0)(+2.0) = +2.0</td>
            <td>(+1.0)&#178; = 1.0</td>
          </tr>
          <tr>
            <td>5</td>
            <td>5.0</td>
            <td>8.0</td>
            <td>5.0 - 3.0 = +2.0</td>
            <td>8.0 - 5.0 = +3.0</td>
            <td>(+2.0)(+3.0) = +6.0</td>
            <td>(+2.0)&#178; = 4.0</td>
          </tr>
          <tr>
            <td><strong>Sum</strong></td>
            <td><strong>&Sigma;x = 15.0</strong></td>
            <td><strong>&Sigma;y = 25.0</strong></td>
            <td>x&#772; = 15.0/5 = <strong>3.0</strong></td>
            <td>y&#772; = 25.0/5 = <strong>5.0</strong></td>
            <td><strong>&Sigma; = +16.0 (Numerator)</strong></td>
            <td><strong>&Sigma; = 10.0 (Denominator)</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>
      Now calculate the parameters:
      <br>1. <strong>Optimal Slope (&beta;&#8321;):</strong> <code>16.0 / 10.0 = 1.600</code>
      <br>2. <strong>Optimal Intercept (&beta;&#8320;):</strong> <code>y&#772; - &beta;&#8321;x&#772; = 5.0 - (1.600 &times; 3.0) = 5.0 - 4.8 = 0.200</code>
      <br>3. <strong>Final Fitted Equation:</strong> <code>&#375; = 0.200 + 1.600 &times; x</code>
    </p>
    <p>
      Executing <code>LinearRegression().fit(X, y)</code> in Python produces the exact same values: <code>coef_ = 1.6000</code> and <code>intercept_ = 0.2000</code>.
    </p>
  </section>

  <!-- SECTION 09: GRADIENT DESCENT: HOW PARAMETERS CAN BE LEARNED -->
  <section id="sec-09" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 09</span>
      <h2 class="section-title">Gradient Descent: How Parameters Can Be Learned</h2>
    </div>
    <p class="section-intro">
      While Ordinary Least Squares solves linear regression analytically in one step using matrix inversion, this formula becomes computationally prohibitive when datasets contain millions of rows or hundreds of thousands of features. <strong>Gradient Descent</strong> provides an iterative optimization alternative that powers modern large-scale machine learning and deep neural networks.
    </p>

    <!-- FIGURE 9.9: GRADIENT DESCENT -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_GRADIENT_DESCENT_CURVE}
      </div>
      <div class="diagram-caption">Figure 9.9: Gradient Descent optimization: Iteratively walking down the convex MSE loss surface along the negative gradient until converging at the global minimum.</div>
    </div>

    <h3>The Mountain Hiker Analogy</h3>
    <p>
      Imagine you are hiking down a foggy mountain shrouded in thick mist. You cannot see the village at the bottom of the valley, but under your hiking boots, you can feel the slope of the ground:
    </p>
    <ul>
      <li><strong>Gradient:</strong> The steepness and direction of the slope under your feet.</li>
      <li><strong>Negative Gradient:</strong> The direction of steepest descent (downhill).</li>
      <li><strong>Learning Rate (&alpha;):</strong> The size of the stride you take on each step.</li>
      <li><strong>Convergence:</strong> Arriving at flat ground in the valley basin where slope = 0.</li>
    </ul>

    <div class="formula-card">
      <div class="formula-title">Gradient Descent Parameter Update Equations</div>
      <div class="formula-box">w_new = w_old - &alpha; &times; (&part;J / &part;w) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b_new = b_old - &alpha; &times; (&part;J / &part;b)</div>
      <div class="formula-desc">
        Where <strong>J</strong> is the MSE loss function, <strong>&alpha;</strong> is the learning rate (step size), and <strong>&part;J/&part;w</strong> is the partial derivative of loss with respect to weight.
      </div>
    </div>

    <h3>Partial Derivatives for Mean Squared Error</h3>
    <p>
      Using simple calculus (the power rule and chain rule), the gradients of MSE with respect to <code>w</code> and <code>b</code> are:
    </p>
    <ul>
      <li><code>&part;J / &part;w = - (2 / n) &Sigma; x&#7522; &times; (y&#7522; - &#375;&#7522;)</code></li>
      <li><code>&part;J / &part;b = - (2 / n) &Sigma; (y&#7522; - &#375;&#7522;)</code></li>
    </ul>

    <h3>The Critical Role of Learning Rate (&alpha;)</h3>
    <ul>
      <li><strong>Learning Rate Too Small (&alpha; = 0.0001):</strong> Optimization moves at a snail's pace, requiring hundreds of thousands of epochs to converge.</li>
      <li><strong>Learning Rate Too Large (&alpha; = 2.5):</strong> Steps overshoot the valley bottom completely, causing the loss to diverge toward infinity (NaN explosion).</li>
      <li><strong>Just Right (&alpha; = 0.05):</strong> The model smoothly and rapidly descends the bowl, converging to within <code>0.01</code> of the analytical OLS solution in under 100 epochs.</li>
    </ul>
  </section>

  <!-- SECTION 10: SIMPLE LINEAR REGRESSION -->
  <section id="sec-10" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 10</span>
      <h2 class="section-title">Simple Linear Regression</h2>
    </div>
    <p class="section-intro">
      <strong>Simple Linear Regression</strong> models the direct bivariate relationship between a single numerical input feature and a continuous target variable.
    </p>

    <div class="card card-def">
      <div class="card-title"><span>&#128202;</span> Python Implementation with Scikit-Learn</div>
      <p>
        In Scikit-Learn, simple linear regression is performed using the <code>LinearRegression</code> estimator:
      </p>
      <div class="code-block">
        <div class="code-header">
          <span class="code-title">simple_linear_regression.py</span>
          <span class="code-lang">python</span>
        </div>
        <pre><code>from sklearn.linear_model import LinearRegression

# Instantiate estimator
model = LinearRegression()

# X must be a 2D matrix (samples x features), y is a 1D vector
model.fit(X_train[['Area_SqFt']], y_train)

# Inspect learned parameters
slope = model.coef_[0]       # +0.1430 kUSD per sq ft
intercept = model.intercept_ # +55.93 kUSD

print(f"Fitted Model: Price = {{intercept:.2f}} + {{slope:.4f}} * Area")
# Predict on unseen test sample (2,000 sq ft house)
pred_price = model.predict([[2000]])[0] # $341.93k USD</code></pre>
      </div>
    </div>

    <h3>Limitations of Simple Linear Regression</h3>
    <p>
      While simple linear regression provides unmatched human interpretability, it suffers from a fundamental limitation: <strong>omitted variable bias</strong>. In the real world, house price is rarely dictated by square footage alone. A 2,000 sq ft home in a deteriorating condition 30 miles from the city center will sell for far less than an identical 2,000 sq ft renovated home in a prime downtown district. To capture real-world phenomena accurately, we must expand our model to accommodate multiple features simultaneously.
    </p>
  </section>
"""
