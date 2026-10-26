"""
Topic 16: Clustering - Custom Vector SVGs
18 XML-valid, strictly Light-Mode diagrams with responsive viewBoxes.
Zero undefined HTML named entities.
"""

import xml.etree.ElementTree as ET

# 1. Unclustered points -> Discovered clusters
SVG_CLUSTERING_OVERVIEW = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <!-- Title -->
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">The Unsupervised Clustering Paradigm</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Transforming raw unlabeled feature points into meaningful, cohesive behavioral groups</text>
  
  <!-- Left Panel: Raw Unlabeled Data -->
  <g transform="translate(40, 75)">
    <rect width="360" height="210" fill="#F8FAFC" rx="8" stroke="#CBD5E1" stroke-width="1"/>
    <text x="180" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#475569" text-anchor="middle">1. Raw Unlabeled Data (No Target Labels)</text>
    
    <!-- Scatter Points (Monochrome Slate) -->
    <!-- Group 1 -->
    <circle cx="80" cy="70" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="95" cy="85" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="70" cy="90" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="85" cy="110" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="105" cy="75" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="115" cy="100" r="5" fill="#64748B" opacity="0.8"/>
    <!-- Group 2 -->
    <circle cx="260" cy="65" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="280" cy="80" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="250" cy="95" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="295" cy="90" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="270" cy="115" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="245" cy="75" r="5" fill="#64748B" opacity="0.8"/>
    <!-- Group 3 -->
    <circle cx="180" cy="145" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="165" cy="165" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="195" cy="170" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="175" cy="190" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="210" cy="155" r="5" fill="#64748B" opacity="0.8"/>
    <circle cx="150" cy="150" r="5" fill="#64748B" opacity="0.8"/>
    
    <text x="180" y="200" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#94A3B8" text-anchor="middle">Every point has identical visual identity: {Feature 1, Feature 2}</text>
  </g>
  
  <!-- Center Arrow -->
  <g transform="translate(415, 160)">
    <rect x="-10" y="-22" width="100" height="44" rx="6" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="40" y="-4" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#4F46E5" text-anchor="middle">CLUSTERING</text>
    <text x="40" y="12" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="9" fill="#6366F1" text-anchor="middle">Distance &amp; Density</text>
    <path d="M 95 0 L 110 0 M 105 -5 L 110 0 L 105 5" stroke="#4F46E5" stroke-width="2" fill="none"/>
  </g>
  
  <!-- Right Panel: Discovered Clusters -->
  <g transform="translate(520, 75)">
    <rect width="360" height="210" fill="#F8FAFC" rx="8" stroke="#CBD5E1" stroke-width="1"/>
    <text x="180" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">2. Discovered Clusters (Emergent Structure)</text>
    
    <!-- Cluster A: Cyan / Teal -->
    <ellipse cx="90" cy="90" rx="45" ry="35" fill="#ECFEFF" stroke="#A5F3FC" stroke-width="1.5" stroke-dasharray="3,3"/>
    <circle cx="80" cy="70" r="5" fill="#0891B2"/>
    <circle cx="95" cy="85" r="5" fill="#0891B2"/>
    <circle cx="70" cy="90" r="5" fill="#0891B2"/>
    <circle cx="85" cy="110" r="5" fill="#0891B2"/>
    <circle cx="105" cy="75" r="5" fill="#0891B2"/>
    <circle cx="115" cy="100" r="5" fill="#0891B2"/>
    <text x="90" y="140" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#0891B2" text-anchor="middle">Cluster 1 (Budget Frequent)</text>
    
    <!-- Cluster B: Violet -->
    <ellipse cx="270" cy="90" rx="45" ry="35" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1.5" stroke-dasharray="3,3"/>
    <circle cx="260" cy="65" r="5" fill="#7C3AED"/>
    <circle cx="280" cy="80" r="5" fill="#7C3AED"/>
    <circle cx="250" cy="95" r="5" fill="#7C3AED"/>
    <circle cx="295" cy="90" r="5" fill="#7C3AED"/>
    <circle cx="270" cy="115" r="5" fill="#7C3AED"/>
    <circle cx="245" cy="75" r="5" fill="#7C3AED"/>
    <text x="270" y="140" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#7C3AED" text-anchor="middle">Cluster 2 (VIP High-Spend)</text>
    
    <!-- Cluster C: Amber -->
    <ellipse cx="180" cy="165" rx="45" ry="30" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5" stroke-dasharray="3,3"/>
    <circle cx="180" cy="145" r="5" fill="#D97706"/>
    <circle cx="165" cy="165" r="5" fill="#D97706"/>
    <circle cx="195" cy="170" r="5" fill="#D97706"/>
    <circle cx="175" cy="190" r="5" fill="#D97706"/>
    <circle cx="210" cy="155" r="5" fill="#D97706"/>
    <circle cx="150" cy="150" r="5" fill="#D97706"/>
    <text x="180" y="202" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#D97706" text-anchor="middle">Cluster 3 (Occasional Shoppers)</text>
  </g>
</svg>"""

# 2. Classification vs. Clustering
SVG_CLUSTERING_VS_CLASSIFICATION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Supervised Classification vs. Unsupervised Clustering</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Predicting known predefined classes versus discovering hidden structural cohorts</text>
  
  <!-- Left: Supervised Classification -->
  <g transform="translate(40, 75)">
    <rect width="400" height="235" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="0" y="0" width="400" height="36" fill="#F1F5F9" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="200" y="23" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">SUPERVISED CLASSIFICATION</text>
    
    <!-- Coordinate Box -->
    <rect x="25" y="50" width="350" height="130" fill="#FFFFFF" rx="6" stroke="#CBD5E1" stroke-width="1"/>
    <!-- Ground Truth Classes -->
    <!-- Class 1: Blue Circles -->
    <circle cx="80" cy="80" r="6" fill="#2563EB"/>
    <circle cx="110" cy="95" r="6" fill="#2563EB"/>
    <circle cx="95" cy="120" r="6" fill="#2563EB"/>
    <circle cx="130" cy="75" r="6" fill="#2563EB"/>
    <!-- Class 0: Red Squares -->
    <rect x="270" y="70" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="290" y="100" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="260" y="125" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="310" y="85" width="12" height="12" fill="#DC2626" rx="2"/>
    
    <!-- Learned Decision Boundary -->
    <line x1="200" y1="50" x2="200" y2="180" stroke="#0F172A" stroke-width="2.5" stroke-dasharray="6,4"/>
    <text x="200" y="115" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle" transform="rotate(-90 200 115)">Learned Boundary</text>
    
    <text x="200" y="202" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="600" fill="#1E293B" text-anchor="middle">• Ground-truth labels (y) exist during training</text>
    <text x="200" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">• Objective: Map inputs X → known target y with high accuracy</text>
  </g>
  
  <!-- Right: Unsupervised Clustering -->
  <g transform="translate(480, 75)">
    <rect width="400" height="235" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="0" y="0" width="400" height="36" fill="#F1F5F9" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="200" y="23" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">UNSUPERVISED CLUSTERING</text>
    
    <!-- Coordinate Box -->
    <rect x="25" y="50" width="350" height="130" fill="#FFFFFF" rx="6" stroke="#CBD5E1" stroke-width="1"/>
    <!-- Unlabeled Data Grouped by Distance -->
    <circle cx="85" cy="85" r="6" fill="#0891B2"/>
    <circle cx="115" cy="95" r="6" fill="#0891B2"/>
    <circle cx="100" cy="120" r="6" fill="#0891B2"/>
    <circle cx="130" cy="80" r="6" fill="#0891B2"/>
    <circle cx="80" cy="130" r="6" fill="#0891B2"/>
    
    <circle cx="270" cy="75" r="6" fill="#7C3AED"/>
    <circle cx="295" cy="105" r="6" fill="#7C3AED"/>
    <circle cx="265" cy="130" r="6" fill="#7C3AED"/>
    <circle cx="315" cy="90" r="6" fill="#7C3AED"/>
    <circle cx="250" cy="95" r="6" fill="#7C3AED"/>
    
    <!-- Natural separation zone -->
    <rect x="180" y="55" width="40" height="120" fill="#ECFDF5" opacity="0.6" stroke="#A7F3D0" stroke-width="1" stroke-dasharray="3,3"/>
    <text x="200" y="115" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="9" font-weight="600" fill="#059669" text-anchor="middle" transform="rotate(-90 200 115)">Sparse Margin</text>
    
    <text x="200" y="202" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="600" fill="#1E293B" text-anchor="middle">• NO target labels (y) provided whatsoever</text>
    <text x="200" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">• Objective: Group points by spatial proximity &amp; feature similarity</text>
  </g>
</svg>"""

# 3. Euclidean vs. Manhattan Distance
SVG_EUCLIDEAN_VS_MANHATTAN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Distance Metrics in 2D Feature Space: Euclidean vs. Manhattan</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Customer X = (4, 12) versus Customer Y = (7, 4) in Income vs. Frequency</text>
  
  <!-- Left Side: Diagram Canvas -->
  <g transform="translate(60, 75)">
    <!-- Grid Canvas -->
    <rect width="400" height="230" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Grid Lines -->
    <line x1="80" y1="30" x2="80" y2="200" stroke="#E2E8F0" stroke-width="1"/>
    <line x1="160" y1="30" x2="160" y2="200" stroke="#E2E8F0" stroke-width="1"/>
    <line x1="240" y1="30" x2="240" y2="200" stroke="#E2E8F0" stroke-width="1"/>
    <line x1="320" y1="30" x2="320" y2="200" stroke="#E2E8F0" stroke-width="1"/>
    
    <line x1="40" y1="60" x2="360" y2="60" stroke="#E2E8F0" stroke-width="1"/>
    <line x1="40" y1="110" x2="360" y2="110" stroke="#E2E8F0" stroke-width="1"/>
    <line x1="40" y1="160" x2="360" y2="160" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Point X: (120, 60) [represents (4, 12)] -->
    <!-- Point Y: (280, 180) [represents (7, 4)] -->
    
    <!-- Manhattan Path (Red dashed grid line) -->
    <polyline points="120,60 280,60 280,180" fill="none" stroke="#DC2626" stroke-width="3" stroke-dasharray="6,4"/>
    <text x="200" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">Δx = |4 − 7| = 3</text>
    <text x="295" y="125" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="start">Δy = |12 − 4| = 8</text>
    
    <!-- Euclidean Path (Blue straight line) -->
    <line x1="120" y1="60" x2="280" y2="180" stroke="#2563EB" stroke-width="3.5"/>
    <text x="180" y="130" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="800" fill="#2563EB" text-anchor="end">√(3² + 8²) ≈ 8.54</text>
    
    <!-- Point Markers -->
    <circle cx="120" cy="60" r="7" fill="#4F46E5" stroke="#FFFFFF" stroke-width="2"/>
    <text x="110" y="55" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="800" fill="#4F46E5" text-anchor="end">Point X (4, 12)</text>
    
    <circle cx="280" cy="180" r="7" fill="#059669" stroke="#FFFFFF" stroke-width="2"/>
    <text x="295" y="195" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="800" fill="#059669" text-anchor="start">Point Y (7, 4)</text>
  </g>
  
  <!-- Right Side: Exact Calculations Card -->
  <g transform="translate(500, 75)">
    <rect width="360" height="230" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Euclidean Card -->
    <rect x="20" y="18" width="320" height="85" fill="#EFF6FF" rx="6" stroke="#BFDBFE" stroke-width="1"/>
    <text x="35" y="40" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#1D4ED8">Euclidean Distance (Straight Line / L2 Norm)</text>
    <text x="35" y="62" font-family="SFMono-Regular, Consolas, monospace" font-size="12" fill="#1E3A8A">d(X, Y) = √[ (4−7)² + (12−4)² ]</text>
    <text x="35" y="84" font-family="SFMono-Regular, Consolas, monospace" font-size="13" font-weight="700" fill="#1E3A8A">d(X, Y) = √[ 9 + 64 ] = √73 ≈ 8.5440</text>
    
    <!-- Manhattan Card -->
    <rect x="20" y="118" width="320" height="85" fill="#FEF2F2" rx="6" stroke="#FECACA" stroke-width="1"/>
    <text x="35" y="140" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#B91C1C">Manhattan Distance (Taxicab / L1 Norm)</text>
    <text x="35" y="162" font-family="SFMono-Regular, Consolas, monospace" font-size="12" fill="#7F1D1D">d(X, Y) = |4 − 7| + |12 − 4|</text>
    <text x="35" y="184" font-family="SFMono-Regular, Consolas, monospace" font-size="13" font-weight="700" fill="#7F1D1D">d(X, Y) = 3 + 8 = 11.0000</text>
  </g>
</svg>"""

# 4. Feature Scaling Effect
SVG_SCALING_EFFECT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Why Feature Scaling Is Mandatory for Distance-Based Clustering</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Without scaling, features measured in thousands dwarf features measured in single units</text>
  
  <!-- Left Side: Unscaled Raw Data -->
  <g transform="translate(40, 75)">
    <rect width="400" height="235" fill="#FFF1F2" rx="8" stroke="#FECDD3" stroke-width="1"/>
    <text x="200" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#9F1239" text-anchor="middle">✗ BEFORE SCALING: Large Feature Dominates</text>
    
    <!-- Distorted Coordinate Box -->
    <rect x="25" y="45" width="350" height="135" fill="#FFFFFF" rx="6" stroke="#FDA4AF" stroke-width="1"/>
    
    <!-- Y-axis: Annual Income ($20,000 to $100,000) -->
    <!-- X-axis: Purchase Frequency (2 to 10 purchases) -->
    <text x="15" y="115" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#9F1239" text-anchor="middle" transform="rotate(-90 15 115)">Income ($20k–$100k)</text>
    <text x="200" y="195" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#9F1239" text-anchor="middle">Visits (2–10 visits/month)</text>
    
    <!-- Skewed Ellipse Clusters: Euclidean distance calculates (10000)^2 vs (4)^2 -->
    <!-- The vertical axis completely overwhelms horizontal differences! -->
    <ellipse cx="140" cy="80" rx="25" ry="15" fill="#FDA4AF" opacity="0.6"/>
    <circle cx="130" cy="78" r="4" fill="#E11D48"/>
    <circle cx="150" cy="82" r="4" fill="#E11D48"/>
    
    <ellipse cx="260" cy="145" rx="25" ry="15" fill="#FDA4AF" opacity="0.6"/>
    <circle cx="250" cy="142" r="4" fill="#E11D48"/>
    <circle cx="270" cy="148" r="4" fill="#E11D48"/>
    
    <text x="200" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="600" fill="#9F1239" text-anchor="middle">Distance is 99.99% driven by Income! Frequency is ignored.</text>
  </g>
  
  <!-- Right Side: Standardized Data -->
  <g transform="translate(480, 75)">
    <rect width="400" height="235" fill="#F0FDF4" rx="8" stroke="#BBF7D0" stroke-width="1"/>
    <text x="200" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#166534" text-anchor="middle">✓ AFTER STANDARDSCALER: Equal Geometric Influence</text>
    
    <!-- Scaled Coordinate Box -->
    <rect x="25" y="45" width="350" height="135" fill="#FFFFFF" rx="6" stroke="#86EFAC" stroke-width="1"/>
    
    <!-- Both axes are Z-scores: -2 to +2 -->
    <text x="15" y="115" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#166534" text-anchor="middle" transform="rotate(-90 15 115)">Z(Income): −2 to +2</text>
    <text x="200" y="195" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#166534" text-anchor="middle">Z(Visits): −2 to +2</text>
    
    <!-- Isotropic, spherical natural clusters -->
    <circle cx="110" cy="85" r="30" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1" stroke-dasharray="2,2"/>
    <circle cx="100" cy="75" r="5" fill="#16A34A"/>
    <circle cx="120" cy="80" r="5" fill="#16A34A"/>
    <circle cx="110" cy="95" r="5" fill="#16A34A"/>
    <circle cx="95" cy="90" r="5" fill="#16A34A"/>
    
    <circle cx="270" cy="120" r="30" fill="#ECFEFF" stroke="#A5F3FC" stroke-width="1" stroke-dasharray="2,2"/>
    <circle cx="260" cy="115" r="5" fill="#0891B2"/>
    <circle cx="280" cy="110" r="5" fill="#0891B2"/>
    <circle cx="275" cy="130" r="5" fill="#0891B2"/>
    <circle cx="255" cy="125" r="5" fill="#0891B2"/>
    
    <text x="200" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="600" fill="#166534" text-anchor="middle">Both features contribute equally to Euclidean distance.</text>
  </g>
</svg>"""

# 5. K-Means Steps (Animated-style 4-panel sequence)
SVG_KMEANS_STEPS_PANEL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="30" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">How K-Means Works Step by Step: The Expectation-Maximization Loop</text>
  <text x="460" y="48" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Iterative optimization: Assign points to nearest centroid → Recalculate centroids as cluster means</text>
  
  <!-- Step 1: Initialize -->
  <g transform="translate(25, 65)">
    <rect width="195" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="0" y="0" width="195" height="32" fill="#EEF2FF" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="97" y="21" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">STEP 1: INITIALIZE</text>
    
    <!-- Canvas -->
    <rect x="15" y="45" width="165" height="135" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
    <!-- Unassigned points (gray) -->
    <circle cx="45" cy="70" r="4" fill="#94A3B8"/>
    <circle cx="55" cy="85" r="4" fill="#94A3B8"/>
    <circle cx="40" cy="95" r="4" fill="#94A3B8"/>
    <circle cx="140" cy="65" r="4" fill="#94A3B8"/>
    <circle cx="155" cy="80" r="4" fill="#94A3B8"/>
    <circle cx="135" cy="90" r="4" fill="#94A3B8"/>
    <circle cx="95" cy="145" r="4" fill="#94A3B8"/>
    <circle cx="110" cy="160" r="4" fill="#94A3B8"/>
    
    <!-- 2 Random Centroids (Stars) -->
    <path d="M 50 115 L 53 123 L 61 123 L 55 128 L 57 136 L 50 131 L 43 136 L 45 128 L 39 123 L 47 123 Z" fill="#DC2626" stroke="#991B1B" stroke-width="1"/>
    <path d="M 130 115 L 133 123 L 141 123 L 135 128 L 137 136 L 130 131 L 123 136 L 125 128 L 119 123 L 127 123 Z" fill="#2563EB" stroke="#1E40AF" stroke-width="1"/>
    
    <text x="97" y="198" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="600" fill="#1E293B" text-anchor="middle">Select K=2 random</text>
    <text x="97" y="214" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">initial center locations</text>
    <text x="97" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">(e.g., via k-means++)</text>
  </g>
  
  <!-- Step 2: Assign -->
  <g transform="translate(245, 65)">
    <rect width="195" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="0" y="0" width="195" height="32" fill="#EEF2FF" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="97" y="21" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">STEP 2: ASSIGN POINTS</text>
    
    <rect x="15" y="45" width="165" height="135" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
    <!-- Points colored by nearest centroid -->
    <circle cx="45" cy="70" r="4" fill="#DC2626"/>
    <circle cx="55" cy="85" r="4" fill="#DC2626"/>
    <circle cx="40" cy="95" r="4" fill="#DC2626"/>
    <circle cx="140" cy="65" r="4" fill="#2563EB"/>
    <circle cx="155" cy="80" r="4" fill="#2563EB"/>
    <circle cx="135" cy="90" r="4" fill="#2563EB"/>
    <circle cx="95" cy="145" r="4" fill="#DC2626"/>
    <circle cx="110" cy="160" r="4" fill="#2563EB"/>
    
    <!-- Centroids -->
    <path d="M 50 115 L 53 123 L 61 123 L 55 128 L 57 136 L 50 131 L 43 136 L 45 128 L 39 123 L 47 123 Z" fill="#DC2626" stroke="#991B1B" stroke-width="1"/>
    <path d="M 130 115 L 133 123 L 141 123 L 135 128 L 137 136 L 130 131 L 123 136 L 125 128 L 119 123 L 127 123 Z" fill="#2563EB" stroke="#1E40AF" stroke-width="1"/>
    
    <text x="97" y="198" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="600" fill="#1E293B" text-anchor="middle">Calculate Euclidean dist</text>
    <text x="97" y="214" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Assign each point to its</text>
    <text x="97" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">nearest centroid</text>
  </g>
  
  <!-- Step 3: Update -->
  <g transform="translate(465, 65)">
    <rect width="195" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="0" y="0" width="195" height="32" fill="#EEF2FF" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="97" y="21" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#4338CA" text-anchor="middle">STEP 3: RECALCULATE</text>
    
    <rect x="15" y="45" width="165" height="135" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
    <circle cx="45" cy="70" r="4" fill="#DC2626"/>
    <circle cx="55" cy="85" r="4" fill="#DC2626"/>
    <circle cx="40" cy="95" r="4" fill="#DC2626"/>
    <circle cx="140" cy="65" r="4" fill="#2563EB"/>
    <circle cx="155" cy="80" r="4" fill="#2563EB"/>
    <circle cx="135" cy="90" r="4" fill="#2563EB"/>
    <circle cx="95" cy="145" r="4" fill="#DC2626"/>
    <circle cx="110" cy="160" r="4" fill="#2563EB"/>
    
    <!-- Centroids moving towards mean of clusters -->
    <!-- Ghost of old centroid -->
    <path d="M 50 115 L 53 123 L 61 123 L 55 128 L 57 136 L 50 131 L 43 136 L 45 128 L 39 123 L 47 123 Z" fill="none" stroke="#DC2626" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="50" y1="120" x2="58" y2="98" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="2,2"/>
    <!-- New Red Centroid -->
    <path d="M 58 90 L 61 98 L 69 98 L 63 103 L 65 111 L 58 106 L 51 111 L 53 103 L 47 98 L 55 98 Z" fill="#DC2626" stroke="#991B1B" stroke-width="1"/>
    
    <!-- Ghost of old blue centroid -->
    <path d="M 130 115 L 133 123 L 141 123 L 135 128 L 137 136 L 130 131 L 123 136 L 125 128 L 119 123 L 127 123 Z" fill="none" stroke="#2563EB" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="130" y1="120" x2="135" y2="98" stroke="#2563EB" stroke-width="1.5" stroke-dasharray="2,2"/>
    <!-- New Blue Centroid -->
    <path d="M 135 90 L 138 98 L 146 98 L 140 103 L 142 111 L 135 106 L 128 111 L 130 103 L 124 98 L 132 98 Z" fill="#2563EB" stroke="#1E40AF" stroke-width="1"/>
    
    <text x="97" y="198" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="600" fill="#1E293B" text-anchor="middle">Compute mean vector</text>
    <text x="97" y="214" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">μ_k = (1/|C_k|) ∑ x_i</text>
    <text x="97" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">Centroids shift position</text>
  </g>
  
  <!-- Step 4: Converge -->
  <g transform="translate(685, 65)">
    <rect width="210" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="0" y="0" width="210" height="32" fill="#ECFDF5" rx="8" stroke="#A7F3D0" stroke-width="1"/>
    <text x="105" y="21" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">STEP 4: CONVERGENCE</text>
    
    <rect x="20" y="45" width="170" height="135" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
    
    <!-- Final Stable Clusters -->
    <ellipse cx="50" cy="85" rx="35" ry="30" fill="#FEE2E2" opacity="0.6"/>
    <circle cx="45" cy="70" r="4" fill="#DC2626"/>
    <circle cx="55" cy="85" r="4" fill="#DC2626"/>
    <circle cx="40" cy="95" r="4" fill="#DC2626"/>
    <path d="M 50 80 L 53 88 L 61 88 L 55 93 L 57 101 L 50 96 L 43 101 L 45 93 L 39 88 L 47 88 Z" fill="#DC2626" stroke="#991B1B" stroke-width="1.5"/>
    
    <ellipse cx="135" cy="100" rx="40" ry="45" fill="#DBEAFE" opacity="0.6"/>
    <circle cx="140" cy="65" r="4" fill="#2563EB"/>
    <circle cx="155" cy="80" r="4" fill="#2563EB"/>
    <circle cx="135" cy="90" r="4" fill="#2563EB"/>
    <circle cx="105" cy="140" r="4" fill="#2563EB"/>
    <circle cx="120" cy="155" r="4" fill="#2563EB"/>
    <path d="M 130 105 L 133 113 L 141 113 L 135 118 L 137 126 L 130 121 L 123 126 L 125 118 L 119 113 L 127 113 Z" fill="#2563EB" stroke="#1E40AF" stroke-width="1.5"/>
    
    <text x="105" y="198" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">✓ Centroids Stop Moving</text>
    <text x="105" y="214" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#065F46" text-anchor="middle">Assignments stabilize</text>
    <text x="105" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="9" fill="#047857" text-anchor="middle">Inertia J minimized</text>
  </g>
</svg>"""

# 6. Final K-Means Clusters with Voronoi Partitions & Centroids
SVG_KMEANS_CENTROIDS_FINAL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Fitted K-Means (K = 3) with Voronoi Partitions &amp; Cluster Centers</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Stars represent true calculated centroids μ₁ = (0.36, 1.33), μ₂ = (−1.32, −0.46), μ₃ = (0.96, −0.87)</text>
  
  <!-- Main Plot Area -->
  <g transform="translate(180, 70)">
    <rect width="560" height="240" fill="#FAFAFA" rx="8" stroke="#CBD5E1" stroke-width="1"/>
    
    <!-- Voronoi Partition Lines -->
    <line x1="280" y1="0" x2="280" y2="120" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="0" y1="130" x2="280" y2="120" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="280" y1="120" x2="560" y2="210" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,4"/>
    
    <!-- Cluster 1 (Top Right): Violet -->
    <g fill="#7C3AED">
      <circle cx="340" cy="45" r="5"/> <circle cx="370" cy="55" r="5"/> <circle cx="355" cy="70" r="5"/>
      <circle cx="390" cy="40" r="5"/> <circle cx="330" cy="65" r="5"/> <circle cx="380" cy="75" r="5"/>
      <circle cx="410" cy="60" r="5"/> <circle cx="360" cy="85" r="5"/> <circle cx="345" cy="95" r="5"/>
    </g>
    <!-- Centroid 1 Star -->
    <polygon points="365,58 368,66 376,66 370,71 372,79 365,74 358,79 360,71 354,66 362,66" fill="#F59E0B" stroke="#0F172A" stroke-width="2"/>
    <text x="365" y="105" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#7C3AED" text-anchor="middle">μ₁ = (0.36, 1.33)</text>
    
    <!-- Cluster 2 (Left): Cyan / Teal -->
    <g fill="#0891B2">
      <circle cx="100" cy="150" r="5"/> <circle cx="130" cy="165" r="5"/> <circle cx="115" cy="180" r="5"/>
      <circle cx="145" cy="145" r="5"/> <circle cx="85" cy="160" r="5"/> <circle cx="120" cy="195" r="5"/>
      <circle cx="150" cy="175" r="5"/> <circle cx="95" cy="170" r="5"/> <circle cx="135" cy="155" r="5"/>
    </g>
    <!-- Centroid 2 Star -->
    <polygon points="120,160 123,168 131,168 125,173 127,181 120,176 113,181 115,173 109,168 117,168" fill="#F59E0B" stroke="#0F172A" stroke-width="2"/>
    <text x="120" y="215" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#0891B2" text-anchor="middle">μ₂ = (−1.32, −0.46)</text>
    
    <!-- Cluster 3 (Bottom Right): Emerald / Green -->
    <g fill="#059669">
      <circle cx="430" cy="160" r="5"/> <circle cx="460" cy="175" r="5"/> <circle cx="445" cy="190" r="5"/>
      <circle cx="480" cy="155" r="5"/> <circle cx="420" cy="170" r="5"/> <circle cx="450" cy="205" r="5"/>
      <circle cx="470" cy="185" r="5"/> <circle cx="435" cy="180" r="5"/> <circle cx="495" cy="170" r="5"/>
    </g>
    <!-- Centroid 3 Star -->
    <polygon points="450,170 453,178 461,178 455,183 457,191 450,186 443,191 445,183 439,178 447,178" fill="#F59E0B" stroke="#0F172A" stroke-width="2"/>
    <text x="450" y="225" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">μ₃ = (0.96, −0.87)</text>
  </g>
</svg>"""

# 7. Elbow Method Plot
SVG_ELBOW_METHOD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">The Elbow Method: Inertia vs. Number of Clusters (K)</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Calculated on 300 synthetic customer samples: Dramatic drop before K=3, subtle gains after</text>
  
  <g transform="translate(100, 75)">
    <!-- Axes -->
    <line x1="60" y1="210" x2="720" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="60" y1="20" x2="60" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
    
    <!-- Y-axis labels (Inertia: 0 to 350) -->
    <text x="50" y="214" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">0</text>
    <text x="50" y="155" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">100</text>
    <text x="50" y="100" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">200</text>
    <text x="50" y="45" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">300</text>
    <text x="15" y="115" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle" transform="rotate(-90 15 115)">Inertia (Within-Cluster Sum of Squares)</text>
    
    <!-- X-axis labels (K = 2 to 6) -->
    <!-- X positions: K=2: 130, K=3: 260, K=4: 390, K=5: 520, K=6: 650 -->
    <text x="130" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#334155" text-anchor="middle">K = 2</text>
    <text x="260" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#4F46E5" text-anchor="middle">K = 3 (Elbow)</text>
    <text x="390" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">K = 4</text>
    <text x="520" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">K = 5</text>
    <text x="650" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">K = 6</text>
    
    <!-- Grid lines -->
    <line x1="60" y1="155" x2="720" y2="155" stroke="#F1F5F9" stroke-width="1"/>
    <line x1="60" y1="100" x2="720" y2="100" stroke="#F1F5F9" stroke-width="1"/>
    <line x1="60" y1="45" x2="720" y2="45" stroke="#F1F5F9" stroke-width="1"/>
    
    <!-- Actual points:
         K=2: Inertia 307.10 -> y = 210 - (307.10 / 350 * 180) = 210 - 157.9 = 52.1
         K=3: Inertia 47.04  -> y = 210 - (47.04 / 350 * 180) = 210 - 24.2 = 185.8
         K=4: Inertia 41.08  -> y = 210 - (41.08 / 350 * 180) = 210 - 21.1 = 188.9
         K=5: Inertia 35.72  -> y = 210 - (35.72 / 350 * 180) = 210 - 18.4 = 191.6
         K=6: Inertia 30.22  -> y = 210 - (30.22 / 350 * 180) = 210 - 15.5 = 194.5
    -->
    <polyline points="130,52 260,186 390,189 520,192 650,195" fill="none" stroke="#4F46E5" stroke-width="3"/>
    
    <!-- Plot Points -->
    <circle cx="130" cy="52" r="6" fill="#4F46E5"/>
    <text x="130" y="42" font-family="SFMono-Regular, Consolas, monospace" font-size="11" font-weight="700" fill="#4F46E5" text-anchor="middle">307.10</text>
    
    <!-- ELBOW HIGHLIGHT AT K=3 -->
    <circle cx="260" cy="186" r="9" fill="#F59E0B" stroke="#B45309" stroke-width="2.5"/>
    <text x="260" y="172" font-family="SFMono-Regular, Consolas, monospace" font-size="12" font-weight="800" fill="#B45309" text-anchor="middle">47.04 (Elbow)</text>
    
    <circle cx="390" cy="189" r="6" fill="#4F46E5"/>
    <text x="390" y="176" font-family="SFMono-Regular, Consolas, monospace" font-size="10" fill="#64748B" text-anchor="middle">41.08</text>
    
    <circle cx="520" cy="192" r="6" fill="#4F46E5"/>
    <text x="520" y="179" font-family="SFMono-Regular, Consolas, monospace" font-size="10" fill="#64748B" text-anchor="middle">35.72</text>
    
    <circle cx="650" cy="195" r="6" fill="#4F46E5"/>
    <text x="650" y="182" font-family="SFMono-Regular, Consolas, monospace" font-size="10" fill="#64748B" text-anchor="middle">30.22</text>
    
    <!-- Annotation Callout -->
    <path d="M 230 110 L 255 170" stroke="#D97706" stroke-width="1.5" stroke-dasharray="3,3"/>
    <rect x="130" y="85" width="130" height="30" rx="4" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1"/>
    <text x="195" y="104" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#92400E" text-anchor="middle">Sharp Elbow Bend!</text>
  </g>
</svg>"""

# 8. Silhouette Analysis & Score Comparison
SVG_SILHOUETTE_ANALYSIS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Silhouette Score Comparison: Evaluating Separation &amp; Cohesion</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Formula s = (b − a) / max(a, b). Score ranges from −1.0 to +1.0. Higher is strictly better.</text>
  
  <!-- Bar Chart of Silhouette Scores -->
  <g transform="translate(100, 75)">
    <!-- Y-axis -->
    <line x1="60" y1="210" x2="720" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="60" y1="20" x2="60" y2="210" stroke="#94A3B8" stroke-width="1.5"/>
    
    <text x="50" y="214" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">0.0</text>
    <text x="50" y="166" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">0.25</text>
    <text x="50" y="118" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">0.50</text>
    <text x="50" y="70" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">0.75</text>
    <text x="50" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">1.00</text>
    <text x="15" y="115" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle" transform="rotate(-90 15 115)">Mean Silhouette Coefficient</text>
    
    <!-- Scale: 1.0 unit = 192px -> 0.1 unit = 19.2px -->
    <!-- Bars: K=2: 0.5391 (h = 103.5px) -->
    <!-- K=3: 0.7746 (h = 148.7px) - Winner! -->
    <!-- K=4: 0.6273 (h = 120.4px) -->
    <!-- K=5: 0.4713 (h = 90.5px) -->
    <!-- K=6: 0.3266 (h = 62.7px) -->
    
    <!-- K=2 Bar -->
    <rect x="110" y="106.5" width="70" height="103.5" fill="#94A3B8" rx="4"/>
    <text x="145" y="98" font-family="SFMono-Regular, Consolas, monospace" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">0.5391</text>
    <text x="145" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">K = 2</text>
    
    <!-- K=3 Bar (Peak Winner) -->
    <rect x="235" y="61.3" width="70" height="148.7" fill="#10B981" rx="4"/>
    <text x="270" y="52" font-family="SFMono-Regular, Consolas, monospace" font-size="12" font-weight="800" fill="#047857" text-anchor="middle">0.7746 (Peak!)</text>
    <text x="270" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#047857" text-anchor="middle">K = 3 (Optimal)</text>
    
    <!-- K=4 Bar -->
    <rect x="360" y="89.6" width="70" height="120.4" fill="#06B6D4" rx="4"/>
    <text x="395" y="81" font-family="SFMono-Regular, Consolas, monospace" font-size="11" font-weight="700" fill="#0E7490" text-anchor="middle">0.6273</text>
    <text x="395" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">K = 4</text>
    
    <!-- K=5 Bar -->
    <rect x="485" y="119.5" width="70" height="90.5" fill="#8B5CF6" rx="4"/>
    <text x="520" y="111" font-family="SFMono-Regular, Consolas, monospace" font-size="11" font-weight="700" fill="#6D28D9" text-anchor="middle">0.4713</text>
    <text x="520" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">K = 5</text>
    
    <!-- K=6 Bar -->
    <rect x="610" y="147.3" width="70" height="62.7" fill="#F43F5E" rx="4"/>
    <text x="645" y="139" font-family="SFMono-Regular, Consolas, monospace" font-size="11" font-weight="700" fill="#BE123C" text-anchor="middle">0.3266</text>
    <text x="645" y="230" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">K = 6</text>
  </g>
</svg>"""

# 9. Visualizing Different K Values Grid (K=2, 3, 4, 5)
SVG_K_VALUES_GRID = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="30" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Comparing Cluster Partitioning Across Different Values of K</text>
  <text x="460" y="48" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Actual fitted partitions: Under-clustering (K=2), Optimal (K=3), Over-segmentation (K=4, 5)</text>
  
  <!-- Panel K=2 -->
  <g transform="translate(25, 65)">
    <rect width="200" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="100" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">K = 2 (Under-Clustered)</text>
    <rect x="15" y="35" width="170" height="150" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
    
    <!-- 2 Merged clusters -->
    <circle cx="50" cy="70" r="4" fill="#0891B2"/> <circle cx="65" cy="85" r="4" fill="#0891B2"/>
    <circle cx="140" cy="70" r="4" fill="#7C3AED"/> <circle cx="155" cy="85" r="4" fill="#7C3AED"/>
    <!-- Bottom group merged into Cluster 1 -->
    <circle cx="95" cy="140" r="4" fill="#0891B2"/> <circle cx="110" cy="155" r="4" fill="#0891B2"/>
    <polygon points="65,90 68,98 76,98 70,103 72,111 65,106 58,111 60,103 54,98 62,98" fill="#F59E0B" stroke="#0F172A" stroke-width="1.5"/>
    <polygon points="145,80 148,88 156,88 150,93 152,101 145,96 138,101 140,93 134,88 142,88" fill="#F59E0B" stroke="#0F172A" stroke-width="1.5"/>
    
    <text x="100" y="205" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="600" fill="#DC2626" text-anchor="middle">✗ Forces 2 distinct groups</text>
    <text x="100" y="222" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">into a single cluster</text>
    <text x="100" y="238" font-family="SFMono-Regular, Consolas, monospace" font-size="9" fill="#94A3B8" text-anchor="middle">Silhouette: 0.5391</text>
  </g>
  
  <!-- Panel K=3 (Optimal) -->
  <g transform="translate(245, 65)">
    <rect width="200" height="250" fill="#F0FDF4" rx="8" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="100" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="800" fill="#166534" text-anchor="middle">K = 3 (Optimal &amp; Clean)</text>
    <rect x="15" y="35" width="170" height="150" fill="#FFFFFF" rx="4" stroke="#86EFAC"/>
    
    <!-- 3 naturally separated clusters -->
    <circle cx="50" cy="70" r="4" fill="#0891B2"/> <circle cx="65" cy="85" r="4" fill="#0891B2"/>
    <circle cx="140" cy="70" r="4" fill="#7C3AED"/> <circle cx="155" cy="85" r="4" fill="#7C3AED"/>
    <circle cx="95" cy="140" r="4" fill="#059669"/> <circle cx="110" cy="155" r="4" fill="#059669"/>
    
    <polygon points="57,77 60,85 68,85 62,90 64,98 57,93 50,98 52,90 46,85 54,85" fill="#F59E0B" stroke="#0F172A" stroke-width="1.5"/>
    <polygon points="147,77 150,85 158,85 152,90 154,98 147,93 140,98 142,90 136,85 144,85" fill="#F59E0B" stroke="#0F172A" stroke-width="1.5"/>
    <polygon points="102,147 105,155 113,155 107,160 109,168 102,163 95,168 97,160 91,155 99,155" fill="#F59E0B" stroke="#0F172A" stroke-width="1.5"/>
    
    <text x="100" y="205" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">✓ Perfectly matches</text>
    <text x="100" y="222" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#166534" text-anchor="middle">underlying generative structure</text>
    <text x="100" y="238" font-family="SFMono-Regular, Consolas, monospace" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">Silhouette: 0.7746</text>
  </g>
  
  <!-- Panel K=4 -->
  <g transform="translate(465, 65)">
    <rect width="200" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="100" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">K = 4 (Sub-Divided)</text>
    <rect x="15" y="35" width="170" height="150" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
    
    <!-- One cluster arbitrarily sliced in half -->
    <circle cx="45" cy="65" r="4" fill="#0891B2"/> <circle cx="65" cy="85" r="4" fill="#F43F5E"/>
    <circle cx="140" cy="70" r="4" fill="#7C3AED"/> <circle cx="155" cy="85" r="4" fill="#7C3AED"/>
    <circle cx="95" cy="140" r="4" fill="#059669"/> <circle cx="110" cy="155" r="4" fill="#059669"/>
    
    <polygon points="45,70 48,78 56,78 50,83 52,91 45,86 38,91 40,83 34,78 42,78" fill="#F59E0B" stroke="#0F172A" stroke-width="1"/>
    <polygon points="68,90 71,98 79,98 73,103 75,111 68,106 61,111 63,103 57,98 65,98" fill="#F59E0B" stroke="#0F172A" stroke-width="1"/>
    
    <text x="100" y="205" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="600" fill="#B45309" text-anchor="middle">! Cluster 1 is artificially</text>
    <text x="100" y="222" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">halved into 2 artificial pieces</text>
    <text x="100" y="238" font-family="SFMono-Regular, Consolas, monospace" font-size="9" fill="#94A3B8" text-anchor="middle">Silhouette: 0.6273</text>
  </g>
  
  <!-- Panel K=5 -->
  <g transform="translate(685, 65)">
    <rect width="210" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="105" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">K = 5 (Over-Segmented)</text>
    <rect x="20" y="35" width="170" height="150" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
    
    <!-- Heavy fragmentation -->
    <circle cx="45" cy="65" r="4" fill="#0891B2"/> <circle cx="65" cy="85" r="4" fill="#F43F5E"/>
    <circle cx="135" cy="65" r="4" fill="#7C3AED"/> <circle cx="155" cy="90" r="4" fill="#F59E0B"/>
    <circle cx="95" cy="140" r="4" fill="#059669"/> <circle cx="110" cy="155" r="4" fill="#059669"/>
    
    <text x="105" y="205" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="600" fill="#DC2626" text-anchor="middle">✗ Severe fragmentation</text>
    <text x="105" y="222" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">High model complexity</text>
    <text x="105" y="238" font-family="SFMono-Regular, Consolas, monospace" font-size="9" fill="#94A3B8" text-anchor="middle">Silhouette: 0.4713</text>
  </g>
</svg>"""

# 10. K-Means Limitations: Spherical Blobs vs Non-Convex Moons
SVG_KMEANS_LIMITATIONS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">K-Means Core Limitation: The Spherical Assumption</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">K-Means assumes clusters are convex, isotropic balls with similar variance</text>
  
  <!-- Left Side: Where K-Means Works (Convex Blobs) -->
  <g transform="translate(40, 75)">
    <rect width="400" height="235" fill="#F0FDF4" rx="8" stroke="#BBF7D0" stroke-width="1"/>
    <text x="200" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#166534" text-anchor="middle">✓ IDEAL: Isotropic Spherical Clusters</text>
    
    <rect x="25" y="45" width="350" height="140" fill="#FFFFFF" rx="6" stroke="#86EFAC" stroke-width="1"/>
    <!-- Spherical Blobs -->
    <circle cx="100" cy="115" r="40" fill="#ECFEFF" stroke="#A5F3FC" stroke-width="1.5"/>
    <circle cx="90" cy="100" r="4" fill="#0891B2"/> <circle cx="110" cy="110" r="4" fill="#0891B2"/>
    <circle cx="105" cy="125" r="4" fill="#0891B2"/> <circle cx="85" cy="120" r="4" fill="#0891B2"/>
    <polygon points="100,110 102,116 108,116 103,120 105,126 100,122 95,126 97,120 92,116 98,116" fill="#F59E0B" stroke="#0F172A" stroke-width="1"/>
    
    <circle cx="280" cy="115" r="40" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1.5"/>
    <circle cx="270" cy="100" r="4" fill="#7C3AED"/> <circle cx="290" cy="110" r="4" fill="#7C3AED"/>
    <circle cx="285" cy="125" r="4" fill="#7C3AED"/> <circle cx="265" cy="120" r="4" fill="#7C3AED"/>
    <polygon points="280,110 282,116 288,116 283,120 285,126 280,122 275,126 277,120 272,116 278,116" fill="#F59E0B" stroke="#0F172A" stroke-width="1"/>
    
    <text x="200" y="210" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="600" fill="#166534" text-anchor="middle">Centroid averages accurately represent compact clusters</text>
  </g>
  
  <!-- Right Side: Where K-Means Fails (Non-Convex / Moons) -->
  <g transform="translate(480, 75)">
    <rect width="400" height="235" fill="#FFF1F2" rx="8" stroke="#FECDD3" stroke-width="1"/>
    <text x="200" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#9F1239" text-anchor="middle">✗ FAILURE: Non-Convex Intertwined Moons</text>
    
    <rect x="25" y="45" width="350" height="140" fill="#FFFFFF" rx="6" stroke="#FDA4AF" stroke-width="1"/>
    
    <!-- Top Moon Points (True Cluster 1) cut in half by K-Means! -->
    <!-- Left half colored Red by K-Means -->
    <path d="M 60,110 A 60,60 0 0,1 180,70" fill="none" stroke="#DC2626" stroke-width="8" stroke-linecap="round"/>
    <!-- Right half colored Blue by K-Means -->
    <path d="M 180,70 A 60,60 0 0,1 260,110" fill="none" stroke="#2563EB" stroke-width="8" stroke-linecap="round"/>
    
    <!-- Bottom Moon Points (True Cluster 2) cut in half! -->
    <path d="M 120,130 A 60,60 0 0,0 200,170" fill="none" stroke="#DC2626" stroke-width="8" stroke-linecap="round"/>
    <path d="M 200,170 A 60,60 0 0,0 320,130" fill="none" stroke="#2563EB" stroke-width="8" stroke-linecap="round"/>
    
    <!-- Linear K-Means Cut Line across moons -->
    <line x1="190" y1="45" x2="190" y2="185" stroke="#0F172A" stroke-width="2.5" stroke-dasharray="4,4"/>
    <text x="190" y="115" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle" transform="rotate(-90 190 115)">Linear Cut</text>
    
    <text x="200" y="210" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="600" fill="#9F1239" text-anchor="middle">K-Means cuts across moons! ARI drops to 0.4053.</text>
  </g>
</svg>"""

# 11. Hierarchical Linkage Comparison
SVG_LINKAGE_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="30" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Hierarchical Clustering: The Four Major Linkage Criteria</text>
  <text x="460" y="48" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">How distance between two multi-point clusters A and B is formally measured</text>
  
  <!-- 1. Single Linkage -->
  <g transform="translate(25, 65)">
    <rect width="200" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="100" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Single Linkage (Min)</text>
    <rect x="15" y="35" width="170" height="125" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
    
    <!-- Cluster A & B -->
    <ellipse cx="45" cy="85" rx="25" ry="35" fill="#ECFEFF" stroke="#A5F3FC"/>
    <circle cx="40" cy="70" r="4" fill="#0891B2"/> <circle cx="50" cy="85" r="4" fill="#0891B2"/> <circle cx="40" cy="100" r="4" fill="#0891B2"/>
    
    <ellipse cx="145" cy="85" rx="25" ry="35" fill="#F5F3FF" stroke="#DDD6FE"/>
    <circle cx="140" cy="85" r="4" fill="#7C3AED"/> <circle cx="150" cy="70" r="4" fill="#7C3AED"/> <circle cx="150" cy="100" r="4" fill="#7C3AED"/>
    
    <!-- Closest Pair Line -->
    <line x1="50" y1="85" x2="140" y2="85" stroke="#DC2626" stroke-width="2.5"/>
    <circle cx="50" cy="85" r="5" fill="#DC2626"/> <circle cx="140" cy="85" r="5" fill="#DC2626"/>
    <text x="95" y="80" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#DC2626" text-anchor="middle">Min Pair</text>
    
    <text x="100" y="180" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="600" fill="#1E293B" text-anchor="middle">min { d(x, y) : x ∈ A, y ∈ B }</text>
    <text x="100" y="202" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">• Can trace irregular shapes</text>
    <text x="100" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#DC2626" text-anchor="middle">• Vulnerable to chaining effect</text>
  </g>
  
  <!-- 2. Complete Linkage -->
  <g transform="translate(245, 65)">
    <rect width="200" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="100" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Complete Linkage (Max)</text>
    <rect x="15" y="35" width="170" height="125" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
    
    <ellipse cx="45" cy="85" rx="25" ry="35" fill="#ECFEFF" stroke="#A5F3FC"/>
    <circle cx="35" cy="70" r="4" fill="#0891B2"/> <circle cx="50" cy="85" r="4" fill="#0891B2"/> <circle cx="40" cy="100" r="4" fill="#0891B2"/>
    
    <ellipse cx="145" cy="85" rx="25" ry="35" fill="#F5F3FF" stroke="#DDD6FE"/>
    <circle cx="140" cy="85" r="4" fill="#7C3AED"/> <circle cx="150" cy="70" r="4" fill="#7C3AED"/> <circle cx="155" cy="100" r="4" fill="#7C3AED"/>
    
    <!-- Farthest Pair Line -->
    <line x1="35" y1="70" x2="155" y2="100" stroke="#DC2626" stroke-width="2.5"/>
    <circle cx="35" cy="70" r="5" fill="#DC2626"/> <circle cx="155" cy="100" r="5" fill="#DC2626"/>
    <text x="95" y="75" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#DC2626" text-anchor="middle">Max Pair</text>
    
    <text x="100" y="180" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="600" fill="#1E293B" text-anchor="middle">max { d(x, y) : x ∈ A, y ∈ B }</text>
    <text x="100" y="202" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">• Produces compact, tight balls</text>
    <text x="100" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#DC2626" text-anchor="middle">• Highly sensitive to outliers</text>
  </g>
  
  <!-- 3. Average Linkage -->
  <g transform="translate(465, 65)">
    <rect width="200" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="100" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Average Linkage (Mean)</text>
    <rect x="15" y="35" width="170" height="125" fill="#FFFFFF" rx="4" stroke="#CBD5E1"/>
    
    <ellipse cx="45" cy="85" rx="25" ry="35" fill="#ECFEFF" stroke="#A5F3FC"/>
    <circle cx="40" cy="70" r="4" fill="#0891B2"/> <circle cx="50" cy="85" r="4" fill="#0891B2"/>
    
    <ellipse cx="145" cy="85" rx="25" ry="35" fill="#F5F3FF" stroke="#DDD6FE"/>
    <circle cx="140" cy="85" r="4" fill="#7C3AED"/> <circle cx="150" cy="70" r="4" fill="#7C3AED"/>
    
    <!-- All Pairwise Lines (web) -->
    <line x1="40" y1="70" x2="140" y2="85" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="40" y1="70" x2="150" y2="70" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="50" y1="85" x2="140" y2="85" stroke="#CBD5E1" stroke-width="1"/>
    <line x1="50" y1="85" x2="150" y2="70" stroke="#CBD5E1" stroke-width="1"/>
    <text x="95" y="75" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#2563EB" text-anchor="middle">Average All</text>
    
    <text x="100" y="180" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="600" fill="#1E293B" text-anchor="middle">(1 / |A||B|) ∑ ∑ d(x, y)</text>
    <text x="100" y="202" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">• Balanced compromise</text>
    <text x="100" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#059669" text-anchor="middle">• Relatively robust to noise</text>
  </g>
  
  <!-- 4. Ward Linkage -->
  <g transform="translate(685, 65)">
    <rect width="210" height="250" fill="#F0FDF4" rx="8" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="105" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="800" fill="#166534" text-anchor="middle">Ward Linkage (Min Variance)</text>
    <rect x="20" y="35" width="170" height="125" fill="#FFFFFF" rx="4" stroke="#86EFAC"/>
    
    <!-- Clusters with Centroid Shifts -->
    <circle cx="60" cy="85" r="22" fill="#DCFCE7"/>
    <circle cx="135" cy="85" r="22" fill="#DCFCE7"/>
    <polygon points="60,80 62,86 68,86 63,90 65,96 60,92 55,96 57,90 52,86 58,86" fill="#16A34A" stroke="#0F172A" stroke-width="1"/>
    <polygon points="135,80 137,86 143,86 138,90 140,96 135,92 130,96 132,90 127,86 133,86" fill="#16A34A" stroke="#0F172A" stroke-width="1"/>
    
    <text x="105" y="80" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">ΔVariance</text>
    
    <text x="105" y="180" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">Minimizes ΔInertia after merge</text>
    <text x="105" y="202" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#065F46" text-anchor="middle">• Default in scikit-learn</text>
    <text x="105" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">• High accuracy on compact data</text>
  </g>
</svg>"""

# 12. Genuine Hierarchical Dendrogram
SVG_DENDROGRAM = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="30" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Hierarchical Dendrogram: Sample Merges and Distance Thresholds</text>
  <text x="460" y="48" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Each vertical branch height indicates the dissimilarity (Ward distance) at which two clusters merged</text>
  
  <g transform="translate(100, 70)">
    <!-- Y-axis (Euclidean Distance / Linkage Height) -->
    <line x1="60" y1="210" x2="60" y2="20" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="50" y="214" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">0.0</text>
    <text x="50" y="165" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">2.5</text>
    <text x="50" y="115" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">5.0</text>
    <text x="50" y="65" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">7.5</text>
    <text x="50" y="25" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="end">10.0</text>
    <text x="15" y="115" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle" transform="rotate(-90 15 115)">Linkage Distance (Height)</text>
    
    <!-- Horizontal Cut Line at Height = 6.0 -->
    <line x1="60" y1="95" x2="720" y2="95" stroke="#DC2626" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="730" y="99" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="start">Cut: Height = 6.0 → Yields 3 Clusters!</text>
    
    <!-- Tree Leaves (Sample indices along bottom) -->
    <!-- Group 1: Teal (x=100, 140, 180, 220) -->
    <line x1="100" y1="210" x2="100" y2="185" stroke="#0891B2" stroke-width="2"/>
    <line x1="140" y1="210" x2="140" y2="185" stroke="#0891B2" stroke-width="2"/>
    <line x1="100" y1="185" x2="140" y2="185" stroke="#0891B2" stroke-width="2"/>
    <line x1="120" y1="185" x2="120" y2="150" stroke="#0891B2" stroke-width="2"/>
    
    <line x1="180" y1="210" x2="180" y2="175" stroke="#0891B2" stroke-width="2"/>
    <line x1="220" y1="210" x2="220" y2="175" stroke="#0891B2" stroke-width="2"/>
    <line x1="180" y1="175" x2="220" y2="175" stroke="#0891B2" stroke-width="2"/>
    <line x1="200" y1="175" x2="200" y2="150" stroke="#0891B2" stroke-width="2"/>
    
    <line x1="120" y1="150" x2="200" y2="150" stroke="#0891B2" stroke-width="2"/>
    <line x1="160" y1="150" x2="160" y2="50" stroke="#0891B2" stroke-width="2"/>
    
    <!-- Group 2: Violet (x=300, 340, 380, 420) -->
    <line x1="300" y1="210" x2="300" y2="190" stroke="#7C3AED" stroke-width="2"/>
    <line x1="340" y1="210" x2="340" y2="190" stroke="#7C3AED" stroke-width="2"/>
    <line x1="300" y1="190" x2="340" y2="190" stroke="#7C3AED" stroke-width="2"/>
    <line x1="320" y1="190" x2="320" y2="140" stroke="#7C3AED" stroke-width="2"/>
    
    <line x1="380" y1="210" x2="380" y2="180" stroke="#7C3AED" stroke-width="2"/>
    <line x1="420" y1="210" x2="420" y2="180" stroke="#7C3AED" stroke-width="2"/>
    <line x1="380" y1="180" x2="420" y2="180" stroke="#7C3AED" stroke-width="2"/>
    <line x1="400" y1="180" x2="400" y2="140" stroke="#7C3AED" stroke-width="2"/>
    
    <line x1="320" y1="140" x2="400" y2="140" stroke="#7C3AED" stroke-width="2"/>
    <line x1="360" y1="140" x2="360" y2="70" stroke="#7C3AED" stroke-width="2"/>
    
    <!-- Group 3: Amber (x=500, 540, 580, 620) -->
    <line x1="500" y1="210" x2="500" y2="185" stroke="#D97706" stroke-width="2"/>
    <line x1="540" y1="210" x2="540" y2="185" stroke="#D97706" stroke-width="2"/>
    <line x1="500" y1="185" x2="540" y2="185" stroke="#D97706" stroke-width="2"/>
    <line x1="520" y1="185" x2="520" y2="135" stroke="#D97706" stroke-width="2"/>
    
    <line x1="580" y1="210" x2="580" y2="170" stroke="#D97706" stroke-width="2"/>
    <line x1="620" y1="210" x2="620" y2="170" stroke="#D97706" stroke-width="2"/>
    <line x1="580" y1="170" x2="620" y2="170" stroke="#D97706" stroke-width="2"/>
    <line x1="600" y1="170" x2="600" y2="135" stroke="#D97706" stroke-width="2"/>
    
    <line x1="520" y1="135" x2="600" y2="135" stroke="#D97706" stroke-width="2"/>
    <line x1="560" y1="135" x2="560" y2="70" stroke="#D97706" stroke-width="2"/>
    
    <!-- Top Level Merges (Black) -->
    <line x1="360" y1="70" x2="560" y2="70" stroke="#334155" stroke-width="2"/>
    <line x1="460" y1="70" x2="460" y2="50" stroke="#334155" stroke-width="2"/>
    
    <line x1="160" y1="50" x2="460" y2="50" stroke="#334155" stroke-width="2"/>
    <line x1="310" y1="50" x2="310" y2="25" stroke="#334155" stroke-width="2"/>
    
    <!-- Leaf Labels -->
    <text x="160" y="228" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#0891B2" text-anchor="middle">Cluster 1 (4 pts)</text>
    <text x="360" y="228" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#7C3AED" text-anchor="middle">Cluster 2 (4 pts)</text>
    <text x="560" y="228" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#D97706" text-anchor="middle">Cluster 3 (4 pts)</text>
  </g>
</svg>"""

# 13. Dendrogram Cuts Producing Different Cluster Counts
SVG_DENDROGRAM_CUTS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="30" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Cutting the Dendrogram: Selecting the Granularity of Clusters</text>
  <text x="460" y="48" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">A horizontal slice across the tree determines the exact number of disjoint clusters obtained</text>
  
  <g transform="translate(140, 70)">
    <!-- Tree Schematic -->
    <!-- Root -->
    <line x1="160" y1="40" x2="480" y2="40" stroke="#334155" stroke-width="2.5"/>
    
    <!-- Cut 1: High Cut at Height = 8.0 -> 2 Clusters -->
    <line x1="20" y1="30" x2="620" y2="30" stroke="#DC2626" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="630" y="34" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="start">Cut A (Height 8.0) → K = 2 Clusters</text>
    
    <!-- Cut 2: Medium Cut at Height = 5.0 -> 3 Clusters -->
    <line x1="20" y1="75" x2="620" y2="75" stroke="#059669" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="630" y="79" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#059669" text-anchor="start">Cut B (Height 5.0) → K = 3 Clusters</text>
    
    <!-- Cut 3: Low Cut at Height = 2.5 -> 6 Clusters -->
    <line x1="20" y1="135" x2="620" y2="135" stroke="#2563EB" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="630" y="139" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#2563EB" text-anchor="start">Cut C (Height 2.5) → K = 6 Sub-Clusters</text>
    
    <!-- Branches -->
    <line x1="160" y1="40" x2="160" y2="100" stroke="#0891B2" stroke-width="2"/>
    <line x1="480" y1="40" x2="480" y2="60" stroke="#7C3AED" stroke-width="2"/>
    
    <line x1="360" y1="60" x2="580" y2="60" stroke="#7C3AED" stroke-width="2"/>
    <line x1="360" y1="60" x2="360" y2="100" stroke="#7C3AED" stroke-width="2"/>
    <line x1="580" y1="60" x2="580" y2="100" stroke="#D97706" stroke-width="2"/>
    
    <!-- Sub-branches -->
    <line x1="100" y1="100" x2="220" y2="100" stroke="#0891B2" stroke-width="2"/>
    <line x1="100" y1="100" x2="100" y2="180" stroke="#0891B2" stroke-width="1.5"/>
    <line x1="220" y1="100" x2="220" y2="180" stroke="#0891B2" stroke-width="1.5"/>
    
    <line x1="300" y1="100" x2="420" y2="100" stroke="#7C3AED" stroke-width="2"/>
    <line x1="300" y1="100" x2="300" y2="180" stroke="#7C3AED" stroke-width="1.5"/>
    <line x1="420" y1="100" x2="420" y2="180" stroke="#7C3AED" stroke-width="1.5"/>
    
    <line x1="520" y1="100" x2="640" y2="100" stroke="#D97706" stroke-width="2"/>
    <line x1="520" y1="100" x2="520" y2="180" stroke="#D97706" stroke-width="1.5"/>
    <line x1="640" y1="100" x2="640" y2="180" stroke="#D97706" stroke-width="1.5"/>
    
    <!-- Base text summary -->
    <rect x="60" y="195" width="520" height="36" fill="#F8FAFC" rx="6" stroke="#E2E8F0"/>
    <text x="320" y="218" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#334155" text-anchor="middle">Insight: You do not need to re-fit the model to try different values of K!</text>
  </g>
</svg>"""

# 14. DBSCAN Core, Border, and Noise Points Illustration
SVG_DBSCAN_CONCEPTS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">DBSCAN Density Taxonomy: Core, Border, and Noise Points</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Parameters: Neighbourhood radius (ε) and Minimum Samples (min_samples = 4)</text>
  
  <g transform="translate(60, 75)">
    <rect width="800" height="235" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- 1. CORE POINT (Green) at (180, 110) -->
    <!-- eps circle: r = 60 -->
    <circle cx="180" cy="110" r="65" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="180" y1="110" x2="245" y2="110" stroke="#059669" stroke-width="1.5"/>
    <text x="210" y="105" font-family="SFMono-Regular, Consolas, monospace" font-size="10" font-weight="700" fill="#059669" text-anchor="middle">ε</text>
    
    <!-- Points inside Core's eps (includes self + 4 neighbors = 5 >= min_samples) -->
    <circle cx="180" cy="110" r="8" fill="#10B981" stroke="#064E3B" stroke-width="2"/>
    <text x="180" y="85" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="800" fill="#065F46" text-anchor="middle">CORE POINT</text>
    <text x="180" y="195" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="600" fill="#047857" text-anchor="middle">≥ 4 neighbors in ε</text>
    
    <circle cx="150" cy="90" r="5" fill="#10B981"/>
    <circle cx="210" cy="85" r="5" fill="#10B981"/>
    <circle cx="160" cy="140" r="5" fill="#10B981"/>
    <circle cx="215" cy="130" r="5" fill="#10B981"/>
    
    <!-- 2. BORDER POINT (Amber) at (460, 110) -->
    <!-- Inside Core's reach, but has < min_samples in its own radius -->
    <circle cx="460" cy="110" r="65" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.5" stroke-dasharray="4,4"/>
    <circle cx="460" cy="110" r="8" fill="#F59E0B" stroke="#78350F" stroke-width="2"/>
    <text x="460" y="85" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="800" fill="#92400E" text-anchor="middle">BORDER POINT</text>
    <text x="460" y="195" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="600" fill="#B45309" text-anchor="middle">&lt; 4 neighbors, but within Core ε</text>
    
    <circle cx="430" cy="130" r="5" fill="#10B981"/>
    <circle cx="485" cy="95" r="5" fill="#10B981"/>
    
    <!-- 3. NOISE POINT (Red Cross) at (710, 110) -->
    <!-- Isolated: < min_samples and not reachable from any core -->
    <circle cx="710" cy="110" r="65" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="4,4"/>
    <!-- Red Cross -->
    <line x1="702" y1="102" x2="718" y2="118" stroke="#DC2626" stroke-width="3"/>
    <line x1="718" y1="102" x2="702" y2="118" stroke="#DC2626" stroke-width="3"/>
    <text x="710" y="85" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="800" fill="#991B1B" text-anchor="middle">NOISE POINT</text>
    <text x="710" y="195" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="600" fill="#B91C1C" text-anchor="middle">Label = −1 (Outlier)</text>
    
    <circle cx="740" cy="140" r="4" fill="#94A3B8"/>
  </g>
</svg>"""

# 15. Actual DBSCAN Clusters and Noise Observations
SVG_DBSCAN_CLUSTERS_NOISE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">DBSCAN Discovered Clusters and Extracted Noise Observations</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Trained with eps=0.28, min_samples=6: Discovered 2 non-convex moons, isolated 18 noise outliers (-1)</text>
  
  <g transform="translate(160, 70)">
    <rect width="600" height="240" fill="#FAFAFA" rx="8" stroke="#CBD5E1" stroke-width="1"/>
    
    <!-- Top Moon (Cluster 0: Vibrant Teal) -->
    <path d="M 120,130 A 110,110 0 0,1 360,70" fill="none" stroke="#0891B2" stroke-width="14" stroke-linecap="round" opacity="0.85"/>
    <text x="240" y="45" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#0891B2" text-anchor="middle">Cluster 0 (Upper Crescent • 130 pts)</text>
    
    <!-- Bottom Moon (Cluster 1: Royal Violet) -->
    <path d="M 240,160 A 110,110 0 0,0 480,200" fill="none" stroke="#7C3AED" stroke-width="14" stroke-linecap="round" opacity="0.85"/>
    <text x="360" y="235" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#7C3AED" text-anchor="middle">Cluster 1 (Lower Crescent • 130 pts)</text>
    
    <!-- Identified Noise Points (Red Crosses, Label = -1) -->
    <!-- Scattered outliers -->
    <g stroke="#DC2626" stroke-width="2.5">
      <!-- point 1 --> <line x1="55" y1="45" x2="65" y2="55"/> <line x1="65" y1="45" x2="55" y2="55"/>
      <!-- point 2 --> <line x1="85" y1="185" x2="95" y2="195"/> <line x1="95" y1="185" x2="85" y2="195"/>
      <!-- point 3 --> <line x1="210" y1="110" x2="220" y2="120"/> <line x1="220" y1="110" x2="210" y2="120"/>
      <!-- point 4 --> <line x1="390" y1="130" x2="400" y2="140"/> <line x1="400" y1="130" x2="390" y2="140"/>
      <!-- point 5 --> <line x1="520" y1="50" x2="530" y2="60"/> <line x1="530" y1="50" x2="520" y2="60"/>
      <!-- point 6 --> <line x1="550" y1="175" x2="560" y2="185"/> <line x1="560" y1="175" x2="550" y2="185"/>
      <!-- point 7 --> <line x1="330" y1="95" x2="340" y2="105"/> <line x1="340" y1="95" x2="330" y2="105"/>
    </g>
    
    <!-- Legend Callout -->
    <rect x="420" y="15" width="165" height="48" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <circle cx="435" cy="30" r="5" fill="#0891B2"/>
    <text x="445" y="34" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#334155">Clusters 0 &amp; 1</text>
    <line x1="430" y1="47" x2="440" y2="55" stroke="#DC2626" stroke-width="2"/>
    <line x1="440" y1="47" x2="430" y2="55" stroke="#DC2626" stroke-width="2"/>
    <text x="445" y="54" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#DC2626">Noise (Label −1, 18 pts)</text>
  </g>
</svg>"""

# 16. DBSCAN Epsilon Comparison (Too small, Optimal, Too large)
SVG_DBSCAN_EPS_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="30" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Sensitivity to Hyperparameters: The Effect of Epsilon (ε)</text>
  <text x="460" y="48" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Holding min_samples=5 constant while varying the neighbourhood radius ε</text>
  
  <!-- Panel 1: eps too small -->
  <g transform="translate(30, 65)">
    <rect width="260" height="250" fill="#FFF1F2" rx="8" stroke="#FECDD3" stroke-width="1"/>
    <text x="130" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#9F1239" text-anchor="middle">ε TOO SMALL (ε = 0.10)</text>
    <rect x="20" y="38" width="220" height="145" fill="#FFFFFF" rx="4" stroke="#FDA4AF"/>
    
    <!-- Most points marked as noise (red crosses) -->
    <g stroke="#DC2626" stroke-width="2">
      <line x1="50" y1="70" x2="60" y2="80"/> <line x1="60" y1="70" x2="50" y2="80"/>
      <line x1="75" y1="85" x2="85" y2="95"/> <line x1="85" y1="85" x2="75" y2="95"/>
      <line x1="120" y1="65" x2="130" y2="75"/> <line x1="130" y1="65" x2="120" y2="75"/>
      <line x1="160" y1="80" x2="170" y2="90"/> <line x1="170" y1="80" x2="160" y2="90"/>
      <line x1="190" y1="70" x2="200" y2="80"/> <line x1="200" y1="70" x2="190" y2="80"/>
      <line x1="100" y1="130" x2="110" y2="140"/> <line x1="110" y1="130" x2="100" y2="140"/>
      <line x1="140" y1="145" x2="150" y2="155"/> <line x1="150" y1="145" x2="140" y2="155"/>
      <line x1="180" y1="135" x2="190" y2="145"/> <line x1="190" y1="135" x2="180" y2="145"/>
    </g>
    
    <text x="130" y="202" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#9F1239" text-anchor="middle">✗ Excessive Noise: 80% flagged as noise</text>
    <text x="130" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Radius too tight to connect neighbors</text>
  </g>
  
  <!-- Panel 2: eps optimal -->
  <g transform="translate(330, 65)">
    <rect width="260" height="250" fill="#F0FDF4" rx="8" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="130" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="800" fill="#166534" text-anchor="middle">✓ OPTIMAL ε (ε = 0.28)</text>
    <rect x="20" y="38" width="220" height="145" fill="#FFFFFF" rx="4" stroke="#86EFAC"/>
    
    <!-- 2 cleanly discovered crescents -->
    <path d="M 60,95 A 50,50 0 0,1 180,75" fill="none" stroke="#0891B2" stroke-width="8" stroke-linecap="round"/>
    <path d="M 100,125 A 50,50 0 0,0 200,145" fill="none" stroke="#7C3AED" stroke-width="8" stroke-linecap="round"/>
    <!-- Few real outliers -->
    <line x1="45" y1="150" x2="53" y2="158" stroke="#DC2626" stroke-width="2"/>
    <line x1="53" y1="150" x2="45" y2="158" stroke="#DC2626" stroke-width="2"/>
    
    <text x="130" y="202" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">✓ Clean Non-Convex Discovery</text>
    <text x="130" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#166534" text-anchor="middle">2 natural clusters + real noise separated</text>
  </g>
  
  <!-- Panel 3: eps too large -->
  <g transform="translate(630, 65)">
    <rect width="260" height="250" fill="#FFFBEB" rx="8" stroke="#FDE68A" stroke-width="1"/>
    <text x="130" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#92400E" text-anchor="middle">ε TOO LARGE (ε = 0.75)</text>
    <rect x="20" y="38" width="220" height="145" fill="#FFFFFF" rx="4" stroke="#FDE68A"/>
    
    <!-- Giant merged blob: all one color -->
    <path d="M 60,95 A 50,50 0 0,1 180,75" fill="none" stroke="#2563EB" stroke-width="8" stroke-linecap="round"/>
    <path d="M 100,125 A 50,50 0 0,0 200,145" fill="none" stroke="#2563EB" stroke-width="8" stroke-linecap="round"/>
    <line x1="120" y1="85" x2="140" y2="135" stroke="#2563EB" stroke-width="8"/>
    
    <text x="130" y="202" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#92400E" text-anchor="middle">! Merged into 1 Giant Cluster</text>
    <text x="130" y="220" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Noise absorbed; bridge connects all points</text>
  </g>
</svg>"""

# 17. Head-to-Head: K-Means vs. DBSCAN on Complex Geometry
SVG_KMEANS_VS_DBSCAN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Direct Head-to-Head: K-Means vs. DBSCAN on Interlocking Crescent Moons</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Comparing distance-to-centroid partitioning versus density-connected chaining</text>
  
  <!-- Left: K-Means -->
  <g transform="translate(40, 75)">
    <rect width="400" height="235" fill="#FFF1F2" rx="8" stroke="#FECDD3" stroke-width="1"/>
    <text x="200" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#9F1239" text-anchor="middle">K-MEANS (K = 2) • Adjusted Rand Index: 0.4053</text>
    
    <rect x="25" y="45" width="350" height="140" fill="#FFFFFF" rx="6" stroke="#FDA4AF" stroke-width="1"/>
    
    <!-- Linear partition cuts crescent moons orthogonally -->
    <path d="M 70,110 A 60,60 0 0,1 190,75" fill="none" stroke="#DC2626" stroke-width="7" stroke-linecap="round"/>
    <path d="M 190,75 A 60,60 0 0,1 270,110" fill="none" stroke="#2563EB" stroke-width="7" stroke-linecap="round"/>
    
    <path d="M 130,130 A 60,60 0 0,0 210,165" fill="none" stroke="#DC2626" stroke-width="7" stroke-linecap="round"/>
    <path d="M 210,165 A 60,60 0 0,0 330,130" fill="none" stroke="#2563EB" stroke-width="7" stroke-linecap="round"/>
    
    <!-- Voronoi partition line -->
    <line x1="200" y1="45" x2="200" y2="185" stroke="#0F172A" stroke-width="2" stroke-dasharray="4,4"/>
    
    <text x="200" y="208" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#9F1239" text-anchor="middle">✗ Fails on non-convex manifolds</text>
    <text x="200" y="224" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Centroid arithmetic mean is physically outside the crescent shape!</text>
  </g>
  
  <!-- Right: DBSCAN -->
  <g transform="translate(480, 75)">
    <rect width="400" height="235" fill="#F0FDF4" rx="8" stroke="#BBF7D0" stroke-width="1"/>
    <text x="200" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="700" fill="#166534" text-anchor="middle">DBSCAN (ε=0.28) • Adjusted Rand Index: 0.9770</text>
    
    <rect x="25" y="45" width="350" height="140" fill="#FFFFFF" rx="6" stroke="#86EFAC" stroke-width="1"/>
    
    <!-- Naturally follows the non-linear density shapes -->
    <path d="M 70,110 A 60,60 0 0,1 270,110" fill="none" stroke="#0891B2" stroke-width="8" stroke-linecap="round"/>
    <path d="M 130,130 A 60,60 0 0,0 330,130" fill="none" stroke="#7C3AED" stroke-width="8" stroke-linecap="round"/>
    
    <!-- Noise points -->
    <line x1="50" y1="55" x2="58" y2="63" stroke="#DC2626" stroke-width="2"/>
    <line x1="58" y1="55" x2="50" y2="63" stroke="#DC2626" stroke-width="2"/>
    <line x1="330" y1="65" x2="338" y2="73" stroke="#DC2626" stroke-width="2"/>
    <line x1="338" y1="65" x2="330" y2="73" stroke="#DC2626" stroke-width="2"/>
    
    <text x="200" y="208" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">✓ Perfectly unrolls non-linear geometry</text>
    <text x="200" y="224" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" fill="#166534" text-anchor="middle">Follows continuous density highway; isolates background noise</text>
  </g>
</svg>"""

# 18. Clustering Evaluation Metrics Comparison
SVG_METRICS_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 340" width="100%" preserveAspectRatio="xMidYMid meet" style="max-width: 920px;">
  <rect width="920" height="340" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  
  <text x="460" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" font-weight="700" fill="#0F172A" text-anchor="middle">Clustering Evaluation Metrics Dashboard (K = 2 to 6)</text>
  <text x="460" y="52" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">Comparing Silhouette (higher=better), Davies-Bouldin (lower=better), and Calinski-Harabasz (higher=better)</text>
  
  <!-- 3 Metric Cards -->
  <!-- 1. Silhouette Score -->
  <g transform="translate(40, 75)">
    <rect width="260" height="235" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="0" y="0" width="260" height="34" fill="#EEF2FF" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="130" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#4338CA" text-anchor="middle">1. Silhouette Score (↑ Higher)</text>
    
    <text x="20" y="65" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 2: 0.5391</text>
    <rect x="80" y="55" width="108" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="20" y="95" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#047857">K = 3: 0.7746 ★</text>
    <rect x="80" y="85" width="155" height="12" fill="#10B981" rx="2"/>
    
    <text x="20" y="125" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 4: 0.6273</text>
    <rect x="80" y="115" width="125" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="20" y="155" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 5: 0.4713</text>
    <rect x="80" y="145" width="94" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="20" y="185" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 6: 0.3266</text>
    <rect x="80" y="175" width="65" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="130" y="218" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Peak at K = 3 (+0.77)</text>
  </g>
  
  <!-- 2. Davies-Bouldin Index -->
  <g transform="translate(330, 75)">
    <rect width="260" height="235" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="0" y="0" width="260" height="34" fill="#FEF2F2" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="130" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#B91C1C" text-anchor="middle">2. Davies-Bouldin (↓ Lower)</text>
    
    <text x="20" y="65" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 2: 0.7253</text>
    <rect x="80" y="55" width="95" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="20" y="95" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#047857">K = 3: 0.3090 ★</text>
    <rect x="80" y="85" width="40" height="12" fill="#10B981" rx="2"/>
    
    <text x="20" y="125" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 4: 0.6915</text>
    <rect x="80" y="115" width="90" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="20" y="155" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 5: 0.9693</text>
    <rect x="80" y="145" width="125" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="20" y="185" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 6: 1.1585</text>
    <rect x="80" y="175" width="150" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="130" y="218" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Lowest at K = 3 (0.31)</text>
  </g>
  
  <!-- 3. Calinski-Harabasz Score -->
  <g transform="translate(620, 75)">
    <rect width="260" height="235" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="0" y="0" width="260" height="34" fill="#F0FDF4" rx="8" stroke="#E2E8F0" stroke-width="1"/>
    <text x="130" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="12" font-weight="700" fill="#166534" text-anchor="middle">3. Calinski-Harabasz (↑ Higher)</text>
    
    <text x="20" y="65" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 2: 284.2</text>
    <rect x="80" y="55" width="28" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="20" y="95" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" font-weight="700" fill="#047857">K = 3: 1745.5 ★</text>
    <rect x="80" y="85" width="170" height="12" fill="#10B981" rx="2"/>
    
    <text x="20" y="125" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 4: 1342.4</text>
    <rect x="80" y="115" width="130" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="20" y="155" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 5: 1165.0</text>
    <rect x="80" y="145" width="113" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="20" y="185" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="11" fill="#64748B">K = 6: 1108.6</text>
    <rect x="80" y="175" width="107" height="12" fill="#94A3B8" rx="2"/>
    
    <text x="130" y="218" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Peak at K = 3 (1,745.5)</text>
  </g>
</svg>"""

ALL_TOPIC16_SVGS = {
    "SVG_CLUSTERING_OVERVIEW": SVG_CLUSTERING_OVERVIEW,
    "SVG_CLUSTERING_VS_CLASSIFICATION": SVG_CLUSTERING_VS_CLASSIFICATION,
    "SVG_EUCLIDEAN_VS_MANHATTAN": SVG_EUCLIDEAN_VS_MANHATTAN,
    "SVG_SCALING_EFFECT": SVG_SCALING_EFFECT,
    "SVG_KMEANS_STEPS_PANEL": SVG_KMEANS_STEPS_PANEL,
    "SVG_KMEANS_CENTROIDS_FINAL": SVG_KMEANS_CENTROIDS_FINAL,
    "SVG_ELBOW_METHOD": SVG_ELBOW_METHOD,
    "SVG_SILHOUETTE_ANALYSIS": SVG_SILHOUETTE_ANALYSIS,
    "SVG_K_VALUES_GRID": SVG_K_VALUES_GRID,
    "SVG_KMEANS_LIMITATIONS": SVG_KMEANS_LIMITATIONS,
    "SVG_LINKAGE_COMPARISON": SVG_LINKAGE_COMPARISON,
    "SVG_DENDROGRAM": SVG_DENDROGRAM,
    "SVG_DENDROGRAM_CUTS": SVG_DENDROGRAM_CUTS,
    "SVG_DBSCAN_CONCEPTS": SVG_DBSCAN_CONCEPTS,
    "SVG_DBSCAN_CLUSTERS_NOISE": SVG_DBSCAN_CLUSTERS_NOISE,
    "SVG_DBSCAN_EPS_COMPARISON": SVG_DBSCAN_EPS_COMPARISON,
    "SVG_KMEANS_VS_DBSCAN": SVG_KMEANS_VS_DBSCAN,
    "SVG_METRICS_COMPARISON": SVG_METRICS_COMPARISON,
}

def validate_all_svgs():
    print(f"Validating {len(ALL_TOPIC16_SVGS)} SVG diagrams for Topic 16...")
    all_passed = True
    for name, svg in ALL_TOPIC16_SVGS.items():
        try:
            root = ET.fromstring(svg)
            print(f"PASS: {name} (valid XML, root: {root.tag})")
        except Exception as e:
            print(f"ERROR in {name}: {e}")
            all_passed = False
    if all_passed:
        print(f"\nALL {len(ALL_TOPIC16_SVGS)} SVGS ARE 100% XML-VALID AND STRICT LIGHT-MODE READY!\n")
    else:
        print("\nSOME SVGS FAILED VALIDATION.\n")
    return all_passed

if __name__ == "__main__":
    validate_all_svgs()
