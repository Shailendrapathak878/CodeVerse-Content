"""
Module: topic8_svgs.py
Contains all 13 inline SVG diagrams for Topic 8: Train, Validation & Test Sets.
All SVGs are verified 100% XML-valid with ElementTree.
"""

import xml.etree.ElementTree as ET

# 1. Figure 8.1: Hero Overview - Complete Dataset Division
SVG_HERO_SPLIT_OVERVIEW = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 260" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <defs>
    <linearGradient id="grad-total" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4F46E5" />
      <stop offset="100%" stop-color="#3730A3" />
    </linearGradient>
    <filter id="shadow8" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Title Banner -->
  <rect x="30" y="15" width="820" height="36" rx="8" fill="#F8FAFC" stroke="#E2E8F0" />
  <text x="440" y="38" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#1E293B">THE GOLDEN TRIAD OF DATASET SPLITTING: INDEPENDENT DATA ROLES</text>

  <!-- Total Dataset Bar (Top) -->
  <g transform="translate(40, 65)" filter="url(#shadow8)">
    <rect width="800" height="42" rx="8" fill="url(#grad-total)" />
    <text x="400" y="26" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF">COMPLETE RAW DATASET (100% • N Samples)</text>
  </g>

  <!-- Splitting Arrows -->
  <path d="M 320 110 L 220 145" stroke="#4F46E5" stroke-width="2" stroke-dasharray="3,3" />
  <polygon points="220,145 228,140 226,149" fill="#4F46E5" />

  <path d="M 440 110 L 440 145" stroke="#F59E0B" stroke-width="2" stroke-dasharray="3,3" />
  <polygon points="440,145 436,137 444,137" fill="#F59E0B" />

  <path d="M 560 110 L 660 145" stroke="#10B981" stroke-width="2" stroke-dasharray="3,3" />
  <polygon points="660,145 654,149 652,140" fill="#10B981" />

  <!-- Partition 1: Training Set (70%) -->
  <g transform="translate(40, 150)" filter="url(#shadow8)">
    <rect width="440" height="90" rx="8" fill="#EEF2FF" stroke="#4F46E5" stroke-width="2" />
    <rect x="0" y="0" width="440" height="26" rx="8" fill="#4F46E5" />
    <text x="220" y="18" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">1. TRAINING SET (70% • Learn Parameters)</text>
    <text x="20" y="48" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#312E81">Role: Model Fitting &amp; Weight Optimization</text>
    <text x="20" y="65" font-family="-apple-system, sans-serif" font-size="10" fill="#4338CA">• Calculates model weights (w), biases (b), and tree splits.</text>
    <text x="20" y="80" font-family="-apple-system, sans-serif" font-size="10" fill="#4338CA">• Fits scalers, imputers, and encoders (Fit ONLY here!).</text>
  </g>

  <!-- Partition 2: Validation Set (15%) -->
  <g transform="translate(500, 150)" filter="url(#shadow8)">
    <rect width="160" height="90" rx="8" fill="#FFFBEB" stroke="#F59E0B" stroke-width="2" />
    <rect x="0" y="0" width="160" height="26" rx="8" fill="#F59E0B" />
    <text x="80" y="18" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">2. VAL SET (15%)</text>
    <text x="12" y="48" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#92400E">Model Selection</text>
    <text x="12" y="63" font-family="-apple-system, sans-serif" font-size="9" fill="#78350F">• Tune hyperparameters (k, α).</text>
    <text x="12" y="77" font-family="-apple-system, sans-serif" font-size="9" fill="#78350F">• Early stopping &amp; comparison.</text>
  </g>

  <!-- Partition 3: Test Set (15%) -->
  <g transform="translate(680, 150)" filter="url(#shadow8)">
    <rect width="160" height="90" rx="8" fill="#F0FDF4" stroke="#10B981" stroke-width="2" />
    <rect x="0" y="0" width="160" height="26" rx="8" fill="#10B981" />
    <text x="80" y="18" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">3. TEST SET (15%)</text>
    <text x="12" y="48" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#065F46">Final Unbiased Audit</text>
    <text x="12" y="63" font-family="-apple-system, sans-serif" font-size="9" fill="#047857">• Evaluated ONLY ONCE at end.</text>
    <text x="12" y="77" font-family="-apple-system, sans-serif" font-size="9" fill="#047857">• Estimates future production.</text>
  </g>
</svg>'''

# 2. Visual 2: Comparison of Two Common Split Ratios (80/20 vs 70/15/15)
SVG_SPLIT_RATIOS_COMPARISON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 230" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">VISUAL COMPARISON OF STANDARD DATASET SPLIT ARCHITECTURES</text>

  <!-- Ratio Strategy A: 2-Way Split (80/20) with Cross-Validation -->
  <g transform="translate(40, 50)">
    <rect width="800" height="70" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1E3A8A">Strategy A: 2-Way Split (80% Train / 20% Test) — Paired with K-Fold Cross-Validation</text>
    
    <!-- Bar -->
    <rect x="18" y="34" width="624" height="26" rx="4" fill="#4F46E5" />
    <text x="330" y="51" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">TRAINING &amp; CV DEVELOPMENT (80%)</text>

    <rect x="646" y="34" width="136" height="26" rx="4" fill="#10B981" />
    <text x="714" y="51" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">TEST (20%)</text>
  </g>

  <!-- Ratio Strategy B: 3-Way Split (70/15/15) Dedicated Sets -->
  <g transform="translate(40, 135)">
    <rect width="800" height="75" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="18" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">Strategy B: 3-Way Split (70% Train / 15% Validation / 15% Test) — Dedicated Development Subset</text>

    <!-- Bar -->
    <rect x="18" y="36" width="546" height="26" rx="4" fill="#4F46E5" />
    <text x="290" y="53" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">TRAIN (70%)</text>

    <rect x="568" y="36" width="109" height="26" rx="4" fill="#F59E0B" />
    <text x="622" y="53" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">VAL (15%)</text>

    <rect x="681" y="36" width="101" height="26" rx="4" fill="#10B981" />
    <text x="731" y="53" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">TEST (15%)</text>
  </g>
</svg>'''

# 3. Visual 3: Sample-Count Calculation (N = 1000, 70/15/15)
SVG_SAMPLE_COUNT_CALCULATION = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 240" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">SAMPLE-COUNT CALCULATION ENGINE: TOTAL N = 1,000 OBSERVATIONS</text>

  <!-- 3 Computation Cards -->
  <!-- Card 1: Train -->
  <g transform="translate(40, 50)">
    <rect width="250" height="165" rx="8" fill="#EEF2FF" stroke="#4F46E5" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="28" rx="8" fill="#4F46E5" />
    <text x="125" y="19" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">TRAINING COUNT (N_train)</text>

    <text x="20" y="55" font-family="monospace" font-size="12" fill="#312E81">Formula: N ✕ r_train</text>
    <text x="20" y="80" font-family="monospace" font-size="12" fill="#312E81">Calc: 1,000 ✕ 0.70</text>
    
    <rect x="20" y="100" width="210" height="45" rx="6" fill="#FFFFFF" stroke="#C7D2FE" />
    <text x="125" y="128" text-anchor="middle" font-family="monospace" font-size="16" font-weight="800" fill="#4338CA">N_train = 700</text>
  </g>

  <!-- Card 2: Validation -->
  <g transform="translate(315, 50)">
    <rect width="250" height="165" rx="8" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="28" rx="8" fill="#F59E0B" />
    <text x="125" y="19" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">VALIDATION COUNT (N_val)</text>

    <text x="20" y="55" font-family="monospace" font-size="12" fill="#78350F">Formula: N ✕ r_val</text>
    <text x="20" y="80" font-family="monospace" font-size="12" fill="#78350F">Calc: 1,000 ✕ 0.15</text>

    <rect x="20" y="100" width="210" height="45" rx="6" fill="#FFFFFF" stroke="#FDE68A" />
    <text x="125" y="128" text-anchor="middle" font-family="monospace" font-size="16" font-weight="800" fill="#D97706">N_val = 150</text>
  </g>

  <!-- Card 3: Test -->
  <g transform="translate(590, 50)">
    <rect width="250" height="165" rx="8" fill="#F0FDF4" stroke="#10B981" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="28" rx="8" fill="#10B981" />
    <text x="125" y="19" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">TEST COUNT (N_test)</text>

    <text x="20" y="55" font-family="monospace" font-size="12" fill="#065F46">Formula: N ✕ r_test</text>
    <text x="20" y="80" font-family="monospace" font-size="12" fill="#065F46">Calc: 1,000 ✕ 0.15</text>

    <rect x="20" y="100" width="210" height="45" rx="6" fill="#FFFFFF" stroke="#A7F3D0" />
    <text x="125" y="128" text-anchor="middle" font-family="monospace" font-size="16" font-weight="800" fill="#059669">N_test = 150</text>
  </g>
</svg>'''

# 4. Visual 4: Random Splitting Illustration (Row Indexing & Shuffle)
SVG_RANDOM_SPLITTING_MECHANICS = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 250" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">HOW RANDOM SHUFFLE SPLITTING WORKS: PREVENTING ROW-ORDER BIAS</text>

  <!-- Left: Ordered Raw Table -->
  <g transform="translate(40, 50)">
    <rect width="260" height="175" rx="8" fill="#FEF2F2" stroke="#FECACA" />
    <text x="130" y="22" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">✕ UNSHUFFLED RAW TABLE (SORTED BIAS)</text>
    
    <!-- Rows sorted by class -->
    <rect x="20" y="35" width="220" height="22" fill="#E2E8F0" />
    <text x="30" y="50" font-family="monospace" font-size="10" fill="#334155">Row 001..080: Class 0 (Patients)</text>
    <rect x="20" y="62" width="220" height="22" fill="#E2E8F0" />
    <text x="30" y="77" font-family="monospace" font-size="10" fill="#334155">Row 081..160: Class 0 (Patients)</text>
    <rect x="20" y="89" width="220" height="22" fill="#FEE2E2" />
    <text x="30" y="104" font-family="monospace" font-size="10" font-weight="700" fill="#DC2626">Row 161..200: Class 1 (Deadly Risk!)</text>

    <text x="130" y="145" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#991B1B">If split sequentially (first 70%):</text>
    <text x="130" y="160" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#7F1D1D">Train gets 0% of Class 1! Catastrophic failure.</text>
  </g>

  <!-- Middle: Random Permutation Engine -->
  <g transform="translate(330, 85)">
    <rect width="180" height="90" rx="8" fill="#4F46E5" />
    <text x="90" y="28" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">PSEUDO-RANDOM</text>
    <text x="90" y="44" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">PERMUTATION</text>
    <text x="90" y="68" text-anchor="middle" font-family="monospace" font-size="10" fill="#C7D2FE">random_state = 42</text>
  </g>

  <!-- Right: Shuffled Partition -->
  <g transform="translate(540, 50)">
    <rect width="300" height="175" rx="8" fill="#F0FDF4" stroke="#BBF7D0" />
    <text x="150" y="22" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#16A34A">✓ PERMUTED INDEX PARTITIONS</text>

    <rect x="20" y="38" width="260" height="34" rx="4" fill="#EEF2FF" stroke="#6366F1" />
    <text x="30" y="54" font-family="monospace" font-size="10" fill="#312E81">Train: [idx 142, idx 003, idx 189, ...]</text>
    <text x="30" y="66" font-family="-apple-system, sans-serif" font-size="9" fill="#4338CA">Contains uniform sample mixture</text>

    <rect x="20" y="80" width="260" height="34" rx="4" fill="#FFFBEB" stroke="#F59E0B" />
    <text x="30" y="96" font-family="monospace" font-size="10" fill="#78350F">Val:   [idx 074, idx 195, idx 012, ...]</text>
    <text x="30" y="108" font-family="-apple-system, sans-serif" font-size="9" fill="#92400E">Independent validation mixture</text>

    <rect x="20" y="122" width="260" height="34" rx="4" fill="#F0FDF4" stroke="#10B981" />
    <text x="30" y="138" font-family="monospace" font-size="10" fill="#065F46">Test:  [idx 051, idx 163, idx 099, ...]</text>
    <text x="30" y="150" font-family="-apple-system, sans-serif" font-size="9" fill="#047857">Pure unseen testing mixture</text>
  </g>
</svg>'''

# 5. Visual 5: Stratified Splitting for Class Imbalance (80% / 20%)
SVG_STRATIFIED_SPLITTING_PRESERVATION = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 270" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">STRATIFIED SPLITTING: PRESERVING MINORITY CLASS PROPORTIONS ACROSS SUBSETS</text>

  <!-- Original Population (Left) -->
  <g transform="translate(30, 48)">
    <rect width="180" height="195" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="90" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1E293B">ORIGINAL (N=200)</text>

    <!-- Stacked bar -->
    <rect x="40" y="45" width="100" height="100" rx="4" fill="#3B82F6" />
    <text x="90" y="95" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">Class 0: 160</text>
    <text x="90" y="110" text-anchor="middle" font-family="monospace" font-size="10" fill="#DBEAFE">(80.0%)</text>

    <rect x="40" y="145" width="100" height="25" rx="4" fill="#EF4444" />
    <text x="90" y="162" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Class 1: 40 (20.0%)</text>
    
    <text x="90" y="188" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748B">p_c = 40 / 200 = 20%</text>
  </g>

  <!-- Arrow -->
  <g transform="translate(225, 125)">
    <path d="M 0 0 L 30 0" stroke="#4F46E5" stroke-width="3" />
    <polygon points="30,-4 38,0 30,4" fill="#4F46E5" />
    <text x="15" y="-10" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#4F46E5">stratify=y</text>
  </g>

  <!-- 3 Stratified Subsets (Right) -->
  <!-- Train Subset -->
  <g transform="translate(280, 48)">
    <rect width="170" height="195" rx="8" fill="#EEF2FF" stroke="#4F46E5" />
    <text x="85" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#312E81">TRAIN (N=140)</text>

    <rect x="40" y="45" width="90" height="100" rx="4" fill="#3B82F6" />
    <text x="85" y="95" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">Class 0: 112</text>
    <text x="85" y="110" text-anchor="middle" font-family="monospace" font-size="10" fill="#DBEAFE">(80.0%)</text>

    <rect x="40" y="145" width="90" height="25" rx="4" fill="#EF4444" />
    <text x="85" y="162" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Class 1: 28 (20.0%)</text>

    <text x="85" y="188" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#4338CA">✓ Ratio: 80% / 20%</text>
  </g>

  <!-- Val Subset -->
  <g transform="translate(480, 48)">
    <rect width="170" height="195" rx="8" fill="#FFFBEB" stroke="#F59E0B" />
    <text x="85" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#78350F">VALIDATION (N=30)</text>

    <rect x="40" y="45" width="90" height="100" rx="4" fill="#3B82F6" />
    <text x="85" y="95" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">Class 0: 24</text>
    <text x="85" y="110" text-anchor="middle" font-family="monospace" font-size="10" fill="#DBEAFE">(80.0%)</text>

    <rect x="40" y="145" width="90" height="25" rx="4" fill="#EF4444" />
    <text x="85" y="162" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Class 1: 6 (20.0%)</text>

    <text x="85" y="188" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#D97706">✓ Ratio: 80% / 20%</text>
  </g>

  <!-- Test Subset -->
  <g transform="translate(680, 48)">
    <rect width="170" height="195" rx="8" fill="#F0FDF4" stroke="#10B981" />
    <text x="85" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">TEST (N=30)</text>

    <rect x="40" y="45" width="90" height="100" rx="4" fill="#3B82F6" />
    <text x="85" y="95" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">Class 0: 24</text>
    <text x="85" y="110" text-anchor="middle" font-family="monospace" font-size="10" fill="#DBEAFE">(80.0%)</text>

    <rect x="40" y="145" width="90" height="25" rx="4" fill="#EF4444" />
    <text x="85" y="162" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Class 1: 6 (20.0%)</text>

    <text x="85" y="188" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#059669">✓ Ratio: 80% / 20%</text>
  </g>
</svg>'''

# 6. Visual 6: Training vs Validation vs Test Role Comparison (Exam Analogy)
SVG_TRAIN_VAL_TEST_ROLES = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 250" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">THE EXAM ANALOGY: ROLES OF TRAIN, VALIDATION, AND TEST SETS</text>

  <!-- 3 Stages -->
  <!-- Stage 1: Train -->
  <g transform="translate(30, 48)">
    <rect width="250" height="180" rx="8" fill="#EEF2FF" stroke="#4F46E5" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="28" rx="8" fill="#4F46E5" />
    <text x="125" y="19" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">1. TRAINING: TEXTBOOK &amp; LECTURES</text>

    <text x="20" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#312E81">Role: Parameter Learning</text>
    <text x="20" y="70" font-family="-apple-system, sans-serif" font-size="10" fill="#4338CA">Student studies textbook examples with solutions visible (X and y).</text>
    <text x="20" y="95" font-family="-apple-system, sans-serif" font-size="10" fill="#4338CA">Gradient descent updates internal weights.</text>
    
    <rect x="15" y="125" width="220" height="36" rx="4" fill="#FFFFFF" stroke="#C7D2FE" />
    <text x="125" y="147" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4F46E5">Fits Model Weights (w, b)</text>
  </g>

  <!-- Stage 2: Val -->
  <g transform="translate(315, 48)">
    <rect width="250" height="180" rx="8" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="28" rx="8" fill="#F59E0B" />
    <text x="125" y="19" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">2. VAL: PRACTICE MOCK EXAMS</text>

    <text x="20" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#78350F">Role: Hyperparameter Tuning</text>
    <text x="20" y="70" font-family="-apple-system, sans-serif" font-size="10" fill="#92400E">Student takes mock tests to compare study strategies (e.g. k=3 vs k=7).</text>
    <text x="20" y="95" font-family="-apple-system, sans-serif" font-size="10" fill="#92400E">Triggers early stopping if score drops.</text>

    <rect x="15" y="125" width="220" height="36" rx="4" fill="#FFFFFF" stroke="#FDE68A" />
    <text x="125" y="147" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#D97706">Selects Best Model Settings</text>
  </g>

  <!-- Stage 3: Test -->
  <g transform="translate(600, 48)">
    <rect width="250" height="180" rx="8" fill="#F0FDF4" stroke="#10B981" stroke-width="1.5" />
    <rect x="0" y="0" width="250" height="28" rx="8" fill="#10B981" />
    <text x="125" y="19" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF">3. TEST: THE FINAL UNSEEN EXAM</text>

    <text x="20" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">Role: Final Generalization Audit</text>
    <text x="20" y="70" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">The official final certification exam taken in a proctored room.</text>
    <text x="20" y="95" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">NO tuning allowed! Evaluated once.</text>

    <rect x="15" y="125" width="220" height="36" rx="4" fill="#FFFFFF" stroke="#A7F3D0" />
    <text x="125" y="147" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#10B981">Unbiased Performance Estimate</text>
  </g>
</svg>'''

# 7. Visual 7: Data Leakage Workflow Comparison (Incorrect vs Correct)
SVG_DATA_LEAKAGE_COMPARISON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 270" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">DATA LEAKAGE IN PREPROCESSING: THE INCORRECT VS CORRECT WORKFLOW</text>

  <!-- Top Bad Path: Leaky Preprocessing -->
  <g transform="translate(30, 45)">
    <rect width="820" height="90" rx="8" fill="#FEF2F2" stroke="#FECACA" />
    <text x="20" y="22" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">✕ INCORRECT (LEAKY): PREPROCESSING APPLIED BEFORE SPLITTING</text>

    <!-- Box 1 -->
    <rect x="20" y="36" width="220" height="40" rx="6" fill="#FFFFFF" stroke="#FCA5A5" />
    <text x="130" y="53" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B">Full Raw Dataset (X_all)</text>
    <text x="130" y="67" text-anchor="middle" font-family="monospace" font-size="10" fill="#B91C1C">Scaler.fit_transform(X_all)</text>

    <!-- Arrow -->
    <path d="M 245 56 L 285 56" stroke="#DC2626" stroke-width="2" />
    <polygon points="285,52 293,56 285,60" fill="#DC2626" />

    <!-- Box 2 -->
    <rect x="295" y="36" width="240" height="40" rx="6" fill="#FFFFFF" stroke="#FCA5A5" />
    <text x="415" y="53" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B">train_test_split(X_scaled)</text>
    <text x="415" y="67" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#B91C1C">Test μ and σ leak into training!</text>

    <!-- Arrow -->
    <path d="M 540 56 L 580 56" stroke="#DC2626" stroke-width="2" />
    <polygon points="580,52 588,56 580,60" fill="#DC2626" />

    <!-- Box 3 -->
    <rect x="590" y="36" width="210" height="40" rx="6" fill="#FEE2E2" stroke="#DC2626" />
    <text x="695" y="53" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#7F1D1D">Overly Optimistic Score</text>
    <text x="695" y="67" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D">Fails silently in Production!</text>
  </g>

  <!-- Bottom Good Path: Clean Pipeline -->
  <g transform="translate(30, 148)">
    <rect width="820" height="105" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5" />
    <text x="20" y="22" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#16A34A">✓ CORRECT (LEAK-FREE): SPLIT FIRST, FIT PREPROCESSING ON TRAIN ONLY</text>

    <!-- Step 1 -->
    <rect x="20" y="36" width="180" height="52" rx="6" fill="#FFFFFF" stroke="#86EFAC" />
    <text x="110" y="54" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">1. Split FIRST</text>
    <text x="110" y="72" text-anchor="middle" font-family="monospace" font-size="10" fill="#047857">train_test_split()</text>

    <!-- Arrow -->
    <path d="M 205 62 L 235 62" stroke="#10B981" stroke-width="2" />
    <polygon points="235,58 243,62 235,66" fill="#10B981" />

    <!-- Step 2 -->
    <rect x="245" y="36" width="270" height="52" rx="6" fill="#FFFFFF" stroke="#86EFAC" />
    <text x="380" y="54" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">2. Pipeline.fit(X_train)</text>
    <text x="380" y="72" text-anchor="middle" font-family="monospace" font-size="10" fill="#047857">scaler.fit(X_train) ONLY</text>

    <!-- Arrow -->
    <path d="M 520 62 L 550 62" stroke="#10B981" stroke-width="2" />
    <polygon points="550,58 558,62 550,66" fill="#10B981" />

    <!-- Step 3 -->
    <rect x="560" y="36" width="240" height="52" rx="6" fill="#DCFCE7" stroke="#16A34A" />
    <text x="680" y="54" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">3. Pipeline.transform(X_test)</text>
    <text x="680" y="72" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#065F46">✓ True Unbiased Validation</text>
  </g>
</svg>'''

# 8. Visual 8: Group-Based Splitting (Preventing Subject Leakage)
SVG_GROUP_BASED_SPLITTING = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 260" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">GROUP-BASED SPLITTING: PREVENTING PATIENT / USER IDENTITY CONTAMINATION</text>

  <!-- Left: Random Split Failure (Patient Contamination) -->
  <g transform="translate(40, 50)">
    <rect width="380" height="185" rx="8" fill="#FEF2F2" stroke="#FECACA" />
    <text x="190" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">✕ RANDOM SPLIT: IDENTITY LEAKAGE</text>
    
    <text x="20" y="50" font-family="-apple-system, sans-serif" font-size="11" fill="#7F1D1D">Patient 101 has 5 hospital visits:</text>
    <rect x="20" y="60" width="340" height="30" rx="4" fill="#FFFFFF" stroke="#FCA5A5" />
    <text x="30" y="79" font-family="monospace" font-size="10" fill="#B91C1C">Train gets: Visit 1, Visit 2, Visit 4</text>
    
    <rect x="20" y="96" width="340" height="30" rx="4" fill="#FFFFFF" stroke="#FCA5A5" />
    <text x="30" y="115" font-family="monospace" font-size="10" fill="#B91C1C">Test gets:  Visit 3, Visit 5</text>

    <text x="20" y="148" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#DC2626">The model memorizes Patient 101's unique physiology!</text>
    <text x="20" y="165" font-family="-apple-system, sans-serif" font-size="10" fill="#991B1B">Test accuracy is artificially high; model fails on new patients.</text>
  </g>

  <!-- Right: Group-Aware Split (Patient Independence) -->
  <g transform="translate(460, 50)">
    <rect width="380" height="185" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5" />
    <text x="190" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#16A34A">✓ GroupShuffleSplit: ZERO PATIENT OVERLAP</text>

    <text x="20" y="50" font-family="-apple-system, sans-serif" font-size="11" fill="#065F46">All visits for a subject are grouped together:</text>
    <rect x="20" y="60" width="340" height="30" rx="4" fill="#FFFFFF" stroke="#86EFAC" />
    <text x="30" y="79" font-family="monospace" font-size="10" fill="#047857">Train gets: Patient 101, 102, 104 (All Visits)</text>

    <rect x="20" y="96" width="340" height="30" rx="4" fill="#FFFFFF" stroke="#86EFAC" />
    <text x="30" y="115" font-family="monospace" font-size="10" fill="#047857">Test gets:  Patient 103, 105 (All Visits)</text>

    <text x="20" y="148" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#059669">✓ True Patient-Level Generalization!</text>
    <text x="20" y="165" font-family="-apple-system, sans-serif" font-size="10" fill="#065F46">Evaluates whether the model diagnoses brand new individuals.</text>
  </g>
</svg>'''

# 9. Visual 9: Chronological Time-Series Splitting (No Lookahead)
SVG_TIME_SERIES_SPLITTING = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 250" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">CHRONOLOGICAL SPLITTING: ELIMINATING LOOKAHEAD BIAS IN TEMPORAL DATA</text>

  <!-- Timeline Axis -->
  <line x1="80" y1="60" x2="800" y2="60" stroke="#94A3B8" stroke-width="2" />
  <polygon points="800,56 808,60 800,64" fill="#94A3B8" />
  <text x="80" y="50" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">Past (Jan 2026)</text>
  <text x="800" y="50" text-anchor="end" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">Future (Dec 2026) →</text>

  <!-- Fold 1 -->
  <g transform="translate(80, 80)">
    <text x="0" y="16" font-family="monospace" font-size="11" font-weight="700" fill="#334155">Split 1:</text>
    <rect x="70" y="0" width="300" height="24" rx="4" fill="#4F46E5" />
    <text x="220" y="16" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Train: Jan – Mar</text>
    <rect x="375" y="0" width="120" height="24" rx="4" fill="#F59E0B" />
    <text x="435" y="16" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Val: Apr</text>
  </g>

  <!-- Fold 2 -->
  <g transform="translate(80, 115)">
    <text x="0" y="16" font-family="monospace" font-size="11" font-weight="700" fill="#334155">Split 2:</text>
    <rect x="70" y="0" width="425" height="24" rx="4" fill="#4F46E5" />
    <text x="280" y="16" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Train: Jan – Apr (Expanding Window)</text>
    <rect x="500" y="0" width="120" height="24" rx="4" fill="#F59E0B" />
    <text x="560" y="16" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Val: May</text>
  </g>

  <!-- Fold 3 (Final Test) -->
  <g transform="translate(80, 150)">
    <text x="0" y="16" font-family="monospace" font-size="11" font-weight="700" fill="#334155">Final:</text>
    <rect x="70" y="0" width="550" height="24" rx="4" fill="#4F46E5" />
    <text x="345" y="16" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Train: Jan – Oct</text>
    <rect x="625" y="0" width="95" height="24" rx="4" fill="#10B981" />
    <text x="672" y="16" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Test: Nov–Dec</text>
  </g>

  <!-- Rule Banner -->
  <rect x="80" y="195" width="720" height="32" rx="6" fill="#F0FDF4" stroke="#86EFAC" />
  <text x="440" y="215" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">✓ CARDINAL TIME-SERIES LAW: Training index (t) must ALWAYS strictly precede testing index (t &gt; max(t_train)).</text>
</svg>'''

# 10. Visual 10: Five-Fold Cross-Validation Diagram
SVG_FIVE_FOLD_CROSS_VALIDATION = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 250" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">5-FOLD CROSS-VALIDATION: ROTATING VALIDATION FOLDS ACROSS TRAINING DATA</text>

  <!-- 5 Iteration Rows -->
  <!-- Iter 1 -->
  <g transform="translate(50, 45)">
    <text x="0" y="16" font-family="monospace" font-size="10" font-weight="700" fill="#334155">Fold 1:</text>
    <rect x="60" y="0" width="140" height="22" rx="3" fill="#F59E0B" />
    <text x="130" y="15" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Val Fold (Score 1)</text>
    <rect x="205" y="0" width="575" height="22" rx="3" fill="#4F46E5" />
    <text x="492" y="15" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#FFFFFF">Training Folds (4/5)</text>
  </g>

  <!-- Iter 2 -->
  <g transform="translate(50, 75)">
    <text x="0" y="16" font-family="monospace" font-size="10" font-weight="700" fill="#334155">Fold 2:</text>
    <rect x="60" y="0" width="140" height="22" rx="3" fill="#4F46E5" />
    <rect x="205" y="0" width="140" height="22" rx="3" fill="#F59E0B" />
    <text x="275" y="15" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Val Fold (Score 2)</text>
    <rect x="350" y="0" width="430" height="22" rx="3" fill="#4F46E5" />
  </g>

  <!-- Iter 3 -->
  <g transform="translate(50, 105)">
    <text x="0" y="16" font-family="monospace" font-size="10" font-weight="700" fill="#334155">Fold 3:</text>
    <rect x="60" y="0" width="285" height="22" rx="3" fill="#4F46E5" />
    <rect x="350" y="0" width="140" height="22" rx="3" fill="#F59E0B" />
    <text x="420" y="15" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Val Fold (Score 3)</text>
    <rect x="495" y="0" width="285" height="22" rx="3" fill="#4F46E5" />
  </g>

  <!-- Iter 4 -->
  <g transform="translate(50, 135)">
    <text x="0" y="16" font-family="monospace" font-size="10" font-weight="700" fill="#334155">Fold 4:</text>
    <rect x="60" y="0" width="430" height="22" rx="3" fill="#4F46E5" />
    <rect x="495" y="0" width="140" height="22" rx="3" fill="#F59E0B" />
    <text x="565" y="15" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Val Fold (Score 4)</text>
    <rect x="640" y="0" width="140" height="22" rx="3" fill="#4F46E5" />
  </g>

  <!-- Iter 5 -->
  <g transform="translate(50, 165)">
    <text x="0" y="16" font-family="monospace" font-size="10" font-weight="700" fill="#334155">Fold 5:</text>
    <rect x="60" y="0" width="575" height="22" rx="3" fill="#4F46E5" />
    <text x="345" y="15" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#FFFFFF">Training Folds (4/5)</text>
    <rect x="640" y="0" width="140" height="22" rx="3" fill="#F59E0B" />
    <text x="710" y="15" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Val Fold (Score 5)</text>
  </g>

  <!-- Average Calculation Banner -->
  <g transform="translate(110, 202)">
    <rect width="660" height="34" rx="6" fill="#EEF2FF" stroke="#6366F1" />
    <text x="330" y="21" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#312E81">Cross-Validation Score = (Score 1 + Score 2 + Score 3 + Score 4 + Score 5) / 5</text>
  </g>
</svg>'''

# 11. Visual 11: Model-Selection Flowchart
SVG_MODEL_SELECTION_FLOWCHART = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 260" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">MODEL-SELECTION FLOWCHART: WHERE VALIDATION AND TEST SETS OPERATE</text>

  <!-- Step 1: Candidate Generation -->
  <g transform="translate(30, 50)">
    <rect width="180" height="85" rx="8" fill="#EEF2FF" stroke="#4F46E5" />
    <text x="90" y="26" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#312E81">1. TRAIN CANDIDATES</text>
    <text x="15" y="48" font-family="-apple-system, sans-serif" font-size="10" fill="#4338CA">• Model A: KNN (k=3)</text>
    <text x="15" y="64" font-family="-apple-system, sans-serif" font-size="10" fill="#4338CA">• Model B: KNN (k=7)</text>
    <text x="90" y="78" text-anchor="middle" font-family="monospace" font-size="9" fill="#6366F1">Fitted on X_train ONLY</text>
  </g>

  <!-- Arrow -->
  <path d="M 215 92 L 255 92" stroke="#64748B" stroke-width="2" />
  <polygon points="255,88 263,92 255,96" fill="#64748B" />

  <!-- Step 2: Validation Evaluation -->
  <g transform="translate(265, 50)">
    <rect width="210" height="85" rx="8" fill="#FFFBEB" stroke="#F59E0B" />
    <text x="105" y="26" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#78350F">2. VALIDATE &amp; COMPARE</text>
    <text x="15" y="48" font-family="-apple-system, sans-serif" font-size="10" fill="#92400E">• Model A Val Acc: 83.3%</text>
    <text x="15" y="64" font-family="-apple-system, sans-serif" font-size="10" fill="#92400E">• Model B Val Acc: 80.0%</text>
    <text x="105" y="78" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#D97706">→ Winner: Model A (k=3)</text>
  </g>

  <!-- Arrow -->
  <path d="M 480 92 L 520 92" stroke="#64748B" stroke-width="2" />
  <polygon points="520,88 528,92 520,96" fill="#64748B" />

  <!-- Step 3: Final Test Evaluation -->
  <g transform="translate(530, 50)">
    <rect width="210" height="85" rx="8" fill="#F0FDF4" stroke="#10B981" />
    <text x="105" y="26" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46">3. UNBIASED TEST AUDIT</text>
    <text x="15" y="48" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">• Evaluated on X_test ONCE.</text>
    <text x="15" y="64" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">• Final Test Acc: 80.0%</text>
    <text x="105" y="78" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#059669">NO MORE TUNING ALLOWED!</text>
  </g>

  <!-- Arrow Down to Deploy -->
  <path d="M 635 140 L 635 170" stroke="#10B981" stroke-width="2" />
  <polygon points="631,170 635,178 639,170" fill="#10B981" />

  <!-- Step 4: Production Deployment -->
  <g transform="translate(530, 180)">
    <rect width="210" height="60" rx="8" fill="#ECFDF5" stroke="#059669" stroke-width="2" />
    <text x="105" y="26" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#065F46">DEPLOY TO PRODUCTION</text>
    <text x="105" y="45" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" fill="#047857">Guards against test-set overfitting</text>
  </g>
</svg>'''

# 12. Visual 12: Python Lab Verification Bar Chart
SVG_LAB_VERIFICATION_CHART = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 230" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">PRACTICAL LAB VERIFICATION: QUANTITATIVE SPLIT DISTRIBUTION &amp; METRICS</text>

  <!-- 3 Bars for Sample Counts -->
  <g transform="translate(80, 50)">
    <!-- Y Axis -->
    <line x1="60" y1="20" x2="60" y2="130" stroke="#94A3B8" />
    <line x1="55" y1="20" x2="60" y2="20" stroke="#94A3B8" />
    <text x="50" y="24" text-anchor="end" font-family="monospace" font-size="9" fill="#64748B">140</text>
    <line x1="55" y1="100" x2="60" y2="100" stroke="#94A3B8" />
    <text x="50" y="104" text-anchor="end" font-family="monospace" font-size="9" fill="#64748B">30</text>
    <line x1="60" y1="130" x2="380" y2="130" stroke="#94A3B8" />

    <!-- Train Bar (140) -->
    <rect x="90" y="20" width="70" height="110" rx="4" fill="#4F46E5" />
    <text x="125" y="75" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">140</text>
    <text x="125" y="148" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#312E81">Train (70%)</text>

    <!-- Val Bar (30) -->
    <rect x="190" y="106" width="70" height="24" rx="4" fill="#F59E0B" />
    <text x="225" y="122" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">30</text>
    <text x="225" y="148" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#78350F">Val (15%)</text>

    <!-- Test Bar (30) -->
    <rect x="290" y="106" width="70" height="24" rx="4" fill="#10B981" />
    <text x="325" y="122" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">30</text>
    <text x="325" y="148" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#065F46">Test (15%)</text>
  </g>

  <!-- Right Side Scorecard -->
  <g transform="translate(500, 50)">
    <rect width="330" height="150" rx="8" fill="#F8FAFC" stroke="#CBD5E1" />
    <text x="20" y="26" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1E293B">Laboratory Verification Scorecard:</text>

    <text x="20" y="52" font-family="monospace" font-size="11" fill="#059669">✓ Total Samples: 200 (100% accounted)</text>
    <text x="20" y="74" font-family="monospace" font-size="11" fill="#059669">✓ Stratified Ratio: 80.0% / 20.0% (exact)</text>
    <text x="20" y="96" font-family="monospace" font-size="11" fill="#059669">✓ Overlap Audit: 0 common IDs across sets</text>
    <text x="20" y="118" font-family="monospace" font-size="11" fill="#059669">✓ Leakage Assertion: Scaler fitted on Train only</text>
    <text x="20" y="140" font-family="monospace" font-size="11" fill="#0369A1">✓ Selected Model: KNN (k=3, 83.3% Val Acc)</text>
  </g>
</svg>'''

# 13. Visual 13: Leakage Pitfall Grid (9 Common Leakage Types)
SVG_NINE_LEAKAGE_VECTORS = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 250" width="100%" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="440" y="24" text-anchor="middle" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">THE 9 CRITICAL DATA LEAKAGE VECTORS DURING DATASET SPLITTING</text>

  <!-- 3x3 Grid of Leakage Pitfalls -->
  <!-- Row 1 -->
  <g transform="translate(30, 42)">
    <rect width="250" height="56" rx="6" fill="#FEF2F2" stroke="#FCA5A5" />
    <text x="12" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">1. Scaling Before Splitting</text>
    <text x="12" y="40" font-family="-apple-system, sans-serif" font-size="9" fill="#7F1D1D">Test mean and std contaminate training.</text>
  </g>

  <g transform="translate(315, 42)">
    <rect width="250" height="56" rx="6" fill="#FEF2F2" stroke="#FCA5A5" />
    <text x="12" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">2. Full-Dataset Imputation</text>
    <text x="12" y="40" font-family="-apple-system, sans-serif" font-size="9" fill="#7F1D1D">Missing values filled using test statistics.</text>
  </g>

  <g transform="translate(600, 42)">
    <rect width="250" height="56" rx="6" fill="#FEF2F2" stroke="#FCA5A5" />
    <text x="12" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">3. Test-Aware Feature Selection</text>
    <text x="12" y="40" font-family="-apple-system, sans-serif" font-size="9" fill="#7F1D1D">Selecting features correlated with test y.</text>
  </g>

  <!-- Row 2 -->
  <g transform="translate(30, 108)">
    <rect width="250" height="56" rx="6" fill="#FEF2F2" stroke="#FCA5A5" />
    <text x="12" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">4. Global Target Encoding</text>
    <text x="12" y="40" font-family="-apple-system, sans-serif" font-size="9" fill="#7F1D1D">Category means leak test evaluation targets.</text>
  </g>

  <g transform="translate(315, 108)">
    <rect width="250" height="56" rx="6" fill="#FEF2F2" stroke="#FCA5A5" />
    <text x="12" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">5. Oversampling Before Split</text>
    <text x="12" y="40" font-family="-apple-system, sans-serif" font-size="9" fill="#7F1D1D">Synthetic SMOTE clones cross into test.</text>
  </g>

  <g transform="translate(600, 108)">
    <rect width="250" height="56" rx="6" fill="#FEF2F2" stroke="#FCA5A5" />
    <text x="12" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">6. Duplicate Record Crossing</text>
    <text x="12" y="40" font-family="-apple-system, sans-serif" font-size="9" fill="#7F1D1D">Identical rows appear in both train &amp; test.</text>
  </g>

  <!-- Row 3 -->
  <g transform="translate(30, 174)">
    <rect width="250" height="56" rx="6" fill="#FEF2F2" stroke="#FCA5A5" />
    <text x="12" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">7. Patient / Subject Group Leakage</text>
    <text x="12" y="40" font-family="-apple-system, sans-serif" font-size="9" fill="#7F1D1D">Same human identity appears in both sets.</text>
  </g>

  <g transform="translate(315, 174)">
    <rect width="250" height="56" rx="6" fill="#FEF2F2" stroke="#FCA5A5" />
    <text x="12" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">8. Time Lookahead Bias</text>
    <text x="12" y="40" font-family="-apple-system, sans-serif" font-size="9" fill="#7F1D1D">Shuffling temporal data trains on future.</text>
  </g>

  <g transform="translate(600, 174)">
    <rect width="250" height="56" rx="6" fill="#FEF2F2" stroke="#FCA5A5" />
    <text x="12" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">9. Test-Score Hyperparameter Tuning</text>
    <text x="12" y="40" font-family="-apple-system, sans-serif" font-size="9" fill="#7F1D1D">Repeatedly tuning decisions to beat test score.</text>
  </g>
</svg>'''

ALL_TOPIC8_SVGS = {
    'SVG_HERO_SPLIT_OVERVIEW': SVG_HERO_SPLIT_OVERVIEW,
    'SVG_SPLIT_RATIOS_COMPARISON': SVG_SPLIT_RATIOS_COMPARISON,
    'SVG_SAMPLE_COUNT_CALCULATION': SVG_SAMPLE_COUNT_CALCULATION,
    'SVG_RANDOM_SPLITTING_MECHANICS': SVG_RANDOM_SPLITTING_MECHANICS,
    'SVG_STRATIFIED_SPLITTING_PRESERVATION': SVG_STRATIFIED_SPLITTING_PRESERVATION,
    'SVG_TRAIN_VAL_TEST_ROLES': SVG_TRAIN_VAL_TEST_ROLES,
    'SVG_DATA_LEAKAGE_COMPARISON': SVG_DATA_LEAKAGE_COMPARISON,
    'SVG_GROUP_BASED_SPLITTING': SVG_GROUP_BASED_SPLITTING,
    'SVG_TIME_SERIES_SPLITTING': SVG_TIME_SERIES_SPLITTING,
    'SVG_FIVE_FOLD_CROSS_VALIDATION': SVG_FIVE_FOLD_CROSS_VALIDATION,
    'SVG_MODEL_SELECTION_FLOWCHART': SVG_MODEL_SELECTION_FLOWCHART,
    'SVG_LAB_VERIFICATION_CHART': SVG_LAB_VERIFICATION_CHART,
    'SVG_NINE_LEAKAGE_VECTORS': SVG_NINE_LEAKAGE_VECTORS
}

def validate_all_svgs():
    for name, svg_str in ALL_TOPIC8_SVGS.items():
        try:
            ET.fromstring(svg_str)
            print(f"[XML-VALID] {name}")
        except ET.ParseError as e:
            print(f"[XML-ERROR] {name}: {e}")
            raise

if __name__ == '__main__':
    validate_all_svgs()
    print(f"\nAll {len(ALL_TOPIC8_SVGS)} Topic 8 SVGs are 100% XML valid!")
