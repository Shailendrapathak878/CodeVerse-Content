"""
Module: topic9_part4.py
Contains HTML for Sections 16 to 19, Glossary, Revision, and Footer of Topic 9: Linear Regression.
"""

from scratch.topic9_svgs import SVG_LAB_EVALUATION_SUMMARY

PART4_HTML = f"""
  <!-- SECTION 16: COMPLETE PYTHON PRACTICAL LAB -->
  <section id="sec-16" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 16</span>
      <h2 class="section-title">Complete Python Practical Lab</h2>
    </div>
    <p class="section-intro">
      In this hands-on laboratory, we build an end-to-end, reproducible linear regression workflow using a 100-sample residential property dataset. We perform an 80/20 train/test split, fit both Simple and Multiple Linear Regression models using Scikit-Learn, evaluate performance using MAE, MSE, RMSE, and R&#178;, inspect coefficients, and assert zero data leakage.
    </p>

    <div class="code-block">
      <div class="code-header">
        <span class="code-title">topic9_complete_practical_lab.py</span>
        <span class="code-lang">python</span>
      </div>
      <pre><code>import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("=== STEP 1: CREATE SYNTHETIC RESIDENTIAL PROPERTY DATASET ===")
# Deterministic seed for reproducible evaluation
np.random.seed(42)
n_houses = 100

# Feature generation with realistic ranges
area = np.random.uniform(800, 3200, n_houses)
bedrooms = np.random.choice([1, 2, 3, 4, 5], size=n_houses, p=[0.1, 0.25, 0.35, 0.2, 0.1])
age = np.random.uniform(1, 35, n_houses)
distance = np.random.uniform(2, 20, n_houses)
noise = np.random.normal(0, 20, n_houses)

# Ground truth underlying price formula (with stochastic noise)
price = 50.0 + 0.14 * area + 22.0 * bedrooms - 1.2 * age - 2.8 * distance + noise

df = pd.DataFrame({{
    'House_ID': [f'HSE-{{i:04d}}' for i in range(1, n_houses + 1)],
    'Area_SqFt': np.round(area, 0),
    'Bedrooms': bedrooms,
    'Age_Years': np.round(age, 1),
    'Distance_Miles': np.round(distance, 1),
    'Price_kUSD': np.round(price, 1)
}})

print(f"Dataset generated. Shape: {{df.shape}}")
print(df.head(3))

print("\\n=== STEP 2: LEAK-FREE 80/20 TRAIN/TEST SPLIT ===")
train_df, test_df = train_test_split(df, test_size=0.20, random_state=42)

print(f"Training Set: {{len(train_df)}} samples (80%)")
print(f"Testing Set:  {{len(test_df)}} samples (20%)")

# Verify zero ID leakage between splits
overlap = set(train_df['House_ID']).intersection(set(test_df['House_ID']))
assert len(overlap) == 0, f"Data Leakage detected! Shared IDs: {{overlap}}"
print("&#10003; Zero ID Overlap Verified across Train and Test sets!")

print("\\n=== STEP 3: FIT SIMPLE LINEAR REGRESSION (AREA ONLY) ===")
X_train_simple = train_df[['Area_SqFt']]
y_train = train_df['Price_kUSD']
X_test_simple = test_df[['Area_SqFt']]
y_test = test_df['Price_kUSD']

slr = LinearRegression()
slr.fit(X_train_simple, y_train)

y_pred_train_slr = slr.predict(X_train_simple)
y_pred_test_slr = slr.predict(X_test_simple)

slr_test_r2 = r2_score(y_test, y_pred_test_slr)
slr_test_mae = mean_absolute_error(y_test, y_pred_test_slr)
slr_test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test_slr))

print(f"SLR Fitted Intercept: {{slr.intercept_:.2f}} kUSD")
print(f"SLR Fitted Slope:     {{slr.coef_[0]:.4f}} kUSD / sq ft")
print(f"SLR Test R&#178; Score:     {{slr_test_r2:.4f}}")
print(f"SLR Test MAE:         ${{slr_test_mae:.2f}}k USD")
print(f"SLR Test RMSE:        ${{slr_test_rmse:.2f}}k USD")

print("\\n=== STEP 4: FIT MULTIPLE LINEAR REGRESSION (4 FEATURES) ===")
feature_cols = ['Area_SqFt', 'Bedrooms', 'Age_Years', 'Distance_Miles']
X_train_multi = train_df[feature_cols]
X_test_multi = test_df[feature_cols]

mlr = LinearRegression()
mlr.fit(X_train_multi, y_train)

y_pred_train_mlr = mlr.predict(X_train_multi)
y_pred_test_mlr = mlr.predict(X_test_multi)

mlr_test_r2 = r2_score(y_test, y_pred_test_mlr)
mlr_test_mae = mean_absolute_error(y_test, y_pred_test_mlr)
mlr_test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test_mlr))

print(f"MLR Fitted Intercept: {{mlr.intercept_:.2f}}")
for col, coef in zip(feature_cols, mlr.coef_):
    print(f"  {{col:15s}}: {{coef:+.4f}}")

print(f"MLR Test R&#178; Score:     {{mlr_test_r2:.4f}}")
print(f"MLR Test MAE:         ${{mlr_test_mae:.2f}}k USD")
print(f"MLR Test RMSE:        ${{mlr_test_rmse:.2f}}k USD")

print("\\n=== STEP 5: VERIFICATION ASSERTIONS ===")
assert mlr_test_r2 &gt; slr_test_r2, "Multiple regression must outperform simple regression!"
assert mlr_test_rmse &lt; slr_test_rmse, "Multiple regression must reduce test RMSE!"
assert np.all(np.isfinite(y_pred_test_mlr)), "Predictions must be finite numbers!"
assert y_pred_test_mlr.shape == (20,), "Predictions must match test set shape!"
print("&#10003; All Model Assertions &amp; Benchmarks Passed Successfully!")</code></pre>
    </div>

    <!-- FIGURE 9.14: LAB EVALUATION SUMMARY -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_LAB_EVALUATION_SUMMARY}
      </div>
      <div class="diagram-caption">Figure 9.14: Python Practical Lab evaluation scorecard: Multiple linear regression cuts test error by 54% and boosts explained variance to 97.0%.</div>
    </div>

    <h3>Quantitative Execution Benchmark Results</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Model Architecture</th>
            <th>Features Used</th>
            <th>Test R&#178; Score</th>
            <th>Test MAE</th>
            <th>Test RMSE</th>
            <th>Engineering Assessment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Simple Linear Regression</strong></td>
            <td>1 Feature (Living Area)</td>
            <td><strong>0.8583 (85.8%)</strong></td>
            <td>$35.04k USD</td>
            <td>$42.71k USD</td>
            <td>Solid baseline, but limited by omitted features.</td>
          </tr>
          <tr>
            <td><strong>Multiple Linear Regression</strong></td>
            <td>4 Features (Area, Bed, Age, Dist)</td>
            <td><strong>0.9700 (97.0%)</strong></td>
            <td><strong>$15.98k USD</strong></td>
            <td><strong>$19.67k USD</strong></td>
            <td><strong>Champion Model:</strong> Errors halved (-54%) by capturing multi-factor context.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 17: REAL-LIFE CASE STUDIES -->
  <section id="sec-17" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 17</span>
      <h2 class="section-title">Real-Life Industry Case Studies</h2>
    </div>
    <p class="section-intro">
      Examine four detailed real-world engineering case studies showing how linear regression is deployed in enterprise production systems.
    </p>

    <!-- Case Study A -->
    <div class="card card-def">
      <div class="card-title"><span>&#127968;</span> Case Study A: Real Estate Property Valuation (PropTech)</div>
      <p><strong>The Business Problem:</strong> An automated online mortgage platform estimates home appraisal values to pre-approve property loans without waiting 3 weeks for an in-person appraiser.</p>
      <p><strong>Input Features:</strong> Interior Square Footage, Bedroom Count, Bathroom Count, Construction Year, Lot Size.</p>
      <p><strong>Numerical Target:</strong> Fair Market Value in US Dollars (continuous).</p>
      <p><strong>Why Regression is Appropriate:</strong> The objective is estimating an exact financial price point rather than a broad price tier.</p>
      <p><strong>Model Limitations:</strong> The linear model cannot capture hyper-local neighborhood prestige (e.g., homes on the north side of the street having ocean views) unless explicitly encoded as spatial coordinates or neighborhood indicator variables.</p>
      <p><strong>Key Metrics &amp; Diagnostics:</strong> RMSE in US Dollars, Residual Plots to check for heteroscedasticity across luxury homes.</p>
    </div>

    <!-- Case Study B -->
    <div class="card card-analogy">
      <div class="card-title"><span>&#127891;</span> Case Study B: Student Study Habits &amp; Academic Outcomes (EdTech)</div>
      <p><strong>The Business Problem:</strong> A university learning analytics department models student exam performance to detect at-risk students who need tutoring intervention early in the semester.</p>
      <p><strong>Input Features:</strong> Online Lecture Hours Watched, Practice Problems Completed, Assignment Submission Timeliness.</p>
      <p><strong>Numerical Target:</strong> Final Course Percentage Score (0.0&ndash;100.0).</p>
      <p><strong>Why Regression is Appropriate:</strong> Continuous grading scale allows fine-grained tracking of improvement.</p>
      <p><strong>Model Limitations:</strong> <em>Diminishing Marginal Returns</em>: Moving from 2 hours of study to 4 hours yields huge gains, but studying from 28 hours to 30 hours yields near-zero gains (or even exhaustion). A pure straight line fails to capture this non-linear saturation curve unless a logarithmic transform is applied.</p>
      <p><strong>Key Metrics &amp; Diagnostics:</strong> Mean Absolute Error (MAE) in percentage points.</p>
    </div>

    <!-- Case Study C -->
    <div class="card card-concept">
      <div class="card-title"><span>&#128200;</span> Case Study C: Retail Supply Chain Demand Forecasting (E-Commerce)</div>
      <p><strong>The Business Problem:</strong> A retail chain forecasts next-week unit sales across 500 grocery stores to optimize warehouse replenishment and minimize perishable food waste.</p>
      <p><strong>Input Features:</strong> Promotional Discount Depth (%), Marketing Ad Spend, Local Foot Traffic Count, Average Competitor Price.</p>
      <p><strong>Numerical Target:</strong> Total Weekly Unit Sales (continuous count).</p>
      <p><strong>Why Regression is Appropriate:</strong> Warehouse inventory planning requires exact order quantities.</p>
      <p><strong>Model Limitations:</strong> Simple linear regression ignores calendar seasonality (e.g. huge spikes during Thanksgiving and Christmas) and inventory stockout bounds (sales cannot fall below zero).</p>
      <p><strong>Key Metrics &amp; Diagnostics:</strong> Root Mean Squared Error (RMSE) to heavily penalize stockouts.</p>
    </div>

    <!-- Case Study D -->
    <div class="card card-success">
      <div class="card-title"><span>&#9889;</span> Case Study D: Municipal Electric Power Grid Load Forecasting (Energy)</div>
      <p><strong>The Business Problem:</strong> A regional electrical utility forecasts hourly megawatt (MW) load to dispatch natural gas peaker plants economically and prevent grid blackouts.</p>
      <p><strong>Input Features:</strong> Ambient Outside Temperature (&deg;F), Humidity, Solar Irradiance, Industrial Factory Operating Index.</p>
      <p><strong>Numerical Target:</strong> Grid Demand in Megawatts (MW).</p>
      <p><strong>Why Regression is Appropriate:</strong> Continuous power generation must match instantaneous consumer load.</p>
      <p><strong>Model Limitations:</strong> <em>The U-Shaped Temperature Curve</em>: Power demand is high at 20&deg;F (electric heating) and high at 95&deg;F (air conditioning), but lowest at a comfortable 68&deg;F. Fitting a single straight line through temperature fails completely! Engineers must use piecewise linear splines or polynomial terms <code>Temp&#178;</code> to model heating and cooling regimes.</p>
      <p><strong>Key Metrics &amp; Diagnostics:</strong> Mean Absolute Percentage Error (MAPE) and Durbin-Watson tests for time-series autocorrelation.</p>
    </div>
  </section>

  <!-- SECTION 18: COMMON BEGINNER MISTAKES -->
  <section id="sec-18" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 18</span>
      <h2 class="section-title">16 Common Beginner Mistakes &amp; Fixes</h2>
    </div>
    <p class="section-intro">
      Learn to recognize and prevent the 16 most frequent mistakes made by junior machine learning practitioners when developing and evaluating linear regression models.
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Common Beginner Mistake</th>
            <th>Why It Causes Serious Failures</th>
            <th>Defensive Safe Engineering Approach</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>01</strong></td>
            <td>Confusing Regression with Classification</td>
            <td>Applying linear regression to predict binary categories (0 or 1) produces unbounded outputs like -1.4 or +2.8, violating probability laws.</td>
            <td>Use <strong>Logistic Regression</strong> for discrete categories; reserve <strong>Linear Regression</strong> for continuous quantities.</td>
          </tr>
          <tr>
            <td><strong>02</strong></td>
            <td>Assuming all data must fit a straight line</td>
            <td>Forcing a straight line onto curved or periodic data creates massive, systematic underfitting (high bias).</td>
            <td>Always plot a scatter plot and residual plot first. If U-shaped patterns appear, engineer polynomial terms.</td>
          </tr>
          <tr>
            <td><strong>03</strong></td>
            <td>Confusing Slope (&beta;&#8321;) with Intercept (&beta;&#8320;)</td>
            <td>Misinterpreting the baseline offset as the rate of change leads to absurd business conclusions.</td>
            <td>Remember: Slope is the <em>rate of change</em> (&Delta;y/&Delta;x); Intercept is the <em>height at x = 0</em>.</td>
          </tr>
          <tr>
            <td><strong>04</strong></td>
            <td>Confusing Actual (y) with Predicted (&#375;)</td>
            <td>Using predictions in place of ground truth corrupts residual calculations and invalidates offline evaluations.</td>
            <td>Strictly maintain notation: <code>y</code> = measured ground truth, <code>&#375;</code> = model output.</td>
          </tr>
          <tr>
            <td><strong>05</strong></td>
            <td>Calculating Residuals with Inverted Sign</td>
            <td>Writing <code>e = &#375; - y</code> inverts the meaning of overestimation and underestimation.</td>
            <td>Always use the standard statistical definition: <code>e&#7522; = y&#7522; - &#375;&#7522;</code> (Actual minus Predicted).</td>
          </tr>
          <tr>
            <td><strong>06</strong></td>
            <td>Interpreting High R&#178; as Proof of Causation</td>
            <td>High R&#178; only indicates observational correlation. Confounders or reverse causality may be at play.</td>
            <td>Never claim feature X "causes" target Y without randomized controlled experimental trials (A/B tests).</td>
          </tr>
          <tr>
            <td><strong>07</strong></td>
            <td>Evaluating Exclusively on Training Data</td>
            <td>Training error measures memorization. A complex model can achieve low training error while failing on unseen data.</td>
            <td>Always split data into independent train and holdout test sets (Topic 8).</td>
          </tr>
          <tr>
            <td><strong>08</strong></td>
            <td>Using the Test Set for Feature Selection</td>
            <td>Repeatedly tweaking model features after checking test R&#178; causes test-set overfitting and evaluation bias.</td>
            <td>Use a validation set or K-Fold Cross-Validation for tuning; evaluate on the test set strictly once at the end.</td>
          </tr>
          <tr>
            <td><strong>09</strong></td>
            <td>Assuming Low Training Error Guarantees Test Success</td>
            <td>A model may have memorized training outliers or noise, leading to catastrophic test generalization error.</td>
            <td>Compare training R&#178; and test R&#178;. If a large gap (&gt; 0.15) exists, the model is overfitting.</td>
          </tr>
          <tr>
            <td><strong>10</strong></td>
            <td>Ignoring Residual Plot Patterns</td>
            <td>Summary metrics like R&#178; = 0.90 can hide extreme non-linearity or heteroscedasticity.</td>
            <td>Always plot residuals against predicted values. Look for uniform horizontal scatter around zero.</td>
          </tr>
          <tr>
            <td><strong>11</strong></td>
            <td>Believing Feature Scaling is Mandatory for OLS</td>
            <td>Ordinary Least Squares calculates analytical closed-form coefficients that are scale-invariant.</td>
            <td>Scaling is optional for unregularized OLS; it is mandatory when using Gradient Descent or Ridge/Lasso penalties.</td>
          </tr>
          <tr>
            <td><strong>12</strong></td>
            <td>Ignoring Influential Outliers</td>
            <td>Because MSE squares errors, a single high-leverage anomaly can torque the entire regression line.</td>
            <td>Use scatter plots, Cook's distance, or <code>RobustScaler</code> to detect and inspect high-leverage outliers.</td>
          </tr>
          <tr>
            <td><strong>13</strong></td>
            <td>Extrapolating Far Beyond Training Domain</td>
            <td>Linear models have no concept of physical boundaries and will output negative prices or impossible physics.</td>
            <td>Never use a model to predict inputs far outside the min/max bounds of the observed training dataset.</td>
          </tr>
          <tr>
            <td><strong>14</strong></td>
            <td>Interpreting Coefficients with Multicollinearity</td>
            <td>When features are strongly correlated, individual coefficients become noisy, unstable, and uninterpretable.</td>
            <td>Inspect feature correlation matrices (<code>df.corr()</code>); prune redundant features with VIF &gt; 5.0.</td>
          </tr>
          <tr>
            <td><strong>15</strong></td>
            <td>Reporting MSE Without Stating Squared Units</td>
            <td>Reporting "an error of 450" when the target is dollars leads stakeholders to think the error is $450 instead of $450&#178;.</td>
            <td>Always report <strong>RMSE</strong> or <strong>MAE</strong> alongside MSE so stakeholders understand real dollar units.</td>
          </tr>
          <tr>
            <td><strong>16</strong></td>
            <td>Relying on a Single Evaluation Metric</td>
            <td>R&#178; tells you explained variance; MAE tells you typical error; RMSE penalizes big mistakes. None is complete alone.</td>
            <td>Always report a holistic metric suite: <code>MAE</code>, <code>RMSE</code>, and <code>R&#178;</code> together.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 19: GLOSSARY, REVISION AND FINAL EXERCISE -->
  <section id="sec-19" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 19</span>
      <h2 class="section-title">Glossary, Revision &amp; Hands-On Exercise</h2>
    </div>
    <p class="section-intro">
      Consolidate your mastery of Linear Regression with a production workflow checklist, comprehensive glossary, interactive revision questions, and a capstone practical assignment.
    </p>

    <!-- Production Checklist -->
    <div class="card card-success">
      <div class="card-title"><span>&#9745;</span> Production Linear Regression Workflow Checklist</div>
      <ul>
        <li><strong>Step 1:</strong> Plot a scatter plot of features vs target to verify approximate linearity.</li>
        <li><strong>Step 2:</strong> Check feature correlation matrix to identify and eliminate severe multicollinearity.</li>
        <li><strong>Step 3:</strong> Partition data into independent train and holdout test sets using a fixed <code>random_state</code>.</li>
        <li><strong>Step 4:</strong> Fit <code>LinearRegression</code> strictly on the training partition (never touch test data).</li>
        <li><strong>Step 5:</strong> Inspect fitted intercept and coefficients; confirm that parameter signs align with domain intuition.</li>
        <li><strong>Step 6:</strong> Generate predictions and compute MAE, MSE, RMSE, and R&#178; across training and testing sets.</li>
        <li><strong>Step 7:</strong> Plot residuals against predicted values; verify homoscedasticity and absence of curved patterns.</li>
        <li><strong>Step 8:</strong> Plot actual vs predicted values along the 45-degree identity line to confirm calibration.</li>
      </ul>
    </div>

    <h3>Comprehensive Glossary of Essential Terms</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Technical Term</th>
            <th>Formal Engineering Definition</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Linear Regression</strong></td>
            <td>A supervised learning model that predicts a continuous target as a linear combination of input features and parameters.</td>
          </tr>
          <tr>
            <td><strong>Ordinary Least Squares (OLS)</strong></td>
            <td>An estimation method that calculates model parameters by minimizing the sum of squared vertical residuals (SSE).</td>
          </tr>
          <tr>
            <td><strong>Slope (&beta;&#8321;)</strong></td>
            <td>The rate of change in predicted target per unit increase in input feature (rise over run: &Delta;y / &Delta;x).</td>
          </tr>
          <tr>
            <td><strong>Intercept (&beta;&#8320;)</strong></td>
            <td>The expected value of the target when all input features equal zero (y-axis crossing point).</td>
          </tr>
          <tr>
            <td><strong>Residual (e&#7522;)</strong></td>
            <td>The vertical difference between actual observed value and predicted model value: <code>e&#7522; = y&#7522; - &#375;&#7522;</code>.</td>
          </tr>
          <tr>
            <td><strong>Sum of Squared Errors (SSE)</strong></td>
            <td>The aggregated sum of squared residuals across all training observations: <code>&Sigma; (y&#7522; - &#375;&#7522;)&#178;</code>.</td>
          </tr>
          <tr>
            <td><strong>Mean Squared Error (MSE)</strong></td>
            <td>The arithmetic mean of squared residuals: <code>SSE / n</code>. The primary loss function for regression.</td>
          </tr>
          <tr>
            <td><strong>Root Mean Squared Error (RMSE)</strong></td>
            <td>The square root of MSE. Restores original target units while maintaining quadratic penalty on large errors.</td>
          </tr>
          <tr>
            <td><strong>Mean Absolute Error (MAE)</strong></td>
            <td>The average magnitude of absolute errors: <code>(1/n) &Sigma; |y&#7522; - &#375;&#7522;|</code>. Robust against extreme outliers.</td>
          </tr>
          <tr>
            <td><strong>R-Squared (R&#178;)</strong></td>
            <td>Coefficient of determination. Measures the proportion of target variance explained by the regression model.</td>
          </tr>
          <tr>
            <td><strong>Gradient Descent</strong></td>
            <td>An iterative optimization algorithm that updates parameters in the direction of the negative gradient of the loss surface.</td>
          </tr>
          <tr>
            <td><strong>Learning Rate (&alpha;)</strong></td>
            <td>A hyperparameter controlling the step size taken along the gradient during optimization.</td>
          </tr>
          <tr>
            <td><strong>Multiple Regression</strong></td>
            <td>A linear model incorporating two or more independent input features, forming a multi-dimensional hyperplane.</td>
          </tr>
          <tr>
            <td><strong>Multicollinearity</strong></td>
            <td>A condition where two or more predictor features are highly linearly correlated, causing unstable coefficient estimates.</td>
          </tr>
          <tr>
            <td><strong>Homoscedasticity</strong></td>
            <td>The statistical assumption that residual variance remains constant across all levels of predicted target values.</td>
          </tr>
          <tr>
            <td><strong>Heteroscedasticity</strong></td>
            <td>The violation of equal error variance, typically displaying a megaphone or funnel pattern on a residual plot.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3>12 Interactive Revision Questions &amp; Detailed Explanations</h3>

    <details>
      <summary><span>&#10067;</span> Question 1: What is the primary difference between regression and classification?</summary>
      <div class="details-content">
        <strong>Answer:</strong> <strong>Classification</strong> predicts discrete categorical labels (e.g. Spam vs Not Spam, Cat vs Dog, 0 or 1). <strong>Regression</strong> predicts continuous numerical values along a real-number continuum (e.g. house price in dollars, temperature in degrees, vehicle fuel efficiency in MPG).
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 2: In the equation &#375; = 3.5x + 12, calculate &#375; when x = 4.0.</summary>
      <div class="details-content">
        <strong>Answer:</strong> Step-by-step arithmetic:
        <br><code>&#375; = 3.5(4.0) + 12 = 14.0 + 12 = 26.0</code>.
        <br>The model predicts an output value of <strong>26.0</strong>.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 3: An observed data point is (x = 3, y = 18). If the model predicts &#375; = 20, what is the residual?</summary>
      <div class="details-content">
        <strong>Answer:</strong> Using the standard formula <code>e&#7522; = y&#7522; - &#375;&#7522;</code>:
        <br><code>e = 18 - 20 = -2.0</code>.
        <br>The residual is <strong>-2.0</strong>, meaning the model <em>overestimated</em> the true target by 2.0 units.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 4: Why are residuals measured vertically instead of perpendicularly to the line?</summary>
      <div class="details-content">
        <strong>Answer:</strong> Because our predictive task is strictly asymmetric: we are given the input feature <code>x</code> as a fixed, error-free quantity, and our sole objective is predicting the target <code>y</code>. Therefore, the error we want to penalize and minimize is strictly the vertical discrepancy along the target dimension.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 5: Why does Mean Squared Error (MSE) square the residuals instead of taking a simple sum?</summary>
      <div class="details-content">
        <strong>Answer:</strong> In Ordinary Least Squares, positive errors (underestimates) and negative errors (overestimates) naturally sum to exact zero. If we didn't square or take absolute values, large positive and negative mistakes would cancel each other out, making a terrible model appear flawless. Squaring ensures all errors contribute positive penalties and creates a smooth, differentiable parabola for optimization.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 6: What does an R&#178; score of 0.82 mean in plain English?</summary>
      <div class="details-content">
        <strong>Answer:</strong> An R&#178; score of 0.82 means that <strong>82% of the variance</strong> in the target variable is successfully explained and accounted for by the linear model. The remaining 18% of variance is due to unobserved factors, measurement noise, or non-linear effects.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 7: Can R&#178; ever be negative? If so, when?</summary>
      <div class="details-content">
        <strong>Answer:</strong> <strong>Yes!</strong> On independent holdout test data, R&#178; can become negative. The R&#178; baseline is 0.0, which corresponds to predicting the flat average of the training data. If your model makes wildly inaccurate predictions on unseen test data, its residual sum of squares (<code>SS_res</code>) will be larger than the total variance (<code>SS_tot</code>), resulting in a negative R&#178; score.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 8: How do you interpret a multiple regression coefficient &beta;&#8321; = +35.0 for feature x&#8321;?</summary>
      <div class="details-content">
        <strong>Answer:</strong> For each one-unit increase in feature <code>x&#8321;</code>, the expected target value increases by <strong>35.0 units</strong>, <em>holding all other features in the model completely constant</em> (the ceteris paribus condition).
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 9: What is multicollinearity and how does it affect linear regression?</summary>
      <div class="details-content">
        <strong>Answer:</strong> Multicollinearity occurs when two or more input features are strongly correlated with each other (e.g. square feet and room count). While it does not reduce the model's overall predictive power or R&#178;, it makes individual coefficient estimates wildly unstable, inflating their standard errors and making it impossible to interpret the unique contribution of each feature.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 10: What does a funnel-shaped pattern on a residual plot indicate?</summary>
      <div class="details-content">
        <strong>Answer:</strong> A funnel (or megaphone) shape indicates <strong>heteroscedasticity</strong>&mdash;meaning the variance of prediction errors is not constant, but expands as predictions grow. This violates the equal-variance assumption of OLS and requires transforming the target (e.g., using <code>np.log1p(y)</code>) or using robust standard errors.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 11: Why does a single extreme outlier have so much power to rotate an OLS regression line?</summary>
      <div class="details-content">
        <strong>Answer:</strong> Because Ordinary Least Squares minimizes the <em>squared</em> residuals: <code>SSE = &Sigma; e&#7522;&#178;</code>. An outlier that is far away from the line produces a massive error; squaring that error (e.g., <code>100&#178; = 10,000</code>) creates an immense penalty that dominates all other points, forcing the line to pivot toward the outlier to reduce that single huge squared penalty.
      </div>
    </details>

    <details>
      <summary><span>&#10067;</span> Question 12: Why is extrapolating far beyond the observed training range dangerous?</summary>
      <div class="details-content">
        <strong>Answer:</strong> Linear regression assumes a constant straight-line relationship across the entire universe. In reality, physical and economic relationships are only approximately linear within the observed range. Extrapolating to extreme values ignores physical limits, diminishing returns, and non-linear regime shifts, leading to wildly invalid predictions (e.g., negative prices or infinite speeds).
      </div>
    </details>

    <h3>Scenario-Based Engineering Challenges</h3>
    <div class="card card-concept">
      <div class="card-title"><span>&#9874;</span> Scenario Challenge 1: The Non-Linear Commute Time Model</div>
      <p>
        <strong>Scenario:</strong> You fit a simple linear regression model predicting morning vehicle commute time (minutes) from distance to office (miles). Your model achieves <code>R&#178; = 0.88</code>. However, when inspecting the residual plot, you observe a clear U-shaped curved pattern: residuals are positive for 1&ndash;5 miles, negative for 6&ndash;15 miles, and positive again for &gt;20 miles.
      </p>
      <p>
        <strong>Challenge:</strong> What does this diagnostic pattern mean, and how should you upgrade your model?
      </p>
      <p>
        <strong>Recommended Solution:</strong> The U-shaped residual pattern proves that the underlying relationship is <strong>non-linear</strong> (violating the Linearity assumption). Highway speeds and congestion create non-linear travel dynamics.
        <br><strong>Fix:</strong> Upgrade the feature matrix by adding a quadratic polynomial feature <code>Distance&#178;</code> or fitting a spline model. This absorbs the curvature and restores random, zero-centered residuals.
      </p>
    </div>

    <div class="card card-analogy">
      <div class="card-title"><span>&#9874;</span> Scenario Challenge 2: The Expanding Luxury Home Residual Funnel</div>
      <p>
        <strong>Scenario:</strong> A real estate regression model predicts home prices. For starter homes ($150k&ndash;$300k), residuals are small (&plusmn;$15k). For luxury homes ($1.5M&ndash;$3.0M), residuals explode to &plusmn;$400k, creating a distinct megaphone funnel on the residual plot.
      </p>
      <p>
        <strong>Challenge:</strong> Which classical regression assumption is violated, and what mathematical transformation fixes it?
      </p>
      <p>
        <strong>Recommended Solution:</strong> This is a classic violation of <strong>Homoscedasticity</strong> (equal error variance). Price variance naturally scales proportionally with asset value.
        <br><strong>Fix:</strong> Fit the model on the natural logarithm of price: <code>y_log = np.log(Price)</code>. Log transformation converts multiplicative percentage errors into additive constant errors, compressing luxury variance and restoring constant homoscedastic error spread.
      </p>
    </div>

    <h3>Final Hands-On Practical Assignment</h3>
    <div class="card card-success">
      <div class="card-title"><span>&#9997;</span> Capstone Assignment: Vehicle Fuel Efficiency Modeling</div>
      <p>
        Given a new automotive dataset with 500 vehicles containing:
        <br>&bull; <code>Curb_Weight_lbs</code>: Vehicle weight in pounds (1,800 to 5,200 lbs)
        <br>&bull; <code>Engine_Displacement_L</code>: Engine size in liters (1.2 to 6.2 L)
        <br>&bull; <code>Horsepower</code>: Engine power output (75 to 450 hp)
        <br>&bull; <code>Fuel_Economy_MPG</code>: Highway miles per gallon (continuous target, 12 to 52 MPG)
      </p>
      <p>
        <strong>Your Engineering Assignment:</strong>
        <br>1. Perform an 80/20 train/test split using <code>random_state=42</code>.
        <br>2. Fit a Simple Linear Regression model using <code>Curb_Weight_lbs</code> alone to predict <code>Fuel_Economy_MPG</code>.
        <br>3. Fit a Multiple Linear Regression model using all three engine and weight features.
        <br>4. Compute and compare Test R&#178;, MAE, and RMSE between both models.
        <br>5. Generate an Actual vs Predicted plot for the test set and plot residuals against predicted MPG.
        <br>6. Confirm that the slope for vehicle weight is negative (heavier vehicles consume more fuel / achieve lower MPG).
      </p>
    </div>

    <div class="notes-footer">
      <p>CodeVerse Machine Learning Educational Notes &bull; Topic 9: Linear Regression</p>
      <p>Strict Light Mode Standard &bull; Validated for Web and Mobile Viewports &bull; Powered by Scikit-Learn 1.9+</p>
    </div>
  </section>
"""
