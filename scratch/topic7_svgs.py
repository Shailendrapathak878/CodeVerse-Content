"""
Module: topic7_svgs.py
Contains all 16 inline SVG diagrams for Topic 7: Feature Scaling & Normalization.
All SVGs are verified 100% XML-valid with ElementTree.
"""

import xml.etree.ElementTree as ET

# 1. Figure 7.1: Hero Overview - Multi-scale features entering scaling engine
SVG_HERO_SCALING_OVERVIEW = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 260" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <defs>
    <linearGradient id="grad-raw" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF" />
      <stop offset="100%" stop-color="#DBEAFE" />
    </linearGradient>
    <linearGradient id="grad-engine" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F46E5" />
      <stop offset="100%" stop-color="#3730A3" />
    </linearGradient>
    <linearGradient id="grad-scaled" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F0FDF4" />
      <stop offset="100%" stop-color="#DCFCE7" />
    </linearGradient>
    <filter id="shadow7" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Left: Raw Heterogeneous Features -->
  <g transform="translate(30, 25)" filter="url(#shadow7)">
    <rect width="250" height="210" rx="10" fill="url(#grad-raw)" stroke="#93C5FD" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="38" rx="10" fill="#3B82F6" />
    <text x="125" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">RAW HETEROGENEOUS SCALES</text>
    
    <!-- Feature 1: Age -->
    <rect x="18" y="52" width="214" height="42" rx="6" fill="#FFFFFF" stroke="#BFDBFE" />
    <text x="30" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1E3A8A">Age (years)</text>
    <text x="30" y="86" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Range: [18 – 65]</text>
    <rect x="150" y="66" width="70" height="14" rx="3" fill="#DBEAFE" />
    <rect x="150" y="66" width="35" height="14" rx="3" fill="#3B82F6" />
    <text x="185" y="77" text-anchor="middle" font-family="monospace" font-size="9" fill="#1E3A8A">mag ~ 10¹</text>

    <!-- Feature 2: Income -->
    <rect x="18" y="104" width="214" height="42" rx="6" fill="#FFFFFF" stroke="#BFDBFE" />
    <text x="30" y="122" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1E3A8A">Annual Income ($)</text>
    <text x="30" y="138" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626">Range: [30,000 – 850,000]</text>
    <rect x="150" y="118" width="70" height="14" rx="3" fill="#FEE2E2" />
    <rect x="150" y="118" width="65" height="14" rx="3" fill="#EF4444" />
    <text x="185" y="129" text-anchor="middle" font-family="monospace" font-size="9" fill="#991B1B">mag ~ 10⁵</text>

    <!-- Feature 3: Experience -->
    <rect x="18" y="156" width="214" height="42" rx="6" fill="#FFFFFF" stroke="#BFDBFE" />
    <text x="30" y="174" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1E3A8A">Purchases Count</text>
    <text x="30" y="190" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Range: [1 – 15]</text>
    <rect x="150" y="170" width="70" height="14" rx="3" fill="#DBEAFE" />
    <rect x="150" y="170" width="18" height="14" rx="3" fill="#3B82F6" />
    <text x="185" y="181" text-anchor="middle" font-family="monospace" font-size="9" fill="#1E3A8A">mag ~ 10⁰</text>
  </g>

  <!-- Middle: Scaling Engine -->
  <g transform="translate(330, 45)" filter="url(#shadow7)">
    <!-- Arrow input -->
    <path d="M-40, 85 L-10, 85" stroke="#6366F1" stroke-width="3" stroke-dasharray="4,4" />
    <polygon points="-10,80 -2,85 -10,90" fill="#6366F1" />

    <rect width="220" height="170" rx="14" fill="url(#grad-engine)" />
    <text x="110" y="32" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="15" font-weight="800" fill="#FFFFFF">FEATURE SCALING</text>
    <text x="110" y="50" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#C7D2FE">Mathematical Harmonizer</text>

    <!-- Formula pills inside engine -->
    <rect x="20" y="65" width="180" height="26" rx="6" fill="rgba(255,255,255,0.15)" />
    <text x="110" y="82" text-anchor="middle" font-family="monospace" font-size="11" fill="#FFFFFF">MinMax: (x - min) / span</text>

    <rect x="20" y="98" width="180" height="26" rx="6" fill="rgba(255,255,255,0.15)" />
    <text x="110" y="115" text-anchor="middle" font-family="monospace" font-size="11" fill="#FFFFFF">Standard: (x - μ) / σ</text>

    <rect x="20" y="131" width="180" height="26" rx="6" fill="rgba(255,255,255,0.15)" />
    <text x="110" y="148" text-anchor="middle" font-family="monospace" font-size="11" fill="#FFFFFF">Robust: (x - Med) / IQR</text>

    <!-- Arrow output -->
    <path d="M225, 85 L255, 85" stroke="#10B981" stroke-width="3" />
    <polygon points="255,80 263,85 255,90" fill="#10B981" />
  </g>

  <!-- Right: Normalized / Scaled Features -->
  <g transform="translate(600, 25)" filter="url(#shadow7)">
    <rect width="250" height="210" rx="10" fill="url(#grad-scaled)" stroke="#86EFAC" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="38" rx="10" fill="#10B981" />
    <text x="125" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">HARMONIZED NUMERICAL SCALE</text>

    <!-- Scaled 1 -->
    <rect x="18" y="52" width="214" height="42" rx="6" fill="#FFFFFF" stroke="#BBF7D0" />
    <text x="30" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">Scaled Age (z-score)</text>
    <text x="30" y="86" font-family="-apple-system, sans-serif" font-size="11" fill="#047857">Mean μ = 0, Std σ = 1</text>
    <rect x="150" y="66" width="70" height="14" rx="3" fill="#DCFCE7" />
    <rect x="150" y="66" width="38" height="14" rx="3" fill="#10B981" />
    <text x="185" y="77" text-anchor="middle" font-family="monospace" font-size="9" fill="#065F46">[-2, +2]</text>

    <!-- Scaled 2 -->
    <rect x="18" y="104" width="214" height="42" rx="6" fill="#FFFFFF" stroke="#BBF7D0" />
    <text x="30" y="122" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">Scaled Income (z-score)</text>
    <text x="30" y="138" font-family="-apple-system, sans-serif" font-size="11" fill="#047857">Equal Footing with Age!</text>
    <rect x="150" y="118" width="70" height="14" rx="3" fill="#DCFCE7" />
    <rect x="150" y="118" width="40" height="14" rx="3" fill="#10B981" />
    <text x="185" y="129" text-anchor="middle" font-family="monospace" font-size="9" fill="#065F46">[-2, +2]</text>

    <!-- Scaled 3 -->
    <rect x="18" y="156" width="214" height="42" rx="6" fill="#FFFFFF" stroke="#BBF7D0" />
    <text x="30" y="174" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">Scaled Purchases</text>
    <text x="30" y="190" font-family="-apple-system, sans-serif" font-size="11" fill="#047857">Balanced Influence!</text>
    <rect x="150" y="170" width="70" height="14" rx="3" fill="#DCFCE7" />
    <rect x="150" y="170" width="35" height="14" rx="3" fill="#10B981" />
    <text x="185" y="181" text-anchor="middle" font-family="monospace" font-size="9" fill="#065F46">[-2, +2]</text>
  </g>
</svg>'''

# 2. Figure 7.2: Why We Need Scaling - Euclidean Distance Domination
SVG_WHY_SCALE_DISTANCE_DOMINANCE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 290" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title banner -->
  <rect x="20" y="15" width="840" height="36" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <text x="440" y="38" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">HOW UNCALIBRATED SCALES DESTROY DISTANCE-BASED ALGORITHMS (KNN / K-MEANS)</text>

  <!-- Left: Unscaled Disaster Box -->
  <g transform="translate(30, 65)">
    <rect width="395" height="205" rx="10" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5" />
    <rect x="0" y="0" width="395" height="32" rx="10" fill="#EF4444" />
    <text x="197" y="21" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">WITHOUT SCALING: DISTANCE HIJACKED</text>

    <!-- Point A & B -->
    <text x="20" y="55" font-family="-apple-system, sans-serif" font-size="12" fill="#7F1D1D">Customer A: Age = 25, Income = $40,000</text>
    <text x="20" y="75" font-family="-apple-system, sans-serif" font-size="12" fill="#7F1D1D">Customer B: Age = 26, Income = $120,000 (Diff: 1 yr, $80k)</text>
    <text x="20" y="95" font-family="-apple-system, sans-serif" font-size="12" fill="#7F1D1D">Customer C: Age = 65, Income = $40,000 (Diff: 40 yrs, $0)</text>

    <!-- Distance calculation formula -->
    <rect x="15" y="110" width="365" height="42" rx="6" fill="#FFFFFF" stroke="#FCA5A5" />
    <text x="25" y="128" font-family="monospace" font-size="11" fill="#B91C1C">d(A, B) = √((26 - 25)² + (120000 - 40000)²)</text>
    <text x="25" y="144" font-family="monospace" font-size="11" fill="#B91C1C">d(A, B) = √(1 + 6,400,000,000) ≈ 80,000.0000</text>

    <text x="20" y="172" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">✕ Age contributes 0.00000001% of the distance!</text>
    <text x="20" y="190" font-family="-apple-system, sans-serif" font-size="11" fill="#991B1B">The algorithm behaves as if Age does not exist!</text>
  </g>

  <!-- Right: Standardized Balanced Box -->
  <g transform="translate(455, 65)">
    <rect width="395" height="205" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5" />
    <rect x="0" y="0" width="395" height="32" rx="10" fill="#10B981" />
    <text x="197" y="21" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">AFTER STANDARDIZATION: FAIR CONTRIBUTION</text>

    <!-- Standardized values -->
    <text x="20" y="55" font-family="-apple-system, sans-serif" font-size="12" fill="#065F46">Customer A: Age_std = -0.80, Inc_std = -0.50</text>
    <text x="20" y="75" font-family="-apple-system, sans-serif" font-size="12" fill="#065F46">Customer B: Age_std = -0.75, Inc_std = +1.50</text>
    <text x="20" y="95" font-family="-apple-system, sans-serif" font-size="12" fill="#065F46">Customer C: Age_std = +1.80, Inc_std = -0.50</text>

    <!-- Distance calculation formula -->
    <rect x="15" y="110" width="365" height="42" rx="6" fill="#FFFFFF" stroke="#86EFAC" />
    <text x="25" y="128" font-family="monospace" font-size="11" fill="#047857">d(A, B) = √((-0.75 - (-0.80))² + (1.50 - (-0.50))²)</text>
    <text x="25" y="144" font-family="monospace" font-size="11" fill="#047857">d(A, B) = √(0.05² + 2.00²) = √(0.0025 + 4.0) ≈ 2.0006</text>

    <text x="20" y="172" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#059669">✓ Age and Income both participate rationally!</text>
    <text x="20" y="190" font-family="-apple-system, sans-serif" font-size="11" fill="#065F46">KNN distance honors both domain dimensions proportionally.</text>
  </g>
</svg>'''

# 3. Figure 7.3: Box Plot Anatomy - Median, Quartiles, IQR, Outliers
SVG_STATISTICAL_SPREAD_ANATOMY = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 230" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">STATISTICAL SPREAD ANATOMY: THE FOUNDATION OF ROBUST SCALING</text>

  <!-- Number line axis -->
  <line x1="80" y1="130" x2="800" y2="130" stroke="#CBD5E1" stroke-width="2" />
  
  <!-- Whiskers -->
  <line x1="150" y1="130" x2="260" y2="130" stroke="#475569" stroke-width="2" />
  <line x1="560" y1="130" x2="680" y2="130" stroke="#475569" stroke-width="2" />
  <line x1="150" y1="105" x2="150" y2="155" stroke="#475569" stroke-width="2" />
  <line x1="680" y1="105" x2="680" y2="155" stroke="#475569" stroke-width="2" />

  <!-- IQR Box -->
  <rect x="260" y="85" width="300" height="90" rx="4" fill="#EEF2FF" stroke="#4F46E5" stroke-width="2" />
  
  <!-- Median Line -->
  <line x1="390" y1="85" x2="390" y2="175" stroke="#DC2626" stroke-width="3" />

  <!-- Outlier point -->
  <circle cx="760" cy="130" r="7" fill="#EF4444" stroke="#991B1B" stroke-width="1.5" />

  <!-- Labels -->
  <!-- Min / Whisker -->
  <text x="150" y="175" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#475569">Min (Non-outlier)</text>
  <text x="150" y="190" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748B">Q1 - 1.5✕IQR</text>

  <!-- Q1 -->
  <text x="260" y="70" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#4338CA">Q1 (25th %)</text>
  <text x="260" y="200" text-anchor="middle" font-family="monospace" font-size="11" fill="#4338CA">Q1 = 30</text>

  <!-- Median -->
  <text x="390" y="65" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#DC2626">Median / Q2 (50th %)</text>
  <text x="390" y="200" text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#DC2626">Median = 40 (Center)</text>

  <!-- Q3 -->
  <text x="560" y="70" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#4338CA">Q3 (75th %)</text>
  <text x="560" y="200" text-anchor="middle" font-family="monospace" font-size="11" fill="#4338CA">Q3 = 50</text>

  <!-- Whisker Max -->
  <text x="680" y="175" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#475569">Max (Non-outlier)</text>
  <text x="680" y="190" text-anchor="middle" font-family="monospace" font-size="10" fill="#64748B">Q3 + 1.5✕IQR</text>

  <!-- Outlier label -->
  <text x="760" y="112" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">Outlier (500)</text>

  <!-- IQR double arrow -->
  <line x1="265" y1="100" x2="555" y2="100" stroke="#4F46E5" stroke-width="1.5" />
  <polygon points="265,97 258,100 265,103" fill="#4F46E5" />
  <polygon points="555,97 562,100 555,103" fill="#4F46E5" />
  <text x="410" y="118" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4F46E5">IQR = Q3 - Q1 = 20 (Scale)</text>
</svg>'''

# 4. Figure 7.4: Standard Normal Curve & Z-Score Boundaries
SVG_Z_SCORE_NORMAL_BELL = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 260" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="25" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">THE STANDARD NORMAL DISTRIBUTION (μ = 0, σ = 1) AND EMPIRICAL Z-SCORES</text>

  <!-- Bell Curve Area -->
  <!-- 68% area (-1 to +1) -->
  <path d="M 320 200 C 350 185, 380 90, 440 60 C 500 90, 530 185, 560 200 Z" fill="#EEF2FF" />
  <!-- 95% area (-2 to +2) -->
  <path d="M 200 200 C 240 198, 280 195, 320 200 L 560 200 C 600 195, 640 198, 680 200 Z" fill="#E0E7FF" opacity="0.6" />

  <!-- Bell Curve Outline -->
  <path d="M 100 200 C 200 200, 260 195, 320 160 C 370 125, 400 60, 440 60 C 480 60, 510 125, 560 160 C 620 195, 680 200, 780 200" fill="none" stroke="#4F46E5" stroke-width="3" />

  <!-- Axis -->
  <line x1="80" y1="200" x2="800" y2="200" stroke="#334155" stroke-width="2" />

  <!-- Vertical tick lines at z = -3, -2, -1, 0, 1, 2, 3 -->
  <line x1="440" y1="60" x2="440" y2="208" stroke="#DC2626" stroke-width="2" stroke-dasharray="4,3" />
  <line x1="560" y1="160" x2="560" y2="208" stroke="#64748B" stroke-width="1.5" stroke-dasharray="3,3" />
  <line x1="320" y1="160" x2="320" y2="208" stroke="#64748B" stroke-width="1.5" stroke-dasharray="3,3" />
  <line x1="680" y1="195" x2="680" y2="208" stroke="#94A3B8" stroke-width="1" />
  <line x1="200" y1="195" x2="200" y2="208" stroke="#94A3B8" stroke-width="1" />

  <!-- Tick Labels (Z-scores) -->
  <text x="440" y="226" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">z = 0 (μ)</text>
  <text x="560" y="226" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#475569">z = +1σ</text>
  <text x="320" y="226" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#475569">z = -1σ</text>
  <text x="680" y="226" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B">z = +2σ</text>
  <text x="200" y="226" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B">z = -2σ</text>

  <!-- Area Percentages -->
  <rect x="390" y="125" width="100" height="22" rx="4" fill="#FFFFFF" stroke="#4F46E5" />
  <text x="440" y="140" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4F46E5">68.27% of Data</text>

  <rect x="365" y="80" width="150" height="20" rx="4" fill="#4338CA" />
  <text x="440" y="94" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">±2σ Encloses 95.45% of Data</text>

  <!-- Takeaway badge below -->
  <text x="440" y="250" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">StandardScaler centers data at zero and measures observations in standard deviation units.</text>
</svg>'''

# 5. Figure 7.5: Row-wise Vector Normalization vs Column-wise Feature Scaling
SVG_ROW_VS_COLUMN_OPERATIONS = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 270" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <rect x="20" y="12" width="840" height="34" rx="6" fill="#F8FAFC" stroke="#E2E8F0" />
  <text x="440" y="34" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">CRITICAL DISTINCTION: COLUMN-WISE SCALING VS ROW-WISE NORMALIZATION</text>

  <!-- Left: Column-wise Feature Scaling -->
  <g transform="translate(35, 58)">
    <rect width="380" height="195" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5" />
    <text x="190" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0369A1">COLUMN-WISE FEATURE SCALING</text>
    <text x="190" y="40" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#0284C7">StandardScaler / MinMaxScaler / RobustScaler</text>

    <!-- Mini Table Matrix -->
    <rect x="30" y="55" width="320" height="95" rx="4" fill="#FFFFFF" stroke="#CBD5E1" />
    <!-- Headers -->
    <rect x="30" y="55" width="80" height="22" fill="#E2E8F0" />
    <rect x="110" y="55" width="80" height="22" fill="#BAE6FD" />
    <rect x="190" y="55" width="80" height="22" fill="#E2E8F0" />
    <rect x="270" y="55" width="80" height="22" fill="#E2E8F0" />
    <text x="70" y="70" text-anchor="middle" font-family="monospace" font-size="10" fill="#334155">Age</text>
    <text x="150" y="70" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#0369A1">Income ↓</text>
    <text x="230" y="70" text-anchor="middle" font-family="monospace" font-size="10" fill="#334155">Exp</text>
    <text x="310" y="70" text-anchor="middle" font-family="monospace" font-size="10" fill="#334155">Score</text>

    <!-- Highlighted Column Arrow -->
    <rect x="110" y="77" width="80" height="73" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="3,2" />
    <text x="150" y="95" text-anchor="middle" font-family="monospace" font-size="10" fill="#0369A1">40,000</text>
    <text x="150" y="115" text-anchor="middle" font-family="monospace" font-size="10" fill="#0369A1">85,000</text>
    <text x="150" y="135" text-anchor="middle" font-family="monospace" font-size="10" fill="#0369A1">120,000</text>

    <text x="190" y="168" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0369A1">↓ Operates VERTICALLY across ALL samples</text>
    <text x="190" y="184" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#0C4A6E">Statistics (μ, σ, min, max) calculated per column.</text>
  </g>

  <!-- Right: Row-wise Vector Normalization -->
  <g transform="translate(465, 58)">
    <rect width="380" height="195" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5" />
    <text x="190" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#6B21A8">ROW-WISE VECTOR NORMALIZATION</text>
    <text x="190" y="40" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#7C3AED">sklearn.preprocessing.Normalizer (L1 / L2)</text>

    <!-- Mini Table Matrix -->
    <rect x="30" y="55" width="320" height="95" rx="4" fill="#FFFFFF" stroke="#CBD5E1" />
    <!-- Headers -->
    <rect x="30" y="55" width="320" height="22" fill="#E2E8F0" />
    <text x="70" y="70" text-anchor="middle" font-family="monospace" font-size="10" fill="#334155">Word_1</text>
    <text x="150" y="70" text-anchor="middle" font-family="monospace" font-size="10" fill="#334155">Word_2</text>
    <text x="230" y="70" text-anchor="middle" font-family="monospace" font-size="10" fill="#334155">Word_3</text>
    <text x="310" y="70" text-anchor="middle" font-family="monospace" font-size="10" fill="#334155">Word_4</text>

    <!-- Highlighted Row Arrow -->
    <rect x="30" y="100" width="320" height="26" fill="#F3E8FF" stroke="#7C3AED" stroke-width="1.5" stroke-dasharray="3,2" />
    <text x="70" y="117" text-anchor="middle" font-family="monospace" font-size="10" fill="#581C87">3.0</text>
    <text x="150" y="117" text-anchor="middle" font-family="monospace" font-size="10" fill="#581C87">4.0</text>
    <text x="230" y="117" text-anchor="middle" font-family="monospace" font-size="10" fill="#581C87">0.0</text>
    <text x="310" y="117" text-anchor="middle" font-family="monospace" font-size="10" fill="#581C87">0.0</text>
    <text x="360" y="117" font-family="monospace" font-size="11" font-weight="700" fill="#7C3AED">→ ||x||=1</text>

    <text x="190" y="168" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#6B21A8">→ Operates HORIZONTALLY across EACH sample</text>
    <text x="190" y="184" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#581C87">Scales each row to unit length (direction preserved).</text>
  </g>
</svg>'''

# 6. Graph 1: Original Feature Ranges (Age, Salary, Experience on original scales)
SVG_GRAPH_1_ORIGINAL_RANGES = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 280" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">GRAPH 1: ORIGINAL FEATURE RANGES ACROSS NUMERICAL FEATURES</text>

  <!-- 3 Separate Panels -->
  <!-- Panel A: Age -->
  <g transform="translate(30, 45)">
    <rect width="250" height="210" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <rect x="0" y="0" width="250" height="28" rx="8" fill="#3B82F6" />
    <text x="125" y="19" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">Age (Years)</text>
    
    <!-- Y Axis -->
    <line x1="45" y1="40" x2="45" y2="175" stroke="#94A3B8" stroke-width="1.5" />
    <line x1="40" y1="50" x2="45" y2="50" stroke="#94A3B8" />
    <text x="35" y="54" text-anchor="end" font-family="monospace" font-size="10" fill="#64748B">60</text>
    <line x1="40" y1="110" x2="45" y2="110" stroke="#94A3B8" />
    <text x="35" y="114" text-anchor="end" font-family="monospace" font-size="10" fill="#64748B">40</text>
    <line x1="40" y1="170" x2="45" y2="170" stroke="#94A3B8" />
    <text x="35" y="174" text-anchor="end" font-family="monospace" font-size="10" fill="#64748B">20</text>

    <!-- Range Bar -->
    <rect x="90" y="50" width="70" height="120" rx="4" fill="#DBEAFE" stroke="#3B82F6" stroke-width="2" />
    <text x="125" y="115" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E3A8A">Span: 38</text>
    <text x="125" y="195" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Range: [22 – 60]</text>
  </g>

  <!-- Panel B: Annual Income -->
  <g transform="translate(315, 45)">
    <rect width="250" height="210" rx="8" fill="#FEF2F2" stroke="#FECACA" />
    <rect x="0" y="0" width="250" height="28" rx="8" fill="#EF4444" />
    <text x="125" y="19" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">Annual Income ($)</text>

    <!-- Y Axis -->
    <line x1="55" y1="40" x2="55" y2="175" stroke="#94A3B8" stroke-width="1.5" />
    <line x1="50" y1="45" x2="55" y2="45" stroke="#94A3B8" />
    <text x="45" y="49" text-anchor="end" font-family="monospace" font-size="9" fill="#991B1B">850k</text>
    <line x1="50" y1="120" x2="55" y2="120" stroke="#94A3B8" />
    <text x="45" y="124" text-anchor="end" font-family="monospace" font-size="9" fill="#991B1B">100k</text>
    <line x1="50" y1="170" x2="55" y2="170" stroke="#94A3B8" />
    <text x="45" y="174" text-anchor="end" font-family="monospace" font-size="9" fill="#991B1B">30k</text>

    <!-- Range Bar -->
    <rect x="90" y="45" width="70" height="125" rx="4" fill="#FEE2E2" stroke="#EF4444" stroke-width="2" />
    <text x="125" y="105" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B">Span: 818,000</text>
    <text x="125" y="125" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#B91C1C">(21,500✕ Age!)</text>
    <text x="125" y="195" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#7F1D1D">Range: [32k – 850k]</text>
  </g>

  <!-- Panel C: Experience -->
  <g transform="translate(600, 45)">
    <rect width="250" height="210" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <rect x="0" y="0" width="250" height="28" rx="8" fill="#10B981" />
    <text x="125" y="19" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">Experience (Years)</text>

    <!-- Y Axis -->
    <line x1="45" y1="40" x2="45" y2="175" stroke="#94A3B8" stroke-width="1.5" />
    <line x1="40" y1="50" x2="45" y2="50" stroke="#94A3B8" />
    <text x="35" y="54" text-anchor="end" font-family="monospace" font-size="10" fill="#64748B">30</text>
    <line x1="40" y1="110" x2="45" y2="110" stroke="#94A3B8" />
    <text x="35" y="114" text-anchor="end" font-family="monospace" font-size="10" fill="#64748B">15</text>
    <line x1="40" y1="170" x2="45" y2="170" stroke="#94A3B8" />
    <text x="35" y="174" text-anchor="end" font-family="monospace" font-size="10" fill="#64748B">1</text>

    <!-- Range Bar -->
    <rect x="90" y="50" width="70" height="120" rx="4" fill="#DCFCE7" stroke="#10B981" stroke-width="2" />
    <text x="125" y="115" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">Span: 29</text>
    <text x="125" y="195" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Range: [1 – 30]</text>
  </g>
</svg>'''

# 7. Graph 2: Min-Max Scaling Before and After
SVG_GRAPH_2_MINMAX_BEFORE_AFTER = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 250" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">GRAPH 2: MIN-MAX SCALING TRANSFORMATION: BOUNDING TO [0, 1]</text>

  <!-- Left: Raw Input Axis [10, 20, 30] -->
  <g transform="translate(60, 50)">
    <text x="160" y="20" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#1E3A8A">ORIGINAL VALUES: X ∈ [10, 30]</text>
    <line x1="30" y1="80" x2="290" y2="80" stroke="#3B82F6" stroke-width="3" />

    <!-- Points on original axis -->
    <circle cx="50" cy="80" r="7" fill="#1D4ED8" />
    <text x="50" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#1E3A8A">x = 10 (min)</text>

    <circle cx="160" cy="80" r="7" fill="#1D4ED8" />
    <text x="160" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#1E3A8A">x = 20</text>

    <circle cx="270" cy="80" r="7" fill="#1D4ED8" />
    <text x="270" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#1E3A8A">x = 30 (max)</text>

    <text x="160" y="145" text-anchor="middle" font-family="monospace" font-size="11" fill="#475569">Formula: x' = (x - 10) / (30 - 10)</text>
  </g>

  <!-- Mapping Arrows in Middle -->
  <g transform="translate(400, 75)">
    <path d="M-10, 35 L50, 35" stroke="#4F46E5" stroke-width="2.5" />
    <polygon points="50,30 60,35 50,40" fill="#4F46E5" />
    <text x="25" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4F46E5">MinMaxScaler</text>
  </g>

  <!-- Right: Scaled Output Axis [0.0, 0.5, 1.0] + Unseen [1.5] -->
  <g transform="translate(500, 50)">
    <text x="160" y="20" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#065F46">TRANSFORMED VALUES: X' ∈ [0, 1]</text>
    <line x1="30" y1="80" x2="310" y2="80" stroke="#10B981" stroke-width="3" />

    <!-- Points on scaled axis -->
    <circle cx="50" cy="80" r="7" fill="#047857" />
    <text x="50" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#065F46">x' = 0.0</text>

    <circle cx="160" cy="80" r="7" fill="#047857" />
    <text x="160" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#065F46">x' = 0.5</text>

    <circle cx="270" cy="80" r="7" fill="#047857" />
    <text x="270" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#065F46">x' = 1.0</text>

    <!-- Outlier / Unseen Point 40 -->
    <circle cx="340" cy="80" r="6" fill="#EF4444" stroke="#991B1B" />
    <text x="340" y="110" text-anchor="middle" font-family="monospace" font-size="11" font-weight="700" fill="#DC2626">x' = 1.5</text>
    <text x="340" y="125" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#991B1B">(Unseen 40)</text>

    <text x="160" y="150" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#047857">✓ Relative spacing preserved: 0.5 is exactly midway.</text>
  </g>
</svg>'''

# 8. Graph 3: Standardization Before and After
SVG_GRAPH_3_STANDARDIZATION_BEFORE_AFTER = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 250" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">GRAPH 3: STANDARDIZATION (Z-SCORE) TRANSFORMATION: μ = 0, σ = 1</text>

  <!-- Left: Raw Input (Mean = 20, Std = 8.165) -->
  <g transform="translate(60, 50)">
    <text x="160" y="20" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#1E3A8A">ORIGINAL: μ = 20.0, σ = 8.165</text>
    <line x1="30" y1="80" x2="290" y2="80" stroke="#3B82F6" stroke-width="3" />

    <circle cx="50" cy="80" r="7" fill="#1D4ED8" />
    <text x="50" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#1E3A8A">x = 10</text>

    <circle cx="160" cy="80" r="7" fill="#DC2626" />
    <text x="160" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#DC2626">x = 20 (μ)</text>

    <circle cx="270" cy="80" r="7" fill="#1D4ED8" />
    <text x="270" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#1E3A8A">x = 30</text>

    <text x="160" y="145" text-anchor="middle" font-family="monospace" font-size="11" fill="#475569">z = (x - 20) / 8.165</text>
  </g>

  <!-- Mapping Arrow -->
  <g transform="translate(400, 75)">
    <path d="M-10, 35 L50, 35" stroke="#4F46E5" stroke-width="2.5" />
    <polygon points="50,30 60,35 50,40" fill="#4F46E5" />
    <text x="25" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4F46E5">StandardScaler</text>
  </g>

  <!-- Right: Standardized Output (Z = -1.225, 0, +1.225) -->
  <g transform="translate(500, 50)">
    <text x="160" y="20" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#065F46">STANDARDIZED: μ = 0.0, σ = 1.0</text>
    <line x1="30" y1="80" x2="290" y2="80" stroke="#10B981" stroke-width="3" />

    <circle cx="50" cy="80" r="7" fill="#047857" />
    <text x="50" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#065F46">z = -1.225</text>
    <text x="50" y="125" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">(below mean)</text>

    <circle cx="160" cy="80" r="7" fill="#DC2626" />
    <text x="160" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#DC2626">z = 0.000</text>
    <text x="160" y="125" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#DC2626">(exact mean)</text>

    <circle cx="270" cy="80" r="7" fill="#047857" />
    <text x="270" y="110" text-anchor="middle" font-family="monospace" font-size="12" font-weight="700" fill="#065F46">z = +1.225</text>
    <text x="270" y="125" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">(above mean)</text>

    <text x="160" y="150" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#047857">✓ Symmetric about zero with standard deviation equal to 1.</text>
  </g>
</svg>'''

# 9. Graph 4: Outlier Impact Comparison (MinMax vs StandardScaler vs RobustScaler)
SVG_GRAPH_4_OUTLIER_IMPACT = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 290" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="22" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">GRAPH 4: OUTLIER RESISTANCE COMPARISON ACROSS 3 SCALERS</text>
  <text x="440" y="38" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Dataset: [20, 25, 30, 35, 40, 45, 50, 55] + Extreme Outlier [500]</text>

  <!-- 3 Rows: MinMax, StandardScaler, RobustScaler -->
  <!-- Row 1: MinMaxScaler (Crushed!) -->
  <g transform="translate(40, 52)">
    <rect width="800" height="60" rx="6" fill="#FEF2F2" stroke="#FECACA" />
    <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">1. MinMaxScaler: CRUSHED DATA</text>
    <text x="18" y="44" font-family="-apple-system, sans-serif" font-size="10" fill="#991B1B">Span = 480. Points [20..55] squeezed into [0.00, 0.07]! 93% of space wasted!</text>
    
    <!-- Mini line -->
    <line x1="380" y1="30" x2="770" y2="30" stroke="#CBD5E1" stroke-width="2" />
    <!-- Crushed clump -->
    <rect x="380" y="22" width="28" height="16" rx="3" fill="#EF4444" opacity="0.8" />
    <text x="394" y="50" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#B91C1C">[0.0 – 0.07]</text>
    <!-- Outlier at far right -->
    <circle cx="770" cy="30" r="6" fill="#DC2626" />
    <text x="770" y="50" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#DC2626">1.0 (500)</text>
  </g>

  <!-- Row 2: StandardScaler (Distorted Mean & Variance) -->
  <g transform="translate(40, 122)">
    <rect width="800" height="60" rx="6" fill="#FFFBEB" stroke="#FDE68A" />
    <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#D97706">2. StandardScaler: SKEWED SPREAD</text>
    <text x="18" y="44" font-family="-apple-system, sans-serif" font-size="10" fill="#92400E">Mean pulled up to 88.9 by single outlier. Regular points have negative z-scores (-0.46 to -0.23).</text>

    <!-- Mini line -->
    <line x1="380" y1="30" x2="770" y2="30" stroke="#CBD5E1" stroke-width="2" />
    <!-- Regular clump -->
    <rect x="420" y="22" width="40" height="16" rx="3" fill="#F59E0B" opacity="0.8" />
    <text x="440" y="50" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#B45309">[-0.46, -0.23]</text>
    <!-- Outlier at +2.8z -->
    <circle cx="740" cy="30" r="6" fill="#D97706" />
    <text x="740" y="50" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#D97706">+2.81z</text>
  </g>

  <!-- Row 3: RobustScaler (Winner!) -->
  <g transform="translate(40, 192)">
    <rect width="800" height="70" rx="6" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5" />
    <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#16A34A">3. RobustScaler: FULL RESOLUTION PRESERVED (✓ WINNER)</text>
    <text x="18" y="42" font-family="-apple-system, sans-serif" font-size="10" fill="#166534">Median = 40, IQR = 20. Regular points cleanly mapped across [-1.00, +0.75].</text>
    <text x="18" y="56" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#047857">The outlier 500 becomes +23.0 without compressing the inliers!</text>

    <!-- Mini line -->
    <line x1="380" y1="35" x2="770" y2="35" stroke="#CBD5E1" stroke-width="2" />
    <!-- Robust spread: healthy wide band -->
    <rect x="400" y="25" width="160" height="20" rx="4" fill="#10B981" opacity="0.85" />
    <text x="480" y="39" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#FFFFFF">[-1.00 – +0.75] (High Detail)</text>
    <!-- Outlier -->
    <circle cx="750" cy="35" r="6" fill="#10B981" stroke="#065F46" />
    <text x="750" y="55" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#065F46">+23.00</text>
  </g>
</svg>'''

# 10. Graph 5: Original vs Scaled Distributions (Preserving Distribution Shape)
SVG_GRAPH_5_DISTRIBUTION_PRESERVATION = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 250" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">GRAPH 5: DISTRIBUTION SHAPE PRESERVATION UNDER LINEAR SCALING</text>

  <!-- Left: Original Bimodal / Skewed Distribution -->
  <g transform="translate(60, 45)">
    <rect width="340" height="180" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
    <text x="170" y="22" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1E3A8A">ORIGINAL FEATURE DISTRIBUTION</text>

    <!-- Skewed histogram bars -->
    <rect x="40" y="120" width="30" height="30" fill="#93C5FD" stroke="#3B82F6" />
    <rect x="75" y="80" width="30" height="70" fill="#60A5FA" stroke="#3B82F6" />
    <rect x="110" y="50" width="30" height="100" fill="#3B82F6" stroke="#1D4ED8" />
    <rect x="145" y="90" width="30" height="60" fill="#60A5FA" stroke="#3B82F6" />
    <rect x="180" y="115" width="30" height="35" fill="#93C5FD" stroke="#3B82F6" />
    <rect x="215" y="135" width="30" height="15" fill="#BFDBFE" stroke="#3B82F6" />

    <line x1="30" y1="150" x2="260" y2="150" stroke="#475569" stroke-width="1.5" />
    <text x="40" y="165" font-family="monospace" font-size="9" fill="#64748B">$30k</text>
    <text x="125" y="165" font-family="monospace" font-size="9" fill="#64748B">$70k</text>
    <text x="230" y="165" font-family="monospace" font-size="9" fill="#64748B">$120k</text>
  </g>

  <!-- Equality Arrow in Middle -->
  <g transform="translate(425, 100)">
    <text x="15" y="0" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="20" font-weight="800" fill="#4F46E5">⇔</text>
    <text x="15" y="22" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4F46E5">Exact Shape</text>
    <text x="15" y="34" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#6366F1">Preserved</text>
  </g>

  <!-- Right: Standardized Distribution (Identical relative heights!) -->
  <g transform="translate(480, 45)">
    <rect width="340" height="180" rx="8" fill="#F0FDF4" stroke="#BBF7D0" />
    <text x="170" y="22" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">STANDARDIZED DISTRIBUTION (Z-SCORE)</text>

    <!-- Identical shape bars, rescaled axis -->
    <rect x="40" y="120" width="30" height="30" fill="#86EFAC" stroke="#10B981" />
    <rect x="75" y="80" width="30" height="70" fill="#4ADE80" stroke="#10B981" />
    <rect x="110" y="50" width="30" height="100" fill="#10B981" stroke="#047857" />
    <rect x="145" y="90" width="30" height="60" fill="#4ADE80" stroke="#10B981" />
    <rect x="180" y="115" width="30" height="35" fill="#86EFAC" stroke="#10B981" />
    <rect x="215" y="135" width="30" height="15" fill="#BBF7D0" stroke="#10B981" />

    <line x1="30" y1="150" x2="260" y2="150" stroke="#475569" stroke-width="1.5" />
    <text x="40" y="165" font-family="monospace" font-size="9" fill="#065F46">-1.8z</text>
    <text x="125" y="165" font-family="monospace" font-size="9" font-weight="700" fill="#DC2626">0.0z (μ)</text>
    <text x="230" y="165" font-family="monospace" font-size="9" fill="#065F46">+2.1z</text>
  </g>
</svg>'''

# 11. Graph 6: Vector Normalization (2D vector, direction preserved, unit circle)
SVG_GRAPH_6_VECTOR_NORMALIZATION = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 270" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">GRAPH 6: L2 VECTOR NORMALIZATION ON 2D CARTESIAN PLANE</text>
  <text x="440" y="40" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">Sample Vector v = [3, 4] with ||v||₂ = 5.0 projected to Unit Circle: v' = [0.6, 0.8]</text>

  <!-- Left Plane: Coordinate Visualization -->
  <g transform="translate(100, 55)">
    <!-- Axes -->
    <line x1="40" y1="180" x2="260" y2="180" stroke="#94A3B8" stroke-width="1.5" />
    <line x1="40" y1="180" x2="40" y2="20" stroke="#94A3B8" stroke-width="1.5" />
    <text x="255" y="195" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">x₁</text>
    <text x="25" y="25" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">x₂</text>

    <!-- Unit Circle Arc (radius = 35px) -->
    <path d="M 40 145 A 35 35 0 0 1 75 180" fill="none" stroke="#10B981" stroke-width="2" stroke-dasharray="3,3" />
    <text x="82" y="170" font-family="monospace" font-size="9" fill="#059669">r = 1.0 (Unit Circle)</text>

    <!-- Original Vector v = [3, 4] -> px = 40 + 3*35 = 145, py = 180 - 4*35 = 40 -->
    <!-- Length = 5 * 35 = 175px -->
    <line x1="40" y1="180" x2="145" y2="40" stroke="#3B82F6" stroke-width="3" />
    <circle cx="145" cy="40" r="5" fill="#1D4ED8" />
    <text x="155" y="42" font-family="monospace" font-size="11" font-weight="700" fill="#1E3A8A">v = [3, 4]</text>
    <text x="155" y="55" font-family="-apple-system, sans-serif" font-size="10" fill="#3B82F6">Length ||v||₂ = 5.0</text>

    <!-- Normalized Vector v' = [0.6, 0.8] -> px = 40 + 0.6*35 = 61, py = 180 - 0.8*35 = 152 -->
    <line x1="40" y1="180" x2="61" y2="152" stroke="#10B981" stroke-width="4" />
    <circle cx="61" cy="152" r="5" fill="#047857" />
    <text x="70" y="145" font-family="monospace" font-size="11" font-weight="700" fill="#065F46">v' = [0.6, 0.8]</text>
    <text x="70" y="157" font-family="-apple-system, sans-serif" font-size="9" fill="#047857">||v'||₂ = 1.000</text>

    <!-- Angle theta -->
    <path d="M 60 180 A 20 20 0 0 0 54 162" fill="none" stroke="#DC2626" stroke-width="1.5" />
    <text x="68" y="174" font-family="monospace" font-size="10" fill="#DC2626">θ = 53.1°</text>
  </g>

  <!-- Right Explanation Card -->
  <g transform="translate(480, 55)">
    <rect width="340" height="190" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="20" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#1E293B">Mathematical Verification:</text>
    
    <text x="20" y="52" font-family="monospace" font-size="11" fill="#334155">1. Norm: ||v||₂ = √(3² + 4²) = √25 = 5.0</text>
    <text x="20" y="76" font-family="monospace" font-size="11" fill="#334155">2. Divide: [3/5, 4/5] = [0.60, 0.80]</text>
    <text x="20" y="100" font-family="monospace" font-size="11" fill="#059669">3. Check: √(0.6² + 0.8²) = √(0.36 + 0.64) = 1.0</text>
    <text x="20" y="124" font-family="monospace" font-size="11" fill="#0369A1">4. Direction: tan(θ) = 4/3 = 0.8/0.6 = 1.333</text>

    <rect x="15" y="142" width="310" height="36" rx="4" fill="#ECFDF5" stroke="#A7F3D0" />
    <text x="25" y="160" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">✓ Key Takeaway:</text>
    <text x="25" y="172" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">Direction is unchanged; only magnitude is scaled to 1.0.</text>
  </g>
</svg>'''

# 12. Graph 7: L1 vs L2 Normalization (Diamond vs Circle constraint)
SVG_GRAPH_7_L1_VS_L2_NORM = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 260" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">GRAPH 7: L1 (MANHATTAN) VS L2 (EUCLIDEAN) UNIT CONSTRAINTS</text>

  <!-- Left: L1 Normalization (Diamond Constraint |x| + |y| = 1) -->
  <g transform="translate(80, 45)">
    <rect width="320" height="200" rx="8" fill="#FDF4FF" stroke="#F5D0FE" />
    <text x="160" y="22" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#86198F">L1 NORMALIZATION (DIAMOND CONTOUR)</text>

    <!-- Axes -->
    <line x1="60" y1="110" x2="260" y2="110" stroke="#CBD5E1" stroke-width="1.5" />
    <line x1="160" y1="20" x2="160" y2="190" stroke="#CBD5E1" stroke-width="1.5" />

    <!-- L1 Diamond: vertices at (160, 40), (230, 110), (160, 180), (90, 110) -->
    <polygon points="160,40 230,110 160,180 90,110" fill="#FAE8FF" stroke="#C026D3" stroke-width="2.5" />
    
    <!-- Vector [3, 4] -> normalized [3/7, 4/7] approx [0.43, 0.57] -->
    <!-- Point = (160 + 0.43*70 = 190, 110 - 0.57*70 = 70) -->
    <circle cx="190" cy="70" r="5" fill="#86198F" />
    <text x="198" y="68" font-family="monospace" font-size="10" font-weight="700" fill="#86198F">[3/7, 4/7]</text>

    <text x="160" y="160" text-anchor="middle" font-family="monospace" font-size="10" fill="#701A75">||v||₁ = |3| + |4| = 7</text>
    <text x="160" y="175" text-anchor="middle" font-family="monospace" font-size="10" fill="#701A75">|3/7| + |4/7| = 1.0 (Unit Sum)</text>
    <text x="160" y="192" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#A21CAF">Useful for probability distributions &amp; TF-IDF</text>
  </g>

  <!-- Right: L2 Normalization (Circle Constraint x² + y² = 1) -->
  <g transform="translate(480, 45)">
    <rect width="320" height="200" rx="8" fill="#F0FDF4" stroke="#BBF7D0" />
    <text x="160" y="22" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">L2 NORMALIZATION (SPHERICAL CIRCLE)</text>

    <!-- Axes -->
    <line x1="60" y1="110" x2="260" y2="110" stroke="#CBD5E1" stroke-width="1.5" />
    <line x1="160" y1="20" x2="160" y2="190" stroke="#CBD5E1" stroke-width="1.5" />

    <!-- L2 Circle: radius = 70px -->
    <circle cx="160" cy="110" r="70" fill="#DCFCE7" stroke="#10B981" stroke-width="2.5" />

    <!-- Vector [3, 4] -> normalized [0.6, 0.8] -->
    <!-- Point = (160 + 0.6*70 = 202, 110 - 0.8*70 = 54) -->
    <circle cx="202" cy="54" r="5" fill="#047857" />
    <text x="210" y="52" font-family="monospace" font-size="10" font-weight="700" fill="#065F46">[0.60, 0.80]</text>

    <text x="160" y="160" text-anchor="middle" font-family="monospace" font-size="10" fill="#065F46">||v||₂ = √(3² + 4²) = 5.0</text>
    <text x="160" y="175" text-anchor="middle" font-family="monospace" font-size="10" fill="#065F46">0.6² + 0.8² = 1.0 (Unit Euclidean)</text>
    <text x="160" y="192" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#047857">Ideal for Cosine Similarity &amp; Embeddings</text>
  </g>
</svg>'''

# 13. Graph 8: Algorithm Sensitivity Matrix / Comparison
SVG_GRAPH_8_ALGORITHM_SENSITIVITY = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 270" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">GRAPH 8: MACHINE LEARNING ALGORITHM SENSITIVITY TO FEATURE SCALE</text>

  <!-- 3 Groups: Highly Sensitive (Red), Moderately Sensitive (Amber), Scale Invariant (Green) -->
  <!-- Group 1: Highly Sensitive -->
  <g transform="translate(30, 45)">
    <rect width="250" height="210" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="30" rx="8" fill="#EF4444" />
    <text x="125" y="20" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">✕ HIGHLY SENSITIVE (MANDATORY)</text>

    <text x="18" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#991B1B">• K-Nearest Neighbors (KNN)</text>
    <text x="28" y="70" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D">Euclidean distance dominated by largest scale.</text>

    <text x="18" y="95" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#991B1B">• K-Means Clustering</text>
    <text x="28" y="110" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D">Cluster centroids distort along large variance axes.</text>

    <text x="18" y="135" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#991B1B">• Support Vector Machines (SVM)</text>
    <text x="28" y="150" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D">RBF kernel bandwidth and margin collapse.</text>

    <text x="18" y="175" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#991B1B">• Principal Component Analysis (PCA)</text>
    <text x="28" y="190" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D">Max variance direction aligns with raw scale.</text>
  </g>

  <!-- Group 2: Moderately Sensitive -->
  <g transform="translate(315, 45)">
    <rect width="250" height="210" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="30" rx="8" fill="#F59E0B" />
    <text x="125" y="20" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">! MODERATELY SENSITIVE</text>

    <text x="18" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#92400E">• Regularized Linear (Ridge / Lasso)</text>
    <text x="28" y="70" font-family="-apple-system, sans-serif" font-size="10" fill="#78350F">L1/L2 penalties penalize large scale weights unfairly.</text>

    <text x="18" y="100" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#92400E">• Logistic Regression</text>
    <text x="28" y="115" font-family="-apple-system, sans-serif" font-size="10" fill="#78350F">Gradient descent converges much faster with scaling.</text>

    <text x="18" y="145" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#92400E">• Deep Neural Networks (MLP / CNN)</text>
    <text x="28" y="160" font-family="-apple-system, sans-serif" font-size="10" fill="#78350F">Prevents vanishing / exploding gradients.</text>
    <text x="28" y="175" font-family="-apple-system, sans-serif" font-size="10" fill="#78350F">Accelerates backpropagation optimizer.</text>
  </g>

  <!-- Group 3: Scale Invariant -->
  <g transform="translate(600, 45)">
    <rect width="250" height="210" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="30" rx="8" fill="#10B981" />
    <text x="125" y="20" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">✓ SCALE INVARIANT (TREE MODELS)</text>

    <text x="18" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">• Decision Trees (CART / ID3)</text>
    <text x="28" y="70" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">Splits on ordering (X &gt; threshold), not distance.</text>

    <text x="18" y="100" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">• Random Forests</text>
    <text x="28" y="115" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">Monotonic scaling does not change optimal cutpoints.</text>

    <text x="18" y="145" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">• Gradient Boosted Trees (XGB / LGBM)</text>
    <text x="28" y="160" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">Works directly on raw unscaled numerical values.</text>
    <text x="28" y="175" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">Scaling neither helps nor hurts tree splits.</text>
  </g>
</svg>'''

# 14. Graph 9: Feature Scaling Decision Flowchart
SVG_GRAPH_9_DECISION_FLOWCHART = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 320" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">GRAPH 9: PRACTICAL FEATURE SCALING DECISION FLOWCHART</text>

  <!-- Node 1: Start -->
  <rect x="360" y="42" width="160" height="34" rx="17" fill="#4F46E5" />
  <text x="440" y="63" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">Numerical Feature X</text>

  <!-- Arrow down -->
  <line x1="440" y1="76" x2="440" y2="98" stroke="#64748B" stroke-width="2" />
  <polygon points="440,98 436,92 444,92" fill="#64748B" />

  <!-- Decision 1: Tree model only? -->
  <rect x="330" y="98" width="220" height="38" rx="6" fill="#EEF2FF" stroke="#6366F1" stroke-width="1.5" />
  <text x="440" y="115" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#312E81">Using Tree-based Model ONLY?</text>
  <text x="440" y="128" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#4338CA">(Random Forest, XGBoost, Decision Tree)</text>

  <!-- Yes -> No scaling needed -->
  <line x1="550" y1="117" x2="680" y2="117" stroke="#10B981" stroke-width="2" />
  <polygon points="680,117 674,113 674,121" fill="#10B981" />
  <text x="610" y="110" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#047857">YES →</text>
  <rect x="680" y="99" width="170" height="36" rx="6" fill="#F0FDF4" stroke="#10B981" />
  <text x="765" y="116" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">NO SCALING NEEDED</text>
  <text x="765" y="129" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#047857">Trees split on rank order</text>

  <!-- No -> Distance/Gradient based -->
  <line x1="440" y1="136" x2="440" y2="160" stroke="#64748B" stroke-width="2" />
  <polygon points="440,160 436,154 444,154" fill="#64748B" />
  <text x="450" y="152" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#475569">NO</text>

  <!-- Decision 2: Extreme Outliers? -->
  <rect x="330" y="160" width="220" height="38" rx="6" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5" />
  <text x="440" y="177" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#78350F">Severe Outliers Present?</text>
  <text x="440" y="190" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#92400E">(Heavy tails / extreme income / spikes)</text>

  <!-- Yes -> RobustScaler -->
  <line x1="330" y1="179" x2="200" y2="179" stroke="#D97706" stroke-width="2" />
  <polygon points="200,179 206,175 206,183" fill="#D97706" />
  <text x="250" y="172" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#B45309">← YES</text>
  <rect x="30" y="161" width="170" height="36" rx="6" fill="#FFFBEB" stroke="#D97706" />
  <text x="115" y="178" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#92400E">ROBUSTSCALER</text>
  <text x="115" y="191" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#B45309">Uses Median &amp; IQR</text>

  <!-- No -> Next Decision -->
  <line x1="440" y1="198" x2="440" y2="222" stroke="#64748B" stroke-width="2" />
  <polygon points="440,222 436,216 444,216" fill="#64748B" />
  <text x="450" y="214" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#475569">NO</text>

  <!-- Decision 3: Fixed Bound [0, 1] Needed? -->
  <rect x="320" y="222" width="240" height="38" rx="6" fill="#F0F9FF" stroke="#0284C7" stroke-width="1.5" />
  <text x="440" y="238" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0369A1">Strict Bounded Range [0, 1] Required?</text>
  <text x="440" y="251" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#0284C7">(Image pixels, Neural activation inputs, Sigmoid)</text>

  <!-- Yes -> MinMaxScaler -->
  <line x1="320" y1="241" x2="200" y2="241" stroke="#0284C7" stroke-width="2" />
  <polygon points="200,241 206,237 206,245" fill="#0284C7" />
  <text x="245" y="234" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0369A1">← YES</text>
  <rect x="30" y="223" width="170" height="36" rx="6" fill="#F0F9FF" stroke="#0284C7" />
  <text x="115" y="240" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0369A1">MINMAXSCALER</text>
  <text x="115" y="253" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#0284C7">Bounds to exact [0, 1]</text>

  <!-- No -> StandardScaler -->
  <line x1="560" y1="241" x2="680" y2="241" stroke="#4F46E5" stroke-width="2" />
  <polygon points="680,241 674,237 674,245" fill="#4F46E5" />
  <text x="605" y="234" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4338CA">NO (DEFAULT) →</text>
  <rect x="680" y="223" width="170" height="36" rx="6" fill="#EEF2FF" stroke="#4F46E5" />
  <text x="765" y="240" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#312E81">STANDARDSCALER</text>
  <text x="765" y="253" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#4338CA">Centers at 0, unit variance</text>

  <!-- Bottom Caution Banner -->
  <rect x="30" y="278" width="820" height="30" rx="6" fill="#FEF2F2" stroke="#FCA5A5" />
  <text x="440" y="297" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">■ MANDATORY MLOPS RULE: Always fit scalers on X_train ONLY! Never call fit() on full dataset or X_test!</text>
</svg>'''

# 15. Figure 7.6: Data Leakage Workflow Architecture
SVG_LEAKAGE_WORKFLOW_ARCHITECTURE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 270" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <rect x="20" y="10" width="840" height="32" rx="6" fill="#F8FAFC" stroke="#E2E8F0" />
  <text x="440" y="31" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#1E293B">PRODUCTION PIPELINE ARCHITECTURE: PREVENTING PREPROCESSING DATA LEAKAGE</text>

  <!-- Top Bad Practice -->
  <g transform="translate(30, 52)">
    <rect width="820" height="85" rx="8" fill="#FEF2F2" stroke="#FECACA" />
    <text x="20" y="22" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">✕ THE DATA LEAKAGE DISASTER (FIT BEFORE SPLIT):</text>

    <!-- Box 1 -->
    <rect x="20" y="34" width="210" height="38" rx="6" fill="#FFFFFF" stroke="#FCA5A5" />
    <text x="125" y="50" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B">Full Raw Dataset</text>
    <text x="125" y="64" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#B91C1C">Scaler.fit_transform(X_all)</text>

    <!-- Arrow -->
    <path d="M235, 53 L265, 53" stroke="#DC2626" stroke-width="2" />
    <polygon points="265,49 273,53 265,57" fill="#DC2626" />

    <!-- Box 2 -->
    <rect x="275" y="34" width="250" height="38" rx="6" fill="#FFFFFF" stroke="#FCA5A5" />
    <text x="400" y="50" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B">train_test_split(X_scaled)</text>
    <text x="400" y="64" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#B91C1C">Test μ and σ leaked into training!</text>

    <!-- Arrow -->
    <path d="M530, 53 L560, 53" stroke="#DC2626" stroke-width="2" />
    <polygon points="560,49 568,53 560,57" fill="#DC2626" />

    <!-- Box 3 -->
    <rect x="570" y="34" width="230" height="38" rx="6" fill="#FEE2E2" stroke="#DC2626" />
    <text x="685" y="50" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B">Overly Optimistic Validation</text>
    <text x="685" y="64" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D">FAILS silently in Production!</text>
  </g>

  <!-- Bottom Good Practice -->
  <g transform="translate(30, 150)">
    <rect width="820" height="105" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5" />
    <text x="20" y="22" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#16A34A">✓ THE PRODUCTION STANDARD (LEAKAGE-SAFE PIPELINE):</text>

    <!-- Step 1 -->
    <rect x="20" y="34" width="180" height="55" rx="6" fill="#FFFFFF" stroke="#86EFAC" />
    <text x="110" y="52" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">1. Split FIRST</text>
    <text x="110" y="68" text-anchor="middle" font-family="monospace" font-size="10" fill="#047857">train_test_split()</text>
    <text x="110" y="80" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#047857">X_train vs X_test</text>

    <!-- Arrow -->
    <path d="M205, 60 L235, 60" stroke="#10B981" stroke-width="2" />
    <polygon points="235,56 243,60 235,64" fill="#10B981" />

    <!-- Step 2 -->
    <rect x="245" y="34" width="260" height="55" rx="6" fill="#FFFFFF" stroke="#86EFAC" />
    <text x="375" y="52" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">2. Pipeline.fit(X_train)</text>
    <text x="375" y="68" text-anchor="middle" font-family="monospace" font-size="10" fill="#047857">scaler.fit(X_train)</text>
    <text x="375" y="80" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#047857">Learns μ_train &amp; σ_train only!</text>

    <!-- Arrow -->
    <path d="M510, 60 L540, 60" stroke="#10B981" stroke-width="2" />
    <polygon points="540,56 548,60 540,64" fill="#10B981" />

    <!-- Step 3 -->
    <rect x="550" y="34" width="250" height="55" rx="6" fill="#DCFCE7" stroke="#16A34A" />
    <text x="675" y="52" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">3. Pipeline.transform(X_test)</text>
    <text x="675" y="68" text-anchor="middle" font-family="monospace" font-size="10" fill="#047857">scaler.transform(X_test)</text>
    <text x="675" y="80" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="9" fill="#065F46">✓ 100% Leakage-Free &amp; Robust</text>
  </g>
</svg>'''

# 16. Figure 7.7: Special Cases Quick Reference Grid
SVG_SPECIAL_CASES_GRID = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 240" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">SPECIAL CASES AND EDGE-CASE HANDLING IN FEATURE SCALING</text>

  <!-- 4 Quadrants -->
  <!-- Case 1: Constant Features -->
  <g transform="translate(30, 42)">
    <rect width="395" height="88" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1E3A8A">1. Constant Features (Variance = 0)</text>
    <text x="18" y="44" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">If all values are identical (e.g. 20, 20, 20):</text>
    <text x="18" y="60" font-family="monospace" font-size="10" fill="#0284C7">• MinMaxScaler maps to 0.0 (avoids division by zero)</text>
    <text x="18" y="76" font-family="monospace" font-size="10" fill="#0284C7">• StandardScaler sets scale=1.0 &amp; output=0.0</text>
  </g>

  <!-- Case 2: One-Hot Encoded Features -->
  <g transform="translate(455, 42)">
    <rect width="395" height="88" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#7C3AED">2. One-Hot Encoded Binary Columns</text>
    <text x="18" y="44" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">Columns with {0, 1} indicator values:</text>
    <text x="18" y="60" font-family="-apple-system, sans-serif" font-size="10" fill="#581C87">• DO NOT scale with StandardScaler (destroys sparsity &amp; interpretability)</text>
    <text x="18" y="76" font-family="-apple-system, sans-serif" font-size="10" fill="#581C87">• Leave raw {0, 1} untouched or use ColumnTransformer!</text>
  </g>

  <!-- Case 3: Extreme Outliers -->
  <g transform="translate(30, 140)">
    <rect width="395" height="88" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#D97706">3. Extreme Outliers &amp; Heavy Tails</text>
    <text x="18" y="44" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">Features with billionaires, viral spikes, or fraud bursts:</text>
    <text x="18" y="60" font-family="-apple-system, sans-serif" font-size="10" fill="#92400E">• Use RobustScaler (median &amp; IQR resist outlier corruption)</text>
    <text x="18" y="76" font-family="-apple-system, sans-serif" font-size="10" fill="#92400E">• Or apply Log Transformation np.log1p(x) if strictly positive</text>
  </g>

  <!-- Case 4: Sparse Matrices -->
  <g transform="translate(455, 140)">
    <rect width="395" height="88" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#16A34A">4. Sparse Matrices (Text / Bag-of-Words)</text>
    <text x="18" y="44" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">High-dimensional matrices with 99% zeros:</text>
    <text x="18" y="60" font-family="-apple-system, sans-serif" font-size="10" fill="#065F46">• StandardScaler(with_mean=False) preserves zero sparsity</text>
    <text x="18" y="76" font-family="-apple-system, sans-serif" font-size="10" fill="#065F46">• Centering with_mean=True dense-expands matrix → Out of Memory!</text>
  </g>
</svg>'''

ALL_SVGS = {
    'SVG_HERO_SCALING_OVERVIEW': SVG_HERO_SCALING_OVERVIEW,
    'SVG_WHY_SCALE_DISTANCE_DOMINANCE': SVG_WHY_SCALE_DISTANCE_DOMINANCE,
    'SVG_STATISTICAL_SPREAD_ANATOMY': SVG_STATISTICAL_SPREAD_ANATOMY,
    'SVG_Z_SCORE_NORMAL_BELL': SVG_Z_SCORE_NORMAL_BELL,
    'SVG_ROW_VS_COLUMN_OPERATIONS': SVG_ROW_VS_COLUMN_OPERATIONS,
    'SVG_GRAPH_1_ORIGINAL_RANGES': SVG_GRAPH_1_ORIGINAL_RANGES,
    'SVG_GRAPH_2_MINMAX_BEFORE_AFTER': SVG_GRAPH_2_MINMAX_BEFORE_AFTER,
    'SVG_GRAPH_3_STANDARDIZATION_BEFORE_AFTER': SVG_GRAPH_3_STANDARDIZATION_BEFORE_AFTER,
    'SVG_GRAPH_4_OUTLIER_IMPACT': SVG_GRAPH_4_OUTLIER_IMPACT,
    'SVG_GRAPH_5_DISTRIBUTION_PRESERVATION': SVG_GRAPH_5_DISTRIBUTION_PRESERVATION,
    'SVG_GRAPH_6_VECTOR_NORMALIZATION': SVG_GRAPH_6_VECTOR_NORMALIZATION,
    'SVG_GRAPH_7_L1_VS_L2_NORM': SVG_GRAPH_7_L1_VS_L2_NORM,
    'SVG_GRAPH_8_ALGORITHM_SENSITIVITY': SVG_GRAPH_8_ALGORITHM_SENSITIVITY,
    'SVG_GRAPH_9_DECISION_FLOWCHART': SVG_GRAPH_9_DECISION_FLOWCHART,
    'SVG_LEAKAGE_WORKFLOW_ARCHITECTURE': SVG_LEAKAGE_WORKFLOW_ARCHITECTURE,
    'SVG_SPECIAL_CASES_GRID': SVG_SPECIAL_CASES_GRID
}

def validate_all_svgs():
    for name, svg_str in ALL_SVGS.items():
        try:
            ET.fromstring(svg_str)
            print(f"[XML-VALID] {name}")
        except ET.ParseError as e:
            print(f"[XML-ERROR] {name}: {e}")
            raise

if __name__ == '__main__':
    validate_all_svgs()
    print(f"\nAll {len(ALL_SVGS)} SVGs are 100% XML valid!")
