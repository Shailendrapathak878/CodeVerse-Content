"""
Module: topic9_svgs.py
Contains 14 hand-crafted, XML-valid vector diagrams for Topic 9: Linear Regression.
All SVGs adhere strictly to Light Mode aesthetics, valid XML structure, and responsive viewBoxes.
"""

import xml.etree.ElementTree as ET

# ----------------------------------------------------------------------
# 1. SVG_REGRESSION_HERO: The Core Architecture of Linear Regression
# ----------------------------------------------------------------------
SVG_REGRESSION_HERO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%">
  <rect width="920" height="320" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="20" y="20" width="880" height="42" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="460" y="46" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">SUPERVISED MACHINE LEARNING: CONTINUOUS NUMERICAL PREDICTION</text>

  <!-- Left: Raw Input Feature X -->
  <rect x="50" y="90" width="220" height="180" rx="12" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="2"/>
  <rect x="70" y="105" width="180" height="30" rx="6" fill="#4F46E5"/>
  <text x="160" y="125" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">1. INPUT FEATURE (X)</text>
  <text x="160" y="160" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#334155" text-anchor="middle">Independent Variable</text>
  <text x="160" y="185" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">• House Living Area (sq ft)</text>
  <text x="160" y="205" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">• Student Study Hours</text>
  <text x="160" y="225" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">• Engine Displacement</text>
  <rect x="75" y="240" width="170" height="20" rx="4" fill="#E0E7FF"/>
  <text x="160" y="254" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">Known Input Signal</text>

  <!-- Arrow 1 -->
  <line x1="280" y1="180" x2="335" y2="180" stroke="#4F46E5" stroke-width="3" stroke-dasharray="4,4"/>
  <polygon points="345,180 333,174 333,186" fill="#4F46E5"/>
  <text x="312" y="170" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4F46E5" text-anchor="middle">Maps To</text>

  <!-- Center: Linear Model Hypothesis -->
  <rect x="350" y="80" width="230" height="200" rx="12" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="2"/>
  <rect x="370" y="95" width="190" height="30" rx="6" fill="#16A34A"/>
  <text x="465" y="115" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">2. LINEAR MODEL (f)</text>
  <rect x="370" y="140" width="190" height="42" rx="6" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1"/>
  <text x="465" y="166" font-family="Courier New, monospace" font-size="16" font-weight="700" fill="#166534" text-anchor="middle">&#375; = &#946;&#8320; + &#946;&#8321;x</text>
  <text x="465" y="202" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#166534" text-anchor="middle">&#946;&#8321;: Learned Slope (Weight)</text>
  <text x="465" y="222" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#166534" text-anchor="middle">&#946;&#8320;: Baseline Intercept (Bias)</text>
  <rect x="375" y="240" width="180" height="24" rx="4" fill="#BBF7D0"/>
  <text x="465" y="256" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#14532D" text-anchor="middle">Ordinary Least Squares Fit</text>

  <!-- Arrow 2 -->
  <line x1="590" y1="180" x2="645" y2="180" stroke="#16A34A" stroke-width="3" stroke-dasharray="4,4"/>
  <polygon points="655,180 643,174 643,186" fill="#16A34A"/>
  <text x="622" y="170" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#16A34A" text-anchor="middle">Predicts</text>

  <!-- Right: Continuous Target -->
  <rect x="660" y="90" width="210" height="180" rx="12" fill="#FEF3C7" stroke="#FDE68A" stroke-width="2"/>
  <rect x="680" y="105" width="170" height="30" rx="6" fill="#D97706"/>
  <text x="765" y="125" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">3. TARGET (&#375;)</text>
  <text x="765" y="160" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#92400E" text-anchor="middle">Continuous Quantity</text>
  <text x="765" y="185" font-family="-apple-system, sans-serif" font-size="12" fill="#B45309" text-anchor="middle">• House Price: $350,000</text>
  <text x="765" y="205" font-family="-apple-system, sans-serif" font-size="12" fill="#B45309" text-anchor="middle">• Exam Score: 87.5%</text>
  <text x="765" y="225" font-family="-apple-system, sans-serif" font-size="12" fill="#B45309" text-anchor="middle">• Fuel Econ: 28.4 MPG</text>
  <rect x="685" y="240" width="160" height="20" rx="4" fill="#FDE68A"/>
  <text x="765" y="254" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#78350F" text-anchor="middle">Not a Discrete Class</text>
</svg>"""

# ----------------------------------------------------------------------
# 2. SVG_SCATTER_OBSERVATIONS: 2D Scatter Plot of Observations
# ----------------------------------------------------------------------
SVG_SCATTER_OBSERVATIONS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="100%">
  <rect width="760" height="380" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="380" y="32" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">SCATTER PLOT: INSPECTING RAW BIVARIATE RELATIONSHIPS</text>

  <!-- Grid lines -->
  <line x1="80" y1="70" x2="700" y2="70" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="80" y1="130" x2="700" y2="130" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="80" y1="190" x2="700" y2="190" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="80" y1="250" x2="700" y2="250" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="80" y1="310" x2="700" y2="310" stroke="#E2E8F0" stroke-width="2"/> <!-- X Axis -->
  <line x1="80" y1="50" x2="80" y2="310" stroke="#E2E8F0" stroke-width="2"/> <!-- Y Axis -->

  <!-- Axis labels -->
  <text x="80" y="332" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">0</text>
  <text x="204" y="332" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">1,000</text>
  <text x="328" y="332" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">1,500</text>
  <text x="452" y="332" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">2,000</text>
  <text x="576" y="332" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">2,500</text>
  <text x="700" y="332" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">3,000</text>

  <text x="390" y="360" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#334155" text-anchor="middle">Input Feature (X): Living Area (sq ft)</text>

  <text x="70" y="314" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="end">$0k</text>
  <text x="70" y="254" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="end">$150k</text>
  <text x="70" y="194" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="end">$300k</text>
  <text x="70" y="134" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="end">$450k</text>
  <text x="70" y="74" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="end">$600k</text>

  <text transform="rotate(-90 25 180)" x="25" y="180" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#334155" text-anchor="middle">Target (y): Sale Price ($k)</text>

  <!-- Data points (scatter) -->
  <circle cx="160" cy="275" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="210" cy="245" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="240" cy="260" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="290" cy="210" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="340" cy="225" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="370" cy="180" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="430" cy="165" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="460" cy="190" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="510" cy="140" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="560" cy="120" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="610" cy="135" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>
  <circle cx="660" cy="90" r="6" fill="#4F46E5" fill-opacity="0.85" stroke="#312E81" stroke-width="1.5"/>

  <!-- Annotation Card -->
  <rect x="420" y="55" width="270" height="60" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="435" y="77" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">&#8226; Positive Linear Association</text>
  <text x="435" y="98" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Points scatter naturally due to unobserved</text>
  <text x="435" y="110" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">factors (location, condition, age).</text>
</svg>"""

# ----------------------------------------------------------------------
# 3. SVG_LINE_OF_BEST_FIT: Fitted Regression Line with Slope & Intercept
# ----------------------------------------------------------------------
SVG_LINE_OF_BEST_FIT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="100%">
  <rect width="760" height="380" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="380" y="32" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">THE LINE OF BEST FIT: MATHEMATICAL ANATOMY</text>

  <!-- Grid lines -->
  <line x1="80" y1="310" x2="700" y2="310" stroke="#CBD5E1" stroke-width="2"/> <!-- X Axis -->
  <line x1="80" y1="50" x2="80" y2="310" stroke="#CBD5E1" stroke-width="2"/> <!-- Y Axis -->

  <!-- Fitted Regression Line: y = mx + b -->
  <line x1="80" y1="285" x2="680" y2="85" stroke="#16A34A" stroke-width="3"/>

  <!-- Intercept marker -->
  <circle cx="80" cy="285" r="6" fill="#DC2626" stroke="#FFFFFF" stroke-width="2"/>
  <rect x="95" y="270" width="140" height="26" rx="4" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
  <text x="165" y="287" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">Intercept (b): Value at x=0</text>

  <!-- Slope triangle -->
  <line x1="380" y1="185" x2="500" y2="185" stroke="#2563EB" stroke-width="2" stroke-dasharray="3,3"/>
  <line x1="500" y1="185" x2="500" y2="145" stroke="#DC2626" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="440" y="202" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#2563EB" text-anchor="middle">Run: &#916;x</text>
  <text x="545" y="168" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">Rise: &#916;y</text>

  <!-- Formula Callout -->
  <rect x="360" y="60" width="230" height="40" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
  <text x="475" y="85" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#166534" text-anchor="middle">Slope (m) = Rise / Run = &#916;y / &#916;x</text>

  <!-- Scatter points -->
  <circle cx="160" cy="275" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="210" cy="245" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="240" cy="260" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="290" cy="210" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="340" cy="225" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="370" cy="180" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="430" cy="165" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="460" cy="190" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="510" cy="140" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="560" cy="120" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="610" cy="135" r="5" fill="#4F46E5" fill-opacity="0.8"/>
  <circle cx="660" cy="90" r="5" fill="#4F46E5" fill-opacity="0.8"/>

  <!-- Legend -->
  <rect x="80" y="335" width="600" height="30" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <circle cx="120" cy="350" r="5" fill="#4F46E5"/>
  <text x="135" y="354" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">Observed Data</text>
  <line x1="260" y1="350" x2="290" y2="350" stroke="#16A34A" stroke-width="3"/>
  <text x="300" y="354" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">Fitted Model: &#375; = mx + b</text>
  <circle cx="460" cy="350" r="5" fill="#DC2626"/>
  <text x="475" y="354" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">Y-Intercept (x = 0)</text>
</svg>"""

# ----------------------------------------------------------------------
# 4. SVG_COMPARING_CANDIDATE_LINES: Why Least Squares Picks Line C
# ----------------------------------------------------------------------
SVG_COMPARING_CANDIDATE_LINES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="100%">
  <rect width="760" height="380" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="380" y="32" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">CANDIDATE LINES: WHY ORDINARY LEAST SQUARES PICKS LINE C</text>

  <!-- Axes -->
  <line x1="80" y1="310" x2="700" y2="310" stroke="#CBD5E1" stroke-width="2"/>
  <line x1="80" y1="60" x2="80" y2="310" stroke="#CBD5E1" stroke-width="2"/>

  <!-- Candidate Line A (Too Flat, High SSE) -->
  <line x1="80" y1="210" x2="680" y2="210" stroke="#DC2626" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="685" y="214" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">Line A (SSE = 340)</text>

  <!-- Candidate Line B (Too Steep, High SSE) -->
  <line x1="80" y1="310" x2="520" y2="60" stroke="#D97706" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="525" y="65" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#D97706">Line B (SSE = 280)</text>

  <!-- Candidate Line C (Optimal OLS Line, Minimum SSE) -->
  <line x1="80" y1="285" x2="680" y2="85" stroke="#16A34A" stroke-width="3.5"/>
  <text x="685" y="90" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#16A34A">&#10003; Line C (Optimal: SSE = 42)</text>

  <!-- Data points -->
  <circle cx="150" cy="270" r="5" fill="#4F46E5"/>
  <circle cx="220" cy="235" r="5" fill="#4F46E5"/>
  <circle cx="280" cy="220" r="5" fill="#4F46E5"/>
  <circle cx="340" cy="190" r="5" fill="#4F46E5"/>
  <circle cx="410" cy="175" r="5" fill="#4F46E5"/>
  <circle cx="480" cy="140" r="5" fill="#4F46E5"/>
  <circle cx="550" cy="125" r="5" fill="#4F46E5"/>
  <circle cx="620" cy="100" r="5" fill="#4F46E5"/>

  <!-- Explanation Box -->
  <rect x="80" y="325" width="600" height="42" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="380" y="343" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Every candidate line produces vertical prediction errors. Ordinary Least Squares (OLS)</text>
  <text x="380" y="359" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">mathematically calculates the unique slope and intercept that minimizes the sum of squared errors (SSE).</text>
</svg>"""

# ----------------------------------------------------------------------
# 5. SVG_SLOPE_INTERCEPT_VARIATIONS: 4-Panel Comparison
# ----------------------------------------------------------------------
SVG_SLOPE_INTERCEPT_VARIATIONS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 360" width="100%">
  <rect width="900" height="360" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="450" y="30" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">HOW SLOPE (m) AND INTERCEPT (b) SHAPE LINE GEOMETRY</text>

  <!-- Panel 1: Positive Slope -->
  <rect x="30" y="55" width="195" height="240" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="127" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#16A34A" text-anchor="middle">Positive Slope (m &gt; 0)</text>
  <line x1="50" y1="260" x2="205" y2="260" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="50" y1="100" x2="50" y2="260" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="60" y1="240" x2="195" y2="120" stroke="#16A34A" stroke-width="3"/>
  <text x="127" y="280" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">As X increases, Y rises.</text>
  <text x="127" y="294" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">e.g. Study Time &#8594; Scores</text>

  <!-- Panel 2: Negative Slope -->
  <rect x="245" y="55" width="195" height="240" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="342" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#DC2626" text-anchor="middle">Negative Slope (m &lt; 0)</text>
  <line x1="265" y1="260" x2="420" y2="260" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="265" y1="100" x2="265" y2="260" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="275" y1="120" x2="410" y2="240" stroke="#DC2626" stroke-width="3"/>
  <text x="342" y="280" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">As X increases, Y falls.</text>
  <text x="342" y="294" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">e.g. Car Age &#8594; Value</text>

  <!-- Panel 3: Zero Slope -->
  <rect x="460" y="55" width="195" height="240" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="557" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#64748B" text-anchor="middle">Zero Slope (m = 0)</text>
  <line x1="480" y1="260" x2="635" y2="260" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="480" y1="100" x2="480" y2="260" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="490" y1="180" x2="625" y2="180" stroke="#64748B" stroke-width="3"/>
  <text x="557" y="280" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">X provides no linear info.</text>
  <text x="557" y="294" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">&#375; = b (Mean baseline)</text>

  <!-- Panel 4: Varying Intercept -->
  <rect x="675" y="55" width="195" height="240" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="772" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#7C3AED" text-anchor="middle">Intercept Shifts (b)</text>
  <line x1="695" y1="260" x2="850" y2="260" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="695" y1="100" x2="695" y2="260" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="705" y1="180" x2="840" y2="110" stroke="#7C3AED" stroke-width="2"/>
  <line x1="705" y1="230" x2="840" y2="160" stroke="#A855F7" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="772" y="280" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">Parallel vertical shifts.</text>
  <text x="772" y="294" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Same slope, different baseline</text>

  <rect x="30" y="310" width="840" height="35" rx="6" fill="#F1F5F9"/>
  <text x="450" y="332" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#334155" text-anchor="middle">Slope controls the steepness and direction of relationship; Intercept controls the vertical height at x=0.</text>
</svg>"""

# ----------------------------------------------------------------------
# 6. SVG_RESIDUAL_LINES: Visualizing Vertical Residuals e_i = y_i - y_hat
# ----------------------------------------------------------------------
SVG_RESIDUAL_LINES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="100%">
  <rect width="760" height="380" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="380" y="32" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">RESIDUALS: MEASURING VERTICAL ERRORS e&#7522; = y&#7522; - &#375;&#7522;</text>

  <!-- Axes -->
  <line x1="80" y1="310" x2="700" y2="310" stroke="#CBD5E1" stroke-width="2"/>
  <line x1="80" y1="50" x2="80" y2="310" stroke="#CBD5E1" stroke-width="2"/>

  <!-- Fitted Line -->
  <line x1="80" y1="280" x2="680" y2="80" stroke="#16A34A" stroke-width="3"/>

  <!-- Vertical Residual Lines & Points -->
  <!-- Point 1: Positive residual (above line) -->
  <line x1="180" y1="247" x2="180" y2="200" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="4,3"/>
  <circle cx="180" cy="200" r="6" fill="#4F46E5" stroke="#FFFFFF" stroke-width="1.5"/>
  <text x="195" y="225" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">e&#8321; &gt; 0 (Underestimated)</text>

  <!-- Point 2: Negative residual (below line) -->
  <line x1="300" y1="207" x2="300" y2="250" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="4,3"/>
  <circle cx="300" cy="250" r="6" fill="#4F46E5" stroke="#FFFFFF" stroke-width="1.5"/>
  <text x="315" y="235" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">e&#8322; &lt; 0 (Overestimated)</text>

  <!-- Point 3: Zero residual (on line) -->
  <circle cx="430" cy="163" r="6" fill="#16A34A" stroke="#FFFFFF" stroke-width="1.5"/>
  <text x="445" y="160" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#16A34A">e&#8323; &#8776; 0 (Perfect)</text>

  <!-- Point 4: Positive residual -->
  <line x1="560" y1="120" x2="560" y2="80" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="4,3"/>
  <circle cx="560" cy="80" r="6" fill="#4F46E5" stroke="#FFFFFF" stroke-width="1.5"/>
  <text x="575" y="105" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">e&#8324; &gt; 0</text>

  <!-- Callout Box -->
  <rect x="80" y="325" width="600" height="42" rx="6" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
  <text x="380" y="343" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#991B1B" text-anchor="middle">Why are residuals VERTICAL differences instead of perpendicular distances?</text>
  <text x="380" y="359" font-family="-apple-system, sans-serif" font-size="11" fill="#7F1D1D" text-anchor="middle">Because our goal is predicting the target Y from a given X. We only penalize errors in the output axis!</text>
</svg>"""

# ----------------------------------------------------------------------
# 7. SVG_LOSS_FUNCTION_COMPARISON: MSE (Quadratic) vs MAE (Linear)
# ----------------------------------------------------------------------
SVG_LOSS_FUNCTION_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" width="100%">
  <rect width="760" height="360" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="380" y="30" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">LOSS FUNCTIONS: MEAN SQUARED ERROR (MSE) VS MEAN ABSOLUTE ERROR (MAE)</text>

  <!-- Coordinate frame -->
  <line x1="80" y1="290" x2="680" y2="290" stroke="#CBD5E1" stroke-width="2"/> <!-- X: Error e -->
  <line x1="380" y1="50" x2="380" y2="290" stroke="#CBD5E1" stroke-width="2"/> <!-- Y: Penalty -->

  <text x="380" y="310" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Error e = (y - &#375;) = 0</text>
  <text x="180" y="310" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">-2.0</text>
  <text x="580" y="310" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">+2.0</text>
  <text x="695" y="294" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#334155">Error (e)</text>

  <!-- MAE V-Shape Line (Linear): y = |x| -->
  <path d="M 180 90 L 380 290 L 580 90" fill="none" stroke="#2563EB" stroke-width="3"/>
  <text x="600" y="100" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#2563EB">MAE Penalty: |e|</text>

  <!-- MSE Parabola (Quadratic): y = x^2 -->
  <path d="M 230 65 Q 380 340 530 65" fill="none" stroke="#DC2626" stroke-width="3"/>
  <text x="545" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">MSE Penalty: e&#178;</text>

  <!-- Key comparison cards -->
  <rect x="90" y="60" width="130" height="50" rx="6" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
  <text x="155" y="80" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">Small Errors (e &lt; 1)</text>
  <text x="155" y="98" font-family="-apple-system, sans-serif" font-size="10" fill="#1E3A8A" text-anchor="middle">e&#178; &lt; |e| (Tolerant)</text>

  <rect x="90" y="125" width="130" height="50" rx="6" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
  <text x="155" y="145" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">Large Errors (e &gt; 2)</text>
  <text x="155" y="163" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">e&#178; &gt;&gt; |e| (Punishing)</text>

  <rect x="80" y="325" width="600" height="25" rx="4" fill="#F8FAFC"/>
  <text x="380" y="342" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Squaring errors makes MSE differentiable (easy to optimize) but highly sensitive to extreme outliers.</text>
</svg>"""

# ----------------------------------------------------------------------
# 8. SVG_OLS_CALCULATION_ENGINE: Closed-Form Formulas & Worked Example
# ----------------------------------------------------------------------
SVG_OLS_CALCULATION_ENGINE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="430" y="30" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">ORDINARY LEAST SQUARES (OLS): CLOSED-FORM NORMAL EQUATIONS</text>

  <!-- Left Card: Slope Formula -->
  <rect x="40" y="55" width="370" height="180" rx="10" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
  <rect x="55" y="70" width="340" height="28" rx="6" fill="#4F46E5"/>
  <text x="225" y="89" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">SLOPE (&#946;&#8321;) FORMULA</text>
  <rect x="55" y="110" width="340" height="48" rx="6" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="1"/>
  <text x="225" y="132" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#312E81" text-anchor="middle">&#946;&#8321; = &#931;(x&#7522; - x&#772;)(y&#7522; - y&#772;) / &#931;(x&#7522; - x&#772;)&#178;</text>
  <text x="225" y="150" font-family="-apple-system, sans-serif" font-size="11" fill="#4338CA" text-anchor="middle">= Covariance(X, Y) / Variance(X)</text>
  <text x="225" y="180" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#1E1B4B" text-anchor="middle">Worked Example (5 Samples):</text>
  <text x="225" y="202" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#4F46E5" text-anchor="middle">&#946;&#8321; = 16.0 / 10.0 = 1.600</text>

  <!-- Right Card: Intercept Formula -->
  <rect x="450" y="55" width="370" height="180" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
  <rect x="465" y="70" width="340" height="28" rx="6" fill="#16A34A"/>
  <text x="635" y="89" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">INTERCEPT (&#946;&#8320;) FORMULA</text>
  <rect x="465" y="110" width="340" height="48" rx="6" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1"/>
  <text x="635" y="132" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#14532D" text-anchor="middle">&#946;&#8320; = y&#772; - &#946;&#8321; × x&#772;</text>
  <text x="635" y="150" font-family="-apple-system, sans-serif" font-size="11" fill="#15803D" text-anchor="middle">Guarantees line passes through centroid (x&#772;, y&#772;)</text>
  <text x="635" y="180" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#064E3B" text-anchor="middle">Worked Example (x&#772; = 3.0, y&#772; = 5.0):</text>
  <text x="635" y="202" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#16A34A" text-anchor="middle">&#946;&#8320; = 5.0 - (1.600 × 3.0) = 0.200</text>

  <!-- Bottom Result Banner -->
  <rect x="40" y="255" width="780" height="80" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="430" y="280" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Final Analytical OLS Fitted Model:</text>
  <text x="430" y="308" font-family="Courier New, monospace" font-size="18" font-weight="700" fill="#4F46E5" text-anchor="middle">&#375; = 0.200 + 1.600 × x</text>
  <text x="430" y="326" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Scikit-Learn LinearRegression calculates these identical coefficients via numerical linear algebra.</text>
</svg>"""

# ----------------------------------------------------------------------
# 9. SVG_GRADIENT_DESCENT_CURVE: Loss Surface & Iteration Curve
# ----------------------------------------------------------------------
SVG_GRADIENT_DESCENT_CURVE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="430" y="30" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">GRADIENT DESCENT: CONVERGENCE TOWARD GLOBAL MINIMUM</text>

  <!-- Left: Convex Bowl Concept -->
  <rect x="40" y="55" width="370" height="280" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="225" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#334155" text-anchor="middle">Convex MSE Loss Bowl J(w, b)</text>
  <path d="M 80 120 Q 225 310 370 120" fill="none" stroke="#4F46E5" stroke-width="3"/>
  <!-- Steps descending -->
  <circle cx="100" cy="140" r="6" fill="#DC2626"/>
  <line x1="100" y1="140" x2="140" y2="190" stroke="#DC2626" stroke-width="2" stroke-dasharray="3,3"/>
  <circle cx="140" cy="190" r="5" fill="#D97706"/>
  <line x1="140" y1="190" x2="185" y2="225" stroke="#D97706" stroke-width="2" stroke-dasharray="3,3"/>
  <circle cx="185" cy="225" r="5" fill="#D97706"/>
  <line x1="185" y1="225" x2="225" y2="238" stroke="#16A34A" stroke-width="2"/>
  <circle cx="225" cy="238" r="7" fill="#16A34A"/>
  <text x="225" y="265" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#16A34A" text-anchor="middle">&#10003; Global Minimum (Loss &#8776; 0.08)</text>
  <text x="225" y="305" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#312E81" text-anchor="middle">w_new = w - &#945; × (&#8706;J / &#8706;w)</text>

  <!-- Right: Iteration Curve -->
  <rect x="450" y="55" width="370" height="280" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="635" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#334155" text-anchor="middle">MSE Loss vs Training Epochs</text>
  <line x1="480" y1="280" x2="790" y2="280" stroke="#94A3B8" stroke-width="1.5"/> <!-- Epochs -->
  <line x1="480" y1="100" x2="480" y2="280" stroke="#94A3B8" stroke-width="1.5"/> <!-- Loss -->

  <!-- Actual decay curve -->
  <path d="M 485 110 Q 520 260 780 272" fill="none" stroke="#DC2626" stroke-width="3"/>
  <circle cx="485" cy="110" r="5" fill="#DC2626"/>
  <text x="515" y="115" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">Epoch 0: Loss = 12.0</text>
  <circle cx="780" cy="272" r="5" fill="#16A34A"/>
  <text x="730" y="260" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#16A34A">Epoch 100: Loss = 0.08</text>

  <text x="635" y="302" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Iterations / Epochs (0 &#8594; 100)</text>
  <text transform="rotate(-90 470 190)" x="470" y="190" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Loss (MSE)</text>
  <text x="635" y="325" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#4338CA" text-anchor="middle">Smooth exponential decay proves convergence</text>
</svg>"""

# ----------------------------------------------------------------------
# 10. SVG_ACTUAL_VS_PREDICTED: Actual vs Predicted with 45-degree Line
# ----------------------------------------------------------------------
SVG_ACTUAL_VS_PREDICTED = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="100%">
  <rect width="760" height="380" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="380" y="32" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">ACTUAL VS PREDICTED PLOT: EVALUATING PREDICTION ACCURACY</text>

  <!-- Axes -->
  <line x1="100" y1="310" x2="680" y2="310" stroke="#CBD5E1" stroke-width="2"/>
  <line x1="100" y1="60" x2="100" y2="310" stroke="#CBD5E1" stroke-width="2"/>

  <!-- Ideal 45-degree Reference Line (y = y_hat) -->
  <line x1="100" y1="310" x2="660" y2="70" stroke="#94A3B8" stroke-width="2.5" stroke-dasharray="6,4"/>
  <text x="600" y="60" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#64748B">Ideal Fit: y = &#375;</text>

  <!-- Tightly clustered test predictions around 45-deg line (R2 = 0.97) -->
  <circle cx="170" cy="275" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>
  <circle cx="210" cy="265" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>
  <circle cx="260" cy="235" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>
  <circle cx="310" cy="220" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>
  <circle cx="340" cy="210" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>
  <circle cx="390" cy="180" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>
  <circle cx="430" cy="170" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>
  <circle cx="480" cy="145" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>
  <circle cx="530" cy="120" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>
  <circle cx="570" cy="115" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>
  <circle cx="620" cy="85" r="5.5" fill="#4F46E5" fill-opacity="0.85"/>

  <!-- Axis labels -->
  <text x="390" y="340" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#334155" text-anchor="middle">Actual Values: y ($k)</text>
  <text transform="rotate(-90 40 185)" x="40" y="185" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#334155" text-anchor="middle">Predicted Values: &#375; ($k)</text>

  <!-- Score card -->
  <rect x="440" y="210" width="220" height="75" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
  <text x="455" y="232" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#166534">High Agreement (R&#178; = 0.970)</text>
  <text x="455" y="252" font-family="-apple-system, sans-serif" font-size="11" fill="#15803D">&#8226; Points hug 45&#176; line closely</text>
  <text x="455" y="270" font-family="-apple-system, sans-serif" font-size="11" fill="#15803D">&#8226; Test MAE = $15.98k (tight bounds)</text>
</svg>"""

# ----------------------------------------------------------------------
# 11. SVG_RESIDUAL_PLOT: Residuals vs Fitted Values (Diagnostics)
# ----------------------------------------------------------------------
SVG_RESIDUAL_PLOT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="430" y="30" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">RESIDUAL PLOTS: DIAGNOSING HOMOSCEDASTICITY VS PATTERNS</text>

  <!-- Panel 1: Ideal Homoscedastic Scatter -->
  <rect x="35" y="55" width="380" height="280" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="225" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#16A34A" text-anchor="middle">&#10003; Ideal: Constant Variance (Homoscedastic)</text>
  <!-- Horizontal zero line -->
  <line x1="55" y1="180" x2="395" y2="180" stroke="#16A34A" stroke-width="2"/>
  <text x="390" y="175" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#16A34A">e = 0</text>
  <!-- Random uniform scatter -->
  <circle cx="85" cy="165" r="4.5" fill="#4F46E5"/>
  <circle cx="115" cy="200" r="4.5" fill="#4F46E5"/>
  <circle cx="145" cy="170" r="4.5" fill="#4F46E5"/>
  <circle cx="175" cy="155" r="4.5" fill="#4F46E5"/>
  <circle cx="205" cy="210" r="4.5" fill="#4F46E5"/>
  <circle cx="235" cy="175" r="4.5" fill="#4F46E5"/>
  <circle cx="265" cy="190" r="4.5" fill="#4F46E5"/>
  <circle cx="295" cy="160" r="4.5" fill="#4F46E5"/>
  <circle cx="325" cy="205" r="4.5" fill="#4F46E5"/>
  <circle cx="355" cy="170" r="4.5" fill="#4F46E5"/>
  <text x="225" y="300" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">Even bounce above/below zero; no pattern.</text>
  <text x="225" y="318" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">Assumptions Satisfied!</text>

  <!-- Panel 2: Flawed Funnel / Non-linear Pattern -->
  <rect x="445" y="55" width="380" height="280" rx="10" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
  <text x="635" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#DC2626" text-anchor="middle">&#10007; Flawed: Heteroscedastic Funnel</text>
  <!-- Horizontal zero line -->
  <line x1="465" y1="180" x2="805" y2="180" stroke="#DC2626" stroke-width="2"/>
  <text x="800" y="175" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#DC2626">e = 0</text>
  <!-- Funnel widening scatter -->
  <circle cx="495" cy="178" r="4.5" fill="#DC2626"/>
  <circle cx="525" cy="182" r="4.5" fill="#DC2626"/>
  <circle cx="555" cy="172" r="4.5" fill="#DC2626"/>
  <circle cx="585" cy="192" r="4.5" fill="#DC2626"/>
  <circle cx="615" cy="160" r="4.5" fill="#DC2626"/>
  <circle cx="645" cy="215" r="4.5" fill="#DC2626"/>
  <circle cx="675" cy="140" r="4.5" fill="#DC2626"/>
  <circle cx="705" cy="235" r="4.5" fill="#DC2626"/>
  <circle cx="735" cy="120" r="4.5" fill="#DC2626"/>
  <circle cx="765" cy="255" r="4.5" fill="#DC2626"/>
  <text x="635" y="300" font-family="-apple-system, sans-serif" font-size="11" fill="#991B1B" text-anchor="middle">Error spread expands as predictions grow.</text>
  <text x="635" y="318" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">Requires Log Transform or Robust Errors</text>
</svg>"""

# ----------------------------------------------------------------------
# 12. SVG_OUTLIER_INFLUENCE: Clean vs High-Leverage Influential Point
# ----------------------------------------------------------------------
SVG_OUTLIER_INFLUENCE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="100%">
  <rect width="760" height="380" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="380" y="32" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">HIGH-LEVERAGE OUTLIERS: HOW A SINGLE POINT ROTATES OLS</text>

  <!-- Axes -->
  <line x1="80" y1="310" x2="700" y2="310" stroke="#CBD5E1" stroke-width="2"/>
  <line x1="80" y1="60" x2="80" y2="310" stroke="#CBD5E1" stroke-width="2"/>

  <!-- Clean regression line (slope = 1.98) -->
  <line x1="90" y1="290" x2="620" y2="70" stroke="#16A34A" stroke-width="3"/>
  <text x="625" y="75" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#16A34A">Clean Line (Slope &#8776; 1.98)</text>

  <!-- Outlier-corrupted regression line (slope = 0.59) -->
  <line x1="90" y1="260" x2="700" y2="160" stroke="#DC2626" stroke-width="3" stroke-dasharray="6,4"/>
  <text x="705" y="165" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">Rotated Line (Slope &#8776; 0.59)</text>

  <!-- Normal points -->
  <circle cx="140" cy="270" r="5" fill="#4F46E5"/>
  <circle cx="210" cy="240" r="5" fill="#4F46E5"/>
  <circle cx="280" cy="210" r="5" fill="#4F46E5"/>
  <circle cx="350" cy="180" r="5" fill="#4F46E5"/>
  <circle cx="420" cy="140" r="5" fill="#4F46E5"/>
  <circle cx="490" cy="110" r="5" fill="#4F46E5"/>

  <!-- Extreme Outlier with High Leverage (far out in X, aberrant in Y) -->
  <circle cx="670" cy="285" r="9" fill="#DC2626" stroke="#991B1B" stroke-width="2"/>
  <rect x="520" y="300" width="180" height="30" rx="4" fill="#FEF2F2" stroke="#F87171" stroke-width="1"/>
  <text x="610" y="320" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">&#9888; High-Leverage Outlier (7, 1)</text>

  <!-- Explanation banner -->
  <rect x="80" y="340" width="600" height="28" rx="4" fill="#F8FAFC"/>
  <text x="380" y="358" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Because squared error penalizes distance quadratically, an extreme high-leverage point exerts massive torque on OLS.</text>
</svg>"""

# ----------------------------------------------------------------------
# 13. SVG_SIMPLE_VS_MULTIPLE_REGRESSION: 2D Line vs 3D Hyperplane
# ----------------------------------------------------------------------
SVG_SIMPLE_VS_MULTIPLE_REGRESSION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="430" y="30" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">GEOMETRIC DIMENSIONALITY: 2D LINE VS MULTI-FEATURE HYPERPLANE</text>

  <!-- Left: 2D Simple Linear Regression -->
  <rect x="40" y="55" width="370" height="280" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="225" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#334155" text-anchor="middle">Simple Regression: 1 Feature (2D)</text>
  <line x1="70" y1="260" x2="380" y2="260" stroke="#94A3B8" stroke-width="1.5"/> <!-- X1 -->
  <line x1="70" y1="90" x2="70" y2="260" stroke="#94A3B8" stroke-width="1.5"/> <!-- Y -->
  <line x1="80" y1="240" x2="370" y2="110" stroke="#4F46E5" stroke-width="3"/>
  <circle cx="150" cy="220" r="4.5" fill="#4F46E5"/>
  <circle cx="230" cy="180" r="4.5" fill="#4F46E5"/>
  <circle cx="310" cy="130" r="4.5" fill="#4F46E5"/>
  <text x="225" y="280" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4F46E5" text-anchor="middle">Decision Surface: 1-Dimensional Line</text>
  <text x="225" y="300" font-family="Courier New, monospace" font-size="13" fill="#1E1B4B" text-anchor="middle">&#375; = &#946;&#8320; + &#946;&#8321;x&#8321;</text>

  <!-- Right: 3D Multiple Linear Regression (Plane) -->
  <rect x="450" y="55" width="370" height="280" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="635" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#334155" text-anchor="middle">Multiple Regression: 2+ Features (3D+)</text>
  <!-- Isometric 3D axes -->
  <line x1="490" y1="260" x2="780" y2="260" stroke="#94A3B8" stroke-width="1.5"/> <!-- X1 -->
  <line x1="490" y1="260" x2="490" y2="90" stroke="#94A3B8" stroke-width="1.5"/> <!-- Y -->
  <line x1="490" y1="260" x2="420" y2="300" stroke="#94A3B8" stroke-width="1.5"/> <!-- X2 -->
  <!-- 2D Plane representing 2 features -->
  <polygon points="520,220 740,160 700,100 480,160" fill="#EEF2FF" fill-opacity="0.8" stroke="#4F46E5" stroke-width="2"/>
  <circle cx="560" cy="170" r="4.5" fill="#16A34A"/>
  <circle cx="620" cy="140" r="4.5" fill="#16A34A"/>
  <circle cx="680" cy="120" r="4.5" fill="#16A34A"/>
  <text x="635" y="280" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#16A34A" text-anchor="middle">Decision Surface: 2D Plane (or Hyperplane in P-dim)</text>
  <text x="635" y="300" font-family="Courier New, monospace" font-size="13" fill="#064E3B" text-anchor="middle">&#375; = &#946;&#8320; + &#946;&#8321;x&#8321; + &#946;&#8322;x&#8322; + ... + &#946;&#7522;x&#7522;</text>
</svg>"""

# ----------------------------------------------------------------------
# 14. SVG_LAB_EVALUATION_SUMMARY: Summary Scorecard & Metrics Comparison
# ----------------------------------------------------------------------
SVG_LAB_EVALUATION_SUMMARY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 340" width="100%">
  <rect width="880" height="340" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="440" y="30" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">PYTHON PRACTICAL LAB EVALUATION SCORECARD</text>

  <!-- Left: Simple Linear Regression (1 Feature) -->
  <rect x="35" y="55" width="385" height="260" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="50" y="70" width="355" height="28" rx="6" fill="#64748B"/>
  <text x="227" y="89" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">SIMPLE LINEAR REGRESSION (AREA ONLY)</text>
  
  <text x="60" y="125" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#334155">Test R&#178; Score:</text>
  <text x="380" y="125" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#4F46E5" text-anchor="end">0.8583 (85.8%)</text>

  <text x="60" y="155" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#334155">Test MAE:</text>
  <text x="380" y="155" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#334155" text-anchor="end">$35.04k USD</text>

  <text x="60" y="185" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#334155">Test RMSE:</text>
  <text x="380" y="185" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#334155" text-anchor="end">$42.71k USD</text>

  <text x="60" y="215" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#334155">Fitted Slope (Area):</text>
  <text x="380" y="215" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#0284C7" text-anchor="end">+$143.0 / sq ft</text>

  <rect x="50" y="240" width="355" height="60" rx="6" fill="#F1F5F9"/>
  <text x="227" y="260" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">Interpretation:</text>
  <text x="227" y="280" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Solid baseline fit, but omits bedrooms, age, and location.</text>

  <!-- Right: Multiple Linear Regression (4 Features) -->
  <rect x="460" y="55" width="385" height="260" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
  <rect x="475" y="70" width="355" height="28" rx="6" fill="#16A34A"/>
  <text x="652" y="89" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">MULTIPLE LINEAR REGRESSION (4 FEATURES)</text>

  <text x="485" y="125" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#166534">Test R&#178; Score:</text>
  <text x="805" y="125" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#16A34A" text-anchor="end">0.9700 (97.0%) &#10003;</text>

  <text x="485" y="155" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#166534">Test MAE:</text>
  <text x="805" y="155" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#166534" text-anchor="end">$15.98k USD (-54%)</text>

  <text x="485" y="185" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#166534">Test RMSE:</text>
  <text x="805" y="185" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#166534" text-anchor="end">$19.67k USD (-54%)</text>

  <text x="485" y="215" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#166534">Key Coefficients:</text>
  <text x="805" y="215" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#14532D" text-anchor="end">Bed: +$20.4k | Age: -$1.4k/yr</text>

  <rect x="475" y="240" width="355" height="60" rx="6" fill="#DCFCE7"/>
  <text x="652" y="260" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#15803D" text-anchor="middle">Superior Generalization:</text>
  <text x="652" y="280" font-family="-apple-system, sans-serif" font-size="11" fill="#166534" text-anchor="middle">Error halved by incorporating multi-dimensional feature context.</text>
</svg>"""

ALL_SVGS = [
    ("SVG_REGRESSION_HERO", SVG_REGRESSION_HERO),
    ("SVG_SCATTER_OBSERVATIONS", SVG_SCATTER_OBSERVATIONS),
    ("SVG_LINE_OF_BEST_FIT", SVG_LINE_OF_BEST_FIT),
    ("SVG_COMPARING_CANDIDATE_LINES", SVG_COMPARING_CANDIDATE_LINES),
    ("SVG_SLOPE_INTERCEPT_VARIATIONS", SVG_SLOPE_INTERCEPT_VARIATIONS),
    ("SVG_RESIDUAL_LINES", SVG_RESIDUAL_LINES),
    ("SVG_LOSS_FUNCTION_COMPARISON", SVG_LOSS_FUNCTION_COMPARISON),
    ("SVG_OLS_CALCULATION_ENGINE", SVG_OLS_CALCULATION_ENGINE),
    ("SVG_GRADIENT_DESCENT_CURVE", SVG_GRADIENT_DESCENT_CURVE),
    ("SVG_ACTUAL_VS_PREDICTED", SVG_ACTUAL_VS_PREDICTED),
    ("SVG_RESIDUAL_PLOT", SVG_RESIDUAL_PLOT),
    ("SVG_OUTLIER_INFLUENCE", SVG_OUTLIER_INFLUENCE),
    ("SVG_SIMPLE_VS_MULTIPLE_REGRESSION", SVG_SIMPLE_VS_MULTIPLE_REGRESSION),
    ("SVG_LAB_EVALUATION_SUMMARY", SVG_LAB_EVALUATION_SUMMARY)
]

if __name__ == '__main__':
    print(f"Validating {len(ALL_SVGS)} Topic 9 SVGs for XML compliance...")
    for name, svg_str in ALL_SVGS:
        try:
            ET.fromstring(svg_str)
            print(f"  [XML PASS] {name}")
        except Exception as e:
            print(f"  [XML FAIL] {name}: {e}")
            raise
    print("All Topic 9 SVGs validated successfully!")
