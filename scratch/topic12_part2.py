"""
Module: topic12_part2.py
Contains Sections 6 to 10 for Topic 12: Decision Trees.
"""

from scratch.topic12_svgs import (
    SVG_GINI_IMPURITY_CURVE,
    SVG_ENTROPY_CURVE,
    SVG_ENTROPY_VS_GINI,
    SVG_INFORMATION_GAIN_WORKED
)

PART2_HTML = f"""
    <!-- SECTION 06: GINI IMPURITY -->
    <section id="sec-06" class="section-card">
      <span class="section-badge">Section 06</span>
      <h2 class="section-title">Gini Impurity Explained</h2>
      <p class="section-lead">
        Gini Impurity is the default criterion used by scikit-learn to measure the mixture or chaos of target classes inside a node. A lower Gini Impurity signifies a purer, more homogeneous node.
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; Gini Impurity Mathematical Formula</div>
        <div class="formula-math">
          Gini = 1 - &sum;<sub>i=1</sub><sup>C</sup> (p<sub>i</sub>)&sup2;
        </div>
        <div class="formula-legend">
          <div class="legend-item"><span class="legend-sym">C</span><span>Total number of target classes in the dataset.</span></div>
          <div class="legend-item"><span class="legend-sym">p<sub>i</sub></span><span>Proportion of data points in the node belonging to class i.</span></div>
          <div class="legend-item"><span class="legend-sym">(p<sub>i</sub>)&sup2;</span><span>Squared probability of randomly drawing class i.</span></div>
        </div>
      </div>

      <h3 class="sub-title">1. Step-by-Step Worked Numerical Examples</h3>
      <p>
        Let us calculate Gini Impurity by hand for three distinct classroom scenarios:
      </p>

      <div class="calc-box">
        <h4 style="margin: 0 0 8px 0; color: #059669;">Case 1: A Completely Pure Node [10 Pass, 0 Fail]</h4>
        <p style="font-size: 0.93rem; color: #334155;">
          &bull; Class Proportions: p<sub>pass</sub> = 10/10 = <strong>1.0</strong>, p<sub>fail</sub> = 0/10 = <strong>0.0</strong>.<br>
          &bull; Sum of Squared Proportions: (1.0)&sup2; + (0.0)&sup2; = 1.0 + 0.0 = <strong>1.0</strong>.<br>
          &bull; <strong>Gini Calculation:</strong> 1 - 1.0 = <strong>0.0000</strong>.<br>
          <em>Interpretation:</em> The node is 100% pure! There is zero uncertainty—every observation is a Pass.
        </p>
      </div>

      <div class="calc-box">
        <h4 style="margin: 0 0 8px 0; color: #DC2626;">Case 2: A Completely Balanced Node [10 Pass, 10 Fail]</h4>
        <p style="font-size: 0.93rem; color: #334155;">
          &bull; Class Proportions: p<sub>pass</sub> = 10/20 = <strong>0.5</strong>, p<sub>fail</sub> = 10/20 = <strong>0.5</strong>.<br>
          &bull; Sum of Squared Proportions: (0.5)&sup2; + (0.5)&sup2; = 0.25 + 0.25 = <strong>0.50</strong>.<br>
          &bull; <strong>Gini Calculation:</strong> 1 - 0.50 = <strong>0.5000</strong>.<br>
          <em>Interpretation:</em> Maximum impurity for binary classification! An even 50/50 split represents complete randomness.
        </p>
      </div>

      <div class="calc-box">
        <h4 style="margin: 0 0 8px 0; color: #0284C7;">Case 3: An Imbalanced Node [14 Pass, 6 Fail]</h4>
        <p style="font-size: 0.93rem; color: #334155;">
          &bull; Total N = 20. Proportions: p<sub>pass</sub> = 14/20 = <strong>0.7</strong>, p<sub>fail</sub> = 6/20 = <strong>0.3</strong>.<br>
          &bull; Sum of Squared Proportions: (0.7)&sup2; + (0.3)&sup2; = 0.49 + 0.09 = <strong>0.58</strong>.<br>
          &bull; <strong>Gini Calculation:</strong> 1 - 0.58 = <strong>0.4200</strong>.<br>
          <em>Interpretation:</em> Impurity drops from 0.5000 down to 0.4200, reflecting the dominant Pass majority.
        </p>
      </div>

      {SVG_GINI_IMPURITY_CURVE}

      <div class="callout callout-info">
        <div class="callout-title">&#128214; Statistical Interpretation of Gini</div>
        <p>
          Gini Impurity represents the probability that a randomly chosen element from the node would be <strong>incorrectly labelled</strong> if it were randomly classified according to the empirical distribution of class labels in that node. It ranges between <strong>0.0 (perfect purity)</strong> and <strong>1 - (1/C) (maximum chaos)</strong>, which equals <strong>0.50 for binary classification</strong>.
        </p>
      </div>
    </section>

    <!-- SECTION 07: ENTROPY -->
    <section id="sec-07" class="section-card">
      <span class="section-badge">Section 07</span>
      <h2 class="section-title">Entropy &amp; Information Theory</h2>
      <p class="section-lead">
        Borrowed from Claude Shannon's landmark 1948 Information Theory, <strong>Entropy</strong> measures the amount of disorder, uncertainty, or "surprise" contained within a probability distribution.
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; Shannon Entropy Mathematical Formula</div>
        <div class="formula-math">
          H = - &sum;<sub>i=1</sub><sup>C</sup> p<sub>i</sub> log<sub>2</sub>(p<sub>i</sub>)
        </div>
        <div class="formula-legend">
          <div class="legend-item"><span class="legend-sym">H</span><span>Entropy, quantified in units of <strong>bits</strong>.</span></div>
          <div class="legend-item"><span class="legend-sym">p<sub>i</sub></span><span>Proportion of data points in class i.</span></div>
          <div class="legend-item"><span class="legend-sym">log<sub>2</sub></span><span>Base-2 logarithm (representing binary bits of information).</span></div>
        </div>
      </div>

      <div class="callout callout-warning">
        <div class="callout-title">&#9888;&#65039; Mathematical Convention for Zero Probability</div>
        <p>
          In mathematics, <code>log<sub>2</sub>(0)</code> is undefined (approaching -&infin;). However, in information theory, an impossible event contributes zero uncertainty. By standard mathematical convention:
          <br><strong>lim<sub>p &rarr; 0</sub> [ p &times; log<sub>2</sub>(p) ] = 0</strong>.
          Whenever a node has zero samples of a class (p<sub>i</sub> = 0), that term simply contributes <code>0</code> to the sum!
        </p>
      </div>

      <h3 class="sub-title">1. Step-by-Step Worked Numerical Examples</h3>
      <div class="calc-box">
        <h4 style="margin: 0 0 8px 0; color: #059669;">Case 1: A Pure Node [10 Pass, 0 Fail]</h4>
        <p style="font-size: 0.93rem; color: #334155;">
          &bull; p<sub>pass</sub> = 1.0, p<sub>fail</sub> = 0.0.<br>
          &bull; Term 1: 1.0 &times; log<sub>2</sub>(1.0) = 1.0 &times; 0 = 0.<br>
          &bull; Term 2: 0 &times; log<sub>2</sub>(0) = 0 (by convention).<br>
          &bull; <strong>Entropy:</strong> - (0 + 0) = <strong>0.0000 bits</strong>.<br>
          <em>Interpretation:</em> Zero surprise. You can predict the outcome with 100% certainty using 0 bits of information.
        </p>
      </div>

      <div class="calc-box">
        <h4 style="margin: 0 0 8px 0; color: #DC2626;">Case 2: A Balanced Node [10 Pass, 10 Fail]</h4>
        <p style="font-size: 0.93rem; color: #334155;">
          &bull; p<sub>pass</sub> = 0.5, p<sub>fail</sub> = 0.5.<br>
          &bull; Recall: log<sub>2</sub>(0.5) = log<sub>2</sub>(2<sup>-1</sup>) = -1.0.<br>
          &bull; <strong>Entropy:</strong> - [ 0.5 &times; (-1.0) + 0.5 &times; (-1.0) ] = - [ -0.5 - 0.5 ] = <strong>1.0000 bit</strong>.<br>
          <em>Interpretation:</em> Maximum uncertainty for binary outcomes. Exactly 1 bit of information is needed to describe the outcome (like a fair coin flip).
        </p>
      </div>

      <div class="calc-box">
        <h4 style="margin: 0 0 8px 0; color: #7C3AED;">Case 3: An Imbalanced Node [14 Pass, 6 Fail]</h4>
        <p style="font-size: 0.93rem; color: #334155;">
          &bull; p<sub>pass</sub> = 0.7, p<sub>fail</sub> = 0.3.<br>
          &bull; log<sub>2</sub>(0.7) &approx; -0.5146, log<sub>2</sub>(0.3) &approx; -1.7370.<br>
          &bull; Term 1: 0.7 &times; (-0.5146) &approx; -0.3602.<br>
          &bull; Term 2: 0.3 &times; (-1.7370) &approx; -0.5211.<br>
          &bull; <strong>Entropy:</strong> - [ -0.3602 - 0.5211 ] = <strong>0.8813 bits</strong>.<br>
          <em>Interpretation:</em> Uncertainty drops from 1.0000 bit down to 0.8813 bits.
        </p>
      </div>

      {SVG_ENTROPY_CURVE}
    </section>

    <!-- SECTION 08: INFORMATION GAIN -->
    <section id="sec-08" class="section-card">
      <span class="section-badge">Section 08</span>
      <h2 class="section-title">Information Gain Arithmetic</h2>
      <p class="section-lead">
        Now that you understand Entropy, we can define <strong>Information Gain (IG)</strong>: the exact quantity of uncertainty eliminated from a dataset when splitting a parent node into child partitions.
      </p>

      <div class="formula-card">
        <div class="formula-title">&#128290; Information Gain Equation</div>
        <div class="formula-math">
          IG = H(parent) - &sum;<sub>j=1</sub><sup>m</sup> (N<sub>j</sub> / N) &times; H(child<sub>j</sub>)
        </div>
        <div class="formula-legend">
          <div class="legend-item"><span class="legend-sym">H(parent)</span><span>Entropy of the parent node before splitting.</span></div>
          <div class="legend-item"><span class="legend-sym">m</span><span>Number of child branches created by split (m = 2 for binary trees).</span></div>
          <div class="legend-item"><span class="legend-sym">N<sub>j</sub> / N</span><span>Fraction of training points routed into child branch j.</span></div>
          <div class="legend-item"><span class="legend-sym">H(child<sub>j</sub>)</span><span>Entropy of child partition j.</span></div>
        </div>
      </div>

      {SVG_INFORMATION_GAIN_WORKED}

      <h3 class="sub-title">Complete 7-Step Arithmetic Walkthrough</h3>
      <p>
        Let us compute the Information Gain for splitting 20 students on <code>Study Hours &ge; 5.0</code>:
      </p>

      <div class="calc-box">
        <ol style="margin-left: 20px; line-height: 1.8; color: #334155;">
          <li><strong>Parent Node Distribution:</strong> 10 Pass, 10 Fail (Total N = 20).
            <br>Parent Entropy: H(parent) = <strong>1.0000 bit</strong>.
          </li>
          <li><strong>Perform Candidate Split:</strong> Data partitions into Left (Hours &lt; 5) and Right (Hours &ge; 5).</li>
          <li><strong>Left Child Node (N<sub>1</sub> = 8):</strong> 1 Pass (12.5%), 7 Fail (87.5%).
            <br>H(left) = - [ 0.125 &times; log<sub>2</sub>(0.125) + 0.875 &times; log<sub>2</sub>(0.875) ]
            <br>H(left) = - [ 0.125 &times; (-3.0) + 0.875 &times; (-0.1926) ] = - [ -0.375 - 0.1686 ] = <strong>0.5436 bits</strong>.
          </li>
          <li><strong>Right Child Node (N<sub>2</sub> = 12):</strong> 9 Pass (75.0%), 3 Fail (25.0%).
            <br>H(right) = - [ 0.75 &times; log<sub>2</sub>(0.75) + 0.25 &times; log<sub>2</sub>(0.25) ]
            <br>H(right) = - [ 0.75 &times; (-0.4150) + 0.25 &times; (-2.0) ] = - [ -0.3113 - 0.5000 ] = <strong>0.8113 bits</strong>.
          </li>
          <li><strong>Compute Weighted Child Entropy:</strong>
            <br>Weighted Entropy = (8 / 20) &times; 0.5436 + (12 / 20) &times; 0.8113
            <br>Weighted Entropy = 0.40 &times; 0.5436 + 0.60 &times; 0.8113 = 0.2174 + 0.4868 = <strong>0.7042 bits</strong>.
          </li>
          <li><strong>Compute Final Information Gain:</strong>
            <br><strong>IG = H(parent) - Weighted Entropy = 1.0000 - 0.7042 = 0.2958 bits</strong>.
          </li>
          <li><strong>Verify Gini Gain on Same Split:</strong>
            <br>Parent Gini: 0.5000. Left Gini: 0.2188. Right Gini: 0.3750.
            <br>Weighted Child Gini: (8/20)&times;0.2188 + (12/20)&times;0.3750 = 0.0875 + 0.2250 = <strong>0.3125</strong>.
            <br><strong>Gini Gain = 0.5000 - 0.3125 = 0.1875</strong>.
          </li>
        </ol>
      </div>

      <div class="callout callout-info">
        <div class="callout-title">&#128161; Information Gain vs. Gini Gain Distinction</div>
        <p>
          Notice that <strong>Information Gain</strong> is formally defined using <strong>Entropy</strong> (measuring bit reduction). When using Gini Impurity, the corresponding metric is called <strong>Gini Gain</strong> or <strong>Impurity Reduction (&Delta; Gini)</strong>. While their numerical scales differ (0.2958 bits vs. 0.1875 Gini reduction), they rank candidate splits in virtually identical order!
        </p>
      </div>
    </section>

    <!-- SECTION 09: CHOOSING BETWEEN GINI AND ENTROPY -->
    <section id="sec-09" class="section-card">
      <span class="section-badge">Section 09</span>
      <h2 class="section-title">Choosing Between Gini Impurity and Entropy</h2>
      <p class="section-lead">
        When building trees in scikit-learn, should you configure <code>criterion='gini'</code> or <code>criterion='entropy'</code>? Let us examine the practical engineering trade-offs.
      </p>

      {SVG_ENTROPY_VS_GINI}

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Evaluation Dimension</th>
              <th>Gini Impurity (<code>criterion='gini'</code>)</th>
              <th>Entropy / Info Gain (<code>criterion='entropy'</code>)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Theoretical Foundation</strong></td>
              <td>Statistical dispersion (Corrado Gini, 1912)</td>
              <td>Information Theory (Claude Shannon, 1948)</td>
            </tr>
            <tr>
              <td><strong>Mathematical Formula</strong></td>
              <td><code>1 - &sum; p<sub>i</sub>&sup2;</code></td>
              <td><code>- &sum; p<sub>i</sub> log<sub>2</sub>(p<sub>i</sub>)</code></td>
            </tr>
            <tr>
              <td><strong>Range for Binary Tasks</strong></td>
              <td>0.0 (Pure) to 0.50 (Max Impurity)</td>
              <td>0.0 (Pure) to 1.00 (Max Uncertainty in bits)</td>
            </tr>
            <tr>
              <td><strong>Computational Speed</strong></td>
              <td><strong>Significantly Faster:</strong> Simple squaring and subtraction; zero floating-point logarithms.</td>
              <td><strong>Slower:</strong> Computing base-2 logarithms for thousands of candidate splits is CPU-heavy.</td>
            </tr>
            <tr>
              <td><strong>Split Behavior</strong></td>
              <td>Slightly favors isolating the largest class into its own pure partition quickly.</td>
              <td>Slightly favors producing more balanced, equal-sized child subsets.</td>
            </tr>
            <tr>
              <td><strong>Production Recommendation</strong></td>
              <td><strong>Use as Default (Best Practice):</strong> Fast, memory-efficient, yields identical trees &gt;98% of the time.</td>
              <td>Use when you need formal information-theoretic interpretation or when testing fine-grained split parity.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 10: HOW THE TREE LEARNS (RECURSION & STOPPING) -->
    <section id="sec-10" class="section-card">
      <span class="section-badge">Section 10</span>
      <h2 class="section-title">How the Tree Learns (Recursive Partitioning &amp; Stopping Rules)</h2>
      <p class="section-lead">
        Decision trees are constructed using a top-down, greedy algorithm known as <strong>Recursive Binary Splitting</strong> (the core of the CART algorithm: Classification and Regression Trees).
      </p>

      <h3 class="sub-title">1. The Greedy Recursive Algorithm Explained</h3>
      <p>
        The algorithm is called <strong>greedy</strong> because at each node, it makes the decision that looks best at that immediate moment without considering whether a different split might lead to a superior overall tree three levels deeper.
      </p>

      <div class="steps-container">
        <div class="step-card">
          <div class="step-number">1</div>
          <div class="step-content">
            <h4 class="step-title">Start at the Root Node</h4>
            <p>Begin with the entire training dataset residing inside the root node.</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">2</div>
          <div class="step-content">
            <h4 class="step-title">Exhaustive Candidate Scan</h4>
            <p>For every feature j and every candidate threshold t, calculate the Impurity Drop (&Delta; Gini or Information Gain).</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">3</div>
          <div class="step-content">
            <h4 class="step-title">Execute the Optimal Split</h4>
            <p>Split the data points into a Left Child (points satisfying the condition) and a Right Child (points failing it).</p>
          </div>
        </div>

        <div class="step-card">
          <div class="step-number">4</div>
          <div class="step-content">
            <h4 class="step-title">Recursion &amp; Stopping Criteria</h4>
            <p>Repeat Steps 2 and 3 independently on each child node. Stop splitting when a pre-configured stopping rule is triggered!</p>
          </div>
        </div>
      </div>

      <h3 class="sub-title">2. Critical Pre-Pruning Hyperparameters</h3>
      <p>
        Without stopping rules, a decision tree will continue splitting until every single training point sits in its own private leaf node, achieving 100% training accuracy but memorizing pure noise! scikit-learn provides crucial hyperparameter controls:
      </p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Hyperparameter</th>
              <th>Default</th>
              <th>Meaning &amp; Impact</th>
              <th>Beginner Tuning Advice</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>max_depth</code></td>
              <td><code>None</code> (Unlimited)</td>
              <td>The maximum allowed distance from root to the deepest leaf node.</td>
              <td>Set to a moderate integer (e.g., 3 to 6) to prevent runaway depth and overfitting.</td>
            </tr>
            <tr>
              <td><code>min_samples_split</code></td>
              <td><code>2</code></td>
              <td>The minimum number of data points a node must contain to be eligible for splitting.</td>
              <td>Increase to 10 or 20 to stop the tree from splitting tiny, noisy pockets of data.</td>
            </tr>
            <tr>
              <td><code>min_samples_leaf</code></td>
              <td><code>1</code></td>
              <td>The minimum number of training samples required to form a valid terminal leaf node.</td>
              <td>Set to 5 or 10 so predictions are backed by a reliable sample size.</td>
            </tr>
            <tr>
              <td><code>max_leaf_nodes</code></td>
              <td><code>None</code></td>
              <td>Limits the total number of terminal leaves in the entire tree.</td>
              <td>Grows the tree in a best-first fashion based on highest relative reduction in impurity.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""

def get_part2():
    return PART2_HTML
