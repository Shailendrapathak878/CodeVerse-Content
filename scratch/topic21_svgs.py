# Topic 21 SVG Graphics Generation Script - 20 Verified Vector SVGs
# Strict Light Mode Only, 100% Valid XML, Rose & Vibrant Crimson Theme

svgs = {}

# 1. Figure 1.1: Model Fitting, Capacity, and Generalization Lifecycle
svgs["__SVG_FIT_WORKFLOW__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Step 1: Historical Data -->
  <g>
    <rect x="25" y="45" width="155" height="150" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="40" y="58" width="125" height="24" rx="4" fill="#64748B"/>
    <text x="102" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. Training Data</text>
    <text x="102" y="105" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">(X_train, y_train)</text>
    <text x="35" y="130" fill="#475569" font-family="-apple-system, sans-serif" font-size="10.5">• Observed samples</text>
    <text x="35" y="148" fill="#475569" font-family="-apple-system, sans-serif" font-size="10.5">• Contains true signal</text>
    <text x="35" y="166" fill="#475569" font-family="-apple-system, sans-serif" font-size="10.5">• Contains random noise</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 190 120 L 215 120" stroke="#E11D48" stroke-width="2.5" marker-end="url(#arr-rose)"/>

  <!-- Step 2: Learning & Capacity -->
  <g>
    <rect x="225" y="45" width="165" height="150" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="2"/>
    <rect x="240" y="58" width="135" height="24" rx="4" fill="#E11D48"/>
    <text x="307" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. Model Fitting</text>
    <text x="307" y="105" fill="#9F1239" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Algorithm &amp; Capacity</text>
    <text x="235" y="130" fill="#881337" font-family="-apple-system, sans-serif" font-size="10.5">• Minimizes loss function</text>
    <text x="235" y="148" fill="#881337" font-family="-apple-system, sans-serif" font-size="10.5">• Adjusts weights (w, b)</text>
    <text x="235" y="166" fill="#881337" font-family="-apple-system, sans-serif" font-size="10.5">• Governed by complexity</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 400 120 L 425 120" stroke="#E11D48" stroke-width="2.5" marker-end="url(#arr-rose)"/>

  <!-- Step 3: The 3 Fitting Outcomes -->
  <g>
    <rect x="435" y="35" width="170" height="170" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <rect x="450" y="48" width="140" height="24" rx="4" fill="#0284C7"/>
    <text x="520" y="64" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. Fitting States</text>
    <rect x="445" y="80" width="150" height="26" rx="4" fill="#FEF3C7" stroke="#FDE68A"/>
    <text x="520" y="97" fill="#92400E" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Underfitting (Too Simple)</text>
    <rect x="445" y="112" width="150" height="26" rx="4" fill="#ECFDF5" stroke="#A7F3D0"/>
    <text x="520" y="129" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">✓ Good Fit (Balanced)</text>
    <rect x="445" y="144" width="150" height="26" rx="4" fill="#FEE2E2" stroke="#FECACA"/>
    <text x="520" y="161" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Overfitting (Noise-Fitting)</text>
  </g>

  <!-- Arrow 3 -->
  <path d="M 615 120 L 640 120" stroke="#E11D48" stroke-width="2.5" marker-end="url(#arr-rose)"/>

  <!-- Step 4: Generalization on Unseen Data -->
  <g>
    <rect x="650" y="45" width="125" height="150" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
    <rect x="660" y="58" width="105" height="24" rx="4" fill="#7E22CE"/>
    <text x="712" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">4. Test Data</text>
    <text x="712" y="105" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Generalization</text>
    <text x="660" y="130" fill="#581C87" font-family="-apple-system, sans-serif" font-size="10.5">• True test error</text>
    <text x="660" y="148" fill="#581C87" font-family="-apple-system, sans-serif" font-size="10.5">• Real-world value</text>
    <text x="660" y="166" fill="#581C87" font-family="-apple-system, sans-serif" font-size="10.5">• Unbiased judge</text>
  </g>

  <defs>
    <marker id="arr-rose" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#E11D48"/>
    </marker>
  </defs>
</svg>'''

# 2. Figure 2.1: Underfitting (High Bias)
svgs["__SVG_UNDERFITTING_DEMO__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="24" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Underfitting: A Straight Line Forced onto Non-Linear Curved Data</text>

  <!-- Plot Area -->
  <line x1="80" y1="190" x2="720" y2="190" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="80" y1="190" x2="80" y2="40" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="725" y="194" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11">Feature (X)</text>
  <text x="80" y="32" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Target (y)</text>

  <!-- Underlying True Non-Linear Curve (Soft Gray Dashed) -->
  <path d="M 90 60 Q 250 200 400 120 T 710 70" fill="none" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="4 4"/>
  <text x="620" y="55" fill="#94A3B8" font-family="-apple-system, sans-serif" font-size="10">True Signal f(X)</text>

  <!-- Scatter points -->
  <circle cx="120" cy="85" r="4.5" fill="#0284C7"/>
  <circle cx="170" cy="135" r="4.5" fill="#0284C7"/>
  <circle cx="230" cy="175" r="4.5" fill="#0284C7"/>
  <circle cx="290" cy="170" r="4.5" fill="#0284C7"/>
  <circle cx="350" cy="140" r="4.5" fill="#0284C7"/>
  <circle cx="410" cy="115" r="4.5" fill="#0284C7"/>
  <circle cx="470" cy="85" r="4.5" fill="#0284C7"/>
  <circle cx="530" cy="70" r="4.5" fill="#0284C7"/>
  <circle cx="590" cy="75" r="4.5" fill="#0284C7"/>
  <circle cx="650" cy="95" r="4.5" fill="#0284C7"/>
  <circle cx="690" cy="80" r="4.5" fill="#0284C7"/>

  <!-- Underfit Straight Line (Red) -->
  <line x1="90" y1="160" x2="710" y2="70" stroke="#DC2626" stroke-width="3"/>
  <text x="500" y="115" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">Fitted Line (Degree 1): High Bias</text>

  <!-- Residual Callout -->
  <line x1="230" y1="175" x2="230" y2="139" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="2 2"/>
  <text x="240" y="160" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="10">Large Systematic Error</text>

  <!-- Summary Box -->
  <rect x="520" y="135" width="190" height="48" rx="6" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="530" y="152" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">• High Training Error</text>
  <text x="530" y="169" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">• High Validation Error</text>
</svg>'''

# 3. Figure 3.1: Good Fit (Optimal Generalization)
svgs["__SVG_GOODFIT_DEMO__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="24" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Good Fit: Captures Underlying Non-Linear Trend Without Fitting Noise</text>

  <!-- Plot Area -->
  <line x1="80" y1="190" x2="720" y2="190" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="80" y1="190" x2="80" y2="40" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="725" y="194" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11">Feature (X)</text>
  <text x="80" y="32" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Target (y)</text>

  <!-- Scatter points -->
  <circle cx="120" cy="85" r="4.5" fill="#0284C7"/>
  <circle cx="170" cy="135" r="4.5" fill="#0284C7"/>
  <circle cx="230" cy="175" r="4.5" fill="#0284C7"/>
  <circle cx="290" cy="170" r="4.5" fill="#0284C7"/>
  <circle cx="350" cy="140" r="4.5" fill="#0284C7"/>
  <circle cx="410" cy="115" r="4.5" fill="#0284C7"/>
  <circle cx="470" cy="85" r="4.5" fill="#0284C7"/>
  <circle cx="530" cy="70" r="4.5" fill="#0284C7"/>
  <circle cx="590" cy="75" r="4.5" fill="#0284C7"/>
  <circle cx="650" cy="95" r="4.5" fill="#0284C7"/>
  <circle cx="690" cy="80" r="4.5" fill="#0284C7"/>

  <!-- Good Fit Smooth Polynomial (Green) -->
  <path d="M 90 62 Q 250 195 400 120 T 710 72" fill="none" stroke="#059669" stroke-width="3"/>
  <text x="450" y="135" fill="#059669" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">Fitted Model (Degree 3): Ideal Generalization</text>

  <!-- Summary Box -->
  <rect x="520" y="135" width="190" height="48" rx="6" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="530" y="152" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">• Low Training Error</text>
  <text x="530" y="169" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">• Low Validation Error (Optimal)</text>
</svg>'''

# 4. Figure 4.1: Overfitting (High Variance)
svgs["__SVG_OVERFITTING_DEMO__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="24" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Overfitting: Excessively Complex Model Interpolating Random Noise</text>

  <!-- Plot Area -->
  <line x1="80" y1="190" x2="720" y2="190" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="80" y1="190" x2="80" y2="40" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="725" y="194" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11">Feature (X)</text>
  <text x="80" y="32" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Target (y)</text>

  <!-- Wildly Oscillating Overfit Polynomial (Purple) -->
  <path d="M 90 120 C 105 40 115 85 120 85 C 140 85 160 145 170 135 C 190 110 210 185 230 175 C 260 155 275 180 290 170 C 320 145 340 155 350 140 C 370 100 395 130 410 115 C 430 90 455 70 470 85 C 490 115 515 55 530 70 C 550 95 575 60 590 75 C 610 105 635 80 650 95 C 670 125 680 70 690 80 L 710 150" fill="none" stroke="#7E22CE" stroke-width="2.5"/>

  <!-- Scatter points directly on curve -->
  <circle cx="120" cy="85" r="4.5" fill="#0284C7"/>
  <circle cx="170" cy="135" r="4.5" fill="#0284C7"/>
  <circle cx="230" cy="175" r="4.5" fill="#0284C7"/>
  <circle cx="290" cy="170" r="4.5" fill="#0284C7"/>
  <circle cx="350" cy="140" r="4.5" fill="#0284C7"/>
  <circle cx="410" cy="115" r="4.5" fill="#0284C7"/>
  <circle cx="470" cy="85" r="4.5" fill="#0284C7"/>
  <circle cx="530" cy="70" r="4.5" fill="#0284C7"/>
  <circle cx="590" cy="75" r="4.5" fill="#0284C7"/>
  <circle cx="650" cy="95" r="4.5" fill="#0284C7"/>
  <circle cx="690" cy="80" r="4.5" fill="#0284C7"/>

  <text x="350" y="45" fill="#7E22CE" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">High-Degree Polynomial: Memorized Noise (High Variance)</text>

  <!-- Summary Box -->
  <rect x="520" y="135" width="190" height="48" rx="6" fill="#FAF5FF" stroke="#E9D5FF"/>
  <text x="530" y="152" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">• Training Error ≈ 0.0 (Memorized)</text>
  <text x="530" y="169" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">• Validation Error → Explodes!</text>
</svg>'''

# 5. Figure 5.1: Side-by-Side Comparison: Underfit vs Good Fit vs Overfit
svgs["__SVG_SIDE_BY_SIDE_FIT__"] = '''<svg viewBox="0 0 800 250" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Panel 1: Underfitting -->
  <g>
    <rect x="15" y="20" width="245" height="215" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
    <rect x="30" y="32" width="120" height="22" rx="4" fill="#D97706"/>
    <text x="90" y="47" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Underfitting</text>
    
    <!-- Mini Plot -->
    <line x1="30" y1="140" x2="245" y2="140" stroke="#CBD5E1"/>
    <!-- Line on curve -->
    <circle cx="50" cy="120" r="3.5" fill="#0284C7"/>
    <circle cx="90" cy="135" r="3.5" fill="#0284C7"/>
    <circle cx="130" cy="130" r="3.5" fill="#0284C7"/>
    <circle cx="170" cy="100" r="3.5" fill="#0284C7"/>
    <circle cx="210" cy="80" r="3.5" fill="#0284C7"/>
    <circle cx="235" cy="85" r="3.5" fill="#0284C7"/>
    <line x1="45" y1="130" x2="240" y2="85" stroke="#DC2626" stroke-width="2.5"/>

    <text x="137" y="165" fill="#92400E" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">High Bias • Too Rigid</text>
    <text x="30" y="186" fill="#78350F" font-family="-apple-system, sans-serif" font-size="10">• Train Error: High (0.187)</text>
    <text x="30" y="202" fill="#78350F" font-family="-apple-system, sans-serif" font-size="10">• Val Error: High (0.288)</text>
    <text x="30" y="218" fill="#92400E" font-family="-apple-system, sans-serif" font-size="10" font-weight="600">• Fix: Increase model capacity</text>
  </g>

  <!-- Panel 2: Good Fit (Ideal) -->
  <g>
    <rect x="275" y="20" width="250" height="215" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="2"/>
    <rect x="290" y="32" width="130" height="22" rx="4" fill="#059669"/>
    <text x="355" y="47" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">✓ Good Fit (Ideal)</text>
    
    <!-- Mini Plot -->
    <line x1="290" y1="140" x2="510" y2="140" stroke="#CBD5E1"/>
    <circle cx="310" cy="120" r="3.5" fill="#0284C7"/>
    <circle cx="350" cy="135" r="3.5" fill="#0284C7"/>
    <circle cx="390" cy="130" r="3.5" fill="#0284C7"/>
    <circle cx="430" cy="100" r="3.5" fill="#0284C7"/>
    <circle cx="470" cy="80" r="3.5" fill="#0284C7"/>
    <circle cx="495" cy="85" r="3.5" fill="#0284C7"/>
    <path d="M 305 115 Q 370 145 440 95 T 505 82" fill="none" stroke="#059669" stroke-width="2.5"/>

    <text x="400" y="165" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Balanced • Generalizes</text>
    <text x="290" y="186" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="10">• Train Error: Low (0.018)</text>
    <text x="290" y="202" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="10">• Val Error: Low (0.018)</text>
    <text x="290" y="218" fill="#047857" font-family="-apple-system, sans-serif" font-size="10" font-weight="600">• Action: Deploy with confidence</text>
  </g>

  <!-- Panel 3: Overfitting -->
  <g>
    <rect x="540" y="20" width="245" height="215" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <rect x="555" y="32" width="115" height="22" rx="4" fill="#E11D48"/>
    <text x="612" y="47" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Overfitting</text>
    
    <!-- Mini Plot -->
    <line x1="555" y1="140" x2="770" y2="140" stroke="#CBD5E1"/>
    <circle cx="575" cy="120" r="3.5" fill="#0284C7"/>
    <circle cx="615" cy="135" r="3.5" fill="#0284C7"/>
    <circle cx="655" cy="130" r="3.5" fill="#0284C7"/>
    <circle cx="695" cy="100" r="3.5" fill="#0284C7"/>
    <circle cx="735" cy="80" r="3.5" fill="#0284C7"/>
    <circle cx="760" cy="85" r="3.5" fill="#0284C7"/>
    <path d="M 570 135 C 575 100 580 120 575 120 C 595 120 605 145 615 135 C 635 110 645 135 655 130 C 675 120 685 90 695 100 C 715 110 725 70 735 80 L 765 85" fill="none" stroke="#E11D48" stroke-width="2.5"/>

    <text x="662" y="165" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">High Variance • Memorized</text>
    <text x="555" y="186" fill="#7F1D1D" font-family="-apple-system, sans-serif" font-size="10">• Train Error: ~0.0 (0.010)</text>
    <text x="555" y="202" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">• Val Error: High (0.024+)</text>
    <text x="555" y="218" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10" font-weight="600">• Fix: Regularize or gather data</text>
  </g>
</svg>'''

# 6. Figure 6.1: Training Error vs Validation Error as Model Complexity Grows
svgs["__SVG_TRAIN_VAL_ERROR_CURVE__"] = '''<svg viewBox="0 0 800 260" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="26" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Training Error vs Validation Error across Model Complexity</text>

  <!-- Axes -->
  <line x1="90" y1="210" x2="720" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="90" y1="210" x2="90" y2="45" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="400" y="235" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Model Complexity (Degree, Tree Depth, Free Parameters) →</text>
  <text x="80" y="40" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Prediction Error</text>

  <!-- Sweet Spot Corridor -->
  <rect x="360" y="45" width="90" height="165" fill="#ECFDF5" fill-opacity="0.6"/>
  <line x1="405" y1="45" x2="405" y2="210" stroke="#059669" stroke-width="2" stroke-dasharray="4 4"/>
  <text x="405" y="40" fill="#059669" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Optimal Sweet Spot</text>

  <!-- Underfitting / Overfitting Zone Labels -->
  <text x="210" y="60" fill="#D97706" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">← Underfitting Zone (High Bias)</text>
  <text x="590" y="60" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Overfitting Zone (High Variance) →</text>

  <!-- Training Error Curve (Monotonically decreasing) -->
  <path d="M 100 180 Q 250 160 405 100 T 710 55" fill="none" stroke="#0284C7" stroke-width="3"/>
  <text x="715" y="60" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Training Error</text>

  <!-- Validation Error Curve (U-shaped) -->
  <path d="M 100 195 C 220 180 320 120 405 95 C 500 95 610 145 710 205" fill="none" stroke="#E11D48" stroke-width="3"/>
  <text x="715" y="210" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Validation Error</text>

  <!-- Generalization Gap Double Arrow at high complexity -->
  <line x1="680" y1="65" x2="680" y2="185" stroke="#9F1239" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="685" y="125" fill="#9F1239" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Generalization Gap</text>
</svg>'''

# 7. Figure 7.1: Bias vs Variance Intuition: Target Dartboards
svgs["__SVG_BIAS_VARIANCE_INTUITION__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Dartboard 1: Low Bias, Low Variance (Bullseye!) -->
  <g transform="translate(40, 30)">
    <circle cx="70" cy="70" r="60" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="42" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="24" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
    <!-- Tightly clustered in center -->
    <circle cx="71" cy="69" r="3" fill="#E11D48"/>
    <circle cx="68" cy="72" r="3" fill="#E11D48"/>
    <circle cx="73" cy="71" r="3" fill="#E11D48"/>
    <circle cx="69" cy="67" r="3" fill="#E11D48"/>
    <text x="70" y="150" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Low Bias, Low Var</text>
    <text x="70" y="166" fill="#475569" font-family="-apple-system, sans-serif" font-size="9.5" text-anchor="middle">(Ideal Generalization)</text>
  </g>

  <!-- Dartboard 2: High Bias, Low Variance -->
  <g transform="translate(230, 30)">
    <circle cx="70" cy="70" r="60" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="42" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="24" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
    <!-- Tightly clustered far away from center -->
    <circle cx="105" cy="35" r="3" fill="#E11D48"/>
    <circle cx="108" cy="38" r="3" fill="#E11D48"/>
    <circle cx="102" cy="39" r="3" fill="#E11D48"/>
    <circle cx="106" cy="33" r="3" fill="#E11D48"/>
    <text x="70" y="150" fill="#92400E" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">High Bias, Low Var</text>
    <text x="70" y="166" fill="#475569" font-family="-apple-system, sans-serif" font-size="9.5" text-anchor="middle">(Underfitting / Rigid)</text>
  </g>

  <!-- Dartboard 3: Low Bias, High Variance -->
  <g transform="translate(420, 30)">
    <circle cx="70" cy="70" r="60" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="42" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="24" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
    <!-- Scattered around center -->
    <circle cx="65" cy="50" r="3" fill="#E11D48"/>
    <circle cx="85" cy="88" r="3" fill="#E11D48"/>
    <circle cx="45" cy="75" r="3" fill="#E11D48"/>
    <circle cx="95" cy="62" r="3" fill="#E11D48"/>
    <text x="70" y="150" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Low Bias, High Var</text>
    <text x="70" y="166" fill="#475569" font-family="-apple-system, sans-serif" font-size="9.5" text-anchor="middle">(Overfitting / Sensitive)</text>
  </g>

  <!-- Dartboard 4: High Bias, High Variance -->
  <g transform="translate(610, 30)">
    <circle cx="70" cy="70" r="60" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="42" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="24" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="70" cy="70" r="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
    <!-- Scattered far away in one quadrant -->
    <circle cx="105" cy="30" r="3" fill="#E11D48"/>
    <circle cx="120" cy="55" r="3" fill="#E11D48"/>
    <circle cx="90" cy="45" r="3" fill="#E11D48"/>
    <circle cx="115" cy="20" r="3" fill="#E11D48"/>
    <text x="70" y="150" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">High Bias, High Var</text>
    <text x="70" y="166" fill="#475569" font-family="-apple-system, sans-serif" font-size="9.5" text-anchor="middle">(Worst Case)</text>
  </g>
</svg>'''

# 8. Figure 8.1: The Bias-Variance Trade-Off: Error Decomposition Curve
svgs["__SVG_BIAS_VARIANCE_TRADEOFF__"] = '''<svg viewBox="0 0 800 260" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="24" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">The Bias–Variance Trade-Off: Expected Error Decomposition</text>

  <!-- Axes -->
  <line x1="90" y1="210" x2="720" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="90" y1="210" x2="90" y2="45" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="400" y="235" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Model Complexity →</text>
  <text x="80" y="40" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Error</text>

  <!-- Irreducible Noise (Flat dashed line) -->
  <line x1="90" y1="180" x2="710" y2="180" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="715" y="184" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10.5">Irreducible Noise (σ²)</text>

  <!-- Bias^2 Curve (Decreasing) -->
  <path d="M 100 70 C 180 85 280 140 400 170 C 520 185 640 190 710 192" fill="none" stroke="#D97706" stroke-width="2.5"/>
  <text x="200" y="95" fill="#D97706" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Bias²</text>

  <!-- Variance Curve (Increasing) -->
  <path d="M 100 195 C 220 195 350 185 450 160 C 560 130 650 70 710 55" fill="none" stroke="#7E22CE" stroke-width="2.5"/>
  <text x="650" y="70" fill="#7E22CE" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Variance</text>

  <!-- Total Expected Error (U-shape) -->
  <path d="M 100 60 C 200 80 320 125 405 110 C 500 110 610 80 710 48" fill="none" stroke="#E11D48" stroke-width="3.5"/>
  <text x="405" y="95" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">Total Expected Error</text>

  <!-- Optimal Sweet Spot Indicator -->
  <line x1="405" y1="110" x2="405" y2="210" stroke="#059669" stroke-width="2" stroke-dasharray="3 3"/>
  <circle cx="405" cy="110" r="4.5" fill="#059669"/>
  <text x="405" y="130" fill="#059669" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Min Total Error</text>
</svg>'''

# 9. Figure 9.1: Actual Executed Polynomial Regressions: Degree 1 vs Degree 3 vs Degree 10
svgs["__SVG_POLYNOMIAL_DEGREES__"] = '''<svg viewBox="0 0 800 270" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="24" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Actual Executed Polynomial Regressions (Synthetic Cosine Signal + Noise)</text>

  <!-- Plot Area -->
  <line x1="80" y1="210" x2="720" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="80" y1="210" x2="80" y2="45" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="725" y="214" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11">X</text>
  <text x="80" y="35" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">y</text>

  <!-- Ground Truth Signal (Dashed Gray) -->
  <path d="M 85 55 C 240 60 400 170 715 190" fill="none" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="4 4"/>

  <!-- Degree 1 Fit (Red straight line) -->
  <line x1="85" y1="70" x2="715" y2="185" stroke="#DC2626" stroke-width="2.5"/>

  <!-- Degree 3 Fit (Emerald smooth curve) -->
  <path d="M 85 58 Q 300 70 450 145 T 715 188" fill="none" stroke="#059669" stroke-width="3"/>

  <!-- Degree 10 Fit (Rose wild oscillations at boundaries) -->
  <path d="M 85 50 C 100 40 140 75 180 65 C 220 50 260 85 300 80 C 350 70 420 160 460 140 C 510 120 560 170 610 185 C 640 195 670 140 715 208" fill="none" stroke="#E11D48" stroke-width="2.5"/>

  <!-- Training Points -->
  <circle cx="110" cy="55" r="4" fill="#0284C7"/>
  <circle cx="160" cy="62" r="4" fill="#0284C7"/>
  <circle cx="210" cy="70" r="4" fill="#0284C7"/>
  <circle cx="270" cy="78" r="4" fill="#0284C7"/>
  <circle cx="340" cy="95" r="4" fill="#0284C7"/>
  <circle cx="410" cy="130" r="4.5" fill="#0284C7"/>
  <circle cx="480" cy="155" r="4" fill="#0284C7"/>
  <circle cx="550" cy="172" r="4" fill="#0284C7"/>
  <circle cx="620" cy="184" r="4" fill="#0284C7"/>
  <circle cx="690" cy="190" r="4" fill="#0284C7"/>

  <!-- Legend Box -->
  <rect x="105" y="145" width="230" height="58" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <line x1="115" y1="158" x2="135" y2="158" stroke="#DC2626" stroke-width="2.5"/>
  <text x="142" y="162" fill="#334155" font-family="-apple-system, sans-serif" font-size="10.5">Deg 1 (MSE: Train 0.187, Test 0.288)</text>
  <line x1="115" y1="174" x2="135" y2="174" stroke="#059669" stroke-width="3"/>
  <text x="142" y="178" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">Deg 3 (MSE: Train 0.018, Test 0.018)</text>
  <line x1="115" y1="190" x2="135" y2="190" stroke="#E11D48" stroke-width="2.5"/>
  <text x="142" y="194" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10.5">Deg 10 (MSE: Train 0.010, Test 0.024)</text>
</svg>'''

# 10. Figure 10.1: Regularization Objective Function: Loss vs Penalty Balance
svgs["__SVG_REGULARIZATION_OBJECTIVE__"] = '''<svg viewBox="0 0 800 220" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Component 1: Data Fitting Loss -->
  <g>
    <rect x="40" y="45" width="220" height="135" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <rect x="55" y="58" width="190" height="24" rx="4" fill="#0284C7"/>
    <text x="150" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Data-Fitting Loss</text>
    <text x="150" y="105" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" text-anchor="middle">∑ (y_i − ŷ_i)²</text>
    <text x="50" y="130" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="11">• Rewards fitting training points</text>
    <text x="50" y="150" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="11">• Encourages model flexibility</text>
  </g>

  <!-- Plus Operator -->
  <text x="285" y="125" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="28" font-weight="800" text-anchor="middle">+</text>

  <!-- Component 2: Multiplier (Lambda / Alpha) -->
  <g>
    <rect x="315" y="60" width="80" height="105" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="2"/>
    <text x="355" y="95" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="24" font-weight="800" text-anchor="middle">λ</text>
    <text x="355" y="120" fill="#9F1239" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">(or α)</text>
    <text x="355" y="145" fill="#881337" font-family="-apple-system, sans-serif" font-size="9.5" text-anchor="middle">Tuning Dial</text>
  </g>

  <!-- Multiply Operator -->
  <text x="415" y="125" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="24" font-weight="800" text-anchor="middle">×</text>

  <!-- Component 3: Regularization Penalty -->
  <g>
    <rect x="435" y="45" width="220" height="135" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
    <rect x="450" y="58" width="190" height="24" rx="4" fill="#7E22CE"/>
    <text x="545" y="74" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Model Complexity Penalty</text>
    <text x="545" y="105" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Penalty(w)</text>
    <text x="445" y="130" fill="#581C87" font-family="-apple-system, sans-serif" font-size="11">• L1 (Lasso): ∑ |w_j|</text>
    <text x="445" y="150" fill="#581C87" font-family="-apple-system, sans-serif" font-size="11">• L2 (Ridge): ∑ w_j²</text>
  </g>

  <!-- Equals Total Objective -->
  <path d="M 670 115 L 700 115" stroke="#E11D48" stroke-width="2.5"/>
  <rect x="705" y="65" width="80" height="95" rx="6" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
  <text x="745" y="98" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">TOTAL</text>
  <text x="745" y="118" fill="#047857" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">OBJECTIVE</text>
  <text x="745" y="138" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">To Minimize</text>
</svg>'''

# 11. Figure 11.1: Geometric Intuition: L1 Diamond Contour vs L2 Circular Contour
svgs["__SVG_L1_VS_L2_CONTOURS__"] = '''<svg viewBox="0 0 800 260" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Left: L1 (Lasso) Diamond -->
  <g transform="translate(60, 20)">
    <text x="140" y="18" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" text-anchor="middle">L1 Regularization (Lasso): Sparsity</text>
    <!-- Axes -->
    <line x1="20" y1="130" x2="260" y2="130" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="140" y1="20" x2="140" y2="240" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="265" y="134" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10">w_1</text>
    <text x="140" y="15" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">w_2</text>

    <!-- Diamond Constraint |w1| + |w2| <= C -->
    <polygon points="140,60 210,130 140,200 70,130" fill="#FFF1F2" stroke="#E11D48" stroke-width="2.5"/>

    <!-- Loss Ellipses -->
    <ellipse cx="210" cy="70" rx="45" ry="30" fill="none" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="3 3"/>
    <ellipse cx="210" cy="70" rx="65" ry="42" fill="none" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="3 3"/>
    <ellipse cx="210" cy="70" rx="82" ry="54" fill="none" stroke="#0284C7" stroke-width="2"/>

    <!-- Corner Contact Point (Sparse!) -->
    <circle cx="140" cy="60" r="5" fill="#E11D48"/>
    <text x="150" y="55" fill="#9F1239" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">Corner Hit: w_1 = 0!</text>
    <text x="140" y="235" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Sharp corners drive coefficients exactly to zero</text>
  </g>

  <!-- Right: L2 (Ridge) Circle -->
  <g transform="translate(460, 20)">
    <text x="140" y="18" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" text-anchor="middle">L2 Regularization (Ridge): Smooth Shrinkage</text>
    <!-- Axes -->
    <line x1="20" y1="130" x2="260" y2="130" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="140" y1="20" x2="140" y2="240" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="265" y="134" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10">w_1</text>
    <text x="140" y="15" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">w_2</text>

    <!-- Circular Constraint w1^2 + w2^2 <= C -->
    <circle cx="140" cy="130" r="60" fill="#FAF5FF" stroke="#7E22CE" stroke-width="2.5"/>

    <!-- Loss Ellipses -->
    <ellipse cx="210" cy="70" rx="40" ry="25" fill="none" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="3 3"/>
    <ellipse cx="210" cy="70" rx="55" ry="35" fill="none" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="3 3"/>
    <ellipse cx="210" cy="70" rx="70" ry="46" fill="none" stroke="#0284C7" stroke-width="2"/>

    <!-- Smooth Contact Point (Non-zero) -->
    <circle cx="178" cy="88" r="5" fill="#7E22CE"/>
    <text x="188" y="85" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">Smooth Edge (w_1 ≠ 0, w_2 ≠ 0)</text>
    <text x="140" y="235" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Smooth curve shrinks weights, rarely hits axes</text>
  </g>
</svg>'''

# 12. Figure 12.1: Actual Ridge vs Lasso vs Elastic Net Coefficient Comparison Bar Chart
svgs["__SVG_COEFFICIENT_PATHS__"] = '''<svg viewBox="0 0 800 270" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="24" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Actual Regularized Model Coefficients (Degree 10 Polynomial Features)</text>

  <!-- Baseline Y = 135 -->
  <line x1="80" y1="135" x2="720" y2="135" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="725" y="139" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10">0.0</text>

  <!-- Feature tick marks on X-axis -->
  <!-- Features 1 to 10 -->
  <!-- We show 3 grouped bars per feature: Ridge (Purple), Lasso (Rose), ElasticNet (Teal) -->
  <!-- Feature 1: Ridge -0.81, Lasso -1.06, ENet -1.07 -->
  <rect x="110" y="135" width="10" height="40" fill="#7E22CE"/>
  <rect x="122" y="135" width="10" height="53" fill="#E11D48"/>
  <rect x="134" y="135" width="10" height="53" fill="#059669"/>
  <text x="127" y="200" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">x¹</text>

  <!-- Feature 2: Ridge -0.65, Lasso 0.0, ENet 0.0 -->
  <rect x="170" y="135" width="10" height="32" fill="#7E22CE"/>
  <rect x="182" y="133" width="10" height="4" fill="#E11D48"/>
  <rect x="194" y="133" width="10" height="4" fill="#059669"/>
  <text x="187" y="155" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">x²</text>

  <!-- Feature 3: Ridge -0.05, Lasso 0.0, ENet 0.0 -->
  <rect x="230" y="135" width="10" height="8" fill="#7E22CE"/>
  <rect x="242" y="133" width="10" height="4" fill="#E11D48"/>
  <rect x="254" y="133" width="10" height="4" fill="#059669"/>
  <text x="247" y="155" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">x³</text>

  <!-- Feature 4: Ridge +0.35, Lasso 0.0, ENet +0.08 -->
  <rect x="290" y="117" width="10" height="18" fill="#7E22CE"/>
  <rect x="302" y="133" width="10" height="4" fill="#E11D48"/>
  <rect x="314" y="131" width="10" height="4" fill="#059669"/>
  <text x="307" y="155" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">x&#x2074;</text>

  <!-- Feature 5: Ridge +0.49, Lasso +0.52, ENet +0.32 -->
  <rect x="350" y="110" width="10" height="25" fill="#7E22CE"/>
  <rect x="362" y="108" width="10" height="27" fill="#E11D48"/>
  <rect x="374" y="119" width="10" height="16" fill="#059669"/>
  <text x="367" y="155" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">x&#x2075;</text>

  <!-- Feature 6: Ridge +0.45, Lasso +0.10, ENet +0.23 -->
  <rect x="410" y="112" width="10" height="23" fill="#7E22CE"/>
  <rect x="422" y="130" width="10" height="5" fill="#E11D48"/>
  <rect x="434" y="123" width="10" height="12" fill="#059669"/>
  <text x="427" y="155" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">x&#x2076;</text>

  <!-- Feature 7: Ridge +0.30, Lasso 0.0, ENet 0.0 -->
  <rect x="470" y="120" width="10" height="15" fill="#7E22CE"/>
  <rect x="482" y="133" width="10" height="4" fill="#E11D48"/>
  <rect x="494" y="133" width="10" height="4" fill="#059669"/>
  <text x="487" y="155" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">x&#x2077;</text>

  <!-- Feature 8: Ridge +0.08, Lasso 0.0, ENet 0.0 -->
  <rect x="530" y="131" width="10" height="4" fill="#7E22CE"/>
  <rect x="542" y="133" width="10" height="4" fill="#E11D48"/>
  <rect x="554" y="133" width="10" height="4" fill="#059669"/>
  <text x="547" y="155" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">x&#x2078;</text>

  <!-- Feature 9: Ridge -0.17, Lasso 0.0, ENet 0.0 -->
  <rect x="590" y="135" width="10" height="9" fill="#7E22CE"/>
  <rect x="602" y="133" width="10" height="4" fill="#E11D48"/>
  <rect x="614" y="133" width="10" height="4" fill="#059669"/>
  <text x="607" y="155" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">x&#x2079;</text>

  <!-- Feature 10: Ridge -0.43, Lasso 0.0, ENet 0.0 -->
  <rect x="650" y="135" width="10" height="22" fill="#7E22CE"/>
  <rect x="662" y="133" width="10" height="4" fill="#E11D48"/>
  <rect x="674" y="133" width="10" height="4" fill="#059669"/>
  <text x="667" y="170" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">x¹&#x2070;</text>

  <!-- Legend -->
  <g transform="translate(150, 230)">
    <rect x="0" y="0" width="14" height="14" fill="#7E22CE" rx="2"/>
    <text x="20" y="11" fill="#334155" font-family="-apple-system, sans-serif" font-size="11">Ridge (L2): All 10 non-zero (Smooth shrinkage)</text>

    <rect x="250" y="0" width="14" height="14" fill="#E11D48" rx="2"/>
    <text x="270" y="11" fill="#334155" font-family="-apple-system, sans-serif" font-size="11">Lasso (L1): 7 Zeroes (Sparse selection)</text>

    <rect x="500" y="0" width="14" height="14" fill="#059669" rx="2"/>
    <text x="520" y="11" fill="#334155" font-family="-apple-system, sans-serif" font-size="11">Elastic Net: 6 Zeroes (Hybrid)</text>
  </g>
</svg>'''

# 13. Figure 14.1: Regularization Strength (Alpha) Validation Curve
svgs["__SVG_ALPHA_SWEEP_CURVE__"] = '''<svg viewBox="0 0 800 260" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="24" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Actual Ridge Regularization Strength Sweep (α from 10−⁴ to 10³)</text>

  <!-- Axes -->
  <line x1="90" y1="210" x2="710" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="90" y1="210" x2="90" y2="45" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="400" y="240" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Regularization Strength α (Logarithmic Scale) →</text>
  <text x="80" y="38" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Mean Squared Error</text>

  <!-- Alpha ticks -->
  <text x="100" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">10−⁴</text>
  <text x="185" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">10−³</text>
  <text x="270" y="224" fill="#059669" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">10−² (✓)</text>
  <text x="355" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">10−¹</text>
  <text x="440" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">10°</text>
  <text x="525" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">10¹</text>
  <text x="610" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">10²</text>
  <text x="695" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">10³</text>

  <!-- Sweet spot vertical guide -->
  <line x1="270" y1="45" x2="270" y2="210" stroke="#059669" stroke-width="1.5" stroke-dasharray="3 3"/>
  <rect x="235" y="45" width="70" height="20" rx="3" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="270" y="59" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Optimal α = 0.01</text>

  <!-- Validation MSE Curve (Actual data: 0.0205, 0.0198, 0.0193, 0.0224, 0.0406, 0.1172, 0.3633, 0.4866) -->
  <path d="M 100 185 L 185 186 L 270 188 L 355 183 L 440 162 L 525 110 L 610 65 L 695 50" fill="none" stroke="#E11D48" stroke-width="3"/>
  <circle cx="270" cy="188" r="5" fill="#059669"/>
  <text x="355" y="165" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">5-Fold CV Validation Error</text>

  <!-- Training MSE Curve (Actual data: monotonically climbs with alpha) -->
  <path d="M 100 196 L 185 195 L 270 194 L 355 190 L 440 175 L 525 115 L 610 70 L 695 53" fill="none" stroke="#0284C7" stroke-width="2.5" stroke-dasharray="4 4"/>
  <text x="440" y="195" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="10.5">Training Error</text>

  <!-- Zone Annotation -->
  <text x="140" y="80" fill="#D97706" font-family="-apple-system, sans-serif" font-size="10.5">← Weak Penalty (Overfit risk)</text>
  <text x="580" y="140" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10.5">Excessive Penalty (Underfit) →</text>
</svg>'''

# 14. Figure 15.1: Feature Scaling Impact on Regularization
svgs["__SVG_FEATURE_SCALING_PENALTY__"] = '''<svg viewBox="0 0 800 230" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Left Box: Without Scaling (Unfair Penalization) -->
  <g>
    <rect x="30" y="25" width="350" height="185" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <rect x="45" y="38" width="180" height="22" rx="4" fill="#DC2626"/>
    <text x="135" y="53" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">&#10006; Unscaled Features (Fatal Flaw)</text>

    <text x="45" y="82" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">• Feature 1: Income ($30,000 to $150,000) → <tspan font-weight="700">w_1 = 0.0002</tspan></text>
    <text x="45" y="104" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">• Feature 2: Bedrooms (1 to 5) → <tspan font-weight="700">w_2 = 25.0</tspan></text>

    <rect x="45" y="120" width="320" height="42" rx="4" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="55" y="137" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">Penalty Impact: (w_2)² = 625.0 vs (w_1)² = 0.00000004!</text>
    <text x="55" y="153" fill="#7F1D1D" font-family="-apple-system, sans-serif" font-size="9.5">Ridge/Lasso crushes w_2 completely while ignoring w_1!</text>

    <text x="205" y="195" fill="#B91C1C" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Result: Arbitrary unit scale dictates feature importance</text>
  </g>

  <!-- Right Box: With StandardScaler (Fair Penalization) -->
  <g>
    <rect x="420" y="25" width="350" height="185" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
    <rect x="435" y="38" width="180" height="22" rx="4" fill="#059669"/>
    <text x="525" y="53" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">✓ StandardScaler Pipeline</text>

    <text x="435" y="82" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">• Income standardized (μ=0, σ=1) → <tspan font-weight="700">w_1 = 1.45</tspan></text>
    <text x="435" y="104" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">• Bedrooms standardized (μ=0, σ=1) → <tspan font-weight="700">w_2 = 0.88</tspan></text>

    <rect x="435" y="120" width="320" height="42" rx="4" fill="#FFFFFF" stroke="#A7F3D0"/>
    <text x="445" y="137" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700">Fair Penalty: Both coefficients on identical scale</text>
    <text x="445" y="153" fill="#047857" font-family="-apple-system, sans-serif" font-size="9.5">Penalty treats both features on their actual predictive merit</text>

    <text x="595" y="195" fill="#047857" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Result: True mathematical regularization achieved</text>
  </g>
</svg>'''

# 15. Figure 17.1: Early Stopping Architecture
svgs["__SVG_EARLY_STOPPING__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="24" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Early Stopping: Halting Iterative Training at the Validation Minimum</text>

  <!-- Axes -->
  <line x1="80" y1="190" x2="720" y2="190" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="80" y1="190" x2="80" y2="40" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="400" y="215" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Training Epochs / Iterations →</text>
  <text x="75" y="32" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Loss</text>

  <!-- Training Loss Curve (Steadily drops) -->
  <path d="M 90 60 C 180 80 300 130 420 160 C 540 175 640 180 710 182" fill="none" stroke="#0284C7" stroke-width="2.5"/>
  <text x="715" y="184" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Training Loss</text>

  <!-- Validation Loss Curve (Reaches valley then ascends) -->
  <path d="M 90 75 C 180 90 280 145 370 140 C 450 142 550 165 710 205" fill="none" stroke="#E11D48" stroke-width="3"/>
  <text x="715" y="208" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Validation Loss</text>

  <!-- Optimal Stop Point (Epoch ~370) -->
  <line x1="370" y1="40" x2="370" y2="190" stroke="#059669" stroke-width="2" stroke-dasharray="4 4"/>
  <circle cx="370" cy="140" r="5" fill="#059669"/>
  <rect x="300" y="45" width="140" height="26" rx="4" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="370" y="62" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">✓ Stop Here (Min Val Loss)</text>

  <!-- Patience Window Indicator -->
  <rect x="370" y="110" width="80" height="50" fill="#FEF3C7" fill-opacity="0.5" stroke="#FDE68A"/>
  <text x="410" y="130" fill="#92400E" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">Patience Buffer</text>
  <text x="410" y="145" fill="#92400E" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">(e.g. 10 epochs)</text>

  <!-- Right text callout -->
  <text x="600" y="120" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Overfitting Begins</text>
  <text x="600" y="138" fill="#475569" font-family="-apple-system, sans-serif" font-size="10">Model memorizes noise</text>
</svg>'''

# 16. Figure 18.1: Actual Executed Learning Curve (Sample Size vs MSE)
svgs["__SVG_LEARNING_CURVE__"] = '''<svg viewBox="0 0 800 260" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="24" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Actual Executed Learning Curve (Polynomial Degree 3, N_train = 30)</text>

  <!-- Axes -->
  <line x1="80" y1="200" x2="720" y2="200" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="80" y1="200" x2="80" y2="40" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="400" y="230" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Training Set Size (Samples) →</text>
  <text x="75" y="32" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">MSE</text>

  <!-- Ticks on X-axis: 4, 9, 14, 19, 24 -->
  <text x="140" y="216" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">4</text>
  <text x="270" y="216" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">9</text>
  <text x="400" y="216" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">14</text>
  <text x="530" y="216" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">19</text>
  <text x="660" y="216" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">24</text>

  <!-- Validation Curve (Actual data: 0.1274, 0.0495, 0.0563, 0.0315, 0.0251) -->
  <path d="M 140 70 L 270 148 L 400 141 L 530 166 L 660 173" fill="none" stroke="#E11D48" stroke-width="3"/>
  <circle cx="140" cy="70" r="4.5" fill="#E11D48"/>
  <circle cx="270" cy="148" r="4.5" fill="#E11D48"/>
  <circle cx="400" cy="141" r="4.5" fill="#E11D48"/>
  <circle cx="530" cy="166" r="4.5" fill="#E11D48"/>
  <circle cx="660" cy="173" r="4.5" fill="#E11D48"/>
  <text x="665" y="165" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Val MSE (0.025)</text>

  <!-- Training Curve (Actual data: 0.0000, 0.0083, 0.0149, 0.0167, 0.0168) -->
  <path d="M 140 200 L 270 191 L 400 184 L 530 182 L 660 182" fill="none" stroke="#0284C7" stroke-width="3"/>
  <circle cx="140" cy="200" r="4.5" fill="#0284C7"/>
  <circle cx="270" cy="191" r="4.5" fill="#0284C7"/>
  <circle cx="400" cy="184" r="4.5" fill="#0284C7"/>
  <circle cx="530" cy="182" r="4.5" fill="#0284C7"/>
  <circle cx="660" cy="182" r="4.5" fill="#0284C7"/>
  <text x="665" y="195" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Train MSE (0.017)</text>

  <!-- Gap narrows callout -->
  <line x1="660" y1="173" x2="660" y2="182" stroke="#059669" stroke-width="2"/>
  <text x="590" y="145" fill="#059669" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Gap Narrows to 0.008!</text>
</svg>'''

# 17. Figure 19.1: Actual Executed Validation Curve (Polynomial Degree 1 to 10)
svgs["__SVG_VALIDATION_CURVE__"] = '''<svg viewBox="0 0 800 260" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="24" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Actual Validation Curve: Polynomial Degree vs Train and Cross-Validation MSE</text>

  <!-- Axes -->
  <line x1="80" y1="210" x2="720" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="80" y1="210" x2="80" y2="45" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="400" y="235" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Polynomial Degree (Model Complexity) →</text>
  <text x="75" y="38" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">MSE</text>

  <!-- Ticks for Degrees 1, 2, 3, 5, 8, 10 -->
  <text x="120" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">1</text>
  <text x="180" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">2</text>
  <text x="240" y="224" fill="#059669" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">3 (✓)</text>
  <text x="360" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">5</text>
  <text x="520" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">8</text>
  <text x="680" y="224" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">10</text>

  <!-- Degree 3 Sweet Spot Vertical Line -->
  <line x1="240" y1="45" x2="240" y2="210" stroke="#059669" stroke-width="1.5" stroke-dasharray="3 3"/>
  <rect x="205" y="45" width="70" height="20" rx="3" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="240" y="59" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Min CV MSE</text>

  <!-- Validation MSE Curve (Actual data: Deg 1=0.225, Deg 2=0.032, Deg 3=0.026, Deg 5=0.028, Deg 8=0.035, Deg 10=0.023) -->
  <path d="M 120 70 L 180 180 L 240 186 L 360 184 L 520 178 L 680 189" fill="none" stroke="#E11D48" stroke-width="3"/>
  <circle cx="120" cy="70" r="4.5" fill="#E11D48"/>
  <circle cx="240" cy="186" r="5" fill="#059669"/>
  <circle cx="680" cy="189" r="4.5" fill="#E11D48"/>
  <text x="250" y="178" fill="#059669" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Optimal Degree 3 (CV MSE = 0.026)</text>

  <!-- Training MSE Curve (Continuously decreases: 0.187 -> 0.025 -> 0.018 -> 0.014 -> 0.011 -> 0.010) -->
  <path d="M 120 85 L 180 185 L 240 192 L 360 196 L 520 199 L 680 200" fill="none" stroke="#0284C7" stroke-width="2.5" stroke-dasharray="4 4"/>
  <text x="685" y="198" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="10.5">Train MSE (0.010)</text>
</svg>'''

# 18. Figure 20.1: Data Leakage Trap vs Leakage-Safe Pipeline in Regularized Workflows
svgs["__SVG_LEAKAGE_VS_SAFE_PIPELINE__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Flawed Leaky Path -->
  <g>
    <rect x="25" y="20" width="750" height="90" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <rect x="40" y="32" width="135" height="22" rx="4" fill="#DC2626"/>
    <text x="107" y="47" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">&#10006; LEAKY WORKFLOW</text>

    <!-- Pipeline steps -->
    <rect x="190" y="30" width="125" height="26" rx="4" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="252" y="47" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">All Data (Train + Test)</text>
    <text x="325" y="47" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="14" font-weight="700">→</text>

    <rect x="345" y="30" width="175" height="26" rx="4" fill="#FEE2E2" stroke="#FCA5A5"/>
    <text x="432" y="47" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">StandardScaler.fit(ALL)</text>
    <text x="530" y="47" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="14" font-weight="700">→</text>

    <rect x="550" y="30" width="180" height="26" rx="4" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="640" y="47" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Cross-Val / Ridge Tuning</text>

    <text x="400" y="85" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">CRITICAL BUG: Scaler calculated μ and σ using test data! Test distribution leaked into tuning.</text>
  </g>

  <!-- Leakage-Safe Pipeline Path -->
  <g>
    <rect x="25" y="125" width="750" height="95" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
    <rect x="40" y="137" width="135" height="22" rx="4" fill="#059669"/>
    <text x="107" y="152" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">✓ SAFE PIPELINE</text>

    <rect x="190" y="135" width="125" height="26" rx="4" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="252" y="152" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Split Folds FIRST</text>
    <text x="325" y="152" fill="#047857" font-family="-apple-system, sans-serif" font-size="14" font-weight="700">→</text>

    <rect x="345" y="135" width="175" height="26" rx="4" fill="#D1FAE5" stroke="#6EE7B7"/>
    <text x="432" y="152" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Fit Scaler on Train Fold</text>
    <text x="530" y="152" fill="#047857" font-family="-apple-system, sans-serif" font-size="14" font-weight="700">→</text>

    <rect x="550" y="135" width="180" height="26" rx="4" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="640" y="152" fill="#047857" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Transform Val Fold Safely</text>

    <text x="400" y="195" fill="#047857" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">PROPER PRACTICE: Scaler parameters fit strictly on training fold • Zero test contamination</text>
  </g>
</svg>'''

# 19. Figure 21.1: Complete Practical Project: Model Prediction Comparison on Test Set
svgs["__SVG_PRACTICAL_PROJECT_PREDICTIONS__"] = '''<svg viewBox="0 0 800 250" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Card 1: Unregularized Degree 10 OLS -->
  <g>
    <rect x="25" y="25" width="230" height="200" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <rect x="40" y="38" width="140" height="22" rx="4" fill="#DC2626"/>
    <text x="110" y="53" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Unregularized Deg 10</text>

    <text x="140" y="90" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="20" font-weight="800" text-anchor="middle">Test MSE: 0.024</text>
    <text x="140" y="112" fill="#7F1D1D" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Train MSE: 0.010 (Overfit!)</text>
    
    <rect x="40" y="130" width="200" height="42" rx="4" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="140" y="147" fill="#B91C1C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Coeffs Explode to ±966.7</text>
    <text x="140" y="162" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="9.5" text-anchor="middle">Zero coefficients: 0/10</text>

    <text x="140" y="198" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10.5" text-anchor="middle">High test variance</text>
  </g>

  <!-- Card 2: Ridge (L2, alpha=0.1) -->
  <g>
    <rect x="285" y="25" width="230" height="200" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
    <rect x="300" y="38" width="140" height="22" rx="4" fill="#7E22CE"/>
    <text x="370" y="53" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Ridge (L2, α=0.1)</text>

    <text x="400" y="90" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="20" font-weight="800" text-anchor="middle">Test MSE: 0.018</text>
    <text x="400" y="112" fill="#581C87" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Train MSE: 0.016</text>
    
    <rect x="300" y="130" width="200" height="42" rx="4" fill="#FFFFFF" stroke="#E9D5FF"/>
    <text x="400" y="147" fill="#6B21A8" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Smooth Shrinkage [-0.8, +0.5]</text>
    <text x="400" y="162" fill="#581C87" font-family="-apple-system, sans-serif" font-size="9.5" text-anchor="middle">Zero coefficients: 0/10</text>

    <text x="400" y="198" fill="#059669" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">✓ Balanced Generalization</text>
  </g>

  <!-- Card 3: Lasso (L1, alpha=0.01) -->
  <g>
    <rect x="545" y="25" width="230" height="200" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="2"/>
    <rect x="560" y="38" width="140" height="22" rx="4" fill="#E11D48"/>
    <text x="630" y="53" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Lasso (L1, α=0.01)</text>

    <text x="660" y="90" fill="#9F1239" font-family="-apple-system, sans-serif" font-size="20" font-weight="800" text-anchor="middle">Test MSE: 0.017</text>
    <text x="660" y="112" fill="#881337" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Train MSE: 0.025</text>
    
    <rect x="560" y="130" width="200" height="42" rx="4" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="660" y="147" fill="#9F1239" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Sparse! 7 Features Zeroed</text>
    <text x="660" y="162" fill="#881337" font-family="-apple-system, sans-serif" font-size="9.5" text-anchor="middle">Zero coefficients: 7/10</text>

    <text x="660" y="198" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">★ Lowest Test Error &amp; Sparse!</text>
  </g>
</svg>'''

# 20. Figure 21.2: End-to-End Model Diagnosis & Regularization Decision Tree Flowchart
svgs["__SVG_MODEL_DIAGNOSIS_FLOWCHART__"] = '''<svg viewBox="0 0 800 250" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Root Question -->
  <g>
    <rect x="290" y="18" width="220" height="42" rx="6" fill="#0F172A"/>
    <text x="400" y="44" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Evaluate Training vs Val Error</text>
  </g>

  <!-- Left Branch: Both High -->
  <path d="M 330 60 L 170 95" stroke="#D97706" stroke-width="2"/>
  <rect x="70" y="95" width="200" height="45" rx="6" fill="#FEF3C7" stroke="#FDE68A"/>
  <text x="170" y="115" fill="#92400E" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Train High + Val High</text>
  <text x="170" y="130" fill="#78350F" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Diagnosis: Underfitting (High Bias)</text>

  <!-- Left Solutions -->
  <path d="M 170 140 L 170 165" stroke="#D97706" stroke-width="1.5"/>
  <rect x="60" y="165" width="220" height="65" rx="6" fill="#FFFFFF" stroke="#FDE68A"/>
  <text x="70" y="182" fill="#92400E" font-family="-apple-system, sans-serif" font-size="10">• Increase polynomial degree / depth</text>
  <text x="70" y="198" fill="#92400E" font-family="-apple-system, sans-serif" font-size="10">• Engineer more informative features</text>
  <text x="70" y="214" fill="#92400E" font-family="-apple-system, sans-serif" font-size="10">• Decrease regularization α</text>

  <!-- Center Branch: Both Low -->
  <path d="M 400 60 L 400 95" stroke="#059669" stroke-width="2"/>
  <rect x="300" y="95" width="200" height="45" rx="6" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="400" y="115" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Train Low + Val Low</text>
  <text x="400" y="130" fill="#047857" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Diagnosis: Good Fit (Ideal)</text>

  <!-- Center Solutions -->
  <path d="M 400 140 L 400 165" stroke="#059669" stroke-width="1.5"/>
  <rect x="290" y="165" width="220" height="65" rx="6" fill="#FFFFFF" stroke="#A7F3D0"/>
  <text x="300" y="182" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10">• Validate on sealed holdout test set</text>
  <text x="300" y="198" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10">• Freeze hyperparameters</text>
  <text x="300" y="214" fill="#065F46" font-family="-apple-system, sans-serif" font-size="10">• Ready for production deployment</text>

  <!-- Right Branch: Low Train, High Val -->
  <path d="M 470 60 L 630 95" stroke="#E11D48" stroke-width="2"/>
  <rect x="530" y="95" width="200" height="45" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
  <text x="630" y="115" fill="#9F1239" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Train Low + Val High</text>
  <text x="630" y="130" fill="#881337" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Diagnosis: Overfitting (High Var)</text>

  <!-- Right Solutions -->
  <path d="M 630 140 L 630 165" stroke="#E11D48" stroke-width="1.5"/>
  <rect x="520" y="165" width="220" height="65" rx="6" fill="#FFFFFF" stroke="#FECDD3"/>
  <text x="530" y="182" fill="#9F1239" font-family="-apple-system, sans-serif" font-size="10">• Apply Ridge (L2) or Lasso (L1)</text>
  <text x="530" y="198" fill="#9F1239" font-family="-apple-system, sans-serif" font-size="10">• Tune α using cross-validation</text>
  <text x="530" y="214" fill="#9F1239" font-family="-apple-system, sans-serif" font-size="10">• Early stopping / gather more data</text>
</svg>'''
