# Topic 23 SVGs
# 20 High-Quality, Accessible, Light Mode Vector SVG Diagrams
# Color Palette: Teal (#0D9488), Deep Teal (#0F766E), Light Mint (#F0FDFA), Cyan/Border (#99F6E4), Slate (#0F172A), Soft Emerald (#10B981), Amber (#F59E0B), Red/Coral (#EF4444)

SVG_MAP = {}

# 1. WORKFLOW
SVG_MAP["__SVG_WORKFLOW__"] = """
<svg viewBox="0 0 860 210" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="wfGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0D9488" />
      <stop offset="100%" stop-color="#0F766E" />
    </linearGradient>
    <filter id="shadowLight" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Step 1: Raw Data -->
  <g transform="translate(10, 30)" filter="url(#shadowLight)">
    <rect width="100" height="120" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="2"/>
    <rect width="100" height="28" rx="10" fill="#F0FDFA"/>
    <text x="50" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">STEP 1</text>
    <text x="50" y="55" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Raw Data</text>
    <text x="50" y="75" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">CSVs, APIs, SQL</text>
    <text x="50" y="92" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Strings &amp; NaNs</text>
    <text x="50" y="125" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">📁</text>
  </g>
  <path d="M 115 90 L 130 90" stroke="#0D9488" stroke-width="2" marker-end="url(#arrow)" fill="none"/>

  <!-- Step 2: Understand -->
  <g transform="translate(130, 30)" filter="url(#shadowLight)">
    <rect width="100" height="120" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="2"/>
    <rect width="100" height="28" rx="10" fill="#F0FDFA"/>
    <text x="50" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">STEP 2</text>
    <text x="50" y="55" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Understand</text>
    <text x="50" y="75" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Types &amp; Distr.</text>
    <text x="50" y="92" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Domain Logic</text>
    <text x="50" y="125" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🔍</text>
  </g>
  <path d="M 235 90 L 250 90" stroke="#0D9488" stroke-width="2" fill="none"/>

  <!-- Step 3: Clean & Impute -->
  <g transform="translate(250, 30)" filter="url(#shadowLight)">
    <rect width="100" height="120" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="2"/>
    <rect width="100" height="28" rx="10" fill="#F0FDFA"/>
    <text x="50" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">STEP 3</text>
    <text x="50" y="55" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Clean &amp; Impute</text>
    <text x="50" y="75" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Fill Missing</text>
    <text x="50" y="92" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Drop Bad IDs</text>
    <text x="50" y="125" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🧹</text>
  </g>
  <path d="M 355 90 L 370 90" stroke="#0D9488" stroke-width="2" fill="none"/>

  <!-- Step 4: Engineer Features -->
  <g transform="translate(370, 30)" filter="url(#shadowLight)">
    <rect width="105" height="120" rx="10" fill="#FFFFFF" stroke="#0D9488" stroke-width="2.5"/>
    <rect width="105" height="28" rx="10" fill="#CCFBF1"/>
    <text x="52" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#115E59" text-anchor="middle">STEP 4 • CORE</text>
    <text x="52" y="55" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0D9488" text-anchor="middle">Feature Eng.</text>
    <text x="52" y="75" font-family="system-ui, sans-serif" font-size="10" fill="#334155" text-anchor="middle">Ratios, DTI, Age</text>
    <text x="52" y="92" font-family="system-ui, sans-serif" font-size="10" fill="#334155" text-anchor="middle">Interactions</text>
    <text x="52" y="125" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">⚡</text>
  </g>
  <path d="M 480 90 L 495 90" stroke="#0D9488" stroke-width="2" fill="none"/>

  <!-- Step 5: Encode & Scale -->
  <g transform="translate(495, 30)" filter="url(#shadowLight)">
    <rect width="105" height="120" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="2"/>
    <rect width="105" height="28" rx="10" fill="#F0FDFA"/>
    <text x="52" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">STEP 5</text>
    <text x="52" y="55" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Encode &amp; Scale</text>
    <text x="52" y="75" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">OneHot, Ordinal</text>
    <text x="52" y="92" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">StandardScaler</text>
    <text x="52" y="125" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">⚖️</text>
  </g>
  <path d="M 605 90 L 620 90" stroke="#0D9488" stroke-width="2" fill="none"/>

  <!-- Step 6: ML Pipeline -->
  <g transform="translate(620, 30)" filter="url(#shadowLight)">
    <rect width="105" height="120" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="2"/>
    <rect width="105" height="28" rx="10" fill="#F0FDFA"/>
    <text x="52" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">STEP 6</text>
    <text x="52" y="55" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Train Pipeline</text>
    <text x="52" y="75" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">ColumnTransformer</text>
    <text x="52" y="92" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">+ Estimator</text>
    <text x="52" y="125" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🔄</text>
  </g>
  <path d="M 730 90 L 745 90" stroke="#0D9488" stroke-width="2" fill="none"/>

  <!-- Step 7: Prediction -->
  <g transform="translate(745, 30)" filter="url(#shadowLight)">
    <rect width="100" height="120" rx="10" fill="#F0FDFA" stroke="#0D9488" stroke-width="2"/>
    <rect width="100" height="28" rx="10" fill="#0D9488"/>
    <text x="50" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">STEP 7</text>
    <text x="50" y="55" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E" text-anchor="middle">Inference</text>
    <text x="50" y="75" font-family="system-ui, sans-serif" font-size="10" fill="#134E4A" text-anchor="middle">Robust &amp; Fair</text>
    <text x="50" y="92" font-family="system-ui, sans-serif" font-size="10" fill="#134E4A" text-anchor="middle">Zero Leakage</text>
    <text x="50" y="125" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🎯</text>
  </g>

  <!-- Flow caption -->
  <text x="430" y="190" font-family="system-ui, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Every transformation step is systematically encapsulated inside an immutable scikit-learn Pipeline.</text>
</svg>
"""

# 2. FEATURE TYPES CLASSIFICATION CHART
SVG_MAP["__SVG_FEATURE_TYPES__"] = """
<svg viewBox="0 0 820 320" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="fShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <!-- Root Node -->
  <g transform="translate(310, 15)" filter="url(#fShadow)">
    <rect width="200" height="46" rx="8" fill="#0D9488" stroke="#0F766E" stroke-width="2"/>
    <text x="100" y="28" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">Data Feature Types</text>
  </g>

  <!-- Connecting Tree Lines -->
  <path d="M 410 61 L 410 85 M 160 85 L 660 85 M 160 85 L 160 105 M 410 85 L 410 105 M 660 85 L 660 105" stroke="#99F6E4" stroke-width="2.5" fill="none"/>

  <!-- Category 1: Numerical -->
  <g transform="translate(60, 105)" filter="url(#fShadow)">
    <rect width="200" height="195" rx="10" fill="#FFFFFF" stroke="#0D9488" stroke-width="1.5"/>
    <rect width="200" height="32" rx="10" fill="#F0FDFA"/>
    <text x="100" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E" text-anchor="middle">1. Numerical Features</text>
    
    <text x="16" y="55" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Continuous (Real numbers):</text>
    <text x="16" y="73" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• Income: $64,250.80</text>
    <text x="16" y="90" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• Temperature: 98.6°F</text>
    
    <text x="16" y="118" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Discrete (Integers / Counts):</text>
    <text x="16" y="136" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• Bedrooms: 3, Bathrooms: 2</text>
    <text x="16" y="153" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• Website visits: 14</text>

    <rect x="12" y="165" width="176" height="20" rx="4" fill="#CCFBF1"/>
    <text x="100" y="179" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" fill="#115E59" text-anchor="middle">Action: Scale / Standardize</text>
  </g>

  <!-- Category 2: Categorical -->
  <g transform="translate(310, 105)" filter="url(#fShadow)">
    <rect width="200" height="195" rx="10" fill="#FFFFFF" stroke="#0D9488" stroke-width="1.5"/>
    <rect width="200" height="32" rx="10" fill="#F0FDFA"/>
    <text x="100" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E" text-anchor="middle">2. Categorical Features</text>
    
    <text x="16" y="55" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Nominal (No inherent order):</text>
    <text x="16" y="73" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• City: Tokyo, Paris, London</text>
    <text x="16" y="90" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• Color: Red, Blue, Green</text>
    
    <text x="16" y="118" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Ordinal (Ordered hierarchy):</text>
    <text x="16" y="136" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• Education: HS &lt; BS &lt; MS &lt; PhD</text>
    <text x="16" y="153" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• Rating: Low &lt; Med &lt; High</text>

    <rect x="12" y="165" width="176" height="20" rx="4" fill="#CCFBF1"/>
    <text x="100" y="179" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" fill="#115E59" text-anchor="middle">Action: One-Hot / Ordinal Encode</text>
  </g>

  <!-- Category 3: Specialized & Identifiers -->
  <g transform="translate(560, 105)" filter="url(#fShadow)">
    <rect width="200" height="195" rx="10" fill="#FFFFFF" stroke="#0D9488" stroke-width="1.5"/>
    <rect width="200" height="32" rx="10" fill="#F0FDFA"/>
    <text x="100" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E" text-anchor="middle">3. Specialized &amp; IDs</text>
    
    <text x="16" y="55" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Temporal &amp; Text:</text>
    <text x="16" y="73" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• Date: 2023-10-24 (Extract!)</text>
    <text x="16" y="90" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• Free text: Customer notes</text>
    
    <text x="16" y="118" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#EF4444">Identifiers (Never Feed!):</text>
    <text x="16" y="136" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• UserID: #892819 (Spurious!)</text>
    <text x="16" y="153" font-family="system-ui, sans-serif" font-size="11.5" fill="#475569">• SSN / Transaction ID</text>

    <rect x="12" y="165" width="176" height="20" rx="4" fill="#FEE2E2"/>
    <text x="100" y="179" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#B91C1C" text-anchor="middle">Action: Extract or Drop IDs</text>
  </g>
</svg>
"""

# 3. RAW DATA VS MODEL-READY DATA
SVG_MAP["__SVG_RAW_VS_READY__"] = """
<svg viewBox="0 0 820 250" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="rShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Left: Raw Messy Data -->
  <g transform="translate(20, 20)" filter="url(#rShadow)">
    <rect width="340" height="205" rx="10" fill="#FFFFFF" stroke="#EF4444" stroke-width="1.5"/>
    <rect width="340" height="30" rx="10" fill="#FEF2F2"/>
    <text x="170" y="20" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#B91C1C" text-anchor="middle">❌ RAW DATA (Unusable by ML)</text>
    
    <!-- Table Mock -->
    <rect x="15" y="45" width="310" height="25" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="30" y="62" font-family="monospace" font-size="11" font-weight="700" fill="#334155">Age</text>
    <text x="90" y="62" font-family="monospace" font-size="11" font-weight="700" fill="#334155">Income</text>
    <text x="170" y="62" font-family="monospace" font-size="11" font-weight="700" fill="#334155">City</text>
    <text x="245" y="62" font-family="monospace" font-size="11" font-weight="700" fill="#334155">Education</text>

    <rect x="15" y="70" width="310" height="25" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="30" y="87" font-family="monospace" font-size="11" fill="#0F172A">35</text>
    <text x="90" y="87" font-family="monospace" font-size="11" fill="#EF4444" font-weight="700">NaN</text>
    <text x="170" y="87" font-family="monospace" font-size="11" fill="#0F172A">"Tokyo"</text>
    <text x="245" y="87" font-family="monospace" font-size="11" fill="#0F172A">"Master"</text>

    <rect x="15" y="95" width="310" height="25" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="30" y="112" font-family="monospace" font-size="11" fill="#0F172A">28</text>
    <text x="90" y="112" font-family="monospace" font-size="11" fill="#0F172A">$48,000</text>
    <text x="170" y="112" font-family="monospace" font-size="11" fill="#0F172A">"Paris"</text>
    <text x="245" y="112" font-family="monospace" font-size="11" fill="#0F172A">"Bachelor"</text>

    <rect x="15" y="120" width="310" height="25" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="30" y="137" font-family="monospace" font-size="11" fill="#0F172A">52</text>
    <text x="90" y="137" font-family="monospace" font-size="11" fill="#0F172A">$125,000</text>
    <text x="170" y="137" font-family="monospace" font-size="11" fill="#EF4444" font-weight="700">NaN</text>
    <text x="245" y="137" font-family="monospace" font-size="11" fill="#0F172A">"PhD"</text>

    <text x="170" y="172" font-family="system-ui, sans-serif" font-size="11" fill="#B91C1C" text-anchor="middle">Contains NaNs, mixed text strings, and</text>
    <text x="170" y="188" font-family="system-ui, sans-serif" font-size="11" fill="#B91C1C" text-anchor="middle">wildly disparate numerical scales ($48k vs 28).</text>
  </g>

  <!-- Center Arrow -->
  <g transform="translate(375, 95)">
    <rect width="70" height="40" rx="6" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.5"/>
    <text x="35" y="18" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0F766E" text-anchor="middle">Pipeline</text>
    <text x="35" y="32" font-family="system-ui, sans-serif" font-size="9" fill="#115E59" text-anchor="middle">Transform ➔</text>
  </g>

  <!-- Right: Model-Ready Data -->
  <g transform="translate(460, 20)" filter="url(#rShadow)">
    <rect width="340" height="205" rx="10" fill="#FFFFFF" stroke="#10B981" stroke-width="1.5"/>
    <rect width="340" height="30" rx="10" fill="#ECFDF5"/>
    <text x="170" y="20" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#047857" text-anchor="middle">✔ MODEL-READY MATRIX (Clean Floats)</text>
    
    <!-- Table Mock -->
    <rect x="15" y="45" width="310" height="25" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="25" y="62" font-family="monospace" font-size="10" font-weight="700" fill="#334155">Age_z</text>
    <text x="75" y="62" font-family="monospace" font-size="10" font-weight="700" fill="#334155">Inc_z</text>
    <text x="130" y="62" font-family="monospace" font-size="10" font-weight="700" fill="#334155">City_TYO</text>
    <text x="195" y="62" font-family="monospace" font-size="10" font-weight="700" fill="#334155">City_PAR</text>
    <text x="260" y="62" font-family="monospace" font-size="10" font-weight="700" fill="#334155">Edu_Ord</text>

    <rect x="15" y="70" width="310" height="25" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="25" y="87" font-family="monospace" font-size="10.5" fill="#047857">-0.24</text>
    <text x="75" y="87" font-family="monospace" font-size="10.5" fill="#047857"> 0.00*</text>
    <text x="130" y="87" font-family="monospace" font-size="10.5" fill="#047857">1.0</text>
    <text x="195" y="87" font-family="monospace" font-size="10.5" fill="#047857">0.0</text>
    <text x="260" y="87" font-family="monospace" font-size="10.5" fill="#047857">2.0</text>

    <rect x="15" y="95" width="310" height="25" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="25" y="112" font-family="monospace" font-size="10.5" fill="#047857">-0.82</text>
    <text x="75" y="112" font-family="monospace" font-size="10.5" fill="#047857">-0.65</text>
    <text x="130" y="112" font-family="monospace" font-size="10.5" fill="#047857">0.0</text>
    <text x="195" y="112" font-family="monospace" font-size="10.5" fill="#047857">1.0</text>
    <text x="260" y="112" font-family="monospace" font-size="10.5" fill="#047857">1.0</text>

    <rect x="15" y="120" width="310" height="25" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="25" y="137" font-family="monospace" font-size="10.5" fill="#047857">+1.16</text>
    <text x="75" y="137" font-family="monospace" font-size="10.5" fill="#047857">+1.42</text>
    <text x="130" y="137" font-family="monospace" font-size="10.5" fill="#047857">0.0</text>
    <text x="195" y="137" font-family="monospace" font-size="10.5" fill="#047857">0.0*</text>
    <text x="260" y="137" font-family="monospace" font-size="10.5" fill="#047857">3.0</text>

    <text x="170" y="172" font-family="system-ui, sans-serif" font-size="11" fill="#047857" text-anchor="middle">Zero missing values, standardized distributions,</text>
    <text x="170" y="188" font-family="system-ui, sans-serif" font-size="11" fill="#047857" text-anchor="middle">one-hot indicators, and ordinal numeric ranks.</text>
  </g>
</svg>
"""

# 4. IMPUTATION STRATEGIES (MEAN VS MEDIAN OUTLIER EFFECT)
SVG_MAP["__SVG_IMPUTATION__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="iShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#iShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Missing Value Imputation: Outlier Sensitivity Comparison</text>
    
    <!-- Data Points on Number Line -->
    <text x="30" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#334155">Sample Incomes: [$35,000,  $42,000,  $48,000,  $52,000,  $2,500,000 (Outlier!)]</text>

    <!-- Axis line -->
    <line x1="50" y1="110" x2="730" y2="110" stroke="#CBD5E1" stroke-width="3"/>
    
    <!-- Clustered normal values -->
    <circle cx="70" cy="110" r="7" fill="#0D9488"/>
    <text x="70" y="95" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">$35k</text>

    <circle cx="90" cy="110" r="7" fill="#0D9488"/>
    <text x="90" y="130" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">$42k</text>

    <circle cx="110" cy="110" r="8" fill="#10B981" stroke="#047857" stroke-width="2"/>
    <text x="110" y="95" font-family="monospace" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">MEDIAN: $48k</text>
    <path d="M 110 98 L 110 102" stroke="#047857" stroke-width="2"/>

    <circle cx="125" cy="110" r="7" fill="#0D9488"/>
    <text x="125" y="130" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">$52k</text>

    <!-- Far Outlier -->
    <circle cx="700" cy="110" r="8" fill="#EF4444" stroke="#B91C1C" stroke-width="2"/>
    <text x="700" y="95" font-family="monospace" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">$2.5 Million (Outlier)</text>

    <!-- Mean Position distorted -->
    <circle cx="320" cy="110" r="8" fill="#F59E0B" stroke="#B45309" stroke-width="2"/>
    <text x="320" y="95" font-family="monospace" font-size="11" font-weight="700" fill="#B45309" text-anchor="middle">MEAN: $535,400</text>
    <text x="320" y="130" font-family="system-ui, sans-serif" font-size="10.5" fill="#B45309" text-anchor="middle">(Severely skewed to right!)</text>
    <path d="M 320 98 L 320 102" stroke="#B45309" stroke-width="2"/>

    <!-- Key Takeaway Banner -->
    <rect x="30" y="150" width="720" height="32" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="40" y="171" font-family="system-ui, sans-serif" font-size="11.5" fill="#334155">
      <tspan font-weight="700" fill="#047857">✔ Best Practice:</tspan> Use <tspan font-family="monospace" font-weight="600">SimpleImputer(strategy='median')</tspan> for skewed/numerical data with outliers. Use <tspan font-family="monospace" font-weight="600">strategy='most_frequent'</tspan> for categorical columns.
    </text>
  </g>
</svg>
"""

# 5. ONE-HOT ENCODING (WITH HANDLE_UNKNOWN="IGNORE")
SVG_MAP["__SVG_ONE_HOT_ENCODING__"] = """
<svg viewBox="0 0 820 230" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="oheShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#oheShadow)">
    <rect width="780" height="200" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">One-Hot Encoding Matrix Expansion (handle_unknown='ignore')</text>

    <!-- Source Column -->
    <g transform="translate(30, 48)">
      <rect width="130" height="26" fill="#E2E8F0" stroke="#CBD5E1"/>
      <text x="65" y="17" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">City (Categorical)</text>

      <rect y="26" width="130" height="24" fill="#FFFFFF" stroke="#CBD5E1"/>
      <text x="65" y="42" font-family="monospace" font-size="11" fill="#334155" text-anchor="middle">"Tokyo"</text>

      <rect y="50" width="130" height="24" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="65" y="66" font-family="monospace" font-size="11" fill="#334155" text-anchor="middle">"Paris"</text>

      <rect y="74" width="130" height="24" fill="#FFFFFF" stroke="#CBD5E1"/>
      <text x="65" y="90" font-family="monospace" font-size="11" fill="#334155" text-anchor="middle">"New York"</text>

      <rect y="98" width="130" height="24" fill="#FEF2F2" stroke="#CBD5E1"/>
      <text x="65" y="114" font-family="monospace" font-size="11" font-weight="700" fill="#EF4444" text-anchor="middle">"Sydney"* (Unseen)</text>
    </g>

    <!-- Arrow -->
    <path d="M 185 110 L 225 110" stroke="#0D9488" stroke-width="2.5" fill="none"/>
    <polygon points="225,105 235,110 225,115" fill="#0D9488"/>

    <!-- Expanded One-Hot Binary Columns -->
    <g transform="translate(250, 48)">
      <!-- Headers -->
      <rect x="0" y="0" width="105" height="26" fill="#CCFBF1" stroke="#99F6E4"/>
      <text x="52" y="17" font-family="monospace" font-size="10.5" font-weight="700" fill="#0F766E" text-anchor="middle">City_London</text>

      <rect x="105" y="0" width="105" height="26" fill="#CCFBF1" stroke="#99F6E4"/>
      <text x="157" y="17" font-family="monospace" font-size="10.5" font-weight="700" fill="#0F766E" text-anchor="middle">City_NewYork</text>

      <rect x="210" y="0" width="105" height="26" fill="#CCFBF1" stroke="#99F6E4"/>
      <text x="262" y="17" font-family="monospace" font-size="10.5" font-weight="700" fill="#0F766E" text-anchor="middle">City_Paris</text>

      <rect x="315" y="0" width="105" height="26" fill="#CCFBF1" stroke="#99F6E4"/>
      <text x="367" y="17" font-family="monospace" font-size="10.5" font-weight="700" fill="#0F766E" text-anchor="middle">City_Tokyo</text>

      <!-- Row 1: Tokyo -->
      <rect x="0" y="26" width="105" height="24" fill="#FFFFFF" stroke="#E2E8F0"/><text x="52" y="42" font-family="monospace" font-size="11" fill="#64748B" text-anchor="middle">0</text>
      <rect x="105" y="26" width="105" height="24" fill="#FFFFFF" stroke="#E2E8F0"/><text x="157" y="42" font-family="monospace" font-size="11" fill="#64748B" text-anchor="middle">0</text>
      <rect x="210" y="26" width="105" height="24" fill="#FFFFFF" stroke="#E2E8F0"/><text x="262" y="42" font-family="monospace" font-size="11" fill="#64748B" text-anchor="middle">0</text>
      <rect x="315" y="26" width="105" height="24" fill="#ECFDF5" stroke="#10B981"/><text x="367" y="42" font-family="monospace" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">1</text>

      <!-- Row 2: Paris -->
      <rect x="0" y="50" width="105" height="24" fill="#F8FAFC" stroke="#E2E8F0"/><text x="52" y="66" font-family="monospace" font-size="11" fill="#64748B" text-anchor="middle">0</text>
      <rect x="105" y="50" width="105" height="24" fill="#F8FAFC" stroke="#E2E8F0"/><text x="157" y="66" font-family="monospace" font-size="11" fill="#64748B" text-anchor="middle">0</text>
      <rect x="210" y="50" width="105" height="24" fill="#ECFDF5" stroke="#10B981"/><text x="262" y="66" font-family="monospace" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">1</text>
      <rect x="315" y="50" width="105" height="24" fill="#F8FAFC" stroke="#E2E8F0"/><text x="367" y="66" font-family="monospace" font-size="11" fill="#64748B" text-anchor="middle">0</text>

      <!-- Row 3: New York -->
      <rect x="0" y="74" width="105" height="24" fill="#FFFFFF" stroke="#E2E8F0"/><text x="52" y="90" font-family="monospace" font-size="11" fill="#64748B" text-anchor="middle">0</text>
      <rect x="105" y="74" width="105" height="24" fill="#ECFDF5" stroke="#10B981"/><text x="157" y="90" font-family="monospace" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">1</text>
      <rect x="210" y="74" width="105" height="24" fill="#FFFFFF" stroke="#E2E8F0"/><text x="262" y="90" font-family="monospace" font-size="11" fill="#64748B" text-anchor="middle">0</text>
      <rect x="315" y="74" width="105" height="24" fill="#FFFFFF" stroke="#E2E8F0"/><text x="367" y="90" font-family="monospace" font-size="11" fill="#64748B" text-anchor="middle">0</text>

      <!-- Row 4: Unseen Sydney -->
      <rect x="0" y="98" width="105" height="24" fill="#FEF2F2" stroke="#FCA5A5"/><text x="52" y="114" font-family="monospace" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">0</text>
      <rect x="105" y="98" width="105" height="24" fill="#FEF2F2" stroke="#FCA5A5"/><text x="157" y="114" font-family="monospace" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">0</text>
      <rect x="210" y="98" width="105" height="24" fill="#FEF2F2" stroke="#FCA5A5"/><text x="262" y="114" font-family="monospace" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">0</text>
      <rect x="315" y="98" width="105" height="24" fill="#FEF2F2" stroke="#FCA5A5"/><text x="367" y="114" font-family="monospace" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">0</text>
    </g>

    <!-- Note on unseen categories -->
    <text x="460" y="185" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">
      <tspan font-weight="700" fill="#B91C1C">*Notice:</tspan> With <tspan font-family="monospace" font-weight="600">handle_unknown='ignore'</tspan>, unknown city "Sydney" produces an all-zero vector instead of crashing inference.
    </text>
  </g>
</svg>
"""

# 6. ORDINAL ENCODING HIERARCHY
SVG_MAP["__SVG_ORDINAL_ENCODING__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="oeShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#oeShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Ordinal Encoding: Preserving Monotonic Structural Hierarchy</text>

    <!-- Staircase Steps -->
    <!-- Step 0: High School -->
    <g transform="translate(60, 130)">
      <rect width="140" height="35" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="70" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">0: High School</text>
    </g>

    <path d="M 200 147 L 230 117" stroke="#0D9488" stroke-width="2" stroke-dasharray="3,3" fill="none"/>

    <!-- Step 1: Bachelor -->
    <g transform="translate(230, 100)">
      <rect width="140" height="35" rx="6" fill="#CCFBF1" stroke="#0D9488" stroke-width="1.5"/>
      <text x="70" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F766E" text-anchor="middle">1: Bachelor's</text>
    </g>

    <path d="M 370 117 L 400 87" stroke="#0D9488" stroke-width="2" stroke-dasharray="3,3" fill="none"/>

    <!-- Step 2: Master -->
    <g transform="translate(400, 70)">
      <rect width="140" height="35" rx="6" fill="#99F6E4" stroke="#0D9488" stroke-width="2"/>
      <text x="70" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#115E59" text-anchor="middle">2: Master's</text>
    </g>

    <path d="M 540 87 L 570 57" stroke="#0D9488" stroke-width="2" stroke-dasharray="3,3" fill="none"/>

    <!-- Step 3: PhD -->
    <g transform="translate(570, 40)">
      <rect width="140" height="35" rx="6" fill="#0D9488" stroke="#0F766E" stroke-width="2"/>
      <text x="70" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">3: Doctorate (PhD)</text>
    </g>

    <!-- Bottom Warning -->
    <rect x="50" y="170" width="680" height="24" rx="4" fill="#FFFBEB" stroke="#FDE68A"/>
    <text x="390" y="186" font-family="system-ui, sans-serif" font-size="11" fill="#78350F" text-anchor="middle">
      <tspan font-weight="700" fill="#B45309">⚠️ Critical Distinction:</tspan> Never apply ordinal encoding to nominal data like Cities or Colors; it creates false mathematical distances (e.g. Paris = 2 × Tokyo).
    </text>
  </g>
</svg>
"""

# 7. FEATURE SCALING COMPARISON
SVG_MAP["__SVG_FEATURE_SCALING__"] = """
<svg viewBox="0 0 820 260" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="fsShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#fsShadow)">
    <rect width="780" height="230" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Feature Scaling: Geometry and Coordinate Space Distortion</text>

    <!-- Left: Unscaled Distorted Space -->
    <g transform="translate(40, 50)">
      <rect width="320" height="150" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="160" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#B91C1C" text-anchor="middle">Unscaled Features (KNN / Gradient Descent Fail)</text>
      
      <!-- Coordinate system -->
      <line x1="40" y1="125" x2="280" y2="125" stroke="#475569" stroke-width="1.5"/>
      <line x1="40" y1="125" x2="40" y2="35" stroke="#475569" stroke-width="1.5"/>
      <text x="270" y="140" font-family="system-ui, sans-serif" font-size="10" fill="#475569">Income ($20k - $250k)</text>
      <text x="45" y="42" font-family="system-ui, sans-serif" font-size="10" fill="#475569">Age (20 - 65)</text>

      <!-- Stretched Ellipse distance -->
      <ellipse cx="160" cy="80" rx="100" ry="25" fill="#EF4444" fill-opacity="0.15" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="4,3"/>
      <text x="160" y="84" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B91C1C" text-anchor="middle">Distance dominated 99.9% by Income scale!</text>
    </g>

    <!-- Right: Standardized / Normalized Space -->
    <g transform="translate(420, 50)">
      <rect width="320" height="150" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <text x="160" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#047857" text-anchor="middle">Scaled Features (StandardScaler z-score)</text>
      
      <!-- Coordinate system -->
      <line x1="160" y1="135" x2="160" y2="35" stroke="#475569" stroke-width="1.5"/>
      <line x1="40" y1="85" x2="280" y2="85" stroke="#475569" stroke-width="1.5"/>
      <text x="270" y="80" font-family="system-ui, sans-serif" font-size="10" fill="#475569">+3σ</text>
      <text x="50" y="80" font-family="system-ui, sans-serif" font-size="10" fill="#475569">-3σ</text>
      <text x="165" y="45" font-family="system-ui, sans-serif" font-size="10" fill="#475569">+3σ</text>

      <!-- Balanced Circular Distance -->
      <circle cx="160" cy="85" r="42" fill="#10B981" fill-opacity="0.15" stroke="#10B981" stroke-width="2"/>
      <text x="160" y="89" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#047857" text-anchor="middle">Equally Weighted Circle</text>
    </g>
  </g>
</svg>
"""

# 8. FEATURE CREATION ENGINE
SVG_MAP["__SVG_FEATURE_CREATION__"] = """
<svg viewBox="0 0 820 230" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="fcShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#fcShadow)">
    <rect width="780" height="200" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Domain Feature Synthesis: Combining Raw Inputs into High-Signal Predictors</text>

    <!-- Raw inputs left -->
    <g transform="translate(30, 50)">
      <rect width="160" height="32" rx="6" fill="#F1F5F9" stroke="#CBD5E1"/>
      <text x="80" y="20" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">loan_amount ($)</text>

      <rect y="42" width="160" height="32" rx="6" fill="#F1F5F9" stroke="#CBD5E1"/>
      <text x="80" y="62" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">annual_income ($)</text>

      <rect y="84" width="160" height="32" rx="6" fill="#F1F5F9" stroke="#CBD5E1"/>
      <text x="80" y="104" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">signup_date (str)</text>
    </g>

    <!-- Synthesis Operations Center -->
    <g transform="translate(260, 50)">
      <!-- Operation 1 -->
      <path d="M -60 16 L 0 16 M -60 58 L 0 16" stroke="#0D9488" stroke-width="1.5"/>
      <rect x="0" y="0" width="160" height="32" rx="6" fill="#CCFBF1" stroke="#0D9488"/>
      <text x="80" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#115E59" text-anchor="middle">Ratio: Loan / Income</text>

      <!-- Operation 2 -->
      <path d="M -60 16 L 0 58 M -60 58 L 0 58" stroke="#0D9488" stroke-width="1.5"/>
      <rect x="0" y="42" width="160" height="32" rx="6" fill="#CCFBF1" stroke="#0D9488"/>
      <text x="80" y="62" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#115E59" text-anchor="middle">Log Transform: log1p</text>

      <!-- Operation 3 -->
      <path d="M -60 100 L 0 100" stroke="#0D9488" stroke-width="1.5"/>
      <rect x="0" y="84" width="160" height="32" rx="6" fill="#CCFBF1" stroke="#0D9488"/>
      <text x="80" y="104" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#115E59" text-anchor="middle">Delta: (Today - Date).days</text>
    </g>

    <!-- Resulting High Signal Features Right -->
    <g transform="translate(490, 50)">
      <path d="M -60 16 L 0 16" stroke="#0D9488" stroke-width="2"/>
      <rect x="0" y="0" width="230" height="32" rx="6" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <text x="115" y="20" font-family="monospace" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">debt_to_income (DTI)</text>

      <path d="M -60 58 L 0 58" stroke="#0D9488" stroke-width="2"/>
      <rect x="0" y="42" width="230" height="32" rx="6" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <text x="115" y="62" font-family="monospace" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">log_income (Normal Bell)</text>

      <path d="M -60 100 L 0 100" stroke="#0D9488" stroke-width="2"/>
      <rect x="0" y="84" width="230" height="32" rx="6" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <text x="115" y="104" font-family="monospace" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">account_age_days (Tenure)</text>
    </g>

    <text x="390" y="180" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">
      Domain knowledge converts raw isolated values into relational metrics that linearly align with real-world credit risk.
    </text>
  </g>
</svg>
"""

# 9. POLYNOMIAL AND INTERACTION FEATURES
SVG_MAP["__SVG_POLYNOMIAL_FEATURES__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="polyShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#polyShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Polynomial &amp; Interaction Expansion: [x1, x2] with Degree=2</text>

    <!-- Input Vector Box -->
    <g transform="translate(40, 60)">
      <rect width="140" height="85" rx="8" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="70" y="26" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#64748B" text-anchor="middle">Input Features (d=2)</text>
      <text x="70" y="52" font-family="monospace" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">[x₁,  x₂]</text>
      <text x="70" y="72" font-family="monospace" font-size="11" fill="#475569" text-anchor="middle">e.g. [2.0,  3.0]</text>
    </g>

    <!-- Arrow -->
    <path d="M 200 102 L 250 102" stroke="#0D9488" stroke-width="3" fill="none"/>
    <polygon points="250,97 260,102 250,107" fill="#0D9488"/>
    <text x="230" y="90" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F766E" text-anchor="middle">Poly(deg=2)</text>

    <!-- Expanded Features Grid -->
    <g transform="translate(275, 60)">
      <rect width="465" height="85" rx="8" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.5"/>
      <text x="232" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">Generated Feature Names (include_bias=False ➔ 5 Features)</text>
      
      <!-- Feature Pills -->
      <g transform="translate(15, 36)">
        <!-- x1 -->
        <rect x="0" y="0" width="75" height="36" rx="6" fill="#FFFFFF" stroke="#99F6E4"/>
        <text x="37" y="16" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">x₁</text>
        <text x="37" y="30" font-family="monospace" font-size="10" fill="#64748B" text-anchor="middle">2.0</text>

        <!-- x2 -->
        <rect x="88" y="0" width="75" height="36" rx="6" fill="#FFFFFF" stroke="#99F6E4"/>
        <text x="125" y="16" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">x₂</text>
        <text x="125" y="30" font-family="monospace" font-size="10" fill="#64748B" text-anchor="middle">3.0</text>

        <!-- x1^2 -->
        <rect x="176" y="0" width="75" height="36" rx="6" fill="#CCFBF1" stroke="#0D9488"/>
        <text x="213" y="16" font-family="monospace" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">x₁²</text>
        <text x="213" y="30" font-family="monospace" font-size="10" fill="#115E59" text-anchor="middle">4.0</text>

        <!-- x1 x2 -->
        <rect x="264" y="0" width="85" height="36" rx="6" fill="#CCFBF1" stroke="#0D9488"/>
        <text x="306" y="16" font-family="monospace" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">x₁ · x₂</text>
        <text x="306" y="30" font-family="monospace" font-size="10" fill="#115E59" text-anchor="middle">6.0</text>

        <!-- x2^2 -->
        <rect x="362" y="0" width="75" height="36" rx="6" fill="#CCFBF1" stroke="#0D9488"/>
        <text x="399" y="16" font-family="monospace" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">x₂²</text>
        <text x="399" y="30" font-family="monospace" font-size="10" fill="#115E59" text-anchor="middle">9.0</text>
      </g>
    </g>

    <!-- Warning Footer -->
    <text x="390" y="172" font-family="system-ui, sans-serif" font-size="11" fill="#475569" text-anchor="middle">
      Dimensionality formula: C(n + d, d) grows combinatorially. Always pair higher-degree polynomials with Ridge/Lasso regularization!
    </text>
  </g>
</svg>
"""

# 10. FEATURE SELECTION RANKING
SVG_MAP["__SVG_FEATURE_SELECTION__"] = """
<svg viewBox="0 0 820 250" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="selShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#selShadow)">
    <rect width="780" height="220" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Feature Selection: SelectKBest (ANOVA F-Score Ranking)</text>

    <!-- Bar 1: debt_to_income -->
    <text x="140" y="65" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">debt_to_income</text>
    <rect x="150" y="52" width="480" height="18" rx="4" fill="#0D9488"/>
    <text x="640" y="66" font-family="monospace" font-size="11" font-weight="700" fill="#0D9488">F=184.2 (Selected ✔)</text>

    <!-- Bar 2: credit_score -->
    <text x="140" y="90" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">credit_score</text>
    <rect x="150" y="77" width="390" height="18" rx="4" fill="#0D9488"/>
    <text x="550" y="91" font-family="monospace" font-size="11" font-weight="700" fill="#0D9488">F=142.8 (Selected ✔)</text>

    <!-- Bar 3: annual_income -->
    <text x="140" y="115" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">annual_income</text>
    <rect x="150" y="102" width="310" height="18" rx="4" fill="#0D9488"/>
    <text x="470" y="116" font-family="monospace" font-size="11" font-weight="700" fill="#0D9488">F=112.5 (Selected ✔)</text>

    <!-- Threshold Cutoff Line -->
    <line x1="420" y1="45" x2="420" y2="185" stroke="#EF4444" stroke-width="2" stroke-dasharray="4,3"/>
    <text x="425" y="198" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#EF4444">Top-K Cutoff Threshold</text>

    <!-- Bar 4: age -->
    <text x="140" y="140" font-family="monospace" font-size="11" fill="#475569" text-anchor="end">applicant_age</text>
    <rect x="150" y="127" width="180" height="18" rx="4" fill="#94A3B8"/>
    <text x="340" y="141" font-family="monospace" font-size="11" fill="#64748B">F=48.2 (Dropped)</text>

    <!-- Bar 5: random_noise_id -->
    <text x="140" y="165" font-family="monospace" font-size="11" fill="#475569" text-anchor="end">customer_id</text>
    <rect x="150" y="152" width="20" height="18" rx="4" fill="#CBD5E1"/>
    <text x="180" y="166" font-family="monospace" font-size="11" fill="#64748B">F=0.4 (Zero Signal)</text>

    <text x="390" y="212" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">
      Filter methods evaluate statistical dependence between features and targets without fitting an expensive ML model.
    </text>
  </g>
</svg>
"""

# 11. DATA LEAKAGE: INCORRECT VS CORRECT WORKFLOW
SVG_MAP["__SVG_DATA_LEAKAGE__"] = """
<svg viewBox="0 0 820 270" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="dlShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#dlShadow)">
    <rect width="780" height="240" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Data Leakage: Flawed Global Preprocessing vs Leakage-Free Pipeline</text>

    <!-- Top: WRONG / LEAKY -->
    <g transform="translate(30, 48)">
      <rect width="720" height="75" rx="6" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="15" y="20" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#B91C1C">❌ WRONG: Preprocessing Fitted on Entire Dataset Before Split (Data Leakage)</text>

      <g transform="translate(15, 30)">
        <rect width="180" height="32" rx="4" fill="#FFFFFF" stroke="#FCA5A5"/>
        <text x="90" y="20" font-family="system-ui, sans-serif" font-size="10.5" fill="#7F1D1D" text-anchor="middle">1. Full Dataset (All Rows)</text>

        <path d="M 185 16 L 215 16" stroke="#EF4444" stroke-width="1.5"/>
        <rect x="220" y="0" width="220" height="32" rx="4" fill="#FEE2E2" stroke="#EF4444"/>
        <text x="330" y="14" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#991B1B" text-anchor="middle">scaler.fit_transform(X_all)</text>
        <text x="330" y="26" font-family="system-ui, sans-serif" font-size="9" fill="#B91C1C" text-anchor="middle">Test set mean &amp; variance leak into train!</text>

        <path d="M 445 16 L 475 16" stroke="#EF4444" stroke-width="1.5"/>
        <rect x="480" y="0" width="210" height="32" rx="4" fill="#FFFFFF" stroke="#FCA5A5"/>
        <text x="585" y="20" font-family="system-ui, sans-serif" font-size="10.5" fill="#7F1D1D" text-anchor="middle">Train/Test Split (Illusion!)</text>
      </g>
    </g>

    <!-- Bottom: CORRECT -->
    <g transform="translate(30, 135)">
      <rect width="720" height="85" rx="6" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <text x="15" y="20" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#047857">✔ CORRECT: Split First, Then Fit Preprocessor Strictly on Training Fold</text>

      <g transform="translate(15, 30)">
        <rect width="180" height="38" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
        <text x="90" y="17" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#14532D" text-anchor="middle">1. Train/Test Split First</text>
        <text x="90" y="30" font-family="system-ui, sans-serif" font-size="9" fill="#15803D" text-anchor="middle">Test set locked away</text>

        <path d="M 185 19 L 215 19" stroke="#10B981" stroke-width="2"/>
        <rect x="220" y="0" width="220" height="38" rx="4" fill="#D1FAE5" stroke="#10B981"/>
        <text x="330" y="16" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#065F46" text-anchor="middle">pipeline.fit(X_train)</text>
        <text x="330" y="30" font-family="system-ui, sans-serif" font-size="9" fill="#047857" text-anchor="middle">Learns μ, σ ONLY from training rows</text>

        <path d="M 445 19 L 475 19" stroke="#10B981" stroke-width="2"/>
        <rect x="480" y="0" width="210" height="38" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
        <text x="585" y="16" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#14532D" text-anchor="middle">pipeline.predict(X_test)</text>
        <text x="585" y="30" font-family="system-ui, sans-serif" font-size="9" fill="#15803D" text-anchor="middle">Transform test with frozen train stats</text>
      </g>
    </g>
  </g>
</svg>
"""

# 12. BASIC ML PIPELINE DIAGRAM
SVG_MAP["__SVG_BASIC_PIPELINE__"] = """
<svg viewBox="0 0 820 180" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="bpShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#bpShadow)">
    <rect width="780" height="150" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="30" rx="10" fill="#F0FDFA"/>
    <text x="25" y="20" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Linear Pipeline Architecture: Sequential Transformers ➔ Final Estimator</text>

    <!-- Stage 1 -->
    <g transform="translate(30, 48)">
      <rect width="150" height="65" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="75" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0D9488" text-anchor="middle">STEP 1: IMPUTE</text>
      <text x="75" y="40" font-family="monospace" font-size="11" fill="#0F172A" text-anchor="middle">SimpleImputer</text>
      <text x="75" y="55" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">strategy='median'</text>
    </g>

    <path d="M 185 80 L 225 80" stroke="#0D9488" stroke-width="2"/>
    <polygon points="225,76 233,80 225,84" fill="#0D9488"/>

    <!-- Stage 2 -->
    <g transform="translate(235, 48)">
      <rect width="150" height="65" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="75" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0D9488" text-anchor="middle">STEP 2: SCALE</text>
      <text x="75" y="40" font-family="monospace" font-size="11" fill="#0F172A" text-anchor="middle">StandardScaler</text>
      <text x="75" y="55" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">z = (x - μ) / σ</text>
    </g>

    <path d="M 390 80 L 430 80" stroke="#0D9488" stroke-width="2"/>
    <polygon points="430,76 438,80 430,84" fill="#0D9488"/>

    <!-- Stage 3 -->
    <g transform="translate(440, 48)">
      <rect width="150" height="65" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="75" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0D9488" text-anchor="middle">STEP 3: SELECT</text>
      <text x="75" y="40" font-family="monospace" font-size="11" fill="#0F172A" text-anchor="middle">SelectKBest</text>
      <text x="75" y="55" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">k=10, f_classif</text>
    </g>

    <path d="M 595 80 L 635 80" stroke="#0D9488" stroke-width="2"/>
    <polygon points="635,76 643,80 635,84" fill="#0D9488"/>

    <!-- Stage 4: Estimator -->
    <g transform="translate(645, 48)">
      <rect width="115" height="65" rx="6" fill="#0D9488" stroke="#0F766E" stroke-width="2"/>
      <text x="57" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#CCFBF1" text-anchor="middle">FINAL STEP</text>
      <text x="57" y="40" font-family="monospace" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">Classifier</text>
      <text x="57" y="55" font-family="system-ui, sans-serif" font-size="9" fill="#F0FDFA" text-anchor="middle">fit() &amp; predict()</text>
    </g>

    <text x="390" y="132" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">
      During <tspan font-family="monospace">fit()</tspan>, all transformers call <tspan font-family="monospace">fit_transform()</tspan>. During <tspan font-family="monospace">predict()</tspan>, only <tspan font-family="monospace">transform()</tspan> is executed.
    </text>
  </g>
</svg>
"""

# 13. COLUMN TRANSFORMER ARCHITECTURE
SVG_MAP["__SVG_COLUMN_TRANSFORMER__"] = """
<svg viewBox="0 0 820 250" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="ctShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#ctShadow)">
    <rect width="780" height="220" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">ColumnTransformer: Branching Heterogeneous Features into Unified Numeric Arrays</text>

    <!-- Raw Data Matrix Left -->
    <g transform="translate(30, 50)">
      <rect width="130" height="130" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="65" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Mixed Raw Table</text>
      
      <rect x="15" y="38" width="100" height="24" rx="4" fill="#CCFBF1"/>
      <text x="65" y="54" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#0F766E" text-anchor="middle">Numerical (6 cols)</text>

      <rect x="15" y="70" width="100" height="24" rx="4" fill="#FEF3C7"/>
      <text x="65" y="86" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#92400E" text-anchor="middle">Categorical (3 cols)</text>

      <rect x="15" y="102" width="100" height="18" rx="4" fill="#E2E8F0"/>
      <text x="65" y="115" font-family="system-ui, sans-serif" font-size="9" fill="#475569" text-anchor="middle">remainder='drop'</text>
    </g>

    <!-- Branch Paths -->
    <path d="M 165 75 L 235 60" stroke="#0D9488" stroke-width="2"/>
    <path d="M 165 115 L 235 130" stroke="#D97706" stroke-width="2"/>

    <!-- Branch 1: Numerical Pipeline -->
    <g transform="translate(240, 42)">
      <rect width="260" height="42" rx="6" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.5"/>
      <text x="130" y="18" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0F766E" text-anchor="middle">num_transformer Pipeline</text>
      <text x="130" y="32" font-family="monospace" font-size="10" fill="#115E59" text-anchor="middle">SimpleImputer(median) ➔ StandardScaler()</text>
    </g>

    <!-- Branch 2: Categorical Pipeline -->
    <g transform="translate(240, 110)">
      <rect width="260" height="42" rx="6" fill="#FFFBEB" stroke="#D97706" stroke-width="1.5"/>
      <text x="130" y="18" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#B45309" text-anchor="middle">cat_transformer Pipeline</text>
      <text x="130" y="32" font-family="monospace" font-size="10" fill="#78350F" text-anchor="middle">Imputer(most_frequent) ➔ OneHotEncoder()</text>
    </g>

    <!-- Merge Paths -->
    <path d="M 505 63 L 565 95" stroke="#0D9488" stroke-width="2"/>
    <path d="M 505 131 L 565 95" stroke="#D97706" stroke-width="2"/>

    <!-- Concatenated Matrix Right -->
    <g transform="translate(570, 50)">
      <rect width="180" height="130" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
      <text x="90" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">Combined NumPy Matrix</text>
      
      <rect x="15" y="38" width="150" height="28" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
      <text x="90" y="56" font-family="monospace" font-size="10.5" font-weight="700" fill="#065F46" text-anchor="middle">np.hstack([Num, Cat])</text>

      <text x="90" y="85" font-family="system-ui, sans-serif" font-size="10" fill="#15803D" text-anchor="middle">6 Scaled Floats</text>
      <text x="90" y="100" font-family="system-ui, sans-serif" font-size="10" fill="#15803D" text-anchor="middle">+ 13 Binary One-Hot Dummies</text>
      <text x="90" y="118" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">= 19 Total Features</text>
    </g>

    <text x="390" y="200" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">
      <tspan font-family="monospace">ColumnTransformer</tspan> routes specified columns to dedicated pipelines and horizontally stacks the resulting arrays.
    </text>
  </g>
</svg>
"""

# 14. MIXED-DATA PREPROCESSING PIPELINE
SVG_MAP["__SVG_MIXED_PIPELINE__"] = """
<svg viewBox="0 0 820 190" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="mpShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#mpShadow)">
    <rect width="780" height="160" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="30" rx="10" fill="#F0FDFA"/>
    <text x="25" y="20" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Full Mixed-Data Architecture: ColumnTransformer Enclosed in Master Pipeline</text>

    <!-- Outer Pipeline Box -->
    <g transform="translate(30, 42)">
      <rect width="720" height="100" rx="8" fill="#F8FAFC" stroke="#0D9488" stroke-width="2" stroke-dasharray="6,4"/>
      <text x="15" y="18" font-family="monospace" font-size="11" font-weight="700" fill="#0D9488">Pipeline(steps=[ ('preprocessor', ct), ('classifier', clf) ])</text>

      <!-- Inside Step 1: Preprocessor -->
      <g transform="translate(15, 26)">
        <rect width="400" height="62" rx="6" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
        <text x="200" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">'preprocessor': ColumnTransformer</text>
        <text x="200" y="40" font-family="system-ui, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Handles Imputation, Scaling, and One-Hot Encoding</text>
      </g>

      <!-- Arrow -->
      <path d="M 425 57 L 465 57" stroke="#0D9488" stroke-width="2.5"/>
      <polygon points="465,53 473,57 465,61" fill="#0D9488"/>

      <!-- Inside Step 2: Classifier -->
      <g transform="translate(480, 26)">
        <rect width="220" height="62" rx="6" fill="#0D9488" stroke="#0F766E" stroke-width="2"/>
        <text x="110" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#CCFBF1" text-anchor="middle">'classifier': Estimator</text>
        <text x="110" y="42" font-family="system-ui, sans-serif" font-size="10" fill="#FFFFFF" text-anchor="middle">RandomForest / LogisticReg</text>
      </g>
    </g>
  </g>
</svg>
"""

# 15. CROSS-VALIDATION WITH FULL PIPELINE
SVG_MAP["__SVG_CV_PIPELINE__"] = """
<svg viewBox="0 0 820 240" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="cvpShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#cvpShadow)">
    <rect width="780" height="210" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Cross-Validation Inside Pipeline: Zero Leakage Across Folds</text>

    <!-- Fold 1 -->
    <g transform="translate(40, 52)">
      <text x="0" y="16" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Fold 1:</text>
      <rect x="60" y="0" width="440" height="22" rx="3" fill="#CCFBF1" stroke="#0D9488"/>
      <text x="280" y="15" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#0F766E" text-anchor="middle">Fit Imputer &amp; Scaler on Folds 2, 3, 4, 5 (Train)</text>
      <rect x="510" y="0" width="110" height="22" rx="3" fill="#FEF3C7" stroke="#F59E0B"/>
      <text x="565" y="15" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">Val Fold 1</text>
      <text x="640" y="15" font-family="monospace" font-size="11" fill="#0F766E">Acc: 0.9250</text>
    </g>

    <!-- Fold 2 -->
    <g transform="translate(40, 80)">
      <text x="0" y="16" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Fold 2:</text>
      <rect x="60" y="0" width="110" height="22" rx="3" fill="#CCFBF1" stroke="#0D9488"/>
      <rect x="175" y="0" width="110" height="22" rx="3" fill="#FEF3C7" stroke="#F59E0B"/>
      <text x="230" y="15" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">Val Fold 2</text>
      <rect x="290" y="0" width="330" height="22" rx="3" fill="#CCFBF1" stroke="#0D9488"/>
      <text x="455" y="15" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#0F766E" text-anchor="middle">Fit Imputer &amp; Scaler on Folds 1, 3, 4, 5 (Train)</text>
      <text x="640" y="15" font-family="monospace" font-size="11" fill="#0F766E">Acc: 0.9125</text>
    </g>

    <!-- Fold 3 -->
    <g transform="translate(40, 108)">
      <text x="0" y="16" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Fold 3:</text>
      <rect x="60" y="0" width="220" height="22" rx="3" fill="#CCFBF1" stroke="#0D9488"/>
      <rect x="285" y="0" width="110" height="22" rx="3" fill="#FEF3C7" stroke="#F59E0B"/>
      <text x="340" y="15" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">Val Fold 3</text>
      <rect x="400" y="0" width="220" height="22" rx="3" fill="#CCFBF1" stroke="#0D9488"/>
      <text x="510" y="15" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#0F766E" text-anchor="middle">Train Folds</text>
      <text x="640" y="15" font-family="monospace" font-size="11" fill="#0F766E">Acc: 0.9375</text>
    </g>

    <!-- Bottom Summary Box -->
    <rect x="40" y="145" width="700" height="42" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="390" y="165" font-family="system-ui, sans-serif" font-size="11.5" fill="#0F172A" text-anchor="middle">
      <tspan font-weight="700" fill="#0D9488">5-Fold CV Mean Score:</tspan> 0.9187 ± 0.0209 Accuracy
    </text>
    <text x="390" y="179" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">
      Because the entire pipeline is wrapped in <tspan font-family="monospace">cross_val_score</tspan>, each fold calculates its own independent means and categories.
    </text>
  </g>
</svg>
"""

# 16. HYPERPARAMETER TUNING INSIDE PIPELINE
SVG_MAP["__SVG_TUNING_PIPELINE__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="tpShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#tpShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">GridSearchCV Inside Pipeline: Tuning Preprocessing &amp; Model Jointly</text>

    <!-- Double Underscore Naming Rule Box -->
    <g transform="translate(30, 48)">
      <rect width="720" height="52" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="20" y="22" font-family="monospace" font-size="12" font-weight="700" fill="#0F766E">step_name__substep_name__parameter_name</text>
      <text x="20" y="40" font-family="system-ui, sans-serif" font-size="11" fill="#475569">
        Scikit-learn uses double underscores (<tspan font-family="monospace" font-weight="700">__</tspan>) to traverse nested pipeline layers and inspect inner parameters.
      </text>
    </g>

    <!-- Grid Candidates -->
    <g transform="translate(30, 110)">
      <!-- Preprocessing Hyperparameter -->
      <rect x="0" y="0" width="345" height="58" rx="6" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.5"/>
      <text x="172" y="18" font-family="monospace" font-size="10.5" font-weight="700" fill="#0F766E" text-anchor="middle">preprocessor__num__imputer__strategy</text>
      <text x="172" y="38" font-family="system-ui, sans-serif" font-size="11" fill="#115E59" text-anchor="middle">Candidate Values: ['mean', 'median']</text>

      <!-- Estimator Hyperparameters -->
      <rect x="365" y="0" width="355" height="58" rx="6" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.5"/>
      <text x="177" y="18" font-family="monospace" font-size="10.5" font-weight="700" fill="#0F766E" text-anchor="middle">classifier__n_estimators &amp; max_depth</text>
      <text x="177" y="38" font-family="system-ui, sans-serif" font-size="11" fill="#115E59" text-anchor="middle">Candidates: [50, 100] &amp; [5, 8, 12]</text>
    </g>

    <text x="390" y="180" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">
      Jointly tuning avoids suboptimal decisions like choosing an imputer strategy based on intuition alone.
    </text>
  </g>
</svg>
"""

# 17. DATE/TIME AND TEXT FEATURE ENGINEERING
SVG_MAP["__SVG_DATETIME_TEXT__"] = """
<svg viewBox="0 0 820 230" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="dtShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#dtShadow)">
    <rect width="780" height="200" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Advanced Encodings: Cyclical Time Coordinates &amp; Text NLP Vectors</text>

    <!-- Left: 24-Hour Cyclical Sine / Cosine Clock -->
    <g transform="translate(30, 48)">
      <rect width="345" height="135" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="172" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">Cyclical Encoding (23:00 and 01:00 are close!)</text>

      <!-- Circular Clock diagram -->
      <circle cx="80" cy="75" r="35" fill="#FFFFFF" stroke="#0D9488" stroke-width="1.5"/>
      <text x="80" y="47" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#0F766E" text-anchor="middle">24h / 0h</text>
      <text x="115" y="78" font-family="system-ui, sans-serif" font-size="9" fill="#0F766E">6h</text>
      <text x="80" y="105" font-family="system-ui, sans-serif" font-size="9" fill="#0F766E" text-anchor="middle">12h</text>
      <text x="42" y="78" font-family="system-ui, sans-serif" font-size="9" fill="#0F766E">18h</text>

      <!-- Formulas right of clock -->
      <text x="140" y="65" font-family="monospace" font-size="10" fill="#0F172A">sin(2π · hour / 24)</text>
      <text x="140" y="90" font-family="monospace" font-size="10" fill="#0F172A">cos(2π · hour / 24)</text>
      <text x="140" y="115" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B">Preserves continuous loop</text>
    </g>

    <!-- Right: Text Tokenization & TF-IDF -->
    <g transform="translate(405, 48)">
      <rect width="345" height="135" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="172" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">Text Vectorization: TfidfVectorizer</text>

      <rect x="20" y="35" width="305" height="24" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="172" y="51" font-family="monospace" font-size="10" fill="#0F172A" text-anchor="middle">"Urgent: Loan approved immediately"</text>

      <!-- Token pills -->
      <g transform="translate(20, 68)">
        <rect x="0" y="0" width="65" height="22" rx="3" fill="#CCFBF1"/>
        <text x="32" y="15" font-family="monospace" font-size="9" fill="#0F766E" text-anchor="middle">"urgent"</text>

        <rect x="72" y="0" width="60" height="22" rx="3" fill="#CCFBF1"/>
        <text x="102" y="15" font-family="monospace" font-size="9" fill="#0F766E" text-anchor="middle">"loan"</text>

        <rect x="139" y="0" width="75" height="22" rx="3" fill="#CCFBF1"/>
        <text x="176" y="15" font-family="monospace" font-size="9" fill="#0F766E" text-anchor="middle">"approved"</text>

        <rect x="221" y="0" width="84" height="22" rx="3" fill="#CCFBF1"/>
        <text x="263" y="15" font-family="monospace" font-size="9" fill="#0F766E" text-anchor="middle">"immediately"</text>
      </g>

      <text x="172" y="115" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" text-anchor="middle">TF-IDF: Term Frequency × Inverse Document Frequency</text>
    </g>
  </g>
</svg>
"""

# 18. CORRELATION HEATMAP
SVG_MAP["__SVG_CORRELATION_HEATMAP__"] = """
<svg viewBox="0 0 820 250" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="hmShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#hmShadow)">
    <rect width="780" height="220" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Feature Correlation Matrix Heatmap (Pearson r)</text>

    <!-- Heatmap Grid (5x5) -->
    <g transform="translate(180, 50)">
      <!-- Labels Top -->
      <text x="35" y="-8" font-family="monospace" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">Age</text>
      <text x="95" y="-8" font-family="monospace" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">Income</text>
      <text x="155" y="-8" font-family="monospace" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">Credit</text>
      <text x="215" y="-8" font-family="monospace" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">LoanAmt</text>
      <text x="275" y="-8" font-family="monospace" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">DTI</text>

      <!-- Row 1: Age -->
      <text x="-15" y="22" font-family="monospace" font-size="10" font-weight="700" fill="#475569" text-anchor="end">Age</text>
      <rect x="5" y="5" width="55" height="26" fill="#0F766E"/><text x="32" y="22" font-family="monospace" font-size="10" fill="#FFFFFF" text-anchor="middle">1.00</text>
      <rect x="65" y="5" width="55" height="26" fill="#CCFBF1"/><text x="92" y="22" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.18</text>
      <rect x="125" y="5" width="55" height="26" fill="#F0FDFA"/><text x="152" y="22" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.05</text>
      <rect x="185" y="5" width="55" height="26" fill="#CCFBF1"/><text x="212" y="22" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.12</text>
      <rect x="245" y="5" width="55" height="26" fill="#FEF2F2"/><text x="272" y="22" font-family="monospace" font-size="10" fill="#B91C1C" text-anchor="middle">-0.04</text>

      <!-- Row 2: Income -->
      <text x="-15" y="52" font-family="monospace" font-size="10" font-weight="700" fill="#475569" text-anchor="end">Income</text>
      <rect x="5" y="35" width="55" height="26" fill="#CCFBF1"/><text x="32" y="52" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.18</text>
      <rect x="65" y="35" width="55" height="26" fill="#0F766E"/><text x="92" y="52" font-family="monospace" font-size="10" fill="#FFFFFF" text-anchor="middle">1.00</text>
      <rect x="125" y="35" width="55" height="26" fill="#F0FDFA"/><text x="152" y="52" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.08</text>
      <rect x="185" y="35" width="55" height="26" fill="#2DD4BF"/><text x="212" y="52" font-family="monospace" font-size="10" fill="#115E59" text-anchor="middle">0.68</text>
      <rect x="245" y="35" width="55" height="26" fill="#FCA5A5"/><text x="272" y="52" font-family="monospace" font-size="10" fill="#7F1D1D" text-anchor="middle">-0.42</text>

      <!-- Row 3: Credit -->
      <text x="-15" y="82" font-family="monospace" font-size="10" font-weight="700" fill="#475569" text-anchor="end">Credit</text>
      <rect x="5" y="65" width="55" height="26" fill="#F0FDFA"/><text x="32" y="82" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.05</text>
      <rect x="65" y="65" width="55" height="26" fill="#F0FDFA"/><text x="92" y="82" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.08</text>
      <rect x="125" y="65" width="55" height="26" fill="#0F766E"/><text x="152" y="82" font-family="monospace" font-size="10" fill="#FFFFFF" text-anchor="middle">1.00</text>
      <rect x="185" y="65" width="55" height="26" fill="#F0FDFA"/><text x="212" y="82" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.02</text>
      <rect x="245" y="65" width="55" height="26" fill="#FEF2F2"/><text x="272" y="82" font-family="monospace" font-size="10" fill="#B91C1C" text-anchor="middle">-0.06</text>

      <!-- Row 4: LoanAmt -->
      <text x="-15" y="112" font-family="monospace" font-size="10" font-weight="700" fill="#475569" text-anchor="end">LoanAmt</text>
      <rect x="5" y="95" width="55" height="26" fill="#CCFBF1"/><text x="32" y="112" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.12</text>
      <rect x="65" y="95" width="55" height="26" fill="#2DD4BF"/><text x="92" y="112" font-family="monospace" font-size="10" fill="#115E59" text-anchor="middle">0.68</text>
      <rect x="125" y="95" width="55" height="26" fill="#F0FDFA"/><text x="152" y="112" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.02</text>
      <rect x="185" y="95" width="55" height="26" fill="#0F766E"/><text x="212" y="112" font-family="monospace" font-size="10" fill="#FFFFFF" text-anchor="middle">1.00</text>
      <rect x="245" y="95" width="55" height="26" fill="#99F6E4"/><text x="272" y="112" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.34</text>

      <!-- Row 5: DTI -->
      <text x="-15" y="142" font-family="monospace" font-size="10" font-weight="700" fill="#475569" text-anchor="end">DTI</text>
      <rect x="5" y="125" width="55" height="26" fill="#FEF2F2"/><text x="32" y="142" font-family="monospace" font-size="10" fill="#B91C1C" text-anchor="middle">-0.04</text>
      <rect x="65" y="125" width="55" height="26" fill="#FCA5A5"/><text x="92" y="142" font-family="monospace" font-size="10" fill="#7F1D1D" text-anchor="middle">-0.42</text>
      <rect x="125" y="125" width="55" height="26" fill="#FEF2F2"/><text x="152" y="142" font-family="monospace" font-size="10" fill="#B91C1C" text-anchor="middle">-0.06</text>
      <rect x="185" y="125" width="55" height="26" fill="#99F6E4"/><text x="212" y="142" font-family="monospace" font-size="10" fill="#0F766E" text-anchor="middle">0.34</text>
      <rect x="245" y="125" width="55" height="26" fill="#0F766E"/><text x="272" y="142" font-family="monospace" font-size="10" fill="#FFFFFF" text-anchor="middle">1.00</text>
    </g>

    <!-- Legend Right -->
    <g transform="translate(540, 65)">
      <text x="0" y="15" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Correlation Scale:</text>
      <rect x="0" y="25" width="20" height="20" fill="#0F766E"/><text x="28" y="40" font-family="monospace" font-size="10" fill="#334155">+1.0 (Strong Positive)</text>
      <rect x="0" y="50" width="20" height="20" fill="#CCFBF1"/><text x="28" y="65" font-family="monospace" font-size="10" fill="#334155">+0.2 (Weak Positive)</text>
      <rect x="0" y="75" width="20" height="20" fill="#FCA5A5"/><text x="28" y="90" font-family="monospace" font-size="10" fill="#334155">-0.4 (Moderate Negative)</text>
    </g>
  </g>
</svg>
"""

# 19. ACTUAL MODEL BENCHMARK COMPARISON
SVG_MAP["__SVG_MODEL_COMPARISON__"] = """
<svg viewBox="0 0 820 250" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="mcShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#mcShadow)">
    <rect width="780" height="220" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Empirical Benchmark: Baseline vs Feature Engineering vs Tuned Pipeline</text>

    <!-- Group 1: Baseline (Raw + LogisticRegression) -->
    <g transform="translate(60, 55)">
      <rect width="200" height="135" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="100" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#64748B" text-anchor="middle">1. Baseline (Raw)</text>
      
      <text x="15" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#475569">Accuracy:</text>
      <text x="185" y="48" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">87.50%</text>

      <text x="15" y="73" font-family="system-ui, sans-serif" font-size="10" fill="#475569">F1-Score:</text>
      <text x="185" y="73" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">0.7423</text>

      <text x="15" y="98" font-family="system-ui, sans-serif" font-size="10" fill="#475569">ROC-AUC:</text>
      <text x="185" y="98" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">0.9547</text>

      <rect x="15" y="112" width="170" height="15" rx="3" fill="#E2E8F0"/>
      <text x="100" y="123" font-family="system-ui, sans-serif" font-size="9" fill="#475569" text-anchor="middle">No Domain Ratios</text>
    </g>

    <!-- Group 2: Feature-Engineered Random Forest -->
    <g transform="translate(290, 55)">
      <rect width="200" height="135" rx="8" fill="#F0FDFA" stroke="#99F6E4"/>
      <text x="100" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F766E" text-anchor="middle">2. Feature-Eng RF (Default)</text>
      
      <text x="15" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#115E59">Accuracy:</text>
      <text x="185" y="48" font-family="monospace" font-size="11" font-weight="700" fill="#0F766E" text-anchor="end">88.50%</text>

      <text x="15" y="73" font-family="system-ui, sans-serif" font-size="10" fill="#115E59">F1-Score:</text>
      <text x="185" y="73" font-family="monospace" font-size="11" font-weight="700" fill="#0F766E" text-anchor="end">0.7460</text>

      <text x="15" y="98" font-family="system-ui, sans-serif" font-size="10" fill="#115E59">5-Fold CV:</text>
      <text x="185" y="98" font-family="monospace" font-size="11" font-weight="700" fill="#0F766E" text-anchor="end">89.00%</text>

      <rect x="15" y="112" width="170" height="15" rx="3" fill="#CCFBF1"/>
      <text x="100" y="123" font-family="system-ui, sans-serif" font-size="9" font-weight="600" fill="#115E59" text-anchor="middle">+ DTI &amp; Loan Ratios</text>
    </g>

    <!-- Group 3: Tuned Pipeline (GridSearchCV) -->
    <g transform="translate(520, 55)">
      <rect width="200" height="135" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
      <text x="100" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">3. Tuned Pipeline (Best ✔)</text>
      
      <text x="15" y="48" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46">Accuracy:</text>
      <text x="185" y="48" font-family="monospace" font-size="11" font-weight="800" fill="#047857" text-anchor="end">89.50% (+2%)</text>

      <text x="15" y="73" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46">F1-Score:</text>
      <text x="185" y="73" font-family="monospace" font-size="11" font-weight="800" fill="#047857" text-anchor="end">0.7529 (+1%)</text>

      <text x="15" y="98" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46">CV ROC-AUC:</text>
      <text x="185" y="98" font-family="monospace" font-size="11" font-weight="800" fill="#047857" text-anchor="end">0.9593</text>

      <rect x="15" y="112" width="170" height="15" rx="3" fill="#A7F3D0"/>
      <text x="100" y="123" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">Optimal Model + Preprocessor</text>
    </g>

    <text x="390" y="205" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">
      Empirically validated on Wisconsin / Synthetic Loan Approval test holdout set (N=200).
    </text>
  </g>
</svg>
"""

# 20. END-TO-END PIPELINE DECISION GUIDE
SVG_MAP["__SVG_DECISION_GUIDE__"] = """
<svg viewBox="0 0 820 280" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="dgShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#dgShadow)">
    <rect width="780" height="250" rx="10" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#F0FDFA"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#0F766E">Master Preprocessing Decision Guide: Choosing the Right Transformer</text>

    <!-- Node 1: Raw Column Type -->
    <g transform="translate(40, 55)">
      <rect width="180" height="42" rx="6" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="90" y="18" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">1. Inspect Column Type</text>
      <text x="90" y="32" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" text-anchor="middle">Numerical vs Categorical vs Text</text>
    </g>

    <!-- Branch Paths -->
    <path d="M 220 76 L 270 76" stroke="#0D9488" stroke-width="2"/>

    <!-- Node 2: Missing Values -->
    <g transform="translate(270, 55)">
      <rect width="210" height="42" rx="6" fill="#CCFBF1" stroke="#0D9488"/>
      <text x="105" y="18" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#115E59" text-anchor="middle">2. Missing Value Imputation</text>
      <text x="105" y="32" font-family="system-ui, sans-serif" font-size="9.5" fill="#0F766E" text-anchor="middle">Skewed: median | Normal: mean</text>
    </g>

    <path d="M 480 76 L 530 76" stroke="#0D9488" stroke-width="2"/>

    <!-- Node 3: Scaling & Encoding -->
    <g transform="translate(530, 55)">
      <rect width="210" height="42" rx="6" fill="#CCFBF1" stroke="#0D9488"/>
      <text x="105" y="18" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#115E59" text-anchor="middle">3. Transform Representation</text>
      <text x="105" y="32" font-family="system-ui, sans-serif" font-size="9.5" fill="#0F766E" text-anchor="middle">OneHot (Nominal) | Scaler (Numeric)</text>
    </g>

    <!-- Branch to Pipeline Assembly -->
    <path d="M 635 97 L 635 125 M 635 125 L 390 125 M 390 125 L 390 145" stroke="#0D9488" stroke-width="2"/>

    <!-- Master ColumnTransformer -->
    <g transform="translate(140, 145)">
      <rect width="500" height="48" rx="8" fill="#F0FDFA" stroke="#0D9488" stroke-width="2"/>
      <text x="250" y="20" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F766E" text-anchor="middle">Assemble into ColumnTransformer</text>
      <text x="250" y="36" font-family="monospace" font-size="10.5" fill="#115E59" text-anchor="middle">ColumnTransformer([ ('num', num_pipe), ('cat', cat_pipe) ])</text>
    </g>

    <!-- Final Pipeline Box -->
    <path d="M 390 193 L 390 205" stroke="#0D9488" stroke-width="2"/>
    <g transform="translate(200, 205)">
      <rect width="380" height="32" rx="6" fill="#0D9488" stroke="#0F766E"/>
      <text x="190" y="21" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Wrap into Pipeline(steps=[('pre', ct), ('clf', model)])</text>
    </g>
  </g>
</svg>
"""
