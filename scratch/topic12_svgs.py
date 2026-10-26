"""
Module: topic12_svgs.py
Generates 15 custom, XML-valid vector diagrams for Topic 12: Decision Trees.
Self-validates every SVG using xml.etree.ElementTree.
"""

import xml.etree.ElementTree as ET

# 1. HERO ARCHITECTURE DIAGRAM
SVG_DT_HERO = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Decision Tree Architecture: Hierarchical Recursive Partitioning</span>
    <span class="svg-badge">Figure 12.1</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 270" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="hero-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
        </filter>
        <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748B" />
        </marker>
        <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
        </marker>
        <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284C7" />
        </marker>
      </defs>

      <!-- Stage 1: Full Dataset -->
      <g transform="translate(30, 40)" filter="url(#hero-shadow)">
        <rect width="165" height="180" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect width="165" height="34" rx="12" fill="#EEF2FF"/>
        <rect y="22" width="165" height="12" fill="#EEF2FF"/>
        <text x="82" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#4338CA" text-anchor="middle">1. UNPARTITIONED DATA</text>
        <text x="82" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle">Entire Population (N=240)</text>
        <circle cx="50" cy="95" r="7" fill="#EF4444"/>
        <circle cx="70" cy="90" r="7" fill="#10B981"/>
        <circle cx="95" cy="100" r="7" fill="#EF4444"/>
        <circle cx="115" cy="95" r="7" fill="#10B981"/>
        <circle cx="60" cy="120" r="7" fill="#EF4444"/>
        <circle cx="85" cy="125" r="7" fill="#10B981"/>
        <circle cx="110" cy="118" r="7" fill="#EF4444"/>
        <text x="82" y="160" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">High Impurity (Mixed)</text>
        <rect x="25" y="175" width="115" height="24" rx="6" fill="#F1F5F9"/>
        <text x="82" y="191" font-family="monospace" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">Entropy = 1.00</text>
      </g>

      <!-- Connector 1 -> 2 -->
      <line x1="195" y1="130" x2="235" y2="130" stroke="#94A3B8" stroke-width="2" marker-end="url(#arrow)"/>

      <!-- Stage 2: Best Split Search -->
      <g transform="translate(245, 40)" filter="url(#hero-shadow)">
        <rect width="180" height="180" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect width="180" height="34" rx="12" fill="#F0F9FF"/>
        <rect y="22" width="180" height="12" fill="#F0F9FF"/>
        <text x="90" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0284C7" text-anchor="middle">2. EVALUATE SPLITS</text>
        <text x="90" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle">Greedy Threshold Scan</text>
        <rect x="15" y="80" width="150" height="26" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
        <text x="90" y="97" font-family="monospace" font-size="10.5" fill="#0284C7" text-anchor="middle">Study Hours ≥ 6.5?</text>
        <text x="90" y="125" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569" text-anchor="middle">Measure Impurity Drop:</text>
        <text x="90" y="145" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">Δ Gini or Info Gain</text>
        <rect x="25" y="165" width="130" height="24" rx="6" fill="#ECFDF5"/>
        <text x="90" y="181" font-family="monospace" font-size="10.5" font-weight="700" fill="#065F46" text-anchor="middle">Max Gain = 0.2958</text>
      </g>

      <!-- Connector 2 -> 3 -->
      <line x1="425" y1="130" x2="465" y2="130" stroke="#94A3B8" stroke-width="2" marker-end="url(#arrow)"/>

      <!-- Stage 3: Recursive Partition -->
      <g transform="translate(475, 40)" filter="url(#hero-shadow)">
        <rect width="180" height="180" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect width="180" height="34" rx="12" fill="#FEF3C7"/>
        <rect y="22" width="180" height="12" fill="#FEF3C7"/>
        <text x="90" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#D97706" text-anchor="middle">3. RECURSIVE SUBTREES</text>
        <text x="90" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle">Branching Child Nodes</text>
        
        <rect x="15" y="80" width="70" height="48" rx="6" fill="#FEE2E2" stroke="#FCA5A5"/>
        <text x="50" y="98" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">Left Child</text>
        <text x="50" y="115" font-family="monospace" font-size="9.5" fill="#991B1B" text-anchor="middle">Fail Dominant</text>

        <rect x="95" y="80" width="70" height="48" rx="6" fill="#D1FAE5" stroke="#6EE7B7"/>
        <text x="130" y="98" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">Right Child</text>
        <text x="130" y="115" font-family="monospace" font-size="9.5" fill="#065F46" text-anchor="middle">Pass Dominant</text>

        <text x="90" y="152" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">Repeats on each branch</text>
        <text x="90" y="172" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">until stopping criteria met</text>
      </g>

      <!-- Connector 3 -> 4 -->
      <line x1="655" y1="130" x2="695" y2="130" stroke="#94A3B8" stroke-width="2" marker-end="url(#arrow)"/>

      <!-- Stage 4: Leaf Predictions -->
      <g transform="translate(705, 40)" filter="url(#hero-shadow)">
        <rect width="145" height="180" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect width="145" height="34" rx="12" fill="#F3E8FF"/>
        <rect y="22" width="145" height="12" fill="#F3E8FF"/>
        <text x="72" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#7E22CE" text-anchor="middle">4. LEAF DECISION</text>
        <text x="72" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle">Pure Terminal Nodes</text>

        <rect x="15" y="82" width="115" height="36" rx="6" fill="#FEE2E2"/>
        <text x="72" y="104" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">Leaf 1: FAIL</text>

        <rect x="15" y="128" width="115" height="36" rx="6" fill="#D1FAE5"/>
        <text x="72" y="150" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">Leaf 2: PASS</text>

        <text x="72" y="185" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Classification: Mode</text>
        <text x="72" y="200" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Regression: Mean</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.1: The 4-Stage Decision Tree Architecture.</strong> A decision tree systematically converts raw, heterogeneous training data into a transparent, hierarchical series of binary rules, culminating in pure leaf node decisions.
  </div>
</div>"""

# 2. ANATOMY OF A DECISION TREE
SVG_DT_ANATOMY = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Anatomy of a Decision Tree: Structural Hierarchy &amp; Vocabulary</span>
    <span class="svg-badge">Figure 12.2</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 340" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="node-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
        <marker id="branch-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748B" />
        </marker>
      </defs>

      <!-- Depth Indicators on Left -->
      <g transform="translate(30, 20)">
        <rect x="0" y="10" width="70" height="24" rx="4" fill="#EEF2FF"/>
        <text x="35" y="26" font-family="monospace" font-size="10.5" font-weight="700" fill="#4338CA" text-anchor="middle">Depth 0</text>

        <rect x="0" y="110" width="70" height="24" rx="4" fill="#EEF2FF"/>
        <text x="35" y="126" font-family="monospace" font-size="10.5" font-weight="700" fill="#4338CA" text-anchor="middle">Depth 1</text>

        <rect x="0" y="225" width="70" height="24" rx="4" fill="#EEF2FF"/>
        <text x="35" y="241" font-family="monospace" font-size="10.5" font-weight="700" fill="#4338CA" text-anchor="middle">Depth 2</text>
      </g>

      <!-- ROOT NODE (Depth 0) -->
      <g transform="translate(340, 15)" filter="url(#node-shadow)">
        <rect width="200" height="58" rx="8" fill="#FFFFFF" stroke="#4F46E5" stroke-width="2.5"/>
        <text x="100" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#4338CA" text-anchor="middle">ROOT NODE (Split Condition)</text>
        <text x="100" y="42" font-family="monospace" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Study Hours ≤ 6.5?</text>
      </g>

      <!-- Branches from Root -->
      <!-- Left Branch: True -->
      <line x1="390" y1="73" x2="230" y2="120" stroke="#0284C7" stroke-width="2" marker-end="url(#branch-arrow)"/>
      <rect x="280" y="85" width="60" height="20" rx="4" fill="#F0F9FF" stroke="#BAE6FD"/>
      <text x="310" y="99" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0284C7" text-anchor="middle">True (Yes)</text>

      <!-- Right Branch: False -->
      <line x1="490" y1="73" x2="650" y2="120" stroke="#059669" stroke-width="2" marker-end="url(#branch-arrow)"/>
      <rect x="540" y="85" width="60" height="20" rx="4" fill="#ECFDF5" stroke="#A7F3D0"/>
      <text x="570" y="99" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#059669" text-anchor="middle">False (No)</text>

      <!-- INTERNAL / DECISION NODES (Depth 1) -->
      <!-- Node Left -->
      <g transform="translate(130, 120)" filter="url(#node-shadow)">
        <rect width="200" height="58" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
        <text x="100" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0284C7" text-anchor="middle">INTERNAL NODE (Child / Parent)</text>
        <text x="100" y="42" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Attendance ≤ 70%?</text>
      </g>

      <!-- Node Right (Leaf Node at Depth 1!) -->
      <g transform="translate(550, 120)" filter="url(#node-shadow)">
        <rect width="200" height="58" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="2.5"/>
        <text x="100" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">LEAF NODE (Terminal)</text>
        <text x="100" y="44" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#065F46" text-anchor="middle">PREDICT: PASS (Class 1)</text>
      </g>

      <!-- Branches from Left Internal Node -->
      <line x1="180" y1="178" x2="130" y2="230" stroke="#DC2626" stroke-width="2" marker-end="url(#branch-arrow)"/>
      <rect x="135" y="195" width="55" height="18" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
      <text x="162" y="208" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#DC2626" text-anchor="middle">≤ 70%</text>

      <line x1="280" y1="178" x2="330" y2="230" stroke="#059669" stroke-width="2" marker-end="url(#branch-arrow)"/>
      <rect x="290" y="195" width="55" height="18" rx="4" fill="#ECFDF5" stroke="#A7F3D0"/>
      <text x="317" y="208" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#059669" text-anchor="middle">&gt; 70%</text>

      <!-- LEAF NODES (Depth 2) -->
      <g transform="translate(30, 230)" filter="url(#node-shadow)">
        <rect width="180" height="55" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
        <text x="90" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">LEAF NODE (Terminal)</text>
        <text x="90" y="40" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#991B1B" text-anchor="middle">PREDICT: FAIL (Class 0)</text>
      </g>

      <g transform="translate(250, 230)" filter="url(#node-shadow)">
        <rect width="180" height="55" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
        <text x="90" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">LEAF NODE (Terminal)</text>
        <text x="90" y="40" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#065F46" text-anchor="middle">PREDICT: PASS (Class 1)</text>
      </g>

      <!-- Subtree Annotation Box -->
      <g transform="translate(480, 220)">
        <rect width="360" height="75" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-dasharray="4"/>
        <text x="180" y="24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#334155" text-anchor="middle">Structural Component Definitions</text>
        <text x="180" y="44" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">• Root: Topmost node holding full unpartitioned dataset</text>
        <text x="180" y="60" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">• Internal Node: Tests feature condition and splits into children</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.2: Structural Anatomy of a Decision Tree.</strong> Shows depth levels (0, 1, 2), root node, decision branches (true/false), internal splitting nodes, and pure terminal leaf nodes producing final predictions.
  </div>
</div>"""

# 3. PREDICTION PATH TRAVERSAL
SVG_DT_PREDICTION_PATH = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Step-by-Step Prediction Traversal: Evaluating Student Alex</span>
    <span class="svg-badge">Figure 12.3</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 260" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="path-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
        <marker id="path-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#4F46E5" />
        </marker>
      </defs>

      <!-- Query Sample Card -->
      <g transform="translate(30, 40)" filter="url(#path-shadow)">
        <rect width="180" height="170" rx="10" fill="#FFFFFF" stroke="#4F46E5" stroke-width="2"/>
        <rect width="180" height="32" rx="10" fill="#EEF2FF"/>
        <rect y="20" width="180" height="12" fill="#EEF2FF"/>
        <text x="90" y="21" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#4338CA" text-anchor="middle">NEW QUERY SAMPLE</text>
        <text x="90" y="58" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Student: Alex</text>
        <line x1="20" y1="72" x2="160" y2="72" stroke="#E2E8F0"/>
        <text x="25" y="95" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Study Hours:</text>
        <text x="155" y="95" font-family="monospace" font-size="12" font-weight="700" fill="#0F172A" text-anchor="end">4.5 hrs</text>
        <text x="25" y="120" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Attendance:</text>
        <text x="155" y="120" font-family="monospace" font-size="12" font-weight="700" fill="#0F172A" text-anchor="end">82.0%</text>
        <rect x="20" y="138" width="140" height="24" rx="4" fill="#F1F5F9"/>
        <text x="90" y="154" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" fill="#475569" text-anchor="middle">Traversing Tree...</text>
      </g>

      <!-- Step 1 Arrow -->
      <line x1="210" y1="125" x2="255" y2="125" stroke="#4F46E5" stroke-width="2.5" marker-end="url(#path-arrow)"/>

      <!-- Step 1: Root Evaluation -->
      <g transform="translate(265, 40)" filter="url(#path-shadow)">
        <rect width="180" height="170" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect width="180" height="32" rx="10" fill="#F8FAFC"/>
        <rect y="20" width="180" height="12" fill="#F8FAFC"/>
        <text x="90" y="21" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">STEP 1: ROOT TEST</text>
        <text x="90" y="60" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" fill="#0F172A" text-anchor="middle">Study Hours ≤ 6.5?</text>
        <rect x="20" y="75" width="140" height="42" rx="6" fill="#EEF2FF" stroke="#C7D2FE"/>
        <text x="90" y="93" font-family="system-ui, sans-serif" font-size="11" fill="#4338CA" text-anchor="middle">Alex: 4.5 ≤ 6.5</text>
        <text x="90" y="108" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">→ Result is TRUE</text>
        <text x="90" y="145" font-family="system-ui, sans-serif" font-size="11" fill="#059669" text-anchor="middle">• Follow Left Branch</text>
        <text x="90" y="165" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">Branch to Child Node</text>
      </g>

      <!-- Step 2 Arrow -->
      <line x1="445" y1="125" x2="490" y2="125" stroke="#4F46E5" stroke-width="2.5" marker-end="url(#path-arrow)"/>

      <!-- Step 2: Internal Node Evaluation -->
      <g transform="translate(500, 40)" filter="url(#path-shadow)">
        <rect width="180" height="170" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect width="180" height="32" rx="10" fill="#F8FAFC"/>
        <rect y="20" width="180" height="12" fill="#F8FAFC"/>
        <text x="90" y="21" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">STEP 2: INTERNAL TEST</text>
        <text x="90" y="60" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" fill="#0F172A" text-anchor="middle">Attendance ≤ 70%?</text>
        <rect x="20" y="75" width="140" height="42" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
        <text x="90" y="93" font-family="system-ui, sans-serif" font-size="11" fill="#065F46" text-anchor="middle">Alex: 82% ≤ 70%</text>
        <text x="90" y="108" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">→ Result is FALSE</text>
        <text x="90" y="145" font-family="system-ui, sans-serif" font-size="11" fill="#0284C7" text-anchor="middle">• Follow Right Branch</text>
        <text x="90" y="165" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">Terminates at Leaf</text>
      </g>

      <!-- Step 3 Arrow -->
      <line x1="680" y1="125" x2="720" y2="125" stroke="#4F46E5" stroke-width="2.5" marker-end="url(#path-arrow)"/>

      <!-- Step 3: Terminal Leaf -->
      <g transform="translate(730, 40)" filter="url(#path-shadow)">
        <rect width="125" height="170" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
        <rect width="125" height="32" rx="10" fill="#D1FAE5"/>
        <rect y="20" width="125" height="12" fill="#D1FAE5"/>
        <text x="62" y="21" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">FINAL LEAF</text>
        <text x="62" y="65" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" fill="#065F46" text-anchor="middle">Terminal Decision</text>
        <circle cx="62" cy="100" r="22" fill="#10B981"/>
        <text x="62" y="106" font-family="system-ui, sans-serif" font-size="18" font-weight="900" fill="#FFFFFF" text-anchor="middle">✓</text>
        <text x="62" y="145" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#065F46" text-anchor="middle">PASS</text>
        <text x="62" y="162" font-family="system-ui, sans-serif" font-size="10" fill="#047857" text-anchor="middle">Class 1</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.3: Prediction Traversal Walkthrough.</strong> Follows query student Alex (Study Hours = 4.5, Attendance = 82%) down the left branch of Root, then right branch of Internal Node to reach Leaf → Predicted: PASS.
  </div>
</div>"""

# 4. CLASSIFICATION VS REGRESSION TREES
SVG_CLASSIFICATION_VS_REGRESSION = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Classification Trees vs. Regression Trees</span>
    <span class="svg-badge">Figure 12.4</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 270" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="comp-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- LEFT: Classification Tree -->
      <g transform="translate(30, 20)" filter="url(#comp-shadow)">
        <rect width="395" height="225" rx="12" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2"/>
        <rect width="395" height="38" rx="12" fill="#EFF6FF"/>
        <rect y="26" width="395" height="12" fill="#EFF6FF"/>
        <text x="197" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1D4ED8" text-anchor="middle">CLASSIFICATION TREE (Discrete Categories)</text>
        
        <text x="25" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Target Variable:</text>
        <text x="135" y="65" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Categorical Label (e.g. Pass / Fail, Apple / Orange)</text>

        <text x="25" y="90" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Leaf Output:</text>
        <text x="135" y="90" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Statistical Mode (Majority Class) or Class Probabilities</text>

        <text x="25" y="115" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Split Criteria:</text>
        <text x="135" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Gini Impurity, Entropy / Information Gain</text>

        <text x="25" y="140" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Core Objective:</text>
        <text x="135" y="140" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Maximize purity of target classes in child partitions</text>

        <!-- Mini Visual: Discrete Classes -->
        <g transform="translate(40, 160)">
          <rect width="140" height="48" rx="6" fill="#FEE2E2" stroke="#FCA5A5"/>
          <text x="70" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#991B1B" text-anchor="middle">Leaf 1: FAIL</text>
          <text x="70" y="38" font-family="monospace" font-size="9.5" fill="#991B1B" text-anchor="middle">p(Fail)=95%</text>

          <rect x="175" y="0" width="140" height="48" rx="6" fill="#D1FAE5" stroke="#6EE7B7"/>
          <text x="245" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#065F46" text-anchor="middle">Leaf 2: PASS</text>
          <text x="245" y="38" font-family="monospace" font-size="9.5" fill="#065F46" text-anchor="middle">p(Pass)=98%</text>
        </g>
      </g>

      <!-- RIGHT: Regression Tree -->
      <g transform="translate(455, 20)" filter="url(#comp-shadow)">
        <rect width="395" height="225" rx="12" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
        <rect width="395" height="38" rx="12" fill="#ECFDF5"/>
        <rect y="26" width="395" height="12" fill="#ECFDF5"/>
        <text x="197" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#047857" text-anchor="middle">REGRESSION TREE (Continuous Quantities)</text>

        <text x="25" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Target Variable:</text>
        <text x="135" y="65" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Continuous Float (e.g. House Price $, Temperature °C)</text>

        <text x="25" y="90" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Leaf Output:</text>
        <text x="135" y="90" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Arithmetic Mean (ȳ) of training points in that leaf</text>

        <text x="25" y="115" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Split Criteria:</text>
        <text x="135" y="115" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Squared Error (Variance Reduction), Absolute Error</text>

        <text x="25" y="140" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Core Objective:</text>
        <text x="135" y="140" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Minimize target variance / squared residuals in children</text>

        <!-- Mini Visual: Continuous Mean -->
        <g transform="translate(40, 160)">
          <rect width="140" height="48" rx="6" fill="#F0F9FF" stroke="#BAE6FD"/>
          <text x="70" y="20" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0369A1" text-anchor="middle">Leaf 1: Small Home</text>
          <text x="70" y="38" font-family="monospace" font-size="10" font-weight="700" fill="#0284C7" text-anchor="middle">ȳ = $148.5k</text>

          <rect x="175" y="0" width="140" height="48" rx="6" fill="#F0F9FF" stroke="#BAE6FD"/>
          <text x="245" y="20" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0369A1" text-anchor="middle">Leaf 2: Large Home</text>
          <text x="245" y="38" font-family="monospace" font-size="10" font-weight="700" fill="#0284C7" text-anchor="middle">ȳ = $312.8k</text>
        </g>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.4: Fundamental Comparison: Classification vs. Regression Trees.</strong> Highlights differences in target variable types, splitting criteria (Gini/Entropy vs. Squared Error), and leaf predictions (majority class vs. numerical mean).
  </div>
</div>"""

# 5. CANDIDATE SPLIT BEFORE AND AFTER
SVG_CANDIDATE_SPLIT_BEFORE_AFTER = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Split Selection: Class Homogeneity Increase</span>
    <span class="svg-badge">Figure 12.5</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 250" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="split-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
        <marker id="split-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284C7" />
        </marker>
      </defs>

      <!-- BEFORE SPLIT (Parent) -->
      <g transform="translate(50, 30)" filter="url(#split-shadow)">
        <rect width="250" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect width="250" height="34" rx="10" fill="#F1F5F9"/>
        <rect y="22" width="250" height="12" fill="#F1F5F9"/>
        <text x="125" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#334155" text-anchor="middle">BEFORE SPLIT (Parent Node)</text>
        
        <text x="125" y="60" font-family="system-ui, sans-serif" font-size="11.5" font-weight="600" fill="#0F172A" text-anchor="middle">20 Students Total</text>
        
        <!-- Bars of classes -->
        <rect x="35" y="75" width="85" height="45" rx="6" fill="#FEE2E2" stroke="#FCA5A5"/>
        <text x="77" y="96" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">10 Fail</text>
        <text x="77" y="112" font-family="monospace" font-size="9.5" fill="#991B1B" text-anchor="middle">p = 0.50</text>

        <rect x="130" y="75" width="85" height="45" rx="6" fill="#D1FAE5" stroke="#6EE7B7"/>
        <text x="172" y="96" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">10 Pass</text>
        <text x="172" y="112" font-family="monospace" font-size="9.5" fill="#065F46" text-anchor="middle">p = 0.50</text>

        <rect x="35" y="135" width="180" height="30" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="125" y="155" font-family="monospace" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">Max Impurity (Gini=0.50)</text>
        <text x="125" y="178" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">50/50 Complete Uncertainty</text>
      </g>

      <!-- Split Decision Connector -->
      <g transform="translate(320, 105)">
        <line x1="0" y1="20" x2="60" y2="20" stroke="#0284C7" stroke-width="2.5" marker-end="url(#split-arrow)"/>
        <rect x="5" y="-5" width="50" height="18" rx="4" fill="#E0F2FE"/>
        <text x="30" y="8" font-family="monospace" font-size="9.5" font-weight="700" fill="#0369A1" text-anchor="middle">SPLIT</text>
        <text x="30" y="48" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" text-anchor="middle">Hours ≥ 5</text>
      </g>

      <!-- AFTER SPLIT (2 Children) -->
      <g transform="translate(410, 30)" filter="url(#split-shadow)">
        <rect width="420" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect width="420" height="34" rx="10" fill="#F0FDF4"/>
        <rect y="22" width="420" height="12" fill="#F0FDF4"/>
        <text x="210" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#15803D" text-anchor="middle">AFTER SPLIT (Homogeneous Child Groups)</text>

        <!-- Left Child -->
        <g transform="translate(20, 50)">
          <rect width="180" height="120" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
          <text x="90" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Left: Hours &lt; 5 (N=8)</text>
          
          <rect x="15" y="32" width="70" height="38" rx="4" fill="#FEE2E2"/>
          <text x="50" y="49" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#991B1B" text-anchor="middle">7 Fail</text>
          <text x="50" y="63" font-family="monospace" font-size="9" fill="#991B1B" text-anchor="middle">87.5%</text>

          <rect x="95" y="32" width="70" height="38" rx="4" fill="#D1FAE5"/>
          <text x="130" y="49" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#065F46" text-anchor="middle">1 Pass</text>
          <text x="130" y="63" font-family="monospace" font-size="9" fill="#065F46" text-anchor="middle">12.5%</text>

          <rect x="15" y="78" width="150" height="24" rx="4" fill="#ECFDF5"/>
          <text x="90" y="94" font-family="monospace" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">Gini = 0.2188 (Low!)</text>
          <text x="90" y="112" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Highly purified Fail group</text>
        </g>

        <!-- Right Child -->
        <g transform="translate(220, 50)">
          <rect width="180" height="120" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
          <text x="90" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Right: Hours ≥ 5 (N=12)</text>
          
          <rect x="15" y="32" width="70" height="38" rx="4" fill="#FEE2E2"/>
          <text x="50" y="49" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#991B1B" text-anchor="middle">3 Fail</text>
          <text x="50" y="63" font-family="monospace" font-size="9" fill="#991B1B" text-anchor="middle">25.0%</text>

          <rect x="95" y="32" width="70" height="38" rx="4" fill="#D1FAE5"/>
          <text x="130" y="49" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#065F46" text-anchor="middle">9 Pass</text>
          <text x="130" y="63" font-family="monospace" font-size="9" fill="#065F46" text-anchor="middle">75.0%</text>

          <rect x="15" y="78" width="150" height="24" rx="4" fill="#ECFDF5"/>
          <text x="90" y="94" font-family="monospace" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">Gini = 0.3750 (Drop!)</text>
          <text x="90" y="112" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Strong Pass concentration</text>
        </g>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.5: Homogeneity Increase via Split.</strong> The parent node is completely mixed (Gini = 0.50). Splitting on Study Hours ≥ 5 segregates the data into two much purer subsets, achieving a weighted child Gini of only 0.3125.
  </div>
</div>"""

# 6. GINI IMPURITY CURVE
SVG_GINI_IMPURITY_CURVE = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Gini Impurity Function: 1 - Σ pᵢ²</span>
    <span class="svg-badge">Figure 12.6</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 270" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="gini-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- Graph Plot Area (Left 520px) -->
      <g transform="translate(60, 30)">
        <!-- Axes -->
        <line x1="60" y1="180" x2="480" y2="180" stroke="#0F172A" stroke-width="1.5"/>
        <line x1="60" y1="20" x2="60" y2="180" stroke="#0F172A" stroke-width="1.5"/>

        <!-- Grid Lines -->
        <line x1="60" y1="100" x2="480" y2="100" stroke="#E2E8F0" stroke-dasharray="3"/>
        <line x1="60" y1="20" x2="480" y2="20" stroke="#E2E8F0" stroke-dasharray="3"/>
        <line x1="270" y1="20" x2="270" y2="180" stroke="#E2E8F0" stroke-dasharray="3"/>

        <!-- Y Axis Labels -->
        <text x="50" y="184" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0.0</text>
        <text x="50" y="104" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0.25</text>
        <text x="50" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0284C7" text-anchor="end">0.50 (Max)</text>
        <text x="-100" y="15" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle" transform="rotate(-90)">Gini Impurity →</text>

        <!-- X Axis Labels -->
        <text x="60" y="200" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">0.0 (Pure 0)</text>
        <text x="270" y="200" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">0.50 (50/50 Balanced)</text>
        <text x="480" y="200" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">1.0 (Pure 1)</text>
        <text x="270" y="218" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Proportion of Positive Class (p₁) →</text>

        <!-- Parabola Path for Gini: Gini = 2*p*(1-p). At p=0: 0, p=0.5: 0.5 (y=20), p=1: 0 (y=180) -->
        <path d="M 60 180 Q 270 -140 480 180" fill="none" stroke="#0284C7" stroke-width="3.5"/>

        <!-- Peak Point Dot -->
        <circle cx="270" cy="20" r="5" fill="#EF4444"/>
        <text x="270" y="12" font-family="monospace" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">Max: Gini = 0.500</text>

        <!-- Pure Base Points -->
        <circle cx="60" cy="180" r="4.5" fill="#10B981"/>
        <circle cx="480" cy="180" r="4.5" fill="#10B981"/>
      </g>

      <!-- Key Insights Box on Right (300px) -->
      <g transform="translate(560, 30)" filter="url(#gini-shadow)">
        <rect width="280" height="200" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
        <text x="140" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0284C7" text-anchor="middle">Gini Key Properties</text>

        <rect x="15" y="40" width="250" height="42" rx="6" fill="#ECFDF5"/>
        <text x="25" y="56" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#065F46">Pure Node (Gini = 0.0):</text>
        <text x="25" y="72" font-family="system-ui, sans-serif" font-size="10.5" fill="#065F46">100% of samples belong to one class.</text>

        <rect x="15" y="90" width="250" height="42" rx="6" fill="#FEF2F2"/>
        <text x="25" y="106" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B">Max Impurity (Gini = 0.50):</text>
        <text x="25" y="122" font-family="system-ui, sans-serif" font-size="10.5" fill="#991B1B">Even 50/50 binary split. Peak chaos.</text>

        <text x="140" y="152" font-family="monospace" font-size="11" fill="#334155" text-anchor="middle">Formula: 1 - (p&#8320;² + p₁²)</text>
        <text x="140" y="172" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">Fast to compute: Zero logarithms!</text>
        <text x="140" y="188" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0284C7" text-anchor="middle">Default criterion in scikit-learn</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.6: The Inverted Parabola of Gini Impurity.</strong> For binary classification, Gini Impurity reaches its maximum value of 0.50 when classes are equally balanced (50/50), and drops to exactly 0.0 when a node is completely pure.
  </div>
</div>"""

# 7. ENTROPY CURVE
SVG_ENTROPY_CURVE = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Entropy Function: - Σ pᵢ log₂(pᵢ)</span>
    <span class="svg-badge">Figure 12.7</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 270" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="ent-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- Graph Plot Area (Left 520px) -->
      <g transform="translate(60, 30)">
        <line x1="60" y1="180" x2="480" y2="180" stroke="#0F172A" stroke-width="1.5"/>
        <line x1="60" y1="20" x2="60" y2="180" stroke="#0F172A" stroke-width="1.5"/>

        <!-- Grid Lines -->
        <line x1="60" y1="100" x2="480" y2="100" stroke="#E2E8F0" stroke-dasharray="3"/>
        <line x1="60" y1="20" x2="480" y2="20" stroke="#E2E8F0" stroke-dasharray="3"/>
        <line x1="270" y1="20" x2="270" y2="180" stroke="#E2E8F0" stroke-dasharray="3"/>

        <!-- Y Axis Labels -->
        <text x="50" y="184" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0.0</text>
        <text x="50" y="104" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0.50</text>
        <text x="50" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#7C3AED" text-anchor="end">1.00 (Max)</text>
        <text x="-100" y="15" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle" transform="rotate(-90)">Entropy (bits) →</text>

        <!-- X Axis Labels -->
        <text x="60" y="200" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">0.0 (Pure 0)</text>
        <text x="270" y="200" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">0.50 (50/50 Balanced)</text>
        <text x="480" y="200" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">1.0 (Pure 1)</text>
        <text x="270" y="218" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Proportion of Positive Class (p₁) →</text>

        <!-- Bell curve of Entropy: H = -p*log2(p) - (1-p)*log2(1-p). Reaches 1.0 at 270 (y=20) -->
        <path d="M 60 180 C 130 50, 200 20, 270 20 C 340 20, 410 50, 480 180" fill="none" stroke="#7C3AED" stroke-width="3.5"/>

        <!-- Peak Point Dot -->
        <circle cx="270" cy="20" r="5" fill="#EF4444"/>
        <text x="270" y="12" font-family="monospace" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">Max: Entropy = 1.000 bit</text>

        <!-- Pure Base Points -->
        <circle cx="60" cy="180" r="4.5" fill="#10B981"/>
        <circle cx="480" cy="180" r="4.5" fill="#10B981"/>
      </g>

      <!-- Key Insights Box on Right (300px) -->
      <g transform="translate(560, 30)" filter="url(#ent-shadow)">
        <rect width="280" height="200" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
        <text x="140" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#7C3AED" text-anchor="middle">Entropy Key Properties</text>

        <rect x="15" y="40" width="250" height="42" rx="6" fill="#ECFDF5"/>
        <text x="25" y="56" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#065F46">Pure Node (H = 0.0 bits):</text>
        <text x="25" y="72" font-family="system-ui, sans-serif" font-size="10.5" fill="#065F46">Zero surprise. Certain outcome.</text>

        <rect x="15" y="90" width="250" height="42" rx="6" fill="#FEF2F2"/>
        <text x="25" y="106" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B">Max Uncertainty (H = 1.0 bit):</text>
        <text x="25" y="122" font-family="system-ui, sans-serif" font-size="10.5" fill="#991B1B">Fair coin flip. Equal uncertainty.</text>

        <text x="140" y="152" font-family="monospace" font-size="10.5" fill="#334155" text-anchor="middle">- Σ pᵢ log₂(pᵢ)</text>
        <text x="140" y="172" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Origin: Claude Shannon (Info Theory)</text>
        <text x="140" y="188" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#7C3AED" text-anchor="middle">Convention: 0 × log₂(0) = 0</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.7: Information Theory Entropy Function.</strong> Measures impurity in units of bits. Complete purity is 0 bits, while an equal 50/50 balance produces maximum uncertainty of exactly 1.000 bit.
  </div>
</div>"""

# 8. ENTROPY VS GINI COMPARISON
SVG_ENTROPY_VS_GINI = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Mathematical Comparison: Entropy vs. Gini Impurity</span>
    <span class="svg-badge">Figure 12.8</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 270" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="comp-shadow2" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- Curve Plot (Left 540px) -->
      <g transform="translate(60, 30)">
        <line x1="60" y1="180" x2="480" y2="180" stroke="#0F172A" stroke-width="1.5"/>
        <line x1="60" y1="20" x2="60" y2="180" stroke="#0F172A" stroke-width="1.5"/>

        <line x1="60" y1="100" x2="480" y2="100" stroke="#E2E8F0" stroke-dasharray="3"/>
        <line x1="60" y1="20" x2="480" y2="20" stroke="#E2E8F0" stroke-dasharray="3"/>
        <line x1="270" y1="20" x2="270" y2="180" stroke="#E2E8F0" stroke-dasharray="3"/>

        <!-- Y Axis -->
        <text x="50" y="184" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0.0</text>
        <text x="50" y="104" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0.50</text>
        <text x="50" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">1.00</text>
        <text x="-100" y="15" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle" transform="rotate(-90)">Impurity Measure →</text>

        <!-- X Axis -->
        <text x="60" y="200" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569" text-anchor="middle">0.0</text>
        <text x="165" y="200" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569" text-anchor="middle">0.25</text>
        <text x="270" y="200" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0F172A" text-anchor="middle">0.50</text>
        <text x="375" y="200" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569" text-anchor="middle">0.75</text>
        <text x="480" y="200" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569" text-anchor="middle">1.0</text>
        <text x="270" y="218" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Proportion of Class 1 (p) →</text>

        <!-- Curve 1: Entropy (Purple) max 1.0 at 270 (y=20) -->
        <path d="M 60 180 C 130 50, 200 20, 270 20 C 340 20, 410 50, 480 180" fill="none" stroke="#7C3AED" stroke-width="3"/>

        <!-- Curve 2: Scaled Gini (4 * p * (1-p)) max 1.0 at 270 (y=20) (dashed dark blue) -->
        <path d="M 60 180 Q 270 -140 480 180" fill="none" stroke="#0284C7" stroke-width="2.5" stroke-dasharray="5 3"/>

        <!-- Curve 3: Raw Gini (Blue) max 0.50 at 270 (y=100) -->
        <path d="M 60 180 Q 270 20 480 180" fill="none" stroke="#2563EB" stroke-width="3"/>

        <!-- Legend inside chart -->
        <g transform="translate(180, 40)">
          <line x1="0" y1="0" x2="25" y2="0" stroke="#7C3AED" stroke-width="3"/>
          <text x="32" y="4" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#7C3AED">Entropy H(p) [Max=1.0]</text>

          <line x1="0" y1="18" x2="25" y2="18" stroke="#0284C7" stroke-width="2.5" stroke-dasharray="4"/>
          <text x="32" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0284C7">Scaled Gini (2 × Gini) [Max=1.0]</text>

          <line x1="0" y1="36" x2="25" y2="36" stroke="#2563EB" stroke-width="3"/>
          <text x="32" y="40" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#2563EB">Raw Gini Impurity [Max=0.5]</text>
        </g>
      </g>

      <!-- Practical Comparison Box (Right) -->
      <g transform="translate(580, 30)" filter="url(#comp-shadow2)">
        <rect width="270" height="200" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <text x="135" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Which Criterion to Pick?</text>

        <rect x="15" y="40" width="240" height="65" rx="6" fill="#EFF6FF"/>
        <text x="25" y="58" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1D4ED8">Gini Impurity (Default):</text>
        <text x="25" y="74" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Faster compute (no log₂ operations)</text>
        <text x="25" y="90" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Recommended for large datasets &amp; speed</text>

        <rect x="15" y="115" width="240" height="65" rx="6" fill="#F5F3FF"/>
        <text x="25" y="133" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#6D28D9">Entropy (Logarithmic):</text>
        <text x="25" y="149" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Slightly steeper penalty near extremes</text>
        <text x="25" y="165" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Yields nearly identical trees &gt;98% of time</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.8: Overlay Comparison of Impurity Metrics.</strong> When Gini is multiplied by 2 (scaled Gini), its shape closely mirrors Entropy. In practice, both criteria yield identical splitting decisions in over 98% of real-world scenarios.
  </div>
</div>"""

# 9. INFORMATION GAIN WORKED EXAMPLE
SVG_INFORMATION_GAIN_WORKED = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Information Gain Calculation: Step-by-Step Entropy Reduction</span>
    <span class="svg-badge">Figure 12.9</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 280" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="ig-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
        <marker id="ig-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748B" />
        </marker>
      </defs>

      <!-- PARENT NODE (Top Center) -->
      <g transform="translate(330, 15)" filter="url(#ig-shadow)">
        <rect width="220" height="72" rx="10" fill="#FFFFFF" stroke="#4F46E5" stroke-width="2"/>
        <text x="110" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">PARENT NODE (N = 20)</text>
        <text x="110" y="38" font-family="system-ui, sans-serif" font-size="11" fill="#0F172A" text-anchor="middle">10 Pass (p=0.5) • 10 Fail (p=0.5)</text>
        <rect x="25" y="46" width="170" height="20" rx="4" fill="#EEF2FF"/>
        <text x="110" y="60" font-family="monospace" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">H(parent) = 1.0000 bit</text>
      </g>

      <!-- Branching lines -->
      <line x1="390" y1="87" x2="230" y2="135" stroke="#94A3B8" stroke-width="2" marker-end="url(#ig-arrow)"/>
      <rect x="280" y="98" width="60" height="18" rx="4" fill="#F1F5F9"/>
      <text x="310" y="111" font-family="monospace" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">Hours &lt; 5</text>

      <line x1="490" y1="87" x2="650" y2="135" stroke="#94A3B8" stroke-width="2" marker-end="url(#ig-arrow)"/>
      <rect x="540" y="98" width="60" height="18" rx="4" fill="#F1F5F9"/>
      <text x="570" y="111" font-family="monospace" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">Hours ≥ 5</text>

      <!-- LEFT CHILD -->
      <g transform="translate(120, 135)" filter="url(#ig-shadow)">
        <rect width="220" height="72" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
        <text x="110" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0284C7" text-anchor="middle">LEFT CHILD (N₁ = 8)</text>
        <text x="110" y="38" font-family="system-ui, sans-serif" font-size="10.5" fill="#0F172A" text-anchor="middle">1 Pass (12.5%) • 7 Fail (87.5%)</text>
        <rect x="25" y="46" width="170" height="20" rx="4" fill="#F0F9FF"/>
        <text x="110" y="60" font-family="monospace" font-size="11" font-weight="700" fill="#0369A1" text-anchor="middle">H(left) = 0.5436 bit</text>
      </g>

      <!-- RIGHT CHILD -->
      <g transform="translate(540, 135)" filter="url(#ig-shadow)">
        <rect width="220" height="72" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
        <text x="110" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">RIGHT CHILD (N₂ = 12)</text>
        <text x="110" y="38" font-family="system-ui, sans-serif" font-size="10.5" fill="#0F172A" text-anchor="middle">9 Pass (75.0%) • 3 Fail (25.0%)</text>
        <rect x="25" y="46" width="170" height="20" rx="4" fill="#ECFDF5"/>
        <text x="110" y="60" font-family="monospace" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">H(right) = 0.8113 bit</text>
      </g>

      <!-- BOTTOM EQUATION RESULT BAR -->
      <g transform="translate(120, 225)" filter="url(#ig-shadow)">
        <rect width="640" height="42" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
        <text x="320" y="20" font-family="monospace" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">IG = H(parent) - [ (8/20)×0.5436 + (12/20)×0.8113 ] = 1.0000 - 0.7042 = 0.2958 bits</text>
        <text x="320" y="34" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#059669" text-anchor="middle">✓ Split successfully reduces uncertainty by 0.2958 bits!</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.9: Complete Information Gain Arithmetic.</strong> Parent entropy of 1.0000 bit is reduced to a weighted child entropy of 0.7042 bit, yielding a verified Information Gain of 0.2958 bits.
  </div>
</div>"""

# 10. ACTUAL TRAINED DECISION TREE VISUALIZATION
SVG_ACTUAL_TRAINED_TREE = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Fitted Scikit-Learn Decision Tree (max_depth=3)</span>
    <span class="svg-badge">Figure 12.10</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 330" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="tree-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
        <marker id="t-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748B" />
        </marker>
      </defs>

      <!-- ROOT NODE (Depth 0) -->
      <g transform="translate(340, 10)" filter="url(#tree-shadow)">
        <rect width="200" height="66" rx="6" fill="#FFFBEB" stroke="#F59E0B" stroke-width="2"/>
        <text x="100" y="16" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#B45309" text-anchor="middle">Study_Hours ≤ 6.45</text>
        <text x="100" y="32" font-family="monospace" font-size="10" fill="#0F172A" text-anchor="middle">gini = 0.500 | samples = 192</text>
        <text x="100" y="47" font-family="monospace" font-size="10" fill="#0F172A" text-anchor="middle">value = [96, 96]</text>
        <text x="100" y="61" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">class = Fail (Tied)</text>
      </g>

      <!-- Depth 1 Connectors -->
      <line x1="390" y1="76" x2="220" y2="105" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#t-arrow)"/>
      <line x1="490" y1="76" x2="660" y2="105" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#t-arrow)"/>

      <!-- DEPTH 1 - LEFT NODE -->
      <g transform="translate(120, 105)" filter="url(#tree-shadow)">
        <rect width="200" height="66" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
        <text x="100" y="16" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">Attendance_Pct ≤ 75.2</text>
        <text x="100" y="32" font-family="monospace" font-size="10" fill="#0F172A" text-anchor="middle">gini = 0.165 | samples = 101</text>
        <text x="100" y="47" font-family="monospace" font-size="10" fill="#0F172A" text-anchor="middle">value = [92, 9]</text>
        <text x="100" y="61" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">class = FAIL (91.1%)</text>
      </g>

      <!-- DEPTH 1 - RIGHT NODE -->
      <g transform="translate(560, 105)" filter="url(#tree-shadow)">
        <rect width="200" height="66" rx="6" fill="#D1FAE5" stroke="#10B981" stroke-width="1.5"/>
        <text x="100" y="16" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">Attendance_Pct ≤ 68.0</text>
        <text x="100" y="32" font-family="monospace" font-size="10" fill="#0F172A" text-anchor="middle">gini = 0.084 | samples = 91</text>
        <text x="100" y="47" font-family="monospace" font-size="10" fill="#0F172A" text-anchor="middle">value = [4, 87]</text>
        <text x="100" y="61" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">class = PASS (95.6%)</text>
      </g>

      <!-- Depth 2 Connectors -->
      <line x1="170" y1="171" x2="100" y2="210" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#t-arrow)"/>
      <line x1="270" y1="171" x2="340" y2="210" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#t-arrow)"/>
      <line x1="610" y1="171" x2="540" y2="210" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#t-arrow)"/>
      <line x1="710" y1="171" x2="780" y2="210" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#t-arrow)"/>

      <!-- LEAF NODES (Depth 2) -->
      <!-- Leaf 1 (Pure Fail) -->
      <g transform="translate(20, 210)" filter="url(#tree-shadow)">
        <rect width="160" height="62" rx="6" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
        <text x="80" y="18" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" fill="#991B1B" text-anchor="middle">LEAF: PURE FAIL</text>
        <text x="80" y="34" font-family="monospace" font-size="9.5" fill="#0F172A" text-anchor="middle">gini = 0.000 | n = 86</text>
        <text x="80" y="50" font-family="monospace" font-size="9.5" font-weight="700" fill="#991B1B" text-anchor="middle">value = [86, 0]</text>
      </g>

      <!-- Leaf 2 (Near Pure Fail) -->
      <g transform="translate(260, 210)" filter="url(#tree-shadow)">
        <rect width="160" height="62" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
        <text x="80" y="18" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" fill="#991B1B" text-anchor="middle">LEAF: FAIL</text>
        <text x="80" y="34" font-family="monospace" font-size="9.5" fill="#0F172A" text-anchor="middle">gini = 0.480 | n = 15</text>
        <text x="80" y="50" font-family="monospace" font-size="9.5" font-weight="700" fill="#991B1B" text-anchor="middle">value = [6, 9]</text>
      </g>

      <!-- Leaf 3 (Near Pure Pass) -->
      <g transform="translate(460, 210)" filter="url(#tree-shadow)">
        <rect width="160" height="62" rx="6" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
        <text x="80" y="18" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" fill="#065F46" text-anchor="middle">LEAF: PASS</text>
        <text x="80" y="34" font-family="monospace" font-size="9.5" fill="#0F172A" text-anchor="middle">gini = 0.444 | n = 6</text>
        <text x="80" y="50" font-family="monospace" font-size="9.5" font-weight="700" fill="#065F46" text-anchor="middle">value = [2, 4]</text>
      </g>

      <!-- Leaf 4 (Pure Pass) -->
      <g transform="translate(700, 210)" filter="url(#tree-shadow)">
        <rect width="160" height="62" rx="6" fill="#ECFDF5" stroke="#059669" stroke-width="2"/>
        <text x="80" y="18" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" fill="#065F46" text-anchor="middle">LEAF: PURE PASS</text>
        <text x="80" y="34" font-family="monospace" font-size="9.5" fill="#0F172A" text-anchor="middle">gini = 0.046 | n = 85</text>
        <text x="80" y="50" font-family="monospace" font-size="9.5" font-weight="700" fill="#065F46" text-anchor="middle">value = [2, 83]</text>
      </g>

      <text x="440" y="305" font-family="system-ui, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Generated via scikit-learn export_text / plot_tree logic on 192 training samples</text>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.10: Actual Fitted Scikit-Learn Decision Tree.</strong> Displays split thresholds (Study_Hours ≤ 6.45, Attendance ≤ 75.2%), node sample counts, Gini impurities, and class distributions across all internal and leaf nodes.
  </div>
</div>"""

# 11. DECISION BOUNDARIES ACROSS DEPTHS
SVG_DECISION_BOUNDARIES_DEPTH = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Decision Boundaries Across Depths: Axis-Aligned Orthogonal Splits</span>
    <span class="svg-badge">Figure 12.11</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 280" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="bound-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- Panel 1: max_depth = 1 (Stump) -->
      <g transform="translate(30, 20)" filter="url(#bound-shadow)">
        <rect width="250" height="230" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect width="250" height="32" rx="10" fill="#F8FAFC"/>
        <rect y="20" width="250" height="12" fill="#F8FAFC"/>
        <text x="125" y="21" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">max_depth = 1 (Decision Stump)</text>

        <!-- 2D Space -->
        <g transform="translate(35, 45)">
          <rect width="180" height="140" fill="#FFFFFF" stroke="#0F172A" stroke-width="1.5"/>
          <!-- Single vertical split at x = 75 (Study Hours = 6.5) -->
          <rect x="0" y="0" width="75" height="140" fill="#FEE2E2" fill-opacity="0.4"/>
          <rect x="75" y="0" width="105" height="140" fill="#D1FAE5" fill-opacity="0.4"/>
          <line x1="75" y1="0" x2="75" y2="140" stroke="#DC2626" stroke-width="2.5"/>

          <!-- Points -->
          <circle cx="35" cy="95" r="4" fill="#EF4444"/>
          <circle cx="50" cy="110" r="4" fill="#EF4444"/>
          <circle cx="60" cy="40" r="4" fill="#EF4444"/>
          <circle cx="110" cy="35" r="4" fill="#10B981"/>
          <circle cx="140" cy="50" r="4" fill="#10B981"/>
          <circle cx="125" cy="85" r="4" fill="#10B981"/>
          <circle cx="155" cy="115" r="4" fill="#10B981"/>
        </g>
        <text x="125" y="204" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" fill="#DC2626" text-anchor="middle">Underfitting: 1 Line Split</text>
        <text x="125" y="218" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" text-anchor="middle">High Bias • Train Acc: 95.3%</text>
      </g>

      <!-- Panel 2: max_depth = 3 (Optimal) -->
      <g transform="translate(315, 20)" filter="url(#bound-shadow)">
        <rect width="250" height="230" rx="10" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
        <rect width="250" height="32" rx="10" fill="#ECFDF5"/>
        <rect y="20" width="250" height="12" fill="#ECFDF5"/>
        <text x="125" y="21" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#065F46" text-anchor="middle">max_depth = 3 (Balanced Sweet Spot)</text>

        <!-- 2D Space -->
        <g transform="translate(35, 45)">
          <rect width="180" height="140" fill="#FFFFFF" stroke="#0F172A" stroke-width="1.5"/>
          <!-- Regions -->
          <rect x="0" y="0" width="75" height="140" fill="#FEE2E2" fill-opacity="0.4"/>
          <rect x="75" y="0" width="105" height="140" fill="#D1FAE5" fill-opacity="0.4"/>
          <!-- Horizontal split on left -->
          <rect x="0" y="0" width="75" height="50" fill="#D1FAE5" fill-opacity="0.3"/>
          <line x1="75" y1="0" x2="75" y2="140" stroke="#0284C7" stroke-width="2"/>
          <line x1="0" y1="50" x2="75" y2="50" stroke="#0284C7" stroke-width="2"/>
          <!-- Horizontal split on right -->
          <line x1="75" y1="100" x2="180" y2="100" stroke="#0284C7" stroke-width="2"/>
          <rect x="75" y="100" width="105" height="40" fill="#FEE2E2" fill-opacity="0.3"/>

          <!-- Points -->
          <circle cx="35" cy="95" r="4" fill="#EF4444"/>
          <circle cx="50" cy="110" r="4" fill="#EF4444"/>
          <circle cx="55" cy="35" r="4" fill="#10B981"/>
          <circle cx="110" cy="35" r="4" fill="#10B981"/>
          <circle cx="140" cy="50" r="4" fill="#10B981"/>
          <circle cx="125" cy="85" r="4" fill="#10B981"/>
          <circle cx="145" cy="115" r="4" fill="#EF4444"/>
        </g>
        <text x="125" y="204" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#065F46" text-anchor="middle">Optimal Generalization</text>
        <text x="125" y="218" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" text-anchor="middle">Balanced • CV Acc: 93.8%</text>
      </g>

      <!-- Panel 3: max_depth = 8 (Overfitting) -->
      <g transform="translate(600, 20)" filter="url(#bound-shadow)">
        <rect width="250" height="230" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
        <rect width="250" height="32" rx="10" fill="#FEF2F2"/>
        <rect y="20" width="250" height="12" fill="#FEF2F2"/>
        <text x="125" y="21" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#991B1B" text-anchor="middle">max_depth = 8 (Severe Overfitting)</text>

        <!-- 2D Space -->
        <g transform="translate(35, 45)">
          <rect width="180" height="140" fill="#FFFFFF" stroke="#0F172A" stroke-width="1.5"/>
          <!-- Chaotic fine boxes isolating single points -->
          <rect x="0" y="0" width="180" height="140" fill="#D1FAE5" fill-opacity="0.3"/>
          <rect x="0" y="60" width="65" height="80" fill="#FEE2E2" fill-opacity="0.5"/>
          <rect x="25" y="80" width="20" height="25" fill="#D1FAE5" fill-opacity="0.8"/>
          <rect x="135" y="105" width="25" height="25" fill="#FEE2E2" fill-opacity="0.8"/>
          <rect x="90" y="25" width="20" height="20" fill="#FEE2E2" fill-opacity="0.8"/>
          <!-- Grid lines -->
          <line x1="65" y1="0" x2="65" y2="140" stroke="#EF4444" stroke-width="1"/>
          <line x1="0" y1="60" x2="180" y2="60" stroke="#EF4444" stroke-width="1"/>
          <line x1="135" y1="60" x2="135" y2="140" stroke="#EF4444" stroke-width="1"/>
          <line x1="135" y1="105" x2="160" y2="105" stroke="#EF4444" stroke-width="1"/>

          <circle cx="35" cy="92" r="4" fill="#10B981"/>
          <circle cx="147" cy="117" r="4" fill="#EF4444"/>
          <circle cx="100" cy="35" r="4" fill="#EF4444"/>
        </g>
        <text x="125" y="204" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#DC2626" text-anchor="middle">Overfitting: Memorizes Noise</text>
        <text x="125" y="218" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" text-anchor="middle">Train: 100% | High Test Variance</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.11: Decision Tree Orthogonal Decision Boundaries.</strong> Decision trees carve feature space exclusively using axis-aligned orthogonal cuts. Depth 1 underfits, Depth 3 captures the underlying distribution, and Depth 8 creates isolated boxes around training noise.
  </div>
</div>"""

# 12. TRAINING VS VALIDATION ERROR CURVE ACROSS DEPTHS
SVG_TRAIN_VAL_ERROR_CURVE = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Model Complexity: Training vs. Validation Accuracy Across Tree Depth</span>
    <span class="svg-badge">Figure 12.12</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 270" width="100%" xmlns="http://www.w3.org/2000/svg">
      <!-- Plot Area -->
      <g transform="translate(60, 30)">
        <line x1="60" y1="180" x2="520" y2="180" stroke="#0F172A" stroke-width="1.5"/>
        <line x1="60" y1="20" x2="60" y2="180" stroke="#0F172A" stroke-width="1.5"/>

        <!-- Y Axis -->
        <text x="50" y="184" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="end">90%</text>
        <text x="50" y="100" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="end">95%</text>
        <text x="50" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">100%</text>
        <text x="-100" y="15" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle" transform="rotate(-90)">Accuracy →</text>

        <!-- X Axis Depths: 1, 2, 3, 4, 5, 6, 8, 10 -->
        <!-- x coordinates: d=1:100, d=2:150, d=3:200, d=4:250, d=5:300, d=6:350, d=8:430, d=10:500 -->
        <text x="100" y="200" font-family="monospace" font-size="11" fill="#475569" text-anchor="middle">1</text>
        <text x="150" y="200" font-family="monospace" font-size="11" fill="#475569" text-anchor="middle">2</text>
        <text x="200" y="200" font-family="monospace" font-size="11" fill="#475569" text-anchor="middle">3</text>
        <text x="250" y="200" font-family="monospace" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">4*</text>
        <text x="300" y="200" font-family="monospace" font-size="11" fill="#475569" text-anchor="middle">5</text>
        <text x="350" y="200" font-family="monospace" font-size="11" fill="#475569" text-anchor="middle">6</text>
        <text x="430" y="200" font-family="monospace" font-size="11" fill="#475569" text-anchor="middle">8</text>
        <text x="500" y="200" font-family="monospace" font-size="11" fill="#475569" text-anchor="middle">10</text>
        <text x="300" y="220" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Tree Depth (max_depth) →</text>

        <!-- Training Curve (Blue): 95.3% -> 97.9% -> 98.4% -> 98.9% -> 99.5% -> 100% -> 100% -> 100% -->
        <!-- Map: 90% = 180, 100% = 20. Diff = 160 px for 10% -> 16 px per 1% -->
        <!-- y = 180 - (acc - 0.90) * 1600 -->
        <!-- d=1 (95.3%): y=95.2; d=2 (97.9%): y=53.6; d=3 (98.4%): y=45.6; d=4 (99.0%): y=36; d=6 (100%): y=20 -->
        <path d="M 100 95 L 150 54 L 200 46 L 250 36 L 300 28 L 350 20 L 430 20 L 500 20" fill="none" stroke="#2563EB" stroke-width="3"/>

        <!-- Validation Curve (Green): 94.3% -> 93.8% -> 93.8% -> 94.8% -> 94.8% -> 94.8% -->
        <!-- d=1 (94.3%): y=111; d=2 (93.8%): y=119; d=3 (93.8%): y=119; d=4 (94.8%): y=103; d=5+: y=103 -->
        <path d="M 100 111 L 150 119 L 200 119 L 250 103 L 300 103 L 350 103 L 430 103 L 500 103" fill="none" stroke="#059669" stroke-width="3" stroke-dasharray="5 3"/>

        <!-- Optimal Marker -->
        <circle cx="250" cy="103" r="5" fill="#059669"/>
        <line x1="250" y1="20" x2="250" y2="180" stroke="#059669" stroke-dasharray="3"/>
        <text x="250" y="15" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#059669" text-anchor="middle">Optimal: Depth 4</text>
      </g>

      <!-- Legend & Insights Box (Right 280px) -->
      <g transform="translate(600, 30)">
        <rect width="250" height="200" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
        <text x="125" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Generalization Dynamics</text>

        <g transform="translate(20, 45)">
          <line x1="0" y1="0" x2="25" y2="0" stroke="#2563EB" stroke-width="3"/>
          <text x="35" y="4" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#2563EB">Training Accuracy</text>
          <text x="35" y="18" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B">Reaches 100% memorization</text>

          <line x1="0" y1="35" x2="25" y2="35" stroke="#059669" stroke-width="3" stroke-dasharray="5 3"/>
          <text x="35" y="39" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#059669">5-Fold CV Accuracy</text>
          <text x="35" y="53" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B">Plateaus &amp; risks overfit</text>
        </g>

        <rect x="15" y="120" width="220" height="65" rx="6" fill="#EFF6FF"/>
        <text x="25" y="138" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1E40AF">Pre-Pruning Solution:</text>
        <text x="25" y="154" font-family="system-ui, sans-serif" font-size="10" fill="#334155">Constrain max_depth ≤ 4 or</text>
        <text x="25" y="170" font-family="system-ui, sans-serif" font-size="10" fill="#334155">min_samples_leaf ≥ 5</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.12: Complexity Curve Across Depths.</strong> Training accuracy climbs steadily toward 100% as depth grows, while cross-validation accuracy peaks around depth 4. Unrestricted depth results in pure memorization with zero added generalization benefit.
  </div>
</div>"""

# 13. FEATURE IMPORTANCE BAR CHART
SVG_FEATURE_IMPORTANCE_BARS = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Fitted Feature Importances (Mean Decrease in Impurity / Gini Importance)</span>
    <span class="svg-badge">Figure 12.13</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 230" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="fi-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- Chart area -->
      <g transform="translate(60, 25)">
        <text x="0" y="20" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F172A">Relative Predictor Impact on Split Impurity Reductions</text>

        <!-- Feature 1: Study_Hours (86.8%) -->
        <g transform="translate(0, 45)">
          <text x="140" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="end">Study_Hours</text>
          <!-- Bar background -->
          <rect x="155" y="6" width="500" height="28" rx="6" fill="#F1F5F9"/>
          <!-- Active bar: 86.8% of 500 = 434 px -->
          <rect x="155" y="6" width="434" height="28" rx="6" fill="#4F46E5"/>
          <text x="600" y="25" font-family="monospace" font-size="12" font-weight="700" fill="#4338CA">0.8677 (86.8%)</text>
        </g>

        <!-- Feature 2: Attendance_Pct (13.2%) -->
        <g transform="translate(0, 95)">
          <text x="140" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="end">Attendance_Pct</text>
          <!-- Bar background -->
          <rect x="155" y="6" width="500" height="28" rx="6" fill="#F1F5F9"/>
          <!-- Active bar: 13.2% of 500 = 66 px -->
          <rect x="155" y="6" width="66" height="28" rx="6" fill="#0284C7"/>
          <text x="235" y="25" font-family="monospace" font-size="12" font-weight="700" fill="#0284C7">0.1323 (13.2%)</text>
        </g>

        <!-- Sum Callout -->
        <line x1="155" y1="145" x2="655" y2="145" stroke="#CBD5E1" stroke-dasharray="3"/>
        <text x="400" y="165" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Σ Importances = 0.8677 + 0.1323 = 1.0000 (100.0%)</text>
        <text x="400" y="183" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569" text-anchor="middle">Caution: MDI importance does not prove real-world causality and can favor continuous features.</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.13: Scikit-Learn Feature Importances.</strong> Study_Hours accounts for 86.8% of the total weighted Gini impurity reduction throughout the tree, while Attendance_Pct contributes the remaining 13.2%.
  </div>
</div>"""

# 14. CONFUSION MATRIX HEATMAP
SVG_CONFUSION_MATRIX_HEATMAP = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Holdout Test Set Confusion Matrix (N = 48 Students)</span>
    <span class="svg-badge">Figure 12.14</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 270" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="cm-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- Matrix Container (Left) -->
      <g transform="translate(60, 20)">
        <!-- Top Prediction Header -->
        <text x="230" y="20" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">PREDICTED OUTCOME</text>
        <text x="155" y="40" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">Predicted FAIL (0)</text>
        <text x="305" y="40" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">Predicted PASS (1)</text>

        <!-- Left Actual Header -->
        <text x="-120" y="15" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle" transform="rotate(-90)">ACTUAL CLASS</text>
        <text x="70" y="105" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="end">Actual FAIL (0)</text>
        <text x="70" y="175" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="end">Actual PASS (1)</text>

        <!-- Top-Left: TN = 20 -->
        <g transform="translate(85, 55)" filter="url(#cm-shadow)">
          <rect width="140" height="68" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="2"/>
          <text x="70" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#065F46" text-anchor="middle">TRUE NEGATIVE (TN)</text>
          <text x="70" y="52" font-family="system-ui, sans-serif" font-size="26" font-weight="900" fill="#065F46" text-anchor="middle">20</text>
        </g>

        <!-- Top-Right: FP = 4 -->
        <g transform="translate(235, 55)" filter="url(#cm-shadow)">
          <rect width="140" height="68" rx="8" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.5"/>
          <text x="70" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#991B1B" text-anchor="middle">FALSE POSITIVE (FP)</text>
          <text x="70" y="52" font-family="system-ui, sans-serif" font-size="26" font-weight="900" fill="#991B1B" text-anchor="middle">4</text>
        </g>

        <!-- Bottom-Left: FN = 1 -->
        <g transform="translate(85, 130)" filter="url(#cm-shadow)">
          <rect width="140" height="68" rx="8" fill="#FEF3C7" stroke="#FCD34D" stroke-width="1.5"/>
          <text x="70" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#92400E" text-anchor="middle">FALSE NEGATIVE (FN)</text>
          <text x="70" y="52" font-family="system-ui, sans-serif" font-size="26" font-weight="900" fill="#92400E" text-anchor="middle">1</text>
        </g>

        <!-- Bottom-Right: TP = 23 -->
        <g transform="translate(235, 130)" filter="url(#cm-shadow)">
          <rect width="140" height="68" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
          <text x="70" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#065F46" text-anchor="middle">TRUE POSITIVE (TP)</text>
          <text x="70" y="52" font-family="system-ui, sans-serif" font-size="26" font-weight="900" fill="#065F46" text-anchor="middle">23</text>
        </g>

        <text x="230" y="220" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">Total Holdout Test Samples = 20 + 4 + 1 + 23 = 48</text>
      </g>

      <!-- Right Summary KPI Cards -->
      <g transform="translate(520, 35)" filter="url(#cm-shadow)">
        <rect width="300" height="185" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
        <text x="150" y="25" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Holdout Performance Metrics</text>

        <g transform="translate(20, 45)">
          <text x="0" y="15" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Accuracy (43/48):</text>
          <text x="260" y="15" font-family="monospace" font-size="12" font-weight="700" fill="#0F172A" text-anchor="end">89.58%</text>

          <text x="0" y="42" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Precision (23/27):</text>
          <text x="260" y="42" font-family="monospace" font-size="12" font-weight="700" fill="#0284C7" text-anchor="end">85.19%</text>

          <text x="0" y="69" font-family="system-ui, sans-serif" font-size="11" fill="#475569">Recall (23/24):</text>
          <text x="260" y="69" font-family="monospace" font-size="12" font-weight="700" fill="#059669" text-anchor="end">95.83%</text>

          <text x="0" y="96" font-family="system-ui, sans-serif" font-size="11" fill="#475569">F1-Score:</text>
          <text x="260" y="96" font-family="monospace" font-size="12" font-weight="700" fill="#7C3AED" text-anchor="end">90.20%</text>
        </g>

        <rect x="20" y="148" width="260" height="24" rx="4" fill="#ECFDF5"/>
        <text x="150" y="164" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">✓ Excellent Recall: Only 1 Pass student missed!</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.14: Confusion Matrix on Unseen Test Students.</strong> 20 True Negatives, 23 True Positives, 4 False Positives, and only 1 False Negative, producing an 89.6% Accuracy and a 95.8% Recall.
  </div>
</div>"""

# 15. REGRESSION TREE PREDICTION CURVE
SVG_REGRESSION_TREE_CURVE = """<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">Decision Tree Regression: Piece-Wise Constant Prediction Steps</span>
    <span class="svg-badge">Figure 12.15</span>
  </div>
  <div class="svg-wrapper">
    <svg viewBox="0 0 880 270" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="reg-shadow" x="-5%" y="-5%" width="110%" height="115%">
          <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
        </filter>
      </defs>

      <!-- Curve Area (Left 540px) -->
      <g transform="translate(60, 30)">
        <line x1="60" y1="180" x2="500" y2="180" stroke="#0F172A" stroke-width="1.5"/>
        <line x1="60" y1="20" x2="60" y2="180" stroke="#0F172A" stroke-width="1.5"/>

        <!-- Y Axis -->
        <text x="50" y="184" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="end">$100k</text>
        <text x="50" y="100" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="end">$250k</text>
        <text x="50" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">$400k</text>
        <text x="-100" y="15" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle" transform="rotate(-90)">House Price ($k) →</text>

        <!-- X Axis -->
        <text x="60" y="200" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">800 sq ft</text>
        <text x="200" y="200" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">1,600</text>
        <text x="350" y="200" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">2,400</text>
        <text x="500" y="200" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">3,200 sq ft</text>
        <text x="280" y="220" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Living Area (Square Footage) →</text>

        <!-- Scatter Points (Noisy Linear trend) -->
        <circle cx="80" cy="165" r="3.5" fill="#94A3B8"/>
        <circle cx="105" cy="155" r="3.5" fill="#94A3B8"/>
        <circle cx="130" cy="140" r="3.5" fill="#94A3B8"/>
        <circle cx="170" cy="130" r="3.5" fill="#94A3B8"/>
        <circle cx="190" cy="145" r="3.5" fill="#94A3B8"/>
        <circle cx="220" cy="115" r="3.5" fill="#94A3B8"/>
        <circle cx="250" cy="100" r="3.5" fill="#94A3B8"/>
        <circle cx="280" cy="105" r="3.5" fill="#94A3B8"/>
        <circle cx="310" cy="90" r="3.5" fill="#94A3B8"/>
        <circle cx="340" cy="75" r="3.5" fill="#94A3B8"/>
        <circle cx="380" cy="65" r="3.5" fill="#94A3B8"/>
        <circle cx="420" cy="55" r="3.5" fill="#94A3B8"/>
        <circle cx="460" cy="40" r="3.5" fill="#94A3B8"/>
        <circle cx="490" cy="30" r="3.5" fill="#94A3B8"/>

        <!-- Step Function (max_depth=3 yields 4-8 steps) -->
        <path d="M 60 160 H 150 V 135 H 240 V 105 H 340 V 70 H 430 V 35 H 500" fill="none" stroke="#0284C7" stroke-width="3.5"/>

        <!-- Sample test home point at 2,000 sq ft (x=280) -> y=105 (Price=$265k) -->
        <circle cx="280" cy="105" r="6" fill="#EF4444"/>
        <line x1="280" y1="105" x2="280" y2="180" stroke="#EF4444" stroke-dasharray="3"/>
        <text x="280" y="92" font-family="monospace" font-size="10.5" font-weight="700" fill="#B91C1C" text-anchor="middle">2,000 sq ft → $265.5k</text>
      </g>

      <!-- Right Explanation Box -->
      <g transform="translate(590, 30)" filter="url(#reg-shadow)">
        <rect width="250" height="200" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
        <text x="125" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0284C7" text-anchor="middle">Regression Tree Dynamics</text>

        <rect x="15" y="40" width="220" height="60" rx="6" fill="#EFF6FF"/>
        <text x="25" y="58" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1D4ED8">Piece-Wise Constant:</text>
        <text x="25" y="74" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Predictions are flat steps</text>
        <text x="25" y="88" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Every home in a leaf gets same mean</text>

        <rect x="15" y="110" width="220" height="75" rx="6" fill="#FEF2F2"/>
        <text x="25" y="128" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#991B1B">Extrapolation Failure:</text>
        <text x="25" y="144" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• Cannot predict above max training</text>
        <text x="25" y="158" font-family="system-ui, sans-serif" font-size="10" fill="#334155">• A 10,000 sq ft mansion still gets</text>
        <text x="25" y="172" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B">the rightmost step value ($380k)!</text>
      </g>
    </svg>
  </div>
  <div class="svg-caption">
    <strong>Figure 12.15: Piece-Wise Constant Steps in Decision Tree Regression.</strong> Regression trees approximate continuous trends using discrete plateaus. A key limitation is inability to extrapolate beyond the maximum training feature range.
  </div>
</div>"""

ALL_SVGS = [
    ("SVG_DT_HERO", SVG_DT_HERO),
    ("SVG_DT_ANATOMY", SVG_DT_ANATOMY),
    ("SVG_DT_PREDICTION_PATH", SVG_DT_PREDICTION_PATH),
    ("SVG_CLASSIFICATION_VS_REGRESSION", SVG_CLASSIFICATION_VS_REGRESSION),
    ("SVG_CANDIDATE_SPLIT_BEFORE_AFTER", SVG_CANDIDATE_SPLIT_BEFORE_AFTER),
    ("SVG_GINI_IMPURITY_CURVE", SVG_GINI_IMPURITY_CURVE),
    ("SVG_ENTROPY_CURVE", SVG_ENTROPY_CURVE),
    ("SVG_ENTROPY_VS_GINI", SVG_ENTROPY_VS_GINI),
    ("SVG_INFORMATION_GAIN_WORKED", SVG_INFORMATION_GAIN_WORKED),
    ("SVG_ACTUAL_TRAINED_TREE", SVG_ACTUAL_TRAINED_TREE),
    ("SVG_DECISION_BOUNDARIES_DEPTH", SVG_DECISION_BOUNDARIES_DEPTH),
    ("SVG_TRAIN_VAL_ERROR_CURVE", SVG_TRAIN_VAL_ERROR_CURVE),
    ("SVG_FEATURE_IMPORTANCE_BARS", SVG_FEATURE_IMPORTANCE_BARS),
    ("SVG_CONFUSION_MATRIX_HEATMAP", SVG_CONFUSION_MATRIX_HEATMAP),
    ("SVG_REGRESSION_TREE_CURVE", SVG_REGRESSION_TREE_CURVE),
]

def validate_all_svgs():
    print("Validating all 15 Decision Tree SVGs via xml.etree.ElementTree...")
    for name, markup in ALL_SVGS:
        start_idx = markup.find("<svg")
        end_idx = markup.find("</svg>") + len("</svg>")
        svg_xml = markup[start_idx:end_idx]
        try:
            ET.fromstring(svg_xml)
            print(f"  [PASS] {name} is XML-valid!")
        except Exception as e:
            print(f"  [FAIL] {name}: {e}")
            raise e
    print("ALL 15 SVGS VALIDATED SUCCESSFULLY!")

if __name__ == "__main__":
    validate_all_svgs()
