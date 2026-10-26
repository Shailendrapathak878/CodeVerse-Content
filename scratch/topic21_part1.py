# Topic 21 Content - Part 1: Sections 01 to 06
# Strict Light Mode Only, Native HTML Math, Verified Numerical Examples

TOPIC21_PART1 = """
    <!-- HERO HEADER -->
    <header class="hero-header">
      <div class="hero-badge">Topic 21 &bull; Model Generalization &amp; Control</div>
      <h1 class="hero-title">Overfitting, Underfitting &amp; Regularization</h1>
      <p class="hero-subtitle">
        A masterclass on the foundations of machine learning generalization. Master the bias&ndash;variance trade-off, model capacity, polynomial fitting dynamics, Ridge (L2), Lasso (L1), Elastic Net, regularization strength tuning, early stopping, and leakage-safe pipelines.
      </p>
      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <span class="hero-meta-label">Prerequisites</span>
          <span class="hero-meta-val">Basic Python, Linear Regression</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Core Focus</span>
          <span class="hero-meta-val">Generalization &amp; Complexity Control</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Algorithms</span>
          <span class="hero-meta-val">Ridge, Lasso, Elastic Net, Polynomial</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Design Mode</span>
          <span class="hero-meta-val">Strict Light Mode &bull; Accessible</span>
        </div>
      </div>
    </header>

    <!-- TABLE OF CONTENTS -->
    <nav class="toc-card" aria-label="Table of Contents">
      <div class="toc-title">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
        Master Curriculum &bull; 24 Sections
      </div>
      <ul class="toc-grid">
        <li><a class="toc-link" href="#sec-01"><span class="toc-num">01</span> Intro to Model Fitting</a></li>
        <li><a class="toc-link" href="#sec-02"><span class="toc-num">02</span> Underfitting Explained</a></li>
        <li><a class="toc-link" href="#sec-03"><span class="toc-num">03</span> Good Fit &amp; Generalization</a></li>
        <li><a class="toc-link" href="#sec-04"><span class="toc-num">04</span> Overfitting Explained</a></li>
        <li><a class="toc-link" href="#sec-05"><span class="toc-num">05</span> Side-by-Side Comparison</a></li>
        <li><a class="toc-link" href="#sec-06"><span class="toc-num">06</span> Training vs Validation Error</a></li>
        <li><a class="toc-link" href="#sec-07"><span class="toc-num">07</span> Bias &amp; Variance Intuition</a></li>
        <li><a class="toc-link" href="#sec-08"><span class="toc-num">08</span> Bias&ndash;Variance Trade-off</a></li>
        <li><a class="toc-link" href="#sec-09"><span class="toc-num">09</span> Polynomial Regression Complexity</a></li>
        <li><a class="toc-link" href="#sec-10"><span class="toc-num">10</span> Introduction to Regularization</a></li>
        <li><a class="toc-link" href="#sec-11"><span class="toc-num">11</span> L1 Regularization (Lasso)</a></li>
        <li><a class="toc-link" href="#sec-12"><span class="toc-num">12</span> L2 Regularization (Ridge)</a></li>
        <li><a class="toc-link" href="#sec-13"><span class="toc-num">13</span> L1 vs L2 vs Elastic Net</a></li>
        <li><a class="toc-link" href="#sec-14"><span class="toc-num">14</span> Regularization Strength (&alpha;)</a></li>
        <li><a class="toc-link" href="#sec-15"><span class="toc-num">15</span> Feature Scaling &amp; Regularization</a></li>
        <li><a class="toc-link" href="#sec-16"><span class="toc-num">16</span> Other Anti-Overfitting Techniques</a></li>
        <li><a class="toc-link" href="#sec-17"><span class="toc-num">17</span> Early Stopping in Iterative Models</a></li>
        <li><a class="toc-link" href="#sec-18"><span class="toc-num">18</span> Diagnosing with Learning Curves</a></li>
        <li><a class="toc-link" href="#sec-19"><span class="toc-num">19</span> Diagnosing with Validation Curves</a></li>
        <li><a class="toc-link" href="#sec-20"><span class="toc-num">20</span> Safe Selection &amp; Data Leakage</a></li>
        <li><a class="toc-link" href="#sec-21"><span class="toc-num">21</span> Complete Python Practical</a></li>
        <li><a class="toc-link" href="#sec-22"><span class="toc-num">22</span> 15 Common Regularization Pitfalls</a></li>
        <li><a class="toc-link" href="#sec-23"><span class="toc-num">23</span> Quick Revision &amp; Formula Sheet</a></li>
        <li><a class="toc-link" href="#sec-24"><span class="toc-num">24</span> Self-Check Quiz &amp; Technical Q&amp;A</a></li>
      </ul>
    </nav>

    <!-- SECTION 01 -->
    <section id="sec-01" class="content-section">
      <span class="section-tag">Section 01</span>
      <h2 class="section-title">Introduction to Model Fitting</h2>
      <p class="section-intro">
        In machine learning, fitting an algorithm to historical data is only the initial step. The central challenge of artificial intelligence is not memorizing the past, but making accurate, robust predictions on completely new, unseen observations.
      </p>

      <h3>What Does Model Fitting Mean?</h3>
      <p>
        <strong>Model Fitting</strong> (also called <em>training</em>) is the mathematical optimization process where an estimator adjusts its internal parameters &mdash; such as coefficients, intercepts, or decision node split thresholds &mdash; to minimize a defined cost or loss function on a training dataset.
      </p>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Technical Definition: Generalization &amp; Prediction Error
        </div>
        <p>
          <strong>Generalization</strong> is the capacity of a trained machine learning model to maintain low prediction error when evaluated on brand-new observations drawn from the same underlying probability distribution as the training data.
          <br><br>
          A <strong>Prediction Error</strong> is the quantitative discrepancy between the model's predicted output (<strong>&ycirc;</strong>) and the actual ground-truth target (<strong>y</strong>). In regression, this is commonly measured by Mean Squared Error (MSE):
        </p>
        <div class="math-box">
          MSE = (1 / n) &times; &sum;<sub>i=1</sub><sup>n</sup> (y<sub>i</sub> &minus; &ycirc;<sub>i</sub>)&sup2;
        </div>
      </div>

      <div class="card card-analogy">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 1 0 10 10"/></svg>
          Everyday Analogy: The Student Preparing for an Exam
        </div>
        <p>
          Imagine three students preparing for a high-stakes mathematics examination:
          <br><br>
          &bull; <strong>Student A (Underfitting):</strong> Skims the textbook carelessly, fails to learn core mathematical formulas, and cannot even solve basic homework exercises. On exam day, they fail.
          <br>&bull; <strong>Student B (Good Fit):</strong> Studies the fundamental mathematical principles, practices problem-solving logic, and understands how to derive solutions. On exam day, they comfortably solve brand-new problems.
          <br>&bull; <strong>Student C (Overfitting):</strong> Spends 100 hours memorizing the exact answers and typos of 50 specific practice questions without understanding the formulas. On practice tests, they score 100%. But on exam day, when presented with numbers they haven't seen before, they fail catastrophically.
        </p>
      </div>

      <h3>The Three Central Fitting Outcomes</h3>
      <p>
        Depending on the balance between <strong>data volume</strong> and <strong>model complexity</strong>, every supervised learning estimator arrives at one of three fundamental states:
      </p>
      <ul>
        <li><strong>Underfitting:</strong> The model is too simple or restrictive to capture the underlying data patterns (High Bias).</li>
        <li><strong>Good Fit:</strong> The model captures the underlying signal while disregarding random sample noise (Optimal Generalization).</li>
        <li><strong>Overfitting:</strong> The model is excessively flexible and fits the training data's random quirks and noise, destroying generalization (High Variance).</li>
      </ul>

      <!-- FIGURE 1.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 1.1 &bull; Model Fitting, Capacity, and Generalization Lifecycle</span>
          <span class="visual-tag">System Architecture</span>
        </div>
        __SVG_FIT_WORKFLOW__
        <div class="visual-caption">
          Figure 1.1: The end-to-end model fitting lifecycle. Historical training data guides parameter optimization; the chosen model capacity dictates whether the system underfits, achieves good fit, or overfits; unseen test data delivers the final unbiased generalization verdict.
        </div>
      </div>
    </section>

    <!-- SECTION 02 -->
    <section id="sec-02" class="content-section">
      <span class="section-tag">Section 02</span>
      <h2 class="section-title">Underfitting Explained</h2>
      <p class="section-intro">
        Underfitting occurs when a machine learning model is too simple, rigid, or constrained to capture the fundamental relationship governing the data.
      </p>

      <h3>Intuition: Forcing a Straight Line onto a Curve</h3>
      <p>
        Consider predicting house prices where the true relationship with square footage is non-linear (e.g., diminishing returns for extremely large mansions). If you force a simple straight line (Linear Regression with degree 1) onto this curved data:
      </p>
      <ul>
        <li>For small homes, the line consistently underpredicts.</li>
        <li>For medium homes, the line consistently overpredicts.</li>
        <li>For large homes, the line consistently underpredicts again.</li>
      </ul>
      <p>
        Because the mathematical hypothesis class is inherently incapable of bending, the model makes systematic errors across the entire domain.
      </p>

      <!-- FIGURE 2.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 2.1 &bull; Underfitting: Linear Model Forced onto Non-Linear Curved Data</span>
          <span class="visual-tag">High Bias</span>
        </div>
        __SVG_UNDERFITTING_DEMO__
        <div class="visual-caption">
          Figure 2.1: Underfitting in action. The rigid straight line (red) fails to capture the true underlying cosine curve (dashed gray), producing large systematic residuals across both the training set and validation sets.
        </div>
      </div>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Quantitative Symptoms of Underfitting
        </div>
        <p>
          &bull; <strong>High Training Error:</strong> Even on the very data it was fitted on, the model achieves poor performance (e.g., Train MSE = 0.1868, R&sup2; = 0.638).
          <br>&bull; <strong>High Validation / Test Error:</strong> Unseen data also suffers from high error (e.g., Test MSE = 0.2884, R&sup2; = 0.105).
          <br>&bull; <strong>Small Generalization Gap:</strong> The gap between training error and validation error is relatively small, but both errors are unacceptably high.
        </p>
      </div>

      <h3>How to Cure Underfitting</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Remedy</th>
              <th>How It Helps</th>
              <th>Concrete Actionable Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Increase Model Complexity</strong></td>
              <td>Expands the hypothesis space to represent non-linear relationships.</td>
              <td>Upgrade from simple Linear Regression to Polynomial Features (Degree 2 or 3), or increase tree depth.</td>
            </tr>
            <tr>
              <td><strong>Engineer Informative Features</strong></td>
              <td>Provides the model with predictive signals directly correlated with target variance.</td>
              <td>Add interaction terms, domain-specific ratios, or non-linear transforms (e.g. log(income)).</td>
            </tr>
            <tr>
              <td><strong>Reduce Regularization Penalty</strong></td>
              <td>Relaxes the penalty constraints that are forcing model parameters toward zero.</td>
              <td>Decrease Ridge or Lasso penalty parameter (&alpha; or &lambda;) from 100.0 to 0.01.</td>
            </tr>
            <tr>
              <td><strong>Train for More Epochs</strong></td>
              <td>Allows iterative gradient-based optimizers sufficient steps to converge.</td>
              <td>Increase <code>max_iter</code> in SGD, Logistic Regression, or Neural Networks.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Warning: Adding Complexity Is Not a Universal Magic Wand
        </div>
        <p>
          Do not assume that if a model underfits, you should immediately jump to a 50-layer deep neural network!
          <br>
          If the underlying data is noisy or the dataset is tiny (N = 30), leaping from a straight line straight to an unconstrained high-degree polynomial will cause the model to swing instantly from severe underfitting to catastrophic <strong>overfitting</strong>.
        </p>
      </div>
    </section>

    <!-- SECTION 03 -->
    <section id="sec-03" class="content-section">
      <span class="section-tag">Section 03</span>
      <h2 class="section-title">Good Fit and Generalization</h2>
      <p class="section-intro">
        A <strong>Good Fit</strong> (also known as the <em>Goldilocks state</em> or optimal generalization) captures the true underlying physical or mathematical signal while remaining impervious to idiosyncratic sample noise.
      </p>

      <h3>What Does a Useful Fitted Model Look Like?</h3>
      <p>
        In the real world, every dataset is composed of two distinct components:
      </p>
      <div class="math-box">
        Observed Target (y) = True Underlying Signal f(X) + Random Noise (&epsilon;)
      </div>
      <p>
        The objective of machine learning is <strong>never</strong> to achieve 0.0 training error, because achieving 0.0 error means the model has memorized the random noise (&epsilon;).
        <br>
        A good fit learns <em>f(X)</em> while letting the noise pass through unmodeled.
      </p>

      <!-- FIGURE 3.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 3.1 &bull; Good Fit: Optimal Model Capturing Underlying Signal without Noise</span>
          <span class="visual-tag">Balanced Model</span>
        </div>
        __SVG_GOODFIT_DEMO__
        <div class="visual-caption">
          Figure 3.1: A well-generalized cubic polynomial fit (green curve). The curve captures the smooth non-linear curvature without contorting itself to hit individual scattered noise points.
        </div>
      </div>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Quantitative Signatures of a Good Fit
        </div>
        <p>
          &bull; <strong>Low Training Error:</strong> Fits the training samples accurately (e.g., Train MSE = 0.0176, R&sup2; = 0.9660).
          <br>&bull; <strong>Low Validation Error:</strong> Performs equally well on unseen samples (e.g., Test MSE = 0.0178, R&sup2; = 0.9448).
          <br>&bull; <strong>Negligible Generalization Gap:</strong> The gap between training and test error is virtually zero (|0.0178 &minus; 0.0176| = 0.0002).
          <br>&bull; <strong>Parameter Stability:</strong> Learned weights remain modest and realistic (e.g., max coefficient &asymp; 9.84).
        </p>
      </div>
    </section>

    <!-- SECTION 04 -->
    <section id="sec-04" class="content-section">
      <span class="section-tag">Section 04</span>
      <h2 class="section-title">Overfitting Explained</h2>
      <p class="section-intro">
        <strong>Overfitting</strong> is the most common failure mode in applied machine learning. It occurs when a model possesses excessive mathematical flexibility relative to the amount of training data available, allowing it to memorize noise, outliers, and accidental correlations.
      </p>

      <h3>How Overfitting Happens</h3>
      <p>
        Suppose we fit a 10th-degree polynomial to our 30 training samples. Because a 10th-degree polynomial has 11 free parameters (slopes for x, x&sup2;, x&sup3;... x&sup1;&deg; plus intercept), it has enough mathematical degrees of freedom to zig-zag violently through every single individual data point.
      </p>

      <!-- FIGURE 4.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 4.1 &bull; Overfitting: High-Capacity Model Interpolating Training Noise</span>
          <span class="visual-tag">High Variance</span>
        </div>
        __SVG_OVERFITTING_DEMO__
        <div class="visual-caption">
          Figure 4.1: Overfitting demonstrated. The 10th-degree polynomial (purple) violently contorts itself to pass through every noisy training sample. Notice the wild, uncontrolled oscillations at the boundary regions &mdash; predictions here will fail catastrophically!
        </div>
      </div>

      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Quantitative Symptoms of Overfitting
        </div>
        <p>
          &bull; <strong>Suspiciously Low Training Error:</strong> Near-perfect score on training samples (e.g., Train MSE = 0.0105, R&sup2; = 0.9797).
          <br>&bull; <strong>Exploding Validation / Test Error:</strong> Massive error on unseen observations (e.g., Test MSE rises to 0.0244+).
          <br>&bull; <strong>Wide Generalization Gap:</strong> Significant divergence between training and test error.
          <br>&bull; <strong>Exploding Coefficient Magnitudes:</strong> To cancel each other out during wild oscillations, polynomial weights explode to enormous numbers (in our executed run, weights hit <strong>&plusmn;3,533.32!</strong>).
        </p>
      </div>

      <h3>Why Overfitting is Not Just About Model Type</h3>
      <p>
        Overfitting is fundamentally a relationship between <strong>model capacity</strong> and <strong>data quantity</strong>:
      </p>
      <ul>
        <li>A complex model (e.g. 50-tree Random Forest) will easily overfit on <strong>50 samples</strong>.</li>
        <li>That exact same model will generalize beautifully without overfitting on <strong>500,000 samples</strong>, because the vast volume of data constrains the model from memorizing individual points.</li>
      </ul>
    </section>

    <!-- SECTION 05 -->
    <section id="sec-05" class="content-section">
      <span class="section-tag">Section 05</span>
      <h2 class="section-title">Underfitting vs Good Fit vs Overfitting: Side-by-Side</h2>
      <p class="section-intro">
        Let us directly compare all three fitting regimes on the exact same dataset to cement the conceptual differences.
      </p>

      <!-- FIGURE 5.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 5.1 &bull; Side-by-Side Comparison: Underfit vs Good Fit vs Overfit on Identical Data</span>
          <span class="visual-tag">Comparative Analysis</span>
        </div>
        __SVG_SIDE_BY_SIDE_FIT__
        <div class="visual-caption">
          Figure 5.1: Three models fitted to identical training data. Left (Underfitting): Too rigid, misses true curvature. Center (Good Fit): Smoothly captures fundamental pattern. Right (Overfitting): Hyper-flexible, memorizes random noise.
        </div>
      </div>

      <h3>Comprehensive Tri-State Comparison Table</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Property</th>
              <th>Underfitting</th>
              <th>Good Fit (Optimal)</th>
              <th>Overfitting</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Hypothesis Complexity</strong></td>
              <td>Too limited / overly simplistic</td>
              <td>Appropriate for underlying signal</td>
              <td>Excessively flexible / high capacity</td>
            </tr>
            <tr>
              <td><strong>Training Error</strong></td>
              <td>High (e.g., MSE = 0.187)</td>
              <td>Low (e.g., MSE = 0.018)</td>
              <td>Near Zero (e.g., MSE = 0.010)</td>
            </tr>
            <tr>
              <td><strong>Validation Error</strong></td>
              <td>High (e.g., MSE = 0.288)</td>
              <td>Low (e.g., MSE = 0.018)</td>
              <td>High / Unstable (e.g., MSE = 0.024+)</td>
            </tr>
            <tr>
              <td><strong>Generalization Gap</strong></td>
              <td>Small (Both errors high)</td>
              <td>Minimal (Near zero gap)</td>
              <td><strong>Large &amp; Widening</strong></td>
            </tr>
            <tr>
              <td><strong>Statistical Diagnosis</strong></td>
              <td>High Bias, Low Variance</td>
              <td>Balanced Bias &amp; Variance</td>
              <td>Low Bias, High Variance</td>
            </tr>
            <tr>
              <td><strong>Primary Remedy</strong></td>
              <td>Increase model capacity, add features</td>
              <td>Deploy model; monitor for drift</td>
              <td>Regularize (Ridge/Lasso), prune, collect data</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 06 -->
    <section id="sec-06" class="content-section">
      <span class="section-tag">Section 06</span>
      <h2 class="section-title">Training Error vs Validation Error</h2>
      <p class="section-intro">
        Tracking training error alone is like asking a student to grade their own practice homework. Tracking validation error alongside training error reveals the model's true trajectory.
      </p>

      <h3>The Generalization Gap Formula</h3>
      <div class="card card-def">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Technical Definition: Generalization Gap
        </div>
        <p>
          The <strong>Generalization Gap</strong> is the quantitative margin between error on unseen validation data and error on training data:
        </p>
        <div class="math-box">
          Generalization Gap = Validation Error &minus; Training Error
        </div>
        <p>
          As an estimator's capacity expands:
          <br>&bull; <strong>Training Error:</strong> Monotonically decreases toward zero. A sufficiently complex model can achieve 100% training accuracy or 0.0 training MSE.
          <br>&bull; <strong>Validation Error:</strong> Follows a distinct <strong>U-shaped trajectory</strong>. It initially declines as the model learns real signal, reaches a minimum at the optimal complexity level, and then ascends steeply as the model starts fitting noise.
        </p>
      </div>

      <!-- FIGURE 6.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">Figure 6.1 &bull; Training Error vs Validation Error as Model Complexity Grows</span>
          <span class="visual-tag">Error Dynamics</span>
        </div>
        __SVG_TRAIN_VAL_ERROR_CURVE__
        <div class="visual-caption">
          Figure 6.1: Error dynamics across model complexity. Training error (blue) continually declines toward zero. Validation error (red) forms a U-curve, hitting a global minimum in the green Sweet Spot corridor before climbing steeply as the Generalization Gap expands.
        </div>
      </div>

      <div class="card card-warn">
        <div class="card-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          Why You Must Never Pick Complexity Using the Test Set
        </div>
        <p>
          Notice in Figure 6.1 that we identify the sweet spot using <strong>cross-validation or a dedicated validation split</strong>.
          <br>
          If you evaluate 20 different complexity levels against your <em>final test set</em> and pick the lowest point, the test set has contaminated your model selection process! The resulting reported error will be artificially optimistic.
        </p>
      </div>
    </section>
"""
