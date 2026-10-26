# Topic 20 SVG Graphics Generation Script - 18 Verified Vector SVGs
# Strict Light Mode Only, 100% Valid XML, Emerald & Royal Teal Theme

svgs = {}

# 1. Figure 1.1: Training, Validation, and Test Workflow
svgs["__SVG_VAL_WORKFLOW__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Step 1: Raw Dataset -->
  <g>
    <rect x="20" y="55" width="125" height="130" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="35" y="70" width="95" height="24" rx="4" fill="#64748B"/>
    <text x="82" y="86" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Full Dataset</text>
    <text x="82" y="118" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">N = 1,000</text>
    <text x="82" y="140" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">All available</text>
    <text x="82" y="155" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">observations</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 155 120 L 180 120" stroke="#059669" stroke-width="2.5" marker-end="url(#arr-green)"/>

  <!-- Step 2: Training Split -->
  <g>
    <rect x="190" y="40" width="165" height="160" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <rect x="205" y="55" width="135" height="24" rx="4" fill="#0284C7"/>
    <text x="272" y="71" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. Training Set (70%)</text>
    <text x="272" y="102" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">700 Samples</text>
    <text x="215" y="128" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="11">&bull; Fits model parameters</text>
    <text x="215" y="148" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="11">&bull; Learns weights / trees</text>
    <text x="215" y="168" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="11">&bull; Used in gradient descent</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 365 120 L 390 120" stroke="#059669" stroke-width="2.5"/>

  <!-- Step 3: Validation Split -->
  <g>
    <rect x="400" y="40" width="175" height="160" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="2"/>
    <rect x="415" y="55" width="145" height="24" rx="4" fill="#059669"/>
    <text x="487" y="71" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. Validation Set (15%)</text>
    <text x="487" y="102" fill="#047857" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">150 Samples (or CV Folds)</text>
    <text x="420" y="128" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="11">&bull; Tunes hyperparameters</text>
    <text x="420" y="148" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="11">&bull; Selects best candidate</text>
    <text x="420" y="168" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="11">&bull; Calibrates threshold</text>
  </g>

  <!-- Arrow 3 -->
  <path d="M 585 120 L 610 120" stroke="#059669" stroke-width="2.5"/>

  <!-- Step 4: Final Test Split (Vault) -->
  <g>
    <rect x="620" y="40" width="160" height="160" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
    <rect x="635" y="55" width="130" height="24" rx="4" fill="#7E22CE"/>
    <text x="700" y="71" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. Final Test (15%)</text>
    <text x="700" y="102" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">150 Samples (Sealed)</text>
    <text x="635" y="128" fill="#581C87" font-family="-apple-system, sans-serif" font-size="11">&bull; Evaluated ONCE only</text>
    <text x="635" y="148" fill="#581C87" font-family="-apple-system, sans-serif" font-size="11">&bull; Unbiased generalization</text>
    <text x="635" y="168" fill="#581C87" font-family="-apple-system, sans-serif" font-size="11">&bull; Never used in tuning!</text>
  </g>

  <defs>
    <marker id="arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#059669"/>
    </marker>
  </defs>
</svg>'''

# 2. Figure 1.2: Dataset Split Proportions Diagram (70/15/15)
svgs["__SVG_SPLIT_RATIOS__"] = '''<svg viewBox="0 0 800 210" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="32" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Dataset Partitioning Protocol (1,000 Total Observations)</text>
  
  <defs>
    <clipPath id="split-bar-clip">
      <rect x="50" y="60" width="700" height="55" rx="8"/>
    </clipPath>
  </defs>

  <!-- Segmented Bar Container with ClipPath -->
  <g clip-path="url(#split-bar-clip)">
    <!-- Training Portion: 70% (490px) -->
    <rect x="50" y="60" width="490" height="55" fill="#0284C7"/>
    <text x="295" y="88" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" text-anchor="middle">TRAINING SET &bull; 70% (700 Samples)</text>
    <text x="295" y="104" fill="#E0F2FE" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Fits model parameters, slopes, and decision thresholds</text>

    <!-- Validation Portion: 15% (105px) -->
    <rect x="540" y="60" width="105" height="55" fill="#059669"/>
    <text x="592" y="88" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">VAL &bull; 15%</text>
    <text x="592" y="104" fill="#D1FAE5" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">150 Samples</text>

    <!-- Test Portion: 15% (105px) -->
    <rect x="645" y="60" width="105" height="55" fill="#7E22CE"/>
    <text x="697" y="88" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">TEST &bull; 15%</text>
    <text x="697" y="104" fill="#F3E8FF" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">150 Samples</text>
  </g>
  <!-- Outer Border -->
  <rect x="50" y="60" width="700" height="55" rx="8" fill="none" stroke="#CBD5E1" stroke-width="1.5"/>

  <!-- Explanatory Footnotes -->
  <g>
    <circle cx="90" cy="145" r="5" fill="#0284C7"/>
    <text x="105" y="149" fill="#334155" font-family="-apple-system, sans-serif" font-size="11"><tspan font-weight="700">Training Set:</tspan> Available during model fitting.</text>

    <circle cx="330" cy="145" r="5" fill="#059669"/>
    <text x="345" y="149" fill="#334155" font-family="-apple-system, sans-serif" font-size="11"><tspan font-weight="700">Validation Set:</tspan> Selects hyperparameters &amp; models.</text>

    <circle cx="580" cy="145" r="5" fill="#7E22CE"/>
    <text x="595" y="149" fill="#334155" font-family="-apple-system, sans-serif" font-size="11"><tspan font-weight="700">Test Set:</tspan> Locked vault for final test check.</text>
  </g>

  <text x="400" y="185" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Alternative common splits: 80/10/10 (larger datasets) or 60/20/20 (smaller datasets where validation needs more statistical power).</text>
</svg>'''

# 3. Figure 1.3: Overfitting vs Generalization Gap Curve
svgs["__SVG_GENERALIZATION_GAP__"] = '''<svg viewBox="0 0 800 300" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Training vs Validation Error &bull; The Generalization Gap</text>

  <!-- Axes -->
  <line x1="100" y1="240" x2="720" y2="240" stroke="#94A3B8" stroke-width="2"/>
  <line x1="100" y1="240" x2="100" y2="50" stroke="#94A3B8" stroke-width="2"/>
  <text x="410" y="275" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Model Complexity (e.g., Tree Depth, Polynomial Degree, Training Epochs)</text>
  <text x="40" y="145" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" transform="rotate(-90 40 145)" text-anchor="middle">Prediction Error (Lower is Better)</text>

  <!-- Underfitting Region (Left) -->
  <rect x="100" y="50" width="190" height="190" fill="#FEF3C7" fill-opacity="0.3"/>
  <text x="195" y="75" fill="#D97706" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Underfitting Zone</text>
  <text x="195" y="92" fill="#92400E" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">High Bias (Too Simple)</text>

  <!-- Optimal Zone (Middle) -->
  <rect x="290" y="50" width="160" height="190" fill="#ECFDF5" fill-opacity="0.5"/>
  <text x="370" y="75" fill="#059669" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Sweet Spot</text>
  <text x="370" y="92" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Best Generalization</text>

  <!-- Overfitting Region (Right) -->
  <rect x="450" y="50" width="270" height="190" fill="#FEE2E2" fill-opacity="0.3"/>
  <text x="585" y="75" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Overfitting Zone</text>
  <text x="585" y="92" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">High Variance (Memorizing Noise)</text>

  <!-- Training Error Curve (Monotonically decreasing) -->
  <path d="M 110 200 Q 250 160 370 120 T 700 65" fill="none" stroke="#0284C7" stroke-width="3"/>
  <text x="680" y="55" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Training Error</text>

  <!-- Validation Error Curve (U-shaped) -->
  <path d="M 110 220 Q 250 170 370 135 T 700 215" fill="none" stroke="#DC2626" stroke-width="3"/>
  <text x="680" y="235" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Validation Error</text>

  <!-- Optimal Point Indicator -->
  <circle cx="370" cy="135" r="6" fill="#059669"/>
  <line x1="370" y1="135" x2="370" y2="240" stroke="#059669" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="370" y="255" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Optimal Model</text>

  <!-- Generalization Gap Bracket in Overfitting Region -->
  <line x1="620" y1="80" x2="620" y2="185" stroke="#9333EA" stroke-width="2"/>
  <line x1="615" y1="80" x2="625" y2="80" stroke="#9333EA" stroke-width="2"/>
  <line x1="615" y1="185" x2="625" y2="185" stroke="#9333EA" stroke-width="2"/>
  <text x="630" y="138" fill="#7E22CE" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Generalization Gap</text>
</svg>'''

# 4. Figure 1.4: Underfitting vs Good Fit vs Overfitting
svgs["__SVG_FIT_SPECTRUM__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Card 1: Underfitting -->
  <g>
    <rect x="25" y="20" width="230" height="200" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
    <rect x="40" y="32" width="100" height="22" rx="4" fill="#D97706"/>
    <text x="90" y="47" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Underfitting</text>
    
    <!-- Mini Plot: Flat line through curved points -->
    <rect x="40" y="65" width="200" height="85" fill="#FFFFFF" stroke="#E2E8F0" rx="4"/>
    <circle cx="60" cy="130" r="3" fill="#64748B"/><circle cx="90" cy="100" r="3" fill="#64748B"/>
    <circle cx="130" cy="80" r="3" fill="#64748B"/><circle cx="170" cy="85" r="3" fill="#64748B"/>
    <circle cx="210" cy="120" r="3" fill="#64748B"/>
    <!-- Rigid straight line -->
    <line x1="50" y1="125" x2="230" y2="90" stroke="#DC2626" stroke-width="2.5"/>

    <text x="140" y="170" fill="#92400E" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">High Bias &bull; Too Simple</text>
    <text x="140" y="188" fill="#78350F" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Low Train Acc &bull; Low Val Acc</text>
    <text x="140" y="204" fill="#64748B" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Fix: Increase model complexity</text>
  </g>

  <!-- Card 2: Good Fit (Optimal) -->
  <g>
    <rect x="285" y="20" width="230" height="200" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="2"/>
    <rect x="300" y="32" width="115" height="22" rx="4" fill="#059669"/>
    <text x="357" y="47" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">&check; Good Fit (Ideal)</text>
    
    <!-- Mini Plot: Smooth curve through curved points -->
    <rect x="300" y="65" width="200" height="85" fill="#FFFFFF" stroke="#E2E8F0" rx="4"/>
    <circle cx="320" cy="130" r="3" fill="#64748B"/><circle cx="350" cy="100" r="3" fill="#64748B"/>
    <circle cx="390" cy="80" r="3" fill="#64748B"/><circle cx="430" cy="85" r="3" fill="#64748B"/>
    <circle cx="470" cy="120" r="3" fill="#64748B"/>
    <!-- Smooth parabola curve -->
    <path d="M 310 140 Q 390 60 490 135" fill="none" stroke="#059669" stroke-width="2.5"/>

    <text x="400" y="170" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Balanced &bull; Generalizes</text>
    <text x="400" y="188" fill="#047857" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">High Train Acc &bull; High Val Acc</text>
    <text x="400" y="204" fill="#64748B" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Goal: Deploy this candidate</text>
  </g>

  <!-- Card 3: Overfitting -->
  <g>
    <rect x="545" y="20" width="230" height="200" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <rect x="560" y="32" width="100" height="22" rx="4" fill="#DC2626"/>
    <text x="610" y="47" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Overfitting</text>
    
    <!-- Mini Plot: Erratic squiggly line through every point -->
    <rect x="560" y="65" width="200" height="85" fill="#FFFFFF" stroke="#E2E8F0" rx="4"/>
    <circle cx="580" cy="130" r="3" fill="#64748B"/><circle cx="610" cy="100" r="3" fill="#64748B"/>
    <circle cx="650" cy="80" r="3" fill="#64748B"/><circle cx="690" cy="85" r="3" fill="#64748B"/>
    <circle cx="730" cy="120" r="3" fill="#64748B"/>
    <!-- Wild zigzag line -->
    <path d="M 570 145 L 580 130 L 595 140 L 610 100 L 630 110 L 650 80 L 670 95 L 690 85 L 710 135 L 730 120 L 745 130" fill="none" stroke="#DC2626" stroke-width="2"/>

    <text x="660" y="170" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">High Variance &bull; Memorizing</text>
    <text x="660" y="188" fill="#B91C1C" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">100% Train Acc &bull; Poor Val Acc</text>
    <text x="660" y="204" fill="#64748B" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Fix: Regularize, prune, gather data</text>
  </g>
</svg>'''

# 5. Figure 1.5: 5-Fold Cross-Validation Architecture
svgs["__SVG_KFOLD_5FOLD__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">K-Fold Cross-Validation (K = 5 Folds)</text>
  <text x="400" y="46" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Dataset divided into 5 equal subsets. In each iteration, 4 folds train the model and 1 fold validates.</text>

  <!-- 5 Equal Folds Layout -->
  <g>
    <!-- Fold 1 -->
    <rect x="50" y="70" width="130" height="90" rx="6" fill="#F0F9FF" stroke="#0284C7" stroke-width="1.5"/>
    <text x="115" y="98" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Fold 1</text>
    <text x="115" y="118" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">20% Samples</text>
    <rect x="65" y="130" width="100" height="20" rx="3" fill="#E0F2FE"/>
    <text x="115" y="144" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Validation Iter 1</text>

    <!-- Fold 2 -->
    <rect x="195" y="70" width="130" height="90" rx="6" fill="#ECFDF5" stroke="#059669" stroke-width="1.5"/>
    <text x="260" y="98" fill="#059669" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Fold 2</text>
    <text x="260" y="118" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">20% Samples</text>
    <rect x="210" y="130" width="100" height="20" rx="3" fill="#D1FAE5"/>
    <text x="260" y="144" fill="#047857" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Validation Iter 2</text>

    <!-- Fold 3 -->
    <rect x="340" y="70" width="130" height="90" rx="6" fill="#FAF5FF" stroke="#7E22CE" stroke-width="1.5"/>
    <text x="405" y="98" fill="#7E22CE" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Fold 3</text>
    <text x="405" y="118" fill="#581C87" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">20% Samples</text>
    <rect x="355" y="130" width="100" height="20" rx="3" fill="#F3E8FF"/>
    <text x="405" y="144" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Validation Iter 3</text>

    <!-- Fold 4 -->
    <rect x="485" y="70" width="130" height="90" rx="6" fill="#FFFBEB" stroke="#D97706" stroke-width="1.5"/>
    <text x="550" y="98" fill="#D97706" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Fold 4</text>
    <text x="550" y="118" fill="#78350F" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">20% Samples</text>
    <rect x="500" y="130" width="100" height="20" rx="3" fill="#FEF3C7"/>
    <text x="550" y="144" fill="#B45309" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Validation Iter 4</text>

    <!-- Fold 5 -->
    <rect x="630" y="70" width="130" height="90" rx="6" fill="#FFF1F2" stroke="#E11D48" stroke-width="1.5"/>
    <text x="695" y="98" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Fold 5</text>
    <text x="695" y="118" fill="#881337" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">20% Samples</text>
    <rect x="645" y="130" width="100" height="20" rx="3" fill="#FFE4E6"/>
    <text x="695" y="144" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Validation Iter 5</text>
  </g>

  <!-- Summary Footer Box -->
  <rect x="50" y="180" width="710" height="40" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="405" y="205" fill="#334155" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Every sample is used for training exactly 4 times and for validation exactly 1 time &bull; Zero data is wasted</text>
</svg>'''

# 6. Figure 1.6: Step-by-Step 5-Fold Rotation Diagram
svgs["__SVG_KFOLD_ROTATION__"] = '''<svg viewBox="0 0 800 290" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Header Columns -->
  <text x="90" y="25" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Iteration</text>
  <text x="210" y="25" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Fold 1</text>
  <text x="310" y="25" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Fold 2</text>
  <text x="410" y="25" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Fold 3</text>
  <text x="510" y="25" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Fold 4</text>
  <text x="610" y="25" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Fold 5</text>
  <text x="710" y="25" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Score (s_i)</text>

  <!-- Row 1: Iteration 1 (Fold 1 is Val) -->
  <g>
    <rect x="40" y="40" width="100" height="34" rx="4" fill="#F1F5F9"/>
    <text x="90" y="62" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Iter 1</text>
    
    <rect x="170" y="40" width="80" height="34" rx="4" fill="#059669"/>
    <text x="210" y="62" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">VAL</text>

    <rect x="270" y="40" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="310" y="62" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="370" y="40" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="410" y="62" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="470" y="40" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="510" y="62" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="570" y="40" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="610" y="62" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <text x="710" y="62" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">s_1 = 95.8%</text>
  </g>

  <!-- Row 2: Iteration 2 (Fold 2 is Val) -->
  <g>
    <rect x="40" y="85" width="100" height="34" rx="4" fill="#F1F5F9"/>
    <text x="90" y="107" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Iter 2</text>
    
    <rect x="170" y="85" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="210" y="107" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="270" y="85" width="80" height="34" rx="4" fill="#059669"/>
    <text x="310" y="107" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">VAL</text>

    <rect x="370" y="85" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="410" y="107" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="470" y="85" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="510" y="107" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="570" y="85" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="610" y="107" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <text x="710" y="107" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">s_2 = 100.0%</text>
  </g>

  <!-- Row 3: Iteration 3 (Fold 3 is Val) -->
  <g>
    <rect x="40" y="130" width="100" height="34" rx="4" fill="#F1F5F9"/>
    <text x="90" y="152" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Iter 3</text>
    
    <rect x="170" y="130" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="210" y="152" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="270" y="130" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="310" y="152" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="370" y="130" width="80" height="34" rx="4" fill="#059669"/>
    <text x="410" y="152" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">VAL</text>

    <rect x="470" y="130" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="510" y="152" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="570" y="130" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="610" y="152" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <text x="710" y="152" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">s_3 = 95.8%</text>
  </g>

  <!-- Row 4: Iteration 4 (Fold 4 is Val) -->
  <g>
    <rect x="40" y="175" width="100" height="34" rx="4" fill="#F1F5F9"/>
    <text x="90" y="197" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Iter 4</text>
    
    <rect x="170" y="175" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="210" y="197" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="270" y="175" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="310" y="197" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="370" y="175" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="410" y="197" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="470" y="175" width="80" height="34" rx="4" fill="#059669"/>
    <text x="510" y="197" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">VAL</text>

    <rect x="570" y="175" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="610" y="197" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <text x="710" y="197" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">s_4 = 100.0%</text>
  </g>

  <!-- Row 5: Iteration 5 (Fold 5 is Val) -->
  <g>
    <rect x="40" y="220" width="100" height="34" rx="4" fill="#F1F5F9"/>
    <text x="90" y="242" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Iter 5</text>
    
    <rect x="170" y="220" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="210" y="242" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="270" y="220" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="310" y="242" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="370" y="220" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="410" y="242" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="470" y="220" width="80" height="34" rx="4" fill="#E0F2FE" stroke="#BAE6FD"/>
    <text x="510" y="242" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Train</text>

    <rect x="570" y="220" width="80" height="34" rx="4" fill="#059669"/>
    <text x="610" y="242" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">VAL</text>

    <text x="710" y="242" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">s_5 = 95.8%</text>
  </g>

  <!-- Summary Bottom Line -->
  <line x1="40" y1="265" x2="760" y2="265" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="400" y="282" fill="#059669" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">Mean Cross-Validation Accuracy = (95.8 + 100.0 + 95.8 + 100.0 + 95.8) / 5 = 97.50% &plusmn; 2.04%</text>
</svg>'''

# 7. Figure 1.7: Ordinary K-Fold vs Stratified K-Fold on Imbalanced Data
svgs["__SVG_ORDINARY_VS_STRATIFIED__"] = '''<svg viewBox="0 0 800 270" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Ordinary K-Fold vs Stratified K-Fold (100 Samples: 90% Class 0, 10% Class 1)</text>

  <!-- Left: Ordinary K-Fold (Irregular / Risky) -->
  <g>
    <rect x="30" y="45" width="350" height="205" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
    <rect x="45" y="58" width="160" height="24" rx="4" fill="#E11D48"/>
    <text x="125" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">&#10006; Ordinary K-Fold (Random)</text>

    <text x="45" y="105" fill="#881337" font-family="-apple-system, sans-serif" font-size="11">Folds receive random samples without balancing:</text>
    
    <text x="55" y="128" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; Fold 1: 19 Class 0 + <tspan fill="#DC2626" font-weight="700">1 Minority (5%)</tspan></text>
    <text x="55" y="148" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; Fold 2: 18 Class 0 + <tspan fill="#059669" font-weight="700">2 Minority (10%)</tspan></text>
    <text x="55" y="168" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; Fold 3: 19 Class 0 + <tspan fill="#DC2626" font-weight="700">1 Minority (5%)</tspan></text>
    <text x="55" y="188" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; Fold 4: 16 Class 0 + <tspan fill="#D97706" font-weight="700">4 Minority (20%!)</tspan></text>
    <text x="55" y="208" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; Fold 5: 18 Class 0 + <tspan fill="#059669" font-weight="700">2 Minority (10%)</tspan></text>

    <text x="205" y="238" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Severe fold-to-fold class distribution fluctuation!</text>
  </g>

  <!-- Right: Stratified K-Fold (Balanced / Representative) -->
  <g>
    <rect x="420" y="45" width="350" height="205" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
    <rect x="435" y="58" width="170" height="24" rx="4" fill="#059669"/>
    <text x="520" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">&check; Stratified K-Fold (Smart)</text>

    <text x="435" y="105" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11">Guarantees exact 10% class ratio in EVERY fold:</text>
    
    <text x="445" y="128" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; Fold 1: 18 Class 0 + <tspan fill="#059669" font-weight="700">2 Minority (10.0%)</tspan> &check;</text>
    <text x="445" y="148" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; Fold 2: 18 Class 0 + <tspan fill="#059669" font-weight="700">2 Minority (10.0%)</tspan> &check;</text>
    <text x="445" y="168" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; Fold 3: 18 Class 0 + <tspan fill="#059669" font-weight="700">2 Minority (10.0%)</tspan> &check;</text>
    <text x="445" y="188" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; Fold 4: 18 Class 0 + <tspan fill="#059669" font-weight="700">2 Minority (10.0%)</tspan> &check;</text>
    <text x="445" y="208" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; Fold 5: 18 Class 0 + <tspan fill="#059669" font-weight="700">2 Minority (10.0%)</tspan> &check;</text>

    <text x="595" y="238" fill="#047857" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Every fold is an exact miniature mirror of the real dataset!</text>
  </g>
</svg>'''

# 8. Figure 1.8: LOOCV, Repeated K-Fold, Group K-Fold Comparison
svgs["__SVG_CV_STRATEGIES_COMPARE__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Card 1: Leave-One-Out (LOOCV) -->
  <g>
    <rect x="25" y="20" width="230" height="200" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <rect x="40" y="32" width="140" height="22" rx="4" fill="#0284C7"/>
    <text x="110" y="47" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Leave-One-Out (LOOCV)</text>

    <text x="40" y="78" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">K = N (N Fits)</text>
    <text x="40" y="98" fill="#334155" font-family="-apple-system, sans-serif" font-size="11">Each observation is validation once; remaining N&minus;1 train.</text>
    
    <rect x="40" y="125" width="200" height="40" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="140" y="142" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Deterministic (Zero randomness)</text>
    <text x="140" y="156" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Costly for large N; high variance</text>

    <text x="140" y="195" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Ideal for: Tiny datasets (N &lt; 50)</text>
  </g>

  <!-- Card 2: Repeated K-Fold -->
  <g>
    <rect x="285" y="20" width="230" height="200" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
    <rect x="300" y="32" width="130" height="22" rx="4" fill="#7E22CE"/>
    <text x="365" y="47" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Repeated K-Fold</text>

    <text x="300" y="78" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">e.g. 5 Folds &times; 10 Repeats</text>
    <text x="300" y="98" fill="#334155" font-family="-apple-system, sans-serif" font-size="11">Shuffles and splits data 10 times, computing 50 scores.</text>
    
    <rect x="300" y="125" width="200" height="40" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="400" y="142" fill="#581C87" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Quantifies split variance</text>
    <text x="400" y="156" fill="#D97706" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Multiplies training time by repeats</text>

    <text x="400" y="195" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Ideal for: Rigorous benchmarking</text>
  </g>

  <!-- Card 3: Group K-Fold -->
  <g>
    <rect x="545" y="20" width="230" height="200" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
    <rect x="560" y="32" width="120" height="22" rx="4" fill="#059669"/>
    <text x="620" y="47" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Group K-Fold</text>

    <text x="560" y="78" fill="#047857" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Entity / Subject Aware</text>
    <text x="560" y="98" fill="#334155" font-family="-apple-system, sans-serif" font-size="11">Keeps all records from same patient or device in same fold.</text>
    
    <rect x="560" y="125" width="200" height="40" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
    <text x="660" y="142" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Prevents subject identity leak</text>
    <text x="660" y="156" fill="#047857" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Zero group overlap between folds</text>

    <text x="660" y="195" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Ideal for: Healthcare, IoT sensors</text>
  </g>
</svg>'''

# 9. Figure 1.9: Time-Series Validation Expanding Window Timeline
svgs["__SVG_TIMESERIES_SPLIT__"] = '''<svg viewBox="0 0 800 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Time-Series Cross-Validation (Expanding Window / Rolling Origin)</text>
  <text x="400" y="46" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Strict chronological order is preserved. Never train on future data to predict the past!</text>

  <!-- Timeline Arrow -->
  <line x1="80" y1="65" x2="720" y2="65" stroke="#94A3B8" stroke-width="2" marker-end="url(#arr-time)"/>
  <text x="80" y="58" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10">Day 1 (Past)</text>
  <text x="700" y="58" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10">Day 100 (Future)</text>

  <!-- Split 1 -->
  <g>
    <text x="70" y="100" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Split 1</text>
    <rect x="120" y="85" width="140" height="26" rx="4" fill="#0284C7"/>
    <text x="190" y="102" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Train: Days 1&ndash;20</text>
    
    <rect x="270" y="85" width="70" height="26" rx="4" fill="#059669"/>
    <text x="305" y="102" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Val: 21&ndash;30</text>
  </g>

  <!-- Split 2 -->
  <g>
    <text x="70" y="138" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Split 2</text>
    <rect x="120" y="123" width="220" height="26" rx="4" fill="#0284C7"/>
    <text x="230" y="140" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Train: Days 1&ndash;40</text>
    
    <rect x="350" y="123" width="70" height="26" rx="4" fill="#059669"/>
    <text x="385" y="140" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Val: 41&ndash;50</text>
  </g>

  <!-- Split 3 -->
  <g>
    <text x="70" y="176" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Split 3</text>
    <rect x="120" y="161" width="300" height="26" rx="4" fill="#0284C7"/>
    <text x="270" y="178" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Train: Days 1&ndash;60</text>
    
    <rect x="430" y="161" width="70" height="26" rx="4" fill="#059669"/>
    <text x="465" y="178" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Val: 61&ndash;70</text>
  </g>

  <!-- Split 4 -->
  <g>
    <text x="70" y="214" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Split 4</text>
    <rect x="120" y="199" width="380" height="26" rx="4" fill="#0284C7"/>
    <text x="310" y="216" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Train: Days 1&ndash;80</text>
    
    <rect x="510" y="199" width="70" height="26" rx="4" fill="#059669"/>
    <text x="545" y="216" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Val: 81&ndash;90</text>
  </g>

  <!-- Split 5 -->
  <g>
    <text x="70" y="252" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Split 5</text>
    <rect x="120" y="237" width="460" height="26" rx="4" fill="#0284C7"/>
    <text x="350" y="254" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Train: Days 1&ndash;90 (Expanding Window)</text>
    
    <rect x="590" y="237" width="80" height="26" rx="4" fill="#059669"/>
    <text x="630" y="254" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Val: 91&ndash;100</text>
  </g>

  <defs>
    <marker id="arr-time" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#94A3B8"/>
    </marker>
  </defs>
</svg>'''

# 10. Figure 1.10: Actual 5-Fold Score Graph from Executed Iris Workflow
svgs["__SVG_ACTUAL_FOLD_SCORES__"] = '''<svg viewBox="0 0 800 270" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Executed 5-Fold Cross-Validation Scores (Iris Dataset, N_train = 120)</text>

  <!-- Y-Axis Ticks & Grid (Range: 90% to 102%) -->
  <line x1="80" y1="210" x2="720" y2="210" stroke="#E2E8F0" stroke-width="1"/>
  <text x="70" y="214" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="end">90.0%</text>

  <line x1="80" y1="165" x2="720" y2="165" stroke="#E2E8F0" stroke-width="1"/>
  <text x="70" y="169" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="end">95.0%</text>

  <line x1="80" y1="120" x2="720" y2="120" stroke="#E2E8F0" stroke-width="1"/>
  <text x="70" y="124" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="end">100.0%</text>

  <!-- Axes lines -->
  <line x1="80" y1="210" x2="720" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="80" y1="210" x2="80" y2="50" stroke="#94A3B8" stroke-width="1.5"/>

  <!-- Standard Deviation Band: 97.50% +/- 2.04% (95.46% to 99.54%) -->
  <rect x="80" y="124" width="640" height="36" fill="#D1FAE5" fill-opacity="0.4"/>

  <!-- Mean Line: 97.50% (Y = 142.5) -->
  <line x1="80" y1="142" x2="720" y2="142" stroke="#059669" stroke-width="2.5" stroke-dasharray="5 5"/>
  <text x="725" y="146" fill="#059669" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Mean: 97.50%</text>

  <!-- Bars for the 5 folds -->
  <!-- Fold 1: 95.83% (height = 52px, y = 158) -->
  <rect x="130" y="158" width="70" height="52" rx="4" fill="#0284C7"/>
  <text x="165" y="188" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">95.83%</text>
  <text x="165" y="228" fill="#334155" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Fold 1</text>

  <!-- Fold 2: 100.00% (height = 90px, y = 120) -->
  <rect x="250" y="120" width="70" height="90" rx="4" fill="#059669"/>
  <text x="285" y="155" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">100.00%</text>
  <text x="285" y="228" fill="#334155" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Fold 2</text>

  <!-- Fold 3: 95.83% (height = 52px, y = 158) -->
  <rect x="370" y="158" width="70" height="52" rx="4" fill="#0284C7"/>
  <text x="405" y="188" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">95.83%</text>
  <text x="405" y="228" fill="#334155" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Fold 3</text>

  <!-- Fold 4: 100.00% (height = 90px, y = 120) -->
  <rect x="490" y="120" width="70" height="90" rx="4" fill="#059669"/>
  <text x="525" y="155" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">100.00%</text>
  <text x="525" y="228" fill="#334155" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Fold 4</text>

  <!-- Fold 5: 95.83% (height = 52px, y = 158) -->
  <rect x="610" y="158" width="70" height="52" rx="4" fill="#0284C7"/>
  <text x="645" y="188" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">95.83%</text>
  <text x="645" y="228" fill="#334155" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Fold 5</text>

  <!-- Caption Footer -->
  <text x="400" y="255" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Mean Score = 97.50% &bull; Sample Standard Deviation = 2.04% &bull; Single split was only 93.3%</text>
</svg>'''

# 11. Figure 1.11: Hyperparameter Tuning Workflow
svgs["__SVG_HYPERPARAM_WORKFLOW__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Step 1: Candidate Configurations -->
  <g>
    <rect x="25" y="45" width="160" height="150" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="35" y="58" width="140" height="24" rx="4" fill="#475569"/>
    <text x="105" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. Candidate Grid</text>
    <text x="35" y="105" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; k = [1, 3, 5, 7, 9, 11]</text>
    <text x="35" y="125" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">&bull; weights = [unif, dist]</text>
    <text x="35" y="148" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">12 Total Combos</text>
    <text x="105" y="178" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Defined before search</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 195 120 L 220 120" stroke="#059669" stroke-width="2.5" marker-end="url(#arr-green)"/>

  <!-- Step 2: Inner K-Fold CV -->
  <g>
    <rect x="230" y="45" width="180" height="150" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="2"/>
    <rect x="245" y="58" width="150" height="24" rx="4" fill="#059669"/>
    <text x="320" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. 5-Fold Cross-Val</text>
    <text x="245" y="105" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="11">&bull; Fits each candidate 5&times;</text>
    <text x="245" y="125" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="11">&bull; Total fits: 12 &times; 5 = 60</text>
    <text x="245" y="148" fill="#047857" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Computes Mean CV</text>
    <text x="320" y="178" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Runs strictly on X_train</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 420 120 L 445 120" stroke="#059669" stroke-width="2.5"/>

  <!-- Step 3: Best Candidate & Refit -->
  <g>
    <rect x="455" y="45" width="165" height="150" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <rect x="470" y="58" width="135" height="24" rx="4" fill="#0284C7"/>
    <text x="537" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. Refit Best Model</text>
    <text x="470" y="105" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="11">&bull; Best: k=5, uniform</text>
    <text x="470" y="125" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="11">&bull; CV Score: 97.50%</text>
    <text x="470" y="148" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Refit on all X_train</text>
    <text x="537" y="178" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Produces best_estimator_</text>
  </g>

  <!-- Arrow 3 -->
  <path d="M 630 120 L 655 120" stroke="#059669" stroke-width="2.5"/>

  <!-- Step 4: Final Test Evaluation -->
  <g>
    <rect x="665" y="45" width="115" height="150" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
    <rect x="675" y="58" width="95" height="24" rx="4" fill="#7E22CE"/>
    <text x="722" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">4. Test Check</text>
    <text x="675" y="105" fill="#581C87" font-family="-apple-system, sans-serif" font-size="11">&bull; Sealed test set</text>
    <text x="675" y="125" fill="#581C87" font-family="-apple-system, sans-serif" font-size="11">&bull; N = 30</text>
    <text x="675" y="148" fill="#7E22CE" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Test: 100.0%</text>
    <text x="722" y="178" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Checked ONCE</text>
  </g>
</svg>'''

# 12. Figure 1.12: Grid Search vs Randomized Search Comparison
svgs["__SVG_GRID_VS_RANDOM__"] = '''<svg viewBox="0 0 800 260" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Hyperparameter Space Exploration: GridSearchCV vs RandomizedSearchCV</text>

  <!-- Left: GridSearchCV (Exhaustive 25 Points) -->
  <g>
    <rect x="35" y="45" width="340" height="200" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="50" y="55" width="120" height="22" rx="4" fill="#0284C7"/>
    <text x="110" y="70" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">GridSearchCV</text>
    <text x="180" y="71" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11">Exhaustive Cartesian Grid</text>

    <!-- 5x5 Grid Points -->
    <rect x="80" y="90" width="140" height="110" fill="#FFFFFF" stroke="#E2E8F0" rx="4"/>
    <!-- Horizontal lines -->
    <line x1="80" y1="112" x2="220" y2="112" stroke="#F1F5F9"/><line x1="80" y1="134" x2="220" y2="134" stroke="#F1F5F9"/>
    <line x1="80" y1="156" x2="220" y2="156" stroke="#F1F5F9"/><line x1="80" y1="178" x2="220" y2="178" stroke="#F1F5F9"/>
    <!-- 25 Points -->
    <circle cx="95" cy="100" r="4" fill="#0284C7"/><circle cx="122" cy="100" r="4" fill="#0284C7"/><circle cx="150" cy="100" r="4" fill="#0284C7"/><circle cx="178" cy="100" r="4" fill="#0284C7"/><circle cx="205" cy="100" r="4" fill="#0284C7"/>
    <circle cx="95" cy="122" r="4" fill="#0284C7"/><circle cx="122" cy="122" r="4" fill="#0284C7"/><circle cx="150" cy="122" r="4" fill="#0284C7"/><circle cx="178" cy="122" r="4" fill="#0284C7"/><circle cx="205" cy="122" r="4" fill="#0284C7"/>
    <circle cx="95" cy="145" r="4" fill="#0284C7"/><circle cx="122" cy="145" r="4" fill="#0284C7"/><circle cx="150" cy="145" r="4" fill="#0284C7"/><circle cx="178" cy="145" r="4" fill="#0284C7"/><circle cx="205" cy="145" r="4" fill="#0284C7"/>
    <circle cx="95" cy="167" r="4" fill="#0284C7"/><circle cx="122" cy="167" r="4" fill="#0284C7"/><circle cx="150" cy="167" r="4" fill="#0284C7"/><circle cx="178" cy="167" r="4" fill="#0284C7"/><circle cx="205" cy="167" r="4" fill="#0284C7"/>
    <circle cx="95" cy="190" r="4" fill="#0284C7"/><circle cx="122" cy="190" r="4" fill="#0284C7"/><circle cx="150" cy="190" r="4" fill="#0284C7"/><circle cx="178" cy="190" r="4" fill="#0284C7"/><circle cx="205" cy="190" r="4" fill="#0284C7"/>

    <text x="240" y="115" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="11">&bull; Tests all 25 combos</text>
    <text x="240" y="135" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="11">&bull; Thorough, systematic</text>
    <text x="240" y="155" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="11">&bull; Exponential blowup</text>
    <text x="240" y="175" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10">Best for: &le; 3 params</text>
  </g>

  <!-- Right: RandomizedSearchCV (Random Sample 9 Points) -->
  <g>
    <rect x="425" y="45" width="340" height="200" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
    <rect x="440" y="55" width="150" height="22" rx="4" fill="#059669"/>
    <text x="515" y="70" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">RandomizedSearchCV</text>
    <text x="600" y="71" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11">Budgeted Random Sample</text>

    <!-- Random Scatter in same space -->
    <rect x="470" y="90" width="140" height="110" fill="#FFFFFF" stroke="#E2E8F0" rx="4"/>
    <circle cx="488" cy="105" r="5" fill="#059669"/><circle cx="530" cy="98" r="5" fill="#059669"/>
    <circle cx="585" cy="115" r="5" fill="#059669"/><circle cx="510" cy="130" r="5" fill="#059669"/>
    <circle cx="560" cy="142" r="5" fill="#059669"/><circle cx="495" cy="165" r="5" fill="#059669"/>
    <circle cx="545" cy="172" r="5" fill="#059669"/><circle cx="590" cy="185" r="5" fill="#059669"/>
    <circle cx="575" cy="95" r="5" fill="#059669"/>

    <text x="630" y="115" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="11">&bull; Tests n_iter points (9)</text>
    <text x="630" y="135" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="11">&bull; Covers wide space</text>
    <text x="630" y="155" fill="#059669" font-family="-apple-system, sans-serif" font-size="11">&bull; Fixed compute budget</text>
    <text x="630" y="175" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10">Best for: Wide search / continuous</text>
  </g>
</svg>'''

# 13. Figure 1.13: Actual Executed Learning Curve
svgs["__SVG_LEARNING_CURVE__"] = '''<svg viewBox="0 0 800 270" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Actual Executed Learning Curve (Decision Tree, Iris N_train = 96)</text>

  <!-- Axes lines -->
  <line x1="80" y1="210" x2="720" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="80" y1="210" x2="80" y2="50" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="400" y="245" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Training Set Size (Samples)</text>
  <text x="35" y="130" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" transform="rotate(-90 35 130)" text-anchor="middle">Accuracy Score</text>

  <!-- Y Ticks (88% to 102%) -->
  <text x="70" y="214" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="end">88.0%</text>
  <line x1="80" y1="160" x2="720" y2="160" stroke="#F1F5F9"/>
  <text x="70" y="164" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="end">94.0%</text>
  <line x1="80" y1="100" x2="720" y2="100" stroke="#F1F5F9"/>
  <text x="70" y="104" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="end">100.0%</text>

  <!-- X Ticks: 19, 38, 57, 76, 96 -->
  <text x="140" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">19</text>
  <text x="270" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">38</text>
  <text x="400" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">57</text>
  <text x="530" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">76</text>
  <text x="660" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">96</text>

  <!-- Training Score Curve (1.0000 -> 0.9947 -> 0.9825 -> 0.9816 -> 0.9792) -->
  <path d="M 140 100 L 270 105 L 400 117 L 530 118 L 660 120" fill="none" stroke="#0284C7" stroke-width="2.5"/>
  <circle cx="140" cy="100" r="4" fill="#0284C7"/><circle cx="270" cy="105" r="4" fill="#0284C7"/>
  <circle cx="400" cy="117" r="4" fill="#0284C7"/><circle cx="530" cy="118" r="4" fill="#0284C7"/>
  <circle cx="660" cy="120" r="4" fill="#0284C7"/>
  <text x="670" y="115" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Train: 97.9%</text>

  <!-- Validation Score Curve (0.9250 -> 0.9333 -> 0.9250 -> 0.9417 -> 0.9583) -->
  <path d="M 140 175 L 270 167 L 400 175 L 530 158 L 660 142" fill="none" stroke="#059669" stroke-width="2.5"/>
  <circle cx="140" cy="175" r="4" fill="#059669"/><circle cx="270" cy="167" r="4" fill="#059669"/>
  <circle cx="400" cy="175" r="4" fill="#059669"/><circle cx="530" cy="158" r="4" fill="#059669"/>
  <circle cx="660" cy="142" r="4" fill="#059669"/>
  <text x="670" y="148" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Val: 95.8%</text>

  <!-- Gap Shrink Note -->
  <text x="400" y="260" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">As sample size increases, training and validation curves converge: Gap shrinks from 7.50% &rarr; 2.08%</text>
</svg>'''

# 14. Figure 1.14: Actual Executed Validation Curve (max_depth 1 to 10)
svgs["__SVG_VALIDATION_CURVE__"] = '''<svg viewBox="0 0 800 270" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Actual Executed Validation Curve (Decision Tree max_depth, 1 to 10)</text>

  <!-- Axes -->
  <line x1="80" y1="210" x2="720" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="80" y1="210" x2="80" y2="50" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="400" y="245" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Hyperparameter: max_depth</text>
  <text x="35" y="130" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" transform="rotate(-90 35 130)" text-anchor="middle">Cross-Validation Score</text>

  <!-- Y Ticks (60% to 105%) -->
  <text x="70" y="214" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="end">60.0%</text>
  <line x1="80" y1="170" x2="720" y2="170" stroke="#F1F5F9"/>
  <text x="70" y="174" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="end">80.0%</text>
  <line x1="80" y1="110" x2="720" y2="110" stroke="#F1F5F9"/>
  <text x="70" y="114" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="end">100.0%</text>

  <!-- X Ticks: 1, 2, 3, 4, 5, 6, 8, 10 -->
  <text x="120" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">1</text>
  <text x="190" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">2</text>
  <text x="260" y="224" fill="#059669" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">3 &check;</text>
  <text x="330" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">4</text>
  <text x="400" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">5</text>
  <text x="470" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">6</text>
  <text x="560" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">8</text>
  <text x="650" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">10</text>

  <!-- Training Score Line (0.6667 -> 0.9667 -> 0.9792 -> 0.9938 -> 1.0000) -->
  <path d="M 120 196 L 190 120 L 260 116 L 330 112 L 400 110 L 470 110 L 560 110 L 650 110" fill="none" stroke="#0284C7" stroke-width="2.5"/>
  <circle cx="120" cy="196" r="4" fill="#0284C7"/><circle cx="190" cy="120" r="4" fill="#0284C7"/>
  <circle cx="260" cy="116" r="4" fill="#0284C7"/><circle cx="330" cy="112" r="4" fill="#0284C7"/>
  <circle cx="400" cy="110" r="4" fill="#0284C7"/><circle cx="650" cy="110" r="4" fill="#0284C7"/>
  <text x="660" y="105" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Train: 100%</text>

  <!-- Validation Score Line (0.6667 -> 0.9417 -> 0.9583 -> 0.9417 -> 0.9500 -> 0.9500) -->
  <path d="M 120 196 L 190 126 L 260 122 L 330 126 L 400 124 L 470 124 L 560 124 L 650 124" fill="none" stroke="#059669" stroke-width="2.5"/>
  <circle cx="120" cy="196" r="4" fill="#059669"/><circle cx="190" cy="126" r="4" fill="#059669"/>
  <circle cx="260" cy="122" r="6" fill="#059669"/><circle cx="330" cy="126" r="4" fill="#059669"/>
  <circle cx="400" cy="124" r="4" fill="#059669"/><circle cx="650" cy="124" r="4" fill="#059669"/>
  <text x="660" y="132" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Val: 95.0%</text>

  <!-- Optimal max_depth marker at 3 -->
  <line x1="260" y1="122" x2="260" y2="210" stroke="#059669" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="260" y="90" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" text-anchor="middle">Optimal max_depth = 3 (Val = 95.83%)</text>
  <text x="400" y="260" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Beyond depth 3, training accuracy hits 100% while validation drops &mdash; classic overfitting onset.</text>
</svg>'''

# 15. Figure 1.15: Data Leakage Comparison: Incorrect vs Safe Workflow
svgs["__SVG_LEAKAGE_COMPARISON__"] = '''<svg viewBox="0 0 800 250" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="26" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Data Preprocessing: Data Leakage Trap vs Leakage-Safe Workflow</text>

  <!-- Top: Wrong / Leaky Workflow -->
  <g>
    <rect x="25" y="45" width="750" height="85" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <rect x="40" y="55" width="130" height="20" rx="4" fill="#DC2626"/>
    <text x="105" y="69" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">&#10006; LEAKY WORKFLOW</text>

    <!-- Pipeline steps -->
    <rect x="180" y="55" width="130" height="30" rx="4" fill="#FFFFFF" stroke="#FCA5A5"/>
    <text x="245" y="74" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Full Dataset X</text>

    <text x="325" y="75" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="14">&rarr;</text>

    <rect x="345" y="55" width="180" height="30" rx="4" fill="#FFFFFF" stroke="#DC2626" stroke-width="2"/>
    <text x="435" y="74" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" text-anchor="middle">fit_transform(scaler) on ALL</text>

    <text x="540" y="75" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="14">&rarr;</text>

    <rect x="560" y="55" width="190" height="30" rx="4" fill="#FFFFFF" stroke="#FCA5A5"/>
    <text x="655" y="74" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Cross-Validation / Splitting</text>

    <text x="400" y="115" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CRITICAL BUG: Scaler calculated mean/std using test data! Test set information leaked into training folds!</text>
  </g>

  <!-- Bottom: Safe / Pipeline Workflow -->
  <g>
    <rect x="25" y="145" width="750" height="90" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="2"/>
    <rect x="40" y="155" width="130" height="20" rx="4" fill="#059669"/>
    <text x="105" y="169" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">&check; SAFE PIPELINE</text>

    <!-- Pipeline steps -->
    <rect x="180" y="155" width="130" height="30" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
    <text x="245" y="174" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Split into Folds First</text>

    <text x="325" y="175" fill="#059669" font-family="-apple-system, sans-serif" font-size="14">&rarr;</text>

    <rect x="345" y="155" width="180" height="30" rx="4" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
    <text x="435" y="174" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" text-anchor="middle">Fit Scaler on Train Fold Only</text>

    <text x="540" y="175" fill="#059669" font-family="-apple-system, sans-serif" font-size="14">&rarr;</text>

    <rect x="560" y="155" width="190" height="30" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
    <text x="655" y="174" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Transform Val Fold Safely</text>

    <text x="400" y="218" fill="#047857" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PROPER PRACTICE: Scaler parameters fit strictly inside each training fold &bull; Zero test contamination</text>
  </g>
</svg>'''

# 16. Figure 1.16: Leakage-Safe scikit-learn Pipeline Encapsulation Diagram
svgs["__SVG_PIPELINE_ARCHITECTURE__"] = '''<svg viewBox="0 0 800 230" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">scikit-learn Pipeline Architecture: Encapsulating Preprocessing with Model</text>

  <!-- Big Outer Container representing Pipeline Object -->
  <rect x="40" y="48" width="720" height="135" rx="10" fill="#F0FDF4" stroke="#059669" stroke-width="2" stroke-dasharray="6 4"/>
  <rect x="60" y="38" width="190" height="22" rx="4" fill="#059669"/>
  <text x="155" y="53" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Pipeline Object (Single Estimator)</text>

  <!-- Stage 1: StandardScaler -->
  <g>
    <rect x="80" y="75" width="220" height="85" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <rect x="95" y="88" width="130" height="20" rx="3" fill="#E0F2FE"/>
    <text x="160" y="102" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Step 1: ('scaler', StandardScaler())</text>
    <text x="95" y="128" fill="#334155" font-family="-apple-system, sans-serif" font-size="10">&bull; fit(): Computes mean &amp; std on train</text>
    <text x="95" y="145" fill="#334155" font-family="-apple-system, sans-serif" font-size="10">&bull; transform(): Scales z = (x &minus; &mu;) / &sigma;</text>
  </g>

  <!-- Connecting Arrow -->
  <path d="M 315 117 L 345 117" stroke="#059669" stroke-width="3" marker-end="url(#arr-green)"/>
  <text x="330" y="105" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Scaled X</text>

  <!-- Stage 2: Classifier / Regressor -->
  <g>
    <rect x="360" y="75" width="230" height="85" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <rect x="375" y="88" width="140" height="20" rx="3" fill="#D1FAE5"/>
    <text x="445" y="102" fill="#047857" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Step 2: ('clf', LogisticRegression())</text>
    <text x="375" y="128" fill="#334155" font-family="-apple-system, sans-serif" font-size="10">&bull; fit(): Optimizes weights using scaled train</text>
    <text x="375" y="145" fill="#334155" font-family="-apple-system, sans-serif" font-size="10">&bull; predict(): Predicts on scaled test samples</text>
  </g>

  <!-- Connecting Arrow to Output -->
  <path d="M 605 117 L 635 117" stroke="#059669" stroke-width="3"/>

  <!-- Final Output Badge -->
  <rect x="645" y="88" width="95" height="58" rx="6" fill="#059669"/>
  <text x="692" y="112" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Predictions</text>
  <text x="692" y="130" fill="#D1FAE5" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">&#375; (Clean)</text>

  <!-- Bottom Explanatory Caption -->
  <text x="400" y="208" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">When cross_val_score(pipeline, X, y) executes, Step 1 is automatically refit on each inner training fold!</text>
</svg>'''

# 17. Figure 1.17: Model Validation & Split Strategy Decision Tree
svgs["__SVG_CV_DECISION_TREE__"] = '''<svg viewBox="0 0 800 290" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="26" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Master Model Validation &amp; Cross-Validation Decision Tree</text>

  <!-- Root Question -->
  <rect x="300" y="42" width="200" height="35" rx="6" fill="#0F172A"/>
  <text x="400" y="64" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">What structure is your data?</text>

  <!-- Branch 1: Time Series -->
  <line x1="330" y1="77" x2="120" y2="120" stroke="#94A3B8" stroke-width="2"/>
  <text x="200" y="98" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Chronological / Dates</text>
  <rect x="40" y="120" width="160" height="50" rx="6" fill="#F0F9FF" stroke="#BAE6FD"/>
  <text x="120" y="140" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">TimeSeriesSplit</text>
  <text x="120" y="156" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Expanding / Rolling window</text>

  <!-- Branch 2: Grouped / Clustered -->
  <line x1="375" y1="77" x2="300" y2="120" stroke="#94A3B8" stroke-width="2"/>
  <text x="310" y="105" fill="#7E22CE" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Patient / Device</text>
  <rect x="220" y="120" width="160" height="50" rx="6" fill="#FAF5FF" stroke="#E9D5FF"/>
  <text x="300" y="140" fill="#7E22CE" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">GroupKFold</text>
  <text x="300" y="156" fill="#581C87" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Zero group overlap in splits</text>

  <!-- Branch 3: Imbalanced Classification -->
  <line x1="425" y1="77" x2="500" y2="120" stroke="#94A3B8" stroke-width="2"/>
  <text x="480" y="105" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Imbalanced Classes</text>
  <rect x="420" y="120" width="160" height="50" rx="6" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="500" y="140" fill="#059669" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">StratifiedKFold</text>
  <text x="500" y="156" fill="#065F46" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Preserves class proportions</text>

  <!-- Branch 4: Standard Tabular / Regression -->
  <line x1="470" y1="77" x2="680" y2="120" stroke="#94A3B8" stroke-width="2"/>
  <text x="600" y="98" fill="#D97706" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Standard I.I.D.</text>
  <rect x="600" y="120" width="160" height="50" rx="6" fill="#FFFBEB" stroke="#FDE68A"/>
  <text x="680" y="140" fill="#D97706" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Standard KFold</text>
  <text x="680" y="156" fill="#78350F" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">5 or 10 folds with shuffle</text>

  <!-- Bottom Golden Rule Box -->
  <rect x="40" y="195" width="720" height="65" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="400" y="220" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">Golden Principle: Model validation must replicate how the model will encounter data in the real world.</text>
  <text x="400" y="242" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">If deployed models predict tomorrow from yesterday, use TimeSeriesSplit. If predicting new patients, use GroupKFold.</text>
</svg>'''

# 18. Figure 1.18: Cross-Validation vs Single Split vs Final Test Comparison
svgs["__SVG_CV_VS_TEST_COMPARE__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Comparative Accuracy: Single Split vs 5-Fold Cross-Validation vs Final Test Set</text>

  <!-- 3 Comparison Bars -->
  <!-- Bar 1: Single Train/Val Split (Pessimistic Artifact) -->
  <g>
    <rect x="80" y="60" width="180" height="130" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="170" y="85" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Single Train/Val Split</text>
    <text x="170" y="125" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="28" font-weight="800" text-anchor="middle">93.33%</text>
    <text x="170" y="152" fill="#7F1D1D" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Subject to bad luck in 1 split</text>
    <text x="170" y="168" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">High variance &bull; Noisy estimate</text>
  </g>

  <!-- Bar 2: 5-Fold Cross-Validation (Stable Benchmark) -->
  <g>
    <rect x="310" y="55" width="180" height="140" rx="8" fill="#ECFDF5" stroke="#059669" stroke-width="2"/>
    <rect x="330" y="45" width="140" height="20" rx="4" fill="#059669"/>
    <text x="400" y="59" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" text-anchor="middle">RELIABLE ESTIMATE</text>

    <text x="400" y="85" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">5-Fold CV (X_train)</text>
    <text x="400" y="125" fill="#059669" font-family="-apple-system, sans-serif" font-size="28" font-weight="800" text-anchor="middle">97.50%</text>
    <text x="400" y="152" fill="#047857" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">&plusmn; 2.04% Std Dev</text>
    <text x="400" y="168" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Averages out single-split noise</text>
  </g>

  <!-- Bar 3: Final Test Set Evaluation (Unbiased Vault) -->
  <g>
    <rect x="540" y="60" width="180" height="130" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
    <text x="630" y="85" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Final Test Set (Held-Out)</text>
    <text x="630" y="125" fill="#7E22CE" font-family="-apple-system, sans-serif" font-size="28" font-weight="800" text-anchor="middle">100.0%</text>
    <text x="630" y="152" fill="#581C87" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Evaluated strictly ONCE</text>
    <text x="630" y="168" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Confirms generalization on vault</text>
  </g>

  <!-- Bottom Explanatory Summary -->
  <text x="400" y="222" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Cross-validation protected model selection from the noisy 93.3% single split and guided GridSearchCV to the optimal parameter (k=5).</text>
</svg>'''

if __name__ == "__main__":
    print(f"Generated {len(svgs)} SVGs for Topic 20.")
    for k in svgs:
        print(f"  {k}")
