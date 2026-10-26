"""
Module: topic12_part1.py
Contains Hero, Table of Contents, and Sections 1 to 5 for Topic 12: Decision Trees.
"""

from scratch.topic12_svgs import (
    SVG_DT_HERO,
    SVG_DT_ANATOMY,
    SVG_DT_PREDICTION_PATH,
    SVG_CLASSIFICATION_VS_REGRESSION,
    SVG_CANDIDATE_SPLIT_BEFORE_AFTER
)

PART1_HTML = f"""
    <!-- HERO HEADER CARD -->
    <header class="hero-card">
      <span class="hero-topic-badge">Supervised Machine Learning &bull; Topic 12</span>
      <h1 class="hero-title">Decision Trees: Complete Beginner Guide</h1>
      <p class="hero-subtitle">
        Master one of the most transparent, intuitive, and widely used machine learning models from absolute zero. Learn how hierarchical if-else decision rules partition complex feature spaces, how Gini Impurity and Entropy mathematically guide split selection, how to prune overfit trees, and how to build production-grade scikit-learn classification and regression pipelines.
      </p>

      <div class="meta-bar">
        <span class="meta-pill">&#128218; 23 Comprehensive Sections</span>
        <span class="meta-pill">&#9889; 15 Hand-Crafted Vector Diagrams</span>
        <span class="meta-pill">&#128300; Verified Scikit-Learn Pipelines</span>
        <span class="meta-pill">&#9878; Strict Light Mode Only</span>
        <span class="meta-pill">&#127919; 100% Mobile &amp; Desktop Tested</span>
      </div>
    </header>

    <!-- HERO DIAGRAM -->
    {SVG_DT_HERO}

    <!-- TABLE OF CONTENTS -->
    <nav class="toc-card" aria-label="Topic 12 Table of Contents">
      <div class="toc-title">&#128203; Table of Contents (23 Sections)</div>
      <div class="toc-grid">
        <a href="#sec-01" class="toc-link"><span class="toc-num">01</span><span>Introduction to Decision Trees</span></a>
        <a href="#sec-02" class="toc-link"><span class="toc-num">02</span><span>Anatomy of a Decision Tree</span></a>
        <a href="#sec-03" class="toc-link"><span class="toc-num">03</span><span>How Predictions Are Made</span></a>
        <a href="#sec-04" class="toc-link"><span class="toc-num">04</span><span>Classification vs. Regression</span></a>
        <a href="#sec-05" class="toc-link"><span class="toc-num">05</span><span>How Trees Choose Splits</span></a>
        <a href="#sec-06" class="toc-link"><span class="toc-num">06</span><span>Gini Impurity Explained</span></a>
        <a href="#sec-07" class="toc-link"><span class="toc-num">07</span><span>Entropy &amp; Information Theory</span></a>
        <a href="#sec-08" class="toc-link"><span class="toc-num">08</span><span>Information Gain Arithmetic</span></a>
        <a href="#sec-09" class="toc-link"><span class="toc-num">09</span><span>Gini vs. Entropy Comparison</span></a>
        <a href="#sec-10" class="toc-link"><span class="toc-num">10</span><span>How the Tree Learns (Recursion)</span></a>
        <a href="#sec-11" class="toc-link"><span class="toc-num">11</span><span>Visualizing Trees in Python</span></a>
        <a href="#sec-12" class="toc-link"><span class="toc-num">12</span><span>Orthogonal Decision Boundaries</span></a>
        <a href="#sec-13" class="toc-link"><span class="toc-num">13</span><span>Overfitting, Underfitting &amp; Pruning</span></a>
        <a href="#sec-14" class="toc-link"><span class="toc-num">14</span><span>Feature Importance (MDI)</span></a>
        <a href="#sec-15" class="toc-link"><span class="toc-num">15</span><span>Python Classification Lab</span></a>
        <a href="#sec-16" class="toc-link"><span class="toc-num">16</span><span>Python Regression Lab</span></a>
        <a href="#sec-17" class="toc-link"><span class="toc-num">17</span><span>Evaluating Classification Trees</span></a>
        <a href="#sec-18" class="toc-link"><span class="toc-num">18</span><span>Advantages &amp; Limitations</span></a>
        <a href="#sec-19" class="toc-link"><span class="toc-num">19</span><span>Trees vs. Other Algorithms</span></a>
        <a href="#sec-20" class="toc-link"><span class="toc-num">20</span><span>Real-Life Case Studies</span></a>
        <a href="#sec-21" class="toc-link"><span class="toc-num">21</span><span>Key Visualizations Gallery</span></a>
        <a href="#sec-22" class="toc-link"><span class="toc-num">22</span><span>Common Beginner Mistakes</span></a>
        <a href="#sec-23" class="toc-link"><span class="toc-num">23</span><span>Summary, Glossary &amp; Revision</span></a>
      </div>
    </nav>

    <!-- SECTION 01: INTRODUCTION TO DECISION TREES -->
    <section id="sec-01" class="section-card">
      <span class="section-badge">Section 01</span>
      <h2 class="section-title">Introduction to Decision Trees</h2>
      <p class="section-lead">
        Humans make complex choices every day by asking a sequence of simple questions. A Decision Tree translates this natural reasoning process into a rigorous, mathematical machine learning algorithm.
      </p>

      <div class="callout callout-analogy">
        <div class="callout-title">&#9728;&#65039; Everyday Example: Deciding Whether to Play Outside</div>
        <p>
          Imagine you want to decide whether to play tennis outside on a Saturday morning. You do not compute complex vector angles in your head. Instead, you follow a quick mental flowchart:
        </p>
        <ul style="margin: 8px 0 0 20px; line-height: 1.6;">
          <li><strong>Question 1:</strong> Is it raining outside?
            <br>&bull; <em>If Yes:</em> Stay indoors and read a book (Immediate Decision!).
            <br>&bull; <em>If No:</em> Proceed to Question 2.
          </li>
          <li><strong>Question 2:</strong> Is the wind speed over 30 km/h?
            <br>&bull; <em>If Yes:</em> Stay indoors (too windy for tennis).
            <br>&bull; <em>If No:</em> Go play tennis outside!
          </li>
        </ul>
        <p style="margin-top: 8px;">
          Notice what just happened: by checking individual attributes one by one, you funneled an uncertain situation into a definitive, confident choice. This mental flowchart is exactly how a <strong>Decision Tree</strong> operates!
        </p>
      </div>

      <h3 class="sub-title">1. What is a Decision Tree?</h3>
      <p>
        A <strong>Decision Tree</strong> is a supervised machine learning model that predicts the target value of an unlabelled data point by learning a hierarchy of simple, binary <code>if-else</code> decision rules inferred directly from training features.
      </p>
      <p>
        Unlike complex black-box models (such as deep neural networks), Decision Trees are known as <strong>white-box models</strong>: their entire internal logic can be visually drawn as an intuitive flowchart that non-technical stakeholders, auditors, and doctors can easily understand, verify, and critique.
      </p>

      <h3 class="sub-title">2. Fundamental Vocabulary Every Beginner Must Know</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th style="width: 25%;">Technical Term</th>
              <th style="width: 35%;">Engineering Definition</th>
              <th style="width: 40%;">Everyday Student Analogy</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Feature (Input, X)</strong></td>
              <td>An individual measurable property or variable of an observation used to inform predictions.</td>
              <td>A student's weekly study hours (e.g. 5.5 hours) or attendance percentage (e.g. 85%).</td>
            </tr>
            <tr>
              <td><strong>Target (Label, y)</strong></td>
              <td>The true outcome or quantity the algorithm seeks to predict from the input features.</td>
              <td>Whether the student passed the final exam (1 = Pass, 0 = Fail).</td>
            </tr>
            <tr>
              <td><strong>Decision Rule</strong></td>
              <td>A logical condition testing a feature against a numerical threshold (e.g., <code>x<sub>j</sub> &le; threshold</code>).</td>
              <td>"Did the student attend at least 75% of class lectures?"</td>
            </tr>
            <tr>
              <td><strong>Split</strong></td>
              <td>The act of dividing a group of data points into two or more distinct subsets based on a decision rule.</td>
              <td>Separating the classroom into two groups: those with &ge; 6 study hours and those with &lt; 6.</td>
            </tr>
            <tr>
              <td><strong>Prediction (y&#770;)</strong></td>
              <td>The final estimated class or numerical value output by the terminal leaf node of the tree.</td>
              <td>The model estimating that student Alex will Pass with 92% confidence.</td>
            </tr>
            <tr>
              <td><strong>Classification</strong></td>
              <td>Predicting a discrete qualitative category or label.</td>
              <td>Spam vs. Not Spam, Fraud vs. Legitimate, Pass vs. Fail.</td>
            </tr>
            <tr>
              <td><strong>Regression</strong></td>
              <td>Predicting a continuous numerical quantity.</td>
              <td>House sale price in dollars ($), vehicle mileage (MPG), tomorrow's temperature (&deg;C).</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 02: ANATOMY OF A DECISION TREE -->
    <section id="sec-02" class="section-card">
      <span class="section-badge">Section 02</span>
      <h2 class="section-title">Anatomy of a Decision Tree</h2>
      <p class="section-lead">
        In computer science, a tree is upside-down: it grows downward from a single root at the top down to terminal leaves at the bottom. Understanding every component of this hierarchy is crucial.
      </p>

      {SVG_DT_ANATOMY}

      <h3 class="sub-title">1. The Core Structural Elements</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Node Component</th>
              <th>Structural Role</th>
              <th>Visual Representation</th>
              <th>What Happens Inside?</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Root Node</strong></td>
              <td>Topmost entry point (Depth 0)</td>
              <td>Top container box</td>
              <td>Contains 100% of the training dataset. Evaluates the single most informative feature split.</td>
            </tr>
            <tr>
              <td><strong>Internal / Decision Node</strong></td>
              <td>Intermediate decision step</td>
              <td>Middle container boxes</td>
              <td>Evaluates an incoming subset of data on another feature rule and forks into children.</td>
            </tr>
            <tr>
              <td><strong>Branch (Edge)</strong></td>
              <td>Connecting path / outcome</td>
              <td>Directed arrows</td>
              <td>Represents the boolean outcome of a test (e.g. <code>True &rarr; Left</code>, <code>False &rarr; Right</code>).</td>
            </tr>
            <tr>
              <td><strong>Leaf (Terminal Node)</strong></td>
              <td>Final prediction endpoint</td>
              <td>Bottom rounded boxes</td>
              <td>Has no children. Holds final prediction: majority class mode (classification) or mean average (regression).</td>
            </tr>
            <tr>
              <td><strong>Tree Depth</strong></td>
              <td>Length of longest decision path</td>
              <td>Vertical distance levels</td>
              <td>Root is Depth 0. First children are Depth 1. Deeper trees have more splits and higher complexity.</td>
            </tr>
            <tr>
              <td><strong>Subtree</strong></td>
              <td>Autonomous subsection</td>
              <td>Any node + its descendants</td>
              <td>A complete valid decision tree nested underneath any internal decision node.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-info">
        <div class="callout-title">&#128161; Parent vs. Child Relationship</div>
        <p>
          Every split creates a <strong>parent-child relationship</strong>: the node initiating the split is the <em>parent node</em>, and the resulting subsets are its <em>child nodes</em> (commonly referred to as the left child and right child in binary trees). Notice that an internal node is simultaneously a child to its parent above and a parent to the nodes beneath it!
        </p>
      </div>
    </section>

    <!-- SECTION 03: HOW A DECISION TREE MAKES PREDICTIONS -->
    <section id="sec-03" class="section-card">
      <span class="section-badge">Section 03</span>
      <h2 class="section-title">How a Decision Tree Makes Predictions</h2>
      <p class="section-lead">
        When an unlabelled query point arrives, how does the model assign a prediction? The process is a deterministic traversal from the root down to a single terminal leaf node.
      </p>

      {SVG_DT_PREDICTION_PATH}

      <h3 class="sub-title">Step-by-Step Traversal Walkthrough</h3>
      <p>
        Let us trace the exact decision sequence for a prospective student, <strong>Alex</strong>, who logged <strong>Study Hours = 4.5</strong> and achieved an <strong>Attendance = 82%</strong>:
      </p>

      <div class="calc-box">
        <h4 style="margin: 0 0 10px 0; color: #0284C7;">Step 1: Evaluation at the Root Node (Depth 0)</h4>
        <p style="margin: 0; color: #334155;">
          The Root Node asks: <code>Is Study_Hours &le; 6.5?</code><br>
          We plug in Alex's measured study hours: <code>4.5 &le; 6.5 &rarr; TRUE</code>.<br>
          Because the condition evaluated to <strong>True</strong>, Alex travels down the <strong>Left Branch</strong> to the next node at Depth 1.
        </p>
      </div>

      <div class="calc-box">
        <h4 style="margin: 0 0 10px 0; color: #0284C7;">Step 2: Evaluation at the Internal Decision Node (Depth 1)</h4>
        <p style="margin: 0; color: #334155;">
          The Internal Node asks: <code>Is Attendance &le; 70%?</code><br>
          We check Alex's lecture attendance: <code>82% &le; 70% &rarr; FALSE</code>.<br>
          Because the condition evaluated to <strong>False</strong>, Alex travels down the <strong>Right Branch</strong>.
        </p>
      </div>

      <div class="calc-box" style="border-left: 4px solid #10B981; background: #ECFDF5;">
        <h4 style="margin: 0 0 10px 0; color: #065F46;">Step 3: Reaching the Terminal Leaf Node (Depth 2)</h4>
        <p style="margin: 0; color: #065F46;">
          Alex reaches a leaf node with label <strong>PASS (Class 1)</strong>. The model terminates traversal and outputs the prediction: <strong>Alex is predicted to PASS the exam</strong>.
        </p>
      </div>

      <div class="callout callout-warning">
        <div class="callout-title">&#9888;&#65039; Distinguish Traversal from Training</div>
        <p>
          Do not confuse <strong>inference (making a prediction)</strong> with <strong>training (learning the tree)</strong>! 
          <strong>Inference</strong> is lightning fast (&Oscr;(Tree Depth)): the model simply checks a handful of if-else inequalities until it hits a leaf. 
          <strong>Training</strong> is where the computational work happens: the algorithm must search through all possible features and thresholds to find the best rules.
        </p>
      </div>
    </section>

    <!-- SECTION 04: CLASSIFICATION TREES VS REGRESSION TREES -->
    <section id="sec-04" class="section-card">
      <span class="section-badge">Section 04</span>
      <h2 class="section-title">Classification Trees vs. Regression Trees</h2>
      <p class="section-lead">
        Decision Trees are versatile: they can solve both categorical classification problems and numerical regression tasks. While their tree-growing mechanics are nearly identical, their leaf predictions and split criteria differ fundamentally.
      </p>

      {SVG_CLASSIFICATION_VS_REGRESSION}

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Comparison Aspect</th>
              <th>Classification Tree</th>
              <th>Regression Tree</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Primary Goal</strong></td>
              <td>Assign an instance to a qualitative category</td>
              <td>Estimate a quantitative continuous numerical value</td>
            </tr>
            <tr>
              <td><strong>Target Variable Type</strong></td>
              <td>Discrete (e.g. 0 or 1, Cat or Dog, Disease or Healthy)</td>
              <td>Continuous Float (e.g. $245,500, 32.5 MPG, 98.6 &deg;F)</td>
            </tr>
            <tr>
              <td><strong>What a Leaf Predicts</strong></td>
              <td><strong>Statistical Mode:</strong> The majority class of training points inside that leaf node.</td>
              <td><strong>Arithmetic Mean (y&#772;):</strong> The average target value of training points inside that leaf node.</td>
            </tr>
            <tr>
              <td><strong>Standard Split Criteria</strong></td>
              <td>Gini Impurity, Entropy / Information Gain</td>
              <td>Mean Squared Error (MSE / Variance), Mean Absolute Error (MAE)</td>
            </tr>
            <tr>
              <td><strong>Evaluation Metrics</strong></td>
              <td>Accuracy, Precision, Recall, F1-Score, ROC-AUC</td>
              <td>Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), R&sup2;</td>
            </tr>
            <tr>
              <td><strong>Scikit-Learn Estimator</strong></td>
              <td><code>DecisionTreeClassifier</code></td>
              <td><code>DecisionTreeRegressor</code></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="sub-title">1. Concrete Examples Side by Side</h3>
      <div class="grid-2col">
        <div class="calc-box">
          <h4 style="margin: 0 0 8px 0; color: #1D4ED8;">Classification Example (Pass/Fail)</h4>
          <p style="font-size: 0.92rem; color: #334155;">
            A leaf node ends up with 15 training students: <strong>14 Passed</strong> and <strong>1 Failed</strong>.
            <br>&bull; <em>Leaf Prediction:</em> <strong>PASS</strong> (Mode)
            <br>&bull; <em>Class Probability:</em> 14/15 = <strong>93.3% Pass</strong>, 1/15 = <strong>6.7% Fail</strong>.
          </p>
        </div>

        <div class="calc-box">
          <h4 style="margin: 0 0 8px 0; color: #047857;">Regression Example (House Prices)</h4>
          <p style="font-size: 0.92rem; color: #334155;">
            A leaf node ends up with 4 training homes whose prices are: $200k, $210k, $220k, and $250k.
            <br>&bull; <em>Leaf Prediction:</em> (200 + 210 + 220 + 250) / 4 = <strong>$220.0k USD</strong> (Mean).
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 05: HOW DOES A DECISION TREE CHOOSE A SPLIT? -->
    <section id="sec-05" class="section-card">
      <span class="section-badge">Section 05</span>
      <h2 class="section-title">How Does a Decision Tree Choose a Split?</h2>
      <p class="section-lead">
        At any node, there are hundreds of possible split questions: Should we split on Study Hours &ge; 4.0? Or Study Hours &ge; 6.5? Or Attendance &ge; 80%? How does the algorithm choose the single best split without guessing?
      </p>

      {SVG_CANDIDATE_SPLIT_BEFORE_AFTER}

      <h3 class="sub-title">1. The Principle of Impurity Reduction</h3>
      <p>
        A decision tree evaluates candidate splits by measuring how much each split <strong>purifies</strong> the target classes in the resulting child nodes. The algorithm's fundamental rule is:
      </p>

      <div class="callout callout-def">
        <div class="callout-title">&#128302; Core Splitting Objective</div>
        <p>
          <strong>Select the feature and numerical threshold that maximizes the reduction in node impurity from parent to children!</strong>
          In simple terms: Choose the question that separates the apples from the oranges as cleanly as possible.
        </p>
      </div>

      <h3 class="sub-title">2. Step-by-Step Candidate Evaluation Workflow</h3>
      <ol style="margin-left: 20px; line-height: 1.7; color: #334155;">
        <li><strong>Measure Parent Impurity:</strong> Calculate how mixed the classes currently are in the parent node before any split occurs.</li>
        <li><strong>Scan Every Candidate Feature:</strong> Loop through Feature 1 (Study Hours), Feature 2 (Attendance Pct), and so on.</li>
        <li><strong>Scan Every Candidate Threshold:</strong> Sort the unique feature values and test midpoints between adjacent observations as candidate thresholds.</li>
        <li><strong>Calculate Weighted Child Impurity:</strong> For each candidate split, partition the data into left and right children and compute their combined weighted impurity:
          <div class="formula-block">Weighted Child Impurity = (N_left / N_total) &times; Impurity(Left) + (N_right / N_total) &times; Impurity(Right)</div>
        </li>
        <li><strong>Compute Impurity Reduction (Gain):</strong>
          <div class="formula-block">&Delta; Impurity = Impurity(Parent) - Weighted Child Impurity</div>
        </li>
        <li><strong>Select the Winner:</strong> The candidate threshold producing the <strong>largest impurity drop</strong> is crowned the winning split!</li>
      </ol>
    </section>
"""

def get_part1():
    return PART1_HTML
