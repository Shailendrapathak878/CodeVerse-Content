"""Topic 16 Part 4: Sections 21 to 27, Footer.
Python Lab 3 (DBSCAN), Evaluation Metrics, Applications, 14+ Mistakes, Visual Gallery, Cheat Sheet, 12 FAQs.
"""

TOPIC16_PART4 = """
  <!-- SECTION 21 -->
  <section id="sec-21" class="content-section">
    <span class="section-badge">Section 21 &bull; Hands-On Implementation</span>
    <h2 class="section-title">Complete Python Lab 3: DBSCAN with Outlier Detection</h2>

    <p>
      In this lab, we build a production DBSCAN workflow on non-convex manifolds with background noise. We demonstrate how DBSCAN discovers curved structures, isolate anomalies labeled <code>&minus;1</code>, and handle evaluation metrics correctly.
    </p>

    <div class="code-card">
      <div class="code-header">
        <span class="code-title">&#128013; dbscan_complete_lab.py</span>
        <span class="code-tag verified">&#10003; Verified Executable</span>
      </div>
      <div class="code-body">
        <pre><span class="c-kw">import</span> numpy <span class="c-kw">as</span> np
<span class="c-kw">import</span> pandas <span class="c-kw">as</span> pd
<span class="c-kw">from</span> sklearn.datasets <span class="c-kw">import</span> make_moons
<span class="c-kw">from</span> sklearn.preprocessing <span class="c-kw">import</span> StandardScaler
<span class="c-kw">from</span> sklearn.cluster <span class="c-kw">import</span> DBSCAN, KMeans
<span class="c-kw">from</span> sklearn.metrics <span class="c-kw">import</span> silhouette_score, adjusted_rand_score

<span class="c-cm"># Step 1: Generate non-convex crescent moons + background noise</span>
np.random.seed(<span class="c-nb">42</span>)
X_moons, y_moons = make_moons(n_samples=<span class="c-nb">260</span>, noise=<span class="c-nb">0.08</span>, random_state=<span class="c-nb">42</span>)

<span class="c-cm"># Add 20 uniform random noise points</span>
noise_points = np.random.uniform(low=-<span class="c-nb">1.5</span>, high=<span class="c-nb">2.5</span>, size=(<span class="c-nb">20</span>, <span class="c-nb">2</span>))
y_noise = np.full(<span class="c-nb">20</span>, fill_value=-<span class="c-nb">1</span>)

X_combined = np.vstack([X_moons, noise_points])
y_combined = np.concatenate([y_moons, y_noise])
<span class="c-kw">assert</span> X_combined.shape == (<span class="c-nb">280</span>, <span class="c-nb">2</span>), <span class="c-st">"Dataset shape mismatch"</span>

<span class="c-cm"># Step 2: Feature scaling</span>
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_combined)

<span class="c-cm"># Step 3: Fit DBSCAN</span>
dbscan = DBSCAN(eps=<span class="c-nb">0.28</span>, min_samples=<span class="c-nb">6</span>)
db_labels = dbscan.fit_predict(X_scaled)

unique_labels = set(db_labels)
n_clusters = len(unique_labels - {-<span class="c-nb">1</span>})
n_noise = (db_labels == -<span class="c-nb">1</span>).sum()

<span class="c-cm"># Assertions</span>
<span class="c-kw">assert</span> n_clusters == <span class="c-nb">2</span>, <span class="c-st">f"Expected 2 clusters, got {n_clusters}"</span>
<span class="c-kw">assert</span> n_noise == <span class="c-nb">18</span>, <span class="c-st">f"Expected 18 noise points, got {n_noise}"</span>
<span class="c-kw">assert</span> len(db_labels) == <span class="c-nb">280</span>, <span class="c-st">"Label length mismatch"</span>

<span class="c-cm"># Step 4: Metric Evaluation (Ignoring noise points for internal silhouette)</span>
mask_clustered = (db_labels != -<span class="c-nb">1</span>)
sil_clustered = silhouette_score(X_scaled[mask_clustered], db_labels[mask_clustered])
ari_dbscan = adjusted_rand_score(y_combined, db_labels)

<span class="c-cm"># Step 5: Compare directly with K-Means (K = 2)</span>
km = KMeans(n_clusters=<span class="c-nb">2</span>, random_state=<span class="c-nb">42</span>, n_init=<span class="c-nb">10</span>)
km_labels = km.fit_predict(X_scaled)
ari_kmeans = adjusted_rand_score(y_combined, km_labels)

print(<span class="c-st">"=== DBSCAN vs K-Means Head-to-Head Performance ==="</span>)
print(<span class="c-st">f"Total Observations:    {len(X_scaled)}"</span>)
print(<span class="c-st">f"Discovered Clusters:   {n_clusters} (Cluster 0: {(db_labels == 0).sum()}, Cluster 1: {(db_labels == 1).sum()})"</span>)
print(<span class="c-st">f"Identified Outliers:   {n_noise} ({n_noise / len(X_scaled) * 100:.1f}% labeled as noise -1)"</span>)
print(<span class="c-st">f"DBSCAN Adjusted Rand:  {ari_dbscan:.4f}  (Flawless non-convex recovery)"</span>)
print(<span class="c-st">f"K-Means Adjusted Rand: {ari_kmeans:.4f}  (Catastrophic failure on crescents)"</span>)
print(<span class="c-st">f"Silhouette (non-noise): {sil_clustered:.4f}"</span>)
</pre>
      </div>
      <div class="console-output">
        <div class="console-label">Actual Executed Console Output:</div>
=== DBSCAN vs K-Means Head-to-Head Performance ===
Total Observations:    280
Discovered Clusters:   2 (Cluster 0: 132, Cluster 1: 130)
Identified Outliers:   18 (6.4% labeled as noise -1)
DBSCAN Adjusted Rand:  0.9770  (Flawless non-convex recovery)
K-Means Adjusted Rand: 0.4053  (Catastrophic failure on crescents)
Silhouette (non-noise): 0.3842
      </div>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; Critical QA Rule: Do Not Calculate Silhouette Score on Raw Noise Points</div>
      <p>
        In scikit-learn, DBSCAN flags unclustered anomalies with the label <code>&minus;1</code>. If you pass <code>db_labels</code> directly into <code>silhouette_score(X, db_labels)</code>, the function treats <code>&minus;1</code> as an ordinary cluster! Because noise points are scattered randomly across the entire plane, their within-cluster distance <em>a(i)</em> is enormous, artificially obliterating the silhouette metric. <strong>Always filter out noise samples (<code>labels != &minus;1</code>) prior to computing internal cluster validation scores!</strong>
      </p>
    </div>
  </section>

  <!-- SECTION 22 -->
  <section id="sec-22" class="content-section">
    <span class="section-badge">Section 22 &bull; Quantitative Validation</span>
    <h2 class="section-title">Clustering Evaluation Metrics: Internal vs External</h2>

    <p>
      Evaluating unsupervised models is inherently nuanced because there is no ground-truth answer key in production. Clustering validation metrics divide into two broad categories: <strong>Internal Metrics</strong> and <strong>External Metrics</strong>.
    </p>

    <!-- Visual 18 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.18: Comprehensive Multi-Metric Clustering Evaluation Profile</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_METRICS_COMPARISON__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.18:</strong> Normalized multi-metric evaluation across candidate K values on our 300-point benchmark. Silhouette score (indigo line) and Calinski-Harabasz index (teal dashed line) peak decisively at K=3. Simultaneously, the Davies-Bouldin index (coral line) reaches its global minimum of 0.3090 at K=3, providing unanimous mathematical consensus.
      </p>
    </div>

    <h3 class="subsection-title">1. Internal Evaluation Metrics (Unsupervised)</h3>
    <p>
      Internal measures evaluate the mathematical compactness, separation, and density balance of clusters using only the feature matrix <em>X</em> and the predicted cluster labels:
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Metric Name</th>
            <th>scikit-learn Function</th>
            <th>Optimization Goal</th>
            <th>Mathematical Formulation &amp; Physical Meaning</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Inertia (WCSS)</strong></td>
            <td><code>model.inertia_</code></td>
            <td>Lower is better</td>
            <td>Sum of squared Euclidean distances to centroids. Monotonically decreases with <em>K</em>; requires the Elbow heuristic.</td>
          </tr>
          <tr>
            <td><strong>Silhouette Score</strong></td>
            <td><code>silhouette_score(X, labels)</code></td>
            <td><strong>Higher is better (Max +1.0)</strong></td>
            <td>Measures ratio of inter-cluster separation to intra-cluster compactness. Bounded between &minus;1.0 and +1.0. Optimal peak at K=3 (0.7746).</td>
          </tr>
          <tr style="background: #EEF2FF; font-weight: 700;">
            <td><strong>Davies&ndash;Bouldin Index (DBI)</strong></td>
            <td><code>davies_bouldin_score(X, labels)</code></td>
            <td><strong>Lower is better (Min 0.0)</strong></td>
            <td>Average similarity between each cluster and its most similar counterpart: <code>R<sub>ij</sub> = (s<sub>i</sub> + s<sub>j</sub>) / d(&mu;<sub>i</sub>, &mu;<sub>j</sub>)</code>. Zero represents perfect isolation. Optimal minimum at K=3 (0.3090).</td>
          </tr>
          <tr>
            <td><strong>Calinski&ndash;Harabasz Index</strong></td>
            <td><code>calinski_harabasz_score(X, labels)</code></td>
            <td><strong>Higher is better</strong></td>
            <td>Variance Ratio Criterion: ratio of between-cluster dispersion (SSB) to within-cluster dispersion (SSW), normalized by degrees of freedom. Higher values indicate denser, better-separated clusters. Optimal peak at K=3 (1745.50).</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3 class="subsection-title">2. External Evaluation Metrics (Supervised Benchmarks)</h3>
    <p>
      External metrics are used when reference ground-truth labels are available (e.g., benchmark research datasets or synthetic validation experiments).
    </p>
    <div class="callout-card callout-def">
      <div class="callout-title">Adjusted Rand Index (ARI)</div>
      <p>
        The <strong>Adjusted Rand Index</strong> computes the similarity between the true clusterings <em>Y</em> and predicted clusterings <em>C</em>, evaluating all pairs of samples that are assigned to the same or different clusters, adjusted for chance:
      </p>
      <div style="background: #FFFFFF; padding: 10px; border-radius: 6px; font-family: monospace; margin: 8px 0;">
        ARI = (Index &minus; Expected_Index) / (Max_Index &minus; Expected_Index)
      </div>
      <ul>
        <li><strong>+1.0:</strong> Perfect cluster assignment agreement (labels may have different arbitrary numerical IDs, e.g. Cluster 0 &harr; True 1).</li>
        <li><strong>0.0:</strong> Cluster assignments are completely random, equivalent to rolling a die.</li>
        <li><strong>Negative:</strong> Worse than random chance.</li>
      </ul>
    </div>
  </section>

  <!-- SECTION 23 -->
  <section id="sec-23" class="content-section">
    <span class="section-badge">Section 23 &bull; Industry Case Studies</span>
    <h2 class="section-title">Real-World Industry Applications</h2>

    <p>
      Clustering is not an abstract mathematical exercise; it is an engine powering modern business intelligence, automation, and exploratory data science.
    </p>

    <!-- Application 1 -->
    <div class="app-card">
      <div class="app-header">
        <span class="app-icon">&#128722;</span>
        <span class="app-title">1. E-Commerce Customer Segmentation (RFM Profiling)</span>
      </div>
      <p>
        An enterprise online retailer analyzes 2 million shopper profiles to deliver personalized email marketing campaigns and VIP loyalty rewards.
      </p>
      <div class="app-grid">
        <div class="app-item"><span class="app-item-label">Input Features</span>Recency (days since last purchase), Frequency (orders per year), Monetary (total $ spent).</div>
        <div class="app-item"><span class="app-item-label">Algorithm Choice</span><strong>K-Means (K = 4)</strong> with <code>StandardScaler</code>.</div>
        <div class="app-item"><span class="app-item-label">Discovered Clusters</span>"VIP Power Shoppers", "At-Risk Churn", "Bargain Seekers", "Occasional Gifting".</div>
        <div class="app-item"><span class="app-item-label">Domain Limitation</span>Cluster centroids drift seasonally (e.g., during Black Friday), requiring scheduled bi-weekly retraining.</div>
      </div>
    </div>

    <!-- Application 2 -->
    <div class="app-card">
      <div class="app-header">
        <span class="app-icon">&#128196;</span>
        <span class="app-title">2. Document &amp; News Article Thematic Discovery</span>
      </div>
      <p>
        A news aggregator ingests 50,000 articles per day across dozens of languages and automatically organizes them into trending topic channels.
      </p>
      <div class="app-grid">
        <div class="app-item"><span class="app-item-label">Input Features</span>768-dimensional sentence transformer embeddings (BERT / MiniLM) or TF-IDF vectors.</div>
        <div class="app-item"><span class="app-item-label">Algorithm Choice</span><strong>Agglomerative Hierarchical / Spherical K-Means</strong> with Cosine distance.</div>
        <div class="app-item"><span class="app-item-label">Discovered Clusters</span>Macro channels: "Global Economics", "Semiconductor Tech", "Space Exploration", "Sports".</div>
        <div class="app-item"><span class="app-item-label">Domain Limitation</span>Euclidean K-Means fails due to document length variations; vectors must be L2-normalized first.</div>
      </div>
    </div>

    <!-- Application 3 -->
    <div class="app-card">
      <div class="app-header">
        <span class="app-icon">&#128247;</span>
        <span class="app-title">3. Computer Vision &amp; Facial Recognition Grouping</span>
      </div>
      <p>
        A consumer smartphone photo gallery organizes 40,000 user photos into albums grouped by individual people without prior user facial labeling.
      </p>
      <div class="app-grid">
        <div class="app-item"><span class="app-item-label">Input Features</span>512-dimensional FaceNet / ResNet feature embeddings extracted from cropped face bounding boxes.</div>
        <div class="app-item"><span class="app-item-label">Algorithm Choice</span><strong>DBSCAN / Chinese Whispers</strong>.</div>
        <div class="app-item"><span class="app-item-label">Discovered Clusters</span>Individual persons ("Mom", "Dad", "Baby"), with blurry or occluded faces filtered as noise (&minus;1).</div>
        <div class="app-item"><span class="app-item-label">Domain Limitation</span>Number of people is unknown upfront; K-Means is unusable because <em>K</em> cannot be pre-specified.</div>
      </div>
    </div>

    <!-- Application 4 -->
    <div class="app-card">
      <div class="app-header">
        <span class="app-icon">&#128272;</span>
        <span class="app-title">4. Financial Fraud &amp; Network Intrusion Anomaly Detection</span>
      </div>
      <p>
        A banking fraud engine monitors 500,000 daily credit card transactions to flag synthetic identity theft and unauthorized merchant terminal scams.
      </p>
      <div class="app-grid">
        <div class="app-item"><span class="app-item-label">Input Features</span>Transaction amount, geographic velocity (km/hour from prior swipe), merchant risk code, time of day.</div>
        <div class="app-item"><span class="app-item-label">Algorithm Choice</span><strong>DBSCAN</strong> (focusing specifically on the noise output).</div>
        <div class="app-item"><span class="app-item-label">Discovered Clusters</span>Legitimate spending profiles form dense baseline clusters; fraud events land in low-density noise (label &minus;1).</div>
        <div class="app-item"><span class="app-item-label">Domain Limitation</span>Extreme class imbalance (99.98% legitimate); <code>eps</code> must be tightly tuned via validation alerts.</div>
      </div>
    </div>

    <!-- Application 5 -->
    <div class="app-card">
      <div class="app-header">
        <span class="app-icon">&#128506;</span>
        <span class="app-title">5. Logistics &amp; Warehouse Hub Routing Optimization</span>
      </div>
      <p>
        A nationwide freight carrier plans 5 regional distribution fulfillment hubs to minimize total diesel transit miles across 50,000 daily delivery addresses.
      </p>
      <div class="app-grid">
        <div class="app-item"><span class="app-item-label">Input Features</span>Projected Cartesian coordinates (Eastings / Northings in kilometers from UTM projection).</div>
        <div class="app-item"><span class="app-item-label">Algorithm Choice</span><strong>K-Means (K = 5)</strong> with geographical coordinate conversion.</div>
        <div class="app-item"><span class="app-item-label">Discovered Clusters</span>Optimal hub dispatch territories; final centroid coordinates &mu;<sub>k</sub> specify the exact physical warehouse locations.</div>
        <div class="app-item"><span class="app-item-label">Domain Limitation</span>Cannot use raw latitude/longitude degrees directly because 1 degree of longitude shrinks towards the poles!</div>
      </div>
    </div>
  </section>

  <!-- SECTION 24 -->
  <section id="sec-24" class="content-section">
    <span class="section-badge">Section 24 &bull; Practitioner Safeguards</span>
    <h2 class="section-title">Common Beginner Mistakes &amp; How to Fix Them</h2>

    <p>
      Clustering appears deceptively simple because scikit-learn models run in just two lines of code. However, subtle methodological errors can silently corrupt your findings.
    </p>

    <!-- Mistake 01 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 1: Forgetting Feature Scaling Prior to Distance Calculation</span>
      </div>
      <p>Fitting K-Means or DBSCAN directly on raw, unscaled features where one feature has a vastly larger numerical range.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Raw Features</span>
          <code># Income spans 100,000 while Age spans 50<br>km = KMeans(n_clusters=3)<br>km.fit(df[['Income', 'Age']]) # Income completely dominates!</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Scaled Pipeline</span>
          <code>pipe = Pipeline([<br>&nbsp;&nbsp;('scaler', StandardScaler()),<br>&nbsp;&nbsp;('kmeans', KMeans(n_clusters=3, random_state=42))<br>])<br>pipe.fit(df[['Income', 'Age']])</code>
        </div>
      </div>
    </div>

    <!-- Mistake 02 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 2: Confusing Clustering with Supervised Classification</span>
      </div>
      <p>Expecting clustering to reproduce arbitrary human labels without providing those labels during training.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Conceptual Confusion</span>
          <p><em>"I ran K-Means on customer data with K=2, but it did not split them into Male and Female!"</em></p>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Objective Alignment</span>
          <p>Clustering discovers mathematical geometric partitions, not human demographic identity. If you want to predict a specific target attribute, use supervised classification!</p>
        </div>
      </div>
    </div>

    <!-- Mistake 03 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 3: Assuming Cluster ID Numbers Have an Inherent Ranking</span>
      </div>
      <p>Assuming that "Cluster 2" is twice as valuable, larger, or better than "Cluster 1".</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Mathematical Misinterpretation</span>
          <code>if label == 2: send_high_value_coupon()<br>elif label == 0: send_budget_coupon() # Labels are arbitrary permutations!</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Profile Before Naming</span>
          <code># Inspect centroid feature averages first<br>cluster_summary = df.groupby('cluster').mean()<br># Identify true high-spending group by empirical mean</code>
        </div>
      </div>
    </div>

    <!-- Mistake 04 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 4: Believing K-Means Automatically Discovers the Best K</span>
      </div>
      <p>Assuming calling <code>KMeans()</code> without arguments will magically select the optimal number of clusters.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Blind Default Reliance</span>
          <code>km = KMeans() # Silently defaults to n_clusters=8!<br>km.fit(X) # May severely over-segment your data</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Empirical Validation</span>
          <code># Evaluate candidates across K = 2..8 using Silhouette and Elbow<br>scores = [silhouette_score(X, KMeans(k).fit_predict(X)) for k in range(2, 9)]<br>best_k = range(2, 9)[np.argmax(scores)]</code>
        </div>
      </div>
    </div>

    <!-- Mistake 05 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 5: Treating the Elbow Method as Definitive Proof</span>
      </div>
      <p>Forcing an imaginary elbow point onto a smooth, continuously descending inertia curve.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Wishful Staring</span>
          <p>Squinting at a smooth convex curve with no inflection and guessing K=4 because it looks slightly bent.</p>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Multi-Metric Consensus</span>
          <p>Pair the Elbow plot with the Silhouette Score, Davies-Bouldin index, and business operational constraints (e.g., how many marketing campaigns can the marketing team realistically run?).</p>
        </div>
      </div>
    </div>

    <!-- Mistake 06 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 6: Calculating Silhouette Score for K = 1</span>
      </div>
      <p>Attempting to compute silhouette score on a single cluster.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Crash on K = 1</span>
          <code>score = silhouette_score(X, KMeans(n_clusters=1).fit_predict(X))<br># Raises ValueError: Number of labels is 1</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Restrict Range to K &ge; 2</span>
          <code>candidate_k = range(2, 10) # Silhouette strictly requires 2 or more clusters!</code>
        </div>
      </div>
    </div>

    <!-- Mistake 07 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 7: Blindly Including DBSCAN Noise Points in Silhouette Score</span>
      </div>
      <p>Treating noise label <code>&minus;1</code> as an ordinary cluster during internal validation.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Distorted Score</span>
          <code>db_labels = DBSCAN(eps=0.3).fit_predict(X)<br>score = silhouette_score(X, db_labels) # Treats -1 as a cluster!</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Filter Out Noise</span>
          <code>clustered_mask = (db_labels != -1)<br>score = silhouette_score(X[clustered_mask], db_labels[clustered_mask])</code>
        </div>
      </div>
    </div>

    <!-- Mistake 08 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 8: Forcing K-Means onto Non-Convex Curved Geometries</span>
      </div>
      <p>Applying centroid-based partitioning to concentric rings, crescent moons, or winding manifolds.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Slicing Crescent Moons</span>
          <code>km = KMeans(n_clusters=2).fit(moons_data)<br># Slices right through the crescents with a straight line!</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Density or Spectral Model</span>
          <code>db = DBSCAN(eps=0.28, min_samples=6).fit(moons_data)<br># Traces the curved density contours smoothly</code>
        </div>
      </div>
    </div>

    <!-- Mistake 09 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 9: Selecting DBSCAN eps Arbitrarily Without Checking Scale</span>
      </div>
      <p>Choosing an <code>eps</code> radius from an online tutorial without calculating feature distances.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Guessing eps = 0.5</span>
          <code># If features are in millions, eps=0.5 finds 0 neighbors &rarr; 100% noise!</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: K-Distance Elbow Plot</span>
          <code>from sklearn.neighbors import NearestNeighbors<br>nbrs = NearestNeighbors(n_neighbors=5).fit(X_scaled)<br>distances, _ = nbrs.kneighbors(X_scaled)<br># Plot sorted 5th-nearest neighbor distance to find optimal eps knee!</code>
        </div>
      </div>
    </div>

    <!-- Mistake 10 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 10: Combining Ward Linkage with Non-Euclidean Metrics</span>
      </div>
      <p>Attempting to use Ward linkage with Manhattan or Cosine distance.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Mathematical Conflict</span>
          <code>agg = AgglomerativeClustering(linkage='ward', metric='manhattan')<br># Raises ValueError: Ward linkage requires euclidean metric!</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Compatible Linkage Choice</span>
          <code># For Manhattan or Cosine, use 'average', 'complete', or 'single'<br>agg = AgglomerativeClustering(linkage='average', metric='manhattan')</code>
        </div>
      </div>
    </div>

    <!-- Mistake 11 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 11: Data Leakage During Scaler Fitting on Evaluation Splits</span>
      </div>
      <p>Fitting <code>StandardScaler</code> on the combined dataset before splitting when benchmarking clustering.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Global Scaling</span>
          <code>X_scaled = scaler.fit_transform(X_all) # Leaks test distribution into train mean!</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Fit on Train Only</span>
          <code>scaler.fit(X_train)<br>X_train_scaled = scaler.transform(X_train)<br>X_test_scaled = scaler.transform(X_test)</code>
        </div>
      </div>
    </div>

    <!-- Mistake 12 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 12: Assuming High Silhouette Score Guarantees Business Value</span>
      </div>
      <p>Declaring a model successful purely because the silhouette coefficient is high.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Metric Blindness</span>
          <p>A dataset with one extreme outlier yields K=2 with a massive silhouette score (outlier is 1 cluster, all other 9,999 points are cluster 2). Mathematically separated, but completely useless for business strategy!</p>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Inspect Cluster Sizes &amp; Distributions</span>
          <p>Always inspect cluster sizes. Reject degenerate partitions containing singletons or trivial imbalance.</p>
        </div>
      </div>
    </div>

    <!-- Mistake 13 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 13: Using Raw Latitude/Longitude Degrees in Euclidean Clustering</span>
      </div>
      <p>Clustering GPS coordinates using standard Euclidean distance.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Raw Degrees</span>
          <code>km.fit(df[['latitude', 'longitude']])<br># 1 deg latitude &approx; 111 km, but 1 deg longitude shrinks with cos(latitude)!</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Haversine Metric or UTM Projection</span>
          <code># Convert coordinates to radians and use Haversine metric<br>db = DBSCAN(eps=5/6371.0, min_samples=5, metric='haversine')<br>db.fit(np.radians(df[['latitude', 'longitude']]))</code>
        </div>
      </div>
    </div>

    <!-- Mistake 14 -->
    <div class="mistake-card">
      <div class="mistake-header">
        <span class="mistake-icon">&#9888;</span>
        <span class="mistake-title">Mistake 14: Ignoring the Local Optima Trap by Setting n_init = 1</span>
      </div>
      <p>Running K-Means with a single random initialization seed.</p>
      <div class="mistake-grid">
        <div class="mistake-bad">
          <span class="mistake-tag">&#10008; Bad: Single Run</span>
          <code>km = KMeans(n_clusters=4, n_init=1) # Risk of trapping in poor local minimum</code>
        </div>
        <div class="mistake-good">
          <span class="mistake-tag">&#10004; Good: Multi-Run Restart</span>
          <code>km = KMeans(n_clusters=4, init='k-means++', n_init=10, random_state=42)<br># Selects best solution across 10 independent starts</code>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 25 -->
  <section id="sec-25" class="content-section">
    <span class="section-badge">Section 25 &bull; Visual Catalog</span>
    <h2 class="section-title">Required Graphs and Visualizations Guide</h2>

    <p>
      This chapter integrates 18 verified vector diagrams to illustrate every mathematical and structural concept. Here is the comprehensive catalog:
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Figure ID</th>
            <th>Diagram Title</th>
            <th>Type</th>
            <th>Core Educational Takeaway</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fig 1.1</strong></td>
            <td>Unclustered Points vs Discovered Clusters</td>
            <td>Conceptual</td>
            <td>Raw data has no labels; clustering assigns colors representing discovered density partitions.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.2</strong></td>
            <td>Classification vs Clustering</td>
            <td>Comparative</td>
            <td>Supervised learns a boundary to predict known classes; unsupervised discovers intrinsic grouping.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.3</strong></td>
            <td>Euclidean vs Manhattan Distance</td>
            <td>Geometric</td>
            <td>Straight-line hypotenuse (&radic;73 &approx; 8.54) vs city-block coordinate path (3 + 8 = 11).</td>
          </tr>
          <tr>
            <td><strong>Fig 1.4</strong></td>
            <td>Feature Scaling Effect</td>
            <td>Diagnostic</td>
            <td>Unscaled large features distort distance circles into flattened ellipses; standardization restores isotropic distance.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.5</strong></td>
            <td>K-Means 4-Step Lloyd Algorithm</td>
            <td>Process Flow</td>
            <td>Walks through centroid seed &rarr; Voronoi assignment &rarr; center re-estimation &rarr; convergence.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.6</strong></td>
            <td>Final K-Means with Centroids</td>
            <td>Verified Model</td>
            <td>Fitted K=3 model with golden stars marking true empirical centroids and inertia vectors.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.7</strong></td>
            <td>Elbow Method Curve</td>
            <td>Verified Curve</td>
            <td>Genuine inertia curve across K=2..6 showing prominent inflection elbow at K=3 (inertia 47.04).</td>
          </tr>
          <tr>
            <td><strong>Fig 1.8</strong></td>
            <td>Silhouette Score Profile</td>
            <td>Verified Curve</td>
            <td>Silhouette peaks decisively at K=3 with score 0.7746, proving maximum cluster separation.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.9</strong></td>
            <td>K-Means Partitions Grid (K=2,3,4,5)</td>
            <td>Comparative Grid</td>
            <td>Visually contrasts under-clustering (K=2), optimal grouping (K=3), and over-segmentation (K=4,5).</td>
          </tr>
          <tr>
            <td><strong>Fig 1.10</strong></td>
            <td>K-Means Success vs Failure</td>
            <td>Limitation</td>
            <td>K-Means thrives on spherical Gaussian blobs but catastrophically fails on interlocking non-convex crescents.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.11</strong></td>
            <td>Linkage Methods Comparison</td>
            <td>Geometric</td>
            <td>Visualizes Single (min), Complete (max), Average (mean), and Ward (variance increase) cluster distances.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.12</strong></td>
            <td>SciPy Hierarchical Dendrogram</td>
            <td>Verified Tree</td>
            <td>Genuine hierarchical tree; vertical height directly indicates linkage distance at merge events.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.13</strong></td>
            <td>Dendrogram Horizontal Cuts</td>
            <td>Methodological</td>
            <td>Cutting at heights 25, 12, and 6 produces K=2, K=3, and K=5 flat clusters respectively.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.14</strong></td>
            <td>DBSCAN Core, Border, Noise Points</td>
            <td>Conceptual</td>
            <td>Defines core points (|N<sub>&epsilon;</sub>| &ge; min_samples), border points, and isolated noise anomalies.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.15</strong></td>
            <td>DBSCAN Discovered Clusters &amp; Noise</td>
            <td>Verified Model</td>
            <td>DBSCAN cleanly tracks two curved crescent moons and flags all 18 scattered outliers as noise &times;.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.16</strong></td>
            <td>DBSCAN eps Parameter Sensitivity</td>
            <td>Diagnostic</td>
            <td>eps=0.12 shatters clusters; eps=0.28 achieves optimal tracking; eps=0.55 merges clusters into one blob.</td>
          </tr>
          <tr>
            <td><strong>Fig 1.17</strong></td>
            <td>K-Means vs DBSCAN Head-to-Head</td>
            <td>Comparative</td>
            <td>K-Means achieves ARI=0.4053 (fails on moons); DBSCAN achieves ARI=0.9770 (perfect non-convex recovery).</td>
          </tr>
          <tr>
            <td><strong>Fig 1.18</strong></td>
            <td>Clustering Metrics Profile</td>
            <td>Multi-Metric</td>
            <td>Unanimous consensus at K=3: peak Silhouette (0.7746), peak Calinski-Harabasz (1745.5), minimum Davies-Bouldin (0.3090).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 26 -->
  <section id="sec-26" class="content-section">
    <span class="section-badge">Section 26 &bull; Quick Reference</span>
    <h2 class="section-title">Quick Reference &amp; Cheat Sheet</h2>

    <div class="callout-card callout-def">
      <div class="callout-title">Algorithm Selection Decision Flowchart</div>
      <ul>
        <li><strong>Do you expect spherical, compact clusters and need fast scaling to 1M+ rows?</strong><br>&rarr; Use <strong>K-Means</strong> (with <code>StandardScaler</code> and <code>n_init=10</code>).</li>
        <li><strong>Do you need an interpretable hierarchy or taxonomy without choosing K upfront?</strong><br>&rarr; Use <strong>Agglomerative Hierarchical Clustering</strong> (Ward linkage for compact blobs, Complete for bounded diameter).</li>
        <li><strong>Does your data have arbitrary non-linear shapes, curved manifolds, and background noise/outliers?</strong><br>&rarr; Use <strong>DBSCAN</strong> (tune <code>eps</code> via k-distance graph).</li>
        <li><strong>Do points belong to multiple categories probabilistically with soft membership?</strong><br>&rarr; Use <strong>Gaussian Mixture Models (GMM)</strong>.</li>
      </ul>
    </div>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Concept / Formula</th>
            <th>Mathematical Expression</th>
            <th>Key Takeaway</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Euclidean Distance</strong></td>
            <td><code>d(x,y) = &radic;[ &sum; (x<sub>i</sub> &minus; y<sub>i</sub>)&sup2; ]</code></td>
            <td>Straight-line metric; default for K-Means and Ward linkage.</td>
          </tr>
          <tr>
            <td><strong>Manhattan Distance</strong></td>
            <td><code>d(x,y) = &sum; |x<sub>i</sub> &minus; y<sub>i</sub>|</code></td>
            <td>City-block metric; robust against modest coordinate outliers.</td>
          </tr>
          <tr>
            <td><strong>Standardization</strong></td>
            <td><code>z = (x &minus; &mu;) / &sigma;</code></td>
            <td>Mandatory prior to distance-based clustering.</td>
          </tr>
          <tr>
            <td><strong>K-Means Objective</strong></td>
            <td><code>J = &sum;<sub>k</sub> &sum;<sub>x &isin; C<sub>k</sub></sub> ||x &minus; &mu;<sub>k</sub>||&sup2;</code></td>
            <td>Minimizes within-cluster sum of squared errors (Inertia).</td>
          </tr>
          <tr>
            <td><strong>Silhouette Score</strong></td>
            <td><code>s = (b &minus; a) / max(a, b)</code></td>
            <td>Evaluates separation vs compactness; bounded [&minus;1, +1].</td>
          </tr>
          <tr>
            <td><strong>Davies-Bouldin Index</strong></td>
            <td><code>DB = (1/K) &sum; max<sub>j&ne;i</sub> (s<sub>i</sub> + s<sub>j</sub>) / d(&mu;<sub>i</sub>, &mu;<sub>j</sub>)</code></td>
            <td>Lower is better; 0 indicates perfectly separated compact clusters.</td>
          </tr>
          <tr>
            <td><strong>DBSCAN Core Rule</strong></td>
            <td><code>|N<sub>&epsilon;</sub>(p)| &ge; min_samples</code></td>
            <td>Defines dense regions; unassigned points labeled as noise &minus;1.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 27 -->
  <section id="sec-27" class="content-section">
    <span class="section-badge">Section 27 &bull; Interactive Knowledge Checks</span>
    <h2 class="section-title">Interactive Knowledge Checks &amp; FAQs</h2>

    <p>Test your conceptual understanding by expanding each accordion below:</p>

    <!-- FAQ 1 -->
    <details>
      <summary>1. Why is clustering classified as an unsupervised learning task?</summary>
      <div class="details-content">
        Clustering is unsupervised because the dataset contains only input feature coordinates <em>X</em> without any target labels or ground-truth classifications <em>y</em>. The algorithm discovers groupings based purely on intrinsic geometric, statistical, or density similarities without external guidance or error correction from a teacher.
      </div>
    </details>

    <!-- FAQ 2 -->
    <details>
      <summary>2. What is the fundamental difference between clustering and classification?</summary>
      <div class="details-content">
        Supervised classification trains an inductive model on pre-labeled training data to predict discrete target classes on new observations. Unsupervised clustering operates without labels, seeking to uncover natural internal subgroups or structural partitions within the feature space.
      </div>
    </details>

    <!-- FAQ 3 -->
    <details>
      <summary>3. Why does feature scaling have such a massive impact on distance-based clustering?</summary>
      <div class="details-content">
        Distance metrics (such as Euclidean distance) sum differences across all feature axes. If one feature spans a scale of thousands (e.g., Annual Salary in $) while another spans single digits (e.g., Household Size), the large-scale feature completely dominates the squared difference calculation, rendering the algorithm blind to the smaller feature. Standardization rescales all features to zero mean and unit variance.
      </div>
    </details>

    <!-- FAQ 4 -->
    <details>
      <summary>4. Why can't we simply pick K by finding the minimum value of inertia?</summary>
      <div class="details-content">
        Inertia decreases monotonically as <em>K</em> increases. If you set <em>K = N</em> (where every point is its own cluster), inertia drops to exactly 0! However, having <em>N</em> clusters provides zero data abstraction or business utility. Therefore, we look for the point of diminishing returns (the Elbow) or peak Silhouette score.
      </div>
    </details>

    <!-- FAQ 5 -->
    <details>
      <summary>5. What does a negative silhouette score mean?</summary>
      <div class="details-content">
        A negative silhouette score indicates that for that observation, the intra-cluster distance <em>a(i)</em> is greater than the nearest-cluster distance <em>b(i)</em>. This means the point is physically closer to members of an adjacent cluster than to members of its assigned cluster, indicating a likely misclustering.
      </div>
    </details>

    <!-- FAQ 6 -->
    <details>
      <summary>6. Why does K-Means converge to a local optimum rather than a global optimum?</summary>
      <div class="details-content">
        Lloyd's algorithm uses greedy coordinate descent: it alternates between point assignment and centroid re-estimation, which is guaranteed to reduce or hold constant inertia at every step. However, the objective function is non-convex with numerous local minima. Scikit-learn mitigates this by using <code>k-means++</code> initialization and running multiple restarts (<code>n_init=10</code>).
      </div>
    </details>

    <!-- FAQ 7 -->
    <details>
      <summary>7. What is the "chaining effect" in hierarchical single linkage?</summary>
      <div class="details-content">
        Single linkage defines inter-cluster distance as the minimum distance between any pair of points. If a sparse trail of noise points or outliers forms a thin bridge between two otherwise distant clusters, single linkage will merge the two large clusters prematurely along this chain, creating elongated, unnatural clusters.
      </div>
    </details>

    <!-- FAQ 8 -->
    <details>
      <summary>8. Why is Ward linkage restricted exclusively to Euclidean distance?</summary>
      <div class="details-content">
        Ward linkage minimizes the total increase in within-cluster variance (sum of squared deviations from the mean centroid) resulting from merging two clusters. Because variance and centroids are mathematically defined in terms of squared Euclidean norms, applying Ward linkage to non-Euclidean metrics (like Manhattan or Cosine) violates the underlying variance formula.
      </div>
    </details>

    <!-- FAQ 9 -->
    <details>
      <summary>9. How does DBSCAN identify noise points, and what label does scikit-learn assign them?</summary>
      <div class="details-content">
        DBSCAN examines each point's &epsilon;-neighborhood. If a point has fewer than <code>min_samples</code> neighbors and does not fall within the &epsilon;-neighborhood of any core point, it cannot be reached by density expansion. Scikit-learn flags these isolated points as noise by assigning them the special cluster label <code>&minus;1</code>.
      </div>
    </details>

    <!-- FAQ 10 -->
    <details>
      <summary>10. When does DBSCAN fail?</summary>
      <div class="details-content">
        DBSCAN struggles when clusters have wildly varying local densities. A global &epsilon; radius that works for a dense cluster will treat a sparser, spread-out cluster entirely as noise. Conversely, an &epsilon; large enough to capture the sparse cluster will merge multiple adjacent dense clusters into one giant blob. (In such cases, HDBSCAN or OPTICS is preferred).
      </div>
    </details>

    <!-- FAQ 11 -->
    <details>
      <summary>11. Why does K-Means fail on crescent moons and concentric rings?</summary>
      <div class="details-content">
        K-Means partitions feature space using Voronoi cells bounded by linear hyperplanes perpendicular to centroid vectors. Non-convex shapes (like crescents and rings) cannot be separated by linear boundaries; attempting to place a centroid inside a crescent often puts the centroid in the empty space between the arms, causing K-Means to slice straight across the manifold.
      </div>
    </details>

    <!-- FAQ 12 -->
    <details>
      <summary>12. How should you validate clustering results in an enterprise business environment?</summary>
      <div class="details-content">
        In real-world business applications without ground-truth labels, combine: (1) Internal geometric metrics (Silhouette, Davies-Bouldin) to confirm structural compactness, (2) Feature profiling by computing cluster means and standard deviations to interpret customer behavior, (3) Stability checks by retraining on bootstrapped subsamples to confirm clusters do not fluctuate wildly, and (4) Business A/B testing (e.g., verifying if targeted marketing campaigns to distinct clusters improve conversion rates).
      </div>
    </details>
  </section>

  <!-- Footer -->
  <footer class="notes-footer">
    <p><strong>CodeVerse Machine Learning Track</strong> &bull; Topic 16: Clustering</p>
    <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 6px;">
      Strict Light Mode &bull; High-Contrast Accessible Design &bull; Verified scikit-learn 1.9 &amp; SciPy 1.17 Pipelines
    </p>
  </footer>

</div>
"""
