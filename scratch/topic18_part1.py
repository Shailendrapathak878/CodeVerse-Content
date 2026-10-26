# Topic 18 - Part 1: Hero, TOC, Sections 01 - 05

PART1_HTML = """
  <div class="container">
    <!-- Hero Header -->
    <header class="hero-header">
      <div class="hero-badge">
        <span>&#9670;</span> CodeVerse Machine Learning Track &bull; Topic 18
      </div>
      <h1 class="hero-title">Anomaly Detection &bull; Spotting the Unusual</h1>
      <p class="hero-subtitle">
        A complete, beginner-friendly, and mathematically grounded guide to identifying rare events, fraud, system failures, and extreme outliers. Master Z-Score, IQR, Isolation Forest, Local Outlier Factor (LOF), and One-Class SVM from intuitive concepts to production scikit-learn pipelines.
      </p>
      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <span class="hero-meta-label">Curriculum Depth</span>
          <span class="hero-meta-val">20 Complete Sections</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Visual Systems</span>
          <span class="hero-meta-val">16 Verified Vector Diagrams</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Executable Labs</span>
          <span class="hero-meta-val">Complete Python Workflows</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Verified Tech Stack</span>
          <span class="hero-meta-val">scikit-learn 1.9 &bull; SciPy 1.17</span>
        </div>
      </div>
    </header>

    <!-- Table of Contents -->
    <nav class="toc-card" aria-label="Curriculum Navigation">
      <div class="toc-title">
        <span>&#9776;</span> Curriculum Table of Contents
      </div>
      <ul class="toc-grid">
        <li><a class="toc-link" href="#sec-01"><span class="toc-num">01</span> Introduction to Anomaly Detection</a></li>
        <li><a class="toc-link" href="#sec-02"><span class="toc-num">02</span> Real-World Applications</a></li>
        <li><a class="toc-link" href="#sec-03"><span class="toc-num">03</span> Anomaly vs Outlier vs Noise</a></li>
        <li><a class="toc-link" href="#sec-04"><span class="toc-num">04</span> Types of Anomaly Detection</a></li>
        <li><a class="toc-link" href="#sec-05"><span class="toc-num">05</span> Anomaly Detection vs Classification vs Clustering</a></li>
        <li><a class="toc-link" href="#sec-06"><span class="toc-num">06</span> Univariate vs Multivariate Anomalies</a></li>
        <li><a class="toc-link" href="#sec-07"><span class="toc-num">07</span> Statistical Method 1: Z-Score</a></li>
        <li><a class="toc-link" href="#sec-08"><span class="toc-num">08</span> Statistical Method 2: IQR Boxplot</a></li>
        <li><a class="toc-link" href="#sec-09"><span class="toc-num">09</span> Machine Learning-Based Approaches</a></li>
        <li><a class="toc-link" href="#sec-10"><span class="toc-num">10</span> Isolation Forest (iForest)</a></li>
        <li><a class="toc-link" href="#sec-11"><span class="toc-num">11</span> Local Outlier Factor (LOF)</a></li>
        <li><a class="toc-link" href="#sec-12"><span class="toc-num">12</span> One-Class SVM</a></li>
        <li><a class="toc-link" href="#sec-13"><span class="toc-num">13</span> Master Algorithm Comparison</a></li>
        <li><a class="toc-link" href="#sec-14"><span class="toc-num">14</span> Data Preprocessing & Scaling</a></li>
        <li><a class="toc-link" href="#sec-15"><span class="toc-num">15</span> Evaluating Anomaly Detectors</a></li>
        <li><a class="toc-link" href="#sec-16"><span class="toc-num">16</span> Choosing Thresholds & Alert Costs</a></li>
        <li><a class="toc-link" href="#sec-17"><span class="toc-num">17</span> Common Mistakes & Limitations</a></li>
        <li><a class="toc-link" href="#sec-18"><span class="toc-num">18</span> Complete Practical Project</a></li>
        <li><a class="toc-link" href="#sec-19"><span class="toc-num">19</span> Quick Revision & Glossary</a></li>
        <li><a class="toc-link" href="#sec-20"><span class="toc-num">20</span> Self-Check Quiz & Interview Q&A</a></li>
      </ul>
    </nav>

    <!-- SECTION 01 -->
    <section class="content-section" id="sec-01">
      <div class="section-tag">Section 01 &bull; Foundational Intuition</div>
      <h2 class="section-title">Introduction to Anomaly Detection</h2>
      <p class="section-intro">
        In machine learning, we spend most of our time training models on common patterns. But what happens when the most valuable piece of information in your dataset is the single observation that <em>does not</em> fit the pattern?
      </p>

      <h3>1. What is an Observation?</h3>
      <p>
        In tabular data, an <strong>observation</strong> (also called a data point, sample, or record) is a single measured entity represented by a set of feature values. For example, in a banking system, one observation is a single card swipe described by:
      </p>
      <ul>
        <li><code>amount</code> = ₹450</li>
        <li><code>hour_of_day</code> = 14 (2:00 PM)</li>
        <li><code>merchant_type</code> = Grocery</li>
        <li><code>distance_from_home</code> = 1.2 km</li>
      </ul>

      <h3>2. What is "Normal" Behavior?</h3>
      <p>
        Across thousands of cardholders, the vast majority (99% or more) follow consistent habits. A college student buys lunch, refuels their scooter, pays an electricity bill, or buys books online. These predictable, repetitive data points establish the <strong>baseline of normality</strong>.
      </p>

      <div class="card card-def">
        <div class="card-title">&#128214; Formal Definition: Anomaly</div>
        An <strong>anomaly</strong> is an observation or pattern of observations that deviates so substantially from the established baseline of normal data that it arouses suspicion that it was generated by a different underlying mechanism.
      </div>

      <h3>3. Everyday Examples of Anomalies</h3>
      <ul>
        <li><strong>Banking:</strong> An account that normally makes ₹100–₹2,000 grocery transactions suddenly has a single charge of ₹5,00,000 for luxury watches at 3:30 AM in another country.</li>
        <li><strong>Server Infrastructure:</strong> A cloud server typically runs at 15%–35% CPU utilization. At 04:12 UTC, CPU utilization spikes to 99.8% and stays pinned for 45 minutes without an increase in user web requests.</li>
        <li><strong>Industrial Sensors:</strong> A factory temperature probe on a cooling pipe that consistently reads 18°C–24°C suddenly reports 210°C.</li>
        <li><strong>Cybersecurity:</strong> An employee account that typically transfers 5 MB of documents per day suddenly downloads 18 GB of encrypted source code archives over an external SSH connection.</li>
      </ul>

      <div class="card card-warn">
        <div class="card-title">&#9888; Critical Beginner Truth: Anomalies Are Not Always Bad!</div>
        An anomaly is simply <strong>statistically or structurally unusual</strong>. It is <em>not</em> automatically fraudulent, broken, or malicious!
        <br><br>
        For instance, a sudden ₹5,00,000 transaction might be a user buying their dream family car. A website traffic spike of 500% could be a viral social media mention bringing legitimate customers. An anomaly detector raises a <strong>flag for investigation</strong>; human judgment or downstream domain rules decide whether the event is harmful or beneficial.
      </div>

      <!-- VISUAL 1.1 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.1: Normal Observations vs Anomalous Outliers</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_ANOMALY_INTRO__
        <div class="visual-caption">
          <strong>Figure 1.1:</strong> In 2D feature space (Transaction Amount vs Velocity), over 95% of ordinary points form a tight, predictable cluster (teal). Three distinct anomalies are highlighted in red: an individual feature extreme (₹5,00,000 amount), an extreme velocity spike (45 tx/hour), and a joint multivariate anomaly.
        </div>
      </div>
    </section>

    <!-- SECTION 02 -->
    <section class="content-section" id="sec-02">
      <div class="section-tag">Section 02 &bull; Industry Landscape</div>
      <h2 class="section-title">Real-World Applications</h2>
      <p class="section-intro">
        Why does anomaly detection receive so much investment across enterprise industries? Because the cost of missing an anomaly is often catastrophic, while the cost of catching it early is a saved business.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Industry Domain</th>
              <th>Observed Data Features</th>
              <th>Anomalous Event Example</th>
              <th>Why Automated Detection is Vital</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Financial Fraud</strong></td>
              <td>Amount, location, merchant, time delta, swipe speed</td>
              <td>Card used simultaneously at an ATM in Mumbai and a POS terminal in London</td>
              <td>Prevents multi-million rupee losses before cardholders even notice unauthorized charges.</td>
            </tr>
            <tr>
              <td><strong>Cybersecurity</strong></td>
              <td>Port scans, packet volumes, login failures, byte counts</td>
              <td>Single IP attempting 10,000 SSH logins per second (Brute Force)</td>
              <td>Blocks DDoS attacks, ransomware infiltration, and credential stuffing in real time.</td>
            </tr>
            <tr>
              <td><strong>Manufacturing QA</strong></td>
              <td>High-resolution camera images, weld dimensions, ultrasonic echoes</td>
              <td>Micro-crack or uneven paint thickness on a car chassis assembly line</td>
              <td>Prevents defective vehicles from reaching dealerships, saving costly safety recalls.</td>
            </tr>
            <tr>
              <td><strong>IoT Sensor Telemetry</strong></td>
              <td>Vibration, temperature, oil pressure, motor RPM</td>
              <td>High-frequency harmonic vibration in a wind turbine gearbox</td>
              <td>Enables <em>predictive maintenance</em>: replace a ₹5,000 bearing before the ₹50,00,000 turbine shatters.</td>
            </tr>
            <tr>
              <td><strong>Healthcare Telemetry</strong></td>
              <td>ECG heartbeat rhythms, blood oxygen (SpO2), systolic blood pressure</td>
              <td>Sudden irregular ventricular arrhythmia during patient sleep</td>
              <td>Immediately alerts intensive care nurses before cardiac arrest occurs.</td>
            </tr>
            <tr>
              <td><strong>Cloud Infrastructure</strong></td>
              <td>API latency, error 500 rates, memory allocation, active database threads</td>
              <td>Sudden memory leak consuming 100% of RAM after a new microservice release</td>
              <td>Auto-restarts crashing pods and alerts on-call DevOps engineers before customers suffer downtime.</td>
            </tr>
            <tr>
              <td><strong>E-Commerce & Retail</strong></td>
              <td>Product order velocity, coupon application rate, refund requests</td>
              <td>Bot network redeeming a single promotional discount code 40,000 times in 2 minutes</td>
              <td>Stops promotional abuse and inventory depletion by malicious bot scrapers.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card card-info">
        <div class="card-title">&#128161; Alert Triage in Production</div>
        In production systems, machine learning anomaly detectors rarely take destructive actions automatically. Instead, they assign an <strong>anomaly score</strong>. High-scoring events trigger automated safeguards (such as requiring Two-Factor Authentication or rate-limiting an API key) while filing an urgent ticket for human investigators.
      </div>
    </section>

    <!-- SECTION 03 -->
    <section class="content-section" id="sec-03">
      <div class="section-tag">Section 03 &bull; Terminology & Taxonomy</div>
      <h2 class="section-title">Anomaly vs Outlier vs Noise</h2>
      <p class="section-intro">
        Beginners frequently use the terms "outlier", "anomaly", and "noise" as if they were identical synonyms. In professional machine learning, they describe distinct phenomena with very different consequences.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Concept</th>
              <th>Core Definition</th>
              <th>Action Required</th>
              <th>Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Noise</strong></td>
              <td>Random low-level variation, electrical interference, or rounding errors inherent in measurement tools.</td>
              <td>Filter out or ignore (e.g., smoothing, moving averages). Does <em>not</em> represent a new process.</td>
              <td>A digital thermometer reading 21.01°C, then 20.98°C, then 21.03°C in a steady room.</td>
            </tr>
            <tr>
              <td><strong>Outlier</strong></td>
              <td>A strictly geometric or statistical term: any point situated far away from the rest of the sample distribution.</td>
              <td>Investigate mathematically. It may be legitimate data, a typo, or an anomaly.</td>
              <td>A survey where average height is 170 cm, but one respondent is 215 cm (a professional basketball player).</td>
            </tr>
            <tr>
              <td><strong>Anomaly</strong></td>
              <td>A data point generated by an <em>abnormal, unintended, or rare mechanism</em> that warrants domain action.</td>
              <td>Flag for immediate operational review, investigation, or automated intervention.</td>
              <td>A survey respondent recording an age of 950 years (a data corruption bug or troll response).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Contextual and Collective Anomalies</h3>
      <p>
        Anomalies are not always extreme numbers in isolation. They fall into three structural categories:
      </p>
      <ol>
        <li><strong>Point Anomalies:</strong> A single data point is extreme on its own (e.g., a credit card charge of ₹10,00,000 when the user's previous max was ₹5,000).</li>
        <li><strong>Contextual Anomalies:</strong> The value itself is completely normal, but <em>abnormal within its specific context</em>:
          <div class="card card-analogy">
            <div class="card-title">&#9728;&#65039; Contextual Example: Temperature in Delhi</div>
            A temperature reading of <strong>32°C (90°F)</strong> is completely ordinary on a sunny afternoon in June.
            <br>
            However, that same reading of <strong>32°C at 3:00 AM in the middle of January</strong> is an alarming contextual anomaly—either the sensor has caught fire or the room's heater thermostat is stuck on maximum!
          </div>
        </li>
        <li><strong>Collective Anomalies:</strong> A collection of related data points is anomalous as an aggregate sequence, even if every individual reading is within legal bounds (e.g., a credit card being charged ₹5 every 3 seconds for 20 minutes continuously).</li>
      </ol>

      <!-- VISUAL 1.2 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.2: Four Quadrants &bull; Normal, Noise, Outlier, and Anomaly</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_ANOMALY_VS_OUTLIER_VS_NOISE__
        <div class="visual-caption">
          <strong>Figure 1.2:</strong> Visual comparison of data phenomena. Normal data forms the core population; Noise consists of small harmless jitters; Outliers are geometrically distant points; Anomalies represent actionable deviations produced by unexpected processes.
        </div>
      </div>
    </section>

    <!-- SECTION 04 -->
    <section class="content-section" id="sec-04">
      <div class="section-tag">Section 04 &bull; Problem Formulations</div>
      <h2 class="section-title">Types of Anomaly Detection</h2>
      <p class="section-intro">
        How you build an anomaly detection system depends fundamentally on one question: <strong>Do you have clean, reliable labels of anomalies in your historical training data?</strong>
      </p>

      <!-- VISUAL 1.3 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.3: Supervised vs Semi-Supervised vs Unsupervised Workflows</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_DETECTION_TYPES__
        <div class="visual-caption">
          <strong>Figure 1.3:</strong> The three operating regimes of anomaly detection. Supervised treats it as imbalanced classification; Semi-Supervised learns an envelope around clean normal samples (Novelty Detection); Unsupervised isolates rare points from uncurated production data.
        </div>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Learning Regime</th>
              <th>Training Data Required</th>
              <th>Common Algorithms</th>
              <th>Best Use Cases</th>
              <th>Primary Pitfall</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Supervised</strong></td>
              <td>Both normal ($y=0$) and anomalous ($y=1$) samples are accurately labeled.</td>
              <td>XGBoost, Random Forest, LightGBM with class weighting.</td>
              <td>Known fraud patterns where millions of past verified transactions have been audited.</td>
              <td>Blind to <em>novel attacks</em>: if hackers invent a new technique, a supervised model will classify it as normal!</td>
            </tr>
            <tr>
              <td><strong>Semi-Supervised (Novelty Detection)</strong></td>
              <td>Exclusively <strong>clean normal</strong> data ($y=0$). Zero anomalies in training.</td>
              <td>One-Class SVM, Autoencoders, Elliptic Envelope.</td>
              <td>Manufacturing assembly lines where every tested factory part is certified pristine before shipping.</td>
              <td>If training data accidentally contains undetected defects, the model will learn them as normal!</td>
            </tr>
            <tr>
              <td><strong>Unsupervised (Outlier Detection)</strong></td>
              <td>Completely <strong>unlabeled</strong> raw data. Assumed to be mostly normal with &lt; 5% hidden anomalies.</td>
              <td>Isolation Forest, Local Outlier Factor (LOF), DBSCAN, Z-Score, IQR.</td>
              <td>Real-world production data where auditing millions of rows manually is too expensive.</td>
              <td>May flag harmless statistical extremes (like Bill Gates's bank account) as malicious fraud.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 05 -->
    <section class="content-section" id="sec-05">
      <div class="section-tag">Section 05 &bull; Machine Learning Taxonomy</div>
      <h2 class="section-title">Anomaly Detection vs Classification vs Clustering</h2>
      <p class="section-intro">
        Students often ask: <em>"Why don't we just use standard classification or clustering to find anomalies?"</em> Let's see why anomaly detection is a distinct third paradigm.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Classification</th>
              <th>Clustering</th>
              <th>Anomaly Detection</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Core Question</strong></td>
              <td>"Which of these known classes does this point belong to?"</td>
              <td>"Which natural cluster does this point group with?"</td>
              <td>"Does this point conform to the expected normal distribution?"</td>
            </tr>
            <tr>
              <td><strong>Class Balance</strong></td>
              <td>Usually balanced or moderately imbalanced (e.g., 60/40 or 90/10).</td>
              <td>Expects clusters with substantial sample support.</td>
              <td><strong>Extremely imbalanced</strong>: anomalies are 0.01% to 2% of the dataset!</td>
            </tr>
            <tr>
              <td><strong>Unseen Behaviors</strong></td>
              <td>Forces every new point into one of the pre-trained classes.</td>
              <td>Assigns every point to the nearest cluster centroid.</td>
              <td>Explicitly flags points that fall outside all known clusters or envelopes.</td>
            </tr>
            <tr>
              <td><strong>Output</strong></td>
              <td>Predicted class label &amp; class probability.</td>
              <td>Cluster assignment ID ($k=0, 1, 2\dots$).</td>
              <td>Continuous anomaly score &amp; binary decision (Inlier vs Outlier).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- VISUAL 1.4 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.4: Decision Objectives &bull; Classification vs Clustering vs Anomaly Detection</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_ANOMALY_VS_CLASS_VS_CLUSTER__
        <div class="visual-caption">
          <strong>Figure 1.4:</strong> Visualizing the different learning goals. Classification constructs separating boundaries between labeled groups; Clustering groups dense clumps; Anomaly Detection constructs an envelope around high-density normality and flags isolated points.
        </div>
      </div>

      <div class="card card-purple">
        <div class="card-title">&#128302; The "Small Cluster" Trap in Clustering</div>
        Beginners often think: <em>"If I run K-Means or DBSCAN, any small cluster is an anomaly!"</em>
        <br><br>
        This is a dangerous misconception. A small, distant cluster of 15 users might simply be a legitimate niche user group (e.g., night-shift doctors purchasing medical supplies at 4:00 AM). Furthermore, genuine anomalies can occur <strong>inside</strong> a large cluster (e.g., a normal transaction amount executed with an abnormal IP address). Ordinary clustering algorithms have no mathematical concept of an "anomaly"—they simply minimize within-cluster distance across all points!
      </div>
    </section>
"""
