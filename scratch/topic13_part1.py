"""
Topic 13: Support Vector Machine (SVM) - Part 1
Contains Hero, TOC, and Sections 1 to 5.
"""

from scratch.topic13_svgs import (
    SVG_TWO_CLASS_HYPERPLANE,
    SVG_MAXIMUM_MARGIN,
    SVG_ACTUAL_SUPPORT_VECTORS,
    SVG_NARROW_VS_WIDE_MARGIN
)

TOPIC13_PART1 = """
  <!-- HERO HEADER -->
  <header class="hero-card">
    <div class="hero-topic-badge">Supervised Machine Learning &bull; Topic 13</div>
    <h1 class="hero-title">Support Vector Machine (SVM): Complete Beginner Guide</h1>
    <p class="hero-subtitle">
      Master one of the most mathematically elegant, powerful, and versatile algorithms in supervised machine learning. 
      Understand how hyperplanes separate complex datasets, why maximum-margin boundaries provide superior generalization, 
      how soft-margin slack parameters balance noise, and how the revolutionary kernel trick projects non-linear patterns into higher dimensions.
    </p>

    <div class="meta-bar">
      <span class="meta-pill">&#128218; 23 Comprehensive Sections</span>
      <span class="meta-pill">&#9889; 15 Hand-Crafted Vector Diagrams</span>
      <span class="meta-pill">&#128300; Verified Scikit-Learn Pipelines</span>
      <span class="meta-pill">&#9878;&#65039; Strict Light Mode Only</span>
      <span class="meta-pill">&#127919; 100% Mobile &amp; Desktop Tested</span>
    </div>
  </header>

  <!-- TABLE OF CONTENTS -->
  <nav class="toc-card" aria-label="Topic Navigation">
    <div class="toc-title">
      <span>&#128203;</span> Table of Contents &bull; Topic 13 Roadmap
    </div>
    <div class="toc-grid">
      <a href="#sec-01" class="toc-link"><span class="toc-num">01</span> Introduction to SVM</a>
      <a href="#sec-02" class="toc-link"><span class="toc-num">02</span> What Is a Hyperplane?</a>
      <a href="#sec-03" class="toc-link"><span class="toc-num">03</span> Understanding the Margin</a>
      <a href="#sec-04" class="toc-link"><span class="toc-num">04</span> What Are Support Vectors?</a>
      <a href="#sec-05" class="toc-link"><span class="toc-num">05</span> Maximum Margin Intuition</a>
      <a href="#sec-06" class="toc-link"><span class="toc-num">06</span> Hard Margin vs. Soft Margin</a>
      <a href="#sec-07" class="toc-link"><span class="toc-num">07</span> The C Regularization Parameter</a>
      <a href="#sec-08" class="toc-link"><span class="toc-num">08</span> Linear SVM Architecture</a>
      <a href="#sec-09" class="toc-link"><span class="toc-num">09</span> Non-Linear Class Separability</a>
      <a href="#sec-10" class="toc-link"><span class="toc-num">10</span> The Kernel Trick &amp; Kernels</a>
      <a href="#sec-11" class="toc-link"><span class="toc-num">11</span> Visualizing Kernel Manifolds</a>
      <a href="#sec-12" class="toc-link"><span class="toc-num">12</span> Understanding Gamma (γ)</a>
      <a href="#sec-13" class="toc-link"><span class="toc-num">13</span> Feature Scaling for SVM</a>
      <a href="#sec-14" class="toc-link"><span class="toc-num">14</span> SVM Practical Workflow</a>
      <a href="#sec-15" class="toc-link"><span class="toc-num">15</span> Complete Python Classification Lab</a>
      <a href="#sec-16" class="toc-link"><span class="toc-num">16</span> SVM Regression: SVR</a>
      <a href="#sec-17" class="toc-link"><span class="toc-num">17</span> Classification Metrics &amp; Confusion Matrix</a>
      <a href="#sec-18" class="toc-link"><span class="toc-num">18</span> Advantages &amp; Limitations</a>
      <a href="#sec-19" class="toc-link"><span class="toc-num">19</span> SVM Compared With Other Models</a>
      <a href="#sec-20" class="toc-link"><span class="toc-num">20</span> Real-Life Case Studies</a>
      <a href="#sec-21" class="toc-link"><span class="toc-num">21</span> Diagram &amp; Visual Gallery</a>
      <a href="#sec-22" class="toc-link"><span class="toc-num">22</span> 12 Common Beginner Mistakes</a>
      <a href="#sec-23" class="toc-link"><span class="toc-num">23</span> Summary, Glossary &amp; Revision</a>
    </div>
  </nav>

  <!-- SECTION 1 -->
  <section id="sec-01" class="section-card">
    <div class="section-badge">Section 01</div>
    <h2 class="section-title">Introduction to Support Vector Machines (SVM)</h2>
    <p class="section-lead">
      Imagine you are a teacher separating students into two distinct study groups based on exam performance and project submissions. 
      You could draw dozens of lines between the two groups. But which line gives both groups the widest possible breathing room so that future students are not unfairly grouped? 
      This fundamental quest for the widest safety corridor is the essence of a <strong>Support Vector Machine (SVM)</strong>.
    </p>

    <div class="analogy-box">
      <div class="analogy-title">
        <span>&#128161;</span> Everyday Analogy: Building a Highway Between Two Towns
      </div>
      <p>
        Imagine two neighboring rival towns, Blueville and Redford. The regional government needs to build a paved divided highway between them. 
        Engineers do not build the road directly touching the fence of either town! If they did, a minor expansion or stray bicycle would cause an accident. 
        Instead, urban planners find the widest possible unoccupied corridor of land between the outermost houses of each town and pave the centerline directly in the middle. 
        In this scenario:
      </p>
      <ul style="margin-left: 1.5rem; margin-top: 0.5rem; color: var(--text-secondary);">
        <li><strong>The Outer Houses:</strong> The critical border homes that limit the highway width are the <strong>Support Vectors</strong>.</li>
        <li><strong>The Highway Width:</strong> The cleared buffer zone between the towns is the <strong>Margin</strong>.</li>
        <li><strong>The Painted Centerline:</strong> The separating boundary deciding which town you are in is the <strong>Hyperplane (Decision Boundary)</strong>.</li>
      </ul>
    </div>

    <h3 class="sub-title">1. What Is a Support Vector Machine?</h3>
    <p>
      A <strong>Support Vector Machine (SVM)</strong> is a powerful supervised learning algorithm primarily used for classification (and regression) that seeks to find the optimal decision boundary that separates data classes with the <strong>maximum possible margin</strong>. 
      While basic classifiers (such as Perceptrons) simply stop searching the moment they find <em>any</em> line that separates the training points, SVM mathematically maximizes the distance between the boundary and the nearest data points of each class.
    </p>

    <div class="figure-container">
      __SVG_TWO_CLASS_HYPERPLANE__
      <div class="figure-caption">
        <strong>Figure 13.1: Two-Class Classification with a Separating Hyperplane.</strong> In 2D space, the separating hyperplane is a straight line: <code>w₁x₁ + w₂x₂ + b = 0</code>. Points on opposite sides receive different predicted class labels.
      </div>
    </div>

    <h3 class="sub-title">2. Fundamental Vocabulary Every Beginner Must Know</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Technical Term</th>
            <th>Mathematical Role</th>
            <th>Everyday Analogy</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Class (Label, y)</strong></td>
            <td>The discrete target category being predicted (e.g. y = +1 for Admitted, y = -1 for Rejected).</td>
            <td>Belonging to Blueville vs. belonging to Redford.</td>
          </tr>
          <tr>
            <td><strong>Feature (Input, x)</strong></td>
            <td>A measurable dimension or variable (e.g. Exam Score x₁, Project Score x₂).</td>
            <td>The GPS coordinates (Latitude, Longitude) of each student's home.</td>
          </tr>
          <tr>
            <td><strong>Hyperplane</strong></td>
            <td>A flat geometric subspace of dimension (D - 1) that divides a D-dimensional feature space into two halves.</td>
            <td>The painted centerline dividing the two sides of the highway.</td>
          </tr>
          <tr>
            <td><strong>Margin</strong></td>
            <td>The perpendicular distance (cushion) between the decision hyperplane and the closest training points.</td>
            <td>The total cleared buffer zone between the two towns.</td>
          </tr>
          <tr>
            <td><strong>Support Vector</strong></td>
            <td>The specific subset of critical training observations that lie on or violate the margin boundaries.</td>
            <td>The outermost houses in each town that dictate how wide the highway can be built.</td>
          </tr>
          <tr>
            <td><strong>Hard Margin</strong></td>
            <td>A strict formulation requiring 100% perfect separation with zero margin violations.</td>
            <td>Demanding that not a single brick or mailbox encroaches on the road corridor.</td>
          </tr>
          <tr>
            <td><strong>Soft Margin</strong></td>
            <td>A robust formulation allowing minor margin violations via slack variables to handle noise and overlap.</td>
            <td>Allowing a small driveway or tree to sit inside the buffer zone with a zoning penalty.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 2 -->
  <section id="sec-02" class="section-card">
    <div class="section-badge">Section 02</div>
    <h2 class="section-title">What Is a Hyperplane?</h2>
    <p class="section-lead">
      The word "hyperplane" sounds intimidating, but in everyday geometry it simply means a flat, unbending decision wall that splits space in two. 
      The mathematical dimension of the hyperplane is always exactly one less than the dimension of the space it lives in.
    </p>

    <h3 class="sub-title">1. Mathematical Definition of a 2D Hyperplane</h3>
    <p>
      In a two-dimensional space with two features (x₁ and x₂), a hyperplane is simply a <strong>straight line</strong>. 
      You are already familiar with the elementary line equation <code>y = mx + c</code>. In machine learning, we express this same linear relationship using weights (coefficients) and a bias term:
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; Two-Feature Linear Hyperplane Equation</div>
      <div class="math-display">w₁x₁ + w₂x₂ + b = 0</div>
      <div class="formula-legend">
        <div class="legend-item"><span class="legend-symbol">x₁, x₂</span><span>Input features (e.g., Exam Score and Project Score)</span></div>
        <div class="legend-item"><span class="legend-symbol">w₁, w₂</span><span>Learned feature weights determining boundary orientation</span></div>
        <div class="legend-item"><span class="legend-symbol">b</span><span>Bias (intercept) shifting the boundary away from the origin</span></div>
      </div>
    </div>

    <h3 class="sub-title">2. General Vector Form Across Any Dimension</h3>
    <p>
      When we have 3, 10, or 10,000 features, writing out individual terms becomes impractical. 
      We package all feature values into a vector <code>x = [x₁, x₂, ..., x_D]ᵀ</code> and all weights into a weight vector <code>w = [w₁, w₂, ..., w_D]ᵀ</code>. 
      Their dot product produces the compact general hyperplane formula:
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; General Hyperplane Vector Equation</div>
      <div class="math-display">wᵀx + b = 0</div>
      <div class="formula-legend">
        <div class="legend-item"><span class="legend-symbol">wᵀx</span><span>Vector dot product: w₁x₁ + w₂x₂ + ... + w_Dx_D</span></div>
        <div class="legend-item"><span class="legend-symbol">b</span><span>Scalar bias determining offset from coordinate origin</span></div>
      </div>
    </div>

    <h3 class="sub-title">3. Hyperplane Dimensionality Across Spaces</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Feature Space Dimension</th>
            <th>Hyperplane Geometry</th>
            <th>Mathematical Representation</th>
            <th>Visual Form</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1D Space (1 Feature)</strong></td>
            <td>0-Dimensional</td>
            <td><code>w₁x₁ + b = 0 &rarr; x₁ = -b/w₁</code></td>
            <td>A single cut-off point on a number line</td>
          </tr>
          <tr>
            <td><strong>2D Space (2 Features)</strong></td>
            <td>1-Dimensional</td>
            <td><code>w₁x₁ + w₂x₂ + b = 0</code></td>
            <td>A straight line separating a 2D plane</td>
          </tr>
          <tr>
            <td><strong>3D Space (3 Features)</strong></td>
            <td>2-Dimensional</td>
            <td><code>w₁x₁ + w₂x₂ + w₃x₃ + b = 0</code></td>
            <td>A flat sheet of paper (plane) slicing through 3D space</td>
          </tr>
          <tr>
            <td><strong>D-Dimensional Space</strong></td>
            <td>(D - 1)-Dimensional</td>
            <td><code>wᵀx + b = 0</code></td>
            <td>A flat mathematical manifold slicing through hyperspace</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="def-box">
      <div class="def-title"><span>&#128214;</span> How the Hyperplane Makes Predictions</div>
      <p>
        For any incoming test observation <code>x_new</code>, the SVM computes the decision value <code>f(x_new) = wᵀx_new + b</code>:
      </p>
      <ul style="margin-left: 1.5rem; margin-top: 0.5rem; color: var(--def-card-text);">
        <li>If <code>wᵀx_new + b &gt; 0</code>: The observation lies on the positive side &rarr; Predict <strong>Class +1</strong> (e.g. Admitted).</li>
        <li>If <code>wᵀx_new + b &lt; 0</code>: The observation lies on the negative side &rarr; Predict <strong>Class -1</strong> (e.g. Rejected).</li>
        <li>If <code>wᵀx_new + b = 0</code>: The point lies directly on the decision boundary (maximum ambiguity).</li>
      </ul>
    </div>
  </section>

  <!-- SECTION 3 -->
  <section id="sec-03" class="section-card">
    <div class="section-badge">Section 03</div>
    <h2 class="section-title">Understanding the Margin</h2>
    <p class="section-lead">
      Any number of straight lines can successfully separate two linearly separable clusters of points. 
      What makes SVM unique is that it does not settle for an arbitrary dividing line—it specifically searches for the boundary that maximizes the <strong>margin</strong>.
    </p>

    <div class="figure-container">
      __SVG_MAXIMUM_MARGIN__
      <div class="figure-caption">
        <strong>Figure 13.2: The Canonical SVM Margin Geometry.</strong> The decision hyperplane sits at <code>wᵀx + b = 0</code>. The two parallel margin planes sit at <code>wᵀx + b = +1</code> and <code>wᵀx + b = -1</code>. The total margin width is exactly <code>M = 2 / ∥w∥</code>.
      </div>
    </div>

    <h3 class="sub-title">1. Canonical Margin Boundaries</h3>
    <p>
      In canonical SVM notation, we scale the weight vector <code>w</code> and bias <code>b</code> such that the closest data points of each class satisfy:
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; Canonical Margin Planes</div>
      <div class="math-display">wᵀx + b = +1 &nbsp;&nbsp;&nbsp;&nbsp; (Positive Margin Plane)</div>
      <div class="math-display">wᵀx + b = -1 &nbsp;&nbsp;&nbsp;&nbsp; (Negative Margin Plane)</div>
      <div class="formula-legend">
        <div class="legend-item"><span class="legend-symbol">+1 Plane</span><span>Passes through closest positive training samples (Class +1)</span></div>
        <div class="legend-item"><span class="legend-symbol">-1 Plane</span><span>Passes through closest negative training samples (Class -1)</span></div>
      </div>
    </div>

    <h3 class="sub-title">2. Derivation of the Margin Width Formula</h3>
    <p>
      From elementary linear algebra, the perpendicular Euclidean distance from any point <code>x₀</code> to a hyperplane <code>wᵀx + b = 0</code> is given by:
    </p>
    <div class="math-display" style="font-size: 1.1rem;">
      Distance = |wᵀx₀ + b| / ∥w∥
    </div>
    <p>
      Since points on the positive margin boundary satisfy <code>wᵀx + b = +1</code>, their perpendicular distance to the decision hyperplane is:
    </p>
    <div class="math-display" style="font-size: 1.1rem;">
      d₊ = |+1| / ∥w∥ = 1 / ∥w∥
    </div>
    <p>
      Similarly, points on the negative margin boundary satisfy <code>wᵀx + b = -1</code>, and their distance to the decision line is:
    </p>
    <div class="math-display" style="font-size: 1.1rem;">
      d₋ = |-1| / ∥w∥ = 1 / ∥w∥
    </div>
    <p>
      Adding these two symmetrical distances together yields the total margin width <code>M</code>:
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; Total Margin Width Formula</div>
      <div class="math-display">Total Margin Width (M) = d₊ + d₋ = (1 / ∥w∥) + (1 / ∥w∥) = 2 / ∥w∥</div>
      <div class="formula-legend">
        <div class="legend-item"><span class="legend-symbol">∥w∥</span><span>Euclidean L2 norm of weight vector: √(w₁² + w₂² + ... + w_D²)</span></div>
        <div class="legend-item"><span class="legend-symbol">Inverse</span><span>Maximizing margin (2/∥w∥) is mathematically equivalent to minimizing ∥w∥</span></div>
      </div>
    </div>

    <h3 class="sub-title">3. Concrete Worked Numerical Calculation</h3>
    <div class="calc-box">
      <div class="calc-step">
        <div class="step-title">Given Parameters:</div>
        <p>Suppose our fitted 2D linear SVM yields weight vector <code>w = [1.2, 1.6]ᵀ</code> and bias <code>b = -3.0</code>.</p>
      </div>
      <div class="calc-step">
        <div class="step-title">Step 1: Compute Euclidean Norm ∥w∥</div>
        <p><code>∥w∥ = √(1.2² + 1.6²) = √(1.44 + 2.56) = √(4.0) = 2.0000</code></p>
      </div>
      <div class="calc-step">
        <div class="step-title">Step 2: Compute Total Margin Width</div>
        <p><code>Margin Width = 2 / ∥w∥ = 2 / 2.0000 = 1.0000 unit</code></p>
      </div>
      <div class="calc-step">
        <div class="step-title">Step 3: Distance of Test Point x_A = [2.5, 2.0]ᵀ</div>
        <p><code>wᵀx_A + b = (1.2 &times; 2.5) + (1.6 &times; 2.0) - 3.0 = 3.0 + 3.2 - 3.0 = +3.2000</code></p>
        <p>Perpendicular distance to decision boundary: <code>d = |3.2000| / 2.0000 = 1.6000 units</code>.</p>
        <p><em>Interpretation:</em> Because <code>wᵀx_A + b = +3.2 &gt; +1.0</code>, student x_A lies safely beyond the positive margin boundary and is confidently classified as <strong>Admitted (Class +1)</strong>.</p>
      </div>
    </div>
  </section>

  <!-- SECTION 4 -->
  <section id="sec-04" class="section-card">
    <div class="section-badge">Section 04</div>
    <h2 class="section-title">What Are Support Vectors?</h2>
    <p class="section-lead">
      In most machine learning algorithms, every single data point in the training set influences the final model parameters. 
      In SVM, something extraordinary happens: <strong>only a small fraction of the training data determines the decision boundary</strong>. 
      These critical points are called <strong>Support Vectors</strong>.
    </p>

    <div class="figure-container">
      __SVG_ACTUAL_SUPPORT_VECTORS__
      <div class="figure-caption">
        <strong>Figure 13.3: Actual Support Vectors Identified on a Fitted Scikit-Learn Model.</strong> Support vectors (highlighted with bold gold rings) lie directly on or inside the margin boundaries. The non-support vector samples (faint dots) exert zero mathematical pull on the boundary.
      </div>
    </div>

    <h3 class="sub-title">1. Why Are They Called "Support" Vectors?</h3>
    <p>
      In civil engineering, a bridge is held up by a few structural support pillars. The rest of the bridge deck rests upon these pillars. 
      In SVM, the support vectors are the geometric pillars that physically "prop up" and stabilize the hyperplane. 
      If you were to delete 95% of your training points that lie far away from the margin, <strong>the fitted hyperplane would not budge by even a millimeter!</strong>
    </p>

    <div class="success-box">
      <div class="success-title"><span>&#10003;</span> The Sparsity Superpower of SVM</div>
      <p>
        Because only support vectors dictate the decision boundary, SVM produces a <strong>sparse solution</strong>. 
        Once training is complete, an SVM does not need to store the entire original dataset in RAM to make future predictions—it only needs to store the support vectors and their dual lagrange multipliers (<code>alpha</code> coefficients).
      </p>
    </div>

    <h3 class="sub-title">2. Inspecting Support Vectors in Scikit-Learn</h3>
    <p>
      When you train an <code>SVC</code> model in scikit-learn, the fitted model exposes three built-in inspection attributes:
    </p>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Scikit-Learn Attribute</th>
            <th>Data Type &amp; Shape</th>
            <th>Concrete Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>clf.support_vectors_</code></td>
            <td>NumPy 2D Array <code>(n_SV, n_features)</code></td>
            <td>The exact feature coordinates of all training samples selected as support vectors.</td>
          </tr>
          <tr>
            <td><code>clf.support_</code></td>
            <td>NumPy 1D Array <code>(n_SV,)</code></td>
            <td>The row indices in <code>X_train</code> corresponding to the support vectors.</td>
          </tr>
          <tr>
            <td><code>clf.n_support_</code></td>
            <td>NumPy 1D Array <code>(n_classes,)</code></td>
            <td>The number of support vectors selected from each target class (e.g. <code>[16, 16]</code>).</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="code-container">
      <div class="code-header">
        <span>PYTHON 3: SUPPORT VECTOR INSPECTION</span>
        <span>scikit-learn runtime</span>
      </div>
      <pre><code>from sklearn.svm import SVC
import numpy as np

# Train a linear SVC on student dataset
model = SVC(kernel='linear', C=1.0)
model.fit(X_train, y_train)

# Inspect support vectors
print(f"Total Support Vectors: {len(model.support_)} out of {len(X_train)} training points")
print(f"Support Vectors per Class: {model.n_support_}")
print(f"Coordinates of first support vector: {model.support_vectors_[0]}")</code></pre>
    </div>
  </section>

  <!-- SECTION 5 -->
  <section id="sec-05" class="section-card">
    <div class="section-badge">Section 05</div>
    <h2 class="section-title">Maximum Margin Intuition</h2>
    <p class="section-lead">
      Why is a wide margin so crucial for real-world machine learning? 
      Why not just accept the first line that achieves 100% training accuracy? 
      The answer lies in the fundamental battle between <strong>empirical memorization</strong> and <strong>generalization to unseen noise</strong>.
    </p>

    <div class="figure-container">
      __SVG_NARROW_VS_WIDE_MARGIN__
      <div class="figure-caption">
        <strong>Figure 13.4: Narrow Margin vs. Wide Margin Generalization.</strong> A narrow margin classifies the training points but leaves zero safety tolerance for real-world test noise, causing misclassifications. A wide margin provides robust clearance.
      </div>
    </div>

    <h3 class="sub-title">1. The Danger of a Narrow Margin</h3>
    <p>
      Consider a boundary that slices right along the edge of your training points with only 0.05 units of clearance. 
      While this boundary achieves 100% training accuracy, it suffers from severe <strong>high variance (overfitting risk)</strong>:
    </p>
    <ul style="margin-left: 1.5rem; margin-top: 0.5rem; color: var(--text-secondary);">
      <li><strong>Measurement Noise:</strong> In real life, sensor readings, survey inputs, and test scores fluctuate by a few percent due to random noise.</li>
      <li><strong>Boundary Vulnerability:</strong> A noisy test point that belongs to Class 1 will easily wander across a narrow boundary into Class 0 territory.</li>
    </ul>

    <h3 class="sub-title">2. Why Maximum Margin Promotes Generalization</h3>
    <p>
      By selecting the hyperplane that sits exactly halfway between the two classes with the <strong>maximum possible clearance on both sides</strong>, SVM minimizes the risk that random perturbations will cause misclassifications. 
      Statistical learning theory (Vapnik-Chervonenkis / VC Dimension Theory) proves that maximizing the margin minimizes the theoretical upper bound on test generalization error!
    </p>
  </section>
"""
