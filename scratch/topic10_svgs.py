"""
Module: topic10_svgs.py
Contains 14 hand-crafted, XML-valid vector diagrams for Topic 10: Logistic Regression.
All SVGs adhere strictly to Light Mode aesthetics, valid XML structure, and responsive viewBoxes.
"""

import xml.etree.ElementTree as ET

# ----------------------------------------------------------------------
# 1. SVG_LOGREG_HERO: The Complete Logistic Regression Pipeline
# ----------------------------------------------------------------------
SVG_LOGREG_HERO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%">
  <rect width="920" height="340" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="20" y="20" width="880" height="42" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="46" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">SUPERVISED CLASSIFICATION: FROM LINEAR SCORE TO CALIBRATED PROBABILITY</text>

  <!-- Stage 1: Input Features -->
  <rect x="40" y="85" width="180" height="225" rx="12" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
  <rect x="55" y="100" width="150" height="28" rx="6" fill="#4F46E5"/>
  <text x="130" y="118" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">1. INPUT FEATURES (X)</text>
  <text x="130" y="150" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#334155" text-anchor="middle">Patient / User Signals</text>
  <text x="130" y="176" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">&#8226; Blood Pressure (x&#8321;)</text>
  <text x="130" y="200" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">&#8226; Blood Sugar (x&#8322;)</text>
  <text x="130" y="224" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">&#8226; Patient Age (x&#8323;)</text>
  <rect x="55" y="255" width="150" height="38" rx="6" fill="#E0E7FF"/>
  <text x="130" y="278" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">Unconstrained Inputs</text>

  <!-- Arrow 1 -->
  <line x1="225" y1="190" x2="255" y2="190" stroke="#4F46E5" stroke-width="2.5" stroke-dasharray="3,3"/>
  <polygon points="265,190 253,184 253,196" fill="#4F46E5"/>

  <!-- Stage 2: Linear Score (Logit) -->
  <rect x="270" y="85" width="180" height="225" rx="12" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
  <rect x="285" y="100" width="150" height="28" rx="6" fill="#0284C7"/>
  <text x="360" y="118" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">2. LINEAR LOGIT (z)</text>
  <rect x="285" y="138" width="150" height="42" rx="6" fill="#E0F2FE" stroke="#7DD3FC" stroke-width="1"/>
  <text x="360" y="164" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#0369A1" text-anchor="middle">z = &#946;&#8320; + &#931; &#946;&#1138; x&#1138;</text>
  <text x="360" y="202" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#0C4A6E" text-anchor="middle">Weighted Sum (Bias + Slopes)</text>
  <text x="360" y="222" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#0369A1" text-anchor="middle">Domain: (-&#8734;, +&#8734;)</text>
  <rect x="285" y="255" width="150" height="38" rx="6" fill="#BAE6FD"/>
  <text x="360" y="278" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#0369A1" text-anchor="middle">Unbounded Real Number</text>

  <!-- Arrow 2 -->
  <line x1="455" y1="190" x2="485" y2="190" stroke="#0284C7" stroke-width="2.5" stroke-dasharray="3,3"/>
  <polygon points="495,190 483,184 483,196" fill="#0284C7"/>

  <!-- Stage 3: Sigmoid Transformation -->
  <rect x="500" y="85" width="180" height="225" rx="12" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
  <rect x="515" y="100" width="150" height="28" rx="6" fill="#16A34A"/>
  <text x="590" y="118" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">3. SIGMOID &#963;(z)</text>
  <rect x="515" y="138" width="150" height="42" rx="6" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1"/>
  <text x="590" y="164" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#15803D" text-anchor="middle">p = 1 / (1 + e&#8315;&#769;)</text>
  <text x="590" y="202" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#14532D" text-anchor="middle">S-Curve Compression</text>
  <text x="590" y="222" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#15803D" text-anchor="middle">Range: Strictly (0, 1)</text>
  <rect x="515" y="255" width="150" height="38" rx="6" fill="#BBF7D0"/>
  <text x="590" y="278" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#14532D" text-anchor="middle">Calibrated Probability</text>

  <!-- Arrow 3 -->
  <line x1="685" y1="190" x2="715" y2="190" stroke="#16A34A" stroke-width="2.5" stroke-dasharray="3,3"/>
  <polygon points="725,190 713,184 713,196" fill="#16A34A"/>

  <!-- Stage 4: Decision Threshold & Prediction -->
  <rect x="730" y="85" width="155" height="225" rx="12" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
  <rect x="742" y="100" width="130" height="28" rx="6" fill="#D97706"/>
  <text x="807" y="118" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">4. THRESHOLD &#964;</text>
  <rect x="742" y="138" width="130" height="42" rx="6" fill="#FEF3C7" stroke="#FCD34D" stroke-width="1"/>
  <text x="807" y="164" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#92400E" text-anchor="middle">&#375; = 1 if p &#8805; 0.50</text>
  <text x="807" y="202" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#92400E" text-anchor="middle">Default Threshold &#964;=0.5</text>
  <text x="807" y="222" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#78350F" text-anchor="middle">Output: Class 0 or 1</text>
  <rect x="742" y="255" width="130" height="38" rx="6" fill="#FDE68A"/>
  <text x="807" y="278" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#78350F" text-anchor="middle">Binary Decision</text>
</svg>"""

# ----------------------------------------------------------------------
# 2. SVG_LINEAR_VS_SIGMOID: Linear Output vs Sigmoid Output
# ----------------------------------------------------------------------
SVG_LINEAR_VS_SIGMOID = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">ORDINARY LINEAR REGRESSION VS. LOGISTIC REGRESSION</text>

  <!-- Left: Linear Regression Flaw -->
  <g transform="translate(40, 55)">
    <rect width="365" height="280" rx="10" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
    <text x="182" y="24" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#DC2626" text-anchor="middle">Ordinary Linear Regression (Flawed for Probabilities)</text>
    
    <!-- Coordinate Box -->
    <rect x="50" y="45" width="280" height="180" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    
    <!-- Valid probability boundary 0 to 1 -->
    <line x1="50" y1="185" x2="330" y2="185" stroke="#64748B" stroke-width="1"/>
    <text x="42" y="190" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">0.0</text>
    <line x1="50" y1="85" x2="330" y2="85" stroke="#64748B" stroke-width="1"/>
    <text x="42" y="90" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">1.0</text>
    
    <!-- Shaded valid band -->
    <rect x="50" y="85" width="280" height="100" fill="#F0FDF4" opacity="0.4"/>
    <text x="190" y="140" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#15803D" text-anchor="middle">Valid Probability Region [0, 1]</text>

    <!-- Straight Linear Line -->
    <line x1="60" y1="215" x2="320" y2="55" stroke="#DC2626" stroke-width="2.5"/>
    
    <!-- Danger zone annotations -->
    <rect x="235" y="48" width="90" height="28" rx="4" fill="#FEE2E2" stroke="#EF4444" stroke-width="1"/>
    <text x="280" y="66" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" fill="#B91C1C" text-anchor="middle">&#375; &gt; 1.0 (Nonsense!)</text>

    <rect x="65" y="192" width="90" height="28" rx="4" fill="#FEE2E2" stroke="#EF4444" stroke-width="1"/>
    <text x="110" y="210" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" fill="#B91C1C" text-anchor="middle">&#375; &lt; 0.0 (Impossible!)</text>

    <text x="182" y="255" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#991B1B" text-anchor="middle">Linear model produces values &lt; 0 or &gt; 1</text>
    <text x="182" y="270" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">Violates probability axioms and causes extreme distortions</text>
  </g>

  <!-- Right: Logistic Sigmoid Solution -->
  <g transform="translate(450, 55)">
    <rect width="370" height="280" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
    <text x="185" y="24" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#16A34A" text-anchor="middle">Logistic Regression (S-Curve Bounded in [0, 1])</text>

    <!-- Coordinate Box -->
    <rect x="50" y="45" width="280" height="180" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Asymptote lines -->
    <line x1="50" y1="185" x2="330" y2="185" stroke="#94A3B8" stroke-width="1" stroke-dasharray="3,3"/>
    <text x="42" y="190" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">0.0</text>
    <line x1="50" y1="85" x2="330" y2="85" stroke="#94A3B8" stroke-width="1" stroke-dasharray="3,3"/>
    <text x="42" y="90" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">1.0</text>
    
    <!-- Threshold line at 0.5 -->
    <line x1="50" y1="135" x2="330" y2="135" stroke="#CBD5E1" stroke-width="1"/>
    <text x="42" y="140" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">0.5</text>

    <!-- Sigmoid S-Curve -->
    <path d="M 55,182 C 120,182 150,175 190,135 C 230,95 260,88 325,88" fill="none" stroke="#16A34A" stroke-width="3"/>

    <!-- Center Point Annotation -->
    <circle cx="190" cy="135" r="5" fill="#4F46E5"/>
    <rect x="145" y="105" width="90" height="22" rx="4" fill="#EEF2FF" stroke="#818CF8" stroke-width="1"/>
    <text x="190" y="120" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" fill="#4338CA" text-anchor="middle">z = 0 &#8594; p = 0.50</text>

    <text x="185" y="255" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#166534" text-anchor="middle">Sigmoid naturally confines predictions to (0, 1)</text>
    <text x="185" y="270" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#14532D" text-anchor="middle">Smooth S-curve models probability with mathematical rigor</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 3. SVG_SIGMOID_CURVE: Understanding the Sigmoid Curve & Asymptotes
# ----------------------------------------------------------------------
SVG_SIGMOID_CURVE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 380" width="100%">
  <rect width="860" height="380" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">THE STANDARD LOGISTIC SIGMOID FUNCTION: &#963;(z) = 1 / (1 + e&#8315;&#769;)</text>

  <!-- Plot Canvas -->
  <g transform="translate(90, 50)">
    <rect width="680" height="260" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Horizontal Grid & Asymptotes -->
    <line x1="0" y1="20" x2="680" y2="20" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="-15" y="25" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#DC2626" text-anchor="end">1.0</text>
    <text x="690" y="25" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#DC2626">Upper Asymptote (z &#8594; +&#8734;)</text>

    <line x1="0" y1="130" x2="680" y2="130" stroke="#94A3B8" stroke-width="1" stroke-dasharray="2,2"/>
    <text x="-15" y="135" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#475569" text-anchor="end">0.5</text>
    <text x="690" y="135" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#475569">Symmetry Center Point</text>

    <line x1="0" y1="240" x2="680" y2="240" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="-15" y="245" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#DC2626" text-anchor="end">0.0</text>
    <text x="690" y="245" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#DC2626">Lower Asymptote (z &#8594; -&#8734;)</text>

    <!-- Vertical Axis at z = 0 -->
    <line x1="340" y1="0" x2="340" y2="260" stroke="#0F172A" stroke-width="1.5"/>
    <text x="340" y="280" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">z = 0</text>

    <!-- Tick marks for z -->
    <text x="100" y="280" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">z = -5</text>
    <text x="220" y="280" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">z = -1.8</text>
    <text x="460" y="280" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">z = +1.8</text>
    <text x="580" y="280" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">z = +5</text>

    <!-- Sigmoid S-Curve -->
    <path d="M 10,238 C 120,238 200,230 280,180 C 320,150 340,130 360,110 C 440,30 520,22 670,22" fill="none" stroke="#4F46E5" stroke-width="3.5"/>

    <!-- Key Points Callouts -->
    <!-- Point 1: z = 0, p = 0.5 -->
    <circle cx="340" cy="130" r="5" fill="#4F46E5"/>
    <rect x="350" y="118" width="115" height="24" rx="4" fill="#EEF2FF" stroke="#818CF8" stroke-width="1"/>
    <text x="407" y="134" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">&#963;(0.0) = 0.5000</text>

    <!-- Point 2: z = +1.8, p = 0.8581 -->
    <circle cx="460" cy="51" r="5" fill="#16A34A"/>
    <line x1="460" y1="51" x2="460" y2="260" stroke="#16A34A" stroke-width="1" stroke-dasharray="2,2"/>
    <rect x="470" y="40" width="125" height="24" rx="4" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1"/>
    <text x="532" y="56" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">&#963;(+1.8) = 0.8581</text>

    <!-- Point 3: z = -1.8, p = 0.1419 -->
    <circle cx="220" cy="209" r="5" fill="#EA580C"/>
    <line x1="220" y1="209" x2="220" y2="260" stroke="#EA580C" stroke-width="1" stroke-dasharray="2,2"/>
    <rect x="90" y="197" width="125" height="24" rx="4" fill="#FFF7ED" stroke="#FDBA74" stroke-width="1"/>
    <text x="152" y="213" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#C2410C" text-anchor="middle">&#963;(-1.8) = 0.1419</text>

    <!-- Gradient / Slope note -->
    <rect x="250" y="5" width="180" height="40" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="340" y="22" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle">STEEPEST REGION (z &#8776; 0)</text>
    <text x="340" y="36" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Max slope = 0.25 (high sensitivity)</text>
  </g>

  <text x="430" y="360" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Symmetry Property: &#963;(z) + &#963;(-z) = 1.0 &#8226; Extremely large positive or negative z saturate gracefully without overflow.</text>
</svg>"""

# ----------------------------------------------------------------------
# 4. SVG_ODDS_PROB_MAPPING: Probability vs Odds vs Log-Odds
# ----------------------------------------------------------------------
SVG_ODDS_PROB_MAPPING = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 320" width="100%">
  <rect width="880" height="320" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="440" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">THE MATHEMATICAL BRIDGE: PROBABILITY &#8594; ODDS &#8594; LOG-ODDS (LOGIT)</text>

  <!-- Step 1: Probability -->
  <g transform="translate(40, 60)">
    <rect width="240" height="230" rx="10" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
    <rect x="20" y="15" width="200" height="30" rx="6" fill="#4F46E5"/>
    <text x="120" y="35" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">1. PROBABILITY (p)</text>
    
    <text x="120" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#334155" text-anchor="middle">Bounded Ratio: [0, 1]</text>
    <text x="120" y="90" font-family="Courier New, monospace" font-size="11" fill="#4338CA" text-anchor="middle">p = Successes / Total</text>

    <!-- Example Pill -->
    <rect x="20" y="110" width="200" height="50" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="120" y="130" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Worked Example:</text>
    <text x="120" y="150" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#4F46E5" text-anchor="middle">p = 0.80 (80%)</text>

    <text x="120" y="185" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Intuitive human metric</text>
    <text x="120" y="202" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Bounded: Cannot be linear</text>
  </g>

  <!-- Arrow 1 to 2 -->
  <g transform="translate(290, 160)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#4F46E5" stroke-width="2.5"/>
    <polygon points="45,0 33,-6 33,6" fill="#4F46E5"/>
    <text x="22" y="-12" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#4F46E5" text-anchor="middle">p / (1-p)</text>
  </g>

  <!-- Step 2: Odds -->
  <g transform="translate(345, 60)">
    <rect width="240" height="230" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <rect x="20" y="15" width="200" height="30" rx="6" fill="#16A34A"/>
    <text x="120" y="35" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">2. ODDS: p / (1 - p)</text>

    <text x="120" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#14532D" text-anchor="middle">Ratio of Chance: [0, +&#8734;)</text>
    <text x="120" y="90" font-family="Courier New, monospace" font-size="11" fill="#15803D" text-anchor="middle">Odds = p / (1 - p)</text>

    <!-- Example Pill -->
    <rect x="20" y="110" width="200" height="50" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="120" y="130" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Worked Example:</text>
    <text x="120" y="150" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#16A34A" text-anchor="middle">0.8 / 0.2 = 4.0 (4 to 1)</text>

    <text x="120" y="185" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#166534" text-anchor="middle">Positive unbounded</text>
    <text x="120" y="202" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#166534" text-anchor="middle">Asymmetric around 1.0</text>
  </g>

  <!-- Arrow 2 to 3 -->
  <g transform="translate(595, 160)">
    <line x1="0" y1="0" x2="35" y2="0" stroke="#16A34A" stroke-width="2.5"/>
    <polygon points="45,0 33,-6 33,6" fill="#16A34A"/>
    <text x="22" y="-12" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#16A34A" text-anchor="middle">ln(Odds)</text>
  </g>

  <!-- Step 3: Log-Odds (Logit) -->
  <g transform="translate(650, 60)">
    <rect width="210" height="230" rx="10" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <rect x="15" y="15" width="180" height="30" rx="6" fill="#0284C7"/>
    <text x="105" y="35" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">3. LOG-ODDS (LOGIT)</text>

    <text x="105" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#0369A1" text-anchor="middle">Linear Space: (-&#8734;, +&#8734;)</text>
    <text x="105" y="90" font-family="Courier New, monospace" font-size="11" fill="#0284C7" text-anchor="middle">z = ln(Odds) = &#946;&#8320; + &#931;&#946;&#1138;x&#1138;</text>

    <!-- Example Pill -->
    <rect x="15" y="110" width="180" height="50" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="105" y="130" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Worked Example:</text>
    <text x="105" y="150" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#0284C7" text-anchor="middle">ln(4.0) = +1.3863</text>

    <text x="105" y="185" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#0C4A6E" text-anchor="middle">Fully Symmetric around 0</text>
    <text x="105" y="202" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#0C4A6E" text-anchor="middle">Ready for standard linear math!</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 5. SVG_THRESHOLD_VARIATION: Decision Threshold Shifting
# ----------------------------------------------------------------------
SVG_THRESHOLD_VARIATION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">DECISION THRESHOLDS (&#964;): BALANCING FALSE POSITIVES VS FALSE NEGATIVES</text>

  <!-- Number line canvas -->
  <g transform="translate(60, 60)">
    <rect width="740" height="250" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Probability Axis -->
    <line x1="50" y1="120" x2="690" y2="120" stroke="#64748B" stroke-width="2"/>
    <text x="50" y="145" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">0.0</text>
    <text x="690" y="145" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">1.0</text>

    <!-- 6 Verified Test Points: [0.15, 0.35, 0.48, 0.52, 0.75, 0.92] -->
    <!-- Scale: x = 50 + p * 640 -->
    <!-- p=0.15 -> x=146 -->
    <circle cx="146" cy="120" r="7" fill="#64748B"/>
    <text x="146" y="100" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">0.15</text>

    <!-- p=0.35 -> x=274 -->
    <circle cx="274" cy="120" r="7" fill="#64748B"/>
    <text x="274" y="100" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">0.35</text>

    <!-- p=0.48 -> x=357.2 -->
    <circle cx="357" cy="120" r="7" fill="#64748B"/>
    <text x="357" y="100" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">0.48</text>

    <!-- p=0.52 -> x=382.8 -->
    <circle cx="383" cy="120" r="7" fill="#64748B"/>
    <text x="383" y="100" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">0.52</text>

    <!-- p=0.75 -> x=530 -->
    <circle cx="530" cy="120" r="7" fill="#64748B"/>
    <text x="530" y="100" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">0.75</text>

    <!-- p=0.92 -> x=638.8 -->
    <circle cx="639" cy="120" r="7" fill="#64748B"/>
    <text x="639" y="100" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">0.92</text>

    <!-- Threshold 1: 0.30 (x = 50 + 0.3*640 = 242) -->
    <line x1="242" y1="30" x2="242" y2="210" stroke="#0284C7" stroke-width="2.5" stroke-dasharray="4,4"/>
    <rect x="180" y="25" width="125" height="40" rx="4" fill="#E0F2FE" stroke="#0284C7" stroke-width="1"/>
    <text x="242" y="42" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#0369A1" text-anchor="middle">&#964; = 0.30 (Sensitive)</text>
    <text x="242" y="58" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#0C4A6E" text-anchor="middle">5 Positives / 1 Neg</text>

    <!-- Threshold 2: 0.50 (x = 50 + 0.5*640 = 370) -->
    <line x1="370" y1="30" x2="370" y2="210" stroke="#4F46E5" stroke-width="3"/>
    <rect x="310" y="25" width="120" height="40" rx="4" fill="#EEF2FF" stroke="#4F46E5" stroke-width="1"/>
    <text x="370" y="42" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">&#964; = 0.50 (Default)</text>
    <text x="370" y="58" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#312E81" text-anchor="middle">3 Positives / 3 Neg</text>

    <!-- Threshold 3: 0.70 (x = 50 + 0.7*640 = 498) -->
    <line x1="498" y1="30" x2="498" y2="210" stroke="#D97706" stroke-width="2.5" stroke-dasharray="4,4"/>
    <rect x="440" y="25" width="120" height="40" rx="4" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
    <text x="500" y="42" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#92400E" text-anchor="middle">&#964; = 0.70 (Conservative)</text>
    <text x="500" y="58" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#78350F" text-anchor="middle">2 Positives / 4 Neg</text>

    <!-- Bottom Legend Banner -->
    <rect x="40" y="175" width="660" height="55" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <text x="370" y="195" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Trade-off Strategy:</text>
    <text x="370" y="215" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Lower threshold (&#964;=0.3) catches more sickness (high recall) &#8226; Higher threshold (&#964;=0.7) prevents spam inboxes (high precision)</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 6. SVG_DECISION_BOUNDARY_1D_2D: Decision Boundaries in 1D and 2D
# ----------------------------------------------------------------------
SVG_DECISION_BOUNDARY_1D_2D = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">DECISION BOUNDARIES: SEPARATING CLASSES IN 1D AND 2D FEATURE SPACE</text>

  <!-- Left: 1D Single Feature -->
  <g transform="translate(40, 55)">
    <rect width="365" height="280" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <text x="182" y="24" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#4F46E5" text-anchor="middle">1D Space: Single Cutoff Threshold</text>
    
    <!-- 1D Plot -->
    <rect x="35" y="45" width="295" height="180" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    
    <!-- S-curve line -->
    <path d="M 45,195 C 120,195 150,180 182,135 C 215,90 250,75 320,75" fill="none" stroke="#4F46E5" stroke-width="2.5"/>
    
    <!-- Horizontal threshold at 0.5 -->
    <line x1="35" y1="135" x2="330" y2="135" stroke="#94A3B8" stroke-width="1" stroke-dasharray="3,3"/>
    
    <!-- Vertical decision boundary -->
    <line x1="182" y1="45" x2="182" y2="225" stroke="#DC2626" stroke-width="2.5"/>
    <circle cx="182" cy="135" r="5" fill="#DC2626"/>

    <!-- Data points -->
    <circle cx="80" cy="205" r="5" fill="#EF4444"/>
    <circle cx="110" cy="205" r="5" fill="#EF4444"/>
    <circle cx="140" cy="205" r="5" fill="#EF4444"/>
    <circle cx="230" cy="65" r="5" fill="#10B981"/>
    <circle cx="260" cy="65" r="5" fill="#10B981"/>
    <circle cx="290" cy="65" r="5" fill="#10B981"/>

    <rect x="125" y="145" width="115" height="36" rx="4" fill="#FEE2E2" stroke="#DC2626" stroke-width="1"/>
    <text x="182" y="160" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">Boundary Point</text>
    <text x="182" y="174" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#B91C1C" text-anchor="middle">x* = -&#946;&#8320; / &#946;&#8321;</text>

    <text x="182" y="255" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#334155" text-anchor="middle">In 1D, the boundary is a single scalar point x*</text>
  </g>

  <!-- Right: 2D Feature Space -->
  <g transform="translate(450, 55)">
    <rect width="370" height="280" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <text x="185" y="24" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#0284C7" text-anchor="middle">2D Space: Linear Separating Hyperplane</text>

    <!-- 2D Canvas -->
    <rect x="40" y="45" width="290" height="180" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Linear Decision Line: beta0 + beta1*x1 + beta2*x2 = 0 -->
    <line x1="50" y1="210" x2="310" y2="60" stroke="#4F46E5" stroke-width="3"/>
    
    <!-- Class 0 Region (Red/Fail) -->
    <circle cx="80" cy="180" r="5" fill="#EF4444"/>
    <circle cx="100" cy="150" r="5" fill="#EF4444"/>
    <circle cx="120" cy="190" r="5" fill="#EF4444"/>
    <circle cx="140" cy="160" r="5" fill="#EF4444"/>
    <circle cx="90" cy="200" r="5" fill="#EF4444"/>
    <circle cx="65" cy="160" r="5" fill="#EF4444"/>
    <text x="85" y="130" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#DC2626">Class 0 (Fail)</text>

    <!-- Class 1 Region (Green/Pass) -->
    <circle cx="210" cy="80" r="5" fill="#10B981"/>
    <circle cx="240" cy="100" r="5" fill="#10B981"/>
    <circle cx="270" cy="70" r="5" fill="#10B981"/>
    <circle cx="230" cy="120" r="5" fill="#10B981"/>
    <circle cx="260" cy="110" r="5" fill="#10B981"/>
    <circle cx="280" cy="90" r="5" fill="#10B981"/>
    <text x="215" y="145" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#15803D">Class 1 (Pass)</text>

    <!-- Formula tag -->
    <rect x="120" y="80" width="130" height="26" rx="4" fill="#EEF2FF" stroke="#4F46E5" stroke-width="1"/>
    <text x="185" y="97" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#4338CA" text-anchor="middle">&#946;&#8320; + &#946;&#8321;x&#8321; + &#946;&#8322;x&#8322; = 0</text>

    <text x="185" y="255" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#334155" text-anchor="middle">In 2D, the decision boundary is a straight line</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 7. SVG_LOG_LOSS_CURVES: Binary Cross-Entropy Loss Dynamics
# ----------------------------------------------------------------------
SVG_LOG_LOSS_CURVES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">LOG LOSS (BINARY CROSS-ENTROPY): SEVERE PENALTIES FOR CONFIDENT MISTAKES</text>

  <!-- Left: Actual y = 1 -->
  <g transform="translate(40, 55)">
    <rect width="365" height="280" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="182" y="24" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#16A34A" text-anchor="middle">Case 1: Actual Label y = 1 (Positive)</text>
    
    <!-- Axes Box -->
    <rect x="45" y="45" width="280" height="180" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="45" y1="210" x2="325" y2="210" stroke="#0F172A" stroke-width="1.5"/>
    <line x1="45" y1="45" x2="45" y2="210" stroke="#0F172A" stroke-width="1.5"/>
    
    <text x="45" y="225" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="middle">0.0</text>
    <text x="315" y="225" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="middle">1.0</text>
    <text x="182" y="225" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Predicted Probability p &#8594;</text>

    <!-- Curve for -ln(p) -->
    <!-- p=1 -> loss=0 (x=315, y=210) -->
    <!-- p=0.9 -> loss=0.105 (x=288, y=200) -->
    <!-- p=0.5 -> loss=0.693 (x=180, y=148) -->
    <!-- p=0.1 -> loss=2.30 (x=72, y=60) -->
    <path d="M 60,48 Q 80,130 180,175 T 315,210" fill="none" stroke="#16A34A" stroke-width="3"/>

    <!-- Low loss point -->
    <circle cx="288" cy="200" r="5" fill="#16A34A"/>
    <text x="270" y="185" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#15803D">p=0.9 &#8594; 0.105</text>

    <!-- High loss point -->
    <circle cx="72" cy="60" r="5" fill="#DC2626"/>
    <text x="80" y="55" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#DC2626">p=0.1 &#8594; 2.303 (21.8&#215;!)</text>

    <text x="182" y="255" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#15803D" text-anchor="middle">Loss = -ln(p)</text>
    <text x="182" y="270" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#166534" text-anchor="middle">Loss goes to 0 as p &#8594; 1; explodes to &#8734; as p &#8594; 0</text>
  </g>

  <!-- Right: Actual y = 0 -->
  <g transform="translate(450, 55)">
    <rect width="370" height="280" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="185" y="24" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#DC2626" text-anchor="middle">Case 2: Actual Label y = 0 (Negative)</text>

    <!-- Axes Box -->
    <rect x="45" y="45" width="280" height="180" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="45" y1="210" x2="325" y2="210" stroke="#0F172A" stroke-width="1.5"/>
    <line x1="45" y1="45" x2="45" y2="210" stroke="#0F172A" stroke-width="1.5"/>

    <text x="45" y="225" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="middle">0.0</text>
    <text x="315" y="225" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="middle">1.0</text>
    <text x="185" y="225" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Predicted Probability p &#8594;</text>

    <!-- Curve for -ln(1-p) -->
    <!-- p=0 -> loss=0 (x=45, y=210) -->
    <!-- p=0.1 -> loss=0.105 (x=72, y=200) -->
    <!-- p=0.5 -> loss=0.693 (x=180, y=148) -->
    <!-- p=0.9 -> loss=2.30 (x=288, y=60) -->
    <path d="M 45,210 Q 180,175 280,130 T 310,48" fill="none" stroke="#DC2626" stroke-width="3"/>

    <!-- Low loss point -->
    <circle cx="72" cy="200" r="5" fill="#16A34A"/>
    <text x="80" y="190" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#15803D">p=0.1 &#8594; 0.105</text>

    <!-- High loss point -->
    <circle cx="288" cy="60" r="5" fill="#DC2626"/>
    <text x="260" y="55" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#DC2626">p=0.9 &#8594; 2.303 (21.8&#215;!)</text>

    <text x="185" y="255" font-family="Courier New, monospace" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">Loss = -ln(1 - p)</text>
    <text x="185" y="270" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#991B1B" text-anchor="middle">Loss goes to 0 as p &#8594; 0; explodes to &#8734; as p &#8594; 1</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 8. SVG_CONFUSION_MATRIX_HEATMAP: 2x2 Confusion Matrix Heatmap
# ----------------------------------------------------------------------
SVG_CONFUSION_MATRIX_HEATMAP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 380" width="100%">
  <rect width="860" height="380" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">THE CONFUSION MATRIX: 100-PATIENT MEDICAL SCREENING EXAMPLE</text>

  <!-- Left 2x2 Matrix Grid -->
  <g transform="translate(60, 65)">
    <!-- Column Headers -->
    <rect x="140" y="0" width="160" height="35" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="220" y="22" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">PREDICTED SICK (1)</text>

    <rect x="310" y="0" width="160" height="35" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="390" y="22" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">PREDICTED HEALTHY (0)</text>

    <!-- Row Headers -->
    <rect x="0" y="45" width="130" height="100" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="65" y="90" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">ACTUAL SICK</text>
    <text x="65" y="110" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">(20 Patients)</text>

    <rect x="0" y="155" width="130" height="100" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="65" y="200" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">ACTUAL HEALTHY</text>
    <text x="65" y="220" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">(80 Patients)</text>

    <!-- Cell Top-Left: True Positive (TP) -->
    <rect x="140" y="45" width="160" height="100" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="2"/>
    <text x="220" y="75" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#166534" text-anchor="middle">TRUE POSITIVE (TP)</text>
    <text x="220" y="115" font-family="Courier New, monospace" font-size="32" font-weight="800" fill="#15803D" text-anchor="middle">18</text>
    <text x="220" y="135" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#14532D" text-anchor="middle">Sick correctly diagnosed</text>

    <!-- Cell Top-Right: False Negative (FN) -->
    <rect x="310" y="45" width="160" height="100" rx="8" fill="#FEE2E2" stroke="#DC2626" stroke-width="2"/>
    <text x="390" y="75" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#991B1B" text-anchor="middle">FALSE NEGATIVE (FN)</text>
    <text x="390" y="115" font-family="Courier New, monospace" font-size="32" font-weight="800" fill="#B91C1C" text-anchor="middle">2</text>
    <text x="390" y="135" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">DANGEROUS: Missed disease!</text>

    <!-- Cell Bottom-Left: False Positive (FP) -->
    <rect x="140" y="155" width="160" height="100" rx="8" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>
    <text x="220" y="185" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#92400E" text-anchor="middle">FALSE POSITIVE (FP)</text>
    <text x="220" y="225" font-family="Courier New, monospace" font-size="32" font-weight="800" fill="#B45309" text-anchor="middle">6</text>
    <text x="220" y="245" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#78350F" text-anchor="middle">False alarm: healthy called sick</text>

    <!-- Cell Bottom-Right: True Negative (TN) -->
    <rect x="310" y="155" width="160" height="100" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="2"/>
    <text x="390" y="185" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#166534" text-anchor="middle">TRUE NEGATIVE (TN)</text>
    <text x="390" y="225" font-family="Courier New, monospace" font-size="32" font-weight="800" fill="#16A34A" text-anchor="middle">74</text>
    <text x="390" y="245" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#14532D" text-anchor="middle">Healthy correctly cleared</text>
  </g>

  <!-- Right: Metrics Scoreboard -->
  <g transform="translate(560, 65)">
    <rect width="250" height="255" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="125" y="25" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Calculated Metrics (N=100)</text>

    <!-- Accuracy -->
    <rect x="15" y="42" width="220" height="42" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <text x="25" y="62" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#334155">Accuracy: (18+74)/100</text>
    <text x="225" y="68" font-family="Courier New, monospace" font-size="15" font-weight="700" fill="#4F46E5" text-anchor="end">92.0%</text>

    <!-- Precision -->
    <rect x="15" y="92" width="220" height="42" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <text x="25" y="112" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#334155">Precision: 18/(18+6)</text>
    <text x="225" y="118" font-family="Courier New, monospace" font-size="15" font-weight="700" fill="#0284C7" text-anchor="end">75.0%</text>

    <!-- Recall -->
    <rect x="15" y="142" width="220" height="42" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <text x="25" y="162" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#334155">Recall (TPR): 18/(18+2)</text>
    <text x="225" y="168" font-family="Courier New, monospace" font-size="15" font-weight="700" fill="#16A34A" text-anchor="end">90.0%</text>

    <!-- F1 Score -->
    <rect x="15" y="192" width="220" height="48" rx="6" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="25" y="214" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#4338CA">F1-Score (Harmonic Mean):</text>
    <text x="225" y="226" font-family="Courier New, monospace" font-size="16" font-weight="800" fill="#4F46E5" text-anchor="end">81.82%</text>
  </g>

  <text x="430" y="360" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Total Samples = TP + TN + FP + FN = 100. False Negatives carry the highest human cost in medical diagnosis.</text>
</svg>"""

# ----------------------------------------------------------------------
# 9. SVG_PRECISION_RECALL_TRADEOFF: Precision-Recall Trade-off Curves
# ----------------------------------------------------------------------
SVG_PRECISION_RECALL_TRADEOFF = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">THE INVERSE PRECISION-RECALL TRADE-OFF ACROSS THRESHOLDS</text>

  <g transform="translate(90, 55)">
    <rect width="680" height="240" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Axes -->
    <line x1="60" y1="200" x2="630" y2="200" stroke="#0F172A" stroke-width="1.5"/>
    <line x1="60" y1="30" x2="60" y2="200" stroke="#0F172A" stroke-width="1.5"/>

    <text x="60" y="220" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">0.0</text>
    <text x="345" y="220" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">0.5</text>
    <text x="630" y="220" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">1.0</text>
    <text x="345" y="238" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#334155" text-anchor="middle">Classification Threshold (&#964;) &#8594;</text>

    <!-- Y Ticks -->
    <text x="50" y="204" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="end">0.0</text>
    <text x="50" y="115" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="end">0.5</text>
    <text x="50" y="35" font-family="Courier New, monospace" font-size="10" fill="#64748B" text-anchor="end">1.0</text>

    <!-- Recall Curve (Decreasing as threshold increases) -->
    <!-- Starts at 1.0 (threshold 0 -> recall 100%), drops towards 0 -->
    <path d="M 60,35 C 200,38 350,70 500,140 C 560,170 600,195 630,200" fill="none" stroke="#16A34A" stroke-width="3"/>
    <text x="180" y="55" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#166534">Recall (True Positive Rate)</text>

    <!-- Precision Curve (Increasing as threshold increases) -->
    <!-- Starts low, climbs towards 1.0 -->
    <path d="M 60,180 C 180,170 300,130 450,70 C 530,42 580,36 630,35" fill="none" stroke="#0284C7" stroke-width="3"/>
    <text x="530" y="55" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#0369A1">Precision</text>

    <!-- F1 Harmonic Balance Point -->
    <circle cx="380" cy="98" r="6" fill="#4F46E5"/>
    <line x1="380" y1="30" x2="380" y2="200" stroke="#4F46E5" stroke-width="1.5" stroke-dasharray="3,3"/>
    <rect x="320" y="110" width="120" height="38" rx="4" fill="#EEF2FF" stroke="#4F46E5" stroke-width="1"/>
    <text x="380" y="126" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" fill="#4338CA" text-anchor="middle">Optimal F1 Balance</text>
    <text x="380" y="140" font-family="Courier New, monospace" font-size="10" font-weight="700" fill="#312E81" text-anchor="middle">Threshold &#8776; 0.52</text>
  </g>

  <text x="430" y="340" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#475569" text-anchor="middle">You cannot simultaneously maximize Precision and Recall &#8226; Raising threshold increases Precision but harms Recall.</text>
</svg>"""

# ----------------------------------------------------------------------
# 10. SVG_ROC_AUC_CURVE: ROC Curve & Area Under Curve (AUC)
# ----------------------------------------------------------------------
SVG_ROC_AUC_CURVE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 380" width="100%">
  <rect width="860" height="380" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">RECEIVER OPERATING CHARACTERISTIC (ROC) &amp; AREA UNDER CURVE (AUC)</text>

  <g transform="translate(80, 55)">
    <!-- Plot Box -->
    <rect width="450" height="260" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Shaded AUC Area -->
    <path d="M 0,260 L 0,15 C 60,12 180,10 450,0 L 450,260 Z" fill="#EEF2FF" opacity="0.6"/>

    <!-- Diagonal No-Skill Baseline (AUC = 0.50) -->
    <line x1="0" y1="260" x2="450" y2="0" stroke="#DC2626" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="260" y="145" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#DC2626" transform="rotate(-30 260 145)">Random Guessing (AUC = 0.50)</text>

    <!-- Logistic Regression ROC Curve -->
    <path d="M 0,260 L 0,20 C 15,15 40,8 80,5 C 160,2 300,1 450,0" fill="none" stroke="#4F46E5" stroke-width="3.5"/>

    <!-- Axes -->
    <line x1="0" y1="260" x2="450" y2="260" stroke="#0F172A" stroke-width="1.5"/>
    <line x1="0" y1="0" x2="0" y2="260" stroke="#0F172A" stroke-width="1.5"/>

    <text x="0" y="280" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">0.0</text>
    <text x="225" y="280" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">0.5</text>
    <text x="450" y="280" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">1.0</text>
    <text x="225" y="300" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#0F172A" text-anchor="middle">False Positive Rate (FPR = 1 - Specificity) &#8594;</text>

    <text x="-12" y="265" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">0.0</text>
    <text x="-12" y="135" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">0.5</text>
    <text x="-12" y="10" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">1.0</text>
    <text x="-35" y="130" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#0F172A" text-anchor="middle" transform="rotate(-90 -35 130)">True Positive Rate (Recall) &#8594;</text>
  </g>

  <!-- Right: Interpretation Card -->
  <g transform="translate(560, 55)">
    <rect width="250" height="260" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="125" y="25" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">AUC Benchmark Guide</text>

    <rect x="15" y="40" width="220" height="42" rx="6" fill="#DCFCE7" stroke="#16A34A" stroke-width="1"/>
    <text x="25" y="60" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#15803D">0.90 - 1.00</text>
    <text x="220" y="60" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#15803D" text-anchor="end">Outstanding</text>
    <text x="25" y="75" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#166534">Our Lab Test Model: 1.0000</text>

    <rect x="15" y="90" width="220" height="38" rx="6" fill="#E0F2FE" stroke="#0284C7" stroke-width="1"/>
    <text x="25" y="112" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#0369A1">0.80 - 0.90</text>
    <text x="220" y="112" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#0369A1" text-anchor="end">Good / Strong</text>

    <rect x="15" y="136" width="220" height="38" rx="6" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
    <text x="25" y="158" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#92400E">0.70 - 0.80</text>
    <text x="220" y="158" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#92400E" text-anchor="end">Fair</text>

    <rect x="15" y="182" width="220" height="38" rx="6" fill="#FEE2E2" stroke="#DC2626" stroke-width="1"/>
    <text x="25" y="204" font-family="Courier New, monospace" font-size="13" font-weight="700" fill="#B91C1C">0.50</text>
    <text x="220" y="204" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="end">Worthless (Coin Flip)</text>

    <text x="125" y="242" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">AUC evaluates ranking discrimination</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 11. SVG_CLASS_IMBALANCE_ILLUSION: The 95% Accuracy Trap
# ----------------------------------------------------------------------
SVG_CLASS_IMBALANCE_ILLUSION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">THE CLASS IMBALANCE ILLUSION: WHY ACCURACY DECEIVES</text>

  <!-- Left: Imbalanced Data Composition -->
  <g transform="translate(50, 60)">
    <rect width="350" height="260" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="175" y="25" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">100 Credit Card Transactions</text>

    <!-- Visual Stacked Bar -->
    <rect x="35" y="50" width="280" height="40" rx="6" fill="#0284C7"/>
    <rect x="301" y="50" width="14" height="40" rx="6" fill="#DC2626"/>

    <text x="160" y="75" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">95 Legitimate Transactions (95%)</text>
    <text x="308" y="75" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">5%</text>

    <!-- Legend -->
    <rect x="35" y="110" width="280" height="130" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <circle cx="55" cy="135" r="7" fill="#0284C7"/>
    <text x="75" y="140" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" fill="#334155">Class 0 (Normal): 95 transactions</text>

    <circle cx="55" cy="170" r="7" fill="#DC2626"/>
    <text x="75" y="175" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#B91C1C">Class 1 (Fraud): 5 transactions</text>

    <text x="175" y="215" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Severely skewed 19:1 baseline ratio</text>
  </g>

  <!-- Right: Naive Dummy Classifier Breakdown -->
  <g transform="translate(440, 60)">
    <rect width="370" height="260" rx="10" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="185" y="25" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#DC2626" text-anchor="middle">The "Predict Always Normal" Model</text>

    <!-- Accuracy Box -->
    <rect x="25" y="45" width="320" height="50" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="35" y="75" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#334155">Reported Accuracy:</text>
    <text x="330" y="78" font-family="Courier New, monospace" font-size="22" font-weight="800" fill="#16A34A" text-anchor="end">95.0% (HIGH!)</text>

    <!-- Fraud Caught Box -->
    <rect x="25" y="105" width="320" height="50" rx="6" fill="#FEE2E2" stroke="#DC2626" stroke-width="1"/>
    <text x="35" y="135" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#991B1B">Fraud Recall (Caught):</text>
    <text x="330" y="138" font-family="Courier New, monospace" font-size="22" font-weight="800" fill="#DC2626" text-anchor="end">0.0% (CATASTROPHIC)</text>

    <text x="185" y="185" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">The model learned nothing but scores 95%!</text>
    <text x="185" y="205" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#7F1D1D" text-anchor="middle">All 5 fraud cases escaped undetected.</text>
    <text x="185" y="235" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#16A34A" text-anchor="middle">Remedy: Use Recall, Precision, PR-AUC, and class_weight</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 12. SVG_REGULARIZATION_L2_C: Regularization Strength & Weight Shrinkage
# ----------------------------------------------------------------------
SVG_REGULARIZATION_L2_C = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">L2 REGULARIZATION &amp; SCIKIT-LEARN'S C PARAMETER: SHRINKING WEIGHTS</text>

  <!-- Left Card: C = 0.01 (Heavy Penalty) -->
  <g transform="translate(40, 60)">
    <rect width="240" height="260" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <rect x="20" y="15" width="200" height="30" rx="6" fill="#16A34A"/>
    <text x="120" y="35" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">C = 0.01 (HEAVY L2)</text>

    <text x="120" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#166534" text-anchor="middle">Inverse Penalty: &#955; = 100</text>
    
    <!-- Weight Bar Visual -->
    <rect x="40" y="90" width="160" height="25" rx="4" fill="#DCFCE7" stroke="#16A34A" stroke-width="1"/>
    <rect x="40" y="90" width="25" height="25" rx="4" fill="#16A34A"/>
    <text x="120" y="135" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#166534" text-anchor="middle">||w|| = 0.4443</text>

    <rect x="20" y="155" width="200" height="80" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="120" y="175" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#15803D" text-anchor="middle">Strongest Shrinkage</text>
    <text x="120" y="195" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#166534" text-anchor="middle">&#8226; Heavily penalizes large weights</text>
    <text x="120" y="215" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#166534" text-anchor="middle">&#8226; Prevents extreme overfitting</text>
  </g>

  <!-- Middle Card: C = 1.0 (Default) -->
  <g transform="translate(310, 60)">
    <rect width="240" height="260" rx="10" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
    <rect x="20" y="15" width="200" height="30" rx="6" fill="#4F46E5"/>
    <text x="120" y="35" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">C = 1.00 (BALANCED)</text>

    <text x="120" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#4338CA" text-anchor="middle">Scikit-Learn Default: &#955; = 1</text>

    <!-- Weight Bar Visual -->
    <rect x="40" y="90" width="160" height="25" rx="4" fill="#E0E7FF" stroke="#4F46E5" stroke-width="1"/>
    <rect x="40" y="90" width="85" height="25" rx="4" fill="#4F46E5"/>
    <text x="120" y="135" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#4338CA" text-anchor="middle">||w|| = 3.8803</text>

    <rect x="20" y="155" width="200" height="80" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="120" y="175" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#4F46E5" text-anchor="middle">Balanced Equilibrium</text>
    <text x="120" y="195" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#334155" text-anchor="middle">&#8226; Good fit to training loss</text>
    <text x="120" y="215" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#334155" text-anchor="middle">&#8226; Moderate weight control</text>
  </g>

  <!-- Right Card: C = 100.0 (Weak Penalty) -->
  <g transform="translate(580, 60)">
    <rect width="240" height="260" rx="10" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
    <rect x="20" y="15" width="200" height="30" rx="6" fill="#D97706"/>
    <text x="120" y="35" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">C = 100.0 (WEAK L2)</text>

    <text x="120" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#92400E" text-anchor="middle">Negligible Penalty: &#955; = 0.01</text>

    <!-- Weight Bar Visual -->
    <rect x="40" y="90" width="160" height="25" rx="4" fill="#FEF9C3" stroke="#D97706" stroke-width="1"/>
    <rect x="40" y="90" width="155" height="25" rx="4" fill="#D97706"/>
    <text x="120" y="135" font-family="Courier New, monospace" font-size="12" font-weight="700" fill="#92400E" text-anchor="middle">||w|| = 7.7703</text>

    <rect x="20" y="155" width="200" height="80" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="120" y="175" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#92400E" text-anchor="middle">Unconstrained Optimization</text>
    <text x="120" y="195" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#78350F" text-anchor="middle">&#8226; Weights can grow very large</text>
    <text x="120" y="215" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#78350F" text-anchor="middle">&#8226; Vulnerable to noise &amp; outliers</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 13. SVG_PROBABILITY_CALIBRATION: Reliability Diagram
# ----------------------------------------------------------------------
SVG_PROBABILITY_CALIBRATION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 360" width="100%">
  <rect width="860" height="360" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="430" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">PROBABILITY CALIBRATION (RELIABILITY DIAGRAM): DISCRIMINATION VS. REALITY</text>

  <g transform="translate(80, 55)">
    <!-- Diagram Canvas -->
    <rect width="450" height="250" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Perfect Calibration Diagonal -->
    <line x1="0" y1="250" x2="450" y2="0" stroke="#16A34A" stroke-width="2.5" stroke-dasharray="4,4"/>
    <text x="260" y="145" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#15803D" transform="rotate(-30 260 145)">Perfect Calibration (x = y)</text>

    <!-- Overconfident Sigmoidal Curve (Typical uncalibrated complex model) -->
    <path d="M 0,250 C 150,240 220,180 300,50 L 450,0" fill="none" stroke="#DC2626" stroke-width="2.5"/>
    <text x="320" y="70" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#DC2626">Overconfident Model</text>

    <!-- Well-calibrated Logistic Regression line -->
    <path d="M 0,250 L 90,205 L 180,155 L 270,102 L 360,52 L 450,0" fill="none" stroke="#4F46E5" stroke-width="3"/>
    <circle cx="90" cy="205" r="4" fill="#4F46E5"/>
    <circle cx="180" cy="155" r="4" fill="#4F46E5"/>
    <circle cx="270" cy="102" r="4" fill="#4F46E5"/>
    <circle cx="360" cy="52" r="4" fill="#4F46E5"/>

    <!-- Axes -->
    <line x1="0" y1="250" x2="450" y2="250" stroke="#0F172A" stroke-width="1.5"/>
    <line x1="0" y1="0" x2="0" y2="250" stroke="#0F172A" stroke-width="1.5"/>

    <text x="0" y="270" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">0.0</text>
    <text x="225" y="270" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">0.5</text>
    <text x="450" y="270" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="middle">1.0</text>
    <text x="225" y="290" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle">Mean Predicted Probability in Bin &#8594;</text>

    <text x="-12" y="255" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">0.0</text>
    <text x="-12" y="130" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">0.5</text>
    <text x="-12" y="10" font-family="Courier New, monospace" font-size="11" fill="#64748B" text-anchor="end">1.0</text>
    <text x="-35" y="125" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle" transform="rotate(-90 -35 125)">Observed Fraction of Positives &#8594;</text>
  </g>

  <!-- Right: Meaning Card -->
  <g transform="translate(560, 55)">
    <rect width="250" height="250" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="125" y="25" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">What Does 80% Mean?</text>

    <rect x="15" y="45" width="220" height="70" rx="6" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="25" y="68" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#4338CA">Calibrated Meaning:</text>
    <text x="25" y="88" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#334155">Out of 100 predictions rated 80%,</text>
    <text x="25" y="103" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-weight="700" fill="#15803D">exactly 80 should truly be Class 1.</text>

    <rect x="15" y="130" width="220" height="95" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="25" y="152" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Logistic Regression Advantage:</text>
    <text x="25" y="172" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#64748B">&#8226; Directly minimizes log-loss</text>
    <text x="25" y="190" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#64748B">&#8226; Naturally well-calibrated</text>
    <text x="25" y="208" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" fill="#64748B">&#8226; Unlike naive Bayes / boosted trees</text>
  </g>
</svg>"""

# ----------------------------------------------------------------------
# 14. SVG_LAB_EVALUATION_SCORECARD: Verified Practical Lab Results
# ----------------------------------------------------------------------
SVG_LAB_EVALUATION_SCORECARD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 340" width="100%">
  <rect width="880" height="340" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="440" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0F172A" text-anchor="middle">PYTHON PRACTICAL LAB EVALUATION SCORECARD (STUDENT EXAM PASS/FAIL)</text>

  <!-- Left: Test Confusion Matrix -->
  <g transform="translate(45, 60)">
    <rect width="360" height="250" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="180" y="25" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Test Confusion Matrix (N = 40)</text>

    <!-- 2x2 Grid -->
    <rect x="50" y="50" width="125" height="75" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="112" y="75" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">True Neg (TN)</text>
    <text x="112" y="108" font-family="Courier New, monospace" font-size="24" font-weight="800" fill="#16A34A" text-anchor="middle">16</text>

    <rect x="185" y="50" width="125" height="75" rx="6" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
    <text x="247" y="75" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#92400E" text-anchor="middle">False Pos (FP)</text>
    <text x="247" y="108" font-family="Courier New, monospace" font-size="24" font-weight="800" fill="#D97706" text-anchor="middle">0</text>

    <rect x="50" y="135" width="125" height="75" rx="6" fill="#FEE2E2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="112" y="160" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">False Neg (FN)</text>
    <text x="112" y="193" font-family="Courier New, monospace" font-size="24" font-weight="800" fill="#DC2626" text-anchor="middle">2</text>

    <rect x="185" y="135" width="125" height="75" rx="6" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5"/>
    <text x="247" y="160" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">True Pos (TP)</text>
    <text x="247" y="193" font-family="Courier New, monospace" font-size="24" font-weight="800" fill="#15803D" text-anchor="middle">22</text>

    <text x="180" y="232" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">40 Test Students (16 Actual Fail, 24 Actual Pass)</text>
  </g>

  <!-- Right: Metrics Table -->
  <g transform="translate(435, 60)">
    <rect width="400" height="250" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="200" y="25" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Test Evaluation Summary</text>

    <g transform="translate(20, 42)">
      <!-- Metric 1: Accuracy -->
      <rect x="0" y="0" width="360" height="34" rx="4" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="15" y="22" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#334155">Test Accuracy: (16+22) / 40</text>
      <text x="345" y="22" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#4F46E5" text-anchor="end">95.00%</text>

      <!-- Metric 2: Precision -->
      <rect x="0" y="40" width="360" height="34" rx="4" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="15" y="62" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#334155">Test Precision: 22 / (22+0)</text>
      <text x="345" y="62" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#0284C7" text-anchor="end">100.00%</text>

      <!-- Metric 3: Recall -->
      <rect x="0" y="80" width="360" height="34" rx="4" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="15" y="102" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#334155">Test Recall: 22 / (22+2)</text>
      <text x="345" y="102" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#16A34A" text-anchor="end">91.67%</text>

      <!-- Metric 4: F1-Score -->
      <rect x="0" y="120" width="360" height="34" rx="4" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="15" y="142" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600" fill="#334155">Test F1-Score:</text>
      <text x="345" y="142" font-family="Courier New, monospace" font-size="14" font-weight="700" fill="#4F46E5" text-anchor="end">95.65%</text>

      <!-- Metric 5: ROC AUC -->
      <rect x="0" y="160" width="360" height="38" rx="4" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
      <text x="15" y="184" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="700" fill="#4338CA">Test ROC AUC (Ranking):</text>
      <text x="345" y="184" font-family="Courier New, monospace" font-size="15" font-weight="800" fill="#4F46E5" text-anchor="end">1.0000 (100%)</text>
    </g>
  </g>
</svg>"""

ALL_SVGS = [
    ("SVG_LOGREG_HERO", SVG_LOGREG_HERO),
    ("SVG_LINEAR_VS_SIGMOID", SVG_LINEAR_VS_SIGMOID),
    ("SVG_SIGMOID_CURVE", SVG_SIGMOID_CURVE),
    ("SVG_ODDS_PROB_MAPPING", SVG_ODDS_PROB_MAPPING),
    ("SVG_THRESHOLD_VARIATION", SVG_THRESHOLD_VARIATION),
    ("SVG_DECISION_BOUNDARY_1D_2D", SVG_DECISION_BOUNDARY_1D_2D),
    ("SVG_LOG_LOSS_CURVES", SVG_LOG_LOSS_CURVES),
    ("SVG_CONFUSION_MATRIX_HEATMAP", SVG_CONFUSION_MATRIX_HEATMAP),
    ("SVG_PRECISION_RECALL_TRADEOFF", SVG_PRECISION_RECALL_TRADEOFF),
    ("SVG_ROC_AUC_CURVE", SVG_ROC_AUC_CURVE),
    ("SVG_CLASS_IMBALANCE_ILLUSION", SVG_CLASS_IMBALANCE_ILLUSION),
    ("SVG_REGULARIZATION_L2_C", SVG_REGULARIZATION_L2_C),
    ("SVG_PROBABILITY_CALIBRATION", SVG_PROBABILITY_CALIBRATION),
    ("SVG_LAB_EVALUATION_SCORECARD", SVG_LAB_EVALUATION_SCORECARD)
]

if __name__ == '__main__':
    print(f"Validating {len(ALL_SVGS)} Topic 10 SVGs for XML compliance...")
    for name, svg_str in ALL_SVGS:
        try:
            ET.fromstring(svg_str)
            print(f"  [XML PASS] {name}")
        except Exception as e:
            print(f"  [XML FAIL] {name}: {e}")
            raise
    print("All Topic 10 SVGs validated successfully!")
