"""
Topic 14: Naive Bayes - Content Part 2
Covers Sections 6 through 10.
Uses literal UTF-8 characters and placeholders __SVG_...__ for diagram insertion.
"""

TOPIC14_PART2 = """
    <!-- Section 6 -->
    <section id="sec-06" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 06</span>
        <h2 class="section-title">From Bayes' Theorem to Naive Bayes</h2>
        <p class="section-subtitle">Extending single-event probability to high-dimensional feature vectors and classification decision rules</p>
      </div>

      <p>In Section 4, we applied Bayes' theorem to a single word event ("free"). In real machine learning problems, however, an input document is represented not by a single word, but by an entire <strong>feature vector</strong> of multiple observations:</p>

      <div class="formula-block">
        <div class="formula-title">Feature Vector Representation</div>
        X = (x₁, x₂, x₃, &hellip;, x<sub>n</sub>)
      </div>

      <p>Here, each x<sub>i</sub> represents an individual observed attribute. In text classification, x<sub>i</sub> could represent whether word i is present (binary 0 or 1) or the number of times word i appears in the text (frequency count).</p>

      <h3>Bayes' Theorem for Feature Vectors</h3>
      <p>Applying Bayes' theorem directly to our class hypothesis C and feature vector X yields:</p>

      <div class="formula-block">
        <div class="formula-title">Bayes' Rule for Classification</div>
        P(C | X) = [ P(X | C) &times; P(C) ] / P(X) = [ P(x₁, x₂, &hellip;, x<sub>n</sub> | C) &times; P(C) ] / P(x₁, x₂, &hellip;, x<sub>n</sub>)
      </div>

      <h3>Why the Denominator P(X) Does Not Affect Class Ranking</h3>
      <p>Notice a remarkable property of the classification decision rule: for any given test email, the evidence vector X is fixed and identical. When comparing the probability of Spam versus Ham for that same email, the denominator P(X) is exactly the same number for both classes!</p>

      <div class="calc-box">
        <div class="calc-title">Comparing Relative Class Scores:</div>
        <div class="calc-step">
          <span class="calc-step-num">&bull;</span>
          <span>P(Spam | X) = [ P(X | Spam) &times; P(Spam) ] / P(X)</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">&bull;</span>
          <span>P(Ham | X) = [ P(X | Ham) &times; P(Ham) ] / P(X)</span>
        </div>
      </div>

      <p>Since P(X) &gt; 0 is a strictly positive constant shared by all candidate classes, dividing by P(X) scales all scores equally but <em>cannot change which class score is larger</em>. Therefore, to determine the winning predicted class, we can discard the denominator and simply maximize the unnormalized numerator score:</p>

      <div class="formula-block">
        <div class="formula-title">The argmax Classification Decision Rule</div>
        Predicted Class = argmax<sub>C</sub> [ P(C) &times; P(x₁, x₂, &hellip;, x<sub>n</sub> | C) ]
      </div>

      <p>This insight saves substantial computational overhead because calculating the exact joint denominator P(x₁, &hellip;, x<sub>n</sub>) across hundreds or thousands of features would be computationally intractable.</p>
    </section>

    <!-- Section 7 -->
    <section id="sec-07" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 07</span>
        <h2 class="section-title">The Naive Independence Assumption</h2>
        <p class="section-subtitle">How factoring multi-dimensional joint distributions makes classification computationally feasible</p>
      </div>

      <h3>The Curse of Dimensionality in Joint Likelihoods</h3>
      <p>Even though we can ignore the denominator P(X), we still face a formidable challenge: how do we calculate the joint class-conditional likelihood <strong>P(x₁, x₂, &hellip;, x<sub>n</sub> | C)</strong>?</p>

      <p>If our vocabulary contains just n = 1,000 words, and each word is simply present or absent (2 possible values), there are 2<sup>1,000</sup> &approx; 10<sup>301</sup> possible combinations of word combinations! To estimate every possible joint combination directly from training data would require more sample emails than there are subatomic particles in the observable universe.</p>

      <h3>The "Naive" Simplification</h3>
      <p>To overcome this combinatorial explosion, the <strong>Naive Bayes</strong> algorithm introduces its defining assumption: <em>all features are assumed to be conditionally independent of each other given the class C</em>.</p>

      <p>Mathematically, when two events A and B are conditionally independent given C, their joint probability factors into the simple product of their individual probabilities: P(A &cap; B | C) = P(A | C) &times; P(B | C). Extending this to n features:</p>

      <div class="formula-block">
        <div class="formula-title">Naive Bayes Likelihood Factorization</div>
        P(x₁, x₂, &hellip;, x<sub>n</sub> | C) &approx; P(x₁ | C) &times; P(x₂ | C) &times; &hellip; &times; P(x<sub>n</sub> | C) = &prod;<sub>i=1</sub><sup>n</sup> P(x<sub>i</sub> | C)
      </div>

      <p>The symbol <strong>&prod;</strong> is mathematical product notation (analogous to &sum; for summation). It instructs us to multiply each individual feature's class-conditional likelihood together.</p>

      <!-- Independence Assumption SVG Visual -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_INDEPENDENCE_ASSUMPTION__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.6:</strong> Architectural comparison between true interconnected word dependencies (left) and the Naive Bayes star-topology assumption (right), where features depend only on the class node C.
        </div>
      </div>

      <h3>Why Does Naive Bayes Work So Well in Practice?</h3>
      <p>In human language, words are obviously not independent. If an email contains "luxury", it is far more likely to also contain "watch" or "hotel". Why then does Naive Bayes consistently deliver high classification accuracy?</p>

      <div class="callout-card success-card">
        <div class="success-title">Insight: Classification Ranking vs. Exact Calibration</div>
        <p>For classification, the model does not need the exact posterior probability P(Spam | X) to be perfectly calibrated. It only needs the ratio Score(Spam) &gt; Score(Ham) to preserve the correct order! Even when feature correlation inflates probability confidence toward 0.999 or 0.001, the <em>decision boundary</em> separating the classes remains remarkably robust.</p>
      </div>
    </section>

    <!-- Section 8 -->
    <section id="sec-08" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 08</span>
        <h2 class="section-title">Step-by-Step Naive Bayes Calculation</h2>
        <p class="section-subtitle">A fully worked, numerically verified multi-feature classification demonstration</p>
      </div>

      <p>Let us trace an incoming email through every step of the Naive Bayes algorithm using real numbers verified with Python.</p>

      <h3>1. Training Statistics</h3>
      <p>Recall our empirical training data of 100 emails (20 Spam, 80 Ham):</p>
      <ul>
        <li><strong>P(Spam) = 20 / 100 = 0.20</strong> &bull; <strong>P(Ham) = 80 / 100 = 0.80</strong></li>
        <li><strong>Likelihoods under Spam (20 emails):</strong>
          <br>&bull; P("free" | Spam) = 16 / 20 = 0.80
          <br>&bull; P("offer" | Spam) = 14 / 20 = 0.70
          <br>&bull; P("prize" | Spam) = 10 / 20 = 0.50
        </li>
        <li><strong>Likelihoods under Ham (80 emails):</strong>
          <br>&bull; P("free" | Ham) = 8 / 80 = 0.10
          <br>&bull; P("offer" | Ham) = 12 / 80 = 0.15
          <br>&bull; P("prize" | Ham) = 4 / 80 = 0.05
        </li>
      </ul>

      <h3>2. The Test Query</h3>
      <p>A new email arrives containing all three words: <strong>X = ("free", "offer", "prize")</strong>.</p>

      <h3>3. Step 1: Calculate Factored Likelihoods for Each Class</h3>
      <div class="calc-box">
        <div class="calc-title">Factored Likelihood Calculations:</div>
        <div class="calc-step">
          <span class="calc-step-num">Spam:</span>
          <span>P(X | Spam) = P("free" | Spam) &times; P("offer" | Spam) &times; P("prize" | Spam)<br>
          P(X | Spam) = 0.80 &times; 0.70 &times; 0.50 = <strong>0.280000</strong>.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">Ham:</span>
          <span>P(X | Ham) = P("free" | Ham) &times; P("offer" | Ham) &times; P("prize" | Ham)<br>
          P(X | Ham) = 0.10 &times; 0.15 &times; 0.05 = <strong>0.000750</strong>.</span>
        </div>
      </div>

      <h3>4. Step 2: Multiply by Class Prior to Obtain Unnormalized Scores</h3>
      <div class="calc-box">
        <div class="calc-title">Unnormalized Score Calculations:</div>
        <div class="calc-step">
          <span class="calc-step-num">Score(Spam):</span>
          <span>P(X | Spam) &times; P(Spam) = 0.280000 &times; 0.20 = <strong>0.056000</strong>.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">Score(Ham):</span>
          <span>P(X | Ham) &times; P(Ham) = 0.000750 &times; 0.80 = <strong>0.000600</strong>.</span>
        </div>
      </div>

      <p>Comparing the raw scores: 0.056000 / 0.000600 = <strong>93.33&times;</strong>. The Spam hypothesis is over 93 times more probable than the Ham hypothesis!</p>

      <h3>5. Step 3: Normalization to Posterior Probabilities</h3>
      <p>To convert these unnormalized scores into true probabilities that sum to 1.0 (100%), we divide each score by the total evidence constant Z:</p>

      <div class="calc-box">
        <div class="calc-title">Normalization Step:</div>
        <div class="calc-step">
          <span class="calc-step-num">Total Z:</span>
          <span>Z = Score(Spam) + Score(Ham) = 0.056000 + 0.000600 = <strong>0.056600</strong>.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">P(Spam | X):</span>
          <span>0.056000 / 0.056600 = <strong>0.989399 &approx; 98.94%</strong>.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">P(Ham | X):</span>
          <span>0.000600 / 0.056600 = <strong>0.010601 &approx; 1.06%</strong>.</span>
        </div>
      </div>

      <!-- Step-by-Step Scores SVG Visual -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_STEP_BY_STEP_SCORES__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.7:</strong> Breakdown of unnormalized class scores (left) converted through evidence normalization into final posterior probabilities (right). The predicted class is unambiguously SPAM (98.94% confidence).
        </div>
      </div>

      <h3>6. Python Code Verification</h3>
      <div class="code-container">
        <div class="code-header">
          <span>Python 3 &bull; Naive Bayes Multi-Feature Arithmetic</span>
          <span class="code-lang-badge">Python</span>
        </div>
        <pre class="code-body"><code># Verified Step-by-Step Multi-Feature Naive Bayes Arithmetic
p_spam, p_ham = 0.20, 0.80

# Likelihoods
p_x_given_spam = 0.80 * 0.70 * 0.50  # 0.280000
p_x_given_ham  = 0.10 * 0.15 * 0.05  # 0.000750

# Unnormalized scores
score_spam = p_x_given_spam * p_spam  # 0.056000
score_ham  = p_x_given_ham * p_ham    # 0.000600

# Normalization
z_total = score_spam + score_ham       # 0.056600
post_spam = score_spam / z_total       # 0.989399 (98.94%)
post_ham  = score_ham / z_total        # 0.010601 (1.06%)

print(f"Score(Spam): {score_spam:.6f} -> Posterior: {post_spam*100:.2f}%")
print(f"Score(Ham):  {score_ham:.6f} -> Posterior: {post_ham*100:.2f}%")
print(f"Predicted Class: {'SPAM' if post_spam > post_ham else 'HAM'}")</code></pre>
        <div class="code-output">
          <div class="code-output-title">Verified Execution Output</div>
Score(Spam): 0.056000 -> Posterior: 98.94%
Score(Ham):  0.000600 -> Posterior: 1.06%
Predicted Class: SPAM
        </div>
      </div>
    </section>

    <!-- Section 9 -->
    <section id="sec-09" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 09</span>
        <h2 class="section-title">The Zero-Frequency Problem</h2>
        <p class="section-subtitle">How a single unseen word can cause catastrophic multiplicative probability collapse</p>
      </div>

      <h3>The Catastrophic Vulnerability of Multiplication</h3>
      <p>Because Naive Bayes multiplies feature likelihoods together in a continuous chain (&prod; P(x<sub>i</sub> | C)), it suffers from a fatal vulnerability known as the <strong>Zero-Frequency Problem</strong>.</p>

      <p>Suppose an incoming message contains four words: <em>"free"</em>, <em>"offer"</em>, <em>"prize"</em>, and <em>"jackpot"</em>. In our training set of 80 legitimate emails, nobody ever happened to use the word "jackpot". Thus:</p>
      <div class="formula-block">
        Count("jackpot", Ham) = 0 &rarr; P("jackpot" | Ham) = 0 / 80 = <strong>0.0</strong>
      </div>

      <p>When calculating the Ham likelihood product for this message:</p>
      <div class="formula-block">
        Score(Ham) = P(Ham) &times; P("free"|Ham) &times; P("offer"|Ham) &times; P("prize"|Ham) &times; <span style="color:#DC2626;font-weight:700;">P("jackpot"|Ham)</span><br>
        Score(Ham) = 0.80 &times; 0.10 &times; 0.15 &times; 0.05 &times; <span style="color:#DC2626;font-weight:700;">0.00</span> = <span style="color:#DC2626;font-weight:700;">0.000000</span>
      </div>

      <!-- Zero Frequency SVG Visual -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_ZERO_FREQUENCY_PROBLEM__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.8:</strong> The zero-frequency catastrophe: a single zero term multiplies across the entire chain, annihilating all other accumulated evidence and forcing the class score to exactly zero.
        </div>
      </div>

      <div class="callout-card warn-card">
        <div class="warn-title">Why Zero Frequency is Philosophically Flawed</div>
        <p>In statistics, <em>absence of evidence is not evidence of impossibility</em>. Just because a legitimate email never used the word "jackpot" in our small 80-message sample does not mean that it is physically impossible for a genuine colleague to write: "Our project hit the jackpot by winning the research grant!" A classifier should never assign absolute zero probability to an event simply because it was absent from a finite training sample.</p>
      </div>
    </section>

    <!-- Section 10 -->
    <section id="sec-10" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 10</span>
        <h2 class="section-title">Laplace Smoothing (&alpha; Additive Correction)</h2>
        <p class="section-subtitle">Preventing zero probabilities through pseudocount adjustments in categorical and count models</p>
      </div>

      <h3>The Principle of Additive Smoothing</h3>
      <p>To prevent probability collapse, we apply <strong>Laplace smoothing</strong> (also called additive smoothing), originally proposed by Pierre-Simon Laplace in the 18th century. The idea is simple: we pretend we have observed every possible outcome an extra &alpha; times before looking at any training data.</p>

      <p>The parameter <strong>&alpha;</strong> (alpha) is a positive smoothing hyperparameter:</p>
      <ul>
        <li>When <strong>&alpha; = 1.0</strong>, it is called standard <strong>Laplace smoothing</strong>.</li>
        <li>When <strong>0 &lt; &alpha; &lt; 1.0</strong>, it is known as <strong>Lidstone smoothing</strong>.</li>
        <li>When <strong>&alpha; = 0.0</strong>, no smoothing is applied (raw empirical counts).</li>
      </ul>

      <h3>1. Categorical / Binary Presence Smoothing Formula</h3>
      <p>For a binary feature with K = 2 possible states (word present or word absent):</p>
      <div class="formula-block">
        <div class="formula-title">Binary Feature Laplace Smoothing (K = 2)</div>
        P(x<sub>i</sub> = 1 | C) = [ Count(x<sub>i</sub> = 1, C) + &alpha; ] / [ N<sub>C</sub> + &alpha; &times; K ]
      </div>

      <p>Where:</p>
      <ul>
        <li><strong>Count(x<sub>i</sub> = 1, C):</strong> Number of times feature i appeared in class C.</li>
        <li><strong>N<sub>C</sub>:</strong> Total number of training documents in class C.</li>
        <li><strong>K:</strong> Number of possible feature states (K = 2 for binary present/absent).</li>
        <li><strong>&alpha;:</strong> Pseudocount added to each state (&alpha; = 1.0).</li>
      </ul>

      <h3>2. Multinomial Bag-of-Words Smoothing Formula</h3>
      <p>For text word-count models where features represent vocabulary token counts from a dictionary of size |V|:</p>
      <div class="formula-block">
        <div class="formula-title">Multinomial Word-Count Smoothing (|V| Vocabulary Size)</div>
        P(w | C) = [ Count(w, C) + &alpha; ] / [ &sum;<sub>w'&isin;V</sub> Count(w', C) + &alpha; &times; |V| ]
      </div>

      <h3>Numerical Comparison: Unsmoothed vs. Smoothed Probabilities</h3>
      <p>Let us recalculate the likelihood of word "jackpot" in our sample with &alpha; = 1.0, K = 2:</p>

      <div class="calc-box">
        <div class="calc-title">Smoothed Probabilities for "jackpot":</div>
        <div class="calc-step">
          <span class="calc-step-num">Ham:</span>
          <span>Count = 0, N<sub>Ham</sub> = 80 &rarr; P<sub>smoothed</sub>("jackpot" | Ham) = (0 + 1) / (80 + 2&times;1) = 1 / 82 = <strong>0.012195 (1.22%)</strong>.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">Spam:</span>
          <span>Count = 4, N<sub>Spam</sub> = 20 &rarr; P<sub>smoothed</sub>("jackpot" | Spam) = (4 + 1) / (20 + 2&times;1) = 5 / 22 = <strong>0.227273 (22.73%)</strong>.</span>
        </div>
      </div>

      <!-- Laplace Smoothing Bar Chart SVG Visual -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_LAPLACE_SMOOTHING__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.9:</strong> Before-and-after Laplace smoothing comparison (&alpha; = 1.0). The zero count in Ham is safely transformed from a fatal 0.00% collapse into a realistic baseline probability of 1.22%.
        </div>
      </div>

      <div class="callout-card success-card">
        <div class="success-title">Guaranteed Stability</div>
        <p>With Laplace smoothing active, no probability term in the Naive Bayes model can ever reach 0.0. The classification pipeline remains numerically stable, resilient to rare vocabulary, and capable of gracefully processing previously unseen words in production.</p>
      </div>
    </section>
"""
