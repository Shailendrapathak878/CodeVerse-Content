"""Topic 16 Part 1: Hero Header, TOC, Sections 1-6.
Strict Light Mode, semantic HTML, math typography, verified numbers.
"""

TOPIC16_PART1 = """
<div class="container">

  <!-- Hero Header -->
  <header class="hero-header">
    <div class="hero-badge">
      <span>&#9670;</span> CodeVerse Machine Learning Track &bull; Topic 16
    </div>
    <h1 class="hero-title">Clustering &amp; Unsupervised Pattern Discovery</h1>
    <p class="hero-subtitle">
      A comprehensive, visual, and mathematical guide to discovering natural groupings in data without labels. Master K-Means, Hierarchical Linkage, Dendrograms, and DBSCAN from geometric intuition to production scikit-learn pipelines.
    </p>

    <div class="hero-meta-grid">
      <div class="meta-item">
        <span class="meta-label">Curriculum Depth</span>
        <span class="meta-value">27 Complete Sections</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Visual Systems</span>
        <span class="meta-value">18 Verified Vector Diagrams</span>
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
      <a href="#sec-01" class="toc-link"><span class="toc-num">01</span> Introduction to Clustering</a>
      <a href="#sec-02" class="toc-link"><span class="toc-num">02</span> Clustering vs Classification</a>
      <a href="#sec-03" class="toc-link"><span class="toc-num">03</span> Understanding Features and Distance</a>
      <a href="#sec-04" class="toc-link"><span class="toc-num">04</span> Why Feature Scaling Matters</a>
      <a href="#sec-05" class="toc-link"><span class="toc-num">05</span> Introduction to K-Means</a>
      <a href="#sec-06" class="toc-link"><span class="toc-num">06</span> How K-Means Works Step by Step</a>
      <a href="#sec-07" class="toc-link"><span class="toc-num">07</span> K-Means Objective &amp; Inertia</a>
      <a href="#sec-08" class="toc-link"><span class="toc-num">08</span> Choosing K: The Elbow Method</a>
      <a href="#sec-09" class="toc-link"><span class="toc-num">09</span> Silhouette Score Analysis</a>
      <a href="#sec-10" class="toc-link"><span class="toc-num">10</span> Visualizing Different K Values</a>
      <a href="#sec-11" class="toc-link"><span class="toc-num">11</span> K-Means Strengths &amp; Limitations</a>
      <a href="#sec-12" class="toc-link"><span class="toc-num">12</span> Hierarchical Clustering Fundamentals</a>
      <a href="#sec-13" class="toc-link"><span class="toc-num">13</span> Hierarchical Linkage Criteria</a>
      <a href="#sec-14" class="toc-link"><span class="toc-num">14</span> Dendrograms &amp; Tree Cutting</a>
      <a href="#sec-15" class="toc-link"><span class="toc-num">15</span> DBSCAN Density Fundamentals</a>
      <a href="#sec-16" class="toc-link"><span class="toc-num">16</span> Visualizing DBSCAN in Action</a>
      <a href="#sec-17" class="toc-link"><span class="toc-num">17</span> Master Paradigm Comparison</a>
      <a href="#sec-18" class="toc-link"><span class="toc-num">18</span> Other Clustering Paradigms</a>
      <a href="#sec-19" class="toc-link"><span class="toc-num">19</span> Python Lab 1: End-to-End K-Means</a>
      <a href="#sec-20" class="toc-link"><span class="toc-num">20</span> Python Lab 2: Hierarchical Clustering</a>
      <a href="#sec-21" class="toc-link"><span class="toc-num">21</span> Python Lab 3: DBSCAN with Outliers</a>
      <a href="#sec-22" class="toc-link"><span class="toc-num">22</span> Internal &amp; External Evaluation</a>
      <a href="#sec-23" class="toc-link"><span class="toc-num">23</span> Real-World Industry Applications</a>
      <a href="#sec-24" class="toc-link"><span class="toc-num">24</span> Common Beginner Mistakes &amp; Fixes</a>
      <a href="#sec-25" class="toc-link"><span class="toc-num">25</span> Visual Gallery &amp; Diagram Guide</a>
      <a href="#sec-26" class="toc-link"><span class="toc-num">26</span> Quick Reference &amp; Cheat Sheet</a>
      <a href="#sec-27" class="toc-link"><span class="toc-num">27</span> Interactive Knowledge Checks &amp; FAQs</a>
    </div>
  </nav>

  <!-- SECTION 01 -->
  <section id="sec-01" class="content-section">
    <span class="section-badge">Section 01 &bull; Core Foundations</span>
    <h2 class="section-title">Introduction to Clustering</h2>

    <p>
      Imagine walking into a massive wholesale bookstore containing 100,000 unlabelled books stacked randomly on pallets. Nobody handed you a catalog, category tags, or genre stickers. How would you organize them? You would naturally inspect each book&#39;s physical and thematic properties: cover thickness, page count, illustration density, vocabulary complexity, and subject keywords. Gradually, piles begin to take shape: large colorful picture books gather in one corner, dense dense mathematics texts gather in another, and pocket mystery novels assemble along the wall.
    </p>

    <div class="callout-card callout-analogy">
      <div class="callout-title">The Real-World Retail Analogy: Customer Segmentation</div>
      <p>
        In modern e-commerce, a retailer records transaction records for 500,000 shoppers. Nobody tells the database who is a <em>"Bargain Hunter"</em>, a <em>"Holiday Splurger"</em>, or a <em>"Loyal Daily Buyer"</em>. By grouping customers based on purchase frequency, cart size, and return rate, clustering algorithms uncover these natural demographic profiles entirely on their own.
      </p>
    </div>

    <p>
      This process of grouping items based purely on intrinsic similarities without pre-existing labels is known as <strong>Clustering</strong>. Unlike supervised learning where a teacher provides the exact target answer for every training sample, clustering operates entirely in an <strong>unsupervised</strong> setting.
    </p>

    <div class="callout-card callout-def">
      <div class="callout-title">Essential Vocabulary &bull; The 7 Core Terms</div>
      <ul>
        <li><strong>Unsupervised Learning:</strong> Machine learning algorithms that uncover underlying patterns, groupings, or geometric structures from feature data without target labels (<em>y</em>).</li>
        <li><strong>Cluster:</strong> A collection of data points that are significantly more similar to one another than to points assigned to other collections.</li>
        <li><strong>Similarity:</strong> A quantitative measure of how alike two observations are; higher similarity corresponds to smaller distances in feature space.</li>
        <li><strong>Distance Metric:</strong> A mathematical function that quantifies the geometric dissimilarity between two feature vectors (e.g., Euclidean or Manhattan distance).</li>
        <li><strong>Feature:</strong> A measurable property or attribute of an observation, such as monthly spend, visit frequency, or customer age.</li>
        <li><strong>Data Point (Sample / Observation):</strong> A single entity represented as an <em>n</em>-dimensional vector <strong>x</strong> = [x<sub>1</sub>, x<sub>2</sub>, &hellip;, x<sub>n</sub>].</li>
        <li><strong>Cluster Assignment:</strong> The discrete index or partition label assigned to a data point by a clustering algorithm (e.g., Cluster 0, 1, or 2).</li>
      </ul>
    </div>

    <!-- Visual 01 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.1: Unclustered Points vs Discovered Clusters</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_CLUSTERING_OVERVIEW__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.1:</strong> Left: Raw, unlabeled observations in a two-dimensional feature space appear as indistinguishable grey markers. Right: The clustering algorithm identifies dense groupings and assigns categorical colors representing discovered structural partitions. Note that these colors reflect discovered clusters, not pre-existing ground-truth labels.
      </p>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; Critical Mindset: Clusters Are Discovered Patterns, Not Universal Truths</div>
      <p>
        The colors assigned to clusters do not reflect pre-existing labels stamped by nature. A clustering algorithm merely discovers mathematical density or distance partitions within the specific feature representation provided. If you change the features, alter the scaling, or select a different distance metric, the resulting clusters can completely shift!
      </p>
    </div>
  </section>

  <!-- SECTION 02 -->
  <section id="sec-02" class="content-section">
    <span class="section-badge">Section 02 &bull; Conceptual Demarcation</span>
    <h2 class="section-title">Clustering vs Classification</h2>

    <p>
      Beginners frequently confuse clustering with classification because both partition observations into discrete categorical groups. However, their underlying mathematical formulations, data requirements, and validation paradigms are fundamentally different.
    </p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Dimension</th>
            <th>Supervised Classification</th>
            <th>Unsupervised Clustering</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Learning Paradigm</strong></td>
            <td>Supervised Learning</td>
            <td>Unsupervised Learning</td>
          </tr>
          <tr>
            <td><strong>Ground-Truth Labels</strong></td>
            <td>Required during training (<em>y</em> &isin; {0, 1, &hellip;, C})</td>
            <td>None available (only feature matrix <em>X</em>)</td>
          </tr>
          <tr>
            <td><strong>Primary Objective</strong></td>
            <td>Learn an inductive decision boundary to accurately predict labels on unseen observations</td>
            <td>Discover underlying geometric structures, subgroups, or density manifolds in the data</td>
          </tr>
          <tr>
            <td><strong>Example Task</strong></td>
            <td>Classifying patient medical scans as <em>"Malignant"</em> or <em>"Benign"</em></td>
            <td>Segmenting hospital patients into holistic wellness recovery groups</td>
          </tr>
          <tr>
            <td><strong>Typical Output</strong></td>
            <td>Predicted class label or class probability distribution</td>
            <td>Cluster membership identifier (0, 1, 2) or noise flag (-1)</td>
          </tr>
          <tr>
            <td><strong>Common Algorithms</strong></td>
            <td>Logistic Regression, Random Forest, XGBoost, Support Vector Machines</td>
            <td>K-Means, Agglomerative Hierarchical Clustering, DBSCAN, Gaussian Mixtures</td>
          </tr>
          <tr>
            <td><strong>Evaluation Basis</strong></td>
            <td>Objective ground-truth metrics: Accuracy, Precision, Recall, ROC-AUC</td>
            <td>Internal geometric metrics (Silhouette, Inertia, Davies-Bouldin) and domain utility</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Visual 02 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.2: Labelled Classification vs Unsupervised Clustering</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_CLUSTERING_VS_CLASSIFICATION__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.2:</strong> Classification (left) learns an optimal separating hyperplane to differentiate pre-known positive (blue circles) and negative (coral squares) classes. Clustering (right) inspects raw unlabeled points and identifies cohesive spatial neighborhoods centered around calculated centroids without external supervision.
      </p>
    </div>

    <p>
      A key takeaway for practitioners: <strong>Clustering discovers mathematical structure; it does not automatically guarantee business or physical meaning.</strong> A cluster only becomes actionable when human domain experts inspect its constituent members and validate its real-world relevance.
    </p>
  </section>

  <!-- SECTION 03 -->
  <section id="sec-03" class="content-section">
    <span class="section-badge">Section 03 &bull; Mathematical Mechanics</span>
    <h2 class="section-title">Understanding Features and Distance Metrics</h2>

    <p>
      How does a computer decide whether two customer profiles are "close" or "far apart"? Because algorithms cannot read qualitative narratives, every observation is translated into an <em>n</em>-dimensional vector of numerical coordinates.
    </p>

    <p>
      Consider two retail customers measured on two features:
    </p>
    <ul>
      <li><strong>Point X (Customer A):</strong> Annual Spending = $4k, Monthly Visits = 12 visits &rarr; <code>X = (4, 12)</code></li>
      <li><strong>Point Y (Customer B):</strong> Annual Spending = $7k, Monthly Visits = 4 visits &rarr; <code>Y = (7, 4)</code></li>
    </ul>

    <h3 class="subsection-title">1. Euclidean Distance (Straight-Line Distance)</h3>
    <p>
      Euclidean distance is the geometric straight-line distance between two points in Euclidean space, derived directly from the Pythagorean theorem:
    </p>

    <div class="formula-block">
      d(x, y) = &radic;[ &sum;<sub>i=1</sub><sup>n</sup> (x<sub>i</sub> &minus; y<sub>i</sub>)&sup2; ]
      <div class="formula-breakdown">
        <div class="breakdown-item"><strong>d(x, y):</strong> Scalar Euclidean distance between vectors x and y</div>
        <div class="breakdown-item"><strong>n:</strong> Dimensionality (number of features)</div>
        <div class="breakdown-item"><strong>x<sub>i</sub>, y<sub>i</sub>:</strong> Coordinate value of feature <em>i</em> for sample <em>x</em> and sample <em>y</em></div>
        <div class="breakdown-item"><strong>(x<sub>i</sub> &minus; y<sub>i</sub>)&sup2;:</strong> Squared coordinate difference along axis <em>i</em></div>
      </div>
    </div>

    <p>
      Let us compute Euclidean distance step-by-step for our points <code>X = (4, 12)</code> and <code>Y = (7, 4)</code>:
    </p>
    <ol>
      <li>Compute coordinate differences: &Delta;x<sub>1</sub> = 7 &minus; 4 = 3, &Delta;x<sub>2</sub> = 4 &minus; 12 = &minus;8</li>
      <li>Square each difference: 3&sup2; = 9, (&minus;8)&sup2; = 64</li>
      <li>Sum the squared differences: 9 + 64 = 73</li>
      <li>Take the square root: <strong>d(X, Y) = &radic;73 &approx; 8.5440</strong></li>
    </ol>

    <h3 class="subsection-title">2. Manhattan Distance (City-Block / L1 Distance)</h3>
    <p>
      Manhattan distance measures the distance traveled along grid-aligned axes, analogous to a taxi navigating perpendicular streets in Manhattan:
    </p>

    <div class="formula-block">
      d(x, y) = &sum;<sub>i=1</sub><sup>n</sup> |x<sub>i</sub> &minus; y<sub>i</sub>|
      <div class="formula-breakdown">
        <div class="breakdown-item"><strong>|x<sub>i</sub> &minus; y<sub>i</sub>|:</strong> Absolute coordinate difference along feature axis <em>i</em></div>
        <div class="breakdown-item"><strong>&sum;:</strong> Direct arithmetic sum of all axis distances without squaring or roots</div>
      </div>
    </div>

    <p>
      Computing Manhattan distance for <code>X = (4, 12)</code> and <code>Y = (7, 4)</code>:
    </p>
    <div style="background: #F8FAFC; padding: 12px 18px; border-radius: 8px; border: 1px solid #E2E8F0; margin-bottom: 16px;">
      <code>d<sub>Manhattan</sub>(X, Y) = |7 &minus; 4| + |4 &minus; 12| = 3 + 8 = <strong>11.0000</strong></code>
    </div>

    <p>
      Notice that Manhattan distance (11.0000) is strictly greater than Euclidean distance (8.5440). By the triangle inequality, the straight-line hypotenuse is always the shortest possible spatial path.
    </p>

    <h3 class="subsection-title">3. Cosine Similarity &amp; Cosine Distance</h3>
    <p>
      In high-dimensional sparse spaces (such as TF-IDF text vectors, NLP embeddings, or document representations), two documents might share the exact same topic distribution even if one document is 10 times longer than the other. Euclidean distance would erroneously label them far apart due to document length. <strong>Cosine Similarity</strong> measures the angle &theta; between vectors regardless of their magnitude:
    </p>

    <div class="formula-block">
      Cosine Similarity = cos(&theta;) = (x &bull; y) / (||x|| &times; ||y||)
    </div>
    <p>
      Cosine distance is simply <code>1 &minus; Cosine Similarity</code>. While invaluable for text embeddings, standard K-Means in scikit-learn optimizes Euclidean distance; using cosine distance requires spherical K-Means or prior L2 unit vector normalization!
    </p>

    <!-- Visual 03 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.3: Euclidean vs Manhattan Distance in 2D Feature Space</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_EUCLIDEAN_VS_MANHATTAN__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.3:</strong> Comparing the straight-line Euclidean distance (solid indigo hypotenuse, &radic;73 &approx; 8.54) against the grid-based Manhattan distance (dashed amber right-angle steps, 3 + 8 = 11) between point X(4, 12) and point Y(7, 4).
      </p>
    </div>
  </section>

  <!-- SECTION 04 -->
  <section id="sec-04" class="content-section">
    <span class="section-badge">Section 04 &bull; Preprocessing Imperative</span>
    <h2 class="section-title">Why Feature Scaling Matters</h2>

    <p>
      Distance calculations sum differences across all feature axes. What happens if Feature 1 is <strong>Annual Income</strong> ranging from $20,000 to $200,000, while Feature 2 is <strong>Household Size</strong> ranging from 1 to 6 people?
    </p>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; The Scale Dominance Disaster</div>
      <p>
        A difference of $5,000 in income yields a squared difference of 5,000&sup2; = <strong>25,000,000</strong>. Meanwhile, a difference of 3 family members yields 3&sup2; = <strong>9</strong>. The income feature contributes 99.9999% of the distance calculation! The clustering algorithm becomes completely blind to household size, treating data points with identical incomes as near-twins even if one is a college student and the other is a family of six.
      </p>
    </div>

    <h3 class="subsection-title">Standardization (Z-Score Normalization)</h3>
    <p>
      Standardization rescales each feature so that it possesses a mean of 0 (&mu; = 0) and a standard deviation of 1 (&sigma; = 1):
    </p>

    <div class="formula-block">
      z = (x &minus; &mu;) / &sigma;
      <div class="formula-breakdown">
        <div class="breakdown-item"><strong>z:</strong> Standardized feature score (dimensionless z-score)</div>
        <div class="breakdown-item"><strong>x:</strong> Original raw feature value</div>
        <div class="breakdown-item"><strong>&mu;:</strong> Empirical mean of the feature across training samples</div>
        <div class="breakdown-item"><strong>&sigma;:</strong> Empirical standard deviation of the feature</div>
      </div>
    </div>

    <p>
      Let us standardize a toy feature array: <code>[20, 40, 60, 80, 100]</code>.
    </p>
    <ul>
      <li>Mean &mu; = (20 + 40 + 60 + 80 + 100) / 5 = <strong>60.0</strong></li>
      <li>Variance &sigma;&sup2; = [(&minus;40)&sup2; + (&minus;20)&sup2; + 0&sup2; + 20&sup2; + 40&sup2;] / 5 = [1600 + 400 + 0 + 400 + 1600] / 5 = 4000 / 5 = 800</li>
      <li>Standard deviation &sigma; = &radic;800 &approx; <strong>28.2843</strong></li>
      <li>Standardized points:
        <br>&bull; z<sub>1</sub> = (20 &minus; 60) / 28.2843 = <strong>&minus;1.4142</strong>
        <br>&bull; z<sub>2</sub> = (40 &minus; 60) / 28.2843 = <strong>&minus;0.7071</strong>
        <br>&bull; z<sub>3</sub> = (60 &minus; 60) / 28.2843 = <strong>0.0000</strong>
        <br>&bull; z<sub>4</sub> = (80 &minus; 60) / 28.2843 = <strong>+0.7071</strong>
        <br>&bull; z<sub>5</sub> = (100 &minus; 60) / 28.2843 = <strong>+1.4142</strong>
      </li>
    </ul>

    <!-- Visual 04 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.4: Feature Scaling Impact on Distance Metric Equivalence</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_SCALING_EFFECT__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.4:</strong> Before scaling (left), the horizontal axis (spanning $0 to $100k) completely dwarfs the vertical axis (spanning 1 to 10 purchases), flattening the visual distribution and distorting Euclidean distance circles into ultra-elongated ellipses. After standardization (right), both features share identical zero mean and unit variance, enabling balanced, isotropic distance evaluation.
      </p>
    </div>

    <div class="callout-card callout-success">
      <div class="callout-title">&#10004; Best Practice: Use scikit-learn Pipeline</div>
      <p>
        Always bundle your preprocessor with the clustering estimator inside a scikit-learn <code>Pipeline</code>. This prevents data leakage and ensures identical transformation logic is applied during prediction:
      </p>
      <code>from sklearn.pipeline import Pipeline<br>from sklearn.preprocessing import StandardScaler<br>from sklearn.cluster import KMeans<br><br>pipeline = Pipeline([('scaler', StandardScaler()), ('kmeans', KMeans(n_clusters=3, random_state=42))])</code>
    </div>
  </section>

  <!-- SECTION 05 -->
  <section id="sec-05" class="content-section">
    <span class="section-badge">Section 05 &bull; Foundational Partitioning</span>
    <h2 class="section-title">Introduction to K-Means</h2>

    <p>
      <strong>K-Means</strong> is one of the most widely used and intuitive unsupervised algorithms in machine learning. Its goal is simple: partition a dataset of <em>N</em> observations into <strong>K distinct, non-overlapping clusters</strong>, where each observation belongs to the cluster with the nearest mean.
    </p>

    <div class="callout-card callout-def">
      <div class="callout-title">The Three Pillars of K-Means</div>
      <ul>
        <li><strong>K (Cluster Count):</strong> A user-specified hyperparameter defining the exact number of clusters to form. The algorithm does not automatically determine <em>K</em>; the practitioner must supply it prior to training.</li>
        <li><strong>Centroid (&mu;<sub>k</sub>):</strong> The geometric center (mean feature vector) of all data points currently assigned to cluster <em>k</em>. For a cluster with points {x<sub>1</sub>, x<sub>2</sub>, &hellip;, x<sub>m</sub>}, the centroid is computed as:
          <br><code>&mu;<sub>k</sub> = (1 / m) &sum;<sub>i=1</sub><sup>m</sup> x<sub>i</sub></code>
        </li>
        <li><strong>Inertia (Within-Cluster Sum of Squares):</strong> The total sum of squared Euclidean distances between each point and its assigned cluster centroid. Lower inertia indicates tighter, more compact clusters.</li>
      </ul>
    </div>

    <p>
      K-Means partitions space into <em>Voronoi cells</em>—polygonal convex regions where every point inside a cell is closer to that cell&#39;s centroid than to any other centroid.
    </p>
  </section>

  <!-- SECTION 06 -->
  <section id="sec-06" class="content-section">
    <span class="section-badge">Section 06 &bull; Algorithmic Execution</span>
    <h2 class="section-title">How K-Means Works Step by Step</h2>

    <p>
      K-Means employs an iterative optimization algorithm known as <strong>Lloyd&#39;s Algorithm</strong>. It alternates between two core operations: point assignment and centroid re-estimation.
    </p>

    <div class="step-flow">
      <div class="step-item">
        <div class="step-number">1</div>
        <div class="step-content">
          <div class="step-title">Specify K Clusters</div>
          <p class="step-desc">The user selects the target number of clusters <em>K</em> based on domain requirements, the Elbow method, or silhouette validation.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">2</div>
        <div class="step-content">
          <div class="step-title">Initialize Centroids</div>
          <p class="step-desc"><em>K</em> initial centroid coordinates are placed into the feature space. Modern scikit-learn uses <strong>k-means++</strong> initialization, which spreads initial seeds far apart to prevent poor local convergence.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">3</div>
        <div class="step-content">
          <div class="step-title">Assignment Step (Expectation)</div>
          <p class="step-desc">Every data point in the dataset calculates its Euclidean distance to all <em>K</em> centroids and is assigned to the nearest one:
          <br><code>c<sup>(i)</sup> = argmin<sub>k</sub> ||x<sup>(i)</sup> &minus; &mu;<sub>k</sub>||&sup2;</code></p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">4</div>
        <div class="step-content">
          <div class="step-title">Update Step (Maximization)</div>
          <p class="step-desc">Each centroid is relocated to the precise mathematical center (mean vector) of all data points currently assigned to it:
          <br><code>&mu;<sub>k</sub> = (1 / |C<sub>k</sub>|) &sum;<sub>x &isin; C<sub>k</sub></sub> x</code></p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">5</div>
        <div class="step-content">
          <div class="step-title">Iterate to Convergence</div>
          <p class="step-desc">Steps 3 and 4 are repeated sequentially. In each round, points may switch clusters, causing centroids to migrate toward the centers of mass.</p>
        </div>
      </div>
      <div class="step-item">
        <div class="step-number">6</div>
        <div class="step-content">
          <div class="step-title">Termination / Stopping Rule</div>
          <p class="step-desc">The algorithm halts when: (a) centroid positions no longer shift beyond a threshold <code>tol</code> (e.g., 1e-4), (b) zero points switch assignments, or (c) <code>max_iter</code> (default 300) is reached.</p>
        </div>
      </div>
    </div>

    <!-- Visual 05 -->
    <div class="visual-card">
      <div class="visual-header">
        <span class="visual-title">&#128202; Figure 1.5: 4-Panel Step-by-Step Evolution of Lloyd&#39;s K-Means Algorithm</span>
        <span class="visual-badge verified">&#10003; Verified Vector SVG</span>
      </div>
      <div class="svg-wrapper">
        __SVG_KMEANS_STEPS_PANEL__
      </div>
      <p class="visual-caption">
        <strong>Figure 1.5:</strong> Visual walkthrough of Lloyd&#39;s algorithm across 4 progressive panels: (1) Random initialization of centroids &mu;<sub>1</sub> and &mu;<sub>2</sub>, (2) Voronoi partition assigning points to their nearest center, (3) Centroid migration to cluster centers of mass, and (4) Stable convergence where assignments solidify and centroids freeze.
      </p>
    </div>

    <div class="callout-card callout-warn">
      <div class="callout-title">&#9888; The Local Optima Trap</div>
      <p>
        Because K-Means optimizes via greedy coordinate descent, it is guaranteed to converge, but <strong>only to a local optimum</strong>, not necessarily the global optimum. Bad initial seeds can trap the algorithm in a poor partition. To solve this, scikit-learn runs K-Means multiple times with different initial seeds (controlled by parameter <code>n_init</code>, default 10 or 'auto') and selects the run with the lowest total inertia!
      </p>
    </div>
  </section>

"""
