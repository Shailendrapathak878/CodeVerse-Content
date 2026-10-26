"""
Module: topic11_svgs.py
Contains 14 hand-crafted, XML-valid vector diagrams for Topic 11: K-Nearest Neighbors (KNN).
All SVGs adhere strictly to Light Mode aesthetics, valid XML structure, and responsive viewBoxes.
"""

import xml.etree.ElementTree as ET

# ----------------------------------------------------------------------
# 1. SVG_KNN_HERO: The K-Nearest Neighbors Lazy Learning Paradigm
# ----------------------------------------------------------------------
SVG_KNN_HERO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%">
  <rect width="920" height="340" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="20" y="20" width="880" height="42" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="46" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">K-NEAREST NEIGHBORS: INSTANCE-BASED LAZY LEARNING ARCHITECTURE</text>

  <!-- Stage 1: Memorization / Storage -->
  <rect x="40" y="85" width="180" height="225" rx="12" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
  <rect x="55" y="100" width="150" height="28" rx="6" fill="#4F46E5"/>
  <text x="130" y="118" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">1. TRAINING PHASE</text>
  <text x="130" y="150" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#334155" text-anchor="middle">Zero Abstraction</text>
  <text x="130" y="176" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">&#8226; No weight fitting</text>
  <text x="130" y="200" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">&#8226; No cost optimization</text>
  <text x="130" y="224" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">&#8226; Stores all N vectors</text>
  <rect x="55" y="255" width="150" height="38" rx="6" fill="#E0E7FF"/>
  <text x="130" y="278" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">Lazy: O(1) Training</text>

  <!-- Arrow 1 -->
  <line x1="225" y1="190" x2="255" y2="190" stroke="#4F46E5" stroke-width="2.5" stroke-dasharray="3,3"/>
  <polygon points="265,190 253,184 253,196" fill="#4F46E5"/>

  <!-- Stage 2: Query & Distance -->
  <rect x="270" y="85" width="180" height="225" rx="12" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
  <rect x="285" y="100" width="150" height="28" rx="6" fill="#0284C7"/>
  <text x="360" y="118" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">2. QUERY ARRIVAL</text>
  <rect x="285" y="138" width="150" height="42" rx="6" fill="#E0F2FE" stroke="#7DD3FC" stroke-width="1"/>
  <text x="360" y="164" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#0369A1" text-anchor="middle">d(x, q) = ||x - q||</text>
  <text x="360" y="202" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#0C4A6E" text-anchor="middle">Compute Euclidean Dist</text>
  <text x="360" y="222" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#0369A1" text-anchor="middle">Compare to ALL N points</text>
  <rect x="285" y="255" width="150" height="38" rx="6" fill="#BAE6FD"/>
  <text x="360" y="278" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#0369A1" text-anchor="middle">Heavy: O(N × d) Query</text>

  <!-- Arrow 2 -->
  <line x1="455" y1="190" x2="485" y2="190" stroke="#0284C7" stroke-width="2.5" stroke-dasharray="3,3"/>
  <polygon points="495,190 483,184 483,196" fill="#0284C7"/>

  <!-- Stage 3: Top-K Neighborhood -->
  <rect x="500" y="85" width="180" height="225" rx="12" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
  <rect x="515" y="100" width="150" height="28" rx="6" fill="#16A34A"/>
  <text x="590" y="118" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">3. SELECT K NEAREST</text>
  <rect x="515" y="138" width="150" height="42" rx="6" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1"/>
  <text x="590" y="164" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#15803D" text-anchor="middle">N_K(q) = {x(1)..x(K)}</text>
  <text x="590" y="202" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#14532D" text-anchor="middle">Sort distances ascending</text>
  <text x="590" y="222" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#15803D" text-anchor="middle">Retain K closest points</text>
  <rect x="515" y="255" width="150" height="38" rx="6" fill="#BBF7D0"/>
  <text x="590" y="278" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#14532D" text-anchor="middle">Local Neighborhood</text>

  <!-- Arrow 3 -->
  <line x1="685" y1="190" x2="715" y2="190" stroke="#16A34A" stroke-width="2.5" stroke-dasharray="3,3"/>
  <polygon points="725,190 713,184 713,196" fill="#16A34A"/>

  <!-- Stage 4: Aggregation / Prediction -->
  <rect x="730" y="85" width="155" height="225" rx="12" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
  <rect x="742" y="100" width="130" height="28" rx="6" fill="#D97706"/>
  <text x="807" y="118" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">4. AGGREGATION</text>
  <rect x="742" y="138" width="130" height="42" rx="6" fill="#FEF3C7" stroke="#FCD34D" stroke-width="1"/>
  <text x="807" y="164" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#92400E" text-anchor="middle">Mode / Mean</text>
  <text x="807" y="202" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#92400E" text-anchor="middle">Class: Majority Vote</text>
  <text x="807" y="222" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#78350F" text-anchor="middle">Reg: Neighbor Average</text>
  <rect x="742" y="255" width="130" height="38" rx="6" fill="#FDE68A"/>
  <text x="807" y="278" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#78350F" text-anchor="middle">Final Prediction</text>
</svg>"""

# ----------------------------------------------------------------------
# 2. SVG_KNN_PREDICTION_FLOWCHART: 7-Step Workflow Flowchart
# ----------------------------------------------------------------------
SVG_KNN_PREDICTION_FLOWCHART = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 340" width="100%">
  <rect width="880" height="340" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="440" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">HOW KNN PREDICTS: THE 7-STEP EXECUTION PIPELINE</text>

  <!-- Flowchart Steps Horizontal Chain -->
  <g transform="translate(30, 65)">
    <!-- Step 1 -->
    <rect x="0" y="0" width="105" height="100" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
    <circle cx="52" cy="22" r="12" fill="#4F46E5"/>
    <text x="52" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">1</text>
    <text x="52" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#312E81" text-anchor="middle">Store Data</text>
    <text x="52" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Load labelled</text>
    <text x="52" y="85" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">training points</text>

    <!-- Arrow 1 -->
    <line x1="108" y1="50" x2="122" y2="50" stroke="#4F46E5" stroke-width="2"/>
    <polygon points="126,50 120,47 120,53" fill="#4F46E5"/>

    <!-- Step 2 -->
    <rect x="128" y="0" width="105" height="100" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
    <circle cx="180" cy="22" r="12" fill="#4F46E5"/>
    <text x="180" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">2</text>
    <text x="180" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#312E81" text-anchor="middle">Select K</text>
    <text x="180" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Choose neighbor</text>
    <text x="180" y="85" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">count (e.g. K=5)</text>

    <!-- Arrow 2 -->
    <line x1="236" y1="50" x2="250" y2="50" stroke="#4F46E5" stroke-width="2"/>
    <polygon points="254,50 248,47 248,53" fill="#4F46E5"/>

    <!-- Step 3 -->
    <rect x="256" y="0" width="105" height="100" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <circle cx="308" cy="22" r="12" fill="#0284C7"/>
    <text x="308" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">3</text>
    <text x="308" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0369A1" text-anchor="middle">New Query</text>
    <text x="308" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Receive unlabelled</text>
    <text x="308" y="85" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">test point q</text>

    <!-- Arrow 3 -->
    <line x1="364" y1="50" x2="378" y2="50" stroke="#0284C7" stroke-width="2"/>
    <polygon points="382,50 376,47 376,53" fill="#0284C7"/>

    <!-- Step 4 -->
    <rect x="384" y="0" width="105" height="100" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <circle cx="436" cy="22" r="12" fill="#0284C7"/>
    <text x="436" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">4</text>
    <text x="436" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0369A1" text-anchor="middle">Distances</text>
    <text x="436" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Compute dist to</text>
    <text x="436" y="85" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">all N points</text>

    <!-- Arrow 4 -->
    <line x1="492" y1="50" x2="506" y2="50" stroke="#0284C7" stroke-width="2"/>
    <polygon points="510,50 504,47 504,53" fill="#0284C7"/>

    <!-- Step 5 -->
    <rect x="512" y="0" width="105" height="100" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <circle cx="564" cy="22" r="12" fill="#16A34A"/>
    <text x="564" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">5</text>
    <text x="564" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#15803D" text-anchor="middle">Find Top-K</text>
    <text x="564" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Sort ascending,</text>
    <text x="564" y="85" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">pick K closest</text>

    <!-- Arrow 5 -->
    <line x1="620" y1="50" x2="634" y2="50" stroke="#16A34A" stroke-width="2"/>
    <polygon points="638,50 632,47 632,53" fill="#16A34A"/>

    <!-- Step 6 -->
    <rect x="640" y="0" width="105" height="100" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
    <circle cx="692" cy="22" r="12" fill="#D97706"/>
    <text x="692" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">6</text>
    <text x="692" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#92400E" text-anchor="middle">Gather Targets</text>
    <text x="692" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Extract labels /</text>
    <text x="692" y="85" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">target values</text>

    <!-- Arrow 6 -->
    <line x1="748" y1="50" x2="762" y2="50" stroke="#D97706" stroke-width="2"/>
    <polygon points="766,50 760,47 760,53" fill="#D97706"/>

    <!-- Step 7 -->
    <rect x="768" y="0" width="105" height="100" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="2"/>
    <circle cx="820" cy="22" r="12" fill="#15803D"/>
    <text x="820" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">7</text>
    <text x="820" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#15803D" text-anchor="middle">Predict</text>
    <text x="820" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#166534" text-anchor="middle">Vote (Class) or</text>
    <text x="820" y="85" font-family="-apple-system, sans-serif" font-size="9" fill="#166534" text-anchor="middle">Average (Reg)</text>
  </g>

  <!-- Explanatory Banner -->
  <g transform="translate(30, 185)">
    <rect width="820" height="120" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="20" y="28" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Why Is KNN a “Lazy Learner”? (Instance-Based Learning)</text>
    <text x="20" y="50" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">&#8226; <tspan font-weight="700">No Model Training Phase:</tspan> Unlike Linear or Logistic Regression, KNN fits zero weights (β). Training simply means saving the dataset into memory.</text>
    <text x="20" y="72" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">&#8226; <tspan font-weight="700">Heavy Prediction Workload:</tspan> All computational effort is deferred until query time, where computing distances to N points takes O(N × d) operations.</text>
    <text x="20" y="94" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">&#8226; <tspan font-weight="700">KNN vs. K-Means:</tspan> KNN is <tspan font-weight="700" fill="#4F46E5">Supervised</tspan> (predicts known labels); K-Means is <tspan font-weight="700" fill="#D97706">Unsupervised</tspan> (discovers unlabelled clusters).</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 3. SVG_KNN_QUERY_NEIGHBORS: Query Point Surrounded by Neighbors
# ----------------------------------------------------------------------
SVG_KNN_QUERY_NEIGHBORS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">FEATURE SPACE NEIGHBORHOOD: CLASSIFYING AN UNKNOWN FRUIT</text>

  <!-- Left: 2D Feature Space Plot -->
  <g transform="translate(60, 55)">
    <rect width="440" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    
    <!-- Axes Grid -->
    <line x1="50" y1="220" x2="410" y2="220" stroke="#0F172A" stroke-width="1.5"/>
    <line x1="50" y1="20" x2="50" y2="220" stroke="#0F172A" stroke-width="1.5"/>
    <text x="230" y="248" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle">Feature 1: Sweetness (1 to 10) &#8594;</text>
    <text x="20" y="120" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle" transform="rotate(-90 20 120)">Feature 2: Crispness &#8594;</text>

    <!-- Query Point Q at (5, 5) -> Pixel coords: x = 50 + 5*35 = 225, y = 220 - 5*18 = 130 -->
    <!-- Distance Circles around Q (x=225, y=130) -->
    <!-- Radius K=1 (d=1.0 -> r=35) -->
    <circle cx="225" cy="130" r="38" fill="none" stroke="#4F46E5" stroke-width="1.5" stroke-dasharray="3,3"/>
    <!-- Radius K=3 (d=2.0 -> r=72) -->
    <circle cx="225" cy="130" r="74" fill="none" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="4,4"/>
    <!-- Radius K=5 (d=2.83 -> r=102) -->
    <circle cx="225" cy="130" r="104" fill="none" stroke="#16A34A" stroke-width="1.5" stroke-dasharray="5,5"/>

    <!-- Training Points (Apples = Green Circles, Oranges = Orange Triangles) -->
    <!-- T1(4, 6): x=190, y=112 (Apple) -->
    <circle cx="190" cy="112" r="7" fill="#16A34A"/>
    <text x="180" y="105" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#15803D">T1</text>

    <!-- T2(6, 5): x=260, y=130 (Apple) -->
    <circle cx="260" cy="130" r="7" fill="#16A34A"/>
    <text x="272" y="125" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#15803D">T2</text>

    <!-- T3(5, 3): x=225, y=166 (Orange) -->
    <polygon points="225,158 219,172 231,172" fill="#EA580C"/>
    <text x="238" y="172" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#C2410C">T3</text>

    <!-- T4(7, 6): x=295, y=112 (Orange) -->
    <polygon points="295,104 289,118 301,118" fill="#EA580C"/>
    <text x="306" y="110" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#C2410C">T4</text>

    <!-- T5(3, 3): x=155, y=166 (Apple) -->
    <circle cx="155" cy="166" r="7" fill="#16A34A"/>
    <text x="142" y="166" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#15803D">T5</text>

    <!-- T6(8, 4): x=330, y=148 (Orange) -->
    <polygon points="330,140 324,154 336,154" fill="#EA580C"/>
    <text x="342" y="152" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#C2410C">T6</text>

    <!-- Query Point Q(5, 5) Star / Diamond -->
    <polygon points="225,120 234,130 225,140 216,130" fill="#4F46E5" stroke="#FFFFFF" stroke-width="1.5"/>
    <text x="225" y="114" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#312E81" text-anchor="middle">Query (Q)</text>
  </g>

  <!-- Right: Legend & Radius Card -->
  <g transform="translate(530, 55)">
    <rect width="280" height="260" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="140" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Neighborhood Radii</text>

    <rect x="15" y="40" width="250" height="42" rx="6" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <circle cx="30" cy="61" r="5" fill="#4F46E5"/>
    <text x="45" y="56" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4338CA">K = 1 Neighborhood:</text>
    <text x="45" y="72" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">1 Nearest: T2 (Apple) &#8594; <tspan font-weight="700" fill="#16A34A">Apple</tspan></text>

    <rect x="15" y="90" width="250" height="48" rx="6" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1"/>
    <circle cx="30" cy="114" r="5" fill="#0284C7"/>
    <text x="45" y="108" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0369A1">K = 3 Neighborhood:</text>
    <text x="45" y="124" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">3 Nearest: 2 Apples, 1 Orange</text>
    <text x="45" y="136" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#16A34A">Winner: Apple (2 vs 1)</text>

    <rect x="15" y="146" width="250" height="48" rx="6" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
    <circle cx="30" cy="170" r="5" fill="#16A34A"/>
    <text x="45" y="164" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#15803D">K = 5 Neighborhood:</text>
    <text x="45" y="180" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">5 Nearest: 3 Apples, 2 Oranges</text>
    <text x="45" y="192" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#16A34A">Winner: Apple (3 vs 2)</text>

    <text x="140" y="222" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#64748B" text-anchor="middle">&#9679; Apple (Class 0)  &#9650; Orange (Class 1)</text>
    <text x="140" y="242" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">Expanding K smooths local boundaries</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 4. SVG_KNN_K_COMPARISON: K = 1, 3, 5 Voting Comparison
# ----------------------------------------------------------------------
SVG_KNN_K_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 300" width="100%">
  <rect width="880" height="300" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="440" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">THE EFFECT OF K ON LOCAL DECISIONS: K = 1 VS K = 3 VS K = 5</text>

  <!-- Panel 1: K = 1 -->
  <g transform="translate(40, 55)">
    <rect width="250" height="225" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="20" y="15" width="210" height="28" rx="6" fill="#4F46E5"/>
    <text x="125" y="34" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">K = 1 (NEAREST NEIGHBOR)</text>

    <rect x="20" y="55" width="210" height="60" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <text x="125" y="78" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">Single closest point:</text>
    <text x="125" y="100" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#16A34A" text-anchor="middle">T2: Apple (d = 1.000)</text>

    <text x="125" y="135" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Vote Tally: Apple 1, Orange 0</text>
    <rect x="35" y="148" width="180" height="30" rx="6" fill="#DCFCE7"/>
    <text x="125" y="168" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#15803D" text-anchor="middle">PREDICTION: APPLE</text>

    <text x="125" y="198" font-family="-apple-system, sans-serif" font-size="10" fill="#DC2626" text-anchor="middle">High Variance • Sensitive to noise</text>
  </g>

  <!-- Panel 2: K = 3 -->
  <g transform="translate(315, 55)">
    <rect width="250" height="225" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="20" y="15" width="210" height="28" rx="6" fill="#0284C7"/>
    <text x="125" y="34" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">K = 3 (MODERATE NEIGHBORHOOD)</text>

    <rect x="20" y="55" width="210" height="60" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <text x="125" y="76" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">T2: Apple (d=1.0) • T1: Apple (d=1.4)</text>
    <text x="125" y="98" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">T3: Orange (d=2.0)</text>

    <text x="125" y="135" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Vote Tally: Apple 2, Orange 1</text>
    <rect x="35" y="148" width="180" height="30" rx="6" fill="#DCFCE7"/>
    <text x="125" y="168" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#15803D" text-anchor="middle">PREDICTION: APPLE</text>

    <text x="125" y="198" font-family="-apple-system, sans-serif" font-size="10" fill="#16A34A" text-anchor="middle">Optimal Balance • Robust to outlier</text>
  </g>

  <!-- Panel 3: K = 5 -->
  <g transform="translate(590, 55)">
    <rect width="250" height="225" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="20" y="15" width="210" height="28" rx="6" fill="#16A34A"/>
    <text x="125" y="34" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">K = 5 (BROADER CONSENSUS)</text>

    <rect x="20" y="55" width="210" height="60" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <text x="125" y="76" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">Apples: T2, T1, T5 (3 points)</text>
    <text x="125" y="98" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">Oranges: T3, T4 (2 points)</text>

    <text x="125" y="135" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Vote Tally: Apple 3, Orange 2</text>
    <rect x="35" y="148" width="180" height="30" rx="6" fill="#DCFCE7"/>
    <text x="125" y="168" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#15803D" text-anchor="middle">PREDICTION: APPLE</text>

    <text x="125" y="198" font-family="-apple-system, sans-serif" font-size="10" fill="#D97706" text-anchor="middle">Smoother • Risk of oversmoothing</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 5. SVG_EUCLIDEAN_VS_MANHATTAN: Distance Measures Comparison
# ----------------------------------------------------------------------
SVG_EUCLIDEAN_VS_MANHATTAN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">DISTANCE METRICS: EUCLIDEAN (STRAIGHT-LINE) VS. MANHATTAN (GRID-BASED)</text>

  <!-- Left: Grid Plot Visual -->
  <g transform="translate(60, 55)">
    <rect width="360" height="270" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    
    <!-- Coordinate Grid (x: 2 to 6, y: 3 to 6) -->
    <!-- Grid lines -->
    <path d="M 60,60 L 300,60 M 60,110 L 300,110 M 60,160 L 300,160 M 60,210 L 300,210" stroke="#E2E8F0" stroke-width="1"/>
    <path d="M 60,60 L 60,210 M 120,60 L 120,210 M 180,60 L 180,210 M 240,60 L 240,210 M 300,60 L 300,210" stroke="#E2E8F0" stroke-width="1"/>

    <!-- Point A at (x=2, y=3) -> pixel (60, 210) -->
    <!-- Point B at (x=6, y=6) -> pixel (300, 60) -->

    <!-- Manhattan Path (Axis-aligned right then up) -->
    <path d="M 60,210 L 300,210 L 300,60" fill="none" stroke="#D97706" stroke-width="3.5" stroke-dasharray="6,4"/>
    <text x="180" y="230" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#B45309" text-anchor="middle">Δx = |6 - 2| = 4</text>
    <text x="315" y="140" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#B45309">Δy = |6 - 3| = 3</text>

    <!-- Euclidean Straight Line -->
    <line x1="60" y1="210" x2="300" y2="60" stroke="#4F46E5" stroke-width="4"/>
    <text x="160" y="125" font-family="Courier New, monospace" font-size="12" font-weight="800" fill="#312E81" transform="rotate(-32 160 125)">d = √(4² + 3²) = 5.0</text>

    <!-- Point A Marker -->
    <circle cx="60" cy="210" r="7" fill="#4F46E5"/>
    <text x="50" y="235" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">A (2, 3)</text>

    <!-- Point B Marker -->
    <circle cx="300" cy="60" r="7" fill="#16A34A"/>
    <text x="300" y="45" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">B (6, 6)</text>
  </g>

  <!-- Right: Comparison Details Card -->
  <g transform="translate(460, 55)">
    <rect width="350" height="270" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="175" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Mathematical Comparison</text>

    <!-- Euclidean Box -->
    <rect x="20" y="40" width="310" height="85" rx="6" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="30" y="60" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4338CA">1. EUCLIDEAN (L2 NORM):</text>
    <text x="30" y="80" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#312E81">d = √((x1-y1)² + (x2-y2)²) = 5.0</text>
    <text x="30" y="105" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">&#8226; Direct “as the crow flies” shortest path</text>
    <text x="30" y="118" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">&#8226; Default metric in scikit-learn (p=2)</text>

    <!-- Manhattan Box -->
    <rect x="20" y="135" width="310" height="85" rx="6" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1"/>
    <text x="30" y="155" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#B45309">2. MANHATTAN (L1 NORM):</text>
    <text x="30" y="175" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#78350F">d = |x1 - y1| + |x2 - y2| = 4 + 3 = 7.0</text>
    <text x="30" y="200" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">&#8226; “City block” path restricted to grid lines</text>
    <text x="30" y="213" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">&#8226; Less sensitive to extreme coordinate outliers</text>

    <text x="175" y="248" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Minkowski generalization: d = (Σ |x-y|^p)^(1/p)</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 6. SVG_MANUAL_DISTANCE_RANKING: Manual KNN Distance Ranking
# ----------------------------------------------------------------------
SVG_MANUAL_DISTANCE_RANKING = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 320" width="100%">
  <rect width="880" height="320" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="440" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">MANUAL KNN WORKED EXAMPLE: RANKING 6 POINTS FROM QUERY Q(5, 5)</text>

  <!-- Horizontal Ranking Bars Grid -->
  <g transform="translate(40, 55)">
    <!-- Header Row -->
    <rect x="0" y="0" width="800" height="30" rx="4" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="35" y="20" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Rank</text>
    <text x="90" y="20" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">ID</text>
    <text x="160" y="20" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Coords (x1, x2)</text>
    <text x="270" y="20" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Class Label</text>
    <text x="390" y="20" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Euclidean Dist</text>
    <text x="520" y="20" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Distance Bar Visual</text>
    <text x="730" y="20" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Selection</text>

    <!-- Rank 1: T2 (dist = 1.000) -->
    <rect x="0" y="35" width="800" height="32" rx="4" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
    <text x="35" y="56" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#15803D">#1</text>
    <text x="90" y="56" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#0F172A">T2</text>
    <text x="160" y="56" font-family="Courier New, monospace" font-size="11" fill="#334155">(6.0, 5.0)</text>
    <text x="270" y="56" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#16A34A">Apple (0)</text>
    <text x="390" y="56" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#15803D">1.0000</text>
    <rect x="490" y="44" width="60" height="14" rx="3" fill="#16A34A"/>
    <rect x="680" y="41" width="100" height="20" rx="4" fill="#4F46E5"/>
    <text x="730" y="55" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">In K=1, 3, 5</text>

    <!-- Rank 2: T1 (dist = 1.414) -->
    <rect x="0" y="72" width="800" height="32" rx="4" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
    <text x="35" y="93" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#15803D">#2</text>
    <text x="90" y="93" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#0F172A">T1</text>
    <text x="160" y="93" font-family="Courier New, monospace" font-size="11" fill="#334155">(4.0, 6.0)</text>
    <text x="270" y="93" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#16A34A">Apple (0)</text>
    <text x="390" y="93" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#15803D">1.4142</text>
    <rect x="490" y="81" width="85" height="14" rx="3" fill="#16A34A"/>
    <rect x="680" y="78" width="100" height="20" rx="4" fill="#0284C7"/>
    <text x="730" y="92" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">In K=3, 5</text>

    <!-- Rank 3: T3 (dist = 2.000) -->
    <rect x="0" y="109" width="800" height="32" rx="4" fill="#FFF7ED" stroke="#FDBA74" stroke-width="1"/>
    <text x="35" y="130" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#C2410C">#3</text>
    <text x="90" y="130" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#0F172A">T3</text>
    <text x="160" y="130" font-family="Courier New, monospace" font-size="11" fill="#334155">(5.0, 3.0)</text>
    <text x="270" y="130" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#EA580C">Orange (1)</text>
    <text x="390" y="130" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#C2410C">2.0000</text>
    <rect x="490" y="118" width="120" height="14" rx="3" fill="#EA580C"/>
    <rect x="680" y="115" width="100" height="20" rx="4" fill="#0284C7"/>
    <text x="730" y="129" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">In K=3, 5</text>

    <!-- Rank 4: T4 (dist = 2.236) -->
    <rect x="0" y="146" width="800" height="32" rx="4" fill="#FFF7ED" stroke="#FDBA74" stroke-width="1"/>
    <text x="35" y="167" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#C2410C">#4</text>
    <text x="90" y="167" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#0F172A">T4</text>
    <text x="160" y="167" font-family="Courier New, monospace" font-size="11" fill="#334155">(7.0, 6.0)</text>
    <text x="270" y="167" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#EA580C">Orange (1)</text>
    <text x="390" y="167" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#C2410C">2.2361</text>
    <rect x="490" y="155" width="134" height="14" rx="3" fill="#EA580C"/>
    <rect x="680" y="152" width="100" height="20" rx="4" fill="#16A34A"/>
    <text x="730" y="166" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">In K=5</text>

    <!-- Rank 5: T5 (dist = 2.828) -->
    <rect x="0" y="183" width="800" height="32" rx="4" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
    <text x="35" y="204" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#15803D">#5</text>
    <text x="90" y="204" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#0F172A">T5</text>
    <text x="160" y="204" font-family="Courier New, monospace" font-size="11" fill="#334155">(3.0, 3.0)</text>
    <text x="270" y="204" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#16A34A">Apple (0)</text>
    <text x="390" y="204" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#15803D">2.8284</text>
    <rect x="490" y="192" width="170" height="14" rx="3" fill="#16A34A"/>
    <rect x="680" y="189" width="100" height="20" rx="4" fill="#16A34A"/>
    <text x="730" y="203" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">In K=5</text>

    <!-- Rank 6: T6 (dist = 3.162) -->
    <rect x="0" y="220" width="800" height="32" rx="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <text x="35" y="241" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#64748B">#6</text>
    <text x="90" y="241" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#64748B">T6</text>
    <text x="160" y="241" font-family="Courier New, monospace" font-size="11" fill="#64748B">(8.0, 4.0)</text>
    <text x="270" y="241" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#94A3B8">Orange (1)</text>
    <text x="390" y="241" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#64748B">3.1623</text>
    <rect x="490" y="229" width="190" height="14" rx="3" fill="#94A3B8"/>
    <rect x="680" y="226" width="100" height="20" rx="4" fill="#E2E8F0"/>
    <text x="730" y="240" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#64748B" text-anchor="middle">Excluded</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 7. SVG_WEIGHTED_VS_UNWEIGHTED: Majority vs Distance-Weighted Voting
# ----------------------------------------------------------------------
SVG_WEIGHTED_VS_UNWEIGHTED = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">DIVERGENT OUTCOMES: UNWEIGHTED MAJORITY VS. DISTANCE-WEIGHTED VOTING</text>

  <!-- Left: Unweighted Majority Voting (Apple Wins 2 vs 1) -->
  <g transform="translate(40, 55)">
    <rect width="365" height="280" rx="10" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
    <text x="182" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#92400E" text-anchor="middle">Unweighted Majority Voting (K=3)</text>
    
    <rect x="20" y="45" width="325" height="42" rx="6" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1"/>
    <text x="35" y="70" font-family="-apple-system, sans-serif" font-size="11" fill="#78350F">Rule: Every neighbor gets exactly <tspan font-weight="700">1 equal vote</tspan></text>

    <!-- Vote counts -->
    <rect x="35" y="105" width="135" height="90" rx="6" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="102" y="130" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">Class 0 (Apple)</text>
    <text x="102" y="168" font-family="Courier New, monospace" font-size="28" font-weight="800" fill="#15803D" text-anchor="middle">2</text>
    <text x="102" y="185" font-family="-apple-system, sans-serif" font-size="9" fill="#166534" text-anchor="middle">Neighbors #2, #3</text>

    <rect x="195" y="105" width="135" height="90" rx="6" fill="#FFF7ED" stroke="#FDBA74" stroke-width="1.5"/>
    <text x="262" y="130" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#C2410C" text-anchor="middle">Class 1 (Orange)</text>
    <text x="262" y="168" font-family="Courier New, monospace" font-size="28" font-weight="800" fill="#EA580C" text-anchor="middle">1</text>
    <text x="262" y="185" font-family="-apple-system, sans-serif" font-size="9" fill="#C2410C" text-anchor="middle">Neighbor #1</text>

    <rect x="25" y="215" width="315" height="40" rx="6" fill="#16A34A"/>
    <text x="182" y="240" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">WINNER: CLASS 0 (APPLE)</text>
    <text x="182" y="270" font-family="-apple-system, sans-serif" font-size="10" fill="#78350F" text-anchor="middle">Apple wins purely by quantity (2 votes vs 1)</text>
  </g>

  <!-- Right: Distance-Weighted Voting (Orange Flips the Win) -->
  <g transform="translate(450, 55)">
    <rect width="370" height="280" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <text x="185" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#16A34A" text-anchor="middle">Distance-Weighted Voting (w = 1 / d)</text>

    <rect x="20" y="45" width="330" height="42" rx="6" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1"/>
    <text x="35" y="70" font-family="-apple-system, sans-serif" font-size="11" fill="#166534">Rule: Nearer points hold <tspan font-weight="700">heavier influence</tspan></text>

    <!-- Weighted tallies -->
    <rect x="35" y="105" width="140" height="90" rx="6" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="105" y="130" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">Class 0 (Apple)</text>
    <text x="105" y="160" font-family="Courier New, monospace" font-size="18" font-weight="800" fill="#15803D" text-anchor="middle">0.6667</text>
    <text x="105" y="180" font-family="-apple-system, sans-serif" font-size="9" fill="#166534" text-anchor="middle">1/3.0 + 1/3.0</text>

    <rect x="195" y="105" width="140" height="90" rx="6" fill="#FFF7ED" stroke="#EA580C" stroke-width="2"/>
    <text x="265" y="130" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#C2410C" text-anchor="middle">Class 1 (Orange)</text>
    <text x="265" y="160" font-family="Courier New, monospace" font-size="18" font-weight="800" fill="#EA580C" text-anchor="middle">1.0000</text>
    <text x="265" y="180" font-family="-apple-system, sans-serif" font-size="9" fill="#C2410C" text-anchor="middle">1 / 1.0 (Very Close!)</text>

    <rect x="25" y="215" width="320" height="40" rx="6" fill="#EA580C"/>
    <text x="185" y="240" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">WINNER: CLASS 1 (ORANGE)</text>
    <text x="185" y="270" font-family="-apple-system, sans-serif" font-size="10" fill="#14532D" text-anchor="middle">Orange wins because it is 3× closer than either Apple!</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 8. SVG_FEATURE_SCALING_EFFECT: Feature Scaling Before and After
# ----------------------------------------------------------------------
SVG_FEATURE_SCALING_EFFECT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">THE FEATURE SCALING CATASTROPHE: WHY SCALING IS MANDATORY FOR KNN</text>

  <!-- Left: Unscaled (Income dwarfs Age) -->
  <g transform="translate(40, 55)">
    <rect width="365" height="280" rx="10" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="182" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#DC2626" text-anchor="middle">Before Scaling (Raw Units: Age vs Income)</text>

    <!-- Stretched Coordinate Box -->
    <rect x="45" y="45" width="280" height="170" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="45" y1="200" x2="320" y2="200" stroke="#0F172A" stroke-width="1.5"/>
    <line x1="45" y1="45" x2="45" y2="200" stroke="#0F172A" stroke-width="1.5"/>
    
    <text x="182" y="218" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Age: 20 to 60 yrs (Span Δ=40)</text>
    <text x="25" y="120" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle" transform="rotate(-90 25 120)">Income: $20k-$150k (Δ=130,000!)</text>

    <!-- Point A(30, 50k), B(50, 50.1k), C(31, 60k) -->
    <circle cx="80" cy="150" r="5" fill="#4F46E5"/>
    <text x="90" y="145" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4338CA">A (Age 30, $50k)</text>

    <circle cx="240" cy="148" r="5" fill="#16A34A"/>
    <text x="245" y="145" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#15803D">B (Age 50, $50.1k)</text>

    <circle cx="85" cy="65" r="5" fill="#DC2626"/>
    <text x="95" y="65" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#B91C1C">C (Age 31, $60k)</text>

    <!-- False nearest line -->
    <line x1="80" y1="150" x2="240" y2="148" stroke="#16A34A" stroke-width="2"/>
    <text x="160" y="165" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#15803D" text-anchor="middle">Dist = 101.98 (WRONG NEIGHBOR!)</text>

    <text x="182" y="245" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">Income variations completely overpower 20 years of Age!</text>
  </g>

  <!-- Right: After Scaling (StandardScaler / MinMax) -->
  <g transform="translate(450, 55)">
    <rect width="370" height="280" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <text x="185" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#16A34A" text-anchor="middle">After Standard Scaling (Normalized [0, 1])</text>

    <!-- Isotropic Coordinate Box -->
    <rect x="45" y="45" width="280" height="170" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="45" y1="200" x2="320" y2="200" stroke="#0F172A" stroke-width="1.5"/>
    <line x1="45" y1="45" x2="45" y2="200" stroke="#0F172A" stroke-width="1.5"/>

    <text x="182" y="218" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Scaled Age ∈ [-1.5, +1.5]</text>
    <text x="25" y="120" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle" transform="rotate(-90 25 120)">Scaled Income ∈ [-1.5, +1.5]</text>

    <!-- Scaled points where C is genuinely closer to A than B -->
    <circle cx="100" cy="150" r="5" fill="#4F46E5"/>
    <text x="110" y="145" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4338CA">A (Scaled)</text>

    <circle cx="270" cy="152" r="5" fill="#DC2626"/>
    <text x="270" y="170" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#B91C1C" text-anchor="middle">B (Far in Age!)</text>

    <circle cx="115" cy="80" r="5" fill="#16A34A"/>
    <text x="125" y="80" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#15803D">C (TRUE NEIGHBOR)</text>

    <!-- Correct nearest line -->
    <line x1="100" y1="150" x2="115" y2="80" stroke="#16A34A" stroke-width="2.5"/>
    <text x="140" y="115" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#15803D">Dist = 2.13 (CLOSEST)</text>

    <text x="185" y="245" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">Both features now contribute equally to geometric distances.</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 9. SVG_DECISION_BOUNDARIES_K: Fitted Boundaries for K = 1, 5, 15
# ----------------------------------------------------------------------
SVG_DECISION_BOUNDARIES_K = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 320" width="100%">
  <rect width="880" height="320" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="440" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">KNN DECISION BOUNDARIES ACROSS K: OVERFITTING VS. SMOOTHING</text>

  <!-- Panel 1: K = 1 (Jagged Overfitting) -->
  <g transform="translate(40, 55)">
    <rect width="250" height="245" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="20" y="12" width="210" height="26" rx="4" fill="#DC2626"/>
    <text x="125" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">K = 1 (OVERFITTING / HIGH VARIANCE)</text>

    <!-- Canvas -->
    <rect x="20" y="48" width="210" height="150" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Jagged boundary with islands -->
    <path d="M 20,130 C 50,110 70,160 110,120 C 140,80 180,150 230,110" fill="none" stroke="#DC2626" stroke-width="2.5"/>
    <!-- Noise island -->
    <circle cx="80" cy="80" r="18" fill="#FEE2E2" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="2,2"/>
    <circle cx="80" cy="80" r="4" fill="#DC2626"/>

    <!-- Data points -->
    <circle cx="50" cy="160" r="4" fill="#16A34A"/>
    <circle cx="90" cy="170" r="4" fill="#16A34A"/>
    <circle cx="150" cy="180" r="4" fill="#16A34A"/>
    <circle cx="190" cy="160" r="4" fill="#16A34A"/>
    <circle cx="150" cy="70" r="4" fill="#DC2626"/>
    <circle cx="180" cy="80" r="4" fill="#DC2626"/>

    <text x="125" y="216" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">Training Acc: 100% | Val Acc: Low</text>
    <text x="125" y="232" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Islands memorise individual noise points</text>
  </g>

  <!-- Panel 2: K = 5 (Optimal Sweet Spot) -->
  <g transform="translate(315, 55)">
    <rect width="250" height="245" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="2"/>
    <rect x="20" y="12" width="210" height="26" rx="4" fill="#16A34A"/>
    <text x="125" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">K = 5 (OPTIMAL SWEET SPOT)</text>

    <!-- Canvas -->
    <rect x="20" y="48" width="210" height="150" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>

    <!-- Smooth S-curve boundary -->
    <path d="M 20,150 C 70,140 120,120 170,95 L 230,85" fill="none" stroke="#16A34A" stroke-width="3"/>

    <!-- Data points -->
    <circle cx="80" cy="80" r="4" fill="#DC2626"/>
    <circle cx="50" cy="160" r="4" fill="#16A34A"/>
    <circle cx="90" cy="170" r="4" fill="#16A34A"/>
    <circle cx="150" cy="180" r="4" fill="#16A34A"/>
    <circle cx="190" cy="160" r="4" fill="#16A34A"/>
    <circle cx="150" cy="70" r="4" fill="#DC2626"/>
    <circle cx="180" cy="80" r="4" fill="#DC2626"/>

    <text x="125" y="216" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#15803D" text-anchor="middle">Test Accuracy: 97.5%</text>
    <text x="125" y="232" font-family="-apple-system, sans-serif" font-size="9" fill="#14532D" text-anchor="middle">Smooth boundary ignores isolated outliers</text>
  </g>

  <!-- Panel 3: K = 15 (Oversmoothed / Underfitting) -->
  <g transform="translate(590, 55)">
    <rect width="250" height="245" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="20" y="12" width="210" height="26" rx="4" fill="#D97706"/>
    <text x="125" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">K = 15 (UNDERFITTING / HIGH BIAS)</text>

    <!-- Canvas -->
    <rect x="20" y="48" width="210" height="150" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>

    <!-- Oversmoothed rigid boundary -->
    <line x1="20" y1="160" x2="230" y2="80" stroke="#D97706" stroke-width="2.5"/>

    <!-- Data points -->
    <circle cx="80" cy="80" r="4" fill="#DC2626"/>
    <circle cx="50" cy="160" r="4" fill="#16A34A"/>
    <circle cx="90" cy="170" r="4" fill="#16A34A"/>
    <circle cx="150" cy="180" r="4" fill="#16A34A"/>
    <circle cx="190" cy="160" r="4" fill="#16A34A"/>
    <circle cx="150" cy="70" r="4" fill="#DC2626"/>
    <circle cx="180" cy="80" r="4" fill="#DC2626"/>

    <text x="125" y="216" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#92400E" text-anchor="middle">Oversmoothed Global Boundary</text>
    <text x="125" y="232" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Loses genuine fine-grained cluster detail</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 10. SVG_TRAIN_VAL_ERROR_CURVE: Training vs Validation Accuracy Across K
# ----------------------------------------------------------------------
SVG_TRAIN_VAL_ERROR_CURVE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">MODEL SELECTION: 5-FOLD CV ACCURACY VS. TRAINING ACCURACY ACROSS K</text>

  <g transform="translate(80, 55)">
    <!-- Canvas Box -->
    <rect width="520" height="250" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Axes -->
    <line x1="50" y1="210" x2="500" y2="210" stroke="#0F172A" stroke-width="1.5"/>
    <line x1="50" y1="20" x2="50" y2="210" stroke="#0F172A" stroke-width="1.5"/>

    <!-- X Ticks: K = 1, 3, 5, 7, 9, 11, 15, 21 -->
    <text x="70" y="228" font-family="Courier New, monospace" font-size="10" fill="#64748B">K=1</text>
    <text x="130" y="228" font-family="Courier New, monospace" font-size="10" fill="#64748B">K=3</text>
    <text x="190" y="228" font-family="Courier New, monospace" font-size="10" fill="#64748B">K=5</text>
    <text x="250" y="228" font-family="Courier New, monospace" font-size="10" fill="#64748B">K=7</text>
    <text x="310" y="228" font-family="Courier New, monospace" font-size="10" fill="#64748B">K=9</text>
    <text x="370" y="228" font-family="Courier New, monospace" font-size="10" fill="#64748B">K=11</text>
    <text x="430" y="228" font-family="Courier New, monospace" font-size="10" fill="#64748B">K=15</text>
    <text x="480" y="228" font-family="Courier New, monospace" font-size="10" fill="#64748B">K=21</text>
    <text x="275" y="248" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle">Number of Neighbors (K) &#8594;</text>

    <!-- Y Ticks: Accuracy 88% to 100% -->
    <text x="42" y="214" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="end">88%</text>
    <text x="42" y="150" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="end">92%</text>
    <text x="42" y="85" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="end">96%</text>
    <text x="42" y="30" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="end">100%</text>

    <!-- Training Curve (Red): Starts at 100% at K=1 and slopes down -->
    <path d="M 70,30 L 130,55 L 190,75 L 250,85 L 310,95 L 370,110 L 430,130 L 480,145" fill="none" stroke="#DC2626" stroke-width="2.5"/>
    <circle cx="70" cy="30" r="4" fill="#DC2626"/>
    <circle cx="130" cy="55" r="4" fill="#DC2626"/>
    <circle cx="190" cy="75" r="4" fill="#DC2626"/>

    <!-- Cross-Validation Curve (Purple/Green): Starts lower at K=1 (92.5%), peaks at K=3-5 (95.0%), drops -->
    <path d="M 70,145 L 130,95 L 190,105 L 250,95 L 310,95 L 370,135 L 430,145 L 480,130" fill="none" stroke="#4F46E5" stroke-width="3"/>
    <circle cx="70" cy="145" r="4" fill="#4F46E5"/>
    <circle cx="130" cy="95" r="5" fill="#16A34A"/>
    <circle cx="190" cy="105" r="4" fill="#4F46E5"/>
    <circle cx="250" cy="95" r="4" fill="#4F46E5"/>
    <circle cx="310" cy="95" r="4" fill="#4F46E5"/>

    <!-- Optimal Peak Callout at K=3 -->
    <line x1="130" y1="20" x2="130" y2="95" stroke="#16A34A" stroke-width="1.5" stroke-dasharray="2,2"/>
    <rect x="95" y="8" width="115" height="22" rx="4" fill="#DCFCE7" stroke="#16A34A" stroke-width="1"/>
    <text x="152" y="23" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#15803D" text-anchor="middle">Peak CV Acc = 95.0%</text>
  </g>

  <!-- Right: Legend & Takeaways -->
  <g transform="translate(630, 55)">
    <rect width="190" height="250" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="95" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Curve Diagnostics</text>

    <rect x="15" y="45" width="160" height="36" rx="4" fill="#FEE2E2" stroke="#DC2626" stroke-width="1"/>
    <text x="25" y="60" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#991B1B">&#9644; Training Curve</text>
    <text x="25" y="73" font-family="-apple-system, sans-serif" font-size="9" fill="#7F1D1D">Always 100% at K=1</text>

    <rect x="15" y="90" width="160" height="36" rx="4" fill="#EEF2FF" stroke="#4F46E5" stroke-width="1"/>
    <text x="25" y="105" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4338CA">&#9644; 5-Fold CV Curve</text>
    <text x="25" y="118" font-family="-apple-system, sans-serif" font-size="9" fill="#312E81">True generalization metric</text>

    <rect x="15" y="140" width="160" height="85" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="25" y="158" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#0F172A">Key Principles:</text>
    <text x="25" y="175" font-family="-apple-system, sans-serif" font-size="9" fill="#475569">&#8226; Never pick K using training error</text>
    <text x="25" y="195" font-family="-apple-system, sans-serif" font-size="9" fill="#475569">&#8226; Never pick K using final test set</text>
    <text x="25" y="215" font-family="-apple-system, sans-serif" font-size="9" fill="#475569">&#8226; Best K = Cross-Validation Peak</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 11. SVG_DATASET_CLASS_DISTRIBUTION: Lab Class Distribution Chart
# ----------------------------------------------------------------------
SVG_DATASET_CLASS_DISTRIBUTION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 300" width="100%">
  <rect width="860" height="300" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">DATASET COMPOSITION &amp; STRATIFIED TRAIN/TEST SPLIT (N = 200)</text>

  <!-- Left: Balanced Class Distribution Bar Chart -->
  <g transform="translate(60, 60)">
    <rect width="350" height="205" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="175" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Total Dataset Balance (N = 200)</text>

    <!-- Bar Class 0 (Apple) -->
    <rect x="70" y="55" width="85" height="100" rx="4" fill="#16A34A"/>
    <text x="112" y="110" font-family="Courier New, monospace" font-size="20" font-weight="800" fill="#FFFFFF" text-anchor="middle">100</text>
    <text x="112" y="175" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#15803D" text-anchor="middle">Class 0</text>
    <text x="112" y="190" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Apple (50%)</text>

    <!-- Bar Class 1 (Orange) -->
    <rect x="195" y="55" width="85" height="100" rx="4" fill="#EA580C"/>
    <text x="237" y="110" font-family="Courier New, monospace" font-size="20" font-weight="800" fill="#FFFFFF" text-anchor="middle">100</text>
    <text x="237" y="175" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#C2410C" text-anchor="middle">Class 1</text>
    <text x="237" y="190" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Orange (50%)</text>
  </g>

  <!-- Right: 80/20 Stratified Partitioning Cards -->
  <g transform="translate(450, 60)">
    <rect width="350" height="205" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="175" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Stratified Split Protocol (Zero Leakage)</text>

    <!-- Training Split (80%) -->
    <rect x="25" y="45" width="300" height="60" rx="6" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="40" y="68" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#4338CA">Training Set: 160 Samples (80%)</text>
    <text x="40" y="90" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">&#8226; 80 Class 0 (50%) • 80 Class 1 (50%) • Scaler Fitted Here</text>

    <!-- Test Split (20%) -->
    <rect x="25" y="115" width="300" height="60" rx="6" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1"/>
    <text x="40" y="138" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#15803D">Holdout Test Set: 40 Samples (20%)</text>
    <text x="40" y="160" font-family="-apple-system, sans-serif" font-size="11" fill="#166534">&#8226; 20 Class 0 (50%) • 20 Class 1 (50%) • Evaluated Once</text>

    <text x="175" y="195" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#64748B" text-anchor="middle">Zero Shared IDs • Preserves exact class ratio</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 12. SVG_CONFUSION_MATRIX_HEATMAP: Practical Lab Test Confusion Matrix
# ----------------------------------------------------------------------
SVG_CONFUSION_MATRIX_HEATMAP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 380" width="100%">
  <rect width="860" height="380" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">HOLDOUT TEST CONFUSION MATRIX (N = 40 SAMPLES, K = 5 PIPELINE)</text>

  <!-- Left 2x2 Matrix Grid -->
  <g transform="translate(60, 65)">
    <!-- Column Headers -->
    <rect x="140" y="0" width="160" height="35" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="220" y="22" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">PREDICTED APPLE (0)</text>

    <rect x="310" y="0" width="160" height="35" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="390" y="22" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">PREDICTED ORANGE (1)</text>

    <!-- Row Headers -->
    <rect x="0" y="45" width="130" height="100" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="65" y="90" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">ACTUAL APPLE (0)</text>
    <text x="65" y="110" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">(20 Fruits)</text>

    <rect x="0" y="155" width="130" height="100" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="65" y="200" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">ACTUAL ORANGE (1)</text>
    <text x="65" y="220" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">(20 Fruits)</text>

    <!-- Cell Top-Left: True Negative (TN) for Apple -->
    <rect x="140" y="45" width="160" height="100" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="2"/>
    <text x="220" y="75" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#166534" text-anchor="middle">TRUE NEGATIVE (TN)</text>
    <text x="220" y="115" font-family="Courier New, monospace" font-size="32" font-weight="800" fill="#16A34A" text-anchor="middle">20</text>
    <text x="220" y="135" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#14532D" text-anchor="middle">Apples correctly classified</text>

    <!-- Cell Top-Right: False Positive (FP) -->
    <rect x="310" y="45" width="160" height="100" rx="8" fill="#FEF3C7" stroke="#FDE68A" stroke-width="2"/>
    <text x="390" y="75" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#92400E" text-anchor="middle">FALSE POSITIVE (FP)</text>
    <text x="390" y="115" font-family="Courier New, monospace" font-size="32" font-weight="800" fill="#D97706" text-anchor="middle">0</text>
    <text x="390" y="135" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#78350F" text-anchor="middle">Zero false alarms!</text>

    <!-- Cell Bottom-Left: False Negative (FN) -->
    <rect x="140" y="155" width="160" height="100" rx="8" fill="#FEE2E2" stroke="#DC2626" stroke-width="2"/>
    <text x="220" y="185" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#991B1B" text-anchor="middle">FALSE NEGATIVE (FN)</text>
    <text x="220" y="225" font-family="Courier New, monospace" font-size="32" font-weight="800" fill="#B91C1C" text-anchor="middle">1</text>
    <text x="220" y="245" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">Only 1 orange called apple</text>

    <!-- Cell Bottom-Right: True Positive (TP) -->
    <rect x="310" y="155" width="160" height="100" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="2"/>
    <text x="390" y="185" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#166534" text-anchor="middle">TRUE POSITIVE (TP)</text>
    <text x="390" y="225" font-family="Courier New, monospace" font-size="32" font-weight="800" fill="#15803D" text-anchor="middle">19</text>
    <text x="390" y="245" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#14532D" text-anchor="middle">Oranges correctly classified</text>
  </g>

  <!-- Right: Metrics Scoreboard -->
  <g transform="translate(560, 65)">
    <rect width="250" height="255" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="125" y="25" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Calculated Lab Metrics</text>

    <!-- Accuracy -->
    <rect x="15" y="42" width="220" height="42" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <text x="25" y="62" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#334155">Accuracy: (20+19)/40</text>
    <text x="225" y="68" font-family="Courier New, monospace" font-size="15" font-weight="700" fill="#4F46E5" text-anchor="end">97.50%</text>

    <!-- Precision -->
    <rect x="15" y="92" width="220" height="42" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <text x="25" y="112" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#334155">Precision: 19/(19+0)</text>
    <text x="225" y="118" font-family="Courier New, monospace" font-size="15" font-weight="700" fill="#0284C7" text-anchor="end">100.00%</text>

    <!-- Recall -->
    <rect x="15" y="142" width="220" height="42" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <text x="25" y="162" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#334155">Recall: 19/(19+1)</text>
    <text x="225" y="168" font-family="Courier New, monospace" font-size="15" font-weight="700" fill="#16A34A" text-anchor="end">95.00%</text>

    <!-- F1 Score -->
    <rect x="15" y="192" width="220" height="48" rx="6" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="25" y="214" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#4338CA">F1-Score (Harmonic Mean):</text>
    <text x="225" y="226" font-family="Courier New, monospace" font-size="16" font-weight="800" fill="#4F46E5" text-anchor="end">97.44%</text>
  </g>

  <text x="430" y="360" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Evaluated on N=40 holdout test samples. Only 1 point misclassified (97.5% Accuracy).</text>
</svg>"""

# ----------------------------------------------------------------------
# 13. SVG_KNN_REGRESSION_CURVE: KNN Regressor Piecewise Averaging Curve
# ----------------------------------------------------------------------
SVG_KNN_REGRESSION_CURVE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">KNN REGRESSION: LOCAL PIECEWISE TARGET AVERAGING</text>

  <g transform="translate(80, 55)">
    <!-- Canvas Box -->
    <rect width="480" height="250" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Axes -->
    <line x1="40" y1="210" x2="450" y2="210" stroke="#0F172A" stroke-width="1.5"/>
    <line x1="40" y1="20" x2="40" y2="210" stroke="#0F172A" stroke-width="1.5"/>

    <text x="245" y="235" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle">Living Area (100s sq ft) &#8594;</text>
    <text x="20" y="115" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle" transform="rotate(-90 20 115)">House Price ($k USD) &#8594;</text>

    <!-- Training Scatter Points -->
    <circle cx="60" cy="180" r="3.5" fill="#94A3B8"/>
    <circle cx="90" cy="170" r="3.5" fill="#94A3B8"/>
    <circle cx="120" cy="155" r="3.5" fill="#94A3B8"/>
    <circle cx="150" cy="140" r="3.5" fill="#94A3B8"/>
    <circle cx="180" cy="135" r="3.5" fill="#94A3B8"/>
    <circle cx="210" cy="120" r="3.5" fill="#94A3B8"/>
    <circle cx="240" cy="115" r="3.5" fill="#94A3B8"/>
    <circle cx="270" cy="95" r="3.5" fill="#94A3B8"/>
    <circle cx="300" cy="85" r="3.5" fill="#94A3B8"/>
    <circle cx="330" cy="70" r="3.5" fill="#94A3B8"/>
    <circle cx="360" cy="65" r="3.5" fill="#94A3B8"/>
    <circle cx="390" cy="50" r="3.5" fill="#94A3B8"/>
    <circle cx="420" cy="40" r="3.5" fill="#94A3B8"/>

    <!-- Step-like Piecewise KNN Regression Line (K = 5) -->
    <path d="M 40,185 L 80,185 L 80,165 L 140,165 L 140,140 L 200,140 L 200,122 L 260,122 L 260,95 L 320,95 L 320,72 L 380,72 L 380,48 L 450,48" fill="none" stroke="#4F46E5" stroke-width="3"/>

    <!-- Point Query Highlight -->
    <line x1="230" y1="210" x2="230" y2="122" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="3,3"/>
    <circle cx="230" cy="122" r="5" fill="#DC2626"/>
    <rect x="235" y="105" width="110" height="24" rx="4" fill="#FEE2E2" stroke="#DC2626" stroke-width="1"/>
    <text x="290" y="121" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#991B1B" text-anchor="middle">Average of 5 Neighbors</text>
  </g>

  <!-- Right: Interpretation Card -->
  <g transform="translate(590, 55)">
    <rect width="230" height="250" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="115" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">How KNN Regression Works</text>

    <rect x="15" y="45" width="200" height="60" rx="6" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="25" y="66" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#4338CA">&#375; = (1 / K) Σ y_i</text>
    <text x="25" y="88" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">Averages target values of K nearest neighbors.</text>

    <rect x="15" y="115" width="200" height="60" rx="6" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
    <text x="25" y="136" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#15803D">Verified Lab Metrics:</text>
    <text x="25" y="156" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#166534">MAE: $11.85k | RMSE: $15.07k</text>

    <text x="115" y="198" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">&#8226; Piecewise-constant output</text>
    <text x="115" y="215" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">&#8226; Cannot extrapolate beyond range</text>
    <text x="115" y="232" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">&#8226; Weighted: w = 1 / d</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 14. SVG_CURSE_OF_DIMENSIONALITY: Curse of Dimensionality Illustration
# ----------------------------------------------------------------------
SVG_CURSE_OF_DIMENSIONALITY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 300" width="100%">
  <rect width="860" height="300" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">THE CURSE OF DIMENSIONALITY: EXPONENTIAL DILUTION OF SPACE</text>

  <!-- 1D Panel (Dense line) -->
  <g transform="translate(40, 60)">
    <rect width="240" height="205" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="120" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">1D Space (1 Feature)</text>
    <text x="120" y="45" font-family="-apple-system, sans-serif" font-size="10" fill="#16A34A" text-anchor="middle">High Density • Close Neighbors</text>

    <!-- Line with 10 dots -->
    <line x1="20" y1="100" x2="220" y2="100" stroke="#0F172A" stroke-width="2"/>
    <circle cx="30" cy="100" r="5" fill="#4F46E5"/>
    <circle cx="55" cy="100" r="5" fill="#4F46E5"/>
    <circle cx="80" cy="100" r="5" fill="#4F46E5"/>
    <circle cx="105" cy="100" r="5" fill="#4F46E5"/>
    <circle cx="130" cy="100" r="5" fill="#4F46E5"/>
    <circle cx="155" cy="100" r="5" fill="#4F46E5"/>
    <circle cx="180" cy="100" r="5" fill="#4F46E5"/>
    <circle cx="205" cy="100" r="5" fill="#4F46E5"/>

    <text x="120" y="145" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">10 points cover 10 sub-intervals</text>
    <text x="120" y="165" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#15803D" text-anchor="middle">Points required: 10^1 = 10</text>
  </g>

  <!-- 2D Panel (Area dilutes points) -->
  <g transform="translate(310, 60)">
    <rect width="240" height="205" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="120" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">2D Space (2 Features)</text>
    <text x="120" y="45" font-family="-apple-system, sans-serif" font-size="10" fill="#D97706" text-anchor="middle">Moderate Density • Area Spreads</text>

    <rect x="40" y="65" width="160" height="80" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <circle cx="60" cy="85" r="4" fill="#4F46E5"/>
    <circle cx="120" cy="90" r="4" fill="#4F46E5"/>
    <circle cx="180" cy="75" r="4" fill="#4F46E5"/>
    <circle cx="80" cy="125" r="4" fill="#4F46E5"/>
    <circle cx="150" cy="130" r="4" fill="#4F46E5"/>

    <text x="120" y="165" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">Requires 10×10 grid cells</text>
    <text x="120" y="185" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#B45309" text-anchor="middle">Points required: 10^2 = 100</text>
  </g>

  <!-- 3D / High-D Panel (Vast empty void) -->
  <g transform="translate(580, 60)">
    <rect width="240" height="205" rx="8" fill="#FEE2E2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="120" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626" text-anchor="middle">High-D Space (p = 50+)</text>
    <text x="120" y="45" font-family="-apple-system, sans-serif" font-size="10" fill="#991B1B" text-anchor="middle">Extreme Emptiness • Loss of Contrast</text>

    <rect x="40" y="65" width="160" height="80" fill="#FFFFFF" stroke="#FECACA" stroke-width="1"/>
    <circle cx="50" cy="75" r="4" fill="#DC2626"/>
    <circle cx="190" cy="135" r="4" fill="#DC2626"/>

    <text x="120" y="165" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">Points are all equidistant &amp; far</text>
    <text x="120" y="185" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">Points required: 10^p → ∞</text>
  </g>
</svg>"""

ALL_SVGS = [
    ("SVG_KNN_HERO", SVG_KNN_HERO),
    ("SVG_KNN_PREDICTION_FLOWCHART", SVG_KNN_PREDICTION_FLOWCHART),
    ("SVG_KNN_QUERY_NEIGHBORS", SVG_KNN_QUERY_NEIGHBORS),
    ("SVG_KNN_K_COMPARISON", SVG_KNN_K_COMPARISON),
    ("SVG_EUCLIDEAN_VS_MANHATTAN", SVG_EUCLIDEAN_VS_MANHATTAN),
    ("SVG_MANUAL_DISTANCE_RANKING", SVG_MANUAL_DISTANCE_RANKING),
    ("SVG_WEIGHTED_VS_UNWEIGHTED", SVG_WEIGHTED_VS_UNWEIGHTED),
    ("SVG_FEATURE_SCALING_EFFECT", SVG_FEATURE_SCALING_EFFECT),
    ("SVG_DECISION_BOUNDARIES_K", SVG_DECISION_BOUNDARIES_K),
    ("SVG_TRAIN_VAL_ERROR_CURVE", SVG_TRAIN_VAL_ERROR_CURVE),
    ("SVG_DATASET_CLASS_DISTRIBUTION", SVG_DATASET_CLASS_DISTRIBUTION),
    ("SVG_CONFUSION_MATRIX_HEATMAP", SVG_CONFUSION_MATRIX_HEATMAP),
    ("SVG_KNN_REGRESSION_CURVE", SVG_KNN_REGRESSION_CURVE),
    ("SVG_CURSE_OF_DIMENSIONALITY", SVG_CURSE_OF_DIMENSIONALITY)
]

if __name__ == '__main__':
    print(f"Validating {len(ALL_SVGS)} Topic 11 SVGs for XML compliance...")
    for name, svg_str in ALL_SVGS:
        try:
            ET.fromstring(svg_str)
            print(f"  [XML PASS] {name}")
        except Exception as e:
            print(f"  [XML FAIL] {name}: {e}")
            raise
    print("All Topic 11 SVGs validated successfully!")
