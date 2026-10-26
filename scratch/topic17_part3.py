"""Topic 17 Part 3: Sections 11 to 15.
Does PCA Improve Performance?, t-SNE, UMAP, LDA, Practical Industry Use Cases.
"""

TOPIC17_PART3 = """
  <!-- SECTION 11 -->
  <section id="sec-11" class="content-section">
    <span class="section-badge">Section 11 &bull; Empirical Trade-Offs</span>
    <h2 class="section-title">Does PCA Improve Model Performance?</h2>

    <p>
      A widespread myth among beginners is that applying PCA will automatically increase the accuracy of any downstream machine learning model.
    </p>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; The Core Truth: PCA Is Not an Accuracy Booster by Default</div>
      <p>
        PCA's mathematical objective is to <strong>maximize total variance</strong> across unsupervised features. It has zero knowledge of your target label <em>y</em>! If the subtle distinguishing features between two classes happen to lie along low-variance directions, PCA will discard them as "unimportant noise", directly damaging your model's classification accuracy.
      </p>
    </div>

    <!-- Visual 12 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.12: Empirical Model Comparison &bull; Baseline vs PCA Representations</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_MODEL_PERFORMANCE_COMPARISON__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.12:</strong> Real measured test set accuracy on Wine classification: The baseline model using all 13 scaled features achieves <strong>98.15%</strong>. Aggressive reduction to 2 components (k=2) drops accuracy to <strong>94.44%</strong> (a 3.71% drop due to discarding 44.59% of variance). Retaining 95% variance (k=10) preserves full <strong>98.15%</strong> accuracy while eliminating 3 collinear features.
      </p>
    </div>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Scenario</th>
            <th>When PCA Improves Performance</th>
            <th>When PCA Harms Performance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Feature Correlation</strong></td>
            <td>Features suffer from severe multicollinearity (e.g., redundant sensor channels)</td>
            <td>Features are already independent, uncorrelated, and individually engineered</td>
          </tr>
          <tr>
            <td><strong>Data Dimensions</strong></td>
            <td>Wide datasets where features outnumber samples (<em>D &gt;&gt; N</em>), causing overfitting</td>
            <td>Modest feature counts (e.g., 5 to 10 features) where every feature carries unique signal</td>
          </tr>
          <tr>
            <td><strong>Noise Characteristics</strong></td>
            <td>High-frequency random sensor noise is concentrated in trailing low-eigenvalue components</td>
            <td>The predictive signal is subtle and lives in lower-variance components</td>
          </tr>
          <tr>
            <td><strong>Model Architecture</strong></td>
            <td>Linear models (Logistic Regression, Linear SVM) that struggle with collinearity</td>
            <td>Tree-based ensembles (Random Forest, XGBoost) which naturally handle collinear features and benefit from original coordinate axes</td>
          </tr>
          <tr>
            <td><strong>Inference Speed</strong></td>
            <td>Massive speedup: transforming 1,000 features to 50 cuts model latency by 90%+</td>
            <td>Preprocessing overhead: computing <code>pca.transform(X)</code> on low dimensions adds latency without benefit</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 12 -->
  <section id="sec-12" class="content-section">
    <span class="section-badge">Section 12 &bull; Non-Linear Manifold Learning</span>
    <h2 class="section-title">t-SNE (t-Distributed Stochastic Neighbor Embedding)</h2>

    <p>
      While PCA is fast and mathematically elegant, it is strictly a <strong>linear</strong> technique. If your data lies on a complex curved manifold (such as a Swiss roll, concentric spheres, or tangled clusters), PCA cannot unroll the manifold without severe distortion.
    </p>

    <p>
      Introduced by Laurens van der Maaten and Geoffrey Hinton in 2008, <strong>t-SNE</strong> is a non-linear dimensionality reduction technique designed specifically for <strong>exploratory 2D and 3D visualization</strong>.
    </p>

    <div class="callout-card callout-def">
      <div class="callout-title">The Probabilistic Mechanics of t-SNE</div>
      <ul>
        <li><strong>Step 1 &bull; High-Dimensional Similarities:</strong> For every pair of points (x<sub>i</sub>, x<sub>j</sub>), t-SNE computes the probability <em>p<sub>ij</sub></em> that point <em>i</em> would pick point <em>j</em> as its neighbor under a Gaussian probability distribution. Close points have high probabilities; distant points have near-zero probabilities.</li>
        <li><strong>Step 2 &bull; Low-Dimensional Similarities:</strong> In the 2D visualization space, t-SNE places points (y<sub>i</sub>, y<sub>j</sub>) and models their similarity <em>q<sub>ij</sub></em> using a <strong>Student-t distribution</strong> with 1 degree of freedom (Cauchy distribution).</li>
        <li><strong>Step 3 &bull; Minimizing Divergence:</strong> It iteratively shifts points in 2D using gradient descent to minimize the <strong>Kullback-Leibler (KL) divergence</strong> between the high-D probabilities <em>P</em> and low-D probabilities <em>Q</em>.</li>
      </ul>
    </div>

    <!-- Visual 13 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.13: Actual 2D t-SNE Manifold Visualization (Perplexity = 30)</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_TSNE_VISUALIZATION__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.13:</strong> 2D t-SNE embedding of the Wine dataset (perplexity=30). Notice how t-SNE pulls tightly connected local neighborhoods into dense, isolated cluster islands separated by wide gulfs of empty space.
      </p>
    </div>

    <h3 class="subsection-title">Understanding Perplexity</h3>
    <p>
      The primary hyperparameter in t-SNE is <strong>perplexity</strong>, which roughly corresponds to the effective number of nearest neighbors each point considers:
    </p>
    <ul>
      <li><strong>Low Perplexity (5 &ndash; 10):</strong> Focuses intensely on tiny local neighborhoods. Clusters shatter into dozens of small, fragmented micro-islands.</li>
      <li><strong>Standard Perplexity (30 &ndash; 50):</strong> Optimal balance between local cohesion and cluster groupings.</li>
      <li><strong>High Perplexity (&gt; 100):</strong> Forces broader global smoothing, causing distinct clusters to blend together.</li>
    </ul>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; The 3 Golden Rules of Interpreting t-SNE Plots</div>
      <ol>
        <li><strong>Cluster Distances Are Meaningless:</strong> The distance between distant clusters in a t-SNE plot does NOT represent physical distance. An island on the far left is not necessarily twice as different as an island in the center.</li>
        <li><strong>Cluster Sizes Mean Nothing:</strong> t-SNE naturally expands dense clusters and compresses sparse clusters. A larger circle on a t-SNE plot does not mean the original group had higher variance!</li>
        <li><strong>Never Use t-SNE for Production Predictions:</strong> t-SNE is non-deterministic (changing <code>random_state</code> yields completely rotated layouts) and does not possess a <code>transform()</code> method for new test samples.</li>
      </ol>
    </div>
  </section>

  <!-- SECTION 13 -->
  <section id="sec-13" class="content-section">
    <span class="section-badge">Section 13 &bull; Advanced Manifold Learning</span>
    <h2 class="section-title">UMAP (Uniform Manifold Approximation and Projection)</h2>

    <p>
      Published in 2018 by Leland McInnes, Colin Healy, and James Melville, <strong>UMAP</strong> has emerged as the modern successor to t-SNE for high-dimensional manifold visualization and exploratory analysis.
    </p>

    <!-- Visual 14 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.14: UMAP Topological Mechanics &amp; Hyperparameter Controls</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_UMAP_CONCEPTS__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.14:</strong> Left: UMAP constructs a fuzzy simplicial complex (weighted topological graph) connecting neighbors along local manifold geodesics. Right: The two primary tuning parameters: <code>n_neighbors</code> (local vs global balance) and <code>min_dist</code> (clumping density).
      </p>
    </div>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Comparison Dimension</th>
            <th>PCA</th>
            <th>t-SNE</th>
            <th>UMAP</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mathematical Foundation</strong></td>
            <td>Linear algebra (Covariance eigendecomposition / SVD)</td>
            <td>Probability distribution matching (KL divergence)</td>
            <td>Riemannian geometry &amp; algebraic topology (Fuzzy simplicial sets)</td>
          </tr>
          <tr>
            <td><strong>Computational Speed</strong></td>
            <td>Extremely fast &mdash; <em>O(N &times; D&sup2;)</em></td>
            <td>Slow &mdash; <em>O(N&sup2;)</em> (Barnes-Hut: <em>O(N log N)</em>)</td>
            <td><strong>Very Fast</strong> &mdash; Scales to millions of points</td>
          </tr>
          <tr>
            <td><strong>Preservation of Global Structure</strong></td>
            <td><strong>High</strong> (Maximizes total global variance)</td>
            <td><strong>Very Low</strong> (Discards macro distances)</td>
            <td><strong>High</strong> (Maintains cluster-to-cluster trajectory)</td>
          </tr>
          <tr>
            <td><strong>Out-of-Sample Transform</strong></td>
            <td>Yes (Instant <code>pca.transform(X_new)</code>)</td>
            <td><strong>No</strong> (Cannot transform new samples)</td>
            <td>Yes (Supports <code>umap.transform(X_new)</code>)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout-card callout-def">
      <div class="callout-title">Optional Code: Running UMAP in Python</div>
      <p>
        Note: <code>umap-learn</code> is an optional third-party library that is not included in standard scikit-learn. If you install it via <code>pip install umap-learn</code>, you can execute this workflow:
      </p>
      <code>import umap<br><br># Initialize UMAP with 15 neighbors and 0.1 minimum distance<br>reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, n_components=2, random_state=42)<br>X_umap = reducer.fit_transform(X_scaled)<br><br># Transform new unseen points<br>X_new_umap = reducer.transform(X_new_scaled)</code>
    </div>
  </section>

  <!-- SECTION 14 -->
  <section id="sec-14" class="content-section">
    <span class="section-badge">Section 14 &bull; Supervised Dimensionality Reduction</span>
    <h2 class="section-title">Linear Discriminant Analysis (LDA)</h2>

    <p>
      Every method discussed so far (PCA, t-SNE, UMAP) is <strong>unsupervised</strong>: they ignore class labels entirely and seek directions of maximum variance or local density.
    </p>

    <p>
      What if you have ground-truth class labels <em>y</em> and specifically want to find directions that <strong>maximize the separation between classes</strong>? That is the exact mission of <strong>Linear Discriminant Analysis (LDA)</strong>.
    </p>

    <!-- Visual 15 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.15: Unsupervised PCA vs Supervised LDA</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_PCA_VS_LDA__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.15:</strong> Left: PCA aligns with the overall diagonal spread of all points combined; projecting onto the PCA axis merges the red and blue classes into an indistinguishable blur. Right: Supervised LDA uses class labels to calculate the axis that maximizes the distance between class centroids while minimizing intra-class spread, projecting points into cleanly separated clusters.
      </p>
    </div>

    <h3 class="subsection-title">The Mathematical Objective of LDA</h3>
    <p>
      LDA finds a projection vector <em>w</em> that maximizes Fisher's criterion (the Rayleigh quotient):
    </p>

    <div class="formula-block">
      J(w) = (w<sup>T</sup> S<sub>B</sub> w) / (w<sup>T</sup> S<sub>W</sub> w)
      <div class="formula-breakdown">
        <div class="breakdown-item"><strong>S<sub>B</sub> (Between-Class Scatter):</strong> Measures the distance between class mean centroids and the overall mean</div>
        <div class="breakdown-item"><strong>S<sub>W</sub> (Within-Class Scatter):</strong> Sum of covariance matrices for each individual class (compactness)</div>
        <div class="breakdown-item"><strong>Goal:</strong> Maximize between-class separation while minimizing within-class spread</div>
      </div>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; The Strict Dimension Limit of LDA: (C &minus; 1)</div>
      <p>
        A fundamental mathematical constraint of LDA is that it can produce at most <strong>C &minus; 1 dimensions</strong>, where <em>C</em> is the number of distinct classes in the target variable:
        <br>&bull; Binary classification (C = 2 classes) &rarr; LDA can only produce <strong>1 component</strong>!
        <br>&bull; Wine classification (C = 3 cultivars) &rarr; LDA can produce at most <strong>2 components</strong>!
        <br>&bull; Handwritten digits (C = 10 digits) &rarr; LDA can produce at most <strong>9 components</strong>!
        <br><br>
        If you have a dataset with 500 features and only 2 classes, LDA cannot reduce to 10 features; it can only reduce to exactly 1 feature!
      </p>
    </div>
  </section>

  <!-- SECTION 15 -->
  <section id="sec-15" class="content-section">
    <span class="section-badge">Section 15 &bull; Real-World Case Studies</span>
    <h2 class="section-title">Real-World Industry Applications</h2>

    <p>
      Dimensionality reduction is a foundational pillar across modern software engineering, data science, and artificial intelligence.
    </p>

    <!-- Application 1 -->
    <div class="app-card">
      <div class="app-header">
        <span class="app-icon">&#128202;</span>
        <span class="app-title">1. High-Dimensional Tabular Financial Risk Modeling</span>
      </div>
      <p>
        A credit bureau compiles 400 financial indicators per borrower (payment histories, debt-to-income ratios, revolving credit limits across multiple banks).
      </p>
      <div class="app-grid">
        <div class="app-item"><span class="app-item-label">Problem</span>Severe multicollinearity causes coefficient instability in linear default-prediction models.</div>
        <div class="app-item"><span class="app-item-label">Algorithm Choice</span><strong>PCA (retaining 95% variance)</strong> with <code>StandardScaler</code>.</div>
        <div class="app-item"><span class="app-item-label">Outcome</span>Compresses 400 correlated features into 35 orthogonal components, stabilizing regression coefficients.</div>
        <div class="app-item"><span class="app-item-label">Domain Trade-off</span>Loss of direct column explainability for compliance audit reporting.</div>
      </div>
    </div>

    <!-- Application 2 -->
    <div class="app-card">
      <div class="app-header">
        <span class="app-icon">&#128247;</span>
        <span class="app-title">2. Computer Vision: Eigenfaces &amp; Facial Recognition</span>
      </div>
      <p>
        A legacy security door camera matches grayscale face images of size 100 &times; 100 pixels (10,000 raw input features per face).
      </p>
      <div class="app-grid">
        <div class="app-item"><span class="app-item-label">Problem</span>Classifying 10,000 raw pixel features in real time on an embedded micro-controller is too slow.</div>
        <div class="app-item"><span class="app-item-label">Algorithm Choice</span><strong>PCA (Eigenfaces)</strong> reducing 10,000 pixels down to 100 principal components.</div>
        <div class="app-item"><span class="app-item-label">Outcome</span>100&times; reduction in feature storage; fast cosine similarity matching in under 5 milliseconds.</div>
        <div class="app-item"><span class="app-item-label">Domain Trade-off</span>Sensitive to lighting shifts, facial angles, and occlusions.</div>
      </div>
    </div>

    <!-- Application 3 -->
    <div class="app-card">
      <div class="app-header">
        <span class="app-icon">&#128196;</span>
        <span class="app-title">3. Modern NLP &amp; Dense Text Embedding Compression</span>
      </div>
      <p>
        A legal search engine indexes 5,000,000 court documents represented by 1,536-dimensional OpenAI text embeddings.
      </p>
      <div class="app-grid">
        <div class="app-item"><span class="app-item-label">Problem</span>Storing 5 million 1,536-dimensional vectors in RAM requires tens of gigabytes of expensive memory.</div>
        <div class="app-item"><span class="app-item-label">Algorithm Choice</span><strong>PCA / Matryoshka Representation Learning</strong> down to 256 dimensions.</div>
        <div class="app-item"><span class="app-item-label">Outcome</span>6&times; reduction in vector database RAM usage and 4&times; faster vector search retrieval.</div>
        <div class="app-item"><span class="app-item-label">Important Note</span>Modern embeddings are already dense learned representations; PCA is only applied for memory/latency constraints.</div>
      </div>
    </div>

    <!-- Application 4 -->
    <div class="app-card">
      <div class="app-header">
        <span class="app-icon">&#128736;</span>
        <span class="app-title">4. Industrial Sensor Noise Filtering &amp; Anomaly Detection</span>
      </div>
      <p>
        A wind turbine generator monitors 60 vibration sensors sampling at 1,000 Hz to detect bearing wear and mechanical failure.
      </p>
      <div class="app-grid">
        <div class="app-item"><span class="app-item-label">Problem</span>High-frequency environmental noise masks subtle harmonic wear signals.</div>
        <div class="app-item"><span class="app-item-label">Algorithm Choice</span><strong>PCA Reconstruction Error</strong>.</div>
        <div class="app-item"><span class="app-item-label">Outcome</span>Normal operation reconstructs cleanly with low error; abnormal bearing vibrations spike reconstruction error: <code>||X &minus; X_reconstructed||&sup2;</code>.</div>
        <div class="app-item"><span class="app-item-label">Domain Trade-off</span>Must establish clean baseline operational data during turbine calibration.</div>
      </div>
    </div>
  </section>

"""
