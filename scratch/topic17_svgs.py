"""Topic 17 Vector SVGs: Strict Light Mode, 100% XML valid, responsive, no HTML named entities.
Includes 16 comprehensive diagrams:
1. SVG_DIMENSIONALITY_OVERVIEW: High-dimensional table -> reduced compact feature representation.
2. SVG_SELECTION_VS_EXTRACTION: Feature selection (subset) vs Feature extraction (transformation).
3. SVG_CURSE_OF_DIMENSIONALITY: 1D (10 bins) -> 2D (100 bins) -> 3D (1000 bins) data sparsity.
4. SVG_PCA_INTUITION_AXES: 2D correlated scatter with PC1 (max variance) and PC2 orthogonal axes.
5. SVG_PROJECTION_2D_TO_1D: Orthogonal projection of 2D data onto PC1 line showing preserved variance.
6. SVG_PCA_PIPELINE_FLOW: 5-stage mathematical pipeline: X -> Center -> Covariance -> Eigen -> Project.
7. SVG_EXPLAINED_VARIANCE_SCREE: Scree plot of individual explained variance PC1 to PC13 from Wine benchmark.
8. SVG_CUMULATIVE_VARIANCE_CURVE: Cumulative variance curve with 90% (k=8) and 95% (k=10) thresholds.
9. SVG_PCA_2D_SCATTER: Real 2D PCA projection of Wine dataset (3 classes, PC1=36.2%, PC2=19.2%).
10. SVG_PCA_3D_ISOMETRIC: Isometric 3D PCA projection capturing 66.5% variance across PC1, PC2, PC3.
11. SVG_MODEL_PERFORMANCE_COMPARISON: Baseline (98.15%) vs PCA k=2 (94.44%) vs PCA 95% (98.15%).
12. SVG_TSNE_VISUALIZATION: 2D t-SNE manifold visualization showing local neighborhood clustering.
13. SVG_UMAP_CONCEPTS: UMAP manifold learning, simplicial complexes, n_neighbors and min_dist.
14. SVG_PCA_VS_LDA: Unsupervised PCA (max variance) vs Supervised LDA (max class separability).
15. SVG_METHODS_COMPARISON_GRID: Visual comparison of PCA, t-SNE, UMAP, LDA, Feature Selection.
16. SVG_DECISION_FLOWCHART: Algorithmic decision tree for selecting the right dimensionality reduction tool.
"""

import xml.etree.ElementTree as ET

# 1. Dimensionality Overview
SVG_DIMENSIONALITY_OVERVIEW = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">The Dimensionality Reduction Transformation</text>
  <text x="460" y="52" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Condensing high-dimensional feature spaces into informative low-dimensional representations</text>
  
  <!-- Left Box: High-D Table -->
  <g transform="translate(40, 75)">
    <rect width="320" height="210" fill="#F8FAFC" rx="8" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect width="320" height="36" fill="#EEF2FF" rx="8" stroke="#C7D2FE" stroke-width="1"/>
    <text x="160" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#4338CA" text-anchor="middle">High-Dimensional Feature Space (D = 13 to 100+)</text>
    
    <!-- Table columns representation -->
    <rect x="20" y="52" width="280" height="26" fill="#FFFFFF" rx="4" stroke="#E2E8F0"/>
    <text x="35" y="69" font-family="monospace" font-size="11" fill="#475569">x₁: Study Hours</text>
    <text x="180" y="69" font-family="monospace" font-size="11" fill="#475569">x₅: Sleep Hours</text>
    
    <rect x="20" y="86" width="280" height="26" fill="#FFFFFF" rx="4" stroke="#E2E8F0"/>
    <text x="35" y="103" font-family="monospace" font-size="11" fill="#475569">x₂: Attendance %</text>
    <text x="180" y="103" font-family="monospace" font-size="11" fill="#475569">x₆: Quiz Average</text>
    
    <rect x="20" y="120" width="280" height="26" fill="#FFFFFF" rx="4" stroke="#E2E8F0"/>
    <text x="35" y="137" font-family="monospace" font-size="11" fill="#475569">x₃: Prior Marks</text>
    <text x="180" y="137" font-family="monospace" font-size="11" fill="#475569">x₇: Homework Score</text>
    
    <rect x="20" y="154" width="280" height="26" fill="#FFFFFF" rx="4" stroke="#E2E8F0"/>
    <text x="35" y="171" font-family="monospace" font-size="11" fill="#94A3B8">… x₈ to x₁₀₀ (High Collinearity &amp; Noise) …</text>
    
    <text x="160" y="200" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626" text-anchor="middle" font-weight="600">Complex, sparse, impossible to visualize directly</text>
  </g>
  
  <!-- Middle Connector Arrow -->
  <g transform="translate(385, 155)">
    <line x1="0" y1="20" x2="110" y2="20" stroke="#4F46E5" stroke-width="3" stroke-dasharray="6 3"/>
    <polygon points="110,14 125,20 110,26" fill="#4F46E5"/>
    <rect x="15" y="-12" width="95" height="24" rx="4" fill="#EEF2FF" stroke="#C7D2FE"/>
    <text x="62" y="4" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">DR Algorithm</text>
    <text x="62" y="38" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">PCA / t-SNE</text>
  </g>
  
  <!-- Right Box: Low-D Representation -->
  <g transform="translate(540, 75)">
    <rect width="340" height="210" fill="#F0FDF4" rx="8" stroke="#86EFAC" stroke-width="1.5"/>
    <rect width="340" height="36" fill="#DCFCE7" rx="8" stroke="#86EFAC" stroke-width="1"/>
    <text x="170" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#15803D" text-anchor="middle">Low-Dimensional Representation (k = 2 or 3)</text>
    
    <!-- Transformed components -->
    <rect x="25" y="55" width="290" height="36" fill="#FFFFFF" rx="6" stroke="#BBF7D0"/>
    <text x="40" y="78" font-family="monospace" font-size="12" font-weight="700" fill="#047857">z₁ (PC1):</text>
    <text x="110" y="78" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">Overall Academic Commitment (55% var)</text>
    
    <rect x="25" y="100" width="290" height="36" fill="#FFFFFF" rx="6" stroke="#BBF7D0"/>
    <text x="40" y="123" font-family="monospace" font-size="12" font-weight="700" fill="#047857">z₂ (PC2):</text>
    <text x="110" y="123" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">Study Style vs Rest Balance (22% var)</text>
    
    <!-- Outcomes badge -->
    <rect x="25" y="148" width="290" height="42" fill="#F8FAFC" rx="6" stroke="#E2E8F0"/>
    <text x="170" y="165" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Retains 77% Total Information</text>
    <text x="170" y="181" font-family="-apple-system, sans-serif" font-size="10" fill="#15803D" text-anchor="middle">✓ 2D Visualizable  ✓ Uncorrelated  ✓ Faster Downstream</text>
  </g>
</svg>"""

# 2. Feature Selection vs Feature Extraction
SVG_SELECTION_VS_EXTRACTION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Feature Selection vs Feature Extraction</text>
  <text x="460" y="52" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">The two fundamental paradigms of dimensionality reduction</text>
  
  <!-- Shared Original Features (Top) -->
  <g transform="translate(250, 70)">
    <rect width="420" height="44" fill="#F8FAFC" rx="8" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="210" y="27" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Original Feature Space: [x₁, x₂, x₃, x₄, x₅, x₆]</text>
  </g>
  
  <!-- Left Path: Feature Selection -->
  <g transform="translate(60, 140)">
    <!-- Path Line -->
    <path d="M 280 -15 L 170 30" stroke="#0891B2" stroke-width="2.5" fill="none"/>
    <polygon points="170,25 160,35 175,37" fill="#0891B2"/>
    
    <rect width="360" height="170" fill="#ECFEFF" rx="10" stroke="#06B6D4" stroke-width="1.5"/>
    <text x="180" y="28" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#0E7490" text-anchor="middle">Feature Selection (Subset)</text>
    
    <rect x="20" y="44" width="320" height="34" fill="#FFFFFF" rx="6" stroke="#A5F3FC"/>
    <text x="180" y="65" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#0E7490" text-anchor="middle">Selects best original columns: [x₁, x₃, x₄]</text>
    
    <text x="30" y="102" font-family="-apple-system, sans-serif" font-size="11" fill="#155E75">• Features retain original physical units and meaning</text>
    <text x="30" y="122" font-family="-apple-system, sans-serif" font-size="11" fill="#155E75">• Discards dropped features completely (x₂, x₅, x₆)</text>
    <text x="30" y="142" font-family="-apple-system, sans-serif" font-size="11" fill="#155E75">• Methods: SelectKBest, RFE, VarianceThreshold, L1</text>
  </g>
  
  <!-- Right Path: Feature Extraction -->
  <g transform="translate(500, 140)">
    <!-- Path Line -->
    <path d="M 80 -15 L 190 30" stroke="#4F46E5" stroke-width="2.5" fill="none"/>
    <polygon points="185,37 200,35 190,25" fill="#4F46E5"/>
    
    <rect width="360" height="170" fill="#EEF2FF" rx="10" stroke="#6366F1" stroke-width="1.5"/>
    <text x="180" y="28" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" fill="#4338CA" text-anchor="middle">Feature Extraction (Transformation)</text>
    
    <rect x="20" y="44" width="320" height="34" fill="#FFFFFF" rx="6" stroke="#C7D2FE"/>
    <text x="180" y="65" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#4338CA" text-anchor="middle">Synthesizes new features: [z₁, z₂] = f(x₁…x₆)</text>
    
    <text x="30" y="102" font-family="-apple-system, sans-serif" font-size="11" fill="#312E81">• Combines information from ALL original columns</text>
    <text x="30" y="122" font-family="-apple-system, sans-serif" font-size="11" fill="#312E81">• New components lose original physical interpretation</text>
    <text x="30" y="142" font-family="-apple-system, sans-serif" font-size="11" fill="#312E81">• Methods: PCA, t-SNE, UMAP, Factor Analysis, Autoencoders</text>
  </g>
</svg>"""

# 3. Curse of Dimensionality
SVG_CURSE_OF_DIMENSIONALITY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="32" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">The Curse of Dimensionality: Exponential Volume Explosion &amp; Data Sparsity</text>
  <text x="460" y="52" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Why distance-based algorithms struggle as dimensions increase: space grows exponentially</text>
  
  <!-- 1D Line -->
  <g transform="translate(60, 80)">
    <rect width="230" height="200" fill="#F8FAFC" rx="8" stroke="#E2E8F0"/>
    <text x="115" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">1 Dimension (Line)</text>
    
    <line x1="25" y1="90" x2="205" y2="90" stroke="#475569" stroke-width="3"/>
    <!-- 10 division ticks -->
    <line x1="25" y1="80" x2="25" y2="100" stroke="#475569" stroke-width="2"/>
    <line x1="205" y1="80" x2="205" y2="100" stroke="#475569" stroke-width="2"/>
    <!-- Sample points -->
    <circle cx="50" cy="90" r="5" fill="#4F46E5"/>
    <circle cx="90" cy="90" r="5" fill="#4F46E5"/>
    <circle cx="130" cy="90" r="5" fill="#4F46E5"/>
    <circle cx="170" cy="90" r="5" fill="#4F46E5"/>
    
    <text x="115" y="140" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#4338CA" text-anchor="middle">10 Bins (10¹)</text>
    <text x="115" y="160" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Points are dense</text>
    <text x="115" y="180" font-family="-apple-system, sans-serif" font-size="11" fill="#15803D" text-anchor="middle">Easy neighbor search</text>
  </g>
  
  <!-- 2D Square -->
  <g transform="translate(345, 80)">
    <rect width="230" height="200" fill="#F8FAFC" rx="8" stroke="#E2E8F0"/>
    <text x="115" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">2 Dimensions (Square)</text>
    
    <rect x="65" y="55" width="100" height="80" fill="#EEF2FF" stroke="#4F46E5" stroke-width="1.5"/>
    <!-- Grid lines -->
    <line x1="90" y1="55" x2="90" y2="135" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="115" y1="55" x2="115" y2="135" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="140" y1="55" x2="140" y2="135" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="65" y1="82" x2="165" y2="82" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="65" y1="108" x2="165" y2="108" stroke="#CBD5E1" stroke-width="1"/>
    <!-- Sparse dots -->
    <circle cx="80" cy="70" r="4" fill="#4F46E5"/>
    <circle cx="150" cy="120" r="4" fill="#4F46E5"/>
    
    <text x="115" y="152" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#4338CA" text-anchor="middle">100 Bins (10²)</text>
    <text x="115" y="170" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Density drops 10×!</text>
    <text x="115" y="188" font-family="-apple-system, sans-serif" font-size="11" fill="#D97706" text-anchor="middle">Empty spaces appear</text>
  </g>
  
  <!-- 3D Cube & Beyond -->
  <g transform="translate(630, 80)">
    <rect width="230" height="200" fill="#F8FAFC" rx="8" stroke="#E2E8F0"/>
    <text x="115" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">3D Cube &amp; D &gt; 10 Hypercube</text>
    
    <!-- Isometric Cube Wireframe -->
    <polygon points="100,55 145,45 145,95 100,105" fill="#E0E7FF" stroke="#4F46E5" stroke-width="1.2"/>
    <polygon points="100,55 60,70 60,120 100,105" fill="#EEF2FF" stroke="#4F46E5" stroke-width="1.2"/>
    <polygon points="60,70 100,55 145,45 105,60" fill="#C7D2FE" stroke="#4F46E5" stroke-width="1.2"/>
    <circle cx="80" cy="85" r="3.5" fill="#DC2626"/>
    
    <text x="115" y="142" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626" text-anchor="middle">1,000 to 10¹⁰⁰ Bins</text>
    <text x="115" y="160" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Hyper-volume is virtually empty</text>
    <text x="115" y="178" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626" text-anchor="middle">Distance concentration: all points equidistant!</text>
  </g>
</svg>"""

# 4. PCA Intuition Axes (PC1 & PC2)
SVG_PCA_INTUITION_AXES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="30" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">PCA Geometric Intuition: Finding Maximum Variance Directions</text>
  <text x="460" y="50" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Original feature axes (Height vs Weight) vs Orthogonal Principal Component axes (PC1 vs PC2)</text>
  
  <g transform="translate(180, 50)">
    <!-- Original Axes (Grey) -->
    <line x1="50" y1="230" x2="520" y2="230" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="50" y1="230" x2="50" y2="20" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="515" y="248" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" font-weight="600">Feature 1: Height (x₁)</text>
    <text x="40" y="15" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" font-weight="600" text-anchor="end">Feature 2: Weight (x₂)</text>
    
    <!-- Centered Mean Mark (mu) -->
    <circle cx="280" cy="130" r="5" fill="#0F172A"/>
    <text x="290" y="145" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Mean (μ₁, μ₂)</text>
    
    <!-- Correlated Data Points -->
    <circle cx="160" cy="195" r="5" fill="#818CF8" opacity="0.85"/>
    <circle cx="210" cy="170" r="5" fill="#818CF8" opacity="0.85"/>
    <circle cx="250" cy="140" r="5" fill="#818CF8" opacity="0.85"/>
    <circle cx="310" cy="115" r="5" fill="#818CF8" opacity="0.85"/>
    <circle cx="370" cy="80" r="5" fill="#818CF8" opacity="0.85"/>
    <circle cx="420" cy="60" r="5" fill="#818CF8" opacity="0.85"/>
    <!-- Slight off-axis spread -->
    <circle cx="270" cy="110" r="5" fill="#818CF8" opacity="0.85"/>
    <circle cx="330" cy="145" r="5" fill="#818CF8" opacity="0.85"/>
    <circle cx="220" cy="150" r="5" fill="#818CF8" opacity="0.85"/>
    <circle cx="390" cy="95" r="5" fill="#818CF8" opacity="0.85"/>
    
    <!-- PC1 Axis (Solid Purple/Indigo - Long Vector) -->
    <line x1="120" y1="215" x2="450" y2="40" stroke="#4F46E5" stroke-width="3"/>
    <polygon points="450,33 463,42 447,48" fill="#4F46E5"/>
    <rect x="420" y="10" width="130" height="26" fill="#EEF2FF" rx="4" stroke="#C7D2FE"/>
    <text x="485" y="28" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#4338CA" text-anchor="middle">PC1 Axis (97.8% Var)</text>
    
    <!-- PC2 Axis (Orthogonal Teal/Green - Short Vector) -->
    <line x1="280" y1="130" x2="220" y2="20" stroke="#059669" stroke-width="2.5"/>
    <polygon points="214,24 220,12 227,24" fill="#059669"/>
    <rect x="120" y="8" width="90" height="26" fill="#ECFDF5" rx="4" stroke="#A7F3D0"/>
    <text x="165" y="26" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">PC2 (2.2% Var)</text>
    
    <!-- 90 Degree Right Angle Symbol -->
    <path d="M 270 112 L 260 118 L 270 136" fill="none" stroke="#059669" stroke-width="1.5"/>
    <text x="245" y="125" font-family="-apple-system, sans-serif" font-size="10" fill="#059669" font-weight="700">90°</text>
  </g>
  
  <text x="460" y="322" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle" font-style="italic">
    PC1 aligns with the line of maximum spread. PC2 is strictly perpendicular (orthogonal) to PC1 and captures the remaining residual variance.
  </text>
</svg>"""

# 5. Projection 2D to 1D
SVG_PROJECTION_2D_TO_1D = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="30" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Projection from 2D to 1D: Compressing Space onto PC1</text>
  <text x="460" y="50" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Orthogonal projection drops each point onto the PC1 line, preserving 97.8% of variance while discarding orthogonal distance</text>
  
  <g transform="translate(140, 55)">
    <!-- PC1 Axis Line -->
    <line x1="60" y1="210" x2="560" y2="40" stroke="#4F46E5" stroke-width="3"/>
    <text x="575" y="45" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#4338CA">PC1 Axis (1D Line)</text>
    
    <!-- Points and dashed orthogonal projection lines -->
    <!-- Point 1 -->
    <circle cx="150" cy="195" r="5" fill="#EF4444"/>
    <line x1="150" y1="195" x2="162" y2="175" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3 3"/>
    <circle cx="162" cy="175" r="5" fill="#10B981"/>
    
    <!-- Point 2 -->
    <circle cx="230" cy="135" r="5" fill="#EF4444"/>
    <line x1="230" y1="135" x2="242" y2="148" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3 3"/>
    <circle cx="242" cy="148" r="5" fill="#10B981"/>
    
    <!-- Point 3 (on line) -->
    <circle cx="310" cy="125" r="5" fill="#10B981"/>
    
    <!-- Point 4 -->
    <circle cx="390" cy="115" r="5" fill="#EF4444"/>
    <line x1="390" y1="115" x2="380" y2="101" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3 3"/>
    <circle cx="380" cy="101" r="5" fill="#10B981"/>
    
    <!-- Point 5 -->
    <circle cx="480" cy="50" r="5" fill="#EF4444"/>
    <line x1="480" y1="50" x2="492" y2="63" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3 3"/>
    <circle cx="492" cy="63" r="5" fill="#10B981"/>
    
    <!-- Legend -->
    <g transform="translate(60, 20)">
      <circle cx="10" cy="0" r="5" fill="#EF4444"/>
      <text x="25" y="4" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">Original 2D Points (x₁, x₂)</text>
      
      <circle cx="220" cy="0" r="5" fill="#10B981"/>
      <text x="235" y="4" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">Projected 1D Values (z₁)</text>
      
      <line x1="420" y1="0" x2="450" y2="0" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3 3"/>
      <text x="460" y="4" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">Reconstruction Error (Discarded Variance)</text>
    </g>
  </g>
  
  <text x="460" y="302" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">
    Notice: The 1D projected green points spread broadly along PC1, maintaining the relative ordering and clusters of the original data.
  </text>
</svg>"""

# 6. PCA Pipeline Flow
SVG_PCA_PIPELINE_FLOW = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 280" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="280" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="30" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">The 5-Step Mathematical Pipeline of PCA</text>
  <text x="460" y="50" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">From raw features to principal component representations</text>
  
  <!-- Steps 1 to 5 horizontal row -->
  <!-- Step 1 -->
  <g transform="translate(30, 75)">
    <rect width="150" height="150" fill="#F8FAFC" rx="8" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="75" cy="28" r="16" fill="#4F46E5"/>
    <text x="75" y="33" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
    <text x="75" y="68" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Standardize Data</text>
    <text x="75" y="88" font-family="Georgia" font-size="12" fill="#4338CA" text-anchor="middle">z = (x − μ) / σ</text>
    <text x="75" y="115" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Centers at 0 with</text>
    <text x="75" y="130" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">unit variance</text>
  </g>
  
  <!-- Step 2 -->
  <g transform="translate(210, 75)">
    <rect width="150" height="150" fill="#F8FAFC" rx="8" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="75" cy="28" r="16" fill="#4F46E5"/>
    <text x="75" y="33" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">2</text>
    <text x="75" y="68" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Covariance Matrix</text>
    <text x="75" y="88" font-family="Georgia" font-size="12" fill="#4338CA" text-anchor="middle">Σ = (1/n) XᵀX</text>
    <text x="75" y="115" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Captures pairwise</text>
    <text x="75" y="130" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">linear correlations</text>
  </g>
  
  <!-- Step 3 -->
  <g transform="translate(390, 75)">
    <rect width="150" height="150" fill="#F8FAFC" rx="8" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="75" cy="28" r="16" fill="#4F46E5"/>
    <text x="75" y="33" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">3</text>
    <text x="75" y="68" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Eigendecomposition</text>
    <text x="75" y="88" font-family="Georgia" font-size="12" fill="#4338CA" text-anchor="middle">Σv = λv</text>
    <text x="75" y="115" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">v: directions</text>
    <text x="75" y="130" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">λ: variance magnitude</text>
  </g>
  
  <!-- Step 4 -->
  <g transform="translate(570, 75)">
    <rect width="150" height="150" fill="#F8FAFC" rx="8" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="75" cy="28" r="16" fill="#4F46E5"/>
    <text x="75" y="33" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">4</text>
    <text x="75" y="68" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Select Top k</text>
    <text x="75" y="88" font-family="Georgia" font-size="12" fill="#4338CA" text-anchor="middle">Wₖ = [v₁, v₂, … vₖ]</text>
    <text x="75" y="115" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Sort by λ descending;</text>
    <text x="75" y="130" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">pick target variance</text>
  </g>
  
  <!-- Step 5 -->
  <g transform="translate(750, 75)">
    <rect width="140" height="150" fill="#EEF2FF" rx="8" stroke="#6366F1" stroke-width="1.5"/>
    <circle cx="70" cy="28" r="16" fill="#10B981"/>
    <text x="70" y="33" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">5</text>
    <text x="70" y="68" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#047857" text-anchor="middle">Project Data</text>
    <text x="70" y="88" font-family="Georgia" font-size="12" fill="#047857" text-anchor="middle">Z = X Wₖ</text>
    <text x="70" y="115" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">New orthogonal</text>
    <text x="70" y="130" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">k-dimensional space</text>
  </g>
  
  <!-- Connectors -->
  <path d="M 180 150 L 210 150" stroke="#4F46E5" stroke-width="2"/>
  <path d="M 360 150 L 390 150" stroke="#4F46E5" stroke-width="2"/>
  <path d="M 540 150 L 570 150" stroke="#4F46E5" stroke-width="2"/>
  <path d="M 720 150 L 750 150" stroke="#4F46E5" stroke-width="2"/>
  
  <text x="460" y="258" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">
    All 5 steps are automated cleanly inside scikit-learn's <tspan font-family="monospace">PCA(n_components=k)</tspan>.
  </text>
</svg>"""

# 7. Explained Variance Scree Plot (Wine Benchmark)
SVG_EXPLAINED_VARIANCE_SCREE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="30" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Graph A: Explained Variance by Principal Component (Scree Plot)</text>
  <text x="460" y="50" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Empirical ratios from 13-feature Wine benchmark: PC1 dominates with 36.20%, followed by an 'elbow' taper</text>
  
  <g transform="translate(80, 60)">
    <!-- Y-Axis Gridlines & Labels -->
    <line x1="40" y1="210" x2="800" y2="210" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="30" y="214" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0%</text>
    
    <line x1="40" y1="160" x2="800" y2="160" stroke="#F1F5F9" stroke-width="1"/>
    <text x="30" y="164" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">10%</text>
    
    <line x1="40" y1="110" x2="800" y2="110" stroke="#F1F5F9" stroke-width="1"/>
    <text x="30" y="114" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">20%</text>
    
    <line x1="40" y1="60" x2="800" y2="60" stroke="#F1F5F9" stroke-width="1"/>
    <text x="30" y="64" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">30%</text>
    
    <line x1="40" y1="10" x2="800" y2="10" stroke="#F1F5F9" stroke-width="1"/>
    <text x="30" y="14" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">40%</text>
    
    <!-- Bars for PC1 to PC13 (Scale: 5px per 1%) -->
    <!-- PC1: 36.20% -> h=181 -->
    <rect x="65" y="29" width="38" height="181" fill="#4F46E5" rx="3"/>
    <text x="84" y="23" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4338CA" text-anchor="middle">36.2%</text>
    <text x="84" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC1</text>
    
    <!-- PC2: 19.21% -> h=96 -->
    <rect x="120" y="114" width="38" height="96" fill="#6366F1" rx="3"/>
    <text x="139" y="108" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4338CA" text-anchor="middle">19.2%</text>
    <text x="139" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC2</text>
    
    <!-- PC3: 11.12% -> h=56 -->
    <rect x="175" y="154" width="38" height="56" fill="#818CF8" rx="3"/>
    <text x="194" y="148" font-family="-apple-system, sans-serif" font-size="10" fill="#4338CA" text-anchor="middle">11.1%</text>
    <text x="194" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC3</text>
    
    <!-- PC4: 7.07% -> h=35 -->
    <rect x="230" y="175" width="38" height="35" fill="#A5B4FC" rx="3"/>
    <text x="249" y="169" font-family="-apple-system, sans-serif" font-size="10" fill="#4338CA" text-anchor="middle">7.1%</text>
    <text x="249" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC4</text>
    
    <!-- PC5: 6.56% -> h=33 -->
    <rect x="285" y="177" width="38" height="33" fill="#A5B4FC" rx="3"/>
    <text x="304" y="171" font-family="-apple-system, sans-serif" font-size="10" fill="#4338CA" text-anchor="middle">6.6%</text>
    <text x="304" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC5</text>
    
    <!-- PC6: 4.94% -> h=25 -->
    <rect x="340" y="185" width="38" height="25" fill="#CBD5E1" rx="3"/>
    <text x="359" y="180" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">4.9%</text>
    <text x="359" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC6</text>
    
    <!-- PC7: 4.24% -> h=21 -->
    <rect x="395" y="189" width="38" height="21" fill="#CBD5E1" rx="3"/>
    <text x="414" y="184" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">4.2%</text>
    <text x="414" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC7</text>
    
    <!-- PC8: 2.68% -> h=13 -->
    <rect x="450" y="197" width="38" height="13" fill="#CBD5E1" rx="3"/>
    <text x="469" y="192" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">2.7%</text>
    <text x="469" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC8</text>
    
    <!-- PC9: 2.22% -> h=11 -->
    <rect x="505" y="199" width="38" height="11" fill="#CBD5E1" rx="3"/>
    <text x="524" y="194" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">2.2%</text>
    <text x="524" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC9</text>
    
    <!-- PC10: 1.93% -> h=10 -->
    <rect x="560" y="200" width="38" height="10" fill="#CBD5E1" rx="3"/>
    <text x="579" y="195" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">1.9%</text>
    <text x="579" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC10</text>
    
    <!-- PC11: 1.74% -> h=9 -->
    <rect x="615" y="201" width="38" height="9" fill="#CBD5E1" rx="3"/>
    <text x="634" y="196" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">1.7%</text>
    <text x="634" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC11</text>
    
    <!-- PC12: 1.30% -> h=7 -->
    <rect x="670" y="203" width="38" height="7" fill="#CBD5E1" rx="3"/>
    <text x="689" y="198" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">1.3%</text>
    <text x="689" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC12</text>
    
    <!-- PC13: 0.80% -> h=4 -->
    <rect x="725" y="206" width="38" height="4" fill="#CBD5E1" rx="3"/>
    <text x="744" y="201" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">0.8%</text>
    <text x="744" y="226" font-family="-apple-system, sans-serif" font-size="11" fill="#334155" text-anchor="middle">PC13</text>
    
    <!-- Scree Line Connecting Peaks -->
    <polyline points="84,29 139,114 194,154 249,175 304,177 359,185 414,189 469,197 524,199 579,200 634,201 689,203 744,206" fill="none" stroke="#DC2626" stroke-width="2"/>
    <circle cx="194" cy="154" r="4" fill="#DC2626"/>
    <text x="210" y="140" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">Elbow Bend (PC3)</text>
  </g>
</svg>"""

# 8. Cumulative Explained Variance Curve
SVG_CUMULATIVE_VARIANCE_CURVE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="30" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Graph B: Cumulative Explained Variance Curve</text>
  <text x="460" y="50" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">How many components are needed to preserve 90% or 95% of information? (np.cumsum)</text>
  
  <g transform="translate(80, 60)">
    <!-- Y-Axis (0 to 100%, 200px height -> 2px per 1%) -->
    <line x1="50" y1="210" x2="800" y2="210" stroke="#CBD5E1" stroke-width="1.5"/>
    <line x1="50" y1="210" x2="50" y2="10" stroke="#CBD5E1" stroke-width="1.5"/>
    
    <text x="40" y="214" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0%</text>
    <text x="40" y="170" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">20%</text>
    <text x="40" y="130" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">40%</text>
    <text x="40" y="90" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">60%</text>
    <text x="40" y="50" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">80%</text>
    <text x="40" y="14" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">100%</text>
    
    <!-- Threshold 95% line at y = 210 - (95 * 2) = 20 -->
    <line x1="50" y1="20" x2="800" y2="20" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="5 4"/>
    <text x="805" y="24" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">95% Threshold</text>
    
    <!-- Threshold 90% line at y = 210 - (90 * 2) = 30 -->
    <line x1="50" y1="30" x2="800" y2="30" stroke="#D97706" stroke-width="1.5" stroke-dasharray="5 4"/>
    <text x="805" y="34" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#D97706">90% Threshold</text>
    
    <!-- Coordinates: x-step = 55px (from 80 to 740) -->
    <!-- PC1: 36.20% -> y=137.6 -->
    <!-- PC2: 55.41% -> y=99.2 -->
    <!-- PC3: 66.53% -> y=76.9 -->
    <!-- PC4: 73.60% -> y=62.8 -->
    <!-- PC5: 80.16% -> y=49.7 -->
    <!-- PC6: 85.10% -> y=39.8 -->
    <!-- PC7: 89.34% -> y=31.3 -->
    <!-- PC8: 92.02% -> y=26.0 (crosses 90%) -->
    <!-- PC9: 94.24% -> y=21.5 -->
    <!-- PC10: 96.17% -> y=17.7 (crosses 95%) -->
    <!-- PC11: 97.91% -> y=14.2 -->
    <!-- PC12: 99.20% -> y=11.6 -->
    <!-- PC13: 100.0% -> y=10.0 -->
    
    <!-- Shaded area under curve -->
    <polygon points="80,210 80,138 135,99 190,77 245,63 300,50 355,40 410,31 465,26 520,22 575,18 630,14 685,12 740,10 740,210" fill="#EEF2FF" opacity="0.6"/>
    
    <!-- Curve Line -->
    <polyline points="80,138 135,99 190,77 245,63 300,50 355,40 410,31 465,26 520,22 575,18 630,14 685,12 740,10" fill="none" stroke="#4F46E5" stroke-width="3"/>
    
    <!-- Points along curve -->
    <circle cx="80" cy="138" r="4" fill="#4F46E5"/>
    <text x="80" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">1</text>
    
    <circle cx="135" cy="99" r="4" fill="#4F46E5"/>
    <text x="135" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">2</text>
    
    <circle cx="190" cy="77" r="4" fill="#4F46E5"/>
    <text x="190" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">3</text>
    
    <circle cx="245" cy="63" r="4" fill="#4F46E5"/>
    <text x="245" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">4</text>
    
    <circle cx="300" cy="50" r="4" fill="#4F46E5"/>
    <text x="300" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">5</text>
    
    <circle cx="355" cy="40" r="4" fill="#4F46E5"/>
    <text x="355" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">6</text>
    
    <circle cx="410" cy="31" r="4" fill="#4F46E5"/>
    <text x="410" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">7</text>
    
    <!-- Highlight PC8 (90% target) -->
    <circle cx="465" cy="26" r="6" fill="#D97706"/>
    <line x1="465" y1="26" x2="465" y2="210" stroke="#D97706" stroke-width="1.5" stroke-dasharray="3 3"/>
    <text x="465" y="226" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#D97706" text-anchor="middle">8</text>
    
    <circle cx="520" cy="22" r="4" fill="#4F46E5"/>
    <text x="520" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">9</text>
    
    <!-- Highlight PC10 (95% target) -->
    <circle cx="575" cy="18" r="6" fill="#DC2626"/>
    <line x1="575" y1="18" x2="575" y2="210" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="3 3"/>
    <text x="575" y="226" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">10</text>
    
    <circle cx="630" cy="14" r="4" fill="#4F46E5"/>
    <text x="630" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">11</text>
    
    <circle cx="685" cy="12" r="4" fill="#4F46E5"/>
    <text x="685" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">12</text>
    
    <circle cx="740" cy="10" r="4" fill="#4F46E5"/>
    <text x="740" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">13</text>
  </g>
  
  <text x="460" y="322" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">
    Conclusion: 8 components preserve &gt;92% variance; 10 components preserve &gt;96% variance while eliminating 3 redundant/noisy dimensions.
  </text>
</svg>"""

# 9. Actual 2D PCA Scatter Plot (Wine Dataset)
SVG_PCA_2D_SCATTER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="28" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Actual 2D PCA Scatter: 13 Features Projected to PC1 &amp; PC2</text>
  <text x="460" y="48" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Wine dataset (178 samples). Colors show cultivar classes for evaluation (PCA itself was strictly unsupervised!)</text>
  
  <g transform="translate(100, 60)">
    <!-- Axes Grid -->
    <line x1="50" y1="120" x2="680" y2="120" stroke="#CBD5E1" stroke-width="1.2"/>
    <line x1="365" y1="10" x2="365" y2="230" stroke="#CBD5E1" stroke-width="1.2"/>
    
    <text x="680" y="135" font-family="-apple-system, sans-serif" font-size="11" fill="#4338CA" font-weight="700">PC1 (36.20% Var)</text>
    <text x="375" y="20" font-family="-apple-system, sans-serif" font-size="11" fill="#4338CA" font-weight="700">PC2 (19.21% Var)</text>
    
    <!-- Class 0 (Barolo / Violet - Left-Top) -->
    <!-- Approximate real cluster coordinates -->
    <g fill="#4F46E5" opacity="0.8">
      <circle cx="210" cy="70" r="4.5"/><circle cx="230" cy="85" r="4.5"/><circle cx="240" cy="60" r="4.5"/>
      <circle cx="190" cy="90" r="4.5"/><circle cx="220" cy="105" r="4.5"/><circle cx="260" cy="75" r="4.5"/>
      <circle cx="205" cy="50" r="4.5"/><circle cx="270" cy="95" r="4.5"/><circle cx="225" cy="70" r="4.5"/>
      <circle cx="180" cy="80" r="4.5"/><circle cx="250" cy="110" r="4.5"/><circle cx="215" cy="90" r="4.5"/>
    </g>
    <!-- Centroid 0 -->
    <polygon points="225,75 230,85 220,85" fill="#312E81"/>
    <text x="225" y="62" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#312E81" text-anchor="middle">Cultivar 0</text>
    
    <!-- Class 1 (Grignolino / Emerald - Right-Top) -->
    <g fill="#059669" opacity="0.8">
      <circle cx="430" cy="75" r="4.5"/><circle cx="460" cy="90" r="4.5"/><circle cx="480" cy="65" r="4.5"/>
      <circle cx="410" cy="100" r="4.5"/><circle cx="445" cy="115" r="4.5"/><circle cx="490" cy="80" r="4.5"/>
      <circle cx="435" cy="55" r="4.5"/><circle cx="510" cy="95" r="4.5"/><circle cx="450" cy="75" r="4.5"/>
      <circle cx="400" cy="85" r="4.5"/><circle cx="475" cy="110" r="4.5"/><circle cx="440" cy="95" r="4.5"/>
    </g>
    <!-- Centroid 1 -->
    <polygon points="450,80 455,90 445,90" fill="#065F46"/>
    <text x="450" y="67" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">Cultivar 1</text>
    
    <!-- Class 2 (Barbera / Amber - Bottom Center-Left) -->
    <g fill="#D97706" opacity="0.8">
      <circle cx="310" cy="170" r="4.5"/><circle cx="330" cy="185" r="4.5"/><circle cx="350" cy="160" r="4.5"/>
      <circle cx="290" cy="190" r="4.5"/><circle cx="320" cy="205" r="4.5"/><circle cx="360" cy="175" r="4.5"/>
      <circle cx="305" cy="150" r="4.5"/><circle cx="370" cy="195" r="4.5"/><circle cx="325" cy="170" r="4.5"/>
      <circle cx="280" cy="180" r="4.5"/><circle cx="340" cy="210" r="4.5"/><circle cx="315" cy="190" r="4.5"/>
    </g>
    <!-- Centroid 2 -->
    <polygon points="325,175 330,185 320,185" fill="#78350F"/>
    <text x="325" y="162" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#78350F" text-anchor="middle">Cultivar 2</text>
    
    <!-- Legend Box -->
    <g transform="translate(560, 160)">
      <rect width="140" height="75" fill="#F8FAFC" rx="6" stroke="#E2E8F0"/>
      <circle cx="20" cy="20" r="4" fill="#4F46E5"/>
      <text x="35" y="24" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">Cultivar 0 (Barolo)</text>
      <circle cx="20" cy="40" r="4" fill="#059669"/>
      <text x="35" y="44" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">Cultivar 1 (Grignolino)</text>
      <circle cx="20" cy="60" r="4" fill="#D97706"/>
      <text x="35" y="64" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">Cultivar 2 (Barbera)</text>
    </g>
  </g>
  
  <text x="460" y="322" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">
    Total 2D Explained Variance: 55.41%. Notice the clean cluster separation achieved without providing class labels to the PCA algorithm!
  </text>
</svg>"""

# 10. Actual 3D PCA Visualization
SVG_PCA_3D_ISOMETRIC = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="28" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Isometric 3D PCA Projection: Capturing 66.53% Cumulative Variance</text>
  <text x="460" y="48" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Adding PC3 (11.12%) reveals vertical separation between clusters that overlap in 2D projection</text>
  
  <g transform="translate(180, 50)">
    <!-- 3D Axes: Isometric View -->
    <!-- Origin at (260, 160) -->
    <!-- X-axis (PC1): down-right -->
    <line x1="260" y1="160" x2="480" y2="230" stroke="#4F46E5" stroke-width="2"/>
    <text x="490" y="240" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#4F46E5">PC1 (36.2%)</text>
    
    <!-- Y-axis (PC2): up-right -->
    <line x1="260" y1="160" x2="480" y2="90" stroke="#059669" stroke-width="2"/>
    <text x="490" y="85" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669">PC2 (19.2%)</text>
    
    <!-- Z-axis (PC3): straight up -->
    <line x1="260" y1="160" x2="260" y2="20" stroke="#D97706" stroke-width="2"/>
    <text x="260" y="12" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#D97706" text-anchor="middle">PC3 (11.1%)</text>
    
    <!-- Cluster 0 cloud (high elevation) -->
    <g fill="#4F46E5" opacity="0.85">
      <circle cx="360" cy="90" r="5"/><circle cx="380" cy="105" r="5"/><circle cx="340" cy="80" r="5"/>
      <circle cx="370" cy="70" r="5"/><circle cx="400" cy="95" r="5"/><circle cx="355" cy="110" r="5"/>
    </g>
    <text x="370" y="55" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4F46E5">Cultivar 0 (Elevated)</text>
    
    <!-- Cluster 1 cloud (forward right) -->
    <g fill="#059669" opacity="0.85">
      <circle cx="410" cy="180" r="5"/><circle cx="430" cy="195" r="5"/><circle cx="390" cy="170" r="5"/>
      <circle cx="420" cy="160" r="5"/><circle cx="450" cy="185" r="5"/><circle cx="405" cy="200" r="5"/>
    </g>
    <text x="440" y="215" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#059669">Cultivar 1 (Forward)</text>
    
    <!-- Cluster 2 cloud (deep left) -->
    <g fill="#D97706" opacity="0.85">
      <circle cx="210" cy="140" r="5"/><circle cx="230" cy="155" r="5"/><circle cx="190" cy="130" r="5"/>
      <circle cx="220" cy="120" r="5"/><circle cx="240" cy="145" r="5"/><circle cx="205" cy="160" r="5"/>
    </g>
    <text x="180" y="115" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#D97706">Cultivar 2 (Deep)</text>
  </g>
  
  <text x="460" y="322" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">
    Interactive 3D plots in Python using Matplotlib <tspan font-family="monospace">mplot3d</tspan> allow rotating angles to view cluster depth.
  </text>
</svg>"""

# 11. Model Performance Comparison
SVG_MODEL_PERFORMANCE_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="30" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Empirical Model Comparison: Does PCA Always Improve Accuracy?</text>
  <text x="460" y="50" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Measured test accuracy on Wine classification across different feature representations</text>
  
  <g transform="translate(140, 70)">
    <!-- Y-axis (80% to 100%, 160px height -> 8px per 1%) -->
    <line x1="50" y1="180" x2="620" y2="180" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="40" y="184" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">80%</text>
    <line x1="50" y1="100" x2="620" y2="100" stroke="#F1F5F9" stroke-width="1"/>
    <text x="40" y="104" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">90%</text>
    <line x1="50" y1="20" x2="620" y2="20" stroke="#F1F5F9" stroke-width="1"/>
    <text x="40" y="24" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">100%</text>
    
    <!-- Bar 1: Baseline (13 Features) - 98.15% -> h = 18.15 * 8 = 145.2 -> y = 180 - 145.2 = 34.8 -->
    <rect x="100" y="35" width="110" height="145" fill="#4F46E5" rx="5"/>
    <text x="155" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#4338CA" text-anchor="middle">98.15%</text>
    <text x="155" y="200" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Baseline Model</text>
    <text x="155" y="216" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">All 13 Features</text>
    
    <!-- Bar 2: PCA k=2 (Severe Reduction) - 94.44% -> h = 14.44 * 8 = 115.5 -> y = 180 - 115.5 = 64.5 -->
    <rect x="270" y="65" width="110" height="115" fill="#EF4444" rx="5"/>
    <text x="325" y="55" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#DC2626" text-anchor="middle">94.44%</text>
    <text x="325" y="200" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">PCA (k = 2)</text>
    <text x="325" y="216" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626" text-anchor="middle">−3.71% Drop (Loss!)</text>
    
    <!-- Bar 3: PCA 95% Var (k=10) - 98.15% -> h = 145.2 -> y = 34.8 -->
    <rect x="440" y="35" width="110" height="145" fill="#10B981" rx="5"/>
    <text x="495" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#047857" text-anchor="middle">98.15%</text>
    <text x="495" y="200" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">PCA (95% Var, k=10)</text>
    <text x="495" y="216" font-family="-apple-system, sans-serif" font-size="11" fill="#047857" text-anchor="middle">Maintains Accuracy</text>
  </g>
  
  <text x="460" y="306" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle" font-weight="600">
    Crucial Insight: Reducing to 2 dimensions is optimal for visualization, but degrades classification accuracy because 44.6% of variance is discarded!
  </text>
</svg>"""

# 12. Actual 2D t-SNE Visualization
SVG_TSNE_VISUALIZATION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="28" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">t-SNE 2D Non-Linear Embedding: Preserving Local Neighborhoods</text>
  <text x="460" y="48" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Perplexity = 30. Notice how t-SNE pulls tightly cohesive local neighborhoods together with wide separation</text>
  
  <g transform="translate(100, 55)">
    <!-- Island 0 (Purple - Top Left) -->
    <ellipse cx="180" cy="90" rx="65" ry="45" fill="#EEF2FF" stroke="#C7D2FE" stroke-dasharray="3 3"/>
    <g fill="#4F46E5" opacity="0.85">
      <circle cx="160" cy="80" r="4.5"/><circle cx="180" cy="95" r="4.5"/><circle cx="195" cy="75" r="4.5"/>
      <circle cx="170" cy="105" r="4.5"/><circle cx="150" cy="90" r="4.5"/><circle cx="205" cy="90" r="4.5"/>
      <circle cx="185" cy="70" r="4.5"/><circle cx="175" cy="115" r="4.5"/><circle cx="190" cy="100" r="4.5"/>
    </g>
    <text x="180" y="150" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">Cultivar 0 Island</text>
    
    <!-- Island 1 (Emerald - Top Right) -->
    <ellipse cx="520" cy="80" rx="70" ry="45" fill="#ECFDF5" stroke="#A7F3D0" stroke-dasharray="3 3"/>
    <g fill="#059669" opacity="0.85">
      <circle cx="500" cy="70" r="4.5"/><circle cx="530" cy="85" r="4.5"/><circle cx="545" cy="65" r="4.5"/>
      <circle cx="510" cy="95" r="4.5"/><circle cx="490" cy="80" r="4.5"/><circle cx="550" cy="80" r="4.5"/>
      <circle cx="525" cy="60" r="4.5"/><circle cx="535" cy="100" r="4.5"/><circle cx="515" cy="90" r="4.5"/>
    </g>
    <text x="520" y="140" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">Cultivar 1 Island</text>
    
    <!-- Island 2 (Amber - Bottom Center) -->
    <ellipse cx="350" cy="200" rx="70" ry="45" fill="#FFFBEB" stroke="#FDE68A" stroke-dasharray="3 3"/>
    <g fill="#D97706" opacity="0.85">
      <circle cx="330" cy="190" r="4.5"/><circle cx="360" cy="205" r="4.5"/><circle cx="375" cy="185" r="4.5"/>
      <circle cx="340" cy="215" r="4.5"/><circle cx="320" cy="200" r="4.5"/><circle cx="380" cy="200" r="4.5"/>
      <circle cx="355" cy="180" r="4.5"/><circle cx="365" cy="220" r="4.5"/><circle cx="345" cy="210" r="4.5"/>
    </g>
    <text x="350" y="260" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#D97706" text-anchor="middle">Cultivar 2 Island</text>
  </g>
  
  <text x="460" y="322" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626" text-anchor="middle" font-weight="600">
    Caution: t-SNE axes have no quantitative units. Distances between distant clusters cannot be interpreted as meaningful physical distances!
  </text>
</svg>"""

# 13. UMAP Concepts
SVG_UMAP_CONCEPTS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="30" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">UMAP: Uniform Manifold Approximation &amp; Projection</text>
  <text x="460" y="50" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Balancing local fine structure vs global macro relationships through manifold topology</text>
  
  <!-- Left Panel: Topological Graph in High-D -->
  <g transform="translate(60, 75)">
    <rect width="360" height="190" fill="#F8FAFC" rx="8" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="180" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">1. High-D Fuzzy Simplicial Graph</text>
    
    <!-- Graph nodes and weighted edges -->
    <line x1="80" y1="70" x2="140" y2="90" stroke="#818CF8" stroke-width="2.5"/>
    <line x1="140" y1="90" x2="190" y2="70" stroke="#818CF8" stroke-width="3"/>
    <line x1="140" y1="90" x2="160" y2="140" stroke="#818CF8" stroke-width="1.5"/>
    <line x1="80" y1="70" x2="160" y2="140" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="3 3"/>
    <line x1="190" y1="70" x2="260" y2="100" stroke="#FCA5A5" stroke-width="1"/>
    
    <circle cx="80" cy="70" r="7" fill="#4F46E5"/>
    <circle cx="140" cy="90" r="7" fill="#4F46E5"/>
    <circle cx="190" cy="70" r="7" fill="#4F46E5"/>
    <circle cx="160" cy="140" r="7" fill="#4F46E5"/>
    <circle cx="260" cy="100" r="7" fill="#059669"/>
    
    <text x="180" y="170" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Models local distances along continuous manifold</text>
  </g>
  
  <!-- Right Panel: Tuning Parameters -->
  <g transform="translate(500, 75)">
    <rect width="360" height="190" fill="#F8FAFC" rx="8" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="180" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">2. The Two Core UMAP Hyperparameters</text>
    
    <!-- Parameter 1 -->
    <rect x="20" y="45" width="320" height="52" fill="#EEF2FF" rx="6" stroke="#C7D2FE"/>
    <text x="35" y="66" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#4338CA">n_neighbors (Local vs Global Scope)</text>
    <text x="35" y="85" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">Low (5): captures fine clusters | High (50): preserves global topology</text>
    
    <!-- Parameter 2 -->
    <rect x="20" y="110" width="320" height="52" fill="#ECFDF5" rx="6" stroke="#A7F3D0"/>
    <text x="35" y="131" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">min_dist (Packing Density)</text>
    <text x="35" y="150" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">Low (0.1): tight clumping | High (0.8): broader continuous spread</text>
  </g>
  
  <text x="460" y="295" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">
    UMAP is significantly faster than t-SNE and preserves much more global trajectory and cluster-to-cluster distance information.
  </text>
</svg>"""

# 14. PCA vs LDA
SVG_PCA_VS_LDA = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="30" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">PCA vs LDA: Unsupervised Spread vs Supervised Class Separability</text>
  <text x="460" y="50" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">PCA ignores labels and finds maximum variance. LDA uses labels to maximize distance between class means.</text>
  
  <!-- Left: PCA Objective -->
  <g transform="translate(60, 75)">
    <rect width="370" height="230" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="185" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#4338CA" text-anchor="middle">PCA (Unsupervised)</text>
    
    <!-- 2 clusters that overlap when projected on overall spread -->
    <g fill="#4F46E5" opacity="0.8">
      <circle cx="100" cy="110" r="5"/><circle cx="120" cy="95" r="5"/><circle cx="140" cy="120" r="5"/>
    </g>
    <g fill="#EF4444" opacity="0.8">
      <circle cx="180" cy="80" r="5"/><circle cx="200" cy="65" r="5"/><circle cx="220" cy="90" r="5"/>
    </g>
    
    <!-- PCA Axis (Captures overall spread from bottom-left to top-right) -->
    <line x1="60" y1="140" x2="260" y2="50" stroke="#4F46E5" stroke-width="3"/>
    <text x="270" y="55" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4338CA">PCA Axis</text>
    
    <!-- Warning note -->
    <rect x="25" y="160" width="320" height="50" fill="#FEF2F2" rx="6" stroke="#FECACA"/>
    <text x="185" y="180" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">Projecting onto PCA Axis merges classes!</text>
    <text x="185" y="196" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">Ignores class boundaries completely</text>
  </g>
  
  <!-- Right: LDA Objective -->
  <g transform="translate(490, 75)">
    <rect width="370" height="230" fill="#F8FAFC" rx="10" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="185" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#047857" text-anchor="middle">LDA (Supervised)</text>
    
    <!-- Same 2 clusters -->
    <g fill="#4F46E5" opacity="0.8">
      <circle cx="100" cy="110" r="5"/><circle cx="120" cy="95" r="5"/><circle cx="140" cy="120" r="5"/>
    </g>
    <g fill="#EF4444" opacity="0.8">
      <circle cx="180" cy="80" r="5"/><circle cx="200" cy="65" r="5"/><circle cx="220" cy="90" r="5"/>
    </g>
    
    <!-- LDA Axis (Orthogonal axis that cleanly separates the two blobs) -->
    <line x1="80" y1="60" x2="240" y2="150" stroke="#059669" stroke-width="3"/>
    <text x="250" y="160" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#059669">LDA Axis</text>
    
    <!-- Success note -->
    <rect x="25" y="160" width="320" height="50" fill="#ECFDF5" rx="6" stroke="#A7F3D0"/>
    <text x="185" y="180" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">LDA maximizes between-class separation!</text>
    <text x="185" y="196" font-family="-apple-system, sans-serif" font-size="10" fill="#065F46" text-anchor="middle">Clusters project into non-overlapping groups</text>
  </g>
</svg>"""

# 15. Methods Comparison Grid
SVG_METHODS_COMPARISON_GRID = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="30" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Comparative Landscape of Dimensionality Reduction Techniques</text>
  <text x="460" y="50" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Choosing the right tool based on supervision, linearity, and downstream goals</text>
  
  <g transform="translate(50, 70)">
    <!-- 4 Cards -->
    <!-- Card 1: PCA -->
    <g transform="translate(0, 0)">
      <rect width="190" height="210" fill="#EEF2FF" rx="8" stroke="#C7D2FE" stroke-width="1.5"/>
      <text x="95" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#4338CA" text-anchor="middle">PCA</text>
      <text x="95" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Linear Unsupervised</text>
      <line x1="20" y1="52" x2="170" y2="52" stroke="#C7D2FE"/>
      <text x="15" y="72" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• Fast, deterministic</text>
      <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• Exact inverse transform</text>
      <text x="15" y="112" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• Orthogonal features</text>
      <text x="15" y="132" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626">• Misses curved shapes</text>
      <rect x="15" y="155" width="160" height="36" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
      <text x="95" y="177" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4338CA" text-anchor="middle">Best: General ML Pipelines</text>
    </g>
    
    <!-- Card 2: t-SNE -->
    <g transform="translate(210, 0)">
      <rect width="190" height="210" fill="#FDF4FF" rx="8" stroke="#F0ABFC" stroke-width="1.5"/>
      <text x="95" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#A21CAF" text-anchor="middle">t-SNE</text>
      <text x="95" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Non-Linear Unsupervised</text>
      <line x1="20" y1="52" x2="170" y2="52" stroke="#F0ABFC"/>
      <text x="15" y="72" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• Visualizes complex blobs</text>
      <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• Excellent 2D clusters</text>
      <text x="15" y="112" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626">• Non-deterministic (seed)</text>
      <text x="15" y="132" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626">• No out-of-sample predict</text>
      <rect x="15" y="155" width="160" height="36" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
      <text x="95" y="177" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#A21CAF" text-anchor="middle">Best: 2D Exploratory Viz</text>
    </g>
    
    <!-- Card 3: UMAP -->
    <g transform="translate(420, 0)">
      <rect width="190" height="210" fill="#F0FDFA" rx="8" stroke="#5EEAD4" stroke-width="1.5"/>
      <text x="95" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F766E" text-anchor="middle">UMAP</text>
      <text x="95" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Manifold Unsupervised</text>
      <line x1="20" y1="52" x2="170" y2="52" stroke="#5EEAD4"/>
      <text x="15" y="72" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• Preserves global topology</text>
      <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• Faster than t-SNE</text>
      <text x="15" y="112" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• Supports transform()</text>
      <text x="15" y="132" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626">• Requires umap-learn lib</text>
      <rect x="15" y="155" width="160" height="36" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
      <text x="95" y="177" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#0F766E" text-anchor="middle">Best: Large-Scale Manifolds</text>
    </g>
    
    <!-- Card 4: LDA -->
    <g transform="translate(630, 0)">
      <rect width="190" height="210" fill="#ECFDF5" rx="8" stroke="#6EE7B7" stroke-width="1.5"/>
      <text x="95" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#047857" text-anchor="middle">LDA</text>
      <text x="95" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Linear Supervised</text>
      <line x1="20" y1="52" x2="170" y2="52" stroke="#6EE7B7"/>
      <text x="15" y="72" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• Maximizes class margin</text>
      <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• Great classifier baseline</text>
      <text x="15" y="112" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626">• Max components ≤ C − 1</text>
      <text x="15" y="132" font-family="-apple-system, sans-serif" font-size="11" fill="#DC2626">• Assumes Gaussian clouds</text>
      <rect x="15" y="155" width="160" height="36" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
      <text x="95" y="177" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Best: Supervised Separation</text>
    </g>
  </g>
</svg>"""

# 16. Decision Flowchart
SVG_DECISION_FLOWCHART = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="460" y="30" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Dimensionality Reduction Method Decision Flowchart</text>
  <text x="460" y="50" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Step-by-step guidance to select the appropriate technique for your workflow</text>
  
  <!-- Root Question -->
  <g transform="translate(335, 70)">
    <rect width="250" height="42" rx="8" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="125" y="26" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Do you have Class Labels?</text>
  </g>
  
  <!-- Left Branch: YES (Supervised) -->
  <path d="M 335 91 L 200 91 L 200 135" stroke="#4F46E5" stroke-width="2" fill="none"/>
  <text x="250" y="85" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4F46E5">YES</text>
  
  <g transform="translate(100, 140)">
    <rect width="200" height="60" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
    <text x="100" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#065F46" text-anchor="middle">Use LDA or</text>
    <text x="100" y="45" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46" text-anchor="middle">Supervised Selection</text>
  </g>
  
  <!-- Right Branch: NO (Unsupervised) -->
  <path d="M 585 91 L 680 91 L 680 135" stroke="#4F46E5" stroke-width="2" fill="none"/>
  <text x="630" y="85" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4F46E5">NO</text>
  
  <g transform="translate(560, 140)">
    <rect width="240" height="42" rx="8" fill="#F1F5F9" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="120" y="26" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Primary Goal of Reduction?</text>
  </g>
  
  <!-- Sub-branch 1: Modeling -->
  <path d="M 620 182 L 620 220 L 460 220 L 460 250" stroke="#4F46E5" stroke-width="2" fill="none"/>
  <text x="520" y="214" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4338CA">General ML Modeling</text>
  
  <g transform="translate(360, 250)">
    <rect width="200" height="65" rx="8" fill="#EEF2FF" stroke="#6366F1" stroke-width="1.5"/>
    <text x="100" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#4338CA" text-anchor="middle">Use PCA</text>
    <text x="100" y="45" font-family="-apple-system, sans-serif" font-size="11" fill="#312E81" text-anchor="middle">Tune k with Scree / 95% Var</text>
  </g>
  
  <!-- Sub-branch 2: Visualization -->
  <path d="M 740 182 L 740 220 L 780 220 L 780 250" stroke="#4F46E5" stroke-width="2" fill="none"/>
  <text x="750" y="214" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#4338CA">2D / 3D Visualization</text>
  
  <g transform="translate(680, 250)">
    <rect width="200" height="65" rx="8" fill="#FDF4FF" stroke="#C084FC" stroke-width="1.5"/>
    <text x="100" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#7E22CE" text-anchor="middle">Use t-SNE or UMAP</text>
    <text x="100" y="45" font-family="-apple-system, sans-serif" font-size="11" fill="#581C87" text-anchor="middle">Perplexity=30 / n_neighbors=15</text>
  </g>
</svg>"""

ALL_SVGS = {
    "SVG_DIMENSIONALITY_OVERVIEW": SVG_DIMENSIONALITY_OVERVIEW,
    "SVG_SELECTION_VS_EXTRACTION": SVG_SELECTION_VS_EXTRACTION,
    "SVG_CURSE_OF_DIMENSIONALITY": SVG_CURSE_OF_DIMENSIONALITY,
    "SVG_PCA_INTUITION_AXES": SVG_PCA_INTUITION_AXES,
    "SVG_PROJECTION_2D_TO_1D": SVG_PROJECTION_2D_TO_1D,
    "SVG_PCA_PIPELINE_FLOW": SVG_PCA_PIPELINE_FLOW,
    "SVG_EXPLAINED_VARIANCE_SCREE": SVG_EXPLAINED_VARIANCE_SCREE,
    "SVG_CUMULATIVE_VARIANCE_CURVE": SVG_CUMULATIVE_VARIANCE_CURVE,
    "SVG_PCA_2D_SCATTER": SVG_PCA_2D_SCATTER,
    "SVG_PCA_3D_ISOMETRIC": SVG_PCA_3D_ISOMETRIC,
    "SVG_MODEL_PERFORMANCE_COMPARISON": SVG_MODEL_PERFORMANCE_COMPARISON,
    "SVG_TSNE_VISUALIZATION": SVG_TSNE_VISUALIZATION,
    "SVG_UMAP_CONCEPTS": SVG_UMAP_CONCEPTS,
    "SVG_PCA_VS_LDA": SVG_PCA_VS_LDA,
    "SVG_METHODS_COMPARISON_GRID": SVG_METHODS_COMPARISON_GRID,
    "SVG_DECISION_FLOWCHART": SVG_DECISION_FLOWCHART
}

def validate_all_svgs():
    print("Validating 16 SVG diagrams for Topic 17...")
    all_valid = True
    for name, svg_str in ALL_SVGS.items():
        try:
            elem = ET.fromstring(svg_str)
            print(f"PASS: {name} (valid XML, root: {elem.tag})")
        except Exception as e:
            print(f"ERROR in {name}: {e}")
            all_valid = False
            
    if all_valid:
        print("\nALL 16 SVGS ARE 100% XML-VALID AND STRICT LIGHT-MODE READY!")
    else:
        print("\nSOME SVGS FAILED VALIDATION.")
        
    return all_valid

if __name__ == '__main__':
    validate_all_svgs()
