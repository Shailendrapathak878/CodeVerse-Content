"""
Topic 13: Support Vector Machine (SVM) - Part 2
Contains Sections 6 to 10.
"""

from scratch.topic13_svgs import (
    SVG_LINEAR_SVM_SEPARABLE,
    SVG_HARD_VS_SOFT_MARGIN,
    SVG_C_PARAMETER_COMPARISON
)

TOPIC13_PART2 = """
  <!-- SECTION 6 -->
  <section id="sec-06" class="section-card">
    <div class="section-badge">Section 06</div>
    <h2 class="section-title">Hard Margin vs. Soft Margin: The Slack Variable (ξ)</h2>
    <p class="section-lead">
      In an ideal textbook world, data points of different classes are cleanly separated with empty space in between. 
      In real-world engineering, datasets contain sensor glitches, mislabelled records, human error, and natural overlap. 
      How does SVM survive when clean linear separation is impossible?
    </p>

    <div class="figure-container">
      __SVG_LINEAR_SVM_SEPARABLE__
      <div class="figure-caption">
        <strong>Figure 13.5: Hard Margin on Linearly Separable Data.</strong> When data is pristine, hard margin conditions hold: every training point satisfies <code>yᵢ(wᵀxᵢ + b) &ge; 1</code> with zero violations.
      </div>
    </div>

    <h3 class="sub-title">1. The Hard Margin Optimization Problem</h3>
    <p>
      In a <strong>Hard Margin SVM</strong>, we require that every single training observation must lie on the correct side of its respective canonical margin plane:
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; Hard Margin Objective &amp; Constraints</div>
      <div class="math-display">min_{w, b} &nbsp; ½ ∥w∥² &nbsp;&nbsp; subject to: &nbsp;&nbsp; yᵢ(wᵀxᵢ + b) ≥ 1 &nbsp;&nbsp; (for all i = 1, ..., N)</div>
      <div class="formula-legend">
        <div class="legend-item"><span class="legend-symbol">min ½∥w∥²</span><span>Equivalent to maximizing total margin width 2/∥w∥</span></div>
        <div class="legend-item"><span class="legend-symbol">y_i &isin; {-1, +1}</span><span>True binary class label of observation i</span></div>
        <div class="legend-item"><span class="legend-symbol">&ge; 1</span><span>Demands that all points sit outside or on the margin corridor</span></div>
      </div>
    </div>

    <div class="warn-box">
      <div class="warn-title"><span>&#9888;&#65039;</span> The Fatal Flaw of Hard Margin SVM</div>
      <p>
        Hard margin SVM has two fatal limitations in practical machine learning:
      </p>
      <ul style="margin-left: 1.5rem; margin-top: 0.5rem; color: var(--warn-card-text);">
        <li><strong>No Mathematical Solution on Overlapping Data:</strong> If even a single Class 1 observation falls inside the Class 0 cloud, no line can satisfy the constraints. The optimization solver crashes with an infeasible error.</li>
        <li><strong>Extreme Outlier Sensitivity:</strong> Even if separable, a single rogue outlier located far from its cluster will force the boundary to tilt wildly, ruining test generalization.</li>
      </ul>
    </div>

    <h3 class="sub-title">2. Soft Margin SVM &amp; Slack Variables (ξᵢ)</h3>
    <p>
      To solve this dilemma, Vladimir Vapnik and Corinna Cortes introduced the <strong>Soft Margin SVM</strong>. 
      They introduced a slack variable <strong>&xi;ᵢ (xi)</strong> for each training sample, representing the distance by which point <code>x_i</code> violates the ideal margin boundary.
    </p>

    <div class="figure-container">
      __SVG_HARD_VS_SOFT_MARGIN__
      <div class="figure-caption">
        <strong>Figure 13.6: Hard Margin vs. Soft Margin with Slack Variables.</strong> Soft margin SVM introduces slack penalties <code>&xi;ᵢ &ge; 0</code>. Points inside the margin corridor (<code>0 &lt; &xi;ᵢ &le; 1</code>) or misclassified points (<code>&xi;ᵢ &gt; 1</code>) are penalized by factor <code>C</code>, keeping the boundary stable.
      </div>
    </div>

    <h3 class="sub-title">3. Interpreting the Three Slack Conditions</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Slack Value</th>
            <th>Point Location</th>
            <th>Classification Status</th>
            <th>Support Vector Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>&xi;ᵢ = 0</code></td>
            <td>On or beyond the correct margin plane</td>
            <td>Correctly classified with full margin clearance</td>
            <td>Non-support vector (if beyond margin) or margin support vector (if exactly on plane)</td>
          </tr>
          <tr>
            <td><code>0 &lt; &xi;ᵢ &le; 1</code></td>
            <td>Inside the margin corridor, but on the correct side of the hyperplane</td>
            <td>Correctly classified, but with reduced safety margin</td>
            <td><strong>Support Vector</strong> (violating margin)</td>
          </tr>
          <tr>
            <td><code>&xi;ᵢ &gt; 1</code></td>
            <td>Across the decision hyperplane on the wrong side</td>
            <td><strong>Misclassified training error</strong></td>
            <td><strong>Support Vector</strong> (violating decision boundary)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 7 -->
  <section id="sec-07" class="section-card">
    <div class="section-badge">Section 07</div>
    <h2 class="section-title">Understanding the C Regularization Parameter</h2>
    <p class="section-lead">
      In scikit-learn, the trade-off between margin width and training violations is governed by a single, critical hyperparameter: <strong><code>C</code></strong>. 
      Understanding how <code>C</code> behaves is essential for tuning high-performance SVM models.
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; The Soft-Margin Optimization Objective</div>
      <div class="math-display">min_{w, b, ξ} &nbsp; ( ½ ∥w∥² + C ∑_{i=1}^{N} ξᵢ ) &nbsp;&nbsp; subject to: &nbsp;&nbsp; yᵢ(wᵀxᵢ + b) ≥ 1 - ξᵢ, &nbsp; ξᵢ ≥ 0</div>
      <div class="formula-legend">
        <div class="legend-item"><span class="legend-symbol">½∥w∥²</span><span>Regularization term: seeks a wider margin (simpler model)</span></div>
        <div class="legend-item"><span class="legend-symbol">C &sum; &xi;ᵢ</span><span>Loss penalty term: penalizes training margin violations</span></div>
        <div class="legend-item"><span class="legend-symbol">C</span><span>Regularization hyperparameter balancing the two opposing forces</span></div>
      </div>
    </div>

    <div class="figure-container">
      __SVG_C_PARAMETER_COMPARISON__
      <div class="figure-caption">
        <strong>Figure 13.7: Decision Boundaries and Margins Across C Values.</strong> Small <code>C = 0.1</code> allows more slack violations (78 SVs) to preserve a wide margin. Large <code>C = 10.0</code> enforces a strict penalty (23 SVs), yielding a narrow boundary vulnerable to overfitting.
      </div>
    </div>

    <h3 class="sub-title">1. The C Parameter Tug-of-War</h3>
    <p>
      Think of <code>C</code> as a dial that controls how strictly the algorithm punishes training mistakes:
    </p>
    <div class="grid-2col">
      <div class="def-box">
        <div class="def-title"><span>&#128313;</span> Small C (e.g. C = 0.01 or 0.1)</div>
        <p><strong>Philosophy:</strong> "A wide margin is far more important than a few training mistakes."</p>
        <ul style="margin-left: 1.25rem; font-size: 0.92rem; color: var(--def-card-text);">
          <li>Tolerates many slack violations (&xi;ᵢ &gt; 0).</li>
          <li>Produces a <strong>wider margin</strong> corridor.</li>
          <li>Selects <strong>more support vectors</strong> (e.g., 78 out of 192).</li>
          <li><strong>High bias, low variance</strong> (prevents overfitting on noisy data).</li>
        </ul>
      </div>

      <div class="warn-box">
        <div class="warn-title"><span>&#128314;</span> Large C (e.g. C = 10 or 100)</div>
        <p><strong>Philosophy:</strong> "Every single training mistake must be heavily penalized!"</p>
        <ul style="margin-left: 1.25rem; font-size: 0.92rem; color: var(--warn-card-text);">
          <li>Severely punishes slack violations (&xi;ᵢ).</li>
          <li>Produces a <strong>narrower margin</strong> corridor.</li>
          <li>Selects <strong>fewer support vectors</strong> (e.g., 23 out of 192).</li>
          <li><strong>Low bias, high variance</strong> (risks fitting to outliers).</li>
        </ul>
      </div>
    </div>

    <h3 class="sub-title">2. Empirical Results on Our Training Set</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>C Value</th>
            <th>Support Vector Count</th>
            <th>% of Training Set (N=192)</th>
            <th>Training Accuracy</th>
            <th>Holdout Test Accuracy</th>
            <th>Model Behavioral Tendency</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>C = 0.1</code></td>
            <td><strong>78</strong></td>
            <td>40.6%</td>
            <td>97.40%</td>
            <td><strong>93.75%</strong></td>
            <td>Wide, relaxed margin corridor; resilient to training noise.</td>
          </tr>
          <tr>
            <td><code>C = 1.0</code></td>
            <td><strong>32</strong></td>
            <td>16.7%</td>
            <td>96.88%</td>
            <td><strong>91.67%</strong></td>
            <td>Balanced default; optimal trade-off for standard distributions.</td>
          </tr>
          <tr>
            <td><code>C = 10.0</code></td>
            <td><strong>23</strong></td>
            <td>12.0%</td>
            <td>97.40%</td>
            <td><strong>93.75%</strong></td>
            <td>Narrow, rigid margin; penalizes margin intruders aggressively.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 8 -->
  <section id="sec-08" class="section-card">
    <div class="section-badge">Section 08</div>
    <h2 class="section-title">Linear SVM Architecture</h2>
    <p class="section-lead">
      When your data is approximately linearly separable, or when the number of features is extremely large (such as text classification with thousands of TF-IDF word tokens), a <strong>Linear SVM</strong> is often the fastest, most effective classifier available.
    </p>

    <h3 class="sub-title">1. SVC(kernel="linear") vs. LinearSVC in Scikit-Learn</h3>
    <p>
      Beginners frequently encounter two different classes in scikit-learn for linear support vector classification. 
      While both construct a linear hyperplane, their underlying C++ implementations differ fundamentally:
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Implementation Feature</th>
            <th><code>SVC(kernel="linear")</code></th>
            <th><code>LinearSVC</code></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Underlying C++ Engine</strong></td>
            <td><code>libsvm</code></td>
            <td><code>liblinear</code></td>
          </tr>
          <tr>
            <td><strong>Optimization Formulation</strong></td>
            <td>Solves the <strong>Dual Problem</strong> (using quadratic programming).</td>
            <td>Solves the <strong>Primal Problem</strong> directly via coordinate descent.</td>
          </tr>
          <tr>
            <td><strong>Training Scalability</strong></td>
            <td>O(N²) to O(N³) with sample count N. Slower for N &gt; 50,000.</td>
            <td>O(N &times; D) linear scaling. Extremely fast on huge datasets.</td>
          </tr>
          <tr>
            <td><strong>Access to Support Vectors</strong></td>
            <td><strong>Yes:</strong> <code>.support_vectors_</code>, <code>.support_</code></td>
            <td><strong>No:</strong> Does not store explicit support vector indices.</td>
          </tr>
          <tr>
            <td><strong>Default Loss Function</strong></td>
            <td>Hinge Loss (standard SVM)</td>
            <td>Squared Hinge Loss (differentiable for fast gradient descent)</td>
          </tr>
          <tr>
            <td><strong>Recommended Use Case</strong></td>
            <td>Educational inspection, moderate datasets (N &lt; 20,000).</td>
            <td>Production text/document classification with massive feature spaces.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 9 -->
  <section id="sec-09" class="section-card">
    <div class="section-badge">Section 09</div>
    <h2 class="section-title">What If the Classes Are Not Linearly Separable?</h2>
    <p class="section-lead">
      Real-world data rarely arranges itself into neat, straight bands. 
      What happens when data points form concentric rings, complex spirals, or XOR patterns? 
      A straight line cannot separate them—any linear model is doomed to fail.
    </p>

    <div class="analogy-box">
      <div class="analogy-title">
        <span>&#128161;</span> The Magic Table Trick: Lifting Data into 3D Space
      </div>
      <p>
        Imagine you place blue marbles in the center of a dinner table and surround them with a ring of red marbles. 
        If you are only allowed to lay a straight wooden ruler flat on the tabletop, you can never separate the blue marbles from the red ones! 
        Every straight cut groups red and blue marbles together.
      </p>
      <p style="margin-top: 0.5rem;">
        Now imagine you tap the underside of the table right beneath the center. 
        The blue marbles launch upward into the air, while the heavier red marbles stay on the table. 
        While the blue marbles are suspended in 3D space, you can effortlessly slide a flat cardboard sheet horizontally beneath the floating blue marbles! 
        A problem that was <strong>impossible in 2D</strong> became <strong>trivially linear in 3D</strong>.
      </p>
    </div>

    <h3 class="sub-title">1. Explicit Feature Mapping Example</h3>
    <p>
      Suppose we have 1D points on a line: negative samples at <code>x = -2, +2</code> and positive samples at <code>x = -1, 0, +1</code>. 
      No single cut point can isolate the positive samples. 
      However, if we create a new feature <code>z = x²</code>:
    </p>
    <ul style="margin-left: 1.5rem; margin-top: 0.5rem; color: var(--text-secondary);">
      <li>Positive points <code>x &isin; {-1, 0, 1} &rarr; z &isin; {1, 0, 1}</code> (all z &le; 1).</li>
      <li>Negative points <code>x &isin; {-2, 2} &rarr; z &isin; {4, 4}</code> (all z &ge; 4).</li>
    </ul>
    <p style="margin-top: 0.5rem;">
      In the new <code>z</code> space, a simple linear threshold at <code>z = 2.5</code> perfectly separates the classes!
    </p>
  </section>

  <!-- SECTION 10 -->
  <section id="sec-10" class="section-card">
    <div class="section-badge">Section 10</div>
    <h2 class="section-title">The Kernel Trick and Important Kernels</h2>
    <p class="section-lead">
      Manually mapping features into higher dimensions is computationally disastrous. 
      If we mapped a 100-feature image into a 10th-degree polynomial space, we would generate billions of synthetic features, exhausting all computer memory! 
      This is where the mathematical miracle called the <strong>Kernel Trick</strong> saves the day.
    </p>

    <h3 class="sub-title">1. What Is the Kernel Trick?</h3>
    <p>
      When solving the mathematical dual formulation of SVM, the algorithm never needs to know the individual coordinates of points in the high-dimensional space! 
      It only ever computes the <strong>dot product (inner product)</strong> between pairs of points: <code>⟨&phi;(x), &phi;(z)⟩</code>.
    </p>
    <p>
      A <strong>kernel function K(x, z)</strong> is a mathematical shortcut that computes this exact high-dimensional dot product directly using the original, low-dimensional coordinates, <strong>without ever actually projecting the data into higher dimensions!</strong>
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; The Three Primary SVM Kernels</div>
      
      <div class="math-display">K(x, z) = xᵀz &nbsp;&nbsp;&nbsp;&nbsp; (Linear Kernel)</div>
      <p style="text-align:center; font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1rem;">Measures standard Euclidean inner product. Constructs linear hyperplanes.</p>

      <div class="math-display">K(x, z) = (γ xᵀz + r)ᵈ &nbsp;&nbsp;&nbsp;&nbsp; (Polynomial Kernel)</div>
      <p style="text-align:center; font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1rem;">Constructs curved, elliptical, or interaction-based decision manifolds of degree d.</p>

      <div class="math-display">K(x, z) = exp( -γ ∥x - z∥² ) &nbsp;&nbsp;&nbsp;&nbsp; (RBF Kernel)</div>
      <p style="text-align:center; font-size: 0.88rem; color: var(--text-muted);">Computes Gaussian similarity decaying with squared Euclidean distance. Equivalent to an infinite-dimensional feature space!</p>
    </div>

    <h3 class="sub-title">2. Kernel Parameter Breakdown</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Kernel Name</th>
            <th>Scikit-Learn Setting</th>
            <th>Key Hyperparameters</th>
            <th>Mathematical Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Linear</strong></td>
            <td><code>kernel='linear'</code></td>
            <td><code>C</code></td>
            <td>Computes direct dot product <code>xᵀz</code>. Fast, interpretable, ideal for high dimensions.</td>
          </tr>
          <tr>
            <td><strong>Polynomial</strong></td>
            <td><code>kernel='poly'</code></td>
            <td><code>degree=d</code>, <code>gamma=&gamma;</code>, <code>coef0=r</code></td>
            <td>Projects into polynomial feature interactions up to degree <code>d</code>.</td>
          </tr>
          <tr>
            <td><strong>RBF (Gaussian)</strong></td>
            <td><code>kernel='rbf'</code></td>
            <td><code>C</code>, <code>gamma=&gamma;</code></td>
            <td>Measures local similarity. Points close together have <code>K(x,z) &approx; 1</code>; points far apart have <code>K(x,z) &rarr; 0</code>.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3 class="sub-title">3. Concrete Worked Kernel Calculations</h3>
    <div class="calc-box">
      <div class="calc-step">
        <div class="step-title">Given Two Observations in 2D Space:</div>
        <p>Let <code>x = [2.0, 3.0]ᵀ</code> and <code>z = [4.0, 1.0]ᵀ</code>.</p>
      </div>
      <div class="calc-step">
        <div class="step-title">1. Linear Kernel:</div>
        <p><code>K(x, z) = xᵀz = (2.0 &times; 4.0) + (3.0 &times; 1.0) = 8.0 + 3.0 = 11.0000</code></p>
      </div>
      <div class="calc-step">
        <div class="step-title">2. Polynomial Kernel (with &gamma;=1.0, r=1.0, d=2):</div>
        <p><code>K(x, z) = (1.0 &times; 11.0 + 1.0)² = (12.0)² = 144.0000</code></p>
      </div>
      <div class="calc-step">
        <div class="step-title">3. RBF Gaussian Kernel (with &gamma;=0.1):</div>
        <p>Squared distance: <code>∥x - z∥² = (2 - 4)² + (3 - 1)² = (-2)² + 2² = 4 + 4 = 8.0000</code></p>
        <p><code>K(x, z) = exp(-0.1 &times; 8.0) = exp(-0.8000) = 0.4493</code></p>
      </div>
    </div>
  </section>
"""
