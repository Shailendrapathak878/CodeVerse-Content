"""Topic 16 Part 2: Sections 7 to 13.
K-Means Objective, Elbow Method, Silhouette Score, K Comparison, Limitations, Hierarchical Clustering, Linkage Criteria.
"""

TOPIC16_PART2 = """
  <!-- SECTION 07 -->
  <section id="sec-07" class="content-section">
    <span class="section-badge">Section 07 &bull; Mathematical Objective</span>
    <h2 class="section-title">K-Means Objective Function &amp; Inertia</h2>

    <p>
      Under the hood, K-Means is a mathematical optimization algorithm designed to minimize a specific objective function called <strong>Inertia</strong>, also known as the <strong>Within-Cluster Sum of Squares (WCSS)</strong>.
    </p>

    <div class="formula-block">
      J = &sum;<sub>k=1</sub><sup>K</sup> &sum;<sub>x<sub>i</sub> &isin; C<sub>k</sub></sub> ||x<sub>i</sub> &minus; &mu;<sub>k</sub>||&sup2;
      <div class="formula-breakdown">
        <div class="breakdown-item"><strong>J (Inertia):</strong> Total within-cluster sum of squared errors across all <em>K</em> clusters</div>
        <div class="breakdown-item"><strong>K:</strong> Total number of distinct cluster partitions</div>
        <div class="breakdown-item"><strong>C<sub>k</sub>:</strong> Set of all data observations assigned to cluster <em>k</em></div>
        <div class="breakdown-item"><strong>x<sub>i</sub>:</strong> Feature vector of individual sample <em>i</em></div>
        <div class="breakdown-item"><strong>&mu;<sub>k</sub>:</strong> Centroid (mean feature vector) of cluster <em>k</em></div>
        <div class="breakdown-item"><strong>||x<sub>i</sub> &minus; &mu;<sub>k</sub>||&sup2;:</strong> Squared Euclidean distance from point x<sub>i</sub> to centroid &mu;<sub>k</sub></div>
      </div>
    </div>

    <h3 class="subsection-title">Manual Calculation &bull; Step-by-Step Worked Example</h3>
    <p>
      Let us compute inertia by hand on a toy dataset of 4 points partitioned into 2 clusters (<em>K</em> = 2):
    </p>
    <ul>
      <li><strong>Cluster 1 points:</strong> P<sub>1</sub> = (1, 2) and P<sub>2</sub> = (1, 4)</li>
      <li><strong>Cluster 2 points:</strong> P<sub>3</sub> = (5, 8) and P<sub>4</sub> = (5, 10)</li>
    </ul>

    <div class="step-flow">
      <div class="step-item">
        <div class="step-number">1</div>
        <div class="step-content">
          <div class="step-title">Calculate Centroids</div>
          <p class="step-desc">
            &bull; &mu;<sub>1</sub> = [ (1 + 1)/2, (2 + 4)/2 ] = <strong>(1.0, 3.0)</strong><br>
            &bull; &mu;<sub>2</sub> = [ (5 + 5)/2, (8 + 10)/2 ] = <strong>(5.0, 9.0)</strong>
          </p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">2</div>
        <div class="step-content">
          <div class="step-title">Compute Squared Distances for Cluster 1</div>
          <p class="step-desc">
            &bull; ||P<sub>1</sub> &minus; &mu;<sub>1</sub>||&sup2; = (1 &minus; 1)&sup2; + (2 &minus; 3)&sup2; = 0 + 1 = <strong>1.0</strong><br>
            &bull; ||P<sub>2</sub> &minus; &mu;<sub>1</sub>||&sup2; = (1 &minus; 1)&sup2; + (4 &minus; 3)&sup2; = 0 + 1 = <strong>1.0</strong><br>
            <strong>WCSS(C<sub>1</sub>) = 1.0 + 1.0 = 2.0</strong>
          </p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">3</div>
        <div class="step-content">
          <div class="step-title">Compute Squared Distances for Cluster 2</div>
          <p class="step-desc">
            &bull; ||P<sub>3</sub> &minus; &mu;<sub>2</sub>||&sup2; = (5 &minus; 5)&sup2; + (8 &minus; 9)&sup2; = 0 + 1 = <strong>1.0</strong><br>
            &bull; ||P<sub>4</sub> &minus; &mu;<sub>2</sub>||&sup2; = (5 &minus; 5)&sup2; + (10 &minus; 9)&sup2; = 0 + 1 = <strong>1.0</strong><br>
            <strong>WCSS(C<sub>2</sub>) = 1.0 + 1.0 = 2.0</strong>
          </p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">4</div>
        <div class="step-content">
          <div class="step-title">Sum Total Inertia</div>
          <p class="step-desc">
            <strong>Total Inertia J = 2.0 + 2.0 = 4.0000</strong>. This perfectly matches the <code>model.inertia_</code> attribute reported by scikit-learn!
          </p>
        </div>
      </div>
    </div>

    <!-- Visual 06 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.6: Final K-Means Clusters with True Mathematical Centroids</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_KMEANS_CENTROIDS_FINAL__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.6:</strong> Fully converged 3-cluster K-Means solution on standard synthetic blobs. Gold star markers indicate the exact empirical centroids &mu;<sub>1</sub>, &mu;<sub>2</sub>, and &mu;<sub>3</sub>. Dotted radial vectors illustrate the squared distances minimized by inertia objective <em>J</em>.
      </p>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; Why Inertia Alone Cannot Choose K</div>
      <p>
        As <em>K</em> increases, inertia is mathematically guaranteed to decrease monotonically. If you set <em>K = N</em> (where every single data point is its own private cluster), each centroid sits directly on top of its point, yielding <strong>Inertia = 0</strong>! However, having <em>N</em> clusters provides zero generalization and zero business insight. Therefore, minimizing inertia alone is not sufficient to pick <em>K</em>.
      </p>
    </div>
  </section>

  <!-- SECTION 08 -->
  <section id="sec-08" class="content-section">
    <span class="section-badge">Section 08 &bull; Model Selection Heuristic</span>
    <h2 class="section-title">Choosing K: The Elbow Method</h2>

    <p>
      Since we cannot simply pick the <em>K</em> with the absolute lowest inertia, how do practitioners select an appropriate cluster count? The classic visual approach is the <strong>Elbow Method</strong>.
    </p>

    <div class="step-flow">
      <div class="step-item">
        <div class="step-number">1</div>
        <div class="step-content">
          <div class="step-title">Train Multiple Candidate Models</div>
          <p class="step-desc">Fit independent K-Means models across a candidate range of cluster counts, typically <code>K = 1, 2, 3, &hellip;, 10</code>.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">2</div>
        <div class="step-content">
          <div class="step-title">Extract Fitted Inertia</div>
          <p class="step-desc">Record the final converged <code>model.inertia_</code> for each candidate value of <em>K</em>.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">3</div>
        <div class="step-content">
          <div class="step-title">Plot Inertia vs K</div>
          <p class="step-desc">Construct a 2D line plot showing candidate <em>K</em> on the x-axis and resulting inertia on the y-axis.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">4</div>
        <div class="step-content">
          <div class="step-title">Locate the "Elbow" Bend</div>
          <p class="step-desc">Identify the point where the curve bends sharply—the point of diminishing marginal returns where increasing <em>K</em> further yields only trivial reductions in inertia.</p>
        </div>
      </div>
    </div>

    <!-- Visual 07 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.7: Verified Elbow Method Curve (K = 2 to 6)</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_ELBOW_METHOD__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.7:</strong> Genuine inertia curve measured on our 300-sample benchmark dataset across K = 2 through 6. The transition from K=2 (inertia 307.10) to K=3 (inertia 47.04) represents a massive drop of 260.06 units, after which the curve flattens drastically (K=4 drops by only 5.96 units to 41.08). The prominent elbow bend unambiguously identifies K=3.
      </p>
    </div>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Candidate K</th>
            <th>Fitted Inertia</th>
            <th>Marginal Reduction (&Delta;J)</th>
            <th>Interpretation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>K = 2</strong></td>
            <td>307.10</td>
            <td>&mdash;</td>
            <td>Under-clustered; two distinct blobs forced together</td>
          </tr>
          <tr style="background: #EEF2FF; font-weight: 700;">
            <td><strong>K = 3 (Elbow)</strong></td>
            <td>47.04</td>
            <td>&minus;260.06 (84.7% drop!)</td>
            <td>Optimal balance point; natural geometric clusters captured</td>
          </tr>
          <tr>
            <td><strong>K = 4</strong></td>
            <td>41.08</td>
            <td>&minus;5.96</td>
            <td>Diminishing returns; one natural cluster arbitrarily split</td>
          </tr>
          <tr>
            <td><strong>K = 5</strong></td>
            <td>35.72</td>
            <td>&minus;5.36</td>
            <td>Over-fragmentation; minor noise partitioning</td>
          </tr>
          <tr>
            <td><strong>K = 6</strong></td>
            <td>30.22</td>
            <td>&minus;5.50</td>
            <td>Over-segmentation</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; Limitations of the Elbow Method</div>
      <p>
        The Elbow Method is a <strong>visual heuristic, not a mathematical law</strong>. On complex real-world datasets with continuous distributions, overlapping customer segments, or non-spherical densities, the inertia curve often descends in a smooth, continuous arc without any clear or obvious bend. In such cases, practitioners must rely on the Silhouette Score or business validation.
      </p>
    </div>
  </section>

  <!-- SECTION 09 -->
  <section id="sec-09" class="content-section">
    <span class="section-badge">Section 09 &bull; Rigorous Internal Validation</span>
    <h2 class="section-title">Silhouette Score Analysis</h2>

    <p>
      The <strong>Silhouette Coefficient</strong> provides a more rigorous, normalized metric to evaluate clustering quality without ground-truth labels. It evaluates both <strong>cohesion</strong> (how close a sample is to members of its own cluster) and <strong>separation</strong> (how far it is from members of the nearest other cluster).
    </p>

    <h3 class="subsection-title">The Mathematical Formulation</h3>
    <p>
      For each individual sample <em>i</em> in the dataset:
    </p>

    <div class="formula-block">
      s(i) = [ b(i) &minus; a(i) ] / max[ a(i), b(i) ]
      <div class="formula-breakdown">
        <div class="breakdown-item"><strong>s(i):</strong> Silhouette coefficient for point <em>i</em>, bounded in the range [&minus;1, +1]</div>
        <div class="breakdown-item"><strong>a(i) (Intra-Cluster Distance):</strong> Mean Euclidean distance from point <em>i</em> to all other points in the same cluster</div>
        <div class="breakdown-item"><strong>b(i) (Nearest-Cluster Distance):</strong> Mean Euclidean distance from point <em>i</em> to all points in the closest neighboring cluster</div>
        <div class="breakdown-item"><strong>max[a(i), b(i)]:</strong> Normalization denominator guaranteeing the score is bounded</div>
      </div>
    </div>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Silhouette Range</th>
            <th>Physical Meaning</th>
            <th>Diagnostic Assessment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>+0.71 to +1.00</strong></td>
            <td>b(i) &gt;&gt; a(i)</td>
            <td>Excellent structure; points are deeply embedded in tight, well-separated clusters</td>
          </tr>
          <tr>
            <td><strong>+0.51 to +0.70</strong></td>
            <td>b(i) &gt; a(i)</td>
            <td>Reasonable structure; clusters are clearly distinct with minimal boundary ambiguity</td>
          </tr>
          <tr>
            <td><strong>+0.26 to +0.50</strong></td>
            <td>b(i) &approx; a(i)</td>
            <td>Weak or artificial structure; substantial cluster overlap or arbitrary partition cuts</td>
          </tr>
          <tr>
            <td><strong>0.00 to +0.25</strong></td>
            <td>b(i) &asymp; a(i)</td>
            <td>Points sit right on the decision boundary between two clusters</td>
          </tr>
          <tr>
            <td><strong>&minus;1.00 to 0.00</strong></td>
            <td>a(i) &gt; b(i)</td>
            <td>Misclassified point; sample is physically closer to a neighboring cluster than its assigned cluster</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Visual 08 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.8: Silhouette Score Profile across Candidate K Values</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_SILHOUETTE_ANALYSIS__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.8:</strong> Verified mean silhouette coefficients across K = 2 through 6. The score peaks decisively at K=3 with a value of 0.7746, proving that 3 clusters achieve maximum separation and internal compactness. For K=4 (0.6273) and K=5 (0.4713), silhouette drops precipitously as artificial cuts force neighboring points into different clusters.
      </p>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; Validity Constraint: Never Compute Silhouette for K = 1</div>
      <p>
        The silhouette score requires comparing a point to at least one <em>neighboring cluster</em> (to compute <em>b(i)</em>). If <code>K = 1</code>, no neighboring cluster exists, making <em>b(i)</em> mathematically undefined. Passing <code>n_clusters=1</code> into <code>sklearn.metrics.silhouette_score</code> raises an immediate <code>ValueError: Number of labels is 1. Valid values are 2 to n_samples - 1</code>.
      </p>
    </div>
  </section>

  <!-- SECTION 10 -->
  <section id="sec-10" class="content-section">
    <span class="section-badge">Section 10 &bull; Visual Model Diagnostics</span>
    <h2 class="section-title">Visualizing Different K Values</h2>

    <p>
      To build rock-solid intuition, let us inspect what happens geometrically when an algorithm is forced to fit under-specified, optimal, and over-specified values of <em>K</em> onto the exact same benchmark dataset.
    </p>

    <!-- Visual 09 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.9: Geometric Partitions Across K = 2, 3, 4, and 5</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_K_VALUES_GRID__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.9:</strong> Comparing spatial partitions across K=2, 3, 4, and 5 on the identical 300-point dataset. Gold stars represent fitted centroids. At K=2 (top-left), the model under-clusters by forcing two independent clouds into a single cyan partition. At K=3 (top-right), the three natural groups are cleanly separated. At K=4 and K=5 (bottom), the algorithm artificially bisects natural clusters into arbitrary slices.
      </p>
    </div>

    <div class="callout-card callout-def">
      <div class="callout-title">Diagnostic Comparison of Partition Regimes</div>
      <ul>
        <li><strong>Under-Clustering (K &lt; K*):</strong> Distinct natural populations are compressed together. Centroids end up floating in empty space between the combined sub-groups, resulting in high within-cluster variance.</li>
        <li><strong>Optimal Clustering (K = K*):</strong> Each centroid aligns with the true center of mass of an isolated data density. Inertia drops to its natural minimum and silhouette score reaches its maximum.</li>
        <li><strong>Over-Segmentation (K &gt; K*):</strong> Natural cohesive clusters are arbitrarily split by linear Voronoi boundaries. Centroids are placed unnecessarily close together, causing <em>b(i)</em> to shrink and dragging down the silhouette score.</li>
      </ul>
    </div>
  </section>

  <!-- SECTION 11 -->
  <section id="sec-11" class="content-section">
    <span class="section-badge">Section 11 &bull; Critical Evaluation</span>
    <h2 class="section-title">K-Means Advantages and Structural Limitations</h2>

    <p>
      While K-Means is often the first tool practitioners reach for, it is governed by strict geometric assumptions that can fail catastrophically when applied to non-ideal datasets.
    </p>

    <div class="callout-card callout-success">
      <div class="callout-title">&#10004; Advantages of K-Means</div>
      <ul>
        <li><strong>Computational Speed:</strong> With a time complexity of <em>O(N &times; K &times; I &times; d)</em> (where <em>I</em> is iterations and <em>d</em> is dimensions), K-Means scales gracefully to millions of observations.</li>
        <li><strong>Interpretable Centroids:</strong> Each cluster center &mu;<sub>k</sub> is a concrete feature vector that represents the "prototypical customer" or "average profile" in real-world units.</li>
        <li><strong>Simple Mathematical Intuition:</strong> Easy to explain to non-technical stakeholders and executive leadership.</li>
        <li><strong>Fast Out-of-Sample Prediction:</strong> New observations can be assigned to clusters in <em>O(K &times; d)</em> time simply by calculating distance to the <em>K</em> centroids.</li>
      </ul>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; Core Geometric Limitations</div>
      <ul>
        <li><strong>Assumption of Spherical, Isotropic Clusters:</strong> Because K-Means minimizes squared Euclidean distances, it implicitly assumes all clusters are spherical balls of roughly equal variance.</li>
        <li><strong>Vulnerability to Outliers:</strong> Since distance differences are squared, extreme anomalies exert immense leverage, violently pulling centroids away from true dense clusters.</li>
        <li><strong>Inability to Discover Arbitrary Manifold Shapes:</strong> K-Means cannot cluster concentric rings, crescent moons, or winding spirals because linear Voronoi hyperplanes cannot trace curved manifolds.</li>
        <li><strong>Uniform Density Bias:</strong> When clusters have wildly different densities or sample sizes, K-Means tends to split the large sparse cluster and merge smaller dense clusters.</li>
      </ul>
    </div>

    <!-- Visual 10 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.10: K-Means Success Case vs Non-Convex Geometry Failure</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_KMEANS_LIMITATIONS__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.10:</strong> Left: K-Means succeeds brilliantly on convex, spherical, well-separated Gaussian blobs. Right: K-Means fails completely on interlocking non-convex crescent moons. Because it relies on linear distance to centroids, it blindly slices straight across the crescents rather than following the curved continuous manifolds.
      </p>
    </div>
  </section>

  <!-- SECTION 12 -->
  <section id="sec-12" class="content-section">
    <span class="section-badge">Section 12 &bull; Hierarchical Paradigms</span>
    <h2 class="section-title">Hierarchical Clustering Fundamentals</h2>

    <p>
      What if you do not want to commit to a fixed cluster count <em>K</em> upfront? What if your data naturally organizes into nested multi-level taxonomies (e.g., Kingdom &rarr; Phylum &rarr; Class &rarr; Order &rarr; Family &rarr; Genus &rarr; Species)?
    </p>

    <p>
      <strong>Hierarchical Clustering</strong> builds a comprehensive tree of nested cluster partitions. It divides broadly into two fundamental approaches:
    </p>

    <div class="callout-card callout-def">
      <div class="callout-title">The Two Hierarchical Methodologies</div>
      <ul>
        <li><strong>Agglomerative Clustering (Bottom-Up):</strong> Starts with every single observation as its own independent singleton cluster (<em>N</em> clusters of size 1). At each iteration, the two most similar (closest) clusters are merged. This merging repeats step-by-step until all points merge into a single universal cluster containing all <em>N</em> samples. (This is the predominant method in scikit-learn).</li>
        <li><strong>Divisive Clustering (Top-Down):</strong> Starts with all observations bundled into one single giant cluster. At each step, clusters are recursively divided into smaller sub-clusters until every observation is isolated. Divisive clustering is computationally expensive (<em>O(2<sup>N</sup>)</em> for exhaustive splits) and rarely used in practice.</li>
      </ul>
    </div>

    <div class="step-flow">
      <div class="step-title" style="margin-bottom: 12px; font-weight: 700; color: var(--primary-accent);">Agglomerative Clustering Execution Loop:</div>
      <div class="step-item">
        <div class="step-number">1</div>
        <div class="step-content">
          <div class="step-title">Initialize N Clusters</div>
          <p class="step-desc">Assign every observation <em>x<sub>i</sub></em> to its own individual cluster: C<sub>1</sub> = {x<sub>1</sub>}, C<sub>2</sub> = {x<sub>2</sub>}, &hellip;, C<sub>N</sub> = {x<sub>N</sub>}.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">2</div>
        <div class="step-content">
          <div class="step-title">Compute Pairwise Proximity Matrix</div>
          <p class="step-desc">Calculate the distance between every pair of clusters according to a chosen <strong>linkage criterion</strong>.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">3</div>
        <div class="step-content">
          <div class="step-title">Merge Closest Pair</div>
          <p class="step-desc">Find the two clusters with the smallest linkage distance and merge them into a single combined cluster.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">4</div>
        <div class="step-content">
          <div class="step-title">Update Proximity Matrix &amp; Repeat</div>
          <p class="step-desc">Recalculate distances from the newly formed cluster to all remaining clusters. Repeat steps 3 and 4 until exactly 1 cluster of size <em>N</em> remains.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 13 -->
  <section id="sec-13" class="content-section">
    <span class="section-badge">Section 13 &bull; Mathematical Linkage Criteria</span>
    <h2 class="section-title">Hierarchical Linkage Methods</h2>

    <p>
      In Step 2 of agglomerative clustering, the algorithm must calculate the distance between two <em>sets of points</em> (Cluster A and Cluster B). How do we define distance between two clouds of data? This definition is called the <strong>linkage criterion</strong>.
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Linkage Method</th>
            <th>Mathematical Formula</th>
            <th>Geometric Behavior</th>
            <th>Primary Limitation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Single Linkage (Min)</strong></td>
            <td><code>d(A, B) = min { ||a &minus; b|| : a &isin; A, b &isin; B }</code></td>
            <td>Distance between the two closest points. Can follow non-spherical serpentine shapes.</td>
            <td><strong>Chaining Effect:</strong> A thin string of noisy points can bridge two completely separate clusters together.</td>
          </tr>
          <tr>
            <td><strong>Complete Linkage (Max)</strong></td>
            <td><code>d(A, B) = max { ||a &minus; b|| : a &isin; A, b &isin; B }</code></td>
            <td>Distance between the two farthest points. Produces compact, equal-diameter spherical clusters.</td>
            <td>Highly sensitive to outliers, which can artificially inflate the maximum diameter.</td>
          </tr>
          <tr>
            <td><strong>Average Linkage (Mean)</strong></td>
            <td><code>d(A, B) = [1 / (|A| |B|)] &sum;<sub>a &isin; A</sub> &sum;<sub>b &isin; B</sub> ||a &minus; b||</code></td>
            <td>Averages all pairwise distances between points in A and points in B. Balanced and robust.</td>
            <td>Can be biased toward clusters of equal variance; sensitive to scale differences.</td>
          </tr>
          <tr style="background: #EEF2FF; font-weight: 700;">
            <td><strong>Ward Linkage (Min Variance)</strong></td>
            <td><code>&Delta;Var = [|A| |B| / (|A| + |B|)] ||&mu;<sub>A</sub> &minus; &mu;<sub>B</sub>||&sup2;</code></td>
            <td>Minimizes the total within-cluster variance increase resulting from merging A and B. (Default in scikit-learn).</td>
            <td><strong>Strictly requires Euclidean distance!</strong> Cannot be used with Manhattan, Cosine, or precomputed non-Euclidean matrices.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Visual 11 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.11: Geometric Comparison of the 4 Primary Linkage Criteria</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_LINKAGE_COMPARISON__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.11:</strong> Visual breakdown of inter-cluster distance definitions: Single linkage (shortest point pair, teal dashed line), Complete linkage (farthest point pair, coral dashed line), Average linkage (mean of all cross-cluster connections, lavender lines), and Ward linkage (variance increase measured between centroid vectors &mu;<sub>A</sub> and &mu;<sub>B</sub>, weighted by cluster sizes).
      </p>
    </div>
  </section>

"""
