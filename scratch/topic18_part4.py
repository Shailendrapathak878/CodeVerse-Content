# Topic 18 - Part 4: Sections 16 - 20 & Footer (Clean Unicode/HTML Math)

PART4_HTML = """
    <!-- SECTION 16 -->
    <section class="content-section" id="sec-16">
      <div class="section-tag">Section 16 &bull; Operational Decision Engineering</div>
      <h2 class="section-title">Choosing an Anomaly Threshold</h2>
      <p class="section-intro">
        Machine learning models do not output a binary yes/no decision directly. Instead, they output a continuous <strong>anomaly score</strong>. Deciding where to place the decision cutoff threshold is a business decision governed by the asymmetric costs of false alarms versus missed attacks.
      </p>

      <h3>1. The Asymmetric Cost of Errors</h3>
      <p>
        In anomaly detection, the cost of a False Positive (FP) is almost never equal to the cost of a False Negative (FN):
      </p>
      <ul>
        <li><strong>Financial Fraud:</strong>
          <br>&bull; <em>False Negative (Miss):</em> A stolen card executes a ₹5,00,000 transaction. The bank suffers a ₹5,00,000 chargeback loss.
          <br>&bull; <em>False Positive (False Alarm):</em> A legitimate user's card is temporarily declined at a restaurant. Cost: ₹5 for an SMS alert and slight customer annoyance.
          <br>&bull; <strong>Strategy:</strong> Tolerate more false alarms to drive Recall as close to 100% as possible.
        </li>
        <li><strong>Nuclear Plant or Airplane Engine Shutdown:</strong>
          <br>&bull; <em>False Positive:</em> Shutting down a commercial passenger flight in mid-air costs ₹25,00,000 in emergency diversions and passenger panic.
          <br>&bull; <strong>Strategy:</strong> Set a conservative threshold requiring overwhelming statistical proof before halting an operational system.
        </li>
      </ul>

      <!-- VISUAL 1.14 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.14: Decision Function Threshold vs Operational Alert Volume</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_THRESHOLD_SWEEP__
        <div class="visual-caption">
          <strong>Figure 1.14:</strong> Measured threshold sweep across Isolation Forest decision scores. Moving the threshold from -0.20 to +0.15 increases alert volume from 0.8% to 34.4%. Setting threshold &approx; 0.0 isolates the intended 5% contamination target.
        </div>
      </div>
    </section>

    <!-- SECTION 17 -->
    <section class="content-section" id="sec-17">
      <div class="section-tag">Section 17 &bull; Practical Pitfalls</div>
      <h2 class="section-title">Common Mistakes and Limitations</h2>
      <p class="section-intro">
        Avoid these 14 common pitfalls that trap beginners and junior machine learning engineers when deploying anomaly detection systems.
      </p>

      <!-- Mistake 1 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 1: Treating Every Outlier as an Error or Fraud</div>
        <p>Assuming that because a data point is far from the mean, it must be malicious, corrupt, or broken.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: AUTOMATIC DELETION</div>
            <code>df = df[df['z_score'] &lt; 3] # Blindly dropping high spenders!</code>
            <p>Automatically deletes VIP high-value customers who legitimately purchase expensive goods.</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: CONTEXTUAL TRIAGE</div>
            <code>df['is_suspicious'] = (z_score &gt; 3) &amp; (~user.is_verified_vip)</code>
            <p>Separates extreme legitimate users from unverified fraudulent actors.</p>
          </div>
        </div>
      </div>

      <!-- Mistake 2 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 2: Evaluating Imbalanced Data with Simple Accuracy</div>
        <p>Reporting 99.8% accuracy on a fraud dataset and assuming the model is world-class.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: ACCURACY REPORTING</div>
            <code>print("Accuracy:", accuracy_score(y_true, y_pred)) # 99.9%</code>
            <p>Hides the fact that the model missed 100% of all actual fraud instances.</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: PRECISION-RECALL &amp; F1</div>
            <code>print("Precision:", precision_score(y_true, y_pred))</code>
            <code>print("Recall:", recall_score(y_true, y_pred))</code>
            <p>Focuses directly on detection rate (Recall) and false alarm burden (Precision).</p>
          </div>
        </div>
      </div>

      <!-- Mistake 3 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 3: Omitting Feature Scaling in Distance-Based Algorithms</div>
        <p>Running LOF, k-NN, or One-Class SVM on unscaled raw features.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: UNSCALED DISTANCES</div>
            <code>lof = LocalOutlierFactor().fit_predict(df[['amount_inr', 'time_sec']])</code>
            <p>Amount (range ₹100k) completely dwarfs time (range 10s), blinding the model to time spikes.</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: ROBUST SCALING</div>
            <code>X_scaled = RobustScaler().fit_transform(df[['amount', 'time']])</code>
            <code>lof = LocalOutlierFactor().fit_predict(X_scaled)</code>
            <p>Puts all features on an identical quartile-normalized scale.</p>
          </div>
        </div>
      </div>

      <!-- Mistake 4 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 4: Treating Contamination as Ground Truth</div>
        <p>Believing that passing <code>contamination=0.05</code> means exactly 5% of the real world is fraudulent.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: CIRCULAR REASONING</div>
            <p>Setting <code>contamination=0.05</code> and telling executives that exactly 5% of our users are fraudsters.</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: SENSITIVITY CALIBRATION</div>
            <p>Treating contamination purely as an internal threshold tuner to balance investigative capacity.</p>
          </div>
        </div>
      </div>

      <!-- Mistake 5 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 5: Data Leakage in Semi-Supervised Novelty Detection</div>
        <p>Fitting preprocessing scalers on the full dataset containing both train and test anomalies.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: GLOBAL FIT</div>
            <code>X_scaled = scaler.fit_transform(X_all) # Test anomalies corrupt scale!</code>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: PIPELINE DISCIPLINE</div>
            <code>scaler.fit(X_train_clean_normal)</code>
            <code>X_test_scaled = scaler.transform(X_test)</code>
          </div>
        </div>
      </div>

      <!-- Mistake 6 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 6: Ignoring Concept Drift &amp; Seasonal Norms</div>
        <p>Deploying a static model and expecting normal behavior to remain constant over time.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: STATIC MODEL DEPLOYMENT</div>
            <p>Training a model in July and running it during Diwali/Black Friday shopping rushes without updates.</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: ADAPTIVE RETRAINING</div>
            <p>Sliding window retraining with seasonal baseline adjustments.</p>
          </div>
        </div>
      </div>

      <!-- Mistake 7 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 7: Misinterpreting scikit-learn Prediction Labels</div>
        <p>Expecting <code>predict()</code> to return 0 for normal and 1 for anomaly.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: WRONG LABEL ASSUMPTION</div>
            <code>anomalies = df[preds == 1] # INVERTED! +1 means INLIER!</code>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: MEMORIZE CONVENTION</div>
            <code>anomalies = df[preds == -1] # Correct: -1 is OUTLIER</code>
          </div>
        </div>
      </div>

      <!-- Mistake 8 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 8: Using Z-Score on Heavily Skewed Data</div>
        <p>Applying z = (x &minus; &mu;) / &sigma; on power-law distributed quantities (like website page views or income).</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: GAUSSIAN ASSUMPTION</div>
            <p>Z-score flags millions of legitimate long-tail users on Pareto-distributed data.</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: LOG TRANSFORM OR IQR</div>
            <code>z_scores = (np.log1p(x) - np.mean(np.log1p(x))) / np.std(np.log1p(x))</code>
          </div>
        </div>
      </div>

      <!-- Mistake 9 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 9: Using LOF on Ultra-High Dimensional Datasets</div>
        <p>Running Local Outlier Factor on 5,000 raw TF-IDF or genomic features.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: CURSE OF DIMENSIONALITY</div>
            <p>In 5,000D, all Euclidean distances converge to identical values; LOF collapses.</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: PCA/AUTOENCODER FIRST</div>
            <p>Reduce dimensions via PCA or use tree-based Isolation Forest.</p>
          </div>
        </div>
      </div>

      <!-- Mistake 10 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 10: Believing One-Class SVM Works Without Parameter Tuning</div>
        <p>Leaving One-Class SVM on default <code>nu=0.5</code>.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: DEFAULT NU</div>
            <code>oc_svm = OneClassSVM() # Rejects 50% of all normal data!</code>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: CONSERVATIVE NU</div>
            <code>oc_svm = OneClassSVM(nu=0.01, kernel='rbf') # Rejects 1% expected outliers</code>
          </div>
        </div>
      </div>

      <!-- Mistake 11 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 11: Alert Fatigue from Uncalibrated Thresholds</div>
        <p>Generating 10,000 alerts per day for a human team that can only inspect 50 cases.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: SENSORS CRYING WOLF</div>
            <p>Investigators ignore all alerts because 99.9% are harmless noise.</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: CAPACITY-BASED TOP-K</div>
            <code>top_alerts = df.sort_values('anomaly_score').head(50)</code>
          </div>
        </div>
      </div>

      <!-- Mistake 12 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 12: Missing Contextual Variables</div>
        <p>Evaluating an amount or temperature without its associated time, day of week, or location.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: ISOLATED METRIC</div>
            <p>Evaluating <code>amount</code> without knowing whether it is a business or personal account.</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: ENGINEER RATIOS</div>
            <code>feature = amount / user_historical_average_30d</code>
          </div>
        </div>
      </div>

      <!-- Mistake 13 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 13: Passing Categorical Variables Directly to Distance Models</div>
        <p>Applying arbitrary integer label encoding (<code>Grocery=1, Gas=2, Luxury=3</code>) before computing distances.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: ARBITRARY EUCLIDEAN DISTANCE</div>
            <p>Imposes an artificial mathematical distance (Luxury is 2x further from Grocery than Gas!).</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: TARGET ENCODING OR ONE-HOT</div>
            <p>Use Target Encoding, One-Hot Encoding, or frequency encoding.</p>
          </div>
        </div>
      </div>

      <!-- Mistake 14 -->
      <div class="mistake-card">
        <div class="mistake-title">&#9888; Mistake 14: Confusing Synthetic Benchmark Metrics with Production Guarantees</div>
        <p>Assuming that achieving 95% F1 on synthetic Gaussian clusters guarantees 95% fraud detection in a real bank.</p>
        <div class="mistake-grid">
          <div class="mistake-bad">
            <div class="mistake-bad-title">&#10006; BAD: OVERCONFIDENCE</div>
            <p>Synthetic benchmarks have clean separation; real attackers actively evade features.</p>
          </div>
          <div class="mistake-good">
            <div class="mistake-good-title">&#10004; GOOD: ADVERSARIAL REALISM</div>
            <p>Treat synthetic labs as algorithmic sanity checks; deploy with continuous human-in-the-loop review.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 18 -->
    <section class="content-section" id="sec-18">
      <div class="section-tag">Section 18 &bull; End-to-End Practical Mini-Project</div>
      <h2 class="section-title">Complete Practical Project: Unusual Transaction Detection with Machine Learning</h2>
      <p class="section-intro">
        Let us build and evaluate a complete, realistic, and leakage-safe fraud anomaly detection system using Python and scikit-learn.
      </p>

      <div class="card card-warn">
        <div class="card-title">&#9888; Educational Disclaimer</div>
        This mini-project uses a synthetic dataset constructed with known statistical distributions to demonstrate model mechanics. It is designed for educational understanding and must not be used as an off-the-shelf production banking fraud system without extensive domain feature engineering and compliance auditing.
      </div>

      <h3>1. Dataset Specification</h3>
      <ul>
        <li><strong>Total Transactions:</strong> 500</li>
        <li><strong>Normal Transactions (475 samples):</strong>
          <br>&bull; <code>amount</code>: Normal distribution with mean ₹1,200, std ₹350.
          <br>&bull; <code>frequency</code>: Normal distribution with mean 4 tx/hour, std 1.5.
        </li>
        <li><strong>Injected Anomalies (25 samples &bull; 5% Contamination):</strong>
          <br>&bull; <em>15 High-Amount Spikes:</em> Amounts ranging from ₹5,500 to ₹15,000.
          <br>&bull; <em>10 Velocity Bursts:</em> Frequencies ranging from 12 to 42 tx/hour with modest amounts (invisible to single-variable amount rules!).
        </li>
      </ul>

      <!-- VISUAL 1.15 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.15: Transaction Dataset Scatter Plot &bull; Normal Cluster vs Dual-Mode Anomalies</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_TRANSACTION_PROJECT__
        <div class="visual-caption">
          <strong>Figure 1.15:</strong> Real project scatter plot. The Isolation Forest successfully isolates both High-Amount Spikes (horizontal outliers) and Velocity Bursts (vertical outliers) while preserving the 473 normal users in the dense lower-left quadrant.
        </div>
      </div>

      <div class="code-container">
        <div class="code-header">
          <span>Python &bull; Complete Executable Mini-Project</span>
          <span>Verified Execution</span>
        </div>
        <pre><code>import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# 1. Reproducible Synthetic Generation
np.random.seed(42)
n_normal = 475
n_anom = 25

# 475 Normal Users
amount_norm = np.clip(np.random.normal(1200, 350, n_normal), 100, 3000)
freq_norm = np.clip(np.random.normal(4, 1.5, n_normal), 1, 10)
X_norm = np.column_stack([amount_norm, freq_norm])

# 25 Injected Anomalies (Dual Mode: High Amount + Velocity Bursts)
amt_anom_1 = np.array([3200, 3400, 5500, 6200, 7100, 7800, 8500, 9200, 
                       9800, 10500, 11200, 12000, 13500, 14200, 15000], dtype=float)
freq_anom_1 = np.array([4.2, 3.8, 2.5, 4.0, 1.8, 3.2, 2.9, 4.5, 3.0, 2.1, 1.5, 3.8, 2.2, 4.1, 1.9], dtype=float)

amt_anom_2 = np.array([850, 1200, 1400, 1600, 1900, 2100, 2300, 2500, 2700, 2800], dtype=float)
freq_anom_2 = np.array([11.5, 12.0, 15.0, 18.5, 22.0, 26.0, 29.5, 34.0, 38.0, 42.0], dtype=float)

X_anom = np.vstack([
    np.column_stack([amt_anom_1, freq_anom_1]),
    np.column_stack([amt_anom_2, freq_anom_2])
])

X = np.vstack([X_norm, X_anom])
y_true = np.array([0] * n_normal + [1] * n_anom)  # 0=Normal, 1=Anomaly

# 2. Fit Isolation Forest with contamination=0.05
iso = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
raw_preds = iso.fit_predict(X)
# Convert scikit-learn convention (-1: outlier, +1: inlier) to binary (1: anomaly, 0: normal)
y_pred = np.where(raw_preds == -1, 1, 0)

# 3. Comprehensive Evaluation
cm = confusion_matrix(y_true, y_pred)
tn, fp, fn, tp = cm.ravel()
prec = precision_score(y_true, y_pred)
rec = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"Dataset Size: {len(X)} transactions ({n_normal} normal, {n_anom} anomalous)")
print(f"Confusion Matrix: TN={tn}, FP={fp}, FN={fn}, TP={tp}")
print(f"Precision: {prec:.4f} ({prec*100:.2f}%)")
print(f"Recall:    {rec:.4f} ({rec*100:.2f}%)")
print(f"F1-Score:  {f1:.4f}")

# Output:
# Dataset Size: 500 transactions (475 normal, 25 anomalous)
# Confusion Matrix: TN=473, FP=2, FN=2, TP=23
# Precision: 0.9200 (92.00%)
# Recall:    0.9200 (92.00%)
# F1-Score:  0.9200</code></pre>
      </div>

      <h3>Interpretation of Actual Measured Results</h3>
      <ul>
        <li><strong>True Negatives (473):</strong> Out of 475 normal cardholders, 473 transactions cleared seamlessly with zero friction.</li>
        <li><strong>True Positives (23):</strong> The model caught 23 out of the 25 attacks, successfully blocking both massive ₹15,000 spikes and rapid 42 tx/hour bot bursts!</li>
        <li><strong>False Positives (2):</strong> Exactly 2 legitimate users who had slight spending bumps were flagged for Two-Factor SMS confirmation.</li>
        <li><strong>False Negatives (2):</strong> Exactly 2 borderline anomalies near ₹3,200 slipped past the 5% cutoff.</li>
        <li><strong>Precision = 92.00% &amp; Recall = 92.00%:</strong> Demonstrates that multivariate Isolation Forest strikes a formidable balance between fraud interception and customer peace of mind.</li>
      </ul>
    </section>

    <!-- SECTION 19 -->
    <section class="content-section" id="sec-19">
      <div class="section-tag">Section 19 &bull; Revision &amp; Decision Guide</div>
      <h2 class="section-title">Quick Revision and Glossary</h2>
      <p class="section-intro">
        Consolidate your mastery with this executive summary, algorithmic selection tree, and technical glossary.
      </p>

      <h3>1. Seven Core Takeaways</h3>
      <ol>
        <li><strong>Anomalies &ne; Outliers &ne; Noise:</strong> Noise is random jitter; outliers are geometric distances; anomalies are rare events generated by an unexpected process.</li>
        <li><strong>Beware the Accuracy Trap:</strong> On 99.9% normal data, a model that classifies everything as normal has 99.9% accuracy but 0% recall! Always evaluate using Precision, Recall, and F1.</li>
        <li><strong>Z-Score Assumes Gaussian Bell Curves:</strong> Use Z-score only when data is symmetric and unimodal. On skewed data, use IQR or log-transform.</li>
        <li><strong>IQR is Robust to Outliers:</strong> The 1.5 &times; IQR rule uses order statistics that cannot be masked by extreme outliers.</li>
        <li><strong>Isolation Forest Isolates, Not Profiles:</strong> iForest cuts random partitions. Anomalies are isolated near tree roots with short path lengths h(x).</li>
        <li><strong>LOF Masters Variable Density:</strong> When clusters have wildly different spreads, LOF's relative density ratio spots local outliers that global distances miss.</li>
        <li><strong>One-Class SVM Excels at Novelty:</strong> If you only have certified clean normal data, One-Class SVM learns an enclosing RBF kernel envelope.</li>
      </ol>

      <!-- VISUAL 1.16 -->
      <div class="visual-wrapper">
        <div class="visual-header">
          <span class="visual-title">&#128202; Figure 1.16: Anomaly Detection Algorithmic Selection Guide</span>
          <span class="visual-tag">&check; VERIFIED VECTOR SVG</span>
        </div>
        __SVG_DECISION_FLOWCHART__
        <div class="visual-caption">
          <strong>Figure 1.16:</strong> Practical decision tree. Start with Z-score or IQR for single features. For multivariate tabular data, Isolation Forest is the premier first-line baseline. Use LOF for variable densities and One-Class SVM for clean normal-only novelty training.
        </div>
      </div>

      <h3>2. Technical Glossary</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Term</th>
              <th>Technical Definition</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Inlier</strong></td>
              <td>A data point that conforms to the expected normal distribution of the dataset.</td>
            </tr>
            <tr>
              <td><strong>Outlier</strong></td>
              <td>An observation that lies an abnormal distance from other values in a random sample.</td>
            </tr>
            <tr>
              <td><strong>Novelty Detection</strong></td>
              <td>Semi-supervised anomaly detection where the training data is clean and contains zero anomalies.</td>
            </tr>
            <tr>
              <td><strong>Contamination</strong></td>
              <td>The expected proportion of outliers present in an uncurated training dataset.</td>
            </tr>
            <tr>
              <td><strong>Path Length h(x)</strong></td>
              <td>In Isolation Forest, the number of recursive binary splits required to isolate sample x.</td>
            </tr>
            <tr>
              <td><strong>Local Reachability Density</strong></td>
              <td>In LOF, the inverse of the average reachability distance of an observation from its k-nearest neighbors.</td>
            </tr>
            <tr>
              <td><strong>Origin Separation</strong></td>
              <td>In One-Class SVM, mapping data to kernel Hilbert space and separating it from the origin with a hyperplane.</td>
            </tr>
            <tr>
              <td><strong>Outlier Masking</strong></td>
              <td>When an extreme outlier artificially inflates the dataset's standard deviation, pulling its own Z-score down.</td>
            </tr>
            <tr>
              <td><strong>False Alarm Rate</strong></td>
              <td>The proportion of normal observations incorrectly flagged as anomalies (FPR = FP / (FP + TN)).</td>
            </tr>
            <tr>
              <td><strong>Adversarial Drift</strong></td>
              <td>When malicious attackers intentionally modify their behavioral patterns to blend into the normal distribution.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 20 -->
    <section class="content-section" id="sec-20">
      <div class="section-tag">Section 20 &bull; Interactive Knowledge Verification</div>
      <h2 class="section-title">Self-Check Quiz &amp; Interview Questions</h2>
      <p class="section-intro">
        Test your conceptual and practical understanding with these 12 comprehensive interview-style questions. Click each question to expand the complete explanation.
      </p>

      <!-- Q1 -->
      <details class="faq-item">
        <summary class="faq-summary">Q1: Why is an anomaly not automatically an error or fraudulent event?</summary>
        <div class="faq-content">
          <p>An anomaly is purely a <strong>statistical deviation</strong> from the majority baseline. It indicates that the observation was generated under different conditions or by a rare mechanism. In many domains, anomalies represent positive, high-value events: a loyal VIP customer making a massive legitimate purchase, a breakthrough scientific discovery in telescope readings, or a viral product launch. Machine learning models flag <em>unusualness</em>; human domain experts evaluate <em>intent and validity</em>.</p>
        </div>
      </details>

      <!-- Q2 -->
      <details class="faq-item">
        <summary class="faq-summary">Q2: Why does an extreme outlier cause "masking" in the standard Z-score calculation?</summary>
        <div class="faq-content">
          <p>The formula for Z-score is z = (x &minus; &mu;) / &sigma;. Because the mean &mu; and standard deviation &sigma; are calculated using every point in the dataset, an extreme outlier increases the numerator (x &minus; &mu;) linearly, but inflates the standard deviation &sigma; in the denominator through squared differences &Sigma; (x_i &minus; &mu;)&sup2;. This drastically increases the denominator, pulling the Z-score of the outlier down towards the threshold and preventing it from being flagged.</p>
        </div>
      </details>

      <!-- Q3 -->
      <details class="faq-item">
        <summary class="faq-summary">Q3: Why is the IQR method superior to Z-score when analyzing skewed or contaminated data?</summary>
        <div class="faq-content">
          <p>The IQR method relies on <strong>order statistics (percentiles and medians)</strong> rather than sample averages. The median (Q<sub>2</sub>), first quartile (Q<sub>1</sub>), and third quartile (Q<sub>3</sub>) depend solely on the rank ordering of observations. Even if an outlier has a value of ₹100,000,000, the 75th percentile (Q<sub>3</sub>) remains completely unaffected. Therefore, the fences Q<sub>1</sub> &minus; 1.5 &times; IQR and Q<sub>3</sub> + 1.5 &times; IQR maintain their robust boundaries regardless of how extreme the outliers are.</p>
        </div>
      </details>

      <!-- Q4 -->
      <details class="faq-item">
        <summary class="faq-summary">Q4: How does Isolation Forest differ conceptually from traditional clustering or density models?</summary>
        <div class="faq-content">
          <p>Traditional methods (like Gaussian Mixture Models, DBSCAN, or LOF) attempt to profile and map the dense, normal regions of data first, flagging anything outside as an anomaly. This is computationally expensive (O(n&sup2;)). <strong>Isolation Forest</strong> isolates anomalies directly by exploiting their vulnerability: because anomalies are few and structurally distant, random recursive binary cuts isolate them in very few splits (short tree depth h(x)). It operates in linear time O(t &times; n log n), making it far faster.</p>
        </div>
      </details>

      <!-- Q5 -->
      <details class="faq-item">
        <summary class="faq-summary">Q5: What do scikit-learn's `predict()` and `decision_function()` return for Isolation Forest?</summary>
        <div class="faq-content">
          <p>In scikit-learn:
          <br>&bull; <code>predict(X)</code> returns <strong>+1 for inliers (normal)</strong> and <strong>-1 for outliers (anomalous)</strong>.
          <br>&bull; <code>decision_function(X)</code> returns a continuous anomaly score where <strong>negative values represent anomalies</strong> and <strong>positive values represent normal inliers</strong>. The default decision threshold is 0.0.</p>
        </div>
      </details>

      <!-- Q6 -->
      <details class="faq-item">
        <summary class="faq-summary">Q6: Why can global distance methods fail when a dataset contains clusters of different densities?</summary>
        <div class="faq-content">
          <p>Global distance metrics compute distance relative to a single global mean or fixed radius. If a dataset has a very dense cluster C<sub>1</sub> and a very sparse cluster C<sub>2</sub>, a point sitting slightly outside C<sub>1</sub> might have a distance of 3 units, while normal points inside sparse cluster C<sub>2</sub> naturally have distances of 10 units. A global threshold of 5 will incorrectly flag all of cluster C<sub>2</sub> as anomalies while missing the true local anomaly near C<sub>1</sub>. Local Outlier Factor (LOF) solves this by computing the <em>ratio of local densities</em>.</p>
        </div>
      </details>

      <!-- Q7 -->
      <details class="faq-item">
        <summary class="faq-summary">Q7: What is the difference between Novelty Detection and Outlier Detection in scikit-learn LOF?</summary>
        <div class="faq-content">
          <p>In standard <strong>Outlier Detection</strong> (<code>novelty=False</code>), the model detects anomalies within the training dataset itself via <code>fit_predict(X)</code>. It does not support predicting on new unseen test points. In <strong>Novelty Detection</strong> (<code>novelty=True</code>), the model is fitted exclusively on clean, normal training data (<code>fit(X_train)</code>) and subsequently provides <code>predict(X_test)</code> and <code>decision_function(X_test)</code> to score new incoming observations.</p>
        </div>
      </details>

      <!-- Q8 -->
      <details class="faq-item">
        <summary class="faq-summary">Q8: How does One-Class SVM construct a boundary around normal data?</summary>
        <div class="faq-content">
          <p>One-Class SVM projects the input data into a high-dimensional kernel space (via the RBF kernel) where it treats the coordinate origin (0, 0, &hellip;, 0) as the solitary representative of the "outlier" class. It then solves a quadratic programming optimization problem to construct a maximum-margin linear hyperplane separating all the normal training data points from the origin. The hyperparameter &nu; (nu) dictates the allowable trade-off between margin width and the fraction of training points permitted to lie outside.</p>
        </div>
      </details>

      <!-- Q9 -->
      <details class="faq-item">
        <summary class="faq-summary">Q9: Why does feature scaling matter for One-Class SVM and LOF, but not for Isolation Forest?</summary>
        <div class="faq-content">
          <p>LOF and One-Class SVM calculate geometric distances (Euclidean or kernel inner products). If one feature has values from 1 to 1,000,000 and another from 0 to 1, the first feature completely dominates distance calculations, rendering the second feature completely invisible. <strong>Isolation Forest</strong>, by contrast, selects a feature randomly and chooses a split point uniformly between that feature's minimum and maximum. Because tree splits depend only on the <em>ordering</em> of points along an axis, monotonic scaling does not alter the partition structure.</p>
        </div>
      </details>

      <!-- Q10 -->
      <details class="faq-item">
        <summary class="faq-summary">Q10: Why is Accuracy a misleading metric in anomaly detection?</summary>
        <div class="faq-content">
          <p>Because anomaly detection datasets exhibit extreme class imbalance (e.g., 99.9% normal vs 0.1% anomalies). A trivial "dummy" model that predicts every single transaction is normal will achieve 99.9% accuracy while having a 0% Recall rate (missing every single fraud event). Model evaluation must always rely on <strong>Precision</strong> (percentage of alarms that are real), <strong>Recall</strong> (percentage of real anomalies caught), and <strong>F1-score</strong> or Precision-Recall AUC.</p>
        </div>
      </details>

      <!-- Q11 -->
      <details class="faq-item">
        <summary class="faq-summary">Q11: What is the trade-off between False Positives (FP) and False Negatives (FN) when adjusting thresholds?</summary>
        <div class="faq-content">
          <p>Lowering the anomaly decision threshold (making the detector more sensitive) catches more subtle anomalies, driving <strong>Recall up and False Negatives down</strong>. However, this inevitably flags more normal observations by mistake, driving <strong>False Positives up (alert fatigue)</strong>. Conversely, raising the threshold makes the detector conservative, reducing false alarms at the cost of missing dangerous anomalies. The optimal threshold is dictated by the asymmetric monetary or human cost of each error type in the specific business domain.</p>
        </div>
      </details>

      <!-- Q12 -->
      <details class="faq-item">
        <summary class="faq-summary">Q12: What is a contextual anomaly and why do traditional 1D threshold gates fail to catch it?</summary>
        <div class="faq-content">
          <p>A contextual anomaly is a data point whose numerical value is within perfectly legal, ordinary bounds, but is anomalous given its <strong>accompanying context</strong> (such as time of day, day of week, or related sensor readings). For example, a credit card charge of ₹800 is normal during the afternoon, but is suspicious at 3:30 AM from an IP address 5,000 km away. Similarly, high engine temperature is normal, but high engine temperature combined with zero oil pressure indicates a catastrophic failure. Single-variable threshold gates evaluate numbers in isolation and cannot detect correlation breakdowns.</p>
        </div>
      </details>
    </section>

    <!-- Chapter Navigation Footer -->
    <footer class="chapter-nav">
      <a class="nav-btn" href="../topic_17/notes.html">
        <span>&larr;</span> Previous: Topic 17 &bull; Dimensionality Reduction
      </a>
      <a class="nav-btn" href="../topic_19/notes.html">
        Next: Topic 19 &bull; Neural Networks &rarr;
      </a>
    </footer>
  </div>
"""
