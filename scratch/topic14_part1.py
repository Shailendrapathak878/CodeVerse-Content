"""
Topic 14: Naive Bayes - Content Part 1
Covers Hero, Table of Contents, and Sections 1 through 5.
Uses literal UTF-8 characters and placeholders __SVG_...__ for diagram insertion.
"""

TOPIC14_PART1 = """
  <div class="container">
    <!-- Hero Header -->
    <header class="hero-header">
      <div class="hero-badge">Topic 14 &bull; Supervised Learning &bull; Probabilistic Classification</div>
      <h1 class="hero-title">Naive Bayes Classifiers: From Probability Fundamentals to Real-World Classification</h1>
      <p class="hero-desc">Master the intuitive mathematics of conditional probability, Bayes' Theorem, feature independence factorization, Laplace smoothing, and scikit-learn classification pipelines through crystal-clear numerical demonstrations and transparent Python labs.</p>
      
      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <span class="hero-meta-label">Domain</span>
          <span class="hero-meta-value">Supervised Classification</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Prerequisites</span>
          <span class="hero-meta-value">Basic Arithmetic &amp; Python</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Key Concept</span>
          <span class="hero-meta-value">Bayes' Theorem &amp; Conditional Independence</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Theme</span>
          <span class="hero-meta-value">Light Mode Only &bull; Royal Violet</span>
        </div>
      </div>
    </header>

    <!-- Table of Contents -->
    <nav class="toc-card" aria-label="Table of Contents">
      <h2 class="toc-title">Table of Contents &bull; 23 Complete Sections</h2>
      <ul class="toc-grid">
        <li><a class="toc-link" href="#sec-01"><span class="toc-number">01</span> Introduction to Naive Bayes</a></li>
        <li><a class="toc-link" href="#sec-02"><span class="toc-number">02</span> Probability Fundamentals</a></li>
        <li><a class="toc-link" href="#sec-03"><span class="toc-number">03</span> Conditional Probability &amp; Contingency Tables</a></li>
        <li><a class="toc-link" href="#sec-04"><span class="toc-number">04</span> Bayes' Theorem Explained</a></li>
        <li><a class="toc-link" href="#sec-05"><span class="toc-number">05</span> Visual Bayes' Theorem Worked Example</a></li>
        <li><a class="toc-link" href="#sec-06"><span class="toc-number">06</span> From Bayes' Theorem to Naive Bayes</a></li>
        <li><a class="toc-link" href="#sec-07"><span class="toc-number">07</span> The Naive Independence Assumption</a></li>
        <li><a class="toc-link" href="#sec-08"><span class="toc-number">08</span> Step-by-Step Multi-Feature Calculation</a></li>
        <li><a class="toc-link" href="#sec-09"><span class="toc-number">09</span> The Zero-Frequency Problem</a></li>
        <li><a class="toc-link" href="#sec-10"><span class="toc-number">10</span> Laplace Smoothing (&alpha; Additive Correction)</a></li>
        <li><a class="toc-link" href="#sec-11"><span class="toc-number">11</span> Types of Naive Bayes Classifiers</a></li>
        <li><a class="toc-link" href="#sec-12"><span class="toc-number">12</span> Comparing Naive Bayes Variants Visually</a></li>
        <li><a class="toc-link" href="#sec-13"><span class="toc-number">13</span> Complete Python Lab: MultinomialNB Spam Classifier</a></li>
        <li><a class="toc-link" href="#sec-14"><span class="toc-number">14</span> Gaussian Naive Bayes Numerical Lab</a></li>
        <li><a class="toc-link" href="#sec-15"><span class="toc-number">15</span> Decision Scores, Probabilities &amp; Log-Space</a></li>
        <li><a class="toc-link" href="#sec-16"><span class="toc-number">16</span> Model Evaluation &amp; Error Cost Tradeoffs</a></li>
        <li><a class="toc-link" href="#sec-17"><span class="toc-number">17</span> Advantages &amp; Fundamental Limitations</a></li>
        <li><a class="toc-link" href="#sec-18"><span class="toc-number">18</span> Naive Bayes vs. Other ML Classifiers</a></li>
        <li><a class="toc-link" href="#sec-19"><span class="toc-number">19</span> Real-Life Production Case Studies</a></li>
        <li><a class="toc-link" href="#sec-20"><span class="toc-number">20</span> Common Beginner Mistakes &amp; Fixes</a></li>
        <li><a class="toc-link" href="#sec-21"><span class="toc-number">21</span> Required Visualizations System &amp; Visual Guide</a></li>
        <li><a class="toc-link" href="#sec-22"><span class="toc-number">22</span> Quick Reference, Formulas &amp; Summary Matrix</a></li>
        <li><a class="toc-link" href="#sec-23"><span class="toc-number">23</span> Interactive Knowledge Checks &amp; FAQs</a></li>
      </ul>
    </nav>

    <!-- Section 1 -->
    <section id="sec-01" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 01</span>
        <h2 class="section-title">Introduction to Naive Bayes</h2>
        <p class="section-subtitle">Understanding probabilistic classification through evidence, likelihood, and everyday intuition</p>
      </div>

      <h3>What is Classification in Machine Learning?</h3>
      <p>In Machine Learning, <strong>classification</strong> is the supervised task of assigning an unseen input data item into one of two or more predefined categorical classes or labels. For example, given an email message, a classification model must assign it to either the class <strong>Spam</strong> or the class <strong>Ham</strong> (legitimate email). Given an X-ray scan, a classifier might predict <strong>Healthy</strong> or <strong>Pneumonia</strong>.</p>
      
      <p>Many machine learning algorithms make decisions using geometric distance (such as K-Nearest Neighbors) or separating boundaries (such as Support Vector Machines and Decision Trees). In contrast, <strong>Naive Bayes</strong> takes a fundamentally probabilistic approach: it asks, <em>"Given the specific evidence observed in this email, what is the probability that it belongs to Class A versus Class B?"</em></p>

      <div class="callout-card def-card">
        <div class="def-title">Core Definition: Probabilistic Classifier</div>
        <p>A <strong>probabilistic classifier</strong> does not merely output a hard label (e.g., "Spam"). Instead, it calculates the conditional probability distribution across all possible candidate classes given the observed input features: P(Class = C | Evidence = X). The classifier then selects the class with the highest probability as its final prediction.</p>
      </div>

      <h3>Why is it Called "Bayes"?</h3>
      <p>The algorithm is named in honor of the English statistician and Presbyterian minister <strong>Thomas Bayes</strong> (1701&ndash;1761), who formulated the foundational principle of inverse probability. <strong>Bayes' Theorem</strong> provides a rigorous mathematical bridge connecting our initial background knowledge (the <em>prior</em> probability) with newly observed empirical evidence (the <em>likelihood</em>) to calculate an updated, refined belief (the <em>posterior</em> probability).</p>

      <h3>Why is it Called "Naive"?</h3>
      <p>The word <strong>"Naive"</strong> (sometimes written as simple or unsophisticated) refers to a deliberate simplifying assumption made by the model: <em>it assumes that all input features are strictly conditionally independent of one another given the target class.</em></p>

      <p>For example, if an email contains the words <strong>"free"</strong>, <strong>"cash"</strong>, and <strong>"prize"</strong>, Naive Bayes assumes that the presence of the word "free" tells us nothing about whether "cash" or "prize" will appear, once we know whether the email is spam or legitimate. In real human communication, this assumption is clearly violated: words often appear together in phrases or contextual clusters. However, despite being linguistically "naive", this assumption dramatically simplifies the mathematical calculations from impossible multi-dimensional joint tables down to simple one-dimensional multiplications &mdash; and in practice, it achieves remarkably accurate classification accuracy.</p>

      <div class="callout-card analogy-card">
        <div class="analogy-title">Everyday Analogy: The Detective Weighing Clues</div>
        <p>Imagine a detective arriving at a crime scene. Before examining anything, the detective knows the historical crime rate in the district (the <em>prior</em>). Then, the detective discovers three clues: muddy footprints, a broken window latch, and a dropped receipt. Rather than trying to calculate the astronomical joint probability of all three clues happening simultaneously in that exact configuration, a "naive" detective examines how often each clue appears in burglary cases independently, multiplies the evidence scores together, and updates their suspicion. If the cumulative evidence overwhelmingly points toward burglary, the case is classified accordingly.</p>
      </div>

      <h3>The Relatable Email Spam Example</h3>
      <p>Consider an incoming email with the subject line: <em>"Claim your free cash prize now!"</em></p>
      <p>Words such as <strong>"free"</strong>, <strong>"offer"</strong>, and <strong>"prize"</strong> frequently appear in spam advertisements. When our classifier observes these tokens, each token acts as a piece of circumstantial evidence. If 80% of spam messages contain "free" while only 10% of authentic messages contain "free", the presence of "free" acts as an 8&times; evidence multiplier tilting the scale toward Spam.</p>

      <div class="callout-card warn-card">
        <div class="warn-title">Important Educational Note: Evidence vs. Proof</div>
        <p>Words like "free", "discount", or "prize" are illustrative indicators, not absolute proof. A legitimate email from your university stating "Free pizza at the coding club meeting" or an email from your bank with "Zero free fees this month" contains the word "free" but is not spam. Naive Bayes combines multiple feature probabilities with class base rates to balance false alarms against missed detections.</p>
      </div>

      <!-- Hero Pipeline SVG Diagram -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_NB_HERO_PIPELINE__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.1:</strong> The complete Naive Bayes classification workflow pipeline, showing raw message tokenization, independent feature extraction, prior and likelihood evaluation, score comparison, and final argmax probability prediction.
        </div>
      </div>
    </section>

    <!-- Section 2 -->
    <section id="sec-02" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 02</span>
        <h2 class="section-title">Probability Fundamentals</h2>
        <p class="section-subtitle">The essential mathematical building blocks required to understand probabilistic modeling</p>
      </div>

      <p>Before diving into Bayes' theorem, let us establish the exact probability terminology and mathematical definitions used throughout machine learning.</p>

      <h3>1. Experiment, Outcome, and Sample Space</h3>
      <ul>
        <li><strong>Random Experiment:</strong> Any repeatable process or observation that produces an uncertain result (e.g., inspecting an incoming email from the internet).</li>
        <li><strong>Outcome:</strong> A single specific result of an experiment (e.g., the inspected message is classified as Spam).</li>
        <li><strong>Sample Space (S):</strong> The complete set of all possible mutually exclusive outcomes. In binary email classification, S = {Spam, Ham}.</li>
      </ul>

      <h3>2. Event and Probability</h3>
      <p>An <strong>event</strong> (denoted as A or E) is any subset of outcomes from the sample space. The <strong>probability</strong> of event A, written as P(A), is a real number between 0.0 and 1.0 quantifying how likely event A is to occur:</p>
      
      <div class="formula-block">
        <div class="formula-title">Classical Probability from Frequency Counts</div>
        P(A) = Count(Outcomes where A occurs) / Total Count of All Observed Outcomes
      </div>

      <h3>3. Prior Probability (Class Base Rate)</h3>
      <p>The <strong>prior probability</strong> P(C) is the baseline probability of an event or class before considering any new or specific evidence. For instance, suppose an email service inspects a sample of 100 emails and finds that 20 are Spam and 80 are Ham (legitimate):</p>

      <div class="calc-box">
        <div class="calc-title">Calculating Class Prior Probabilities:</div>
        <div class="calc-step">
          <span class="calc-step-num">1.</span>
          <span>Total sample size: N = 100 emails.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">2.</span>
          <span>Spam count = 20 &rarr; P(Spam) = 20 / 100 = 0.20 (20.0%).</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">3.</span>
          <span>Ham count = 80 &rarr; P(Ham) = 80 / 100 = 0.80 (80.0%).</span>
        </div>
      </div>

      <p>This means that if your phone rings with a notification before you even unlock the screen or read a single word of the text, your prior belief is that there is an 80% chance the email is authentic and a 20% chance it is spam.</p>

      <!-- Prior Probabilities Bar Chart SVG -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_PROBABILITY_BARS__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.2:</strong> Visual representation of class prior probabilities P(Spam) = 0.20 and P(Ham) = 0.80 derived from an empirical sample of 100 emails.
        </div>
      </div>

      <h3>4. Joint Probability, Conditional Probability, and Complement</h3>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Concept</th>
              <th>Mathematical Notation</th>
              <th>Plain-English Meaning</th>
              <th>Numerical Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Prior Probability</strong></td>
              <td>P(A)</td>
              <td>Unconditional baseline probability of event A occurring.</td>
              <td>P(Spam) = 0.20</td>
            </tr>
            <tr>
              <td><strong>Joint Probability</strong></td>
              <td>P(A &cap; B) or P(A, B)</td>
              <td>Probability that event A and event B occur simultaneously.</td>
              <td>P(Spam &cap; "free") = 16 / 100 = 0.16</td>
            </tr>
            <tr>
              <td><strong>Conditional Probability</strong></td>
              <td>P(A | B)</td>
              <td>Probability of event A occurring given that event B has already occurred.</td>
              <td>P("free" | Spam) = 16 / 20 = 0.80</td>
            </tr>
            <tr>
              <td><strong>Complement Probability</strong></td>
              <td>P(A<sup>c</sup>) or P(&not;A)</td>
              <td>Probability that event A does NOT occur: P(A<sup>c</sup>) = 1 &minus; P(A).</td>
              <td>P(Ham) = 1 &minus; 0.20 = 0.80</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout-card warn-card">
        <div class="warn-title">Pedagogical Distinction: Sample Frequency vs. True Population</div>
        <p>In our example, P(Spam) = 20 / 100 = 0.20 represents the empirical proportion within our specific observed training dataset. It is not an immutable law of all global email traffic. If a company's spam filter receives 60% spam in production, its prior will reflect that operational environment.</p>
      </div>
    </section>

    <!-- Section 3 -->
    <section id="sec-03" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 03</span>
        <h2 class="section-title">Conditional Probability &amp; Contingency Tables</h2>
        <p class="section-subtitle">Understanding "the probability of A given B" through the restricted denominator principle</p>
      </div>

      <h3>What Does P(A | B) Really Mean?</h3>
      <p>The expression <strong>P(A | B)</strong> is read as <em>"the probability of event A given that event B has occurred"</em>. The vertical bar <strong>|</strong> represents conditioning: it tells us that event B is no longer a possibility; it is a known fact.</p>

      <p>When event B occurs, the universe of possibilities collapses. We no longer care about the entire sample space S. Instead, our reference denominator is strictly restricted to only those outcomes where B is true.</p>

      <div class="formula-block">
        <div class="formula-title">Formal Mathematical Definition of Conditional Probability</div>
        P(A | B) = P(A &cap; B) / P(B)   [Provided P(B) &gt; 0]
      </div>

      <h3>The 2&times;2 Contingency Table</h3>
      <p>To see how this works with concrete numbers, let us analyze our sample of 100 emails. Each email is categorized by its class (Spam or Ham) and whether it contains the keyword <strong>"free"</strong>:</p>

      <!-- Contingency Table SVG Visual -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_CONTINGENCY_TABLE__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.3:</strong> A 2&times;2 contingency table illustrating how conditioning restricts the denominator. P(Free | Spam) restricts attention to the 20 Spam rows (16/20 = 0.80), while P(Spam | Free) restricts attention to the 24 "Free" columns (16/24 = 0.6667).
        </div>
      </div>

      <h3>Manual Step-by-Step Calculation:</h3>
      <p>Let us calculate the probabilities directly from the counts in the contingency table:</p>

      <div class="calc-box">
        <div class="calc-title">Step-by-Step Calculations:</div>
        <div class="calc-step">
          <span class="calc-step-num">1.</span>
          <span><strong>Total Emails:</strong> N = 100. Total containing "free" = 16 + 8 = 24 &rarr; P(Free) = 24 / 100 = 0.24.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">2.</span>
          <span><strong>Total Spam:</strong> N<sub>Spam</sub> = 20 &rarr; P(Spam) = 20 / 100 = 0.20.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">3.</span>
          <span><strong>Joint Probability:</strong> Emails that are both Spam and contain "free" = 16 &rarr; P(Free &cap; Spam) = 16 / 100 = 0.16.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">4.</span>
          <span><strong>Likelihood P(Free | Spam):</strong> Condition on the Spam row (20 total):<br>
          P(Free | Spam) = Count(Free &amp; Spam) / Count(Spam) = 16 / 20 = <strong>0.80 (80.0%)</strong>.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">5.</span>
          <span><strong>Posterior P(Spam | Free):</strong> Condition on the "Free" column (24 total):<br>
          P(Spam | Free) = Count(Free &amp; Spam) / Count(Free) = 16 / 24 = <strong>0.6667 (66.67%)</strong>.</span>
        </div>
      </div>

      <div class="callout-card warn-card">
        <div class="warn-title">The Most Common Beginner Trap: Confusing P(A | B) with P(B | A)</div>
        <p>Notice the stark difference:
        <br>&bull; <strong>P(Free | Spam) = 0.80:</strong> 80% of spam messages contain the word "free".
        <br>&bull; <strong>P(Spam | Free) = 0.6667:</strong> 66.67% of messages containing "free" are spam.
        <br>These numbers are fundamentally different because their reference denominators (20 vs. 24) are different. Confusing likelihood with posterior probability is one of the most frequent errors in applied data science!</p>
      </div>
    </section>

    <!-- Section 4 -->
    <section id="sec-04" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 04</span>
        <h2 class="section-title">Bayes' Theorem Explained</h2>
        <p class="section-subtitle">How evidence rigorously updates initial beliefs into updated posterior probabilities</p>
      </div>

      <p>In many real-world scenarios, it is relatively easy to measure how evidence behaves under a known condition (e.g., how often spam messages contain the word "free"). However, in practice, we face the <em>inverse problem</em>: given that we observe the word "free" in an unlabelled incoming message, what is the probability that the message is spam?</p>

      <p><strong>Bayes' Theorem</strong> provides the exact mathematical formula to invert conditional probabilities:</p>

      <div class="formula-block">
        <div class="formula-title">Bayes' Theorem Formula</div>
        P(A | B) = [ P(B | A) &times; P(A) ] / P(B)
      </div>

      <h3>The Four Components of Bayes' Theorem</h3>
      <p>In the context of machine learning classification, we denote class hypothesis as <strong>C</strong> and observed evidence as <strong>X</strong>:</p>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Term</th>
              <th>Symbol</th>
              <th>Conceptual Meaning</th>
              <th>Value in Our Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Prior Probability</strong></td>
              <td>P(C)</td>
              <td>Initial belief that the class occurs, before inspecting any evidence.</td>
              <td>P(Spam) = 0.20 (20%)</td>
            </tr>
            <tr>
              <td><strong>Likelihood</strong></td>
              <td>P(X | C)</td>
              <td>The probability of observing evidence X given that the class is C.</td>
              <td>P(Free | Spam) = 0.80 (80%)</td>
            </tr>
            <tr>
              <td><strong>Marginal Evidence</strong></td>
              <td>P(X)</td>
              <td>Total probability of observing evidence X across all possible classes.</td>
              <td>P(Free) = 0.24 (24%)</td>
            </tr>
            <tr>
              <td><strong>Posterior Probability</strong></td>
              <td>P(C | X)</td>
              <td>Updated probability that the message belongs to class C after observing evidence X.</td>
              <td>P(Spam | Free) = 0.6667 (66.7%)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Expanding the Denominator: The Law of Total Probability</h3>
      <p>How do we calculate the marginal evidence P(X)? By summing the joint probabilities across all mutually exclusive classes:</p>
      
      <div class="formula-block">
        <div class="formula-title">Law of Total Probability for Evidence P(X)</div>
        P(X) = P(X | Class 1) &times; P(Class 1) + P(X | Class 2) &times; P(Class 2)
      </div>

      <p>Substituting our actual numbers:</p>
      <div class="formula-block">
        P(Free) = P(Free | Spam) &times; P(Spam) + P(Free | Ham) &times; P(Ham)<br>
        P(Free) = (0.80 &times; 0.20) + (0.10 &times; 0.80) = 0.16 + 0.08 = 0.24
      </div>

      <h3>Complete Worked Verification:</h3>
      <div class="calc-box">
        <div class="calc-title">Applying Bayes' Theorem to Calculate P(Spam | Free):</div>
        <div class="calc-step">
          <span class="calc-step-num">1.</span>
          <span>Numerator = Likelihood &times; Prior = P(Free | Spam) &times; P(Spam) = 0.80 &times; 0.20 = <strong>0.1600</strong>.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">2.</span>
          <span>Denominator = Total Evidence = P(Free) = <strong>0.2400</strong>.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">3.</span>
          <span>Posterior P(Spam | Free) = 0.1600 / 0.2400 = 2 / 3 = <strong>0.6667 (66.67%)</strong>.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">4.</span>
          <span>Posterior P(Ham | Free) = [ P(Free | Ham) &times; P(Ham) ] / P(Free) = [ 0.10 &times; 0.80 ] / 0.24 = 0.08 / 0.24 = <strong>0.3333 (33.33%)</strong>.</span>
        </div>
        <div class="calc-step">
          <span class="calc-step-num">5.</span>
          <span>Sanity Check: P(Spam | Free) + P(Ham | Free) = 0.6667 + 0.3333 = 1.0000 (100.0%).</span>
        </div>
      </div>

      <!-- Bayes Update SVG Visual -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_BAYES_THEOREM_UPDATE__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.4:</strong> Visualizing Bayes' Theorem: initial prior belief P(Spam) = 20.0% is transformed by the strong evidence ratio of "free" (8&times; higher likelihood in spam) into an updated posterior belief of 66.7%.
        </div>
      </div>
    </section>

    <!-- Section 5 -->
    <section id="sec-05" class="content-section">
      <div class="section-header">
        <span class="section-badge">Section 05</span>
        <h2 class="section-title">Visual Bayes' Theorem Worked Example</h2>
        <p class="section-subtitle">Comparing prior and likelihood ratios across spam and legitimate email vocabulary</p>
      </div>

      <p>Let us deepen our understanding by analyzing how different words exert different degrees of evidence pressure on the posterior probability.</p>

      <h3>Comparing Multiple Vocabulary Tokens</h3>
      <p>Suppose our spam filter monitors three specific keywords across our 100 training messages (20 Spam, 80 Ham):</p>
      <ul>
        <li><strong>"free":</strong> Appears in 16 of 20 Spam (80%), and in 8 of 80 Ham (10%).</li>
        <li><strong>"offer":</strong> Appears in 14 of 20 Spam (70%), and in 12 of 80 Ham (15%).</li>
        <li><strong>"prize":</strong> Appears in 10 of 20 Spam (50%), and in 4 of 80 Ham (5%).</li>
      </ul>

      <!-- Likelihood Comparison Horizontal Bar Chart SVG -->
      <div class="visual-container">
        <div class="svg-wrapper">
          __SVG_SPAM_WORDS_LIKELIHOOD__
        </div>
        <div class="visual-caption">
          <strong>Figure 14.5:</strong> Class-conditional feature likelihoods P(Word | Class) for "free", "offer", and "prize". Each word demonstrates a substantial likelihood ratio favoring the Spam class.
        </div>
      </div>

      <h3>Likelihood Ratios:</h3>
      <p>The <strong>Likelihood Ratio (LR)</strong> measures how much more probable an observed feature is under one class compared to another:</p>
      <div class="formula-block">
        Likelihood Ratio = P(Word | Spam) / P(Word | Ham)<br>
        &bull; LR("free") = 0.80 / 0.10 = 8.0&times;<br>
        &bull; LR("offer") = 0.70 / 0.15 = 4.67&times;<br>
        &bull; LR("prize") = 0.50 / 0.05 = 10.0&times;
      </div>

      <p>When an incoming email contains words with likelihood ratios substantially greater than 1.0, Bayes' theorem progressively multiplies the prior odds, driving the posterior belief toward the Spam hypothesis.</p>

      <div class="callout-card success-card">
        <div class="success-title">Key Intuition to Remember:</div>
        <p>A prior of 20% tells us spam is relatively uncommon. But when an email contains the word "prize" (10&times; more common in spam), that single strong piece of evidence overcomes the low base rate. In the next section, we see how Naive Bayes handles emails with multiple simultaneous words!</p>
      </div>
    </section>
"""
