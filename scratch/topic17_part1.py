"""Topic 17 Part 1: Hero Header, TOC, Sections 1 to 5.
Strict Light Mode, semantic HTML, math typography, verified numbers.
"""

TOPIC17_PART1 = """
<div class="container">

  <!-- Hero Header -->
  <header class="hero-header">
    <div class="hero-badge">
      <span>&#9670;</span> CodeVerse Machine Learning Track &bull; Topic 17
    </div>
    <h1 class="hero-title">Dimensionality Reduction &amp; Feature Extraction</h1>
    <p class="hero-subtitle">
      A comprehensive, visual, and mathematical guide to taming the Curse of Dimensionality. Master Principal Component Analysis (PCA), Covariance Eigendecomposition, Explained Variance, 2D/3D Visualizations, t-SNE, UMAP, and LDA from geometric intuition to production scikit-learn pipelines.
    </p>

    <div class="hero-meta-grid">
      <div class="meta-item">
        <span class="meta-label">Curriculum Depth</span>
        <span class="meta-value">20 Complete Sections</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Visual Systems</span>
        <span class="meta-value">16 Verified Vector Diagrams</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Executable Labs</span>
        <span class="meta-value">3 Complete Python Labs</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Verified Tech Stack</span>
        <span class="meta-value">scikit-learn 1.9 &bull; SciPy 1.17</span>
      </div>
    </div>
  </header>

  <!-- Table of Contents -->
  <nav class="toc-card" aria-label="Table of Contents">
    <div class="toc-header">
      <span style="font-size: 1.3rem; color: var(--primary-accent);">&#9776;</span>
      <h2 class="toc-title">Curriculum Table of Contents</h2>
    </div>
    <div class="toc-grid">
      <a href="#sec-01" class="toc-link"><span class="toc-num">01</span> Introduction to Dimensionality Reduction</a>
      <a href="#sec-02" class="toc-link"><span class="toc-num">02</span> Why Do We Need Dimensionality Reduction?</a>
      <a href="#sec-03" class="toc-link"><span class="toc-num">03</span> Feature Selection vs Feature Extraction</a>
      <a href="#sec-04" class="toc-link"><span class="toc-num">04</span> Main Dimensionality Reduction Methods</a>
      <a href="#sec-05" class="toc-link"><span class="toc-num">05</span> PCA Geometric Intuition</a>
      <a href="#sec-06" class="toc-link"><span class="toc-num">06</span> PCA Mathematical Foundations</a>
      <a href="#sec-07" class="toc-link"><span class="toc-num">07</span> Step-by-Step Numerical PCA Example</a>
      <a href="#sec-08" class="toc-link"><span class="toc-num">08</span> Explained Variance &amp; Choosing Components</a>
      <a href="#sec-09" class="toc-link"><span class="toc-num">09</span> Visualizing PCA in 2D and 3D</a>
      <a href="#sec-10" class="toc-link"><span class="toc-num">10</span> PCA with scikit-learn Pipelines</a>
      <a href="#sec-11" class="toc-link"><span class="toc-num">11</span> Does PCA Improve Model Performance?</a>
      <a href="#sec-12" class="toc-link"><span class="toc-num">12</span> t-SNE Non-Linear Manifold Learning</a>
      <a href="#sec-13" class="toc-link"><span class="toc-num">13</span> UMAP Manifold Approximation</a>
      <a href="#sec-14" class="toc-link"><span class="toc-num">14</span> Linear Discriminant Analysis (LDA)</a>
      <a href="#sec-15" class="toc-link"><span class="toc-num">15</span> Real-World Industry Applications</a>
      <a href="#sec-16" class="toc-link"><span class="toc-num">16</span> Common Beginner Mistakes &amp; Fixes</a>
      <a href="#sec-17" class="toc-link"><span class="toc-num">17</span> Visual Gallery &amp; Diagram Guide</a>
      <a href="#sec-18" class="toc-link"><span class="toc-num">18</span> Quick Revision &amp; Decision Guide</a>
      <a href="#sec-19" class="toc-link"><span class="toc-num">19</span> Complete Python Lab: End-to-End PCA</a>
      <a href="#sec-20" class="toc-link"><span class="toc-num">20</span> Interactive Knowledge Checks &amp; FAQs</a>
    </div>
  </nav>

  <!-- SECTION 01 -->
  <section id="sec-01" class="content-section">
    <span class="section-badge">Section 01 &bull; Core Foundations</span>
    <h2 class="section-title">Introduction to Dimensionality Reduction</h2>

    <p>
      In machine learning, every measurable attribute recorded about an observation is known as a <strong>feature</strong>. In tabular data, each feature corresponds to a column, and each observation corresponds to a row. In geometric terms, each feature defines an independent axis in a mathematical coordinate system called the <strong>feature space</strong>.
    </p>

    <div class="callout-card callout-def">
      <div class="callout-title">Understanding Dimensions in Data</div>
      <ul>
        <li><strong>1 Feature (1D):</strong> A single numerical scale, such as student test scores, plotted along a simple 1D number line.</li>
        <li><strong>2 Features (2D):</strong> Two measurements, such as <em>Study Hours</em> and <em>Exam Score</em>, plotted on a familiar 2D Cartesian plane (x, y).</li>
        <li><strong>3 Features (3D):</strong> Three attributes, such as <em>Study Hours</em>, <em>Attendance Rate</em>, and <em>Exam Score</em>, plotted in a 3D volume (x, y, z).</li>
        <li><strong>D Features (D-Dimensional Hyper-Space):</strong> When a tabular dataset contains 10, 50, 100, or 1,000 features, each data point becomes a coordinate vector residing in a <em>D-dimensional mathematical space</em>.</li>
      </ul>
    </div>

    <div class="callout-card callout-analogy">
      <div class="callout-title">Everyday Analogy: The University Student Dataset</div>
      <p>
        Imagine a university registrar recording 50 distinct metrics for every student: weekly study hours, lecture attendance percentage, quiz scores, assignment completion, library checkouts, sleep duration, commute time, extracurricular hours, prerequisite grades, and dozens of survey responses.
        <br><br>
        While each metric sounds helpful, many of them are tightly interrelated: students with high study hours usually have high assignment completion, high quiz scores, and high library checkouts. Storing and analyzing all 50 columns separately introduces immense redundancy and computational drag without adding proportional new information!
      </p>
    </div>

    <p>
      <strong>Dimensionality Reduction (DR)</strong> is the process of transforming data from a high-dimensional feature space into a meaningful lower-dimensional representation, while retaining as much of the original variance, geometric structure, and predictive signal as possible.
    </p>

    <!-- Visual 01 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.1: The Dimensionality Reduction Transformation</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_DIMENSIONALITY_OVERVIEW__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.1:</strong> Left: A sprawling, high-dimensional table with dozens of correlated, noisy columns is difficult to visualize and computationally heavy. Right: Dimensionality reduction condenses these redundant measurements into a small set of orthogonal, highly informative components (z₁, z₂) that preserve the underlying patterns.
      </p>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; Critical Mindset: Dimensionality Reduction Is Not a Free Lunch</div>
      <p>
        Reducing the number of features does not automatically make every machine learning model perform better. Dimensionality reduction always involves an information trade-off: you discard some variance to achieve compactness, speed, and visual interpretability. If you reduce dimensions too aggressively, you risk throwing away subtle predictive signals that your model needs!
      </p>
    </div>
  </section>

  <!-- SECTION 02 -->
  <section id="sec-02" class="content-section">
    <span class="section-badge">Section 02 &bull; The Curse of Dimensionality</span>
    <h2 class="section-title">Why Do We Need Dimensionality Reduction?</h2>

    <p>
      Why can't we simply collect hundreds or thousands of features and feed them all directly into our machine learning algorithms? While modern computers have abundant RAM, high-dimensional spaces introduce severe geometric, statistical, and computational pathologies.
    </p>

    <div class="step-flow">
      <div class="step-item">
        <div class="step-number">1</div>
        <div class="step-content">
          <div class="step-title">High Computational &amp; Storage Cost</div>
          <p class="step-desc">The computational time of many machine learning algorithms scales super-linearly with the number of features. Training on 1,000 features requires vastly more memory, matrix operations, and floating-point calculations than training on 20 features.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">2</div>
        <div class="step-content">
          <div class="step-title">Multicollinearity &amp; Feature Redundancy</div>
          <p class="step-desc">Features often duplicate information. For example, in an e-commerce database, <em>"Total Dollars Spent"</em> and <em>"Total Items Purchased"</em> are strongly correlated. Feeding both into linear models inflates coefficient variance and causes numerical instability.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">3</div>
        <div class="step-content">
          <div class="step-title">Noise Accumulation &amp; Overfitting</div>
          <p class="step-desc">As the number of features grows relative to the number of training samples (<em>D &gt;&gt; N</em>), complex models can latch onto random noise patterns, achieving 100% training accuracy while failing catastrophically on unseen test data.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">4</div>
        <div class="step-content">
          <div class="step-title">The Human Visualization Barrier</div>
          <p class="step-desc">Human sensory perception is strictly limited to 2D screens and 3D physical spaces. We cannot visualize 13-dimensional wine characteristics or 768-dimensional text embeddings without projecting them down to 2D or 3D.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">5</div>
        <div class="step-content">
          <div class="step-title">The Curse of Dimensionality (Geometric Sparsity)</div>
          <p class="step-desc">As dimensions increase, the volume of the feature space grows exponentially. Data points become isolated in vast empty space, causing distance metrics to degenerate.</p>
        </div>
      </div>
    </div>

    <!-- Visual 02 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.2: Exponential Volume Explosion and Data Sparsity</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_CURSE_OF_DIMENSIONALITY__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.2:</strong> If we divide each feature into 10 intervals, a 1D line requires 10 bins to cover. A 2D square requires 100 bins (10²). A 3D cube requires 1,000 bins (10³). In 100 dimensions, space explodes to 10¹⁰⁰ bins! A finite sample of observations becomes intensely sparse, rendering distance-based algorithms blind.
      </p>
    </div>

    <div class="callout-card callout-def">
      <div class="callout-title">The Distance Concentration Phenomenon</div>
      <p>
        In high-dimensional spaces, a bizarre mathematical phenomenon occurs: the ratio between the distance to the nearest neighbor and the distance to the farthest neighbor approaches 1!
      </p>
      <div style="background: #FFFFFF; padding: 10px 14px; border-radius: 6px; font-family: monospace; margin: 8px 0; border: 1px solid #E2E8F0;">
        lim<sub>D &rarr; &infin;</sub> [ (dist<sub>max</sub> &minus; dist<sub>min</sub>) / dist<sub>min</sub> ] = 0
      </div>
      <p>
        Every single point becomes roughly equidistant from every other point. Algorithms that rely on spatial proximity—such as K-Nearest Neighbors (KNN), K-Means clustering, and Radial Basis Function (RBF) Support Vector Machines—struggle to distinguish true neighbors from distant noise.
      </p>
    </div>
  </section>

  <!-- SECTION 03 -->
  <section id="sec-03" class="content-section">
    <span class="section-badge">Section 03 &bull; Methodological Taxonomy</span>
    <h2 class="section-title">Feature Selection vs Feature Extraction</h2>

    <p>
      When faced with too many features, practitioners have two distinct strategic choices: <strong>Feature Selection</strong> or <strong>Feature Extraction</strong>. Beginners often confuse them, but their mathematical operations and practical consequences are fundamentally different.
    </p>

    <!-- Visual 03 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.3: Feature Selection vs Feature Extraction Workflow</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_SELECTION_VS_EXTRACTION__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.3:</strong> Feature Selection (left) picks a subset of the original columns (x₁, x₃, x₄) and drops the rest. Feature Extraction (right) transforms all original columns through a mathematical mapping f(X) into new composite components (z₁, z₂) that pool information across the entire dataset.
      </p>
    </div>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Dimension</th>
            <th>Feature Selection (Subset)</th>
            <th>Feature Extraction (Transformation)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Core Operation</strong></td>
            <td>Selects a subset of original features without modification</td>
            <td>Combines and transforms original features into new composite features</td>
          </tr>
          <tr>
            <td><strong>Physical Interpretability</strong></td>
            <td><strong>High</strong> (Original column names and physical units are preserved)</td>
            <td><strong>Low to Moderate</strong> (New components are mathematical mixtures of multiple features)</td>
          </tr>
          <tr>
            <td><strong>Information Utilization</strong></td>
            <td>Information in unselected columns is completely discarded</td>
            <td>Retains variance and joint information from all original columns</td>
          </tr>
          <tr>
            <td><strong>Collinearity Handling</strong></td>
            <td>Drops one of two collinear features manually or via score</td>
            <td>Naturally transforms correlated features into strictly orthogonal components</td>
          </tr>
          <tr>
            <td><strong>Common Algorithms</strong></td>
            <td>VarianceThreshold, SelectKBest, RFE, LASSO L1 penalty</td>
            <td><strong>PCA</strong>, t-SNE, UMAP, Factor Analysis, Autoencoders</td>
          </tr>
          <tr>
            <td><strong>Best Suited For</strong></td>
            <td>Domain-critical applications requiring strict regulatory explainability (e.g., credit scoring, clinical diagnostics)</td>
            <td>Exploratory 2D/3D visualization, image feature compression, overcoming severe multicollinearity</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout-card callout-success">
      <div class="callout-title">&#10004; Crucial Categorization Rule</div>
      <p>
        <strong>Principal Component Analysis (PCA) is strictly a feature extraction technique.</strong> It never selects or highlights individual original columns. Instead, it constructs brand new mathematical directions that are weighted linear combinations of every single original feature!
      </p>
    </div>
  </section>

  <!-- SECTION 04 -->
  <section id="sec-04" class="content-section">
    <span class="section-badge">Section 04 &bull; Algorithmic Landscape</span>
    <h2 class="section-title">Main Dimensionality Reduction Methods</h2>

    <p>
      Dimensionality reduction is a diverse family of algorithms. Different methods optimize completely different mathematical objectives: some preserve global variance, others preserve local neighborhoods, and some maximize class separability.
    </p>

    <!-- Visual 04 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.4: Comparative Landscape of Dimensionality Reduction Techniques</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_METHODS_COMPARISON_GRID__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.4:</strong> Overview of the 4 primary dimensionality reduction paradigms: PCA (linear unsupervised, max variance), t-SNE (non-linear unsupervised, local clusters), UMAP (manifold learning, balance of local and global topology), and LDA (linear supervised, max class margin).
      </p>
    </div>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Method</th>
            <th>Type</th>
            <th>Linearity</th>
            <th>Primary Objective</th>
            <th>Downstream Modeling?</th>
            <th>Exploratory Viz?</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>PCA</strong></td>
            <td>Unsupervised</td>
            <td>Linear</td>
            <td>Maximizes global variance; minimizes reconstruction error</td>
            <td><strong>Excellent</strong> (Fast, deterministic, invertible)</td>
            <td>Good for linear trends</td>
          </tr>
          <tr>
            <td><strong>t-SNE</strong></td>
            <td>Unsupervised</td>
            <td>Non-Linear</td>
            <td>Preserves local neighborhood probabilities (Kullback-Leibler divergence)</td>
            <td><strong>Poor</strong> (No out-of-sample transform; stochastic)</td>
            <td><strong>Exceptional</strong> for 2D/3D cluster maps</td>
          </tr>
          <tr>
            <td><strong>UMAP</strong></td>
            <td>Unsupervised</td>
            <td>Non-Linear</td>
            <td>Preserves fuzzy simplicial topological manifold structure</td>
            <td>Moderate (supports <code>transform()</code>, but evaluates locally)</td>
            <td><strong>Exceptional</strong> (Faster than t-SNE, preserves global layout)</td>
          </tr>
          <tr>
            <td><strong>LDA</strong></td>
            <td><strong>Supervised</strong></td>
            <td>Linear</td>
            <td>Maximizes between-class variance over within-class variance</td>
            <td><strong>Excellent</strong> for classification preprocessing</td>
            <td>Good (up to C &minus; 1 dimensions)</td>
          </tr>
          <tr>
            <td><strong>Feature Selection</strong></td>
            <td>Supervised or Unsupervised</td>
            <td>N/A (Subset)</td>
            <td>Selects best original columns using statistical tests or model weights</td>
            <td><strong>Excellent</strong> (Keeps original physical units)</td>
            <td>N/A (Limited to original columns)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; These Methods Are Not Interchangeable!</div>
      <p>
        Beginners often try to use t-SNE as a preprocessing step inside a machine learning production pipeline. This is a severe mistake! t-SNE is a non-parametric visualization technique; standard scikit-learn t-SNE cannot transform new incoming test samples (it lacks a <code>transform()</code> method). For downstream predictive modeling, PCA or Feature Selection is the proper industry standard.
      </p>
    </div>
  </section>

  <!-- SECTION 05 -->
  <section id="sec-05" class="content-section">
    <span class="section-badge">Section 05 &bull; Intuitive Foundations</span>
    <h2 class="section-title">PCA Geometric Intuition</h2>

    <p>
      <strong>Principal Component Analysis (PCA)</strong> is the foundational technique of dimensionality reduction. Invented by Karl Pearson in 1901 and independently expanded by Harold Hotelling in 1933, PCA discovers new coordinate axes that capture the maximum possible spread (variance) of the data.
    </p>

    <h3 class="subsection-title">The Height &amp; Weight Analogy</h3>
    <p>
      Imagine measuring the <strong>Height</strong> (in inches) and <strong>Weight</strong> (in pounds) of 200 adults:
    </p>
    <ul>
      <li>Taller people generally weigh more; shorter people generally weigh less.</li>
      <li>If you plot Height on the x-axis and Weight on the y-axis, the points do not form a circular cloud. Instead, they form an elongated, diagonal oval stretching from the bottom-left to the top-right.</li>
      <li>Notice that both features convey overlapping information about <em>overall human physical size</em>.</li>
    </ul>

    <p>
      What if, instead of describing someone using separate Height and Weight coordinates, we rotate our perspective?
    </p>

    <!-- Visual 05 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.5: Principal Component Axes vs Original Feature Axes</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_PCA_INTUITION_AXES__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.5:</strong> The original feature axes (Height x₁ and Weight x₂) run horizontally and vertically. PCA discovers <strong>PC1</strong> (solid indigo vector), which aligns directly along the longest diagonal axis of maximum data spread (97.8% of variance). <strong>PC2</strong> (green vector) is strictly perpendicular (orthogonal, 90°) to PC1, capturing the tiny remaining width (2.2% of variance).
      </p>
    </div>

    <div class="callout-card callout-def">
      <div class="callout-title">The Principal Components Defined</div>
      <ul>
        <li><strong>PC1 (First Principal Component):</strong> The straight line passing through the multidimensional center of mass along which the data points vary the most. It captures the maximum possible variance.</li>
        <li><strong>PC2 (Second Principal Component):</strong> The line strictly perpendicular (orthogonal) to PC1 that captures the highest remaining variance not already explained by PC1.</li>
        <li><strong>PCk (k-th Principal Component):</strong> The line orthogonal to all previous components (PC1 through PC<sub>k-1</sub>) that captures the highest remaining variance.</li>
        <li><strong>Orthogonality:</strong> Every principal component is at a 90° angle to every other component. This means the new features are <strong>completely uncorrelated</strong> (their pairwise covariance is exactly 0.0)!</li>
      </ul>
    </div>

    <h3 class="subsection-title">Projecting from 2D onto 1D</h3>
    <p>
      Once PCA identifies the direction of maximum spread (PC1), how do we reduce dimensions? We <strong>project</strong> every point orthogonally onto that single line!
    </p>

    <!-- Visual 06 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.6: Orthogonal Projection Compressing 2D Space to 1D</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_PROJECTION_2D_TO_1D__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.6:</strong> Each red 2D point is dropped perpendicularly onto the indigo PC1 axis, producing a new 1D coordinate (green marker). The spread along the line preserves 97.8% of the original information. The tiny dashed red distances represent the discarded orthogonal variance (reconstruction error).
      </p>
    </div>

    <p>
      By keeping only the 1D coordinate along PC1, we have successfully reduced our dataset from 2 dimensions to 1 dimension while retaining almost the entire variation of the original data!
    </p>
  </section>

"""
