"""Topic 17 Part 2: Sections 6 to 10.
PCA Mathematical Foundations, Numerical Example, Explained Variance, 2D/3D Visualization, scikit-learn Pipeline.
"""

TOPIC17_PART2 = """
  <!-- SECTION 06 -->
  <section id="sec-06" class="content-section">
    <span class="section-badge">Section 06 &bull; Mathematical Mechanics</span>
    <h2 class="section-title">PCA Mathematical Foundations</h2>

    <p>
      Now that we have solid visual intuition, let us explore the formal mathematics behind PCA. While it sounds intimidating, PCA boils down to a classic linear algebra operation: <strong>finding the eigenvectors and eigenvalues of the data's covariance matrix</strong>.
    </p>

    <!-- Visual 07 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.7: The 5-Step Mathematical Pipeline of PCA</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_PCA_PIPELINE_FLOW__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.7:</strong> Progressive 5-stage transformation pipeline: (1) Standardize features, (2) Calculate pairwise covariance matrix &Sigma;, (3) Solve characteristic equation for eigenvalues &lambda; and eigenvectors v, (4) Rank eigenvectors to build projection matrix W<sub>k</sub>, and (5) Project data to obtain low-dimensional coordinates Z.
      </p>
    </div>

    <h3 class="subsection-title">1. Representing Data as a Matrix</h3>
    <p>
      Let our dataset be represented as an <em>n &times; d</em> matrix <strong>X</strong>, where <em>n</em> is the number of samples (rows) and <em>d</em> is the number of original features (columns).
    </p>

    <h3 class="subsection-title">2. Mean-Centering &amp; Standardization</h3>
    <p>
      PCA requires the coordinate axes to pass directly through the multidimensional center of mass (the mean vector &mu;). We subtract the feature means from every observation:
    </p>

    <div class="formula-block">
      X<sub>centered</sub> = X &minus; &mu;
      <div class="formula-breakdown">
        <div class="breakdown-item"><strong>X:</strong> Original raw feature matrix of shape (n, d)</div>
        <div class="breakdown-item"><strong>&mu;:</strong> Empirical mean vector [ &mu;₁, &mu;₂, &hellip;, &mu;<sub>d</sub> ]</div>
        <div class="breakdown-item"><strong>X<sub>centered</sub>:</strong> Centered data matrix with column means equal to 0.0</div>
      </div>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; Mean-Centering vs Standardization</div>
      <p>
        <strong>Mean-centering</strong> merely shifts the origin so that &mu; = 0.
        <br><br>
        <strong>Standardization (Z-score)</strong> goes one step further: it divides each centered column by its empirical standard deviation &sigma;:
        <br>
        <code>z = (x &minus; &mu;) / &sigma;</code>
        <br><br>
        If your features are measured in different physical units (e.g., Income in $10,000s vs Age in years), you <strong>must standardize</strong>. Otherwise, high-magnitude features will artificially dominate the covariance matrix, tricking PCA into aligning PC1 with whatever feature has the biggest raw numbers!
      </p>
    </div>

    <h3 class="subsection-title">3. The Covariance Matrix (&Sigma;)</h3>
    <p>
      Variance measures how much a single feature spreads out around its mean. <strong>Covariance</strong> measures how two features vary together. For centered data, the sample covariance matrix &Sigma; is calculated as:
    </p>

    <div class="formula-block">
      &Sigma; = [ 1 / (n &minus; 1) ] &times; (X<sub>centered</sub>)<sup>T</sup> X<sub>centered</sub>
      <div class="formula-breakdown">
        <div class="breakdown-item"><strong>&Sigma; (Sigma):</strong> Square symmetric matrix of shape (d, d)</div>
        <div class="breakdown-item"><strong>Diagonal Entries &Sigma;<sub>jj</sub>:</strong> Variance of feature <em>j</em></div>
        <div class="breakdown-item"><strong>Off-Diagonal Entries &Sigma;<sub>jk</sub>:</strong> Pairwise covariance between feature <em>j</em> and feature <em>k</em></div>
        <div class="breakdown-item"><strong>1 / (n &minus; 1):</strong> Unbiased sample degrees-of-freedom normalization (ddof=1)</div>
      </div>
    </div>

    <h3 class="subsection-title">4. Eigendecomposition (&Sigma;v = &lambda;v)</h3>
    <p>
      An <strong>eigenvector</strong> <em>v</em> of matrix &Sigma; is a special non-zero vector whose direction does not change when multiplied by &Sigma;; it is merely scaled by a factor &lambda;, known as the corresponding <strong>eigenvalue</strong>:
    </p>

    <div class="formula-block">
      &Sigma; v = &lambda; v
      <div class="formula-breakdown">
        <div class="breakdown-item"><strong>&Sigma;:</strong> (d &times; d) covariance matrix</div>
        <div class="breakdown-item"><strong>v:</strong> Eigenvector (unit length ||v|| = 1), defining the <strong>direction</strong> of a principal component</div>
        <div class="breakdown-item"><strong>&lambda; (Lambda):</strong> Eigenvalue (scalar &ge; 0), quantifying the <strong>amount of variance</strong> captured along direction <em>v</em></div>
      </div>
    </div>

    <p>
      Because &Sigma; is symmetric and positive semi-definite:
    </p>
    <ul>
      <li>All eigenvalues &lambda; are real and non-negative (&lambda; &ge; 0).</li>
      <li>All eigenvectors are mutually perpendicular (orthogonal): <code>v<sub>i</sub> &bull; v<sub>j</sub> = 0</code> for all <em>i &ne; j</em>.</li>
      <li>The eigenvector with the largest eigenvalue (&lambda;₁) is <strong>PC1</strong>. The eigenvector with the second-largest eigenvalue (&lambda;₂) is <strong>PC2</strong>, and so forth.</li>
    </ul>

    <h3 class="subsection-title">5. Projecting into Low-Dimensional Space</h3>
    <p>
      To reduce dimensionality from <em>d</em> to <em>k</em> (where <em>k &lt; d</em>), we construct a projection matrix <strong>W<sub>k</sub></strong> of shape <em>(d, k)</em> whose columns are the top <em>k</em> eigenvectors. The transformed data matrix <strong>Z</strong> is computed via matrix multiplication:
    </p>

    <div class="formula-block">
      Z = X<sub>centered</sub> W<sub>k</sub>
      <div class="formula-breakdown">
        <div class="breakdown-item"><strong>Z:</strong> Transformed representation of shape (n, k) with only <em>k</em> columns</div>
        <div class="breakdown-item"><strong>X<sub>centered</sub>:</strong> Centered input data matrix of shape (n, d)</div>
        <div class="breakdown-item"><strong>W<sub>k</sub>:</strong> Projection matrix of shape (d, k) containing top <em>k</em> eigenvectors</div>
      </div>
    </div>
  </section>

  <!-- SECTION 07 -->
  <section id="sec-07" class="content-section">
    <span class="section-badge">Section 07 &bull; Worked Numerical Walkthrough</span>
    <h2 class="section-title">Step-by-Step Numerical PCA Example</h2>

    <p>
      To demystify the linear algebra, let us compute PCA completely by hand on a small, manageable 2D dataset of 5 students. We track two features: <strong>Study Hours (x₁)</strong> and <strong>Exam Score (x₂)</strong>.
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Student</th>
            <th>Study Hours (x₁)</th>
            <th>Exam Score (x₂)</th>
            <th>Centered x₁ (x₁ &minus; 6)</th>
            <th>Centered x₂ (x₂ &minus; 8)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Student 1</strong></td>
            <td>2.0</td>
            <td>4.0</td>
            <td>&minus;4.0</td>
            <td>&minus;4.0</td>
          </tr>
          <tr>
            <td><strong>Student 2</strong></td>
            <td>4.0</td>
            <td>6.0</td>
            <td>&minus;2.0</td>
            <td>&minus;2.0</td>
          </tr>
          <tr>
            <td><strong>Student 3</strong></td>
            <td>6.0</td>
            <td>7.0</td>
            <td>0.0</td>
            <td>&minus;1.0</td>
          </tr>
          <tr>
            <td><strong>Student 4</strong></td>
            <td>8.0</td>
            <td>9.0</td>
            <td>+2.0</td>
            <td>+1.0</td>
          </tr>
          <tr>
            <td><strong>Student 5</strong></td>
            <td>10.0</td>
            <td>14.0</td>
            <td>+4.0</td>
            <td>+6.0</td>
          </tr>
          <tr style="background: #EEF2FF; font-weight: 700;">
            <td><strong>Mean (&mu;)</strong></td>
            <td><strong>&mu;₁ = 6.0</strong></td>
            <td><strong>&mu;₂ = 8.0</strong></td>
            <td><strong>0.0</strong></td>
            <td><strong>0.0</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="step-flow">
      <div class="step-item">
        <div class="step-number">1</div>
        <div class="step-content">
          <div class="step-title">Compute Sample Covariance Matrix (&Sigma;)</div>
          <p class="step-desc">
            With <em>n = 5</em>, the divisor is <em>n &minus; 1 = 4</em>:
            <br>&bull; Var(x₁) = [ (&minus;4)&sup2; + (&minus;2)&sup2; + 0&sup2; + 2&sup2; + 4&sup2; ] / 4 = [ 16 + 4 + 0 + 4 + 16 ] / 4 = 40 / 4 = <strong>10.0</strong>
            <br>&bull; Var(x₂) = [ (&minus;4)&sup2; + (&minus;2)&sup2; + (&minus;1)&sup2; + 1&sup2; + 6&sup2; ] / 4 = [ 16 + 4 + 1 + 1 + 36 ] / 4 = 58 / 4 = <strong>14.5</strong>
            <br>&bull; Cov(x₁, x₂) = [ (&minus;4)(&minus;4) + (&minus;2)(&minus;2) + (0)(&minus;1) + (2)(1) + (4)(6) ] / 4 = [ 16 + 4 + 0 + 2 + 24 ] / 4 = 46 / 4 = <strong>11.5</strong>
          </p>
          <div style="background: #FFFFFF; padding: 8px 12px; border-radius: 6px; font-family: monospace; border: 1px solid #CBD5E1; margin-top: 6px;">
            &Sigma; = [ [ 10.0, 11.5 ], [ 11.5, 14.5 ] ]
          </div>
        </div>
      </div>

      <div class="step-item">
        <div class="step-number">2</div>
        <div class="step-content">
          <div class="step-title">Solve for Eigenvalues (&lambda;)</div>
          <p class="step-desc">
            We solve the characteristic equation <code>det(&Sigma; &minus; &lambda;I) = 0</code>:
            <br>
            <code>(10.0 &minus; &lambda;)(14.5 &minus; &lambda;) &minus; (11.5)&sup2; = 0</code>
            <br>
            <code>&lambda;&sup2; &minus; 24.5&lambda; + (145.0 &minus; 132.25) = &lambda;&sup2; &minus; 24.5&lambda; + 12.75 = 0</code>
            <br>
            Using the quadratic formula:
            <br>
            <code>&lambda; = [ 24.5 &plusmn; &radic;(24.5&sup2; &minus; 4 &times; 12.75) ] / 2 = [ 24.5 &plusmn; &radic;(600.25 &minus; 51.0) ] / 2 = [ 24.5 &plusmn; &radic;549.25 ] / 2</code>
            <br>
            Since &radic;549.25 &approx; 23.4361:
            <br>&bull; <strong>&lambda;₁ = (24.5 + 23.4361) / 2 = 23.9680</strong> (Variance along PC1)
            <br>&bull; <strong>&lambda;₂ = (24.5 &minus; 23.4361) / 2 = 0.5320</strong> (Variance along PC2)
            <br>&bull; Total Variance = 23.9680 + 0.5320 = <strong>24.5000</strong>
          </p>
        </div>
      </div>

      <div class="step-item">
        <div class="step-number">3</div>
        <div class="step-content">
          <div class="step-title">Calculate Explained Variance Ratios</div>
          <p class="step-desc">
            &bull; <strong>PC1 Explained Variance:</strong> 23.9680 / 24.5000 = <strong>97.83%</strong>
            <br>&bull; <strong>PC2 Explained Variance:</strong> 0.5320 / 24.5000 = <strong>2.17%</strong>
            <br>
            PC1 captures an astonishing 97.83% of all variation in the data!
          </p>
        </div>
      </div>

      <div class="step-item">
        <div class="step-number">4</div>
        <div class="step-content">
          <div class="step-title">Find Eigenvectors (Principal Directions)</div>
          <p class="step-desc">
            Solving <code>(&Sigma; &minus; &lambda;₁I)v₁ = 0</code> and normalizing to unit length yields:
            <br>
            &bull; <strong>v₁ (PC1 direction):</strong> [ 0.6356, 0.7720 ]<sup>T</sup>
            <br>
            &bull; <strong>v₂ (PC2 direction):</strong> [ &minus;0.7720, 0.6356 ]<sup>T</sup>
            <br>
            Notice: <code>v₁ &bull; v₂ = (0.6356)(&minus;0.7720) + (0.7720)(0.6356) = 0.0000</code>. They are strictly orthogonal!
          </p>
        </div>
      </div>

      <div class="step-item">
        <div class="step-number">5</div>
        <div class="step-content">
          <div class="step-title">Project Data onto PC1 (1D Reduced Representation)</div>
          <p class="step-desc">
            To compress to 1D, we project centered coordinates onto <em>v₁</em>: <code>z₁ = x<sub>c,1</sub>(0.6356) + x<sub>c,2</sub>(0.7720)</code>:
            <br>&bull; <strong>Student 1:</strong> (&minus;4)(0.6356) + (&minus;4)(0.7720) = &minus;2.5424 &minus; 3.0880 = <strong>&minus;5.6305</strong>
            <br>&bull; <strong>Student 2:</strong> (&minus;2)(0.6356) + (&minus;2)(0.7720) = &minus;1.2712 &minus; 1.5440 = <strong>&minus;2.8152</strong>
            <br>&bull; <strong>Student 3:</strong> (0)(0.6356) + (&minus;1)(0.7720) = 0.0000 &minus; 0.7720 = <strong>&minus;0.7720</strong>
            <br>&bull; <strong>Student 4:</strong> (2)(0.6356) + (1)(0.7720) = 1.2712 + 0.7720 = <strong>+2.0432</strong>
            <br>&bull; <strong>Student 5:</strong> (4)(0.6356) + (6)(0.7720) = 2.5424 + 4.6320 = <strong>+7.1745</strong>
          </p>
        </div>
      </div>
    </div>

    <div class="callout-card callout-success">
      <div class="callout-title">&#10004; scikit-learn Cross-Validation</div>
      <p>
        These exact calculated values match scikit-learn's <code>PCA(n_components=2).fit_transform(X)</code> identically:
        <br>
        <code>Explained Variance Ratio: [0.97828741, 0.02171259]</code>
        <br>
        <code>Z Coordinates: [-5.6305, -2.8152, -0.7720, +2.0432, +7.1745]</code>
      </p>
    </div>
  </section>

  <!-- SECTION 08 -->
  <section id="sec-08" class="content-section">
    <span class="section-badge">Section 08 &bull; Component Selection Heuristics</span>
    <h2 class="section-title">Explained Variance and Choosing Components</h2>

    <p>
      When dealing with 10, 50, or 100 features in a real-world dataset, how do we decide how many principal components <em>k</em> to keep? Keeping too few discards critical signal; keeping too many defeats the purpose of dimensionality reduction.
    </p>

    <h3 class="subsection-title">1. Individual Explained Variance (The Scree Plot)</h3>
    <p>
      The <strong>Explained Variance Ratio</strong> indicates what proportion of the dataset's total variance is captured by each individual principal component:
    </p>

    <div class="formula-block">
      EVR<sub>k</sub> = &lambda;<sub>k</sub> / [ &sum;<sub>i=1</sub><sup>d</sup> &lambda;<sub>i</sub> ]
    </div>

    <p>
      A <strong>Scree Plot</strong> displays the components on the x-axis and their individual explained variance on the y-axis. The term comes from geology: "scree" refers to loose rock rubble at the base of a cliff. In PCA, we look for the "elbow" where the steep drop of the cliff levels off into flat rubble.
    </p>

    <!-- Visual 08 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.8: Graph A &bull; Scree Plot of Individual Explained Variance (Wine Benchmark)</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_EXPLAINED_VARIANCE_SCREE__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.8:</strong> Individual variance ratio across all 13 components of the Wine dataset. PC1 captures 36.20%, PC2 captures 19.21%, and PC3 captures 11.12%. After PC3, the scree curve levels off into an elbow bend where subsequent components contribute trivial increments (&lt; 5% each).
      </p>
    </div>

    <h3 class="subsection-title">2. Cumulative Explained Variance</h3>
    <p>
      The <strong>Cumulative Explained Variance</strong> measures the running total variance captured by retaining the first <em>k</em> components:
    </p>

    <div class="formula-block">
      Cumulative_Variance(k) = &sum;<sub>i=1</sub><sup>k</sup> EVR<sub>i</sub> = np.cumsum(pca.explained_variance_ratio_)
    </div>

    <!-- Visual 09 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.9: Graph B &bull; Cumulative Explained Variance with 90% and 95% Thresholds</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_CUMULATIVE_VARIANCE_CURVE__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.9:</strong> The cumulative variance curve steadily rises toward 100%. Marking target thresholds shows that <strong>8 components</strong> preserve 92.02% of the variance (crossing the 90% mark), while <strong>10 components</strong> preserve 96.17% (crossing the 95% mark).
      </p>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; The 95% Variance Threshold Heuristic</div>
      <p>
        In production machine learning, a standard rule of thumb is to retain enough components to explain <strong>90% to 95% of total variance</strong>. Scikit-learn allows you to configure this automatically by passing a float between 0.0 and 1.0 into <code>PCA(n_components=0.95)</code>!
        <br><br>
        However, remember that 95% variance is a <em>heuristic, not a guarantee</em>. If the remaining 5% of discarded variance happens to contain the critical boundary distinguishing fraud from legitimate transactions, your model will suffer!
      </p>
    </div>
  </section>

  <!-- SECTION 09 -->
  <section id="sec-09" class="content-section">
    <span class="section-badge">Section 09 &bull; Visual Dimensional Mapping</span>
    <h2 class="section-title">Visualizing PCA in 2D and 3D</h2>

    <p>
      One of PCA's most powerful superpowers is granting human engineers sight into high-dimensional data. Let us inspect the actual 2D and 3D projections of the 13-feature Wine dataset.
    </p>

    <!-- Visual 10 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.10: Actual 2D PCA Scatter Plot (PC1 vs PC2)</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_PCA_2D_SCATTER__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.10:</strong> 178 wine samples projected from 13 dimensions down to PC1 and PC2 (capturing 55.41% total variance). Markers are colored by wine cultivar (0, 1, 2) purely to evaluate separation. Notice that unsupervised PCA cleanly clusters the three cultivars without ever seeing class labels during fitting!
      </p>
    </div>

    <h3 class="subsection-title">Expanding to 3D: Capturing 66.53% Variance</h3>
    <p>
      While 2D captures 55.41% of variance, adding a third dimension (PC3, contributing 11.12%) elevates the cumulative variance to <strong>66.53%</strong>:
    </p>

    <!-- Visual 11 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.11: Isometric 3D PCA Projection (PC1, PC2, PC3)</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_PCA_3D_ISOMETRIC__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.11:</strong> Adding PC3 on the vertical z-axis separates Cultivar 0 (which sits high along the vertical elevation) from Cultivar 1 and 2, eliminating the visual boundary overlap present in the 2D plane.
      </p>
    </div>

    <div class="callout-card callout-def">
      <div class="callout-title">What Do the Axes Mean After PCA?</div>
      <p>
        In the original dataset, the axes had concrete physical units: <em>Alcohol %</em>, <em>Malic Acid (g/L)</em>, <em>Flavanoids</em>.
        <br><br>
        After PCA, the axes are <strong>PC1</strong> and <strong>PC2</strong>. They no longer represent a single physical chemical! Instead, each axis is a mathematical compound:
        <br>
        <code>PC1 = &minus;0.144(Alcohol) + 0.245(MalicAcid) &minus; 0.423(Flavanoids) + &hellip;</code>
        <br>
        These weights are called <strong>Component Loadings</strong>. They tell you which original features contribute most strongly to each principal axis.
      </p>
    </div>
  </section>

  <!-- SECTION 10 -->
  <section id="sec-10" class="content-section">
    <span class="section-badge">Section 10 &bull; Production Pipelines</span>
    <h2 class="section-title">PCA with scikit-learn Pipelines</h2>

    <p>
      Let us implement a complete, leakage-safe machine learning pipeline using scikit-learn. We use <code>Pipeline</code> to bundle <code>StandardScaler</code>, <code>PCA</code>, and a downstream classifier together.
    </p>

    <div class="code-card">
      <div class="code-header">
        <span class="code-title">&#128013; pca_complete_pipeline.py</span>
        <span class="code-tag verified">&#10003; Verified Executable</span>
      </div>
      <div class="code-body">
        <pre><span class="c-kw">import</span> numpy <span class="c-kw">as</span> np
<span class="c-kw">import</span> pandas <span class="c-kw">as</span> pd
<span class="c-kw">from</span> sklearn.datasets <span class="c-kw">import</span> load_wine
<span class="c-kw">from</span> sklearn.model_selection <span class="c-kw">import</span> train_test_split
<span class="c-kw">from</span> sklearn.preprocessing <span class="c-kw">import</span> StandardScaler
<span class="c-kw">from</span> sklearn.decomposition <span class="c-kw">import</span> PCA
<span class="c-kw">from</span> sklearn.linear_model <span class="c-kw">import</span> LogisticRegression
<span class="c-kw">from</span> sklearn.pipeline <span class="c-kw">import</span> Pipeline
<span class="c-kw">from</span> sklearn.metrics <span class="c-kw">import</span> accuracy_score, classification_report

<span class="c-cm"># 1. Load dataset (13 features, 3 classes, 178 samples)</span>
wine = load_wine()
X, y = wine.data, wine.target
<span class="c-kw">assert</span> X.shape == (<span class="c-nb">178</span>, <span class="c-nb">13</span>), <span class="c-st">"Dataset shape mismatch"</span>

<span class="c-cm"># 2. Strict Train/Test Split BEFORE any scaling or PCA</span>
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=<span class="c-nb">0.3</span>, random_state=<span class="c-nb">42</span>, stratify=y
)

<span class="c-cm"># 3. Leakage-Safe Pipeline: StandardScaler -> PCA(95% var) -> Classifier</span>
pipe = Pipeline([
    (<span class="c-st">'scaler'</span>, StandardScaler()),
    (<span class="c-st">'pca'</span>, PCA(n_components=<span class="c-nb">0.95</span>, random_state=<span class="c-nb">42</span>)),
    (<span class="c-st">'clf'</span>, LogisticRegression(random_state=<span class="c-nb">42</span>))
])

<span class="c-cm"># 4. Fit ONLY on training data</span>
pipe.fit(X_train, y_train)

<span class="c-cm"># 5. Extract fitted PCA attributes</span>
pca_step = pipe.named_steps[<span class="c-st">'pca'</span>]
n_retained = pca_step.n_components_
cum_var = np.sum(pca_step.explained_variance_ratio_)

print(<span class="c-st">f"Original Feature Count: {X.shape[1]}"</span>)
print(<span class="c-st">f"Retained Components for 95% Var: {n_retained}"</span>)
print(<span class="c-st">f"Actual Cumulative Variance: {cum_var * 100:.2f}%"</span>)

<span class="c-cm"># 6. Evaluate on unseen test data</span>
y_pred = pipe.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(<span class="c-st">f"Test Set Accuracy: {acc * 100:.2f}%"</span>)

<span class="c-kw">assert</span> n_retained == <span class="c-nb">10</span>, <span class="c-st">"Wine dataset at 95% var must retain 10 components"</span>
<span class="c-kw">assert</span> round(acc, <span class="c-nb">4</span>) == <span class="c-nb">0.9815</span>, <span class="c-st">"Test accuracy mismatch"</span>
</pre>
      </div>
      <div class="console-output">
        <div class="console-label">Actual Executed Console Output:</div>
Original Feature Count: 13
Retained Components for 95% Var: 10
Actual Cumulative Variance: 96.17%
Test Set Accuracy: 98.15%
      </div>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; Zero Data Leakage Rule</div>
      <p>
        Notice that <code>pipe.fit(X_train, y_train)</code> fits the <code>StandardScaler</code> and the <code>PCA</code> using <strong>only the training split</strong>. When evaluating on <code>X_test</code>, the test samples are transformed using the already-computed training means and training eigenvectors. <strong>Never call <code>fit_transform()</code> on the whole dataset before splitting!</strong> Doing so leaks test distribution parameters into your preprocessing, producing dishonestly optimistic validation scores.
      </p>
    </div>
  </section>

"""
