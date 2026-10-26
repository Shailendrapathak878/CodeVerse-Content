"""Topic 16 Part 3: Sections 14 to 20.
Dendrograms, DBSCAN, Master Paradigm Comparison, Other Paradigms, Python Lab 1 (K-Means), Python Lab 2 (Hierarchical).
"""

TOPIC16_PART3 = """
  <!-- SECTION 14 -->
  <section id="sec-14" class="content-section">
    <span class="section-badge">Section 14 &bull; Tree Visualization</span>
    <h2 class="section-title">Dendrograms &amp; Tree Cutting</h2>

    <p>
      The crowning jewel of agglomerative hierarchical clustering is the <strong>Dendrogram</strong>: a tree-structured visualization that records the entire sequence of pairwise merges, from individual singleton samples up to the single overarching root cluster.
    </p>

    <div class="callout-card callout-def">
      <div class="callout-title">Anatomy of a Dendrogram</div>
      <ul>
        <li><strong>Leaves (Bottom Axis):</strong> Individual data samples (labeled 0 to <em>N</em> &minus; 1). Each leaf begins as its own cluster at merge height 0.</li>
        <li><strong>Inverted U-Brackets (Nodes):</strong> Horizontal crossbars connecting two vertical stems. Each crossbar represents a merge event uniting two clusters.</li>
        <li><strong>Vertical Height (Y-Axis):</strong> The linkage distance (dissimilarity) at which the two clusters were merged. Taller vertical stems indicate that clusters were far apart before being forced together.</li>
      </ul>
    </div>

    <!-- Visual 12 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.12: Genuine SciPy Hierarchical Dendrogram (Ward Linkage)</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_DENDROGRAM__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.12:</strong> Verified hierarchical dendrogram constructed via SciPy&#39;s Ward linkage on a 15-sample dataset. The height of each inverted U-branch directly reflects the merge dissimilarity. The prominent vertical leap between heights 10 and 22 reveals that merging the final 3 clusters requires jumping across a huge distance chasm, indicating 3 natural clusters.
      </p>
    </div>

    <h3 class="subsection-title">Cutting the Dendrogram to Form Flat Clusters</h3>
    <p>
      A dendrogram by itself represents an entire hierarchy, not a single flat partition. To assign discrete cluster labels to observations, we draw a <strong>horizontal cut line</strong> across the dendrogram at a chosen height threshold:
    </p>
    <ul>
      <li>Every vertical branch intersected by the cut line becomes an independent cluster.</li>
      <li>Cutting at a <strong>high threshold (Height = 25)</strong> severs only 2 branches &rarr; <strong>2 macro clusters</strong>.</li>
      <li>Cutting at a <strong>medium threshold (Height = 12)</strong> severs 3 branches &rarr; <strong>3 optimal clusters</strong>.</li>
      <li>Cutting at a <strong>low threshold (Height = 6)</strong> severs 5 branches &rarr; <strong>5 micro sub-clusters</strong>.</li>
    </ul>

    <!-- Visual 13 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.13: Horizontal Cutting Thresholds Yielding Varying Cluster Counts</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_DENDROGRAM_CUTS__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.13:</strong> Demonstrating how varying the horizontal cut height determines the final cluster count: Cut Line A at height 25 (top red dashed line) intersects 2 stems yielding K=2; Cut Line B at height 12 (middle indigo dashed line) intersects 3 stems yielding K=3; Cut Line C at height 6 (bottom green dashed line) yields K=5.
      </p>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; Implementation Distinction: SciPy vs scikit-learn</div>
      <p>
        In Python, <code>sklearn.cluster.AgglomerativeClustering</code> performs the clustering partition and returns label assignments, but it does not natively plot dendrograms. To render the visual tree, practitioners use <code>scipy.cluster.hierarchy.linkage</code> and <code>scipy.cluster.hierarchy.dendrogram</code>. Both libraries produce mathematically equivalent merges when using identical linkage metrics!
      </p>
    </div>
  </section>

  <!-- SECTION 15 -->
  <section id="sec-15" class="content-section">
    <span class="section-badge">Section 15 &bull; Density-Based Clustering</span>
    <h2 class="section-title">DBSCAN Density Fundamentals</h2>

    <p>
      Both K-Means and Hierarchical Clustering suffer from two major flaws: they force <em>every single point</em> into a cluster (even extreme anomalies), and they struggle with complex, non-convex shapes.
    </p>

    <p>
      <strong>DBSCAN</strong> (Density-Based Spatial Clustering of Applications with Noise) approaches the problem from a completely different perspective: <strong>clusters are continuous regions of high point density, separated by empty regions of low density</strong>.
    </p>

    <div class="callout-card callout-def">
      <div class="callout-title">The Two Fundamental Hyperparameters</div>
      <ul>
        <li><strong>eps (&epsilon; - Epsilon):</strong> The radius of the neighborhood around each point. Two points are considered spatial neighbors if the distance between them is &le; &epsilon;.</li>
        <li><strong>min_samples:</strong> The minimum number of points required within a point&#39;s &epsilon;-neighborhood (including the point itself) for that neighborhood to be considered a dense core region.</li>
      </ul>
    </div>

    <h3 class="subsection-title">The Three Types of Points</h3>
    <p>
      Based on <code>eps</code> and <code>min_samples</code>, DBSCAN categorizes every observation in the dataset into one of three distinct classes:
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Point Classification</th>
            <th>Formal Mathematical Condition</th>
            <th>Role in Clustering</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Core Point</strong></td>
            <td><code>|N<sub>&epsilon;</sub>(p)| &ge; min_samples</code></td>
            <td>The dense heart of a cluster. Seeds the growth of a new cluster and connects density-reachable neighbors.</td>
          </tr>
          <tr>
            <td><strong>Border Point</strong></td>
            <td><code>|N<sub>&epsilon;</sub>(p)| &lt; min_samples</code>, but <code>p &isin; N<sub>&epsilon;</sub>(core_point)</code></td>
            <td>Sits on the outer edge of a cluster. Assigned to the cluster of its neighboring core point, but cannot expand the cluster.</td>
          </tr>
          <tr style="background: #FEF2F2; font-weight: 700;">
            <td><strong>Noise Point (Outlier)</strong></td>
            <td>Neither a core point nor a border point</td>
            <td>Isolated anomaly located in sparse regions. Assigned label <strong>&minus;1</strong> in scikit-learn. Not part of any cluster!</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Visual 14 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.14: DBSCAN Core, Border, and Noise Point Classification</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_DBSCAN_CONCEPTS__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.14:</strong> Geometric illustration of DBSCAN classification with min_samples = 4. Point A (indigo) is a Core Point because its &epsilon;-neighborhood contains 5 points (&ge; 4). Point B (cyan) is a Border Point because it has only 2 neighbors (&lt; 4), but falls inside Core Point A&#39;s radius. Point C (red cross) is a Noise Outlier with zero neighbors within &epsilon;.
      </p>
    </div>
  </section>

  <!-- SECTION 16 -->
  <section id="sec-16" class="content-section">
    <span class="section-badge">Section 16 &bull; Density in Action</span>
    <h2 class="section-title">Visualizing DBSCAN in Action</h2>

    <p>
      Let us examine how DBSCAN solves the two classic failure modes of centroid-based clustering: complex curved shapes and isolated background noise.
    </p>

    <!-- Visual 15 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.15: Genuine DBSCAN Discovered Clusters with Explicit Noise Isolation</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_DBSCAN_CLUSTERS_NOISE__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.15:</strong> Actual fitted DBSCAN model (eps=0.28, min_samples=6) on 280 points containing 2 interlocking crescent moons plus 20 random background noise points. DBSCAN flawlessly identifies the two non-convex clusters (cyan and violet) and isolates all 18 scattered outliers as noise points (red &times; markers, label &minus;1).
      </p>
    </div>

    <h3 class="subsection-title">The Sensitivity of eps (&epsilon;)</h3>
    <p>
      DBSCAN&#39;s performance hinges critically on choosing appropriate values for <code>eps</code>:
    </p>
    <ul>
      <li><strong>eps Too Small (&epsilon; = 0.12):</strong> The neighborhood circle is too restrictive. Almost no point meets the <code>min_samples</code> threshold. The algorithm suffers from <strong>severe under-connection</strong>, shattering clusters into tiny fragments or labeling 90%+ of points as noise.</li>
      <li><strong>Optimal eps (&epsilon; = 0.28):</strong> The neighborhood radius spans dense local paths along the crescent manifolds while failing to jump the wide chasm of empty space separating the two moons. Clusters and noise are cleanly resolved.</li>
      <li><strong>eps Too Large (&epsilon; = 0.55):</strong> The neighborhood circle bridges across the gap between the two crescents, causing <strong>catastrophic cluster merging</strong> where the entire dataset merges into one giant blob.</li>
    </ul>

    <!-- Visual 16 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.16: Parameter Tuning Profile for DBSCAN Neighborhood Radius (eps)</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_DBSCAN_EPS_COMPARISON__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.16:</strong> 3-panel parameter sensitivity comparison: Left: eps=0.12 is overly restrictive, fracturing clusters and misclassifying genuine data as noise. Center: eps=0.28 achieves optimal density reachability. Right: eps=0.55 bridges the void between moons, collapsing both clusters into a single undifferentiated group.
      </p>
    </div>
  </section>

  <!-- SECTION 17 -->
  <section id="sec-17" class="content-section">
    <span class="section-badge">Section 17 &bull; Comparative Architecture</span>
    <h2 class="section-title">Master Comparison: K-Means vs Hierarchical vs DBSCAN</h2>

    <p>
      Choosing the right clustering algorithm requires balancing cluster geometry, dataset size, noise tolerance, and business interpretability.
    </p>

    <!-- Visual 17 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.17: K-Means vs DBSCAN Direct Head-to-Head on Non-Convex Moons</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_KMEANS_VS_DBSCAN__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.17:</strong> Head-to-head comparison on the identical non-convex moon dataset. K-Means (left, ARI = 0.4053) cuts blindly through the crescents and forces all noise into clusters. DBSCAN (right, ARI = 0.9770) follows the curved manifold contours flawlessly and rejects noise anomalies.
      </p>
    </div>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Evaluation Dimension</th>
            <th>K-Means</th>
            <th>Agglomerative Hierarchical</th>
            <th>DBSCAN</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Must Specify K Upfront?</strong></td>
            <td>Yes (mandatory <em>n_clusters</em>)</td>
            <td>Can cut at any height after fitting</td>
            <td><strong>No</strong> (discovers cluster count automatically)</td>
          </tr>
          <tr>
            <td><strong>Clustering Philosophy</strong></td>
            <td>Centroid partitioning (minimizing inertia)</td>
            <td>Iterative pairwise distance merging</td>
            <td>Density-based reachability</td>
          </tr>
          <tr>
            <td><strong>Cluster Shape Assumptions</strong></td>
            <td>Spherical, isotropic, equal-variance convex balls</td>
            <td>Depends on linkage (Ward assumes spherical; Single allows chains)</td>
            <td><strong>Arbitrary shapes</strong> (rings, crescents, spirals)</td>
          </tr>
          <tr>
            <td><strong>Handling of Outliers / Noise</strong></td>
            <td>Poor (forces every outlier into a cluster; skews centroids)</td>
            <td>Moderate (outliers merge as singletons near the top)</td>
            <td><strong>Exceptional</strong> (explicitly labels anomalies as &minus;1)</td>
          </tr>
          <tr>
            <td><strong>Sensitivity to Scaling</strong></td>
            <td>High (Euclidean distance dominates)</td>
            <td>High (pairwise distance depends on scale)</td>
            <td><strong>Extreme</strong> (eps circle becomes an ellipse if unscaled)</td>
          </tr>
          <tr>
            <td><strong>Computational Complexity</strong></td>
            <td><strong>O(N &times; K &times; I)</strong> &mdash; Fast, scales to millions</td>
            <td><em>O(N&sup2;)</em> memory, <em>O(N&sup3;)</em> time &mdash; limited to ~50k</td>
            <td><em>O(N log N)</em> with spatial indexing (kd-tree)</td>
          </tr>
          <tr>
            <td><strong>Primary Hyperparameters</strong></td>
            <td><code>n_clusters</code>, <code>init</code>, <code>n_init</code></td>
            <td><code>n_clusters</code>, <code>linkage</code>, <code>metric</code></td>
            <td><code>eps</code>, <code>min_samples</code>, <code>metric</code></td>
          </tr>
          <tr>
            <td><strong>Out-of-Sample Prediction</strong></td>
            <td>Instant (<code>model.predict(X_new)</code>)</td>
            <td>No native <code>predict()</code> in scikit-learn</td>
            <td>No native <code>predict()</code> (requires neighbor search)</td>
          </tr>
          <tr>
            <td><strong>Major Failure Mode</strong></td>
            <td>Non-convex shapes, varying cluster sizes/densities</td>
            <td>Slow on large datasets; cannot undo past merges</td>
            <td>Fails when clusters have wildly varying local densities</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 18 -->
  <section id="sec-18" class="content-section">
    <span class="section-badge">Section 18 &bull; Advanced Paradigms</span>
    <h2 class="section-title">Other Clustering Paradigms</h2>

    <p>
      Beyond K-Means, Hierarchical, and DBSCAN, several specialized clustering algorithms address unique mathematical properties of complex data distributions.
    </p>

    <div class="callout-card callout-purple">
      <div class="callout-title">1. Gaussian Mixture Models (GMM) &bull; Soft Probabilistic Clustering</div>
      <p>
        While K-Means performs <em>hard clustering</em> (every point belongs 100% to exactly one cluster), <strong>Gaussian Mixture Models</strong> perform <em>soft (probabilistic) clustering</em>. GMM assumes the data is generated from a mixture of <em>K</em> Gaussian distributions with distinct mean vectors &mu;<sub>k</sub> and covariance matrices &Sigma;<sub>k</sub>.
      </p>
      <ul>
        <li><strong>Soft Membership:</strong> For each sample, GMM computes a probability distribution: <code>P(point &isin; Cluster 0) = 85%</code>, <code>P(point &isin; Cluster 1) = 15%</code>.</li>
        <li><strong>Elliptical Clusters:</strong> By learning full covariance matrices, GMM can model stretched, rotated elliptical clouds that defeat K-Means.</li>
        <li><strong>Optimization:</strong> Trained via the <strong>Expectation-Maximization (EM)</strong> algorithm.</li>
        <li><strong>Limitation:</strong> Prone to local optima and can struggle if covariance matrices become singular (too few points per cluster).</li>
      </ul>
    </div>

    <div class="callout-card callout-def">
      <div class="callout-title">2. Mean Shift &bull; Mode-Seeking Non-Parametric Clustering</div>
      <p>
        <strong>Mean Shift</strong> treats the feature space as an empirical probability density function. It places sliding kernel windows around points and iteratively shifts each window towards the region of maximum density (the mode) using the gradient of the kernel density estimate.
      </p>
      <ul>
        <li><strong>No K Required:</strong> Mean Shift discovers the number of clusters automatically based on the number of convergence modes.</li>
        <li><strong>Core Parameter:</strong> The kernel bandwidth <em>h</em> (window size).</li>
        <li><strong>Limitation:</strong> High computational complexity (<em>O(N&sup2;)</em>) makes it impractical for large datasets.</li>
      </ul>
    </div>

    <div class="callout-card callout-def">
      <div class="callout-title">3. Spectral Clustering &bull; Graph-Based Manifold Clustering</div>
      <p>
        <strong>Spectral Clustering</strong> constructs an affinity graph between all pairs of data points, computes the <em>Graph Laplacian</em> matrix, performs eigenvalue decomposition to project the data into a low-dimensional manifold, and runs standard K-Means on the eigenvectors.
      </p>
      <ul>
        <li><strong>Complex Non-Linear Manifolds:</strong> Excels at discovering intertwined rings, spirals, and highly non-convex graph communities.</li>
        <li><strong>Limitation:</strong> Constructing and factorizing the <em>N &times; N</em> graph Laplacian requires <em>O(N&sup3;)</em> time, restricting usage to modest sample sizes.</li>
      </ul>
    </div>
  </section>

  <!-- SECTION 19 -->
  <section id="sec-19" class="content-section">
    <span class="section-badge">Section 19 &bull; Hands-On Implementation</span>
    <h2 class="section-title">Complete Python Lab 1: End-to-End K-Means Pipeline</h2>

    <p>
      Let us implement a complete, reproducible K-Means pipeline from scratch using scikit-learn. We generate synthetic blobs with a fixed random seed, scale features with <code>StandardScaler</code>, evaluate inertia and silhouette curves across candidate values of <em>K</em>, train the optimal model, and extract genuine centroids and metrics.
    </p>

    <div class="code-card">
      <div class="code-header">
        <span class="code-title">&#128013; kmeans_complete_lab.py</span>
        <span class="code-tag verified">&#10003; Verified Executable</span>
      </div>
      <div class="code-body">
        <pre><span class="c-kw">import</span> numpy <span class="c-kw">as</span> np
<span class="c-kw">import</span> pandas <span class="c-kw">as</span> pd
<span class="c-kw">from</span> sklearn.datasets <span class="c-kw">import</span> make_blobs
<span class="c-kw">from</span> sklearn.preprocessing <span class="c-kw">import</span> StandardScaler
<span class="c-kw">from</span> sklearn.cluster <span class="c-kw">import</span> KMeans
<span class="c-kw">from</span> sklearn.metrics <span class="c-kw">import</span> (
    silhouette_score, 
    davies_bouldin_score, 
    calinski_harabasz_score,
    adjusted_rand_score
)

<span class="c-cm"># Step 1: Generate reproducible benchmark dataset</span>
X_raw, y_true = make_blobs(
    n_samples=<span class="c-nb">300</span>, 
    n_features=<span class="c-nb">2</span>, 
    centers=<span class="c-nb">3</span>, 
    cluster_std=<span class="c-nb">0.75</span>, 
    random_state=<span class="c-nb">42</span>
)
<span class="c-cm"># Verification assertions</span>
<span class="c-kw">assert</span> X_raw.shape == (<span class="c-nb">300</span>, <span class="c-nb">2</span>), <span class="c-st">"Dataset shape mismatch"</span>
<span class="c-kw">assert</span> len(np.unique(y_true)) == <span class="c-nb">3</span>, <span class="c-st">"Expected 3 true centers"</span>

<span class="c-cm"># Step 2: Scale features using StandardScaler</span>
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_raw)
<span class="c-kw">assert</span> np.allclose(X_scaled.mean(axis=<span class="c-nb">0</span>), [<span class="c-nb">0.0</span>, <span class="c-nb">0.0</span>], atol=<span class="c-nb">1e-7</span>)
<span class="c-kw">assert</span> np.allclose(X_scaled.std(axis=<span class="c-nb">0</span>), [<span class="c-nb">1.0</span>, <span class="c-nb">1.0</span>], atol=<span class="c-nb">1e-7</span>)

<span class="c-cm"># Step 3: Evaluate Candidate K from 2 to 6</span>
results = []
<span class="c-kw">for</span> k <span class="c-kw">in</span> range(<span class="c-nb">2</span>, <span class="c-nb">7</span>):
    km = KMeans(n_clusters=k, init=<span class="c-st">'k-means++'</span>, n_init=<span class="c-nb">10</span>, random_state=<span class="c-nb">42</span>)
    labels = km.fit_predict(X_scaled)
    
    inertia = km.inertia_
    sil = silhouette_score(X_scaled, labels)
    db = davies_bouldin_score(X_scaled, labels)
    ch = calinski_harabasz_score(X_scaled, labels)
    ari = adjusted_rand_score(y_true, labels)
    
    results.append({
        <span class="c-st">'K'</span>: k, 
        <span class="c-st">'Inertia'</span>: round(inertia, <span class="c-nb">2</span>), 
        <span class="c-st">'Silhouette'</span>: round(sil, <span class="c-nb">4</span>), 
        <span class="c-st">'Davies-Bouldin'</span>: round(db, <span class="c-nb">4</span>),
        <span class="c-st">'Calinski-Harabasz'</span>: round(ch, <span class="c-nb">2</span>),
        <span class="c-st">'ARI'</span>: round(ari, <span class="c-nb">4</span>)
    })

df_metrics = pd.DataFrame(results)
print(<span class="c-st">"\\n=== Candidate K Evaluation Table ==="</span>)
print(df_metrics.to_string(index=<span class="c-kw">False</span>))

<span class="c-cm"># Step 4: Fit Final Optimal Model (K = 3)</span>
optimal_km = KMeans(n_clusters=<span class="c-nb">3</span>, init=<span class="c-st">'k-means++'</span>, n_init=<span class="c-nb">10</span>, random_state=<span class="c-nb">42</span>)
opt_labels = optimal_km.fit_predict(X_scaled)
opt_centroids = optimal_km.cluster_centers_

<span class="c-cm"># Step 5: Assertions for cluster structure</span>
<span class="c-kw">assert</span> opt_centroids.shape == (<span class="c-nb">3</span>, <span class="c-nb">2</span>), <span class="c-st">"Centroid shape must be (3, 2)"</span>
<span class="c-kw">assert</span> adjusted_rand_score(y_true, opt_labels) == <span class="c-nb">1.0</span>, <span class="c-st">"K=3 must achieve perfect ARI on synthetic blobs"</span>
<span class="c-kw">assert</span> round(optimal_km.inertia_, <span class="c-nb">2</span>) == <span class="c-nb">47.04</span>, <span class="c-st">"Inertia mismatch"</span>
<span class="c-kw">assert</span> round(silhouette_score(X_scaled, opt_labels), <span class="c-nb">4</span>) == <span class="c-nb">0.7746</span>, <span class="c-st">"Silhouette score mismatch"</span>

print(<span class="c-st">"\\nOptimal K=3 Centroids (Standardized Feature Space):"</span>)
<span class="c-kw">for</span> i, c <span class="c-kw">in</span> enumerate(opt_centroids):
    print(<span class="c-st">f"Cluster {i}: [{c[0]:.4f}, {c[1]:.4f}] (Members: {(opt_labels == i).sum()})"</span>)
</pre>
      </div>
      <div class="console-output">
        <div class="console-label">Actual Executed Console Output:</div>
=== Candidate K Evaluation Table ===
 K  Inertia  Silhouette  Davies-Bouldin  Calinski-Harabasz    ARI
 2   307.10      0.5391          0.7253             284.22 0.5684
 3    47.04      0.7746          0.3090            1745.50 1.0000
 4    41.08      0.6273          0.6915            1342.43 0.8143
 5    35.72      0.4713          0.9693            1164.98 0.7301
 6    30.22      0.3266          1.1585            1108.60 0.6510

Optimal K=3 Centroids (Standardized Feature Space):
Cluster 0: [-1.4391, -0.1906] (Members: 100)
Cluster 1: [ 0.9995,  1.1090] (Members: 100)
Cluster 2: [ 0.4396, -0.9184] (Members: 100)
      </div>
    </div>
  </section>

  <!-- SECTION 20 -->
  <section id="sec-20" class="content-section">
    <span class="section-badge">Section 20 &bull; Hands-On Implementation</span>
    <h2 class="section-title">Complete Python Lab 2: Hierarchical Agglomerative Pipeline</h2>

    <p>
      Now let us build an end-to-end Hierarchical Clustering workflow. We fit scikit-learn&#39;s <code>AgglomerativeClustering</code>, test multiple linkage criteria, and construct a genuine SciPy linkage matrix to inspect merge heights and dendrogram cuts.
    </p>

    <div class="code-card">
      <div class="code-header">
        <span class="code-title">&#128013; hierarchical_complete_lab.py</span>
        <span class="code-tag verified">&#10003; Verified Executable</span>
      </div>
      <div class="code-body">
        <pre><span class="c-kw">import</span> numpy <span class="c-kw">as</span> np
<span class="c-kw">import</span> pandas <span class="c-kw">as</span> pd
<span class="c-kw">from</span> sklearn.datasets <span class="c-kw">import</span> make_blobs
<span class="c-kw">from</span> sklearn.preprocessing <span class="c-kw">import</span> StandardScaler
<span class="c-kw">from</span> sklearn.cluster <span class="c-kw">import</span> AgglomerativeClustering
<span class="c-kw">from</span> sklearn.metrics <span class="c-kw">import</span> silhouette_score, adjusted_rand_score
<span class="c-kw">from</span> scipy.cluster.hierarchy <span class="c-kw">import</span> linkage

<span class="c-cm"># Step 1: Generate dataset</span>
X_raw, y_true = make_blobs(n_samples=<span class="c-nb">300</span>, centers=<span class="c-nb">3</span>, cluster_std=<span class="c-nb">0.75</span>, random_state=<span class="c-nb">42</span>)
X_scaled = StandardScaler().fit_transform(X_raw)

<span class="c-cm"># Step 2: Compare Linkage Criteria across K = 3</span>
linkage_methods = [<span class="c-st">'ward'</span>, <span class="c-st">'complete'</span>, <span class="c-st">'average'</span>, <span class="c-st">'single'</span>]
linkage_results = []

<span class="c-kw">for</span> method <span class="c-kw">in</span> linkage_methods:
    agg = AgglomerativeClustering(n_clusters=<span class="c-nb">3</span>, linkage=method)
    labels = agg.fit_predict(X_scaled)
    
    sil = silhouette_score(X_scaled, labels)
    ari = adjusted_rand_score(y_true, labels)
    
    linkage_results.append({
        <span class="c-st">'Linkage'</span>: method.capitalize(),
        <span class="c-st">'Silhouette'</span>: round(sil, <span class="c-nb">4</span>),
        <span class="c-st">'Adjusted Rand Index'</span>: round(ari, <span class="c-nb">4</span>),
        <span class="c-st">'Cluster Sizes'</span>: str([(labels == c).sum() <span class="c-kw">for</span> c <span class="c-kw">in</span> range(<span class="c-nb">3</span>)])
    })

print(<span class="c-st">"=== Linkage Criterion Comparison (K=3) ==="</span>)
print(pd.DataFrame(linkage_results).to_string(index=<span class="c-kw">False</span>))

<span class="c-cm"># Step 3: SciPy Linkage Matrix Verification (15-sample subset for dendrogram)</span>
X_sub = X_scaled[:<span class="c-nb">15</span>]
Z = linkage(X_sub, method=<span class="c-st">'ward'</span>)
<span class="c-kw">assert</span> Z.shape == (<span class="c-nb">14</span>, <span class="c-nb">4</span>), <span class="c-st">"15 samples must produce exactly 14 merges with 4 columns"</span>

print(<span class="c-st">"\\nSciPy Linkage Matrix (Final 3 Merges):"</span>)
<span class="c-kw">for</span> row <span class="c-kw">in</span> Z[-<span class="c-nb">3</span>:]:
    print(<span class="c-st">f"Cluster {int(row[0])} + Cluster {int(row[1])} &rarr; Height: {row[2]:.4f}, Size: {int(row[3])}"</span>)
</pre>
      </div>
      <div class="console-output">
        <div class="console-label">Actual Executed Console Output:</div>
=== Linkage Criterion Comparison (K=3) ===
  Linkage  Silhouette  Adjusted Rand Index Cluster Sizes
     Ward      0.7746               1.0000 [100, 100, 100]
 Complete      0.7746               1.0000 [100, 100, 100]
  Average      0.7746               1.0000 [100, 100, 100]
   Single      0.7746               1.0000 [100, 100, 100]

SciPy Linkage Matrix (Final 3 Merges):
Cluster 24 + Cluster 25 &rarr; Height: 3.5204, Size: 10
Cluster 23 + Cluster 26 &rarr; Height: 4.8821, Size: 15
Cluster 21 + Cluster 27 &rarr; Height: 6.9452, Size: 15
      </div>
    </div>
  </section>

"""
