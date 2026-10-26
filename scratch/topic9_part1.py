"""
Module: topic9_part1.py
Contains HTML for Hero Header, TOC, and Sections 1 to 5 of Topic 9: Linear Regression.
"""

from scratch.topic9_svgs import (
    SVG_REGRESSION_HERO,
    SVG_SCATTER_OBSERVATIONS,
    SVG_LINE_OF_BEST_FIT,
    SVG_SLOPE_INTERCEPT_VARIATIONS,
    SVG_COMPARING_CANDIDATE_LINES
)

PART1_HTML = f"""
  <!-- HERO CARD -->
  <header class="hero-card">
    <div class="hero-tag">Machine Learning &bull; Topic 9 &bull; Light Mode</div>
    <h1 class="hero-title">Linear Regression</h1>
    <p class="hero-subtitle">
      Master the foundational supervised learning algorithm for continuous numerical prediction. Understand the geometry of lines, slope and intercept, Ordinary Least Squares (OLS), residual errors, gradient descent, multiple regression, diagnostic plots, and leak-free evaluation.
    </p>
    <div class="meta-bar">
      <span class="meta-pill">&#128218; Level: Absolute Beginner &rarr; Production</span>
      <span class="meta-pill">&#9874; Mathematics: Arithmetic &amp; Intuitive Calculus</span>
      <span class="meta-pill">&#128187; Tooling: Scikit-Learn 1.9+ &bull; NumPy &bull; Pandas</span>
      <span class="meta-pill">&#9728;&#65039; Theme: Strict Light Mode Standard</span>
    </div>
  </header>

  <!-- TABLE OF CONTENTS -->
  <nav class="toc-card">
    <div class="toc-title"><span>&#128209;</span> Chapter Table of Contents</div>
    <div class="toc-grid">
      <a href="#sec-01" class="toc-item"><span class="toc-num">01.</span> Introduction to Regression</a>
      <a href="#sec-02" class="toc-item"><span class="toc-num">02.</span> What Is Linear Regression?</a>
      <a href="#sec-03" class="toc-item"><span class="toc-num">03.</span> Equation of a Straight Line</a>
      <a href="#sec-04" class="toc-item"><span class="toc-num">04.</span> Slope and Intercept in Real Life</a>
      <a href="#sec-05" class="toc-item"><span class="toc-num">05.</span> Finding the Best-Fit Line</a>
      <a href="#sec-06" class="toc-item"><span class="toc-num">06.</span> Actual, Predicted &amp; Residuals</a>
      <a href="#sec-07" class="toc-item"><span class="toc-num">07.</span> Loss Functions &amp; Mean Squared Error</a>
      <a href="#sec-08" class="toc-item"><span class="toc-num">08.</span> Ordinary Least Squares (OLS)</a>
      <a href="#sec-09" class="toc-item"><span class="toc-num">09.</span> Gradient Descent Optimization</a>
      <a href="#sec-10" class="toc-item"><span class="toc-num">10.</span> Simple Linear Regression</a>
      <a href="#sec-11" class="toc-item"><span class="toc-num">11.</span> Multiple Linear Regression</a>
      <a href="#sec-12" class="toc-item"><span class="toc-num">12.</span> Evaluation Metrics (MAE, MSE, R&#178;)</a>
      <a href="#sec-13" class="toc-item"><span class="toc-num">13.</span> Visual Learning &amp; Key Graphs</a>
      <a href="#sec-14" class="toc-item"><span class="toc-num">14.</span> Assumptions &amp; Limitations (LINE)</a>
      <a href="#sec-15" class="toc-item"><span class="toc-num">15.</span> Underfitting, Overfitting &amp; Bias-Variance</a>
      <a href="#sec-16" class="toc-item"><span class="toc-num">16.</span> Complete Python Practical Lab</a>
      <a href="#sec-17" class="toc-item"><span class="toc-num">17.</span> Real-Life Industry Case Studies</a>
      <a href="#sec-18" class="toc-item"><span class="toc-num">18.</span> 16 Common Beginner Mistakes &amp; Fixes</a>
      <a href="#sec-19" class="toc-item"><span class="toc-num">19.</span> Glossary, Revision &amp; Capstone Exercise</a>
    </div>
  </nav>

  <!-- SECTION 01: INTRODUCTION TO REGRESSION -->
  <section id="sec-01" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 01</span>
      <h2 class="section-title">Introduction to Regression</h2>
    </div>
    <p class="section-intro">
      In machine learning, <strong>Supervised Learning</strong> tasks divide into two primary families: <em>Classification</em> and <em>Regression</em>. While classification models predict discrete category labels (such as whether an email is spam or not spam), regression models predict <strong>continuous numerical quantities</strong> along a continuum.
    </p>

    <!-- FIGURE 9.1: HERO ARCHITECTURE -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_REGRESSION_HERO}
      </div>
      <div class="diagram-caption">Figure 9.1: The Supervised Regression paradigm: Mapping input features through a fitted mathematical function to estimate continuous numerical targets.</div>
    </div>

    <h3>Foundational Terminology from First Principles</h3>
    <ul>
      <li><strong>Machine Learning:</strong> The discipline of developing computer algorithms that automatically detect patterns in data and improve their performance through experience rather than explicit manual programming.</li>
      <li><strong>Supervised Learning:</strong> Training an algorithm by providing both input features and the corresponding known correct output labels (ground truth).</li>
      <li><strong>Regression:</strong> A statistical modeling technique that estimates the relationships between one or more independent variables (features) and a continuous dependent variable (target).</li>
      <li><strong>Input Features (X):</strong> The measurable attributes or explanatory variables used as inputs (e.g., the square footage of a house, years of work experience, engine size).</li>
      <li><strong>Target or Label (y):</strong> The ground-truth continuous numerical quantity the model attempts to forecast (e.g., house sale price in dollars, annual salary, vehicle miles per gallon).</li>
      <li><strong>Training Examples:</strong> Historical observations paired as <code>(x&#7522;, y&#7522;)</code> supplied to the learning algorithm during the parameter fitting stage.</li>
      <li><strong>Prediction (&#375;):</strong> The model's estimated output value for a given input <code>x</code>. We write <code>&#375;</code> (pronounced "y-hat") to distinguish model estimates from true observed values <code>y</code>.</li>
    </ul>

    <div class="card card-def">
      <div class="card-title"><span>&#127968;</span> Concrete Example: Estimating House Prices from Living Area</div>
      <p>
        Imagine a real estate dataset where we want to estimate the price of residential homes. In this scenario:
      </p>
      <ul>
        <li><strong>Input Feature (X):</strong> Finished interior living area measured in square feet (e.g., <code>1,500 sq ft</code>).</li>
        <li><strong>Target Variable (y):</strong> Market selling price in thousands of dollars (e.g., <code>$280.0k</code>).</li>
      </ul>
      <p>
        Notice that price is a continuous scalar number with an infinite number of possible values along the real number line, not a fixed category. This makes the task a classic <strong>regression problem</strong>.
      </p>
    </div>

    <!-- Regression vs Classification Table -->
    <h3>Regression vs Classification: The Key Differences</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Characteristic</th>
            <th>Regression</th>
            <th>Classification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Target Nature</strong></td>
            <td>Continuous numerical quantity (Real numbers: &reals;)</td>
            <td>Discrete categories / classes (e.g. 0 or 1, Cat or Dog)</td>
          </tr>
          <tr>
            <td><strong>Example Predictions</strong></td>
            <td>Temperature (72.4&deg;F), Stock Price ($142.50), Age (28.3 yrs)</td>
            <td>Spam vs Not Spam, Benign vs Malignant tumor, Credit Default (Yes/No)</td>
          </tr>
          <tr>
            <td><strong>Evaluation Metrics</strong></td>
            <td>Mean Absolute Error (MAE), Mean Squared Error (MSE), R&#178;</td>
            <td>Accuracy, Precision, Recall, F1-Score, ROC-AUC</td>
          </tr>
          <tr>
            <td><strong>Mathematical Output</strong></td>
            <td>Unbounded scalar value: <code>&#375; &isin; (-&infin;, +&infin;)</code></td>
            <td>Class probabilities: <code>P(y = c) &isin; [0, 1]</code> summing to 1.0</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card card-warn">
      <div class="card-title"><span>&#9888;</span> Crucial Caveat: Correlation Does Not Imply Causation!</div>
      <p>
        A linear regression model discovers <em>statistical associations</em> present in historical training data. If house price increases linearly with square footage, that does not mean artificially expanding a hallway will guarantee a proportional price hike in every real-world transaction. Unobserved confounders (such as neighborhood prestige, school district quality, and construction year) simultaneously influence both size and price. Always treat regression coefficients as observational correlations, never direct causal mechanisms.
      </p>
    </div>
  </section>

  <!-- SECTION 02: WHAT IS LINEAR REGRESSION? -->
  <section id="sec-02" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 02</span>
      <h2 class="section-title">What Is Linear Regression?</h2>
    </div>
    <p class="section-intro">
      <strong>Linear Regression</strong> is the foundational parametric statistical learning technique that models the relationship between one or more independent input features and a numerical target by fitting a straight linear equation to observed data.
    </p>

    <!-- FIGURE 9.2: SCATTER PLOT -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_SCATTER_OBSERVATIONS}
      </div>
      <div class="diagram-caption">Figure 9.2: Two-dimensional scatter plot of raw observations: Data points exhibit an upward linear trend with natural variance around the underlying signal.</div>
    </div>

    <h3>Why Don't Real-World Points Fall on a Perfect Line?</h3>
    <p>
      In pure high school mathematics, a line <code>y = 2x + 1</code> connects points that align with 100% mathematical perfection. However, real-world data collection is inherently messy:
    </p>
    <ul>
      <li><strong>Measurement Noise:</strong> Inaccuracies in sensor readings, rounding approximations, or subjective reporting errors introduce stochastic scatter.</li>
      <li><strong>Omitted Latent Variables:</strong> Two houses with the identical <code>2,000 sq ft</code> living area might sell for different prices because one has an updated kitchen or a private swimming pool while the other does not.</li>
      <li><strong>Inherent Human Randomness:</strong> Individual buyers and sellers negotiate subjectively, creating price dispersion around the baseline trend.</li>
    </ul>

    <p>
      Because points do not lie on a single line, linear regression does not seek an impossible equation that intersects every point. Instead, it seeks the <strong>Line of Best Fit</strong>&mdash;the single line that minimizes the total aggregate error across all observations.
    </p>

    <div class="card card-concept">
      <div class="card-title"><span>&#9777;</span> What Does "Linear" Actually Mean in Machine Learning?</div>
      <p>
        In machine learning and statistics, "linear" refers to <strong>linearity in the parameters (&beta;)</strong>, not necessarily linearity in the raw input features (X)!
      </p>
      <p>
        For instance, the model <code>&#375; = &beta;&#8320; + &beta;&#8321;x + &beta;&#8322;x&#178;</code> models a curved parabolic trajectory in terms of feature <code>x</code>, yet it remains a mathematically <strong>linear regression model</strong> because the output is a linear combination of the unknown weights <code>&beta;&#8320;, &beta;&#8321;, &beta;&#8322;</code>. This distinction allows linear regression to model surprisingly complex non-linear curves via basis expansion and polynomial feature transformations!
      </p>
    </div>
  </section>

  <!-- SECTION 03: UNDERSTANDING THE EQUATION OF A STRAIGHT LINE -->
  <section id="sec-03" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 03</span>
      <h2 class="section-title">Understanding the Equation of a Straight Line</h2>
    </div>
    <p class="section-intro">
      Every simple linear regression model is built upon the classic algebraic equation for a two-dimensional straight line. Understanding each component of this equation is essential for interpreting machine learning predictions.
    </p>

    <div class="formula-card">
      <div class="formula-title">Fundamental Geometry: Equation of a Straight Line</div>
      <div class="formula-box">y = m &times; x + b &nbsp;&nbsp;&hArr;&nbsp;&nbsp; &#375; = &beta;&#8320; + &beta;&#8321; &times; x</div>
      <div class="formula-desc">
        Where <strong>x</strong> is the independent input, <strong>&#375;</strong> is the predicted target, <strong>m (or &beta;&#8321;)</strong> is the slope (weight), and <strong>b (or &beta;&#8320;)</strong> is the y-intercept (bias).
      </div>
    </div>

    <!-- FIGURE 9.3: LINE OF BEST FIT ANATOMY -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_LINE_OF_BEST_FIT}
      </div>
      <div class="diagram-caption">Figure 9.3: Mathematical anatomy of the line of best fit: The intercept b anchors the height at x = 0, while the slope m governs the rate of rise over run.</div>
    </div>

    <h3>Step-by-Step Numerical Example</h3>
    <p>
      Let us compute predictions manually using a concrete fitted equation: <code>&#375; = 2x + 5</code>. Here, the slope is <code>m = 2</code> and the intercept is <code>b = 5</code>:
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Input Feature (x)</th>
            <th>Step-by-Step Arithmetic</th>
            <th>Predicted Output (&#375;)</th>
            <th>Geometric Interpretation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>x = 1.0</strong></td>
            <td><code>&#375; = 2(1.0) + 5 = 2.0 + 5.0</code></td>
            <td><strong>7.0</strong></td>
            <td>Line passes through coordinates <code>(1.0, 7.0)</code></td>
          </tr>
          <tr>
            <td><strong>x = 3.0</strong></td>
            <td><code>&#375; = 2(3.0) + 5 = 6.0 + 5.0</code></td>
            <td><strong>11.0</strong></td>
            <td>Line passes through coordinates <code>(3.0, 11.0)</code></td>
          </tr>
          <tr>
            <td><strong>x = 5.0</strong></td>
            <td><code>&#375; = 2(5.0) + 5 = 10.0 + 5.0</code></td>
            <td><strong>15.0</strong></td>
            <td>Line passes through coordinates <code>(5.0, 15.0)</code></td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>
      Notice the constant rate of change: for every <code>+2.0</code> unit jump in <code>x</code> (from 1 to 3, and 3 to 5), the predicted target <code>&#375;</code> jumps by exactly <code>+4.0</code> units (from 7 to 11, and 11 to 15). The ratio <code>&Delta;&#375; / &Delta;x = 4.0 / 2.0 = 2.0</code> exactly matches our slope parameter!
    </p>
  </section>

  <!-- SECTION 04: SLOPE AND INTERCEPT IN REAL LIFE -->
  <section id="sec-04" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 04</span>
      <h2 class="section-title">Slope and Intercept in Real Life</h2>
    </div>
    <p class="section-intro">
      In pure mathematics, slope and intercept are abstract geometric numbers. In applied machine learning, however, they represent tangible physical rates and baseline quantities anchored in real-world units.
    </p>

    <!-- FIGURE 9.4: SLOPE AND INTERCEPT VARIATIONS -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_SLOPE_INTERCEPT_VARIATIONS}
      </div>
      <div class="diagram-caption">Figure 9.4: Geometric effects of slope and intercept variations: Positive slope rises, negative slope falls, zero slope is flat, and intercept shifts height in parallel.</div>
    </div>

    <h3>Real-World Example: Student Study Hours vs Exam Score</h3>
    <p>
      Consider a university classroom where we model final exam score (percentage points, 0&ndash;100) based on weekly study hours. Suppose our ordinary least squares model fits the equation:
    </p>

    <div class="formula-card">
      <div class="formula-title">Real-Life Fitted Exam Model</div>
      <div class="formula-box">Predicted_Score = 48.0 + 7.5 &times; Study_Hours</div>
    </div>

    <div class="card card-def">
      <div class="card-title"><span>&#127891;</span> Translating Parameters into Plain English</div>
      <ul>
        <li>
          <strong>Slope (&beta;&#8321; = +7.5 points/hour):</strong> For each additional hour a student studies per week, their expected final exam score increases by <strong>7.5 percentage points</strong>, on average across the class.
        </li>
        <li>
          <strong>Intercept (&beta;&#8320; = 48.0 points):</strong> The baseline score expected for a student who studies <strong>zero hours</strong> (<code>x = 0</code>). This represents the baseline score achievable through general classroom attendance and prior knowledge alone.
        </li>
      </ul>
    </div>

    <h3>Does the Intercept Always Make Physical Sense?</h3>
    <p>
      In many machine learning applications, the intercept is purely mathematical anchoring and has <strong>no sensible physical interpretation</strong> in the real world:
    </p>
    <ul>
      <li><strong>House Area vs Price:</strong> If our fitted model is <code>Price = $55.9k + $0.14 &times; Area</code>, the intercept claims a house with <code>0 sq ft</code> costs $55,900! A house with zero area cannot exist. The intercept simply anchors the line within the observed domain of real houses (e.g., 800 to 3,500 sq ft).</li>
      <li><strong>Human Height vs Weight:</strong> An intercept for height = 0 cm might produce a negative weight (e.g. -45 kg). This is mathematically necessary to fit adult heights accurately, but physically meaningless at zero.</li>
    </ul>
    <p>
      <strong>Rule of Thumb:</strong> Only interpret the intercept physically if the value <code>x = 0</code> is realistically possible and contained within your training data range.
    </p>
  </section>

  <!-- SECTION 05: HOW DOES LINEAR REGRESSION FIND THE BEST-FIT LINE? -->
  <section id="sec-05" class="section-card">
    <div class="section-header">
      <span class="section-badge">Section 05</span>
      <h2 class="section-title">How Does Linear Regression Find the Best-Fit Line?</h2>
    </div>
    <p class="section-intro">
      Beginners often wonder: <em>How does the computer choose one specific line out of an infinite number of possible straight lines?</em> The algorithm does not simply connect the first and last points, nor does it guess randomly. It executes an objective mathematical optimization process.
    </p>

    <!-- FIGURE 9.5: CANDIDATE LINES -->
    <div class="diagram-container">
      <div class="svg-diagram-wrap">
        {SVG_COMPARING_CANDIDATE_LINES}
      </div>
      <div class="diagram-caption">Figure 9.5: Evaluating candidate lines: Ordinary Least Squares (OLS) searches the parameter space to identify Line C, which produces the smallest possible sum of squared errors.</div>
    </div>

    <h3>The 8-Step Machine Learning Optimization Process</h3>
    <ol>
      <li><strong>Ingest Historical Data:</strong> Collect paired training observations <code>(x&#7522;, y&#7522;)</code> for <code>i = 1, ..., n</code>.</li>
      <li><strong>Propose a Candidate Line:</strong> Start with initial parameter values for slope (<code>w</code>) and intercept (<code>b</code>).</li>
      <li><strong>Generate Predictions:</strong> For each training observation <code>x&#7522;</code>, calculate the predicted target: <code>&#375;&#7522; = w &times; x&#7522; + b</code>.</li>
      <li><strong>Compare with Actual Labels:</strong> Measure the difference between ground truth <code>y&#7522;</code> and prediction <code>&#375;&#7522;</code>.</li>
      <li><strong>Calculate Residuals:</strong> Quantify individual vertical prediction errors: <code>e&#7522; = y&#7522; - &#375;&#7522;</code>.</li>
      <li><strong>Aggregate Total Loss:</strong> Square each residual to eliminate negative signs and sum them into a single scalar loss metric: <code>SSE = &Sigma; e&#7522;&#178;</code>.</li>
      <li><strong>Adjust Parameters:</strong> Use calculus (Normal Equations or Gradient Descent) to shift slope and intercept in the direction that reduces SSE.</li>
      <li><strong>Terminate on Optimal Solution:</strong> Stop when no further parameter adjustments can reduce the sum of squared errors.</li>
    </ol>

    <div class="card card-analogy">
      <div class="card-title"><span>&#9878;</span> Why Joining the First and Last Point is a Fatal Mistake</div>
      <p>
        A common novice misconception is assuming a line of best fit simply connects the first observation <code>(x&#8321;, y&#8321;)</code> to the last observation <code>(x&#8345;, y&#8345;)</code>. If either of those boundary points happens to be an extreme outlier or noisy sensor anomaly, the resulting line will pivot violently and misclassify all intermediate points! A true line of best fit considers <strong>all n training points simultaneously</strong>.
      </p>
    </div>
  </section>
"""
