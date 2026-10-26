# Python script to generate all 16 verified vector SVGs for Topic 18: Anomaly Detection

svgs = {}

# 1. Figure 1.1: Anomaly Intro Scatter
svgs["__SVG_ANOMALY_INTRO__"] = '''<svg viewBox="0 0 800 380" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Grid background -->
  <defs>
    <pattern id="grid18_1" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#F1F5F9" stroke-width="1.5"/>
    </pattern>
  </defs>
  <rect width="800" height="380" fill="url(#grid18_1)" rx="12"/>
  
  <!-- Axes -->
  <line x1="80" y1="320" x2="740" y2="320" stroke="#94A3B8" stroke-width="2"/>
  <line x1="80" y1="320" x2="80" y2="40" stroke="#94A3B8" stroke-width="2"/>
  <text x="740" y="345" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="end">Transaction Amount (₹)</text>
  <text x="70" y="35" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" text-anchor="start">Frequency / Velocity</text>
  
  <!-- Normal Data Cluster (Dense teal/slate dots) -->
  <g fill="#0284C7" opacity="0.65">
    <!-- Centered around x=260, y=220 -->
    <circle cx="240" cy="230" r="5"/><circle cx="255" cy="210" r="5"/><circle cx="270" cy="240" r="5"/>
    <circle cx="250" cy="225" r="5"/><circle cx="230" cy="215" r="5"/><circle cx="280" cy="220" r="5"/>
    <circle cx="265" cy="205" r="5"/><circle cx="245" cy="245" r="5"/><circle cx="290" cy="235" r="5"/>
    <circle cx="235" cy="200" r="5"/><circle cx="275" cy="215" r="5"/><circle cx="260" cy="230" r="5"/>
    <circle cx="250" cy="195" r="5"/><circle cx="285" cy="250" r="5"/><circle cx="220" cy="225" r="5"/>
    <circle cx="300" cy="220" r="5"/><circle cx="270" cy="190" r="5"/><circle cx="240" cy="255" r="5"/>
    <circle cx="295" cy="210" r="5"/><circle cx="225" cy="240" r="5"/><circle cx="310" cy="230" r="5"/>
    <circle cx="260" cy="250" r="5"/><circle cx="280" cy="200" r="5"/><circle cx="250" cy="210" r="5"/>
  </g>
  <!-- Normal cluster envelope -->
  <ellipse cx="265" cy="225" rx="75" ry="50" fill="#E0F2FE" fill-opacity="0.35" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="265" y="295" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Normal Observations (95%+ of dataset)</text>
  
  <!-- Anomalies (Bright Crimson / Rose) -->
  <!-- Anomaly 1: Massive Amount -->
  <g>
    <circle cx="680" cy="240" r="14" fill="#FFE4E6" stroke="#E11D48" stroke-width="2"/>
    <circle cx="680" cy="240" r="7" fill="#E11D48"/>
    <line x1="680" y1="220" x2="680" y2="160" stroke="#E11D48" stroke-width="1.5" stroke-dasharray="3 3"/>
    <rect x="580" y="115" width="200" height="42" rx="6" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1"/>
    <text x="680" y="132" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Point Outlier: Amount ₹5,00,000</text>
    <text x="680" y="148" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Individual feature is extreme</text>
  </g>
  
  <!-- Anomaly 2: Extreme Velocity -->
  <g>
    <circle cx="250" cy="70" r="14" fill="#FFE4E6" stroke="#E11D48" stroke-width="2"/>
    <circle cx="250" cy="70" r="7" fill="#E11D48"/>
    <line x1="265" y1="70" x2="340" y2="70" stroke="#E11D48" stroke-width="1.5" stroke-dasharray="3 3"/>
    <rect x="345" y="50" width="210" height="42" rx="6" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1"/>
    <text x="450" y="67" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Velocity Anomaly: 45 tx/hour</text>
    <text x="450" y="83" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Normal amount, abnormal speed</text>
  </g>

  <!-- Anomaly 3: Contextual / Bivariate combination -->
  <g>
    <circle cx="530" cy="110" r="14" fill="#FFE4E6" stroke="#E11D48" stroke-width="2"/>
    <circle cx="530" cy="110" r="7" fill="#E11D48"/>
    <text x="530" y="90" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Joint Anomaly</text>
  </g>
</svg>'''

# 2. Figure 1.2: Anomaly vs Outlier vs Noise
svgs["__SVG_ANOMALY_VS_OUTLIER_VS_NOISE__"] = '''<svg viewBox="0 0 800 320" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <rect x="20" y="20" width="170" height="280" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="210" y="20" width="170" height="280" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="400" y="20" width="170" height="280" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
  <rect x="590" y="20" width="190" height="280" rx="10" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>

  <!-- Card 1: Normal Data -->
  <circle cx="105" cy="60" r="22" fill="#E0F2FE" stroke="#0284C7" stroke-width="2"/>
  <text x="105" y="66" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="16" font-weight="800" text-anchor="middle">1</text>
  <text x="105" y="110" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Normal Data</text>
  <text x="105" y="130" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Standard Behavior</text>
  <line x1="40" y1="145" x2="170" y2="145" stroke="#E2E8F0" stroke-width="1"/>
  <text x="105" y="170" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Points generated by</text>
  <text x="105" y="186" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">the core underlying</text>
  <text x="105" y="202" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">data generation process.</text>
  <rect x="35" y="225" width="140" height="55" rx="6" fill="#F1F5F9"/>
  <text x="105" y="245" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Example:</text>
  <text x="105" y="262" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">₹150 grocery purchase</text>

  <!-- Card 2: Noise -->
  <circle cx="295" cy="60" r="22" fill="#F3E8FF" stroke="#9333EA" stroke-width="2"/>
  <text x="295" y="66" fill="#9333EA" font-family="-apple-system, sans-serif" font-size="16" font-weight="800" text-anchor="middle">2</text>
  <text x="295" y="110" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Noise</text>
  <text x="295" y="130" fill="#9333EA" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Random Fluctuations</text>
  <line x1="230" y1="145" x2="360" y2="145" stroke="#E2E8F0" stroke-width="1"/>
  <text x="295" y="170" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Harmless measurement</text>
  <text x="295" y="186" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">error or sensor jitter;</text>
  <text x="295" y="202" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">does not carry interest.</text>
  <rect x="225" y="225" width="140" height="55" rx="6" fill="#F1F5F9"/>
  <text x="295" y="245" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Example:</text>
  <text x="295" y="262" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Temp reads 21.2° vs 21.0°</text>

  <!-- Card 3: Outlier -->
  <circle cx="485" cy="60" r="22" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>
  <text x="485" y="66" fill="#D97706" font-family="-apple-system, sans-serif" font-size="16" font-weight="800" text-anchor="middle">3</text>
  <text x="485" y="110" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Outlier</text>
  <text x="485" y="130" fill="#D97706" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Statistical Distance</text>
  <line x1="420" y1="145" x2="550" y2="145" stroke="#E2E8F0" stroke-width="1"/>
  <text x="485" y="170" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Mathematically far</text>
  <text x="485" y="186" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">from the center or mean;</text>
  <text x="485" y="202" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">purely geometric fact.</text>
  <rect x="415" y="225" width="140" height="55" rx="6" fill="#F1F5F9"/>
  <text x="485" y="245" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Example:</text>
  <text x="485" y="262" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Bill Gates visits a coffee shop</text>

  <!-- Card 4: Anomaly -->
  <circle cx="685" cy="60" r="22" fill="#FFE4E6" stroke="#E11D48" stroke-width="2"/>
  <text x="685" y="66" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="16" font-weight="800" text-anchor="middle">!</text>
  <text x="685" y="110" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Anomaly</text>
  <text x="685" y="130" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Actionable Deviation</text>
  <line x1="610" y1="145" x2="760" y2="145" stroke="#FECDD3" stroke-width="1"/>
  <text x="685" y="170" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Significantly unusual</text>
  <text x="685" y="186" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">behavior generated by an</text>
  <text x="685" y="202" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">abnormal mechanism.</text>
  <rect x="605" y="225" width="160" height="55" rx="6" fill="#FFFFFF" stroke="#FECDD3"/>
  <text x="685" y="245" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Actionable Alert:</text>
  <text x="685" y="262" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Credit card used in 2 nations</text>
</svg>'''

# 3. Figure 1.3: Supervised vs Semi-Supervised vs Unsupervised Workflow
svgs["__SVG_DETECTION_TYPES__"] = '''<svg viewBox="0 0 800 320" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Track 1: Supervised -->
  <g>
    <rect x="30" y="30" width="220" height="260" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <rect x="45" y="45" width="190" height="30" rx="6" fill="#0284C7"/>
    <text x="140" y="65" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. Supervised Learning</text>
    
    <text x="140" y="105" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Training Data Available:</text>
    <rect x="50" y="115" width="180" height="32" rx="4" fill="#FFFFFF" stroke="#BAE6FD"/>
    <text x="140" y="135" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Labeled Normal + Labeled Anomaly</text>
    
    <text x="140" y="170" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Model Strategy:</text>
    <text x="140" y="190" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Standard binary classification</text>
    <text x="140" y="206" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">(Random Forest, XGBoost)</text>
    
    <rect x="50" y="225" width="180" height="45" rx="4" fill="#E0F2FE"/>
    <text x="140" y="242" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Key Limitation:</text>
    <text x="140" y="258" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Cannot catch brand-new zero-day attack types</text>
  </g>

  <!-- Track 2: Semi-Supervised -->
  <g>
    <rect x="290" y="30" width="220" height="260" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <rect x="305" y="45" width="190" height="30" rx="6" fill="#16A34A"/>
    <text x="400" y="65" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. Semi-Supervised (Novelty)</text>
    
    <text x="400" y="105" fill="#15803D" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Training Data Available:</text>
    <rect x="310" y="115" width="180" height="32" rx="4" fill="#FFFFFF" stroke="#BBF7D0"/>
    <text x="400" y="135" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Clean Normal Samples ONLY</text>
    
    <text x="400" y="170" fill="#15803D" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Model Strategy:</text>
    <text x="400" y="190" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Learn boundary of normality;</text>
    <text x="400" y="206" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">flag anything outside (One-Class SVM)</text>
    
    <rect x="310" y="225" width="180" height="45" rx="4" fill="#DCFCE7"/>
    <text x="400" y="242" fill="#15803D" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Key Advantage:</text>
    <text x="400" y="258" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Catches completely unknown anomalies</text>
  </g>

  <!-- Track 3: Unsupervised -->
  <g>
    <rect x="550" y="30" width="220" height="260" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
    <rect x="565" y="45" width="190" height="30" rx="6" fill="#E11D48"/>
    <text x="660" y="65" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. Unsupervised Outliers</text>
    
    <text x="660" y="105" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Training Data Available:</text>
    <rect x="570" y="115" width="180" height="32" rx="4" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="660" y="135" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Unlabeled Raw Production Mix</text>
    
    <text x="660" y="170" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Model Strategy:</text>
    <text x="660" y="190" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Assumes anomalies are rare &amp; isolated</text>
    <text x="660" y="206" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">(Isolation Forest, LOF)</text>
    
    <rect x="570" y="225" width="180" height="45" rx="4" fill="#FFE4E6"/>
    <text x="660" y="242" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Key Assumption:</text>
    <text x="660" y="258" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Contamination is low (&lt; 5–10%)</text>
  </g>
</svg>'''

# 4. Figure 1.4: Classification vs Clustering vs Anomaly Detection
svgs["__SVG_ANOMALY_VS_CLASS_VS_CLUSTER__"] = '''<svg viewBox="0 0 800 260" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Section 1: Classification -->
  <g>
    <rect x="25" y="20" width="230" height="220" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="140" y="45" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Classification</text>
    <text x="140" y="65" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">"Which known class is it?"</text>
    <!-- 2 classes separated by line -->
    <circle cx="80" cy="110" r="5" fill="#3B82F6"/><circle cx="95" cy="130" r="5" fill="#3B82F6"/><circle cx="70" cy="140" r="5" fill="#3B82F6"/>
    <circle cx="180" cy="110" r="5" fill="#10B981"/><circle cx="195" cy="135" r="5" fill="#10B981"/><circle cx="170" cy="145" r="5" fill="#10B981"/>
    <line x1="135" y1="80" x2="135" y2="180" stroke="#EF4444" stroke-width="2" stroke-dasharray="4 4"/>
    <rect x="45" y="195" width="190" height="30" rx="4" fill="#F1F5F9"/>
    <text x="140" y="214" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Separates balanced labeled classes</text>
  </g>

  <!-- Section 2: Clustering -->
  <g>
    <rect x="285" y="20" width="230" height="220" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="400" y="45" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Clustering</text>
    <text x="400" y="65" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">"Which group does it resemble?"</text>
    <!-- 2 dense groups -->
    <ellipse cx="350" cy="130" rx="35" ry="25" fill="#E0E7FF" stroke="#6366F1" stroke-width="1"/>
    <ellipse cx="445" cy="130" rx="30" ry="22" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1"/>
    <circle cx="350" cy="130" r="4" fill="#4F46E5"/><circle cx="340" cy="125" r="4" fill="#4F46E5"/><circle cx="360" cy="135" r="4" fill="#4F46E5"/>
    <circle cx="445" cy="130" r="4" fill="#D97706"/><circle cx="435" cy="135" r="4" fill="#D97706"/><circle cx="455" cy="125" r="4" fill="#D97706"/>
    <rect x="305" y="195" width="190" height="30" rx="4" fill="#F1F5F9"/>
    <text x="400" y="214" fill="#334155" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Partitions all points into groups</text>
  </g>

  <!-- Section 3: Anomaly Detection -->
  <g>
    <rect x="545" y="20" width="230" height="220" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
    <text x="660" y="45" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Anomaly Detection</text>
    <text x="660" y="65" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">"Does it conform to normality?"</text>
    <!-- Normal envelope + external outlier -->
    <ellipse cx="640" cy="135" rx="55" ry="32" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5"/>
    <circle cx="625" cy="130" r="4" fill="#0284C7"/><circle cx="645" cy="140" r="4" fill="#0284C7"/><circle cx="655" cy="125" r="4" fill="#0284C7"/><circle cx="635" cy="145" r="4" fill="#0284C7"/>
    <!-- Anomaly outside -->
    <circle cx="735" cy="95" r="8" fill="#FFE4E6" stroke="#E11D48" stroke-width="2"/>
    <circle cx="735" cy="95" r="4" fill="#E11D48"/>
    <text x="735" y="80" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Anomaly</text>
    <rect x="565" y="195" width="190" height="30" rx="4" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="660" y="214" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" text-anchor="middle">Isolates rare non-conforming points</text>
  </g>
</svg>'''

# 5. Figure 1.5: Univariate vs Multivariate Anomalies
svgs["__SVG_UNIVARIATE_VS_MULTIVARIATE__"] = '''<svg viewBox="0 0 800 300" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Left: Univariate Anomaly (1D distribution) -->
  <g>
    <rect x="30" y="20" width="350" height="260" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="205" y="48" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Univariate Anomaly (Single Feature)</text>
    
    <!-- Bell Curve -->
    <path d="M 60 210 Q 140 210 170 170 Q 205 70 205 70 Q 205 70 240 170 Q 270 210 350 210" fill="none" stroke="#0284C7" stroke-width="2.5"/>
    <line x1="50" y1="210" x2="360" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
    
    <!-- Mean & Threshold -->
    <line x1="205" y1="70" x2="205" y2="210" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="3 3"/>
    <text x="205" y="225" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Mean (μ)</text>
    
    <!-- Extreme Outlier -->
    <circle cx="340" cy="208" r="7" fill="#E11D48"/>
    <line x1="340" y1="200" x2="340" y2="140" stroke="#E11D48" stroke-width="1.5"/>
    <text x="340" y="130" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Extreme Value</text>
    <text x="340" y="245" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Value > 3σ from mean</text>
  </g>

  <!-- Right: Multivariate Anomaly (2D correlation) -->
  <g>
    <rect x="420" y="20" width="350" height="260" rx="10" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
    <text x="595" y="48" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Multivariate Anomaly (Correlation Break)</text>
    
    <!-- Axes -->
    <line x1="460" y1="220" x2="730" y2="220" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="460" y1="220" x2="460" y2="80" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="730" y="240" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="end">Engine Temp (°C)</text>
    <text x="450" y="75" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="start">Oil Pressure (PSI)</text>
    
    <!-- Diagonal Correlated Cloud -->
    <ellipse cx="580" cy="150" rx="60" ry="22" transform="rotate(-35 580 150)" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="3 3"/>
    <circle cx="550" cy="175" r="4" fill="#0284C7"/><circle cx="580" cy="150" r="4" fill="#0284C7"/><circle cx="610" cy="125" r="4" fill="#0284C7"/>
    <circle cx="570" cy="160" r="4" fill="#0284C7"/><circle cx="595" cy="135" r="4" fill="#0284C7"/>

    <!-- Multivariate Anomaly: Normal temp, Normal pressure, but IMPOSSIBLE combination -->
    <circle cx="640" cy="205" r="8" fill="#FFE4E6" stroke="#E11D48" stroke-width="2"/>
    <circle cx="640" cy="205" r="4" fill="#E11D48"/>
    <line x1="640" y1="195" x2="640" y2="135" stroke="#E11D48" stroke-width="1.5"/>
    <rect x="560" y="105" width="160" height="30" rx="4" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="640" y="124" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Normal X, Normal Y alone!</text>
    <text x="595" y="260" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">High temp + Zero pressure = Blown engine!</text>
  </g>
</svg>'''

# 6. Figure 1.6: Z-Score Distribution
svgs["__SVG_ZSCORE_DISTRIBUTION__"] = '''<svg viewBox="0 0 800 320" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Baseline axis -->
  <line x1="80" y1="240" x2="720" y2="240" stroke="#CBD5E1" stroke-width="2"/>
  
  <!-- Shaded normal zone (-3 to +3) -->
  <path d="M 170 240 Q 285 240 330 150 Q 400 50 400 50 Q 400 50 470 150 Q 515 240 630 240 Z" fill="#F0FDF4" stroke="none"/>
  
  <!-- Shaded Rejection Tail Left -->
  <path d="M 80 240 L 170 240 Q 140 240 100 235 Z" fill="#FFE4E6"/>
  <!-- Shaded Rejection Tail Right -->
  <path d="M 630 240 L 720 240 Q 680 235 630 240 Z" fill="#FFE4E6"/>
  
  <!-- Bell Curve Stroke -->
  <path d="M 80 240 Q 285 240 330 150 Q 400 50 400 50 Q 400 50 470 150 Q 515 240 720 240" fill="none" stroke="#059669" stroke-width="3"/>
  
  <!-- Markers for standard deviations -->
  <!-- Mean 0 -->
  <line x1="400" y1="50" x2="400" y2="250" stroke="#0F172A" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="400" y="265" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">μ (z = 0)</text>
  <text x="400" y="280" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Center: 356.0</text>
  
  <!-- +1 sigma -->
  <line x1="480" y1="170" x2="480" y2="245" stroke="#94A3B8" stroke-width="1"/>
  <text x="480" y="265" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">+1σ</text>
  
  <!-- -1 sigma -->
  <line x1="320" y1="170" x2="320" y2="245" stroke="#94A3B8" stroke-width="1"/>
  <text x="320" y="265" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">-1σ</text>

  <!-- +2 sigma -->
  <line x1="555" y1="215" x2="555" y2="245" stroke="#94A3B8" stroke-width="1"/>
  <text x="555" y="265" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">+2σ</text>

  <!-- -2 sigma -->
  <line x1="245" y1="215" x2="245" y2="245" stroke="#94A3B8" stroke-width="1"/>
  <text x="245" y="265" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">-2σ</text>

  <!-- +3 sigma Threshold (Rejection boundary) -->
  <line x1="630" y1="130" x2="630" y2="250" stroke="#E11D48" stroke-width="2"/>
  <text x="630" y="265" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">+3σ Cutoff</text>
  <rect x="590" y="95" width="160" height="30" rx="4" fill="#FFF1F2" stroke="#FECDD3"/>
  <text x="670" y="114" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Anomaly: |z| &gt; 3.0</text>

  <!-- -3 sigma Threshold -->
  <line x1="170" y1="130" x2="170" y2="250" stroke="#E11D48" stroke-width="2"/>
  <text x="170" y="265" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">-3σ Cutoff</text>

  <!-- Highlight 99.7% Empirical Rule -->
  <rect x="300" y="15" width="200" height="26" rx="13" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="400" y="32" fill="#047857" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Normal Region: 99.73% of Data</text>
  
  <!-- Point 1500 plotted at z = 2.95 -->
  <circle cx="625" cy="238" r="6" fill="#E11D48"/>
  <text x="625" y="225" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">1500 (z=2.95)</text>
</svg>'''

# 7. Figure 1.7: IQR Boxplot Diagram
svgs["__SVG_IQR_BOXPLOT__"] = '''<svg viewBox="0 0 800 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Axis line -->
  <line x1="60" y1="210" x2="740" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="740" y="235" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="end">Value Scale</text>
  
  <!-- Left Whisker: from Lower Fence to Q1 -->
  <!-- Let Q1 = 300, Q3 = 500, IQR = 200. Lower Fence = 300 - 300 = 0 (say at x=140), Upper Fence = 500 + 300 = 800 (say at x=640) -->
  <!-- Box: x=280 to x=480 -->
  <rect x="280" y="90" width="200" height="70" rx="4" fill="#F0F9FF" stroke="#0284C7" stroke-width="2"/>
  
  <!-- Median Line (at x=370) -->
  <line x1="370" y1="90" x2="370" y2="160" stroke="#0369A1" stroke-width="3"/>
  <text x="370" y="80" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">Median (Q2: 67.5)</text>
  
  <!-- Q1 and Q3 Labels -->
  <text x="280" y="180" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Q1 (58.8)</text>
  <text x="480" y="180" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Q3 (76.2)</text>
  
  <!-- IQR Bracket above box -->
  <line x1="280" y1="65" x2="480" y2="65" stroke="#0284C7" stroke-width="1.5"/>
  <line x1="280" y1="60" x2="280" y2="70" stroke="#0284C7" stroke-width="1.5"/>
  <line x1="480" y1="60" x2="480" y2="70" stroke="#0284C7" stroke-width="1.5"/>
  <text x="380" y="55" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">IQR = Q3 - Q1 (17.5)</text>
  
  <!-- Left Whisker -->
  <line x1="160" y1="125" x2="280" y2="125" stroke="#0284C7" stroke-width="2"/>
  <line x1="160" y1="105" x2="160" y2="145" stroke="#0284C7" stroke-width="2"/>
  <text x="160" y="180" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Lower Whisker</text>
  
  <!-- Right Whisker -->
  <line x1="480" y1="125" x2="590" y2="125" stroke="#0284C7" stroke-width="2"/>
  <line x1="590" y1="105" x2="590" y2="145" stroke="#0284C7" stroke-width="2"/>
  <text x="590" y="180" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Upper Whisker</text>
  
  <!-- Upper Fence Marker -->
  <line x1="610" y1="85" x2="610" y2="165" stroke="#E11D48" stroke-width="2" stroke-dasharray="4 4"/>
  <text x="610" y="75" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Upper Fence (102.5)</text>
  <text x="610" y="195" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Q3 + 1.5×IQR</text>
  
  <!-- Outlier Points beyond Upper Fence -->
  <circle cx="700" cy="125" r="7" fill="#E11D48"/>
  <text x="700" y="110" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">140</text>
  <text x="700" y="150" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">IQR Outlier!</text>
</svg>'''

# 8. Figure 1.8: Anomaly Detection End-to-End Workflow
svgs["__SVG_ANOMALY_WORKFLOW__"] = '''<svg viewBox="0 0 800 220" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- 5 sequential workflow boxes connected by arrows -->
  <!-- Box 1 -->
  <rect x="20" y="40" width="130" height="130" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
  <circle cx="85" cy="70" r="16" fill="#E2E8F0"/>
  <text x="85" y="75" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">1</text>
  <text x="85" y="105" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Raw Stream</text>
  <text x="85" y="125" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Transactions /</text>
  <text x="85" y="140" fill="#64748B" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Sensor telemetry</text>
  
  <path d="M 155 105 L 175 105" stroke="#94A3B8" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Box 2 -->
  <rect x="180" y="40" width="130" height="130" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
  <circle cx="245" cy="70" r="16" fill="#BAE6FD"/>
  <text x="245" y="75" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">2</text>
  <text x="245" y="105" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Preprocessing</text>
  <text x="245" y="125" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Robust Scaling /</text>
  <text x="245" y="140" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Velocity features</text>

  <path d="M 315 105 L 335 105" stroke="#94A3B8" stroke-width="2"/>
  
  <!-- Box 3 -->
  <rect x="340" y="40" width="130" height="130" rx="8" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1.5"/>
  <circle cx="405" cy="70" r="16" fill="#DDD6FE"/>
  <text x="405" y="75" fill="#7C3AED" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">3</text>
  <text x="405" y="105" fill="#7C3AED" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Fit Detector</text>
  <text x="405" y="125" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Isolation Forest /</text>
  <text x="405" y="140" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">LOF / One-Class</text>

  <path d="M 475 105 L 495 105" stroke="#94A3B8" stroke-width="2"/>

  <!-- Box 4 -->
  <rect x="500" y="40" width="130" height="130" rx="8" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
  <circle cx="565" cy="70" r="16" fill="#FDE68A"/>
  <text x="565" y="75" fill="#D97706" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">4</text>
  <text x="565" y="105" fill="#D97706" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Score &amp; Threshold</text>
  <text x="565" y="125" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Evaluate cost:</text>
  <text x="565" y="140" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">FP vs FN trade-off</text>

  <path d="M 635 105 L 655 105" stroke="#94A3B8" stroke-width="2"/>

  <!-- Box 5 -->
  <rect x="660" y="40" width="120" height="130" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
  <circle cx="720" cy="70" r="16" fill="#FECDD3"/>
  <text x="720" y="75" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">5</text>
  <text x="720" y="105" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Human Review</text>
  <text x="720" y="125" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Triage alert,</text>
  <text x="720" y="140" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">verify root cause</text>
</svg>'''

# 9. Figure 1.9: Isolation Forest Tree Splits Concept
svgs["__SVG_ISOLATION_FOREST__"] = '''<svg viewBox="0 0 800 320" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Left Side: Isolation of Anomaly (Few splits) -->
  <g>
    <rect x="30" y="20" width="350" height="280" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
    <text x="205" y="48" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Anomaly: Few Splits to Isolate</text>
    
    <!-- 2D Box representation -->
    <rect x="60" y="70" width="140" height="140" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1.5"/>
    <!-- Normal points inside -->
    <circle cx="130" cy="140" r="4" fill="#0284C7"/><circle cx="140" cy="150" r="4" fill="#0284C7"/><circle cx="120" cy="160" r="4" fill="#0284C7"/>
    <circle cx="150" cy="145" r="4" fill="#0284C7"/><circle cx="135" cy="165" r="4" fill="#0284C7"/>
    <!-- Anomaly Point isolated at corner -->
    <circle cx="75" cy="85" r="6" fill="#E11D48"/>
    <!-- Single random cut line -->
    <line x1="60" y1="105" x2="200" y2="105" stroke="#E11D48" stroke-width="2" stroke-dasharray="4 2"/>
    <text x="130" y="100" fill="#E11D48" font-family="-apple-system, sans-serif" font-size="9" font-weight="700">Split 1 (Isolates x_anomaly!)</text>

    <!-- Tree diagram for Anomaly -->
    <circle cx="280" cy="90" r="14" fill="#E2E8F0"/>
    <text x="280" y="94" fill="#334155" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Root</text>
    <line x1="270" y1="102" x2="245" y2="135" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="290" y1="102" x2="315" y2="135" stroke="#94A3B8" stroke-width="1.5"/>
    
    <!-- Left Leaf = Anomaly! Depth = 1 -->
    <rect x="220" y="135" width="50" height="26" rx="4" fill="#FFE4E6" stroke="#E11D48"/>
    <text x="245" y="152" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">x_anom</text>
    
    <rect x="50" y="235" width="310" height="45" rx="6" fill="#FFFFFF" stroke="#FECDD3"/>
    <text x="205" y="252" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Short Path Length h(x) = 1</text>
    <text x="205" y="268" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Few random cuts easily separate anomalies!</text>
  </g>

  <!-- Right Side: Normal Point (Many splits) -->
  <g>
    <rect x="420" y="20" width="350" height="280" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <text x="595" y="48" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Normal Point: Many Splits to Isolate</text>

    <!-- 2D Box representation with multiple cuts -->
    <rect x="450" y="70" width="140" height="140" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="450" y1="110" x2="590" y2="110" stroke="#0284C7" stroke-width="1"/>
    <line x1="510" y1="70" x2="510" y2="210" stroke="#0284C7" stroke-width="1"/>
    <line x1="450" y1="160" x2="510" y2="160" stroke="#0284C7" stroke-width="1"/>
    <line x1="480" y1="110" x2="480" y2="160" stroke="#0284C7" stroke-width="1"/>
    <circle cx="495" cy="135" r="5" fill="#0284C7"/>
    <text x="520" y="140" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="9" font-weight="700">Deep Point</text>

    <!-- Deep Tree Diagram -->
    <circle cx="680" cy="80" r="10" fill="#E2E8F0"/>
    <line x1="680" y1="90" x2="660" y2="110" stroke="#94A3B8" stroke-width="1.5"/>
    <circle cx="660" cy="115" r="8" fill="#E2E8F0"/>
    <line x1="660" y1="123" x2="675" y2="140" stroke="#94A3B8" stroke-width="1.5"/>
    <circle cx="675" cy="145" r="8" fill="#E2E8F0"/>
    <line x1="675" y1="153" x2="665" y2="170" stroke="#94A3B8" stroke-width="1.5"/>
    <rect x="645" y="170" width="45" height="22" rx="4" fill="#E0F2FE" stroke="#0284C7"/>
    <text x="667" y="184" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" text-anchor="middle">x_norm</text>

    <rect x="440" y="235" width="310" height="45" rx="6" fill="#FFFFFF" stroke="#BAE6FD"/>
    <text x="595" y="252" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Long Path Length h(x) = 8+</text>
    <text x="595" y="268" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Dense cluster points require numerous partitions!</text>
  </g>
</svg>'''

# 10. Figure 1.10: Isolation Forest Scatter Results
svgs["__SVG_ISOLATION_FOREST_SCATTER__"] = '''<svg viewBox="0 0 800 360" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="400" y="30" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Isolation Forest Fitted Results (208 Total Points, Contamination = 0.05)</text>
  <text x="400" y="50" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Empirical scikit-learn run: Flagged 11 Anomalies (Rose) and 197 Inliers (Teal)</text>

  <!-- Axes -->
  <line x1="80" y1="300" x2="720" y2="300" stroke="#CBD5E1" stroke-width="1.5"/>
  <line x1="80" y1="300" x2="80" y2="70" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="720" y="325" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="end">Feature 1 (Centered at 5.0)</text>
  <text x="70" y="65" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="start">Feature 2 (Centered at 5.0)</text>

  <!-- Inlier points cloud around (400, 185) -->
  <g fill="#0284C7" opacity="0.6">
    <circle cx="380" cy="180" r="4.5"/><circle cx="410" cy="190" r="4.5"/><circle cx="395" cy="165" r="4.5"/>
    <circle cx="420" cy="175" r="4.5"/><circle cx="370" cy="195" r="4.5"/><circle cx="430" cy="185" r="4.5"/>
    <circle cx="385" cy="205" r="4.5"/><circle cx="400" cy="170" r="4.5"/><circle cx="415" cy="210" r="4.5"/>
    <circle cx="365" cy="175" r="4.5"/><circle cx="440" cy="195" r="4.5"/><circle cx="390" cy="190" r="4.5"/>
    <circle cx="405" cy="160" r="4.5"/><circle cx="425" cy="200" r="4.5"/><circle cx="375" cy="185" r="4.5"/>
    <circle cx="435" cy="170" r="4.5"/><circle cx="395" cy="215" r="4.5"/><circle cx="410" cy="175" r="4.5"/>
    <circle cx="360" cy="190" r="4.5"/><circle cx="445" cy="185" r="4.5"/><circle cx="385" cy="170" r="4.5"/>
    <circle cx="415" cy="195" r="4.5"/><circle cx="400" cy="220" r="4.5"/><circle cx="430" cy="205" r="4.5"/>
  </g>

  <!-- Decision Boundary contour (soft dashed envelope) -->
  <ellipse cx="400" cy="185" rx="90" ry="65" fill="#E0F2FE" fill-opacity="0.25" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="4 4"/>

  <!-- Flagged Anomalies (11 points scattered externally) -->
  <g>
    <!-- Anomaly points -->
    <circle cx="150" cy="110" r="7" fill="#E11D48"/><circle cx="150" cy="110" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="650" cy="130" r="7" fill="#E11D48"/><circle cx="650" cy="130" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="620" cy="260" r="7" fill="#E11D48"/><circle cx="620" cy="260" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="180" cy="250" r="7" fill="#E11D48"/><circle cx="180" cy="250" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="230" cy="90" r="7" fill="#E11D48"/><circle cx="230" cy="90" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="560" cy="95" r="7" fill="#E11D48"/><circle cx="560" cy="95" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="280" cy="270" r="7" fill="#E11D48"/><circle cx="280" cy="270" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="520" cy="275" r="7" fill="#E11D48"/><circle cx="520" cy="275" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="130" cy="180" r="7" fill="#E11D48"/><circle cx="130" cy="180" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="670" cy="210" r="7" fill="#E11D48"/><circle cx="670" cy="210" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="400" cy="90" r="7" fill="#E11D48"/><circle cx="400" cy="90" r="13" fill="none" stroke="#E11D48" stroke-width="1.5"/>
  </g>

  <!-- Legend -->
  <rect x="520" y="65" width="230" height="55" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
  <circle cx="535" cy="82" r="5" fill="#0284C7"/>
  <text x="550" y="86" fill="#334155" font-family="-apple-system, sans-serif" font-size="11">Normal Inliers (predict = 1): 197</text>
  <circle cx="535" cy="104" r="5" fill="#E11D48"/>
  <text x="550" y="108" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Flagged Anomalies (predict = -1): 11</text>
</svg>'''

# 11. Figure 1.11: Local Outlier Factor (LOF) Local Density Concept
svgs["__SVG_LOF_CONCEPT__"] = '''<svg viewBox="0 0 800 320" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="32" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Local Density &amp; Local Outlier Factor (LOF) Intuition</text>
  
  <!-- Cluster A: Dense Cluster (Left) -->
  <g>
    <circle cx="200" cy="160" r="70" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="200" y="75" fill="#15803D" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Dense Cluster C1 (High Density)</text>
    <!-- Tight points -->
    <circle cx="180" cy="150" r="4" fill="#15803D"/><circle cx="210" cy="155" r="4" fill="#15803D"/>
    <circle cx="195" cy="170" r="4" fill="#15803D"/><circle cx="205" cy="140" r="4" fill="#15803D"/>
    <circle cx="170" cy="165" r="4" fill="#15803D"/><circle cx="225" cy="160" r="4" fill="#15803D"/>
    
    <!-- Local Anomaly p1 near C1 -->
    <circle cx="295" cy="190" r="7" fill="#E11D48"/><circle cx="295" cy="190" r="14" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <text x="295" y="220" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Point p1 (Local Outlier!)</text>
    <text x="295" y="236" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">LOF Score &gt;&gt; 1.0</text>
    <text x="295" y="250" fill="#64748B" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Low density compared to C1 neighbors</text>
  </g>

  <!-- Cluster B: Sparse Cluster (Right) -->
  <g>
    <circle cx="580" cy="160" r="100" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
    <text x="580" y="45" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Sparse Cluster C2 (Low Density Naturally)</text>
    <!-- Widely spaced points -->
    <circle cx="530" cy="130" r="4" fill="#0284C7"/><circle cx="630" cy="130" r="4" fill="#0284C7"/>
    <circle cx="550" cy="200" r="4" fill="#0284C7"/><circle cx="620" cy="210" r="4" fill="#0284C7"/>
    <circle cx="580" cy="160" r="4" fill="#0284C7"/>
    
    <rect x="490" y="245" width="240" height="50" rx="6" fill="#FFFFFF" stroke="#BAE6FD"/>
    <text x="610" y="265" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Global methods fail here!</text>
    <text x="610" y="282" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">Distance to C2 is large, but LOF ≈ 1.0 (Normal)</text>
  </g>
</svg>'''

# 12. Figure 1.12: One-Class SVM Decision Region
svgs["__SVG_ONE_CLASS_SVM__"] = '''<svg viewBox="0 0 800 320" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="30" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">One-Class SVM: Non-Linear RBF Decision Boundary</text>
  
  <!-- Outer rejected area (Soft pink) -->
  <rect x="40" y="50" width="720" height="240" rx="10" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
  <text x="120" y="80" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="12" font-weight="700">Rejected Region (Score &lt; 0)</text>

  <!-- Inside Inlier Envelopes (Curved organic RBF kernel boundary) -->
  <path d="M 220 120 Q 350 90 480 120 Q 560 150 540 210 Q 480 250 330 240 Q 180 230 180 170 Z" fill="#F0FDF4" stroke="#16A34A" stroke-width="2.5"/>
  <text x="360" y="140" fill="#15803D" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" text-anchor="middle">Accepted Inlier Envelope (Score &#8805; 0)</text>
  
  <!-- Normal points inside envelope -->
  <g fill="#16A34A">
    <circle cx="280" cy="160" r="5"/><circle cx="320" cy="175" r="5"/><circle cx="350" cy="155" r="5"/>
    <circle cx="380" cy="180" r="5"/><circle cx="410" cy="165" r="5"/><circle cx="440" cy="185" r="5"/>
    <circle cx="300" cy="190" r="5"/><circle cx="370" cy="205" r="5"/><circle cx="460" cy="170" r="5"/>
    <circle cx="250" cy="170" r="5"/><circle cx="490" cy="190" r="5"/><circle cx="330" cy="215" r="5"/>
  </g>

  <!-- Support Vectors on the border (Highlighted with outer circles) -->
  <g>
    <circle cx="210" cy="140" r="5" fill="#D97706"/><circle cx="210" cy="140" r="9" fill="none" stroke="#D97706" stroke-width="1.5"/>
    <circle cx="485" cy="120" r="5" fill="#D97706"/><circle cx="485" cy="120" r="9" fill="none" stroke="#D97706" stroke-width="1.5"/>
    <circle cx="535" cy="205" r="5" fill="#D97706"/><circle cx="535" cy="205" r="9" fill="none" stroke="#D97706" stroke-width="1.5"/>
    <text x="210" y="125" fill="#B45309" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Support Vector</text>
  </g>

  <!-- Outside Anomalies -->
  <g>
    <circle cx="100" cy="180" r="6" fill="#E11D48"/><circle cx="100" cy="180" r="12" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <text x="100" y="205" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Anomaly</text>
    
    <circle cx="660" cy="140" r="6" fill="#E11D48"/><circle cx="660" cy="140" r="12" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <text x="660" y="165" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Anomaly</text>
  </g>

  <!-- Parameter notes card -->
  <rect x="520" y="235" width="220" height="45" rx="6" fill="#FFFFFF" stroke="#FECDD3"/>
  <text x="630" y="252" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Tuning Parameter: nu (ν = 0.05)</text>
  <text x="630" y="268" fill="#475569" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Controls upper bound on fraction of outliers</text>
</svg>'''

# 13. Figure 1.13: Confusion Matrix & Metric Tiles
svgs["__SVG_CONFUSION_MATRIX__"] = '''<svg viewBox="0 0 800 340" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="30" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Confusion Matrix: Transaction Detection Project (500 Total Samples)</text>

  <!-- Left: 2x2 Grid -->
  <!-- Headers -->
  <text x="210" y="70" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Predicted Normal (0)</text>
  <text x="360" y="70" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Predicted Anomaly (1)</text>
  <text x="120" y="130" fill="#475569" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="end">Actual Normal (0)</text>
  <text x="120" y="220" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="end">Actual Anomaly (1)</text>

  <!-- Top-Left: TN = 473 -->
  <rect x="140" y="85" width="140" height="80" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
  <text x="210" y="120" fill="#15803D" font-family="-apple-system, sans-serif" font-size="22" font-weight="800" text-anchor="middle">473</text>
  <text x="210" y="145" fill="#166534" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">True Negative (TN)</text>

  <!-- Top-Right: FP = 2 -->
  <rect x="290" y="85" width="140" height="80" rx="6" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
  <text x="360" y="120" fill="#D97706" font-family="-apple-system, sans-serif" font-size="22" font-weight="800" text-anchor="middle">2</text>
  <text x="360" y="145" fill="#92400E" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">False Positive (FP - False Alarm)</text>

  <!-- Bottom-Left: FN = 2 -->
  <rect x="140" y="175" width="140" height="80" rx="6" fill="#FEE2E2" stroke="#FCA5A5" stroke-width="1.5"/>
  <text x="210" y="210" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="22" font-weight="800" text-anchor="middle">2</text>
  <text x="210" y="235" fill="#991B1B" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">False Negative (FN - Missed!)</text>

  <!-- Bottom-Right: TP = 23 -->
  <rect x="290" y="175" width="140" height="80" rx="6" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="1.5"/>
  <text x="360" y="210" fill="#059669" font-family="-apple-system, sans-serif" font-size="22" font-weight="800" text-anchor="middle">23</text>
  <text x="360" y="235" fill="#065F46" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">True Positive (TP - Caught)</text>

  <!-- Right Side: Key Metrics Badges -->
  <g>
    <!-- Precision Card -->
    <rect x="470" y="85" width="280" height="50" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="490" y="115" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="13" font-weight="700">Precision:</text>
    <text x="560" y="115" fill="#059669" font-family="-apple-system, sans-serif" font-size="15" font-weight="800">92.00%</text>
    <text x="640" y="115" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11">TP / (TP + FP) = 23/25</text>

    <!-- Recall Card -->
    <rect x="470" y="145" width="280" height="50" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="490" y="175" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="13" font-weight="700">Recall:</text>
    <text x="545" y="175" fill="#059669" font-family="-apple-system, sans-serif" font-size="15" font-weight="800">92.00%</text>
    <text x="625" y="175" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11">TP / (TP + FN) = 23/25</text>

    <!-- F1-Score Card -->
    <rect x="470" y="205" width="280" height="50" rx="8" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1.5"/>
    <text x="490" y="235" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="13" font-weight="700">F1-Score:</text>
    <text x="565" y="235" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="16" font-weight="800">0.9200</text>
    <text x="645" y="235" fill="#475569" font-family="-apple-system, sans-serif" font-size="11">Harmonic Balance</text>
  </g>

  <!-- Footer explanation -->
  <text x="400" y="300" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">High accuracy (99.2%) is misleading on imbalanced data; Precision (92%) and Recall (92%) reveal the true detection trade-off.</text>
</svg>'''

# 14. Figure 1.14: Threshold vs Flagged Observations Curve
svgs["__SVG_THRESHOLD_SWEEP__"] = '''<svg viewBox="0 0 800 320" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="30" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Anomaly Threshold vs Number of Flagged Observations</text>
  <text x="400" y="48" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Measured sweep across Isolation Forest decision scores: moving threshold controls operational alert volume</text>

  <!-- Axes -->
  <line x1="80" y1="260" x2="720" y2="260" stroke="#CBD5E1" stroke-width="1.5"/>
  <line x1="80" y1="260" x2="80" y2="70" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="400" y="295" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Decision Function Threshold (Lower = More Conservative / Higher = More Alerts)</text>
  <text x="65" y="65" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="start">Total Flagged (Alerts)</text>

  <!-- Empirical Curve -->
  <!-- (-0.259: 0), (-0.209: 4), (-0.159: 11), (-0.109: 19), (-0.059: 23), (-0.009: 24), (+0.041: 37), (+0.090: 65), (+0.140: 172), (+0.190: 499) -->
  <path d="M 120 260 L 180 258 L 240 254 L 300 250 L 360 248 L 420 247 L 480 238 L 540 220 L 600 150 L 660 75" fill="none" stroke="#E11D48" stroke-width="3"/>

  <!-- Marked default threshold at ~ 0.0 (Flagged = 25) -->
  <circle cx="420" cy="247" r="6" fill="#E11D48"/>
  <line x1="420" y1="247" x2="420" y2="120" stroke="#E11D48" stroke-width="1.5" stroke-dasharray="3 3"/>
  <rect x="340" y="90" width="160" height="40" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
  <text x="420" y="107" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">Default Threshold (0.00)</text>
  <text x="420" y="122" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" text-anchor="middle">25 Alerts (5.0% volume)</text>

  <!-- Left: Too Strict (Missed anomalies) -->
  <rect x="100" y="170" width="140" height="45" rx="6" fill="#FEF3C7" stroke="#FDE68A"/>
  <text x="170" y="188" fill="#D97706" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Conservative (&lt; -0.15)</text>
  <text x="170" y="202" fill="#78350F" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">High False Negatives (Misses)</text>

  <!-- Right: Too Lenient (Alert Fatigue) -->
  <rect x="540" y="140" width="160" height="45" rx="6" fill="#FEE2E2" stroke="#FCA5A5"/>
  <text x="620" y="158" fill="#DC2626" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Permissive (&gt; +0.10)</text>
  <text x="620" y="172" fill="#7F1D1D" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Alert Fatigue (65+ Alerts)</text>
</svg>'''

# 15. Figure 1.15: Synthetic Transaction Project Scatter
svgs["__SVG_TRANSACTION_PROJECT__"] = '''<svg viewBox="0 0 800 380" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Project Visual: Transaction Amount vs Frequency (500 Transactions)</text>
  <text x="400" y="46" fill="#64748B" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Fitted Isolation Forest isolates Amount Spikes and Velocity Bursts</text>

  <!-- Axes -->
  <line x1="80" y1="320" x2="740" y2="320" stroke="#CBD5E1" stroke-width="1.5"/>
  <line x1="80" y1="320" x2="80" y2="70" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="740" y="345" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="end">Transaction Amount (₹100 to ₹15,000)</text>
  <text x="70" y="65" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="start">Frequency (tx/hour)</text>

  <!-- Normal Cluster (Teal points around Amount 1200, Freq 4) -->
  <g fill="#0284C7" opacity="0.65">
    <!-- Centered around x=180, y=280 -->
    <circle cx="160" cy="275" r="4"/><circle cx="190" cy="285" r="4"/><circle cx="175" cy="265" r="4"/>
    <circle cx="210" cy="270" r="4"/><circle cx="150" cy="290" r="4"/><circle cx="220" cy="280" r="4"/>
    <circle cx="180" cy="295" r="4"/><circle cx="165" cy="260" r="4"/><circle cx="230" cy="275" r="4"/>
    <circle cx="140" cy="285" r="4"/><circle cx="200" cy="260" r="4"/><circle cx="170" cy="305" r="4"/>
    <circle cx="195" cy="290" r="4"/><circle cx="155" cy="270" r="4"/><circle cx="215" cy="295" r="4"/>
  </g>
  <ellipse cx="185" cy="280" rx="70" ry="40" fill="#E0F2FE" fill-opacity="0.3" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="185" y="340" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">475 Normal Users (₹1200, 4 tx/hr)</text>

  <!-- Anomaly Type 1: High Amount (x=450 to 700, low freq y=280) -->
  <g>
    <circle cx="480" cy="280" r="6" fill="#E11D48"/><circle cx="480" cy="280" r="12" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="560" cy="290" r="6" fill="#E11D48"/><circle cx="560" cy="290" r="12" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="640" cy="275" r="6" fill="#E11D48"/><circle cx="640" cy="275" r="12" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="710" cy="285" r="6" fill="#E11D48"/><circle cx="710" cy="285" r="12" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <rect x="490" y="215" width="220" height="35" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
    <text x="600" y="232" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">15 High-Amount Anomalies</text>
    <text x="600" y="244" fill="#475569" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">₹5,500 – ₹15,000 spikes</text>
  </g>

  <!-- Anomaly Type 2: Velocity Spikes (x=160 to 240, high freq y=90 to 170) -->
  <g>
    <circle cx="180" cy="170" r="6" fill="#E11D48"/><circle cx="180" cy="170" r="12" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="210" cy="130" r="6" fill="#E11D48"/><circle cx="210" cy="130" r="12" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="190" cy="95" r="6" fill="#E11D48"/><circle cx="190" cy="95" r="12" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <circle cx="230" cy="80" r="6" fill="#E11D48"/><circle cx="230" cy="80" r="12" fill="none" stroke="#E11D48" stroke-width="1.5"/>
    <rect x="250" y="90" width="210" height="35" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
    <text x="355" y="107" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">10 Velocity Bursts (12–42 tx/hr)</text>
    <text x="355" y="119" fill="#475569" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Missed by single-variable rules!</text>
  </g>

  <!-- Legend -->
  <rect x="520" y="70" width="230" height="55" rx="6" fill="#FFFFFF" stroke="#E2E8F0"/>
  <circle cx="535" cy="87" r="5" fill="#0284C7"/>
  <text x="550" y="91" fill="#334155" font-family="-apple-system, sans-serif" font-size="11">Normal Transactions (TN=473)</text>
  <circle cx="535" cy="109" r="5" fill="#E11D48"/>
  <text x="550" y="113" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="700">Flagged Anomalies (TP=23)</text>
</svg>'''

# 16. Figure 1.16: Decision Flowchart
svgs["__SVG_DECISION_FLOWCHART__"] = '''<svg viewBox="0 0 800 360" width="100%" xmlns="http://www.w3.org/2000/svg" style="background:#FFFFFF; border-radius:12px;">
  <!-- Title -->
  <text x="400" y="28" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Anomaly Detection Method Selection Guide</text>
  
  <!-- Root question -->
  <rect x="300" y="45" width="200" height="40" rx="8" fill="#0F172A"/>
  <text x="400" y="69" fill="#FFFFFF" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" text-anchor="middle">How many features are you testing?</text>
  
  <!-- Branch 1: Single Feature (Univariate) -->
  <line x1="330" y1="85" x2="160" y2="130" stroke="#94A3B8" stroke-width="2"/>
  <text x="210" y="105" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Single Feature (1D)</text>
  
  <rect x="70" y="130" width="180" height="40" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="160" y="154" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Is the data Gaussian / Bell-curved?</text>
  
  <!-- Sub-branch 1a: Yes -> Z-score -->
  <line x1="120" y1="170" x2="80" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="85" y="190" fill="#059669" font-family="-apple-system, sans-serif" font-size="9" font-weight="700">Yes (Normal)</text>
  <rect x="20" y="210" width="120" height="45" rx="6" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="80" y="230" fill="#047857" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Z-Score</text>
  <text x="80" y="244" fill="#065F46" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">|z| &gt; 3.0 threshold</text>

  <!-- Sub-branch 1b: No -> IQR -->
  <line x1="200" y1="170" x2="240" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="235" y="190" fill="#D97706" font-family="-apple-system, sans-serif" font-size="9" font-weight="700">No (Skewed)</text>
  <rect x="180" y="210" width="120" height="45" rx="6" fill="#FEF3C7" stroke="#FDE68A"/>
  <text x="240" y="230" fill="#D97706" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">IQR Boxplot</text>
  <text x="240" y="244" fill="#92400E" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Fences Q1/Q3 ± 1.5×IQR</text>

  <!-- Branch 2: Multivariate -->
  <line x1="470" y1="85" x2="620" y2="130" stroke="#94A3B8" stroke-width="2"/>
  <text x="575" y="105" fill="#475569" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Multiple Features (2D to 1,000D)</text>
  
  <rect x="520" y="130" width="200" height="40" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="620" y="154" fill="#0F172A" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">What is the data structure &amp; labels?</text>
  
  <!-- Sub-branch 2a: General Tabular & High-D -> Isolation Forest -->
  <line x1="560" y1="170" x2="420" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="470" y="190" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="9" font-weight="700">High-D / Tabular</text>
  <rect x="340" y="210" width="160" height="55" rx="6" fill="#FFF1F2" stroke="#FECDD3"/>
  <text x="420" y="230" fill="#BE123C" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Isolation Forest</text>
  <text x="420" y="244" fill="#475569" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Default Top Pick! Fast,</text>
  <text x="420" y="256" fill="#475569" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">no scaling needed</text>

  <!-- Sub-branch 2b: Varying Local Density -> LOF -->
  <line x1="620" y1="170" x2="620" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="625" y="190" fill="#0369A1" font-family="-apple-system, sans-serif" font-size="9" font-weight="700">Variable Density</text>
  <rect x="530" y="210" width="160" height="55" rx="6" fill="#F0F9FF" stroke="#BAE6FD"/>
  <text x="610" y="230" fill="#0284C7" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" text-anchor="middle">Local Outlier Factor</text>
  <text x="610" y="244" fill="#475569" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">Detects relative density,</text>
  <text x="610" y="256" fill="#475569" font-family="-apple-system, sans-serif" font-size="9" text-anchor="middle">requires distance scaling</text>

  <!-- Sub-branch 2c: Clean Normal Training Only -> One-Class SVM -->
  <line x1="680" y1="170" x2="740" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
  <text x="730" y="190" fill="#7C3AED" font-family="-apple-system, sans-serif" font-size="9" font-weight="700">Normal Only</text>
  <rect x="680" y="210" width="115" height="55" rx="6" fill="#F5F3FF" stroke="#DDD6FE"/>
  <text x="737" y="230" fill="#7C3AED" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" text-anchor="middle">One-Class SVM</text>
  <text x="737" y="244" fill="#475569" font-family="-apple-system, sans-serif" font-size="8" text-anchor="middle">Novelty bounds,</text>
  <text x="737" y="256" fill="#475569" font-family="-apple-system, sans-serif" font-size="8" text-anchor="middle">strict normal train</text>

  <!-- Bottom banner -->
  <rect x="80" y="300" width="640" height="35" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="400" y="322" fill="#475569" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Rule of Thumb: Start with Z-score/IQR for single variables. Use Isolation Forest as your reliable multivariate baseline.</text>
</svg>'''

if __name__ == "__main__":
    print(f"Generated {len(svgs)} SVGs successfully.")
    for k, v in svgs.items():
        assert v.startswith("<svg") and v.endswith("</svg>")
        print(f"  {k}: {len(v)} chars")
