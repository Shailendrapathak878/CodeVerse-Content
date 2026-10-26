"""
Module: topic9_part3.py
Contains HTML for Sections 11 to 15 of Topic 9: Linear Regression.
"""

from scratch.topic9_svgs import (
    SVG_SIMPLE_VS_MULTIPLE_REGRESSION,
    SVG_ACTUAL_VS_PREDICTED,
    SVG_RESIDUAL_PLOT,
    SVG_OUTLIER_INFLUENCE
)

PART3_HTML = f"""
  <!-- SECTION 11: MULTIPLE LINEAR REGRESSION -->
  <section id="sec-11" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 11</span>
      <h2 class="section-title">Multiple Linear Regression</h2>
    </div>
    <p class="section-intro">
      In real-world applications, a target outcome is almost never determined by a single isolated factor. <strong>Multiple Linear Regression</strong> extends simple regression by modeling the target as a linear combination of two or more explanatory input features simultaneously.
    </p>

    <div class="formula-card">
      <div class="formula-title">Mathematical Formula: Multiple Linear Regression</div>
      <div class="formula-box">&#375; = &beta;&#8320; + &beta;&#8321;x&#8321; + &beta;&#8322;x&#8322; + &beta;&#8323;x&#8323; + ... + &beta;&#7522;x&#7522;</div>
      <div class="formula-desc">
        Where <strong>p</strong> is the number of features, <strong>x&#119895;</strong> is the <em>j</em>-th feature value, <strong>&beta;&#119895;</strong> is its partial regression coefficient, and <strong>&beta;&#8320;</strong> is the baseline intercept.
      </div>
    </div>

    <!-- FIGURE 9.10: SIMPLE VS MULTIPLE REGRESSION -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_SIMPLE_VS_MULTIPLE_REGRESSION}
      </div>
      <div class="diagram-caption">Figure 9.10: Geometric dimensionality: Simple linear regression fits a 1D line in 2D space; multiple regression fits a 2D plane in 3D space, or a multi-dimensional hyperplane in higher dimensions.</div>
    </div>

    <h3>Interpreting Partial Regression Coefficients: The "Ceteris Paribus" Rule</h3>
    <p>
      In simple regression, the slope represents the total rate of change. In multiple regression, each coefficient <code>&beta;&#119895;</code> has a far more precise meaning:
    </p>

    <div class="card card-def">
      <div class="card-title"><span>&#9878;</span> Definition: Partial Regression Coefficient</div>
      <p>
        The coefficient <code>&beta;&#119895;</code> represents the expected change in target <code>y</code> for a one-unit increase in feature <code>x&#119895;</code>, <strong>holding all other features in the model completely constant</strong> (<em>ceteris paribus</em>).
      </p>
      <p>
        For example, in our fitted house price model:
        <br><code>Price = 59.42 + 0.1376(Area) + 20.44(Bedrooms) - 1.43(Age) - 2.38(Distance)</code>
      </p>
      <ul>
        <li><strong>Bedrooms (+20.44 kUSD):</strong> Adding one additional bedroom is associated with a <code>+$20,440</code> price increase, <em>assuming living area, age, and distance to center remain strictly unchanged</em>.</li>
        <li><strong>Age (-1.43 kUSD/yr):</strong> For each year a house ages, price drops by <code>$1,430</code>, holding size, room count, and location fixed.</li>
      </ul>
    </div>

    <h3>Multicollinearity: When Input Features Collide</h3>
    <p>
      When two or more input features are strongly correlated with each other (e.g. Living Area in sq ft and Total Rooms, or Vehicle Curb Weight and Engine Displacement), <strong>multicollinearity</strong> occurs.
    </p>
    <ul>
      <li><strong>The Problem:</strong> When features move in lockstep, the algorithm cannot isolate the unique mathematical effect of one feature while holding the other constant.</li>
      <li><strong>The Symptom:</strong> The model's overall prediction accuracy and R&#178; score remain high, but individual coefficient estimates become wildly unstable, showing huge standard errors or even nonsensical signs (e.g. positive features flipping negative).</li>
      <li><strong>The Remedy:</strong> Check the correlation matrix (<code>df.corr()</code>), remove redundant duplicate features, or compute Variance Inflation Factors (VIF &lt; 5.0 is healthy).</li>
    </ul>
  </section>

  <!-- SECTION 12: EVALUATION METRICS FOR REGRESSION -->
  <section id="sec-12" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 12</span>
      <h2 class="section-title">Evaluation Metrics for Regression</h2>
    </div>
    <p class="section-intro">
      Because regression predicts continuous numbers, we cannot calculate "accuracy" in the classification sense (e.g., whether a prediction was 100% correct or wrong). Instead, we quantify the <strong>magnitude of error</strong> and the <strong>proportion of variance explained</strong>.
    </p>

    <!-- FIGURE 9.11: ACTUAL VS PREDICTED PLOT -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_ACTUAL_VS_PREDICTED}
      </div>
      <div class="diagram-caption">Figure 9.11: Actual vs Predicted evaluation plot: When a model generalizes well (R&#178; = 0.970), test predictions cluster tightly along the diagonal 45-degree identity line (y = &#375;).</div>
    </div>

    <h3>The 4 Essential Regression Evaluation Metrics</h3>

    <div class="formula-card">
      <div class="formula-title">1. Mean Absolute Error (MAE)</div>
      <div class="formula-box">MAE = (1 / n) &times; &Sigma; |y&#7522; - &#375;&#7522;|</div>
      <div class="formula-desc">
        Average absolute distance between predictions and actual values. Measured in identical units to the target. Highly intuitive and robust to outliers.
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-title">2. Mean Squared Error (MSE)</div>
      <div class="formula-box">MSE = (1 / n) &times; &Sigma; (y&#7522; - &#375;&#7522;)&#178;</div>
      <div class="formula-desc">
        Average squared difference. Penalizes large errors quadratically. Measured in squared target units (e.g. dollars squared).
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-title">3. Root Mean Squared Error (RMSE)</div>
      <div class="formula-box">RMSE = &radic;MSE = &radic;[(1 / n) &times; &Sigma; (y&#7522; - &#375;&#7522;)&#178;]</div>
      <div class="formula-desc">
        Square root of MSE, restoring original target units while retaining the heavy penalty on large outlier mistakes.
      </div>
    </div>

    <div class="formula-card">
      <div class="formula-title">4. Coefficient of Determination (R&#178;)</div>
      <div class="formula-box">R&#178; = 1 - [ &Sigma;(y&#7522; - &#375;&#7522;)&#178; / &Sigma;(y&#7522; - y&#772;)&#178; ] = 1 - [ SS_res / SS_tot ]</div>
      <div class="formula-desc">
        The proportion of total target variance explained by the model compared to a naive baseline that simply predicts the mean y&#772;.
      </div>
    </div>

    <h3>Understanding R&#178; (R-Squared) Values</h3>
    <ul>
      <li><strong>R&#178; = 1.0 (100%):</strong> Perfect fit. Residual sum of squares <code>SS_res = 0</code>. Every prediction matches reality exactly.</li>
      <li><strong>R&#178; = 0.85 (85%):</strong> Strong fit. The model accounts for 85% of the variance in target <code>y</code>; 15% remains unexplained noise.</li>
      <li><strong>R&#178; = 0.0 (0%):</strong> Baseline fit. The model performs no better than predicting the flat average <code>y&#772;</code> for every observation.</li>
      <li><strong>R&#178; &lt; 0 (Negative R&#178;):</strong> Catastrophic failure! On holdout test data, a model can produce negative R&#178; if its predictions have larger total squared errors than simply guessing the training mean!</li>
    </ul>
  </section>

  <!-- SECTION 13: IMPORTANT GRAPHS AND VISUAL LEARNING -->
  <section id="sec-13" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 13</span>
      <h2 class="section-title">Important Graphs and Visual Learning</h2>
    </div>
    <p class="section-intro">
      In machine learning engineering, summary numbers (such as R&#178; or MAE) can easily mask critical model defects. Visualizing data and model behavior is mandatory for reliable diagnostics. Below are the key graphs every regression practitioner must master.
    </p>

    <!-- FIGURE 9.12: RESIDUAL PLOT -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_RESIDUAL_PLOT}
      </div>
      <div class="diagram-caption">Figure 9.12: Residual diagnostic plot: Contrasting an ideal homoscedastic random scatter (left) against an invalid heteroscedastic funnel pattern (right).</div>
    </div>

    <!-- FIGURE 9.13: OUTLIER INFLUENCE -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_OUTLIER_INFLUENCE}
      </div>
      <div class="diagram-caption">Figure 9.13: Outlier leverage and influence: A single anomalous observation with high leverage pulls and rotates the OLS regression line downward.</div>
    </div>

    <h3>The 12 Mandatory Visual Learning Graphs Summary</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Diagnostic Graph</th>
            <th>X-Axis / Y-Axis</th>
            <th>Primary Engineering Insight</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>01</strong></td>
            <td>Scatter Plot of Observations</td>
            <td>Feature X vs Target Y</td>
            <td>Inspects linearity, spread, and natural correlation before modeling.</td>
          </tr>
          <tr>
            <td><strong>02</strong></td>
            <td>Line of Best Fit</td>
            <td>Feature X vs Target Y</td>
            <td>Visualizes the fitted trajectory, slope steepness, and intercept baseline.</td>
          </tr>
          <tr>
            <td><strong>03</strong></td>
            <td>Comparing Candidate Lines</td>
            <td>Feature X vs Target Y</td>
            <td>Demonstrates why least squares selects the minimum SSE line over arbitrary alternatives.</td>
          </tr>
          <tr>
            <td><strong>04</strong></td>
            <td>Slope and Intercept Shifts</td>
            <td>Feature X vs Target Y</td>
            <td>Demonstrates geometric effects of positive, negative, zero slopes and parallel height shifts.</td>
          </tr>
          <tr>
            <td><strong>05</strong></td>
            <td>Vertical Residual Segments</td>
            <td>Feature X vs Target Y</td>
            <td>Shows individual prediction errors e&#7522; connecting points to the fitted line.</td>
          </tr>
          <tr>
            <td><strong>06</strong></td>
            <td>Actual vs Predicted Plot</td>
            <td>Actual Y vs Predicted &#375;</td>
            <td>Assesses calibration along the 45-degree identity line (y = &#375;).</td>
          </tr>
          <tr>
            <td><strong>07</strong></td>
            <td>Residual Plot</td>
            <td>Predicted &#375; vs Residual e</td>
            <td>Detects heteroscedasticity (funnel shape) and non-linear curvature patterns.</td>
          </tr>
          <tr>
            <td><strong>08</strong></td>
            <td>Loss Function Curves</td>
            <td>Error e vs Loss Penalty</td>
            <td>Contrasts quadratic penalty of MSE against linear penalty of MAE.</td>
          </tr>
          <tr>
            <td><strong>09</strong></td>
            <td>Gradient Descent Convergence</td>
            <td>Epochs vs MSE Loss</td>
            <td>Confirms smooth exponential decay toward the global minimum basin.</td>
          </tr>
          <tr>
            <td><strong>10</strong></td>
            <td>Outlier Influence Plot</td>
            <td>Feature X vs Target Y</td>
            <td>Identifies high-leverage points that torque or distort parameter estimates.</td>
          </tr>
          <tr>
            <td><strong>11</strong></td>
            <td>2D Line vs 3D Hyperplane</td>
            <td>X&#8321;, X&#8322; vs Target Y</td>
            <td>Visualizes multi-dimensional feature combination and planar decision boundaries.</td>
          </tr>
          <tr>
            <td><strong>12</strong></td>
            <td>Evaluation Scorecard</td>
            <td>Model Variant vs Metrics</td>
            <td>Quantitative benchmark comparing Simple vs Multiple regression performance.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 14: REGRESSION ASSUMPTIONS AND LIMITATIONS -->
  <section id="sec-14" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 14</span>
      <h2 class="section-title">Regression Assumptions and Limitations (LINE)</h2>
    </div>
    <p class="section-intro">
      Ordinary Least Squares linear regression rests upon four classical statistical assumptions, remembered by the acronym <strong>LINE</strong>, plus three critical practical constraints.
    </p>

    <!-- LINE Framework Cards -->
    <div class="card card-def">
      <div class="card-title"><span>&#128207;</span> L &mdash; Linearity of the Relationship</div>
      <p>
        The true underlying relationship between features and target must be reasonably linear. If the true data follows an exponential curve or a U-shaped parabola, a straight line will systematically underfit.
        <br><strong>Diagnostic Check:</strong> Inspect the scatter plot and residual plot. If residuals show a curved U-shape, linearity is violated.
      </p>
    </div>

    <div class="card card-concept">
      <div class="card-title"><span>&#128065;</span> I &mdash; Independence of Residuals</div>
      <p>
        Individual observation errors must be statistically independent of one another. Autocorrelation (common in time-series data where yesterday's temperature correlates with today's) or clustered groupings (multiple hospital visits by the same patient) violate independence.
        <br><strong>Diagnostic Check:</strong> Durbin-Watson test statistic (ideal value &approx; 2.0).
      </p>
    </div>

    <div class="card card-analogy">
      <div class="card-title"><span>&#128200;</span> N &mdash; Normality of Residuals</div>
      <p>
        The residuals should be approximately normally distributed with mean zero: <code>e &sim; N(0, &sigma;&#178;)</code>. While minor non-normality does not destroy prediction accuracy in large sample sizes (via the Central Limit Theorem), it is required for valid hypothesis tests, p-values, and confidence intervals.
        <br><strong>Diagnostic Check:</strong> Q-Q (Quantile-Quantile) plot or Shapiro-Wilk test.
      </p>
    </div>

    <div class="card card-amber">
      <div class="card-title"><span>&#9878;</span> E &mdash; Equal Variance (Homoscedasticity)</div>
      <p>
        The variance of the residuals must remain constant across all predicted values. If error spread widens like a megaphone (funnel shape) as predictions grow, the model suffers from <em>heteroscedasticity</em>.
        <br><strong>Remedy:</strong> Apply a logarithmic transformation <code>np.log1p(y)</code> to stabilize variance.
      </p>
    </div>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> The Danger of Extrapolation Beyond the Training Domain</div>
      <p>
        Linear regression models are only valid <strong>within the numerical range of observed training data</strong>. If your model trained on houses between 800 and 3,500 sq ft, predicting the price of an 18,000 sq ft mega-mansion is pure reckless speculation. The linear assumption almost certainly breaks down at extreme scales!
      </p>
    </div>
  </section>

  <!-- SECTION 15: UNDERFITTING, OVERFITTING AND GENERALIZATION -->
  <section id="sec-15" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 15</span>
      <h2 class="section-title">Underfitting, Overfitting and Generalization</h2>
    </div>
    <p class="section-intro">
      Connecting directly to the principles established in Topic 8 (Train, Validation &amp; Test Sets), every linear model must navigate the fundamental trade-off between <strong>Bias</strong> (underfitting) and <strong>Variance</strong> (overfitting).
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Model State</th>
            <th>Root Cause</th>
            <th>Training Error</th>
            <th>Test Error</th>
            <th>Practical Engineering Remedy</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Underfitting (High Bias)</strong></td>
            <td>Model is too simplistic to capture the true phenomenon (e.g. fitting a straight line through complex non-linear data).</td>
            <td>High Error (Poor)</td>
            <td>High Error (Poor)</td>
            <td>Add polynomial features (<code>x&#178;, x&#179;</code>), engineer interaction terms, or adopt non-linear models (Decision Trees, Random Forests).</td>
          </tr>
          <tr>
            <td><strong>Optimal Balance</strong></td>
            <td>Model captures genuine underlying relationships while ignoring random measurement noise.</td>
            <td>Low Error (Good)</td>
            <td>Low Error (Good)</td>
            <td>Deploy and monitor model performance on live inference data.</td>
          </tr>
          <tr>
            <td><strong>Overfitting (High Variance)</strong></td>
            <td>Model is excessively flexible (e.g. 15th-degree polynomial), memorizing training noise and specific sample quirks.</td>
            <td>Near-Zero Error</td>
            <td>Massive Error (Catastrophic)</td>
            <td>Prune unnecessary features, collect more training samples, or apply regularization (Ridge L2 or Lasso L1 penalties).</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-success">
      <div class="card-title"><span>&#9745;</span> The Golden Rule of Model Evaluation</div>
      <p>
        Always evaluate your final regression model on a <strong>strictly quarantined holdout test set</strong> that was never seen during training or hyperparameter selection. A model that achieves <code>R&#178; = 0.99</code> on training data but drops to <code>R&#178; = 0.45</code> on test data is an overfitted failure that cannot be trusted in production.
      </p>
    </div>
  </section>
"""
