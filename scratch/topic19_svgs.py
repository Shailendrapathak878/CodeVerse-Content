# Topic 19 SVG Generation Script - 17 Verified Vector SVGs

svgs = {}

# 1. Figure 1.1: Classification vs Regression Evaluation Overview
svgs["__SVG_CLS_VS_REG__"] = '''<svg viewBox="0 0 800 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Left Side: Classification Evaluation -->
  <g>
    <rect x="25" y="20" width="355" height="240" rx="10" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
    <rect x="40" y="35" width="180" height="28" rx="6" fill="#4F46E5"/>
    <text x="130" y="54" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Classification Evaluation</text>
    
    <text x="45" y="90" fill="#1E1B4B" font-family="-apple-system, sans-serif" font-size="13" font-weight="700">Target Type:</text>
    <text x="135" y="90" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="13" font-weight="600">Discrete Classes / Categories</text>
    
    <text x="45" y="115" fill="#475569" font-family="-apple-system, sans-serif" font-size="11">Example: Spam (1) vs Not Spam (0)</text>
    
    <!-- Visual Representation: 2 boxes with check / cross -->
    <rect x="45" y="130" width="150" height="45" rx="6" fill="#FFFFFF" stroke="#818CF8"/>
    <text x="120" y="148" fill="#1E1B4B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Prediction: Spam (1)</text>
    <text x="120" y="164" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">&check; Correct (Match!)</text>

    <rect x="210" y="130" width="150" height="45" rx="6" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="285" y="148" fill="#1E1B4B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Prediction: Not Spam</text>
    <text x="285" y="164" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">&#10006; Wrong (Mismatch!)</text>

    <!-- Core Metrics Pill -->
    <rect x="45" y="195" width="315" height="45" rx="6" fill="#FFFFFF" stroke="#C7D2FE"/>
    <text x="202" y="214" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Core Metrics: Accuracy, Precision, Recall, F1</text>
    <text x="202" y="230" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Measures match rate between discrete labels</text>
  </g>

  <!-- Right Side: Regression Evaluation -->
  <g>
    <rect x="420" y="20" width="355" height="240" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <rect x="435" y="35" width="170" height="28" rx="6" fill="#059669"/>
    <text x="520" y="54" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Regression Evaluation</text>

    <text x="440" y="90" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="13" font-weight="700">Target Type:</text>
    <text x="530" y="90" fill="#047857" font-family="-apple-system, sans-serif" font-size="13" font-weight="600">Continuous Numbers</text>

    <text x="440" y="115" fill="#475569" font-family="-apple-system, sans-serif" font-size="11">Example: House Price ($350,000)</text>

    <!-- Visual Representation: Error ruler -->
    <rect x="440" y="130" width="315" height="45" rx="6" fill="#FFFFFF" stroke="#6EE7B7"/>
    <text x="455" y="150" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">Actual: <tspan font-weight="700">$350,000</tspan></text>
    <text x="575" y="150" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11">Predicted: <tspan font-weight="700">$340,000</tspan></text>
    <text x="597" y="166" fill="#D97706" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Error = Actual &minus; Predicted = +$10,000</text>

    <!-- Core Metrics Pill -->
    <rect x="440" y="195" width="315" height="45" rx="6" fill="#FFFFFF" stroke="#BBF7D0"/>
    <text x="597" y="214" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Core Metrics: MAE, MSE, RMSE, R&sup2;</text>
    <text x="597" y="230" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Measures numerical distance and residual magnitude</text>
  </g>
</svg>'''

# 2. Figure 1.2: Probabilities vs Thresholds
svgs["__SVG_PROB_THRESHOLD__"] = '''<svg viewBox="0 0 800 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <text x="400" y="30" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Predicted Probability to Class Label via Decision Threshold</text>
  <text x="400" y="48" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Classifier predicts continuous probability P(y=1|x) &isin; [0, 1]. A threshold splits it into binary classes.</text>

  <!-- Number line 0.0 to 1.0 -->
  <line x1="80" y1="140" x2="720" y2="140" stroke="#94A3B8" stroke-width="3"/>
  
  <!-- Ticks -->
  <line x1="80" y1="130" x2="80" y2="150" stroke="#475569" stroke-width="2"/>
  <text x="80" y="170" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">0.0</text>

  <line x1="240" y1="135" x2="240" y2="145" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="240" y="165" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">0.25</text>

  <line x1="400" y1="130" x2="400" y2="150" stroke="#4F46E5" stroke-width="3"/>
  <text x="400" y="170" fill="#4F46E5" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">0.50 (Default)</text>

  <line x1="560" y1="135" x2="560" y2="145" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="560" y="165" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">0.75</text>

  <line x1="720" y1="130" x2="720" y2="150" stroke="#475569" stroke-width="2"/>
  <text x="720" y="170" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1.0</text>

  <!-- Threshold Dividing Line (Vertical dashed) -->
  <line x1="400" y1="70" x2="400" y2="210" stroke="#4F46E5" stroke-width="2.5" stroke-dasharray="4 4"/>
  <rect x="330" y="70" width="140" height="26" rx="4" fill="#EEF2FF" stroke="#818CF8"/>
  <text x="400" y="87" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Threshold = 0.50</text>

  <!-- Left Zone: Predict Class 0 -->
  <rect x="90" y="85" width="230" height="35" rx="6" fill="#F1F5F9"/>
  <text x="205" y="106" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">P &lt; 0.50 &rarr; Predict Class 0 (Not Spam)</text>

  <!-- Right Zone: Predict Class 1 -->
  <rect x="480" y="85" width="230" height="35" rx="6" fill="#EEF2FF"/>
  <text x="595" y="106" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">P &ge; 0.50 &rarr; Predict Class 1 (Spam)</text>

  <!-- Plotted points on number line -->
  <!-- Negatives -->
  <circle cx="140" cy="140" r="6" fill="#64748B"/><text x="140" y="125" fill="#64748B" font-size="9" text-anchor="middle">0.10</text>
  <circle cx="210" cy="140" r="6" fill="#64748B"/><text x="210" y="125" fill="#64748B" font-size="9" text-anchor="middle">0.20</text>
  <circle cx="270" cy="140" r="6" fill="#64748B"/><text x="270" y="125" fill="#64748B" font-size="9" text-anchor="middle">0.30</text>
  <circle cx="340" cy="140" r="6" fill="#64748B"/><text x="340" y="125" fill="#64748B" font-size="9" text-anchor="middle">0.40</text>
  
  <!-- Positives -->
  <circle cx="460" cy="140" r="6" fill="#4F46E5"/><text x="460" y="125" fill="#4F46E5" font-size="9" font-weight="700" text-anchor="middle">0.60</text>
  <circle cx="500" cy="140" r="6" fill="#4F46E5"/><text x="500" y="125" fill="#4F46E5" font-size="9" font-weight="700" text-anchor="middle">0.65</text>
  <circle cx="580" cy="140" r="6" fill="#4F46E5"/><text x="580" y="125" fill="#4F46E5" font-size="9" font-weight="700" text-anchor="middle">0.78</text>
  <circle cx="630" cy="140" r="6" fill="#4F46E5"/><text x="630" y="125" fill="#4F46E5" font-size="9" font-weight="700" text-anchor="middle">0.85</text>
  <circle cx="680" cy="140" r="6" fill="#4F46E5"/><text x="680" y="125" fill="#4F46E5" font-size="9" font-weight="700" text-anchor="middle">0.92</text>

  <!-- Bottom Explanatory Caption -->
  <text x="400" y="245" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Shifting threshold to the left (&lt; 0.5) catches more positive cases (higher recall) at the cost of more false alarms (lower precision).</text>
</svg>'''

# 3. Figure 1.3: Confusion Matrix Anatomy
svgs["__SVG_CONFUSION_MATRIX_ANATOMY__"] = '''<svg viewBox="0 0 800 340" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">The 2&times;2 Confusion Matrix Anatomy &bull; Four Foundational Outcomes</text>

  <!-- Column Headers (Predicted) -->
  <text x="310" y="65" fill="#047857" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Predicted Negative (Class 0)</text>
  <text x="570" y="65" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Predicted Positive (Class 1)</text>

  <!-- Row Headers (Actual) -->
  <text x="175" y="130" fill="#047857" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="end">Actual Negative (0)</text>
  <text x="175" y="235" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="end">Actual Positive (1)</text>

  <!-- Cell 1: True Negative (TN) - Top Left -->
  <rect x="190" y="80" width="240" height="100" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="2"/>
  <rect x="205" y="92" width="60" height="22" rx="4" fill="#DCFCE7"/>
  <text x="235" y="107" fill="#15803D" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">TN</text>
  <text x="275" y="108" fill="#15803D" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">True Negative</text>
  <text x="205" y="138" fill="#166534" font-family="-apple-system, sans-serif" font-size="11">Actual: Normal / Negative</text>
  <text x="205" y="156" fill="#166534" font-family="-apple-system, sans-serif" font-size="11">Predicted: Normal &rarr; <tspan font-weight="700">&check; Correct!</tspan></text>
  <text x="205" y="172" fill="#475569" font-family="-apple-system, sans-serif" font-size="10">Example: Clean email stays in inbox</text>

  <!-- Cell 2: False Positive (FP - Type I Error) - Top Right -->
  <rect x="450" y="80" width="240" height="100" rx="8" fill="#FEF3C7" stroke="#FDE68A" stroke-width="2"/>
  <rect x="465" y="92" width="60" height="22" rx="4" fill="#FEF3C7"/>
  <text x="495" y="107" fill="#D97706" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">FP</text>
  <text x="535" y="108" fill="#D97706" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">False Positive (Type I)</text>
  <text x="465" y="138" fill="#92400E" font-family="-apple-system, sans-serif" font-size="11">Actual: Normal / Negative</text>
  <text x="465" y="156" fill="#B45309" font-family="-apple-system, sans-serif" font-size="11">Predicted: Positive &rarr; <tspan font-weight="700">&#10006; False Alarm!</tspan></text>
  <text x="465" y="172" fill="#475569" font-family="-apple-system, sans-serif" font-size="10">Example: Important work email sent to Spam</text>

  <!-- Cell 3: False Negative (FN - Type II Error) - Bottom Left -->
  <rect x="190" y="195" width="240" height="100" rx="8" fill="#FEE2E2" stroke="#FCA5A5" stroke-width="2"/>
  <rect x="205" y="207" width="60" height="22" rx="4" fill="#FEE2E2"/>
  <text x="235" y="222" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">FN</text>
  <text x="275" y="223" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">False Negative (Type II)</text>
  <text x="205" y="253" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="11">Actual: Disease / Positive</text>
  <text x="205" y="271" fill="#B91C1C" font-family="-apple-system, sans-serif" font-size="11">Predicted: Normal &rarr; <tspan font-weight="700">&#10006; Missed!</tspan></text>
  <text x="205" y="287" fill="#475569" font-family="-apple-system, sans-serif" font-size="10">Example: Malicious virus bypasses antivirus</text>

  <!-- Cell 4: True Positive (TP) - Bottom Right -->
  <rect x="450" y="195" width="240" height="100" rx="8" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="2"/>
  <rect x="465" y="207" width="60" height="22" rx="4" fill="#E0E7FF"/>
  <text x="495" y="222" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">TP</text>
  <text x="535" y="223" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">True Positive</text>
  <text x="465" y="253" fill="#3730A3" font-family="-apple-system, sans-serif" font-size="11">Actual: Positive / Spam</text>
  <text x="465" y="271" fill="#3730A3" font-family="-apple-system, sans-serif" font-size="11">Predicted: Positive &rarr; <tspan font-weight="700">&check; Caught!</tspan></text>
  <text x="465" y="287" fill="#475569" font-family="-apple-system, sans-serif" font-size="10">Example: Phishing email blocked</text>

  <!-- Bottom Caption -->
  <text x="400" y="322" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Diagonal cells (Green TN &amp; Blue TP) are correct decisions; Off-diagonal cells (Yellow FP &amp; Red FN) are classification errors.</text>
</svg>'''

# 4. Figure 1.4: Accuracy Paradox (Balanced vs Imbalanced)
svgs["__SVG_ACCURACY_PARADOX__"] = '''<svg viewBox="0 0 800 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">The Accuracy Paradox: Balanced vs Heavily Imbalanced Datasets</text>

  <!-- Left: Balanced Dataset -->
  <g>
    <rect x="30" y="50" width="350" height="200" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="205" y="75" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Case A: Balanced Dataset (50% Class 0 / 50% Class 1)</text>

    <!-- Stacked bar 50/50 -->
    <rect x="60" y="95" width="145" height="35" fill="#0284C7"/>
    <text x="132" y="117" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Class 0: 50%</text>

    <rect x="205" y="95" width="145" height="35" fill="#4F46E5"/>
    <text x="277" y="117" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Class 1: 50%</text>

    <text x="205" y="155" fill="#334155" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">A dumb majority guesser gets <tspan font-weight="700">50% Accuracy</tspan>.</text>
    <rect x="60" y="175" width="290" height="50" rx="6" fill="#F0FDF4" stroke="#86EFAC"/>
    <text x="205" y="195" fill="#15803D" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">&check; Accuracy Works Great Here!</text>
    <text x="205" y="212" fill="#166534" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">An 85% accuracy model genuinely learned meaningful signal.</text>
  </g>

  <!-- Right: Imbalanced Dataset -->
  <g>
    <rect x="420" y="50" width="350" height="200" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
    <text x="595" y="75" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Case B: Imbalanced Dataset (99% Normal / 1% Fraud)</text>

    <!-- Stacked bar 99/1 -->
    <rect x="450" y="95" width="280" height="35" fill="#0284C7"/>
    <text x="580" y="117" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Class 0 (Normal): 99%</text>

    <rect x="730" y="95" width="10" height="35" fill="#E11D48"/>

    <text x="595" y="155" fill="#334155" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">A dumb model predicting "Normal" for everything:</text>
    <rect x="450" y="175" width="290" height="50" rx="6" fill="#FEF2F2" stroke="#FECACA"/>
    <text x="595" y="195" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">&#10006; 99.0% Accuracy &bull; 0% Fraud Recall!</text>
    <text x="595" y="212" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">High accuracy creates a dangerous, false illusion of success.</text>
  </g>
</svg>'''

# 5. Figure 1.5: Precision vs Recall Trade-Off
svgs["__SVG_PRECISION_VS_RECALL__"] = '''<svg viewBox="0 0 800 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Left: Precision Focused -->
  <g>
    <rect x="30" y="25" width="350" height="230" rx="10" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <rect x="45" y="40" width="170" height="28" rx="6" fill="#0284C7"/>
    <text x="130" y="59" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Precision Focused</text>
    
    <text x="45" y="95" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">"When you predict positive, be certain!"</text>
    <text x="45" y="118" fill="#475569" font-family="-apple-system, sans-serif" font-size="11">Formula: TP / (TP + FP)</text>
    
    <rect x="45" y="130" width="320" height="55" rx="6" fill="#FFFFFF" stroke="#BAE6FD"/>
    <text x="205" y="150" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">High Precision = Extremely Few False Alarms</text>
    <text x="205" y="170" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Every email marked Spam is truly spam. Inbox never drops real mail.</text>

    <text x="45" y="210" fill="#0C4A6E" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Best When: False Positives are disastrous</text>
    <text x="45" y="226" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10">E.g., Spam filter, job applicant shortlisting, criminal sentencing.</text>
  </g>

  <!-- Right: Recall Focused -->
  <g>
    <rect x="420" y="25" width="350" height="230" rx="10" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
    <rect x="435" y="40" width="160" height="28" rx="6" fill="#E11D48"/>
    <text x="515" y="59" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Recall Focused</text>

    <text x="435" y="95" fill="#881337" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">"Find every single positive case out there!"</text>
    <text x="435" y="118" fill="#475569" font-family="-apple-system, sans-serif" font-size="11">Formula: TP / (TP + FN)</text>

    <rect x="435" y="130" width="320" height="55" rx="6" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="595" y="150" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">High Recall = Extremely Few Missed Cases</text>
    <text x="595" y="170" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Every malignant tumor is flagged, even if some benign ones are retested.</text>

    <text x="435" y="210" fill="#881337" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Best When: False Negatives are fatal</text>
    <text x="435" y="226" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10">E.g., Cancer screening, airport weapon detection, fraud alerts.</text>
  </g>
</svg>'''

# 6. Figure 1.6: Specificity, FPR, FNR Relationships
svgs["__SVG_SPECIFICITY_FPR_FNR__"] = '''<svg viewBox="0 0 800 260" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Rates &amp; Complements: Specificity, FPR, Recall, and FNR</text>

  <!-- Left Side: Negative Class Ground Truth (Actual 0 = TN + FP) -->
  <g>
    <rect x="30" y="50" width="350" height="180" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="205" y="75" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Actual Negative Group (Ground Truth = 0)</text>
    
    <!-- Split Bar -->
    <rect x="60" y="95" width="232" height="36" fill="#10B981" rx="4"/>
    <text x="176" y="118" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Specificity = TN / (TN + FP) = 80%</text>

    <rect x="292" y="95" width="58" height="36" fill="#F59E0B" rx="4"/>
    <text x="321" y="118" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">FPR = 20%</text>

    <!-- Formula Connection -->
    <rect x="60" y="150" width="290" height="60" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="205" y="172" fill="#047857" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">FPR = 1 &minus; Specificity</text>
    <text x="205" y="194" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">The proportion of healthy people mistakenly marked sick.</text>
  </g>

  <!-- Right Side: Positive Class Ground Truth (Actual 1 = TP + FN) -->
  <g>
    <rect x="420" y="50" width="350" height="180" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="595" y="75" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Actual Positive Group (Ground Truth = 1)</text>

    <!-- Split Bar -->
    <rect x="450" y="95" width="232" height="36" fill="#4F46E5" rx="4"/>
    <text x="566" y="118" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Recall = TP / (TP + FN) = 80%</text>

    <rect x="682" y="95" width="58" height="36" fill="#EF4444" rx="4"/>
    <text x="711" y="118" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">FNR = 20%</text>

    <!-- Formula Connection -->
    <rect x="450" y="150" width="290" height="60" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="595" y="172" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">FNR = 1 &minus; Recall</text>
    <text x="595" y="194" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">The proportion of actual sick patients missed by the test.</text>
  </g>
</svg>'''

# 7. Figure 1.7: Threshold Selection Sweep
svgs["__SVG_THRESHOLD_SWEEP__"] = '''<svg viewBox="0 0 800 300" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Impact of Moving Decision Threshold &tau; &isin; [0.1, 0.9] on Errors</text>
  <text x="400" y="46" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Lowering threshold catches more positives (low FN) but triggers false alarms (high FP).</text>

  <!-- Axis -->
  <line x1="80" y1="240" x2="720" y2="240" stroke="#CBD5E1" stroke-width="2"/>
  <line x1="80" y1="240" x2="80" y2="70" stroke="#CBD5E1" stroke-width="2"/>
  <text x="400" y="275" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Classification Threshold &tau; (0.0 to 1.0)</text>
  <text x="65" y="65" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="start">Metric Value (0% to 100%)</text>

  <!-- Recall Curve (Decreasing from 100% to 0%) -->
  <path d="M 80 80 Q 300 90 400 130 Q 550 180 720 240" fill="none" stroke="#E11D48" stroke-width="3"/>
  <text x="180" y="85" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Recall (Sensitivity)</text>

  <!-- Precision Curve (Increasing from baseline prevalence to ~100%) -->
  <path d="M 80 200 Q 250 190 400 130 Q 550 100 720 85" fill="none" stroke="#0284C7" stroke-width="3"/>
  <text x="620" y="85" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Precision</text>

  <!-- Intersection (Optimal F1 point around 0.50) -->
  <circle cx="400" cy="130" r="6" fill="#4F46E5"/>
  <line x1="400" y1="130" x2="400" y2="240" stroke="#4F46E5" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="400" y="255" fill="#4F46E5" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">&tau; = 0.50</text>

  <!-- Legend Card -->
  <rect x="520" y="130" width="220" height="70" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="535" y="150" fill="#334155" font-family="-apple-system, sans-serif" font-size="10"><tspan font-weight="700">Low Threshold (&tau; = 0.2):</tspan></text>
  <text x="535" y="165" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10">High Recall (95%), Low Precision (60%)</text>
  <text x="535" y="180" fill="#334155" font-family="-apple-system, sans-serif" font-size="10"><tspan font-weight="700">High Threshold (&tau; = 0.8):</tspan></text>
  <text x="535" y="195" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="10">High Precision (98%), Low Recall (40%)</text>
</svg>'''

# 8. Figure 1.8: ROC Curve & AUC
svgs["__SVG_ROC_CURVE__"] = '''<svg viewBox="0 0 800 320" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Receiver Operating Characteristic (ROC) Curve &bull; Measured AUC = 0.9960</text>

  <!-- Axes -->
  <line x1="120" y1="260" x2="680" y2="260" stroke="#94A3B8" stroke-width="2"/>
  <line x1="120" y1="260" x2="120" y2="60" stroke="#94A3B8" stroke-width="2"/>
  <text x="400" y="295" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="middle">False Positive Rate (FPR = 1 &minus; Specificity)</text>
  <text x="50" y="160" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" transform="rotate(-90 50 160)" text-anchor="middle">True Positive Rate (TPR = Recall)</text>

  <!-- Grid lines -->
  <line x1="120" y1="60" x2="680" y2="60" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="680" y1="60" x2="680" y2="260" stroke="#F1F5F9" stroke-width="1"/>

  <!-- Shaded AUC Area -->
  <path d="M 120 260 L 125 70 Q 200 62 680 60 L 680 260 Z" fill="#EEF2FF" opacity="0.6"/>

  <!-- Random Diagonal Baseline (Coin flip AUC = 0.50) -->
  <line x1="120" y1="260" x2="680" y2="60" stroke="#94A3B8" stroke-width="2" stroke-dasharray="6 6"/>
  <text x="450" y="180" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" transform="rotate(-20 450 180)">Random Classifier (AUC = 0.50)</text>

  <!-- Empirical ROC Curve -->
  <path d="M 120 260 L 125 70 Q 200 62 680 60" fill="none" stroke="#4F46E5" stroke-width="3.5"/>

  <!-- Ticks -->
  <text x="120" y="278" fill="#475569" font-size="11" text-anchor="middle">0.0</text>
  <text x="400" y="278" fill="#475569" font-size="11" text-anchor="middle">0.5</text>
  <text x="680" y="278" fill="#475569" font-size="11" text-anchor="middle">1.0</text>

  <text x="105" y="265" fill="#475569" font-size="11" text-anchor="end">0.0</text>
  <text x="105" y="165" fill="#475569" font-size="11" text-anchor="end">0.5</text>
  <text x="105" y="65" fill="#475569" font-size="11" text-anchor="end">1.0</text>

  <!-- Legend & Badges -->
  <rect x="420" y="80" width="240" height="75" rx="8" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="1.5"/>
  <circle cx="435" cy="98" r="5" fill="#4F46E5"/>
  <text x="450" y="102" fill="#1E1B4B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Fitted Model (AUC = 0.9960)</text>
  <text x="435" y="124" fill="#475569" font-family="-apple-system, sans-serif" font-size="10">P(Score(Pos) &gt; Score(Neg)) = 99.6%</text>
  <text x="435" y="140" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">&check; Outstanding Ranking Separation</text>
</svg>'''

# 9. Figure 1.9: Precision-Recall Curve
svgs["__SVG_PR_CURVE__"] = '''<svg viewBox="0 0 800 320" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Precision&ndash;Recall Curve &bull; Measured Average Precision (AP) = 0.9960</text>

  <!-- Axes -->
  <line x1="120" y1="260" x2="680" y2="260" stroke="#94A3B8" stroke-width="2"/>
  <line x1="120" y1="260" x2="120" y2="60" stroke="#94A3B8" stroke-width="2"/>
  <text x="400" y="295" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Recall (Completeness &bull; TP / Positives)</text>
  <text x="50" y="160" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" transform="rotate(-90 50 160)" text-anchor="middle">Precision (Purity &bull; TP / (TP + FP))</text>

  <!-- Baseline Prevalence Line (e.g. 10% positive prevalence) -->
  <line x1="120" y1="230" x2="680" y2="230" stroke="#E11D48" stroke-width="1.5" stroke-dasharray="5 5"/>
  <text x="550" y="222" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="600">Baseline Prevalence (P = Pos/Total)</text>

  <!-- Empirical PR Curve -->
  <path d="M 120 70 L 580 75 Q 640 100 680 160" fill="none" stroke="#059669" stroke-width="3.5"/>

  <!-- Ticks -->
  <text x="120" y="278" fill="#475569" font-size="11" text-anchor="middle">0.0</text>
  <text x="400" y="278" fill="#475569" font-size="11" text-anchor="middle">0.5</text>
  <text x="680" y="278" fill="#475569" font-size="11" text-anchor="middle">1.0</text>

  <text x="105" y="265" fill="#475569" font-size="11" text-anchor="end">0.0</text>
  <text x="105" y="165" fill="#475569" font-size="11" text-anchor="end">0.5</text>
  <text x="105" y="65" fill="#475569" font-size="11" text-anchor="end">1.0</text>

  <!-- Legend Card -->
  <rect x="150" y="150" width="260" height="75" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
  <circle cx="165" cy="168" r="5" fill="#059669"/>
  <text x="180" y="172" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">PR Curve: Area = AP = 0.9960</text>
  <text x="165" y="195" fill="#475569" font-family="-apple-system, sans-serif" font-size="10">Maintains &gt; 95% precision up to 90% recall.</text>
  <text x="165" y="210" fill="#059669" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">&check; Far superior to baseline prevalence</text>
</svg>'''

# 10. Figure 1.10: Multiclass 3x3 Confusion Matrix
svgs["__SVG_MULTICLASS_CM__"] = '''<svg viewBox="0 0 800 320" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Multiclass 3&times;3 Confusion Matrix (Cat, Dog, Bird &bull; 15 Samples)</text>

  <!-- Column Headers (Predicted) -->
  <text x="280" y="65" fill="#4F46E5" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Pred: Cat</text>
  <text x="390" y="65" fill="#4F46E5" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Pred: Dog</text>
  <text x="500" y="65" fill="#4F46E5" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Pred: Bird</text>

  <!-- Row Headers (Actual) -->
  <text x="210" y="115" fill="#4F46E5" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="end">Actual: Cat</text>
  <text x="210" y="175" fill="#4F46E5" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="end">Actual: Dog</text>
  <text x="210" y="235" fill="#4F46E5" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="end">Actual: Bird</text>

  <!-- Row 1: Cat (4, 1, 0) -->
  <rect x="230" y="85" width="100" height="50" rx="4" fill="#DCFCE7" stroke="#86EFAC" stroke-width="2"/>
  <text x="280" y="116" fill="#15803D" font-size="18" font-weight="800" text-anchor="middle">4</text>
  
  <rect x="340" y="85" width="100" height="50" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="390" y="116" fill="#DC2626" font-size="16" font-weight="700" text-anchor="middle">1</text>

  <rect x="450" y="85" width="100" height="50" rx="4" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="500" y="116" fill="#64748B" font-size="16" font-weight="600" text-anchor="middle">0</text>

  <!-- Row 2: Dog (1, 3, 1) -->
  <rect x="230" y="145" width="100" height="50" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="280" y="176" fill="#DC2626" font-size="16" font-weight="700" text-anchor="middle">1</text>

  <rect x="340" y="145" width="100" height="50" rx="4" fill="#DCFCE7" stroke="#86EFAC" stroke-width="2"/>
  <text x="390" y="176" fill="#15803D" font-size="18" font-weight="800" text-anchor="middle">3</text>

  <rect x="450" y="145" width="100" height="50" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="500" y="176" fill="#DC2626" font-size="16" font-weight="700" text-anchor="middle">1</text>

  <!-- Row 3: Bird (0, 1, 4) -->
  <rect x="230" y="205" width="100" height="50" rx="4" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="280" y="236" fill="#64748B" font-size="16" font-weight="600" text-anchor="middle">0</text>

  <rect x="340" y="205" width="100" height="50" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="390" y="236" fill="#DC2626" font-size="16" font-weight="700" text-anchor="middle">1</text>

  <rect x="450" y="205" width="100" height="50" rx="4" fill="#DCFCE7" stroke="#86EFAC" stroke-width="2"/>
  <text x="500" y="236" fill="#15803D" font-size="18" font-weight="800" text-anchor="middle">4</text>

  <!-- Right Metrics Card -->
  <rect x="580" y="85" width="180" height="170" rx="8" fill="#F8FAFC" stroke="#C7D2FE" stroke-width="1.5"/>
  <text x="670" y="112" fill="#1E1B4B" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Overall Acc = 73.3%</text>
  <line x1="595" y1="125" x2="745" y2="125" stroke="#E2E8F0"/>
  <text x="600" y="145" fill="#475569" font-size="11">Cat: Prec 80%, Rec 80%</text>
  <text x="600" y="165" fill="#475569" font-size="11">Dog: Prec 60%, Rec 60%</text>
  <text x="600" y="185" fill="#475569" font-size="11">Bird: Prec 80%, Rec 80%</text>
  <line x1="595" y1="200" x2="745" y2="200" stroke="#E2E8F0"/>
  <text x="670" y="222" fill="#4338CA" font-size="11" font-weight="700" text-anchor="middle">Macro F1 = 73.33%</text>
  <text x="670" y="240" fill="#4338CA" font-size="11" font-weight="700" text-anchor="middle">Micro F1 = 73.33%</text>
</svg>'''

# 11. Figure 1.11: Macro vs Micro vs Weighted Averaging
svgs["__SVG_MACRO_MICRO_WEIGHTED__"] = '''<svg viewBox="0 0 800 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Card 1: Macro Average -->
  <g>
    <rect x="30" y="30" width="225" height="220" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
    <rect x="45" y="45" width="195" height="28" rx="6" fill="#4F46E5"/>
    <text x="142" y="64" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Macro Averaging</text>

    <text x="142" y="100" fill="#1E1B4B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Simple Unweighted Mean</text>
    <rect x="45" y="110" width="195" height="35" rx="4" fill="#FFFFFF" stroke="#C7D2FE"/>
    <text x="142" y="132" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" text-anchor="middle">(Metric_1 + Metric_2 + Metric_3) / 3</text>

    <text x="142" y="170" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Treats every class equally,</text>
    <text x="142" y="185" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">regardless of sample size.</text>
    
    <rect x="45" y="200" width="195" height="36" rx="4" fill="#F8FAFC"/>
    <text x="142" y="222" fill="#1E1B4B" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Best When: Minority classes matter equally!</text>
  </g>

  <!-- Card 2: Weighted Average -->
  <g>
    <rect x="285" y="30" width="225" height="220" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <rect x="300" y="45" width="195" height="28" rx="6" fill="#059669"/>
    <text x="397" y="64" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Weighted Averaging</text>

    <text x="397" y="100" fill="#064E3B" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Support-Weighted Mean</text>
    <rect x="300" y="110" width="195" height="35" rx="4" fill="#FFFFFF" stroke="#BBF7D0"/>
    <text x="397" y="132" fill="#047857" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" text-anchor="middle">&Sigma; (Metric_i &times; Support_i) / Total</text>

    <text x="397" y="170" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Weights performance by the</text>
    <text x="397" y="185" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">true prevalence of each class.</text>

    <rect x="300" y="200" width="195" height="36" rx="4" fill="#F8FAFC"/>
    <text x="397" y="222" fill="#065F46" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Best When: Real population reflects support</text>
  </g>

  <!-- Card 3: Micro Average -->
  <g>
    <rect x="540" y="30" width="230" height="220" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
    <rect x="555" y="45" width="200" height="28" rx="6" fill="#E11D48"/>
    <text x="655" y="64" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Micro Averaging</text>

    <text x="655" y="100" fill="#881337" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Global Pool of All TP, FP, FN</text>
    <rect x="555" y="110" width="200" height="35" rx="4" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="655" y="132" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" text-anchor="middle">&Sigma; TP / (&Sigma; TP + &Sigma; FP)</text>

    <text x="655" y="170" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Pools all predictions together;</text>
    <text x="655" y="185" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">mathematically equals Accuracy!</text>

    <rect x="555" y="200" width="200" height="36" rx="4" fill="#F8FAFC"/>
    <text x="655" y="222" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Fact: Micro Prec = Micro Rec = Overall Acc</text>
  </g>
</svg>'''

# 12. Figure 1.12: Regression Residuals Geometric Diagram
svgs["__SVG_REGRESSION_RESIDUALS__"] = '''<svg viewBox="0 0 800 300" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Anatomy of Regression Residuals: e_i = y_i &minus; &ycirc;_i</text>

  <!-- Axes -->
  <line x1="100" y1="250" x2="700" y2="250" stroke="#94A3B8" stroke-width="2"/>
  <line x1="100" y1="250" x2="100" y2="50" stroke="#94A3B8" stroke-width="2"/>
  <text x="700" y="275" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="end">House Size (sq ft)</text>
  <text x="90" y="45" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="start">Actual Price y ($)</text>

  <!-- Fitted Regression Line y_hat -->
  <line x1="130" y1="220" x2="670" y2="80" stroke="#4F46E5" stroke-width="3"/>
  <text x="675" y="75" fill="#4F46E5" font-family="-apple-system, sans-serif" font-size="12" font-weight="800">Fitted Line &ycirc;</text>

  <!-- Data Point 1: Underpredicted (Actual > Predicted, e > 0) -->
  <circle cx="260" cy="140" r="6" fill="#059669"/>
  <line x1="260" y1="140" x2="260" y2="186" stroke="#059669" stroke-width="2" stroke-dasharray="3 3"/>
  <circle cx="260" cy="186" r="4" fill="#4F46E5"/>
  <rect x="270" y="145" width="170" height="36" rx="4" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="355" y="160" fill="#047857" font-size="10" font-weight="700" text-anchor="middle">Actual y_1 = $250k &gt; &ycirc;_1</text>
  <text x="355" y="174" fill="#047857" font-size="10" text-anchor="middle">Residual e_1 &gt; 0 (Underprediction)</text>

  <!-- Data Point 2: Overpredicted (Actual < Predicted, e < 0) -->
  <circle cx="500" cy="160" r="6" fill="#DC2626"/>
  <line x1="500" y1="160" x2="500" y2="124" stroke="#DC2626" stroke-width="2" stroke-dasharray="3 3"/>
  <circle cx="500" cy="124" r="4" fill="#4F46E5"/>
  <rect x="510" y="125" width="170" height="36" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="595" y="140" fill="#B91C1C" font-size="10" font-weight="700" text-anchor="middle">Actual y_2 = $300k &lt; &ycirc;_2</text>
  <text x="595" y="154" fill="#B91C1C" font-size="10" text-anchor="middle">Residual e_2 &lt; 0 (Overprediction)</text>

  <!-- Bottom Explanatory Caption -->
  <text x="400" y="292" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">The residual e_i is the vertical signed distance from the actual observation dot to the model line.</text>
</svg>'''

# 13. Figure 1.13: MAE vs MSE Error Penalty Curve
svgs["__SVG_MAE_VS_MSE_CURVE__"] = '''<svg viewBox="0 0 800 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Error Magnitude vs Penalty: MAE (Linear) vs MSE (Quadratic)</text>

  <!-- Axes -->
  <line x1="120" y1="240" x2="680" y2="240" stroke="#94A3B8" stroke-width="2"/>
  <line x1="120" y1="240" x2="120" y2="50" stroke="#94A3B8" stroke-width="2"/>
  <text x="400" y="270" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Raw Error Magnitude |e| (e.g., 0 to 10 units)</text>
  <text x="65" y="60" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="start">Loss / Penalty</text>

  <!-- MAE Linear Line (y = x) -->
  <line x1="120" y1="240" x2="600" y2="120" stroke="#0284C7" stroke-width="3"/>
  <text x="610" y="125" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">MAE Penalty: |e|</text>

  <!-- MSE Quadratic Curve (y = x^2) -->
  <path d="M 120 240 Q 300 235 450 180 Q 550 120 620 50" fill="none" stroke="#E11D48" stroke-width="3.5"/>
  <text x="630" y="55" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="12" font-weight="800">MSE Penalty: e&sup2;</text>

  <!-- Example Comparison Callout -->
  <rect x="220" y="70" width="250" height="65" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
  <text x="345" y="90" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Small error (e = 2): MSE = 4, MAE = 2 (2&times;)</text>
  <text x="345" y="108" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Large error (e = 10): MSE = 100, MAE = 10 (10&times;!)</text>
  <text x="345" y="124" fill="#475569" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Squaring disproportionately punishes large outlier mistakes!</text>
</svg>'''

# 14. Figure 1.14: R^2 Baseline Comparison
svgs["__SVG_R2_BASELINE__"] = '''<svg viewBox="0 0 800 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Understanding R&sup2;: Total Sum of Squares (TSS) vs Residual Sum of Squares (RSS)</text>

  <!-- Left Side: TSS (Predicting Mean y_bar) -->
  <g>
    <rect x="40" y="50" width="340" height="200" rx="8" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
    <text x="210" y="75" fill="#B45309" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Baseline: Naive Mean &ybar; (TSS)</text>
    
    <!-- Horizontal Mean Line -->
    <line x1="70" y1="140" x2="350" y2="140" stroke="#D97706" stroke-width="2" stroke-dasharray="4 4"/>
    <text x="355" y="145" fill="#D97706" font-size="10" font-weight="700">Mean &ybar;</text>

    <!-- Points and vertical distances to Mean -->
    <circle cx="120" cy="90" r="5" fill="#D97706"/><line x1="120" y1="90" x2="120" y2="140" stroke="#D97706" stroke-width="1.5"/>
    <circle cx="210" cy="180" r="5" fill="#D97706"/><line x1="210" y1="180" x2="210" y2="140" stroke="#D97706" stroke-width="1.5"/>
    <circle cx="300" cy="80" r="5" fill="#D97706"/><line x1="300" y1="80" x2="300" y2="140" stroke="#D97706" stroke-width="1.5"/>

    <text x="210" y="215" fill="#78350F" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Total Variance in y: <tspan font-weight="700">TSS = &Sigma; (y_i &minus; &ybar;)&sup2;</tspan></text>
    <text x="210" y="235" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Our 5-House Example: TSS = 25,000</text>
  </g>

  <!-- Right Side: RSS (Model Fitted Line y_hat) -->
  <g>
    <rect x="420" y="50" width="340" height="200" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
    <text x="590" y="75" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Model: Fitted Line &ycirc; (RSS)</text>

    <!-- Sloped regression line -->
    <line x1="450" y1="190" x2="730" y2="90" stroke="#4F46E5" stroke-width="2.5"/>

    <!-- Points and vertical distances to Line -->
    <circle cx="500" cy="160" r="5" fill="#4F46E5"/><line x1="500" y1="160" x2="500" y2="172" stroke="#4F46E5" stroke-width="1.5"/>
    <circle cx="590" cy="130" r="5" fill="#4F46E5"/><line x1="590" y1="130" x2="590" y2="140" stroke="#4F46E5" stroke-width="1.5"/>
    <circle cx="680" cy="120" r="5" fill="#4F46E5"/><line x1="680" y1="120" x2="680" y2="108" stroke="#4F46E5" stroke-width="1.5"/>

    <text x="590" y="215" fill="#1E1B4B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Unexplained Error: <tspan font-weight="700">RSS = &Sigma; (y_i &minus; &ycirc;_i)&sup2;</tspan></text>
    <text x="590" y="235" fill="#4338CA" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">R&sup2; = 1 &minus; (1,100 / 25,000) = 0.9560 (95.6% Explained!)</text>
  </g>
</svg>'''

# 15. Figure 1.15: Residual Plots Diagnostic
svgs["__SVG_RESIDUAL_PLOTS__"] = '''<svg viewBox="0 0 800 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Left: Healthy Residual Plot (Random Homoscedastic Scatter) -->
  <g>
    <rect x="30" y="20" width="350" height="240" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <text x="205" y="45" fill="#15803D" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">&check; Healthy Residual Plot (Ideal)</text>

    <!-- Center Zero line -->
    <line x1="60" y1="140" x2="350" y2="140" stroke="#059669" stroke-width="1.5" stroke-dasharray="3 3"/>
    <text x="355" y="144" fill="#059669" font-size="10" font-weight="700">e=0</text>

    <!-- Random scatter points -->
    <g fill="#059669" opacity="0.7">
      <circle cx="90" cy="120" r="4"/><circle cx="120" cy="155" r="4"/><circle cx="150" cy="130" r="4"/>
      <circle cx="180" cy="160" r="4"/><circle cx="210" cy="125" r="4"/><circle cx="240" cy="145" r="4"/>
      <circle cx="270" cy="115" r="4"/><circle cx="300" cy="150" r="4"/><circle cx="330" cy="135" r="4"/>
    </g>

    <text x="205" y="215" fill="#166534" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Homoscedasticity Verified</text>
    <text x="205" y="232" fill="#475569" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Uniform spread around zero line; no missing non-linear terms.</text>
  </g>

  <!-- Right: Unhealthy Heteroscedastic / Curved Pattern -->
  <g>
    <rect x="420" y="20" width="350" height="240" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="595" y="45" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">&#10006; Problematic Residual Plot (Warning)</text>

    <!-- Center Zero line -->
    <line x1="450" y1="140" x2="740" y2="140" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="3 3"/>

    <!-- Funnel / Expanding variance shape -->
    <g fill="#DC2626" opacity="0.7">
      <circle cx="480" cy="138" r="4"/><circle cx="510" cy="142" r="4"/><circle cx="540" cy="135" r="4"/>
      <circle cx="580" cy="155" r="4"/><circle cx="610" cy="120" r="4"/><circle cx="650" cy="175" r="4"/>
      <circle cx="680" cy="100" r="4"/><circle cx="710" cy="190" r="4"/><circle cx="730" cy="85" r="4"/>
    </g>

    <text x="595" y="215" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Heteroscedasticity / Funnel Shape</text>
    <text x="595" y="232" fill="#475569" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Variance explodes for high predictions; log transform required.</text>
  </g>
</svg>'''

# 16. Figure 1.16: Train vs Validation vs Test Evaluation Pipeline
svgs["__SVG_EVAL_SPLITS_PIPELINE__"] = '''<svg viewBox="0 0 800 240" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Three-Way Evaluation Split &bull; Preventing Test-Set Leakage</text>

  <!-- Box 1: Training Set (60%) -->
  <rect x="40" y="55" width="220" height="130" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
  <rect x="55" y="70" width="120" height="24" rx="4" fill="#4F46E5"/>
  <text x="115" y="86" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">1. Training Set</text>
  <text x="55" y="115" fill="#1E1B4B" font-size="11" font-weight="700">Purpose: Model Fitting</text>
  <text x="55" y="132" fill="#475569" font-size="10">Learn weights &amp; tree splits</text>
  <text x="55" y="148" fill="#475569" font-size="10">Fit preprocessing scalers</text>
  <text x="55" y="168" fill="#4338CA" font-size="10" font-weight="600">Typically 60% &ndash; 70% of data</text>

  <!-- Arrow -->
  <path d="M 270 120 L 295 120" stroke="#94A3B8" stroke-width="2"/>

  <!-- Box 2: Validation Set (20%) -->
  <rect x="300" y="55" width="220" height="130" rx="8" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
  <rect x="315" y="70" width="130" height="24" rx="4" fill="#D97706"/>
  <text x="380" y="86" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">2. Validation Set</text>
  <text x="315" y="115" fill="#78350F" font-size="11" font-weight="700">Purpose: Hyperparameters</text>
  <text x="315" y="132" fill="#475569" font-size="10">Tune tree depth, regularization</text>
  <text x="315" y="148" fill="#475569" font-size="10">Tune decision threshold &tau;</text>
  <text x="315" y="168" fill="#B45309" font-size="10" font-weight="600">Typically 15% &ndash; 20% of data</text>

  <!-- Arrow -->
  <path d="M 530 120 L 555 120" stroke="#94A3B8" stroke-width="2"/>

  <!-- Box 3: Test Set (20% - Vault) -->
  <rect x="560" y="55" width="200" height="130" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="2"/>
  <rect x="575" y="70" width="120" height="24" rx="4" fill="#15803D"/>
  <text x="635" y="86" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">3. Final Test Vault</text>
  <text x="575" y="115" fill="#166534" font-size="11" font-weight="700">Purpose: Generalization</text>
  <text x="575" y="132" fill="#475569" font-size="10">Evaluated ONLY ONCE</text>
  <text x="575" y="148" fill="#DC2626" font-size="10" font-weight="700">Never tune thresholds here!</text>
  <text x="575" y="168" fill="#15803D" font-size="10" font-weight="600">Simulates real world</text>

  <text x="400" y="215" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Golden Rule: Fitting a scaler on the test set, or tuning &tau; on test labels, invalidates all reported metrics.</text>
</svg>'''

# 17. Figure 1.17: Master Metric Decision Guide Flowchart
svgs["__SVG_METRIC_DECISION_TREE__"] = '''<svg viewBox="0 0 800 340" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="26" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Master Evaluation Metric Decision Guide</text>

  <!-- Root Question -->
  <rect x="300" y="42" width="200" height="36" rx="6" fill="#0F172A"/>
  <text x="400" y="64" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">What is your task type?</text>

  <!-- Left Branch: Classification -->
  <line x1="330" y1="78" x2="180" y2="115" stroke="#94A3B8" stroke-width="2"/>
  <text x="210" y="98" fill="#4338CA" font-size="10" font-weight="700">Classification (Classes)</text>

  <rect x="80" y="115" width="200" height="35" rx="6" fill="#EEF2FF" stroke="#C7D2FE"/>
  <text x="180" y="136" fill="#1E1B4B" font-size="10" font-weight="600" text-anchor="middle">Is the target class balanced?</text>

  <!-- Sub-branch Cls: Yes -> Accuracy -->
  <line x1="130" y1="150" x2="80" y2="190" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="80" y="172" fill="#059669" font-size="9" font-weight="700">Yes (~50/50)</text>
  <rect x="20" y="190" width="120" height="45" rx="6" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="80" y="210" fill="#047857" font-size="11" font-weight="800" text-anchor="middle">Accuracy</text>
  <text x="80" y="225" fill="#475569" font-size="9" text-anchor="middle">Or ROC-AUC</text>

  <!-- Sub-branch Cls: No -> Precision / Recall / F1 / PR-AUC -->
  <line x1="230" y1="150" x2="260" y2="190" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="260" y="172" fill="#DC2626" font-size="9" font-weight="700">No (Imbalanced)</text>
  <rect x="180" y="190" width="160" height="55" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
  <text x="260" y="210" fill="#BE123C" font-size="11" font-weight="800" text-anchor="middle">Precision &amp; Recall / F1</text>
  <text x="260" y="225" fill="#475569" font-size="9" text-anchor="middle">Or Average Precision (AP)</text>
  <text x="260" y="238" fill="#475569" font-size="9" text-anchor="middle">Never use accuracy alone!</text>

  <!-- Right Branch: Regression -->
  <line x1="470" y1="78" x2="620" y2="115" stroke="#94A3B8" stroke-width="2"/>
  <text x="580" y="98" fill="#047857" font-size="10" font-weight="700">Regression (Numbers)</text>

  <rect x="520" y="115" width="200" height="35" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
  <text x="620" y="136" fill="#064E3B" font-size="10" font-weight="600" text-anchor="middle">How should errors be penalized?</text>

  <!-- Sub-branch Reg 1: Linear / Outlier Robust -> MAE -->
  <line x1="560" y1="150" x2="440" y2="190" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="470" y="172" fill="#0284C7" font-size="9" font-weight="700">Linear / Robust</text>
  <rect x="380" y="190" width="120" height="45" rx="6" fill="#F0F9FF" stroke="#BAE6FD"/>
  <text x="440" y="210" fill="#0284C7" font-size="11" font-weight="800" text-anchor="middle">MAE</text>
  <text x="440" y="225" fill="#475569" font-size="9" text-anchor="middle">Same units, intuitive</text>

  <!-- Sub-branch Reg 2: Heavy Outlier Penalty -> RMSE -->
  <line x1="620" y1="150" x2="600" y2="190" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="615" y="172" fill="#D97706" font-size="9" font-weight="700">Penalize Outliers</text>
  <rect x="540" y="190" width="120" height="45" rx="6" fill="#FEF3C7" stroke="#FDE68A"/>
  <text x="600" y="210" fill="#D97706" font-size="11" font-weight="800" text-anchor="middle">RMSE / MSE</text>
  <text x="600" y="225" fill="#475569" font-size="9" text-anchor="middle">Squares large errors</text>

  <!-- Sub-branch Reg 3: Variance Ratio -> R^2 -->
  <line x1="680" y1="150" x2="740" y2="190" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="730" y="172" fill="#7C3AED" font-size="9" font-weight="700">Baseline Ratio</text>
  <rect x="680" y="190" width="115" height="45" rx="6" fill="#FAF5FF" stroke="#E9D5FF"/>
  <text x="737" y="210" fill="#7C3AED" font-size="11" font-weight="800" text-anchor="middle">R&sup2; Score</text>
  <text x="737" y="225" fill="#475569" font-size="9" text-anchor="middle">% variance explained</text>

  <!-- Bottom Banner -->
  <rect x="40" y="275" width="720" height="35" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="400" y="297" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Best Practice: Report both an absolute error metric (MAE or RMSE) and a relative metric (R&sup2; or AP) together!</text>
</svg>'''

if __name__ == "__main__":
    print(f"Generated {len(svgs)} SVGs successfully.")
    for k, v in svgs.items():
        assert v.startswith("<svg") and v.endswith("</svg>")
        print(f"  {k}: {len(v)} chars")
