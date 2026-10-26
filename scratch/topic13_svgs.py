"""
Generates and validates all 15 inline SVG diagrams for Topic 13: Support Vector Machine (SVM).
Strict Light Mode, clear typography, verified numerical geometry, valid XML.
Uses literal UTF-8 symbols (no undefined HTML named entities).
"""

import xml.etree.ElementTree as ET

# 1. Hero / Two-Class Hyperplane (Figure 13.1)
SVG_TWO_CLASS_HYPERPLANE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <defs>
    <linearGradient id="bg-grad-1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>
    <filter id="shadow-1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Title & Subtitle -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Two-Class Classification &amp; The Separating Hyperplane</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">In 2D space, the separating hyperplane is a straight boundary line: w₁x₁ + w₂x₂ + b = 0</text>

  <!-- Coordinate Axes Box -->
  <g transform="translate(60, 90)">
    <!-- Grid lines -->
    <rect x="0" y="0" width="460" height="280" fill="url(#bg-grad-1)" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <line x1="0" y1="70" x2="460" y2="70" stroke="#E2E8F0" stroke-dasharray="4,4"/>
    <line x1="0" y1="140" x2="460" y2="140" stroke="#E2E8F0" stroke-dasharray="4,4"/>
    <line x1="0" y1="210" x2="460" y2="210" stroke="#E2E8F0" stroke-dasharray="4,4"/>
    <line x1="115" y1="0" x2="115" y2="280" stroke="#E2E8F0" stroke-dasharray="4,4"/>
    <line x1="230" y1="0" x2="230" y2="280" stroke="#E2E8F0" stroke-dasharray="4,4"/>
    <line x1="345" y1="0" x2="345" y2="280" stroke="#E2E8F0" stroke-dasharray="4,4"/>

    <!-- Decision Regions Soft Fill -->
    <polygon points="0,0 280,0 60,280 0,280" fill="#EFF6FF" fill-opacity="0.6"/>
    <polygon points="280,0 460,0 460,280 60,280" fill="#FEF2F2" fill-opacity="0.6"/>

    <!-- Hyperplane Decision Boundary -->
    <line x1="280" y1="0" x2="60" y2="280" stroke="#2563EB" stroke-width="3.5"/>
    
    <!-- Class 0 Data Points (Blue circles - Admitted) -->
    <circle cx="50" cy="50" r="7" fill="#2563EB" stroke="#FFFFFF" stroke-width="2"/>
    <circle cx="90" cy="70" r="7" fill="#2563EB" stroke="#FFFFFF" stroke-width="2"/>
    <circle cx="70" cy="120" r="7" fill="#2563EB" stroke="#FFFFFF" stroke-width="2"/>
    <circle cx="130" cy="40" r="7" fill="#2563EB" stroke="#FFFFFF" stroke-width="2"/>
    <circle cx="120" cy="90" r="7" fill="#2563EB" stroke="#FFFFFF" stroke-width="2"/>
    <circle cx="170" cy="60" r="7" fill="#2563EB" stroke="#FFFFFF" stroke-width="2"/>
    <circle cx="110" cy="160" r="7" fill="#2563EB" stroke="#FFFFFF" stroke-width="2"/>
    <circle cx="50" cy="200" r="7" fill="#2563EB" stroke="#FFFFFF" stroke-width="2"/>

    <!-- Class 1 Data Points (Red squares - Rejected) -->
    <rect x="250" y="220" width="14" height="14" fill="#DC2626" rx="3" stroke="#FFFFFF" stroke-width="2"/>
    <rect x="310" y="190" width="14" height="14" fill="#DC2626" rx="3" stroke="#FFFFFF" stroke-width="2"/>
    <rect x="280" y="140" width="14" height="14" fill="#DC2626" rx="3" stroke="#FFFFFF" stroke-width="2"/>
    <rect x="360" y="160" width="14" height="14" fill="#DC2626" rx="3" stroke="#FFFFFF" stroke-width="2"/>
    <rect x="390" y="90" width="14" height="14" fill="#DC2626" rx="3" stroke="#FFFFFF" stroke-width="2"/>
    <rect x="340" y="70" width="14" height="14" fill="#DC2626" rx="3" stroke="#FFFFFF" stroke-width="2"/>
    <rect x="420" y="230" width="14" height="14" fill="#DC2626" rx="3" stroke="#FFFFFF" stroke-width="2"/>
    <rect x="300" y="250" width="14" height="14" fill="#DC2626" rx="3" stroke="#FFFFFF" stroke-width="2"/>

    <!-- Boundary Annotation -->
    <rect x="185" y="115" width="200" height="32" rx="6" fill="#FFFFFF" stroke="#2563EB" stroke-width="1.5" filter="url(#shadow-1)"/>
    <text x="285" y="136" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1D4ED8" text-anchor="middle">Hyperplane: wᵀx + b = 0</text>

    <!-- Axes Labels -->
    <text x="230" y="305" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#475569" text-anchor="middle">Feature x₁ (Exam Score) →</text>
    <text x="-20" y="140" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#475569" text-anchor="middle" transform="rotate(-90, -20, 140)">Feature x₂ (Project Score) →</text>
  </g>

  <!-- Side Legend & Key Takeaway Card -->
  <g transform="translate(550, 90)">
    <rect x="0" y="0" width="210" height="280" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="16" y="28" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A">Key Concepts</text>
    
    <circle cx="26" cy="60" r="6" fill="#2563EB"/>
    <text x="42" y="64" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#1E40AF">Class +1 (Admitted)</text>
    <text x="42" y="78" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">wᵀx + b &gt; 0</text>

    <rect x="20" y="96" width="12" height="12" fill="#DC2626" rx="2"/>
    <text x="42" y="106" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#991B1B">Class -1 (Rejected)</text>
    <text x="42" y="120" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B">wᵀx + b &lt; 0</text>

    <line x1="16" y1="140" x2="194" y2="140" stroke="#E2E8F0"/>

    <text x="16" y="165" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Dimensionality:</text>
    <text x="16" y="185" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 2D Space → 1D Line</text>
    <text x="16" y="202" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• 3D Space → 2D Flat Plane</text>
    <text x="16" y="219" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">• D-dim → (D-1) Hyperplane</text>

    <rect x="12" y="235" width="186" height="32" rx="6" fill="#EFF6FF" stroke="#BFDBFE"/>
    <text x="105" y="255" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#1E40AF" text-anchor="middle">Separates classes with a margin</text>
  </g>
</svg>"""

# 2. Maximum-Margin Geometry (Figure 13.2)
SVG_MAXIMUM_MARGIN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <defs>
    <linearGradient id="margin-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#F5F3FF"/>
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#4F46E5"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">The Canonical SVM Margin: Maximum Separation Geometry</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">The optimal hyperplane maximizes the total margin width: M = 2 / ∥w∥</text>

  <!-- Diagram Box -->
  <g transform="translate(60, 90)">
    <!-- Base Canvas -->
    <rect x="0" y="0" width="480" height="280" fill="#FAFAFA" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>

    <!-- Margin Zone Shading -->
    <!-- Positive margin: (170,0) to (20,280), Decision: (230,0) to (80,280), Negative margin: (290,0) to (140,280) -->
    <polygon points="170,0 290,0 140,280 20,280" fill="url(#margin-grad)" fill-opacity="0.8"/>

    <!-- Positive Margin Boundary: w^T x + b = +1 -->
    <line x1="170" y1="0" x2="20" y2="280" stroke="#059669" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="90" y="35" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#059669">Positive Margin: wᵀx + b = +1</text>

    <!-- Decision Boundary: w^T x + b = 0 -->
    <line x1="230" y1="0" x2="80" y2="280" stroke="#2563EB" stroke-width="3"/>
    <text x="175" y="65" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#2563EB">Hyperplane: wᵀx + b = 0</text>

    <!-- Negative Margin Boundary: w^T x + b = -1 -->
    <line x1="290" y1="0" x2="140" y2="280" stroke="#DC2626" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="240" y="95" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">Negative Margin: wᵀx + b = -1</text>

    <!-- Non-Support Vector Points (Class +1) -->
    <circle cx="50" cy="50" r="6" fill="#2563EB"/>
    <circle cx="40" cy="110" r="6" fill="#2563EB"/>
    <circle cx="30" cy="180" r="6" fill="#2563EB"/>
    <circle cx="70" cy="30" r="6" fill="#2563EB"/>

    <!-- Support Vectors (Class +1) on Margin Plane -->
    <g transform="translate(130, 75)">
      <circle cx="0" cy="0" r="12" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="3,2"/>
      <circle cx="0" cy="0" r="6" fill="#2563EB"/>
      <text x="-70" y="-12" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#D97706">Support Vector</text>
    </g>
    <g transform="translate(75, 177)">
      <circle cx="0" cy="0" r="12" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="3,2"/>
      <circle cx="0" cy="0" r="6" fill="#2563EB"/>
    </g>

    <!-- Non-Support Vector Points (Class -1) -->
    <rect x="360" y="160" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="400" y="120" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="320" y="240" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="420" y="210" width="12" height="12" fill="#DC2626" rx="2"/>

    <!-- Support Vectors (Class -1) on Margin Plane -->
    <g transform="translate(235, 102)">
      <circle cx="6" cy="6" r="12" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="3,2"/>
      <rect x="0" y="0" width="12" height="12" fill="#DC2626" rx="2"/>
      <text x="22" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#D97706">Support Vector</text>
    </g>
    <g transform="translate(180, 205)">
      <circle cx="6" cy="6" r="12" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="3,2"/>
      <rect x="0" y="0" width="12" height="12" fill="#DC2626" rx="2"/>
    </g>

    <!-- Margin Width Arrow -->
    <line x1="95" y1="140" x2="215" y2="140" stroke="#4F46E5" stroke-width="2.5" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
    <rect x="110" y="148" width="90" height="24" rx="4" fill="#FFFFFF" stroke="#4F46E5" stroke-width="1.2"/>
    <text x="155" y="164" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4F46E5" text-anchor="middle">Margin = 2/∥w∥</text>
  </g>

  <!-- Side Mathematical Breakdown Card -->
  <g transform="translate(565, 90)">
    <rect x="0" y="0" width="195" height="280" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="14" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A">Margin Mathematics</text>

    <rect x="12" y="42" width="171" height="52" rx="6" fill="#EFF6FF" stroke="#BFDBFE"/>
    <text x="97" y="62" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">Distance from Point to Line:</text>
    <text x="97" y="82" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1D4ED8" text-anchor="middle">d = |wᵀx + b| / ∥w∥</text>

    <text x="14" y="116" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155">On Margin Planes:</text>
    <text x="14" y="134" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Class +1: wᵀx + b = +1</text>
    <text x="14" y="150" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Class -1: wᵀx + b = -1</text>
    <text x="14" y="166" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Distance to center = 1/∥w∥</text>

    <line x1="14" y1="180" x2="181" y2="180" stroke="#E2E8F0"/>

    <text x="14" y="200" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155">Maximizing Margin Width:</text>
    <text x="14" y="220" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Max ( 2 / ∥w∥ ) is exactly</text>
    <text x="14" y="238" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">equivalent to:</text>
    <rect x="12" y="246" width="171" height="26" rx="4" fill="#ECFDF5" stroke="#A7F3D0"/>
    <text x="97" y="263" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">Min ( ½ ∥w∥² )</text>
  </g>
</svg>"""

# 3. Actual Support Vectors Highlighted (Figure 13.3)
SVG_ACTUAL_SUPPORT_VECTORS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Actual Support Vectors Identified on Fitted Scikit-Learn Model</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Only the support vectors determine the boundary position; non-support points could be deleted without moving the line!</text>

  <!-- Canvas -->
  <g transform="translate(60, 85)">
    <rect x="0" y="0" width="480" height="260" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>

    <!-- Margins and Boundary -->
    <line x1="160" y1="0" x2="40" y2="260" stroke="#059669" stroke-width="1.5" stroke-dasharray="5,4"/>
    <line x1="220" y1="0" x2="100" y2="260" stroke="#2563EB" stroke-width="3"/>
    <line x1="280" y1="0" x2="160" y2="260" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="5,4"/>

    <!-- Regular Non-Support Vector points (faint opacity) -->
    <circle cx="45" cy="50" r="6" fill="#93C5FD" opacity="0.6"/>
    <circle cx="30" cy="110" r="6" fill="#93C5FD" opacity="0.6"/>
    <circle cx="65" cy="140" r="6" fill="#93C5FD" opacity="0.6"/>
    <circle cx="20" cy="190" r="6" fill="#93C5FD" opacity="0.6"/>
    <circle cx="70" cy="20" r="6" fill="#93C5FD" opacity="0.6"/>

    <rect x="340" y="140" width="12" height="12" fill="#FCA5A5" rx="2" opacity="0.6"/>
    <rect x="380" y="100" width="12" height="12" fill="#FCA5A5" rx="2" opacity="0.6"/>
    <rect x="420" y="180" width="12" height="12" fill="#FCA5A5" rx="2" opacity="0.6"/>
    <rect x="300" y="220" width="12" height="12" fill="#FCA5A5" rx="2" opacity="0.6"/>

    <!-- Support Vectors with Double Gold Rings and Solid Fills -->
    <!-- SV Class +1 -->
    <g transform="translate(130, 65)">
      <circle cx="0" cy="0" r="13" fill="none" stroke="#D97706" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="6" fill="#1D4ED8"/>
      <text x="-95" y="4" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#B45309">SV #1 (Class 1)</text>
    </g>
    <g transform="translate(85, 163)">
      <circle cx="0" cy="0" r="13" fill="none" stroke="#D97706" stroke-width="2.5"/>
      <circle cx="0" cy="0" r="6" fill="#1D4ED8"/>
      <text x="-95" y="4" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#B45309">SV #2 (Class 1)</text>
    </g>

    <!-- SV Class -1 -->
    <g transform="translate(230, 108)">
      <circle cx="6" cy="6" r="13" fill="none" stroke="#D97706" stroke-width="2.5"/>
      <rect x="0" y="0" width="12" height="12" fill="#B91C1C" rx="2"/>
      <text x="25" y="10" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#B45309">SV #3 (Class 0)</text>
    </g>
    <g transform="translate(180, 217)">
      <circle cx="6" cy="6" r="13" fill="none" stroke="#D97706" stroke-width="2.5"/>
      <rect x="0" y="0" width="12" height="12" fill="#B91C1C" rx="2"/>
      <text x="25" y="10" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#B45309">SV #4 (Class 0)</text>
    </g>
  </g>

  <!-- Inspection Panel -->
  <g transform="translate(565, 85)">
    <rect x="0" y="0" width="195" height="260" fill="#FFFBEB" rx="8" stroke="#FDE68A" stroke-width="1.5"/>
    <text x="16" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#92400E">Fitted Model Attributes</text>

    <text x="16" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#78350F">Scikit-Learn Inspection:</text>
    <rect x="12" y="60" width="171" height="58" rx="4" fill="#FFFFFF" stroke="#FDE68A"/>
    <text x="18" y="78" font-family="monospace" font-size="10" fill="#1E293B">clf.support_vectors_</text>
    <text x="18" y="94" font-family="monospace" font-size="10" fill="#1E293B">clf.support_</text>
    <text x="18" y="110" font-family="monospace" font-size="10" fill="#1E293B">clf.n_support_</text>

    <line x1="16" y1="130" x2="179" y2="130" stroke="#FDE68A"/>

    <text x="16" y="152" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#92400E">Critical Takeaway:</text>
    <text x="16" y="172" font-family="-apple-system, sans-serif" font-size="11" fill="#78350F">If you move or remove any</text>
    <text x="16" y="188" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#B45309">non-support vector</text>
    <text x="16" y="204" font-family="-apple-system, sans-serif" font-size="11" fill="#78350F">the hyperplane remains</text>
    <text x="16" y="220" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#059669">100% identical!</text>

    <rect x="12" y="232" width="171" height="20" rx="3" fill="#FEF3C7"/>
    <text x="97" y="246" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">Sparsity of Solution</text>
  </g>
</svg>"""

# 4. Narrow Margin vs Wider Margin (Figure 13.4)
SVG_NARROW_VS_WIDE_MARGIN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 360" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Narrow Margin vs. Wide Margin Generalization</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">A boundary with a tiny margin is vulnerable to test noise; a wide margin provides robust safety clearance</text>

  <!-- Left: Narrow Margin (High Risk) -->
  <g transform="translate(50, 90)">
    <rect x="0" y="0" width="330" height="230" fill="#FEF2F2" rx="8" stroke="#FECACA" stroke-width="1.5"/>
    <text x="16" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#991B1B">Narrow Margin (High Variance Risk)</text>
    
    <!-- Boundary passing very close to points -->
    <line x1="210" y1="40" x2="110" y2="210" stroke="#DC2626" stroke-width="2.5"/>
    <line x1="195" y1="40" x2="95" y2="210" stroke="#DC2626" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="225" y1="40" x2="125" y2="210" stroke="#DC2626" stroke-width="1" stroke-dasharray="3,3"/>

    <!-- Data Points hugging the line -->
    <circle cx="130" cy="90" r="6" fill="#2563EB"/>
    <circle cx="100" cy="140" r="6" fill="#2563EB"/>
    <circle cx="70" cy="80" r="6" fill="#2563EB"/>

    <rect x="180" y="140" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="220" y="90" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="250" y="170" width="12" height="12" fill="#DC2626" rx="2"/>

    <!-- New Test Point entering margin and misclassified -->
    <circle cx="160" cy="130" r="8" fill="#F59E0B" stroke="#B45309" stroke-width="2"/>
    <text x="175" y="125" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#B45309">Noisy Test Sample</text>
    <text x="175" y="138" font-family="-apple-system, sans-serif" font-size="10" fill="#DC2626">MISCLASSIFIED!</text>

    <rect x="12" y="195" width="306" height="24" rx="4" fill="#FEE2E2"/>
    <text x="165" y="211" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#991B1B" text-anchor="middle">Tiny clearance → Overfitting vulnerability</text>
  </g>

  <!-- Right: Wide Maximum Margin (Robust) -->
  <g transform="translate(420, 90)">
    <rect x="0" y="0" width="330" height="230" fill="#ECFDF5" rx="8" stroke="#A7F3D0" stroke-width="1.5"/>
    <text x="16" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#065F46">Maximum Wide Margin (Optimal Generalization)</text>

    <!-- Wide Margin Boundaries -->
    <polygon points="120,40 210,40 150,210 60,210" fill="#D1FAE5" opacity="0.6"/>
    <line x1="165" y1="40" x2="105" y2="210" stroke="#059669" stroke-width="3"/>
    <line x1="120" y1="40" x2="60" y2="210" stroke="#059669" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="210" y1="40" x2="150" y2="210" stroke="#059669" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Data Points with ample safety buffer -->
    <circle cx="60" cy="90" r="6" fill="#2563EB"/>
    <circle cx="40" cy="140" r="6" fill="#2563EB"/>
    <circle cx="30" cy="80" r="6" fill="#2563EB"/>

    <rect x="230" y="140" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="250" y="90" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="270" y="170" width="12" height="12" fill="#DC2626" rx="2"/>

    <!-- Test point successfully classified -->
    <circle cx="130" cy="130" r="8" fill="#F59E0B" stroke="#B45309" stroke-width="2"/>
    <text x="145" y="125" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#065F46">Noisy Test Sample</text>
    <text x="145" y="138" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#059669">Correctly Classified!</text>

    <rect x="12" y="195" width="306" height="24" rx="4" fill="#D1FAE5"/>
    <text x="165" y="211" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#065F46" text-anchor="middle">Wide safety buffer → Resilient to real-world noise</text>
  </g>
</svg>"""

# 5. Linear SVM on Linearly Separable Dataset (Figure 13.5)
SVG_LINEAR_SVM_SEPARABLE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Linear SVM on Linearly Separable Data</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">When data points have clean separation, canonical hard-margin conditions hold perfectly with zero violations</text>

  <!-- Plot Canvas -->
  <g transform="translate(60, 85)">
    <rect x="0" y="0" width="480" height="260" fill="#F8FAFC" rx="8" stroke="#CBD5E1" stroke-width="1.5"/>

    <!-- Margin Corridor -->
    <polygon points="180,0 300,0 160,260 40,260" fill="#EFF6FF" opacity="0.7"/>
    <line x1="240" y1="0" x2="100" y2="260" stroke="#2563EB" stroke-width="3"/>
    <line x1="180" y1="0" x2="40" y2="260" stroke="#059669" stroke-width="1.8" stroke-dasharray="5,4"/>
    <line x1="300" y1="0" x2="160" y2="260" stroke="#DC2626" stroke-width="1.8" stroke-dasharray="5,4"/>

    <!-- Class 1 Points (Passed) -->
    <circle cx="50" cy="40" r="6" fill="#2563EB"/>
    <circle cx="70" cy="90" r="6" fill="#2563EB"/>
    <circle cx="30" cy="140" r="6" fill="#2563EB"/>
    <circle cx="60" cy="200" r="6" fill="#2563EB"/>

    <!-- Support Vectors on positive margin -->
    <circle cx="140" cy="74" r="12" fill="none" stroke="#D97706" stroke-width="2"/>
    <circle cx="140" cy="74" r="6" fill="#2563EB"/>

    <circle cx="90" cy="167" r="12" fill="none" stroke="#D97706" stroke-width="2"/>
    <circle cx="90" cy="167" r="6" fill="#2563EB"/>

    <!-- Class 0 Points (Failed) -->
    <rect x="340" y="100" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="380" y="160" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="420" y="80" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="300" y="210" width="12" height="12" fill="#DC2626" rx="2"/>

    <!-- Support Vectors on negative margin -->
    <circle cx="251" cy="96" r="12" fill="none" stroke="#D97706" stroke-width="2"/>
    <rect x="245" y="90" width="12" height="12" fill="#DC2626" rx="2"/>

    <circle cx="201" cy="189" r="12" fill="none" stroke="#D97706" stroke-width="2"/>
    <rect x="195" y="183" width="12" height="12" fill="#DC2626" rx="2"/>

    <text x="235" y="245" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#2563EB">wᵀx + b = 0</text>
  </g>

  <!-- Side Properties Card -->
  <g transform="translate(565, 85)">
    <rect x="0" y="0" width="195" height="260" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="14" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A">Hard Margin Rules</text>

    <text x="14" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#334155">Constraint Satisfaction:</text>
    <rect x="12" y="60" width="171" height="42" rx="4" fill="#ECFDF5" stroke="#A7F3D0"/>
    <text x="97" y="78" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">yᵢ(wᵀxᵢ + b) ≥ 1</text>
    <text x="97" y="94" font-family="-apple-system, sans-serif" font-size="10" fill="#047857" text-anchor="middle">for all i = 1, ..., N</text>

    <text x="14" y="125" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Zero margin violations (ξᵢ = 0)</text>
    <text x="14" y="145" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Zero misclassifications</text>
    <text x="14" y="165" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Empty margin corridor</text>

    <line x1="14" y1="185" x2="181" y2="185" stroke="#E2E8F0"/>

    <rect x="12" y="200" width="171" height="48" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
    <text x="97" y="218" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">Fatal Weakness:</text>
    <text x="97" y="236" font-family="-apple-system, sans-serif" font-size="10" fill="#B91C1C" text-anchor="middle">Fails if even 1 outlier overlaps!</text>
  </g>
</svg>"""

# 6. Hard Margin vs Soft Margin (Figure 13.6)
SVG_HARD_VS_SOFT_MARGIN = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Hard Margin vs. Soft Margin: The Slack Variable (ξ)</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Soft margin SVM introduces slack variables ξᵢ ≥ 0 to tolerate realistic noise without model breakdown</text>

  <!-- Left: Hard Margin Breakdown on Noise -->
  <g transform="translate(50, 90)">
    <rect x="0" y="0" width="330" height="250" fill="#FEF2F2" rx="8" stroke="#FECACA" stroke-width="1.5"/>
    <text x="16" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#991B1B">Hard Margin Breakdown</text>

    <!-- Faint intended boundary -->
    <line x1="180" y1="40" x2="120" y2="210" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Data points -->
    <circle cx="80" cy="80" r="6" fill="#2563EB"/>
    <circle cx="60" cy="150" r="6" fill="#2563EB"/>
    <rect x="240" y="90" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="220" y="160" width="12" height="12" fill="#DC2626" rx="2"/>

    <!-- The 1 Outlier Intruder -->
    <circle cx="210" cy="110" r="7" fill="#2563EB" stroke="#DC2626" stroke-width="2"/>
    <text x="140" y="130" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#991B1B">Outlier Intruder!</text>

    <!-- Hard Margin Line Severely Distorted -->
    <line x1="235" y1="40" x2="215" y2="210" stroke="#DC2626" stroke-width="2.5"/>

    <rect x="12" y="200" width="306" height="38" rx="4" fill="#FEE2E2"/>
    <text x="165" y="216" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">No feasible solution exists, or line is</text>
    <text x="165" y="230" font-family="-apple-system, sans-serif" font-size="10" fill="#B91C1C" text-anchor="middle">catastrophically tilted by a single noisy point!</text>
  </g>

  <!-- Right: Soft Margin Tolerates Slack -->
  <g transform="translate(420, 90)">
    <rect x="0" y="0" width="330" height="250" fill="#EFF6FF" rx="8" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="16" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E40AF">Soft Margin (Slack Penalty C)</text>

    <!-- Robust Hyperplane and Margins -->
    <polygon points="120,40 210,40 150,210 60,210" fill="#DBEAFE" opacity="0.5"/>
    <line x1="165" y1="40" x2="105" y2="210" stroke="#2563EB" stroke-width="3"/>
    <line x1="120" y1="40" x2="60" y2="210" stroke="#059669" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="210" y1="40" x2="150" y2="210" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Data points -->
    <circle cx="80" cy="80" r="6" fill="#2563EB"/>
    <circle cx="60" cy="150" r="6" fill="#2563EB"/>
    <rect x="250" y="90" width="12" height="12" fill="#DC2626" rx="2"/>
    <rect x="230" y="160" width="12" height="12" fill="#DC2626" rx="2"/>

    <!-- Outlier with slack variable arrow -->
    <circle cx="180" cy="110" r="7" fill="#2563EB" stroke="#D97706" stroke-width="2"/>
    <line x1="180" y1="110" x2="100" y2="110" stroke="#D97706" stroke-width="2" stroke-dasharray="2,2"/>
    <rect x="135" y="94" width="45" height="18" rx="3" fill="#FFFBEB" stroke="#D97706"/>
    <text x="157" y="107" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">ξᵢ &gt; 1</text>

    <rect x="12" y="200" width="306" height="38" rx="4" fill="#DBEAFE"/>
    <text x="165" y="216" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">Min ( ½ ∥w∥² + C ∑ ξᵢ )</text>
    <text x="165" y="230" font-family="-apple-system, sans-serif" font-size="10" fill="#1D4ED8" text-anchor="middle">Maintains optimal wide boundary despite noise!</text>
  </g>
</svg>"""

# 7. Decision Boundaries for Multiple C Values (Figure 13.7)
SVG_C_PARAMETER_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 370" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Decision Boundaries &amp; Margins Across C Parameter</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">C controls the penalty for margin violations: Small C = Wide Margin; Large C = Narrow Margin</text>

  <!-- Panel 1: C = 0.1 -->
  <g transform="translate(40, 85)">
    <rect x="0" y="0" width="220" height="245" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="8" y="8" width="85" height="22" rx="4" fill="#EFF6FF" stroke="#BFDBFE"/>
    <text x="50" y="23" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1D4ED8" text-anchor="middle">C = 0.1 (Soft)</text>

    <!-- Very wide margin band -->
    <polygon points="50,40 180,40 140,190 10,190" fill="#EFF6FF" opacity="0.8"/>
    <line x1="115" y1="40" x2="75" y2="190" stroke="#2563EB" stroke-width="2.5"/>
    <line x1="50" y1="40" x2="10" y2="190" stroke="#2563EB" stroke-dasharray="3,3"/>
    <line x1="180" y1="40" x2="140" y2="190" stroke="#2563EB" stroke-dasharray="3,3"/>

    <!-- Points -->
    <circle cx="40" cy="70" r="5" fill="#2563EB"/>
    <circle cx="70" cy="110" r="5" fill="#2563EB" stroke="#F59E0B" stroke-width="2"/>
    <rect x="150" y="130" width="10" height="10" fill="#DC2626" rx="2" stroke="#F59E0B" stroke-width="2"/>
    <rect x="180" y="100" width="10" height="10" fill="#DC2626" rx="2"/>

    <text x="110" y="210" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">Wide Margin (78 SVs)</text>
    <text x="110" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">High tolerance for errors</text>
  </g>

  <!-- Panel 2: C = 1.0 (Balanced) -->
  <g transform="translate(290, 85)">
    <rect x="0" y="0" width="220" height="245" fill="#F8FAFC" rx="8" stroke="#3B82F6" stroke-width="2"/>
    <rect x="8" y="8" width="105" height="22" rx="4" fill="#DBEAFE" stroke="#60A5FA"/>
    <text x="60" y="23" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">C = 1.0 (Optimal)</text>

    <!-- Moderate margin band -->
    <polygon points="75,40 155,40 120,190 40,190" fill="#DBEAFE" opacity="0.8"/>
    <line x1="115" y1="40" x2="80" y2="190" stroke="#2563EB" stroke-width="2.5"/>
    <line x1="75" y1="40" x2="40" y2="190" stroke="#2563EB" stroke-dasharray="3,3"/>
    <line x1="155" y1="40" x2="120" y2="190" stroke="#2563EB" stroke-dasharray="3,3"/>

    <!-- Points -->
    <circle cx="40" cy="70" r="5" fill="#2563EB"/>
    <circle cx="72" cy="110" r="5" fill="#2563EB" stroke="#F59E0B" stroke-width="2"/>
    <rect x="150" y="130" width="10" height="10" fill="#DC2626" rx="2" stroke="#F59E0B" stroke-width="2"/>
    <rect x="180" y="100" width="10" height="10" fill="#DC2626" rx="2"/>

    <text x="110" y="210" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#1D4ED8" text-anchor="middle">Balanced Margin (32 SVs)</text>
    <text x="110" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Optimal Generalization</text>
  </g>

  <!-- Panel 3: C = 10.0 (Strict) -->
  <g transform="translate(540, 85)">
    <rect x="0" y="0" width="220" height="245" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="8" y="8" width="85" height="22" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
    <text x="50" y="23" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">C = 10.0 (Hard)</text>

    <!-- Very narrow margin band -->
    <polygon points="100,40 135,40 102,190 67,190" fill="#FEE2E2" opacity="0.8"/>
    <line x1="117" y1="40" x2="85" y2="190" stroke="#DC2626" stroke-width="2.5"/>
    <line x1="100" y1="40" x2="67" y2="190" stroke="#DC2626" stroke-dasharray="3,3"/>
    <line x1="135" y1="40" x2="102" y2="190" stroke="#DC2626" stroke-dasharray="3,3"/>

    <!-- Points -->
    <circle cx="40" cy="70" r="5" fill="#2563EB"/>
    <circle cx="70" cy="110" r="5" fill="#2563EB"/>
    <rect x="150" y="130" width="10" height="10" fill="#DC2626" rx="2"/>
    <rect x="180" y="100" width="10" height="10" fill="#DC2626" rx="2"/>

    <text x="110" y="210" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">Narrow Margin (23 SVs)</text>
    <text x="110" y="226" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Strict zero-violation penalty</text>
  </g>
</svg>"""

# 8. Kernel Comparison (Figure 13.8)
SVG_KERNEL_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 370" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Kernel Comparison on Concentric Non-Linear Dataset</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">A linear hyperplane fails on circular patterns; Polynomial and RBF kernels construct non-linear decision manifolds</text>

  <!-- Panel 1: Linear Kernel (Fails) -->
  <g transform="translate(40, 85)">
    <rect x="0" y="0" width="220" height="245" fill="#FEF2F2" rx="8" stroke="#FECACA" stroke-width="1.5"/>
    <rect x="8" y="8" width="95" height="22" rx="4" fill="#FEE2E2"/>
    <text x="55" y="23" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">Linear Kernel</text>

    <!-- Concentric points -->
    <!-- Inner Circle: Class 1 -->
    <circle cx="110" cy="115" r="5" fill="#2563EB"/>
    <circle cx="95" cy="105" r="5" fill="#2563EB"/>
    <circle cx="125" cy="105" r="5" fill="#2563EB"/>
    <circle cx="110" cy="130" r="5" fill="#2563EB"/>
    <!-- Outer Ring: Class 0 -->
    <rect x="50" y="60" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="160" y="60" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="40" y="150" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="170" y="150" width="9" height="9" fill="#DC2626" rx="2"/>

    <!-- Inadequate straight line -->
    <line x1="30" y1="50" x2="190" y2="180" stroke="#991B1B" stroke-width="2.5"/>

    <text x="110" y="208" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">Test Accuracy: 54.0%</text>
    <text x="110" y="224" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">Cannot separate circles</text>
  </g>

  <!-- Panel 2: Polynomial Kernel (Degree 2) -->
  <g transform="translate(290, 85)">
    <rect x="0" y="0" width="220" height="245" fill="#F0FDF4" rx="8" stroke="#BBF7D0" stroke-width="1.5"/>
    <rect x="8" y="8" width="115" height="22" rx="4" fill="#DCFCE7"/>
    <text x="65" y="23" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">Polynomial (d=2)</text>

    <!-- Concentric points -->
    <circle cx="110" cy="115" r="5" fill="#2563EB"/>
    <circle cx="95" cy="105" r="5" fill="#2563EB"/>
    <circle cx="125" cy="105" r="5" fill="#2563EB"/>
    <circle cx="110" cy="130" r="5" fill="#2563EB"/>
    <rect x="50" y="60" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="160" y="60" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="40" y="150" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="170" y="150" width="9" height="9" fill="#DC2626" rx="2"/>

    <!-- Elliptical boundary -->
    <ellipse cx="110" cy="115" rx="38" ry="32" fill="none" stroke="#16A34A" stroke-width="2.5"/>

    <text x="110" y="208" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">Test Accuracy: 100.0%</text>
    <text x="110" y="224" font-family="-apple-system, sans-serif" font-size="10" fill="#15803D" text-anchor="middle">Captures quadratic terms</text>
  </g>

  <!-- Panel 3: RBF Kernel (Radial Basis) -->
  <g transform="translate(540, 85)">
    <rect x="0" y="0" width="220" height="245" fill="#EFF6FF" rx="8" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect x="8" y="8" width="105" height="22" rx="4" fill="#DBEAFE"/>
    <text x="60" y="23" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">RBF Kernel (γ=1)</text>

    <!-- Concentric points -->
    <circle cx="110" cy="115" r="5" fill="#2563EB"/>
    <circle cx="95" cy="105" r="5" fill="#2563EB"/>
    <circle cx="125" cy="105" r="5" fill="#2563EB"/>
    <circle cx="110" cy="130" r="5" fill="#2563EB"/>
    <rect x="50" y="60" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="160" y="60" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="40" y="150" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="170" y="150" width="9" height="9" fill="#DC2626" rx="2"/>

    <!-- Smooth radial contour -->
    <circle cx="110" cy="115" r="35" fill="none" stroke="#2563EB" stroke-width="2.5"/>

    <text x="110" y="208" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">Test Accuracy: 100.0%</text>
    <text x="110" y="224" font-family="-apple-system, sans-serif" font-size="10" fill="#1D4ED8" text-anchor="middle">Smooth infinite-dim similarity</text>
  </g>
</svg>"""

# 9. RBF Gamma Comparison (Figure 13.9)
SVG_RBF_GAMMA_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 370" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">RBF Gamma Parameter (γ): Radius of Point Influence</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Small γ gives points wide reach (smooth boundary); Large γ gives points tiny reach (island overfitting)</text>

  <!-- Panel 1: gamma = 0.1 -->
  <g transform="translate(40, 85)">
    <rect x="0" y="0" width="220" height="245" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="8" y="8" width="90" height="22" rx="4" fill="#EFF6FF" stroke="#BFDBFE"/>
    <text x="53" y="23" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1D4ED8" text-anchor="middle">γ = 0.1 (Broad)</text>

    <!-- Broad smooth boundary -->
    <path d="M 40,50 Q 110,80 180,50 L 180,180 L 40,180 Z" fill="#EFF6FF" opacity="0.6"/>
    <path d="M 40,50 Q 110,80 180,50" fill="none" stroke="#2563EB" stroke-width="2.5"/>

    <circle cx="80" cy="110" r="5" fill="#2563EB"/>
    <circle cx="140" cy="120" r="5" fill="#2563EB"/>
    <rect x="70" y="35" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="150" y="35" width="9" height="9" fill="#DC2626" rx="2"/>

    <text x="110" y="208" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">Broad Influence (79 SVs)</text>
    <text x="110" y="224" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Smooth, high bias tendency</text>
  </g>

  <!-- Panel 2: gamma = 1.0 (Optimal) -->
  <g transform="translate(290, 85)">
    <rect x="0" y="0" width="220" height="245" fill="#F8FAFC" rx="8" stroke="#3B82F6" stroke-width="2"/>
    <rect x="8" y="8" width="105" height="22" rx="4" fill="#DBEAFE" stroke="#60A5FA"/>
    <text x="60" y="23" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">γ = 1.0 (Optimal)</text>

    <!-- Well contoured boundary -->
    <ellipse cx="110" cy="115" rx="55" ry="40" fill="#DBEAFE" opacity="0.6"/>
    <ellipse cx="110" cy="115" rx="55" ry="40" fill="none" stroke="#2563EB" stroke-width="2.5"/>

    <circle cx="85" cy="110" r="5" fill="#2563EB"/>
    <circle cx="135" cy="115" r="5" fill="#2563EB"/>
    <rect x="40" y="55" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="170" y="55" width="9" height="9" fill="#DC2626" rx="2"/>

    <text x="110" y="208" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1D4ED8" text-anchor="middle">Well-Tuned (37 SVs)</text>
    <text x="110" y="224" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Ideal generalization balance</text>
  </g>

  <!-- Panel 3: gamma = 10.0 (Overfitting) -->
  <g transform="translate(540, 85)">
    <rect x="0" y="0" width="220" height="245" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="8" y="8" width="95" height="22" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
    <text x="55" y="23" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">γ = 10.0 (Tight)</text>

    <!-- Isolated tight boundary pockets (islands) -->
    <circle cx="85" cy="110" r="16" fill="#FEE2E2" stroke="#DC2626" stroke-width="2"/>
    <circle cx="135" cy="115" r="16" fill="#FEE2E2" stroke="#DC2626" stroke-width="2"/>

    <circle cx="85" cy="110" r="5" fill="#2563EB"/>
    <circle cx="135" cy="115" r="5" fill="#2563EB"/>
    <rect x="40" y="55" width="9" height="9" fill="#DC2626" rx="2"/>
    <rect x="170" y="55" width="9" height="9" fill="#DC2626" rx="2"/>

    <text x="110" y="208" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">Island Pockets (89 SVs)</text>
    <text x="110" y="224" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">Severe Overfitting / High Variance</text>
  </g>
</svg>"""

# 10. Feature Scaling Effect (Figure 13.10)
SVG_FEATURE_SCALING_EFFECT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 370" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Before vs. After Feature Scaling in SVM</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Distance-based Euclidean metrics are completely distorted by unscaled features with large numerical magnitudes</text>

  <!-- Left: Unscaled (Distorted Aspect Ratio) -->
  <g transform="translate(50, 90)">
    <rect x="0" y="0" width="330" height="240" fill="#FEF2F2" rx="8" stroke="#FECACA" stroke-width="1.5"/>
    <text x="16" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#991B1B">Unscaled Features (Income $100k vs Age 40)</text>

    <!-- Heavily skewed ellipse/aspect ratio -->
    <ellipse cx="165" cy="110" rx="120" ry="25" fill="#FEE2E2" opacity="0.6"/>
    <!-- Distorted horizontal boundary line -->
    <line x1="30" y1="110" x2="300" y2="110" stroke="#DC2626" stroke-width="2.5"/>

    <circle cx="120" cy="95" r="5" fill="#2563EB"/>
    <circle cx="210" cy="95" r="5" fill="#2563EB"/>
    <rect x="120" y="125" width="10" height="10" fill="#DC2626" rx="2"/>
    <rect x="210" y="125" width="10" height="10" fill="#DC2626" rx="2"/>

    <text x="165" y="165" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">Income completely dominates Euclidean distance (Δ=30,000)</text>
    <text x="165" y="180" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">Age differences (Δ=15) are ignored as zero!</text>

    <rect x="12" y="198" width="306" height="28" rx="4" fill="#FEE2E2"/>
    <text x="165" y="216" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">Test Accuracy: 88.0% | 44 Support Vectors</text>
  </g>

  <!-- Right: Standardized (Isotropic Balanced Geometry) -->
  <g transform="translate(420, 90)">
    <rect x="0" y="0" width="330" height="240" fill="#ECFDF5" rx="8" stroke="#A7F3D0" stroke-width="1.5"/>
    <text x="16" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#065F46">StandardScaler Applied (μ=0, σ=1)</text>

    <!-- Balanced circular symmetry -->
    <circle cx="165" cy="110" r="55" fill="#D1FAE5" opacity="0.6"/>
    <line x1="120" y1="50" x2="210" y2="170" stroke="#059669" stroke-width="3"/>
    <line x1="85" y1="75" x2="175" y2="195" stroke="#059669" stroke-dasharray="3,3"/>
    <line x1="155" y1="25" x2="245" y2="145" stroke="#059669" stroke-dasharray="3,3"/>

    <circle cx="110" cy="90" r="5" fill="#2563EB"/>
    <circle cx="130" cy="130" r="5" fill="#2563EB"/>
    <rect x="190" y="85" width="10" height="10" fill="#DC2626" rx="2"/>
    <rect x="210" y="125" width="10" height="10" fill="#DC2626" rx="2"/>

    <text x="165" y="172" font-family="-apple-system, sans-serif" font-size="10" fill="#065F46" text-anchor="middle">Both features exert equal mathematical weight</text>

    <rect x="12" y="198" width="306" height="28" rx="4" fill="#D1FAE5"/>
    <text x="165" y="216" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">Test Accuracy: 100.0% | 20 Support Vectors</text>
  </g>
</svg>"""

# 11. Training vs Validation Performance (Figure 13.11)
SVG_TRAIN_VAL_PERFORMANCE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Training vs. Validation Accuracy Across C Candidates</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Hyperparameter selection performed strictly on training data via 5-Fold Cross-Validation</text>

  <!-- Chart Canvas -->
  <g transform="translate(60, 90)">
    <rect x="0" y="0" width="480" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>

    <!-- Horizontal grid lines -->
    <line x1="0" y1="50" x2="480" y2="50" stroke="#E2E8F0" stroke-dasharray="3,3"/>
    <line x1="0" y1="100" x2="480" y2="100" stroke="#E2E8F0" stroke-dasharray="3,3"/>
    <line x1="0" y1="150" x2="480" y2="150" stroke="#E2E8F0" stroke-dasharray="3,3"/>
    <line x1="0" y1="200" x2="480" y2="200" stroke="#E2E8F0" stroke-dasharray="3,3"/>

    <!-- Y-axis labels -->
    <text x="-10" y="54" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="end">98%</text>
    <text x="-10" y="104" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="end">95%</text>
    <text x="-10" y="154" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="end">90%</text>
    <text x="-10" y="204" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="end">80%</text>

    <!-- X-axis points: C = 0.01 (40), 0.1 (130), 1.0 (230), 10.0 (330), 100.0 (430) -->
    <!-- Validation Curve (Green) -->
    <!-- 0.01: 77.9% (210), 0.1: 97.4% (60), 1.0: 96.9% (68), 10.0: 95.8% (85), 100: 95.3% (93) -->
    <polyline points="40,210 130,60 230,68 330,85 430,93" fill="none" stroke="#059669" stroke-width="3"/>
    
    <!-- Training Curve (Blue) -->
    <!-- 0.01: 78.5% (205), 0.1: 97.4% (60), 1.0: 98.4% (45), 10.0: 99.5% (28), 100: 100% (20) -->
    <polyline points="40,205 130,60 230,45 330,28 430,20" fill="none" stroke="#2563EB" stroke-width="2.5" stroke-dasharray="5,4"/>

    <!-- Data markers -->
    <!-- Peak Validation C = 0.1 -->
    <circle cx="130" cy="60" r="7" fill="#059669" stroke="#FFFFFF" stroke-width="2"/>
    <rect x="90" y="25" width="80" height="24" rx="4" fill="#ECFDF5" stroke="#059669"/>
    <text x="130" y="41" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#065F46" text-anchor="middle">Peak CV: 97.4%</text>

    <circle cx="40" cy="210" r="5" fill="#059669"/>
    <circle cx="230" cy="68" r="5" fill="#059669"/>
    <circle cx="330" cy="85" r="5" fill="#059669"/>
    <circle cx="430" cy="93" r="5" fill="#059669"/>

    <!-- X-axis ticks -->
    <text x="40" y="240" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">C = 0.01</text>
    <text x="130" y="240" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#059669" text-anchor="middle">C = 0.1</text>
    <text x="230" y="240" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">C = 1.0</text>
    <text x="330" y="240" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">C = 10.0</text>
    <text x="430" y="240" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">C = 100.0</text>
  </g>

  <!-- Legend Panel -->
  <g transform="translate(565, 90)">
    <rect x="0" y="0" width="195" height="250" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="14" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A">Model Tuning Key</text>

    <line x1="14" y1="50" x2="38" y2="50" stroke="#059669" stroke-width="3"/>
    <text x="45" y="54" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#065F46">5-Fold CV Validation</text>

    <line x1="14" y1="75" x2="38" y2="75" stroke="#2563EB" stroke-width="2.5" stroke-dasharray="4,3"/>
    <text x="45" y="79" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#1E40AF">Training Accuracy</text>

    <line x1="14" y1="95" x2="181" y2="95" stroke="#E2E8F0"/>

    <text x="14" y="118" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155">Overfitting Region:</text>
    <text x="14" y="136" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">For C &gt; 10, training reaches</text>
    <text x="14" y="152" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#2563EB">100%</text>
    <text x="48" y="152" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">while validation drops,</text>
    <text x="14" y="168" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">signaling overfitting.</text>

    <rect x="12" y="185" width="171" height="50" rx="4" fill="#EFF6FF" stroke="#BFDBFE"/>
    <text x="97" y="202" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">Selected: C = 0.1 to 1.0</text>
    <text x="97" y="218" font-family="-apple-system, sans-serif" font-size="10" fill="#1D4ED8" text-anchor="middle">Optimal Generalization</text>
    <text x="97" y="230" font-family="-apple-system, sans-serif" font-size="9" fill="#2563EB" text-anchor="middle">Test set kept untouched!</text>
  </g>
</svg>"""

# 12. Class Distribution (Figure 13.12)
SVG_CLASS_DISTRIBUTION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 320" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Admissions Dataset: Target Class Distribution</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Balanced binary dataset of N = 240 university applicant records (120 Admitted vs. 120 Rejected)</text>

  <!-- Horizontal Bars Canvas -->
  <g transform="translate(60, 90)">
    <rect x="0" y="0" width="680" height="190" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>

    <!-- Bar 1: Class 0 (Rejected) -->
    <text x="30" y="62" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#991B1B">Class 0: Rejected</text>
    <rect x="160" y="44" width="360" height="28" rx="6" fill="#DC2626"/>
    <text x="530" y="63" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A">120 (50.0%)</text>
    <text x="175" y="63" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">Train: 96 | Holdout Test: 24</text>

    <!-- Bar 2: Class 1 (Admitted) -->
    <text x="30" y="122" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Class 1: Admitted</text>
    <rect x="160" y="104" width="360" height="28" rx="6" fill="#2563EB"/>
    <text x="530" y="123" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A">120 (50.0%)</text>
    <text x="175" y="123" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">Train: 96 | Holdout Test: 24</text>

    <!-- Bottom summary note -->
    <rect x="30" y="152" width="620" height="24" rx="4" fill="#EFF6FF"/>
    <text x="340" y="168" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#1E40AF" text-anchor="middle">✓ Stratified 80/20 train/test split preserves exact 50/50 balance in both partitions</text>
  </g>
</svg>"""

# 13. Confusion Matrix Heatmap (Figure 13.13)
SVG_CONFUSION_MATRIX_HEATMAP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 390" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Holdout Test Set Confusion Matrix (N = 48)</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Performance on held-out test data: Accuracy = 91.7%, Precision = 88.5%, Recall = 95.8%, F1 = 92.0%</text>

  <!-- 2x2 Heatmap Canvas -->
  <g transform="translate(100, 95)">
    <!-- Column Headers -->
    <text x="175" y="18" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Predicted: Rejected (0)</text>
    <text x="325" y="18" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">Predicted: Admitted (1)</text>

    <!-- Row Headers -->
    <text x="90" y="80" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="end">Actual: Rejected</text>
    <text x="90" y="170" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="end">Actual: Admitted</text>

    <!-- Quadrant 1: True Negative (TN) -->
    <rect x="105" y="35" width="140" height="85" fill="#D1FAE5" rx="6" stroke="#A7F3D0" stroke-width="2"/>
    <text x="175" y="68" font-family="-apple-system, sans-serif" font-size="24" font-weight="800" fill="#065F46" text-anchor="middle">21</text>
    <text x="175" y="90" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">True Negative (TN)</text>
    <text x="175" y="105" font-family="-apple-system, sans-serif" font-size="10" fill="#059669" text-anchor="middle">Correct Rejections</text>

    <!-- Quadrant 2: False Positive (FP) -->
    <rect x="255" y="35" width="140" height="85" fill="#FEE2E2" rx="6" stroke="#FECACA" stroke-width="2"/>
    <text x="325" y="68" font-family="-apple-system, sans-serif" font-size="24" font-weight="800" fill="#991B1B" text-anchor="middle">3</text>
    <text x="325" y="90" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">False Positive (FP)</text>
    <text x="325" y="105" font-family="-apple-system, sans-serif" font-size="10" fill="#DC2626" text-anchor="middle">Type I Error</text>

    <!-- Quadrant 3: False Negative (FN) -->
    <rect x="105" y="130" width="140" height="85" fill="#FEF3C7" rx="6" stroke="#FDE68A" stroke-width="2"/>
    <text x="175" y="163" font-family="-apple-system, sans-serif" font-size="24" font-weight="800" fill="#92400E" text-anchor="middle">1</text>
    <text x="175" y="185" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#B45309" text-anchor="middle">False Negative (FN)</text>
    <text x="175" y="200" font-family="-apple-system, sans-serif" font-size="10" fill="#D97706" text-anchor="middle">Type II Error</text>

    <!-- Quadrant 4: True Positive (TP) -->
    <rect x="255" y="130" width="140" height="85" fill="#DBEAFE" rx="6" stroke="#BFDBFE" stroke-width="2"/>
    <text x="325" y="163" font-family="-apple-system, sans-serif" font-size="24" font-weight="800" fill="#1E40AF" text-anchor="middle">23</text>
    <text x="325" y="185" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1D4ED8" text-anchor="middle">True Positive (TP)</text>
    <text x="325" y="200" font-family="-apple-system, sans-serif" font-size="10" fill="#2563EB" text-anchor="middle">Correct Admissions</text>
  </g>

  <!-- Side Metrics Calculation Card -->
  <g transform="translate(530, 95)">
    <rect x="0" y="0" width="230" height="235" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="16" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A">Derived Metrics Walkthrough</text>

    <text x="16" y="52" font-family="-apple-system, sans-serif" font-size="11" fill="#334155"><tspan font-weight="700">Accuracy:</tspan> (21+23)/48 = <tspan font-weight="700" fill="#059669">91.67%</tspan></text>
    <text x="16" y="74" font-family="-apple-system, sans-serif" font-size="11" fill="#334155"><tspan font-weight="700">Precision:</tspan> 23/(23+3) = <tspan font-weight="700" fill="#2563EB">88.46%</tspan></text>
    <text x="16" y="96" font-family="-apple-system, sans-serif" font-size="11" fill="#334155"><tspan font-weight="700">Recall:</tspan> 23/(23+1) = <tspan font-weight="700" fill="#D97706">95.83%</tspan></text>
    <text x="16" y="118" font-family="-apple-system, sans-serif" font-size="11" fill="#334155"><tspan font-weight="700">F1-Score:</tspan> 2*(P*R)/(P+R) = <tspan font-weight="700" fill="#7C3AED">92.00%</tspan></text>

    <line x1="16" y1="135" x2="214" y2="135" stroke="#E2E8F0"/>

    <text x="16" y="156" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Takeaway:</text>
    <text x="16" y="174" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">The model missed only 1 actual</text>
    <text x="16" y="190" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">admitted applicant (95.8% Recall),</text>
    <text x="16" y="206" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">demonstrating excellent screening.</text>
  </g>
</svg>"""

# 14. Support Vector Regression (Figure 13.14)
SVG_SVR_REGRESSION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 390" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Support Vector Regression (SVR): The ε-Insensitive Tube</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">SVR ignores errors inside the tube (|y - f(x)| ≤ ε); only points lying on or outside the tube become support vectors</text>

  <!-- Plot Canvas -->
  <g transform="translate(60, 90)">
    <rect x="0" y="0" width="480" height="260" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>

    <!-- Grid lines -->
    <line x1="0" y1="65" x2="480" y2="65" stroke="#E2E8F0" stroke-dasharray="3,3"/>
    <line x1="0" y1="130" x2="480" y2="130" stroke="#E2E8F0" stroke-dasharray="3,3"/>
    <line x1="0" y1="195" x2="480" y2="195" stroke="#E2E8F0" stroke-dasharray="3,3"/>

    <!-- Epsilon Tube Band -->
    <!-- Non-linear curve: starts high left, drops smoothly, levels off -->
    <path d="M 40,40 Q 200,160 440,210 L 440,240 Q 200,190 40,70 Z" fill="#EFF6FF" opacity="0.8"/>
    
    <!-- Central Regression Curve f(x) -->
    <path d="M 40,55 Q 200,175 440,225" fill="none" stroke="#2563EB" stroke-width="3"/>

    <!-- Upper Boundary: f(x) + epsilon -->
    <path d="M 40,40 Q 200,160 440,210" fill="none" stroke="#059669" stroke-width="1.8" stroke-dasharray="5,4"/>
    <text x="350" y="195" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#059669">f(x) + ε</text>

    <!-- Lower Boundary: f(x) - epsilon -->
    <path d="M 40,70 Q 200,190 440,240" fill="none" stroke="#059669" stroke-width="1.8" stroke-dasharray="5,4"/>
    <text x="350" y="255" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#059669">f(x) - ε</text>

    <!-- Points Inside Tube (Zero Loss, Not Support Vectors) -->
    <circle cx="90" cy="80" r="5" fill="#94A3B8"/>
    <circle cx="150" cy="120" r="5" fill="#94A3B8"/>
    <circle cx="230" cy="180" r="5" fill="#94A3B8"/>
    <circle cx="310" cy="205" r="5" fill="#94A3B8"/>
    <circle cx="380" cy="220" r="5" fill="#94A3B8"/>

    <!-- Points Outside Tube (Penalized Support Vectors) with Slack Arrow -->
    <!-- Upper Violator -->
    <g transform="translate(180, 85)">
      <circle cx="0" cy="0" r="11" fill="none" stroke="#DC2626" stroke-width="2"/>
      <circle cx="0" cy="0" r="5" fill="#DC2626"/>
      <line x1="0" y1="0" x2="0" y2="60" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="2,2"/>
      <text x="15" y="-2" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#DC2626">Slack ξᵢ</text>
    </g>

    <!-- Lower Violator -->
    <g transform="translate(260, 245)">
      <circle cx="0" cy="0" r="11" fill="none" stroke="#DC2626" stroke-width="2"/>
      <circle cx="0" cy="0" r="5" fill="#DC2626"/>
      <line x1="0" y1="0" x2="0" y2="-40" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="2,2"/>
      <text x="15" y="8" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#DC2626">Slack ξᵢ*</text>
    </g>

    <!-- Tube width label -->
    <line x1="120" y1="65" x2="120" y2="95" stroke="#4F46E5" stroke-width="2"/>
    <text x="130" y="84" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#4F46E5">Width = 2ε</text>
  </g>

  <!-- Side Legend Panel -->
  <g transform="translate(565, 90)">
    <rect x="0" y="0" width="195" height="260" fill="#F8FAFC" rx="8" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="14" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A">SVR Epsilon Tube</text>

    <rect x="12" y="42" width="171" height="52" rx="4" fill="#EFF6FF" stroke="#BFDBFE"/>
    <text x="97" y="60" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">Loss Function Lε:</text>
    <text x="97" y="80" font-family="-apple-system, sans-serif" font-size="11" fill="#1D4ED8" text-anchor="middle">0 if |y - f(x)| ≤ ε</text>

    <text x="14" y="115" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155">Engine MPG Lab:</text>
    <text x="14" y="135" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Holdout MAE: 1.37 MPG</text>
    <text x="14" y="152" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Holdout RMSE: 1.80 MPG</text>
    <text x="14" y="169" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• 27 / 60 Support Vectors</text>

    <line x1="14" y1="185" x2="181" y2="185" stroke="#E2E8F0"/>

    <text x="14" y="205" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#059669">Key Distinction:</text>
    <text x="14" y="222" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">In SVC, SVs are near boundary.</text>
    <text x="14" y="238" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">In SVR, SVs are outside tube!</text>
  </g>
</svg>"""

# 15. Complete SVM Workflow Flowchart (Figure 13.15)
SVG_SVM_WORKFLOW = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title -->
  <text x="40" y="38" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">The End-to-End SVM Machine Learning Pipeline</text>
  <text x="40" y="62" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Leakage-free protocol: preprocessing, scaling, cross-validation hyperparameter selection, and holdout evaluation</text>

  <!-- Flowchart Steps -->
  <g transform="translate(30, 95)">
    <!-- Step 1: Data & Stratified Split -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="130" height="130" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
      <circle cx="22" cy="22" r="12" fill="#2563EB"/>
      <text x="22" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">1</text>
      <text x="14" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Data Split</text>
      <text x="14" y="75" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">• 80% Training</text>
      <text x="14" y="90" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">• 20% Holdout Test</text>
      <text x="14" y="105" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#059669">• Stratify target!</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 135,65 L 148,65" stroke="#94A3B8" stroke-width="2" marker-end="url(#arrow)"/>

    <!-- Step 2: Scaling in Pipeline -->
    <g transform="translate(152, 0)">
      <rect x="0" y="0" width="130" height="130" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
      <circle cx="22" cy="22" r="12" fill="#059669"/>
      <text x="22" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">2</text>
      <text x="14" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#065F46">StandardScaler</text>
      <text x="14" y="75" font-family="-apple-system, sans-serif" font-size="10" fill="#15803D">• Fit on train only!</text>
      <text x="14" y="90" font-family="-apple-system, sans-serif" font-size="10" fill="#15803D">• μ = 0, σ = 1</text>
      <text x="14" y="105" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#047857">• Zero data leak</text>
    </g>

    <!-- Arrow 2 -->
    <path d="M 287,65 L 300,65" stroke="#94A3B8" stroke-width="2"/>

    <!-- Step 3: Kernel & Model Setup -->
    <g transform="translate(304, 0)">
      <rect x="0" y="0" width="130" height="130" rx="8" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
      <circle cx="22" cy="22" r="12" fill="#2563EB"/>
      <text x="22" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">3</text>
      <text x="14" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#1E40AF">Kernel Choice</text>
      <text x="14" y="75" font-family="-apple-system, sans-serif" font-size="10" fill="#1D4ED8">• Linear: Simple/fast</text>
      <text x="14" y="90" font-family="-apple-system, sans-serif" font-size="10" fill="#1D4ED8">• RBF: Non-linear</text>
      <text x="14" y="105" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#1E40AF">• Poly: Interactions</text>
    </g>

    <!-- Arrow 3 -->
    <path d="M 439,65 L 452,65" stroke="#94A3B8" stroke-width="2"/>

    <!-- Step 4: 5-Fold CV Tuning -->
    <g transform="translate(456, 0)">
      <rect x="0" y="0" width="130" height="130" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
      <circle cx="22" cy="22" r="12" fill="#D97706"/>
      <text x="22" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">4</text>
      <text x="14" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#92400E">5-Fold CV Tuning</text>
      <text x="14" y="75" font-family="-apple-system, sans-serif" font-size="10" fill="#78350F">• Tune C &amp; γ</text>
      <text x="14" y="90" font-family="-apple-system, sans-serif" font-size="10" fill="#78350F">• Strictly on train!</text>
      <text x="14" y="105" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#B45309">• Best: C = 0.1 to 1</text>
    </g>

    <!-- Arrow 4 -->
    <path d="M 591,65 L 604,65" stroke="#94A3B8" stroke-width="2"/>

    <!-- Step 5: Final Holdout Test -->
    <g transform="translate(608, 0)">
      <rect x="0" y="0" width="130" height="130" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
      <circle cx="22" cy="22" r="12" fill="#7C3AED"/>
      <text x="22" y="26" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">5</text>
      <text x="14" y="55" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#6B21A8">Holdout Test</text>
      <text x="14" y="75" font-family="-apple-system, sans-serif" font-size="10" fill="#581C87">• Accuracy: 91.7%</text>
      <text x="14" y="90" font-family="-apple-system, sans-serif" font-size="10" fill="#581C87">• Precision: 88.5%</text>
      <text x="14" y="105" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#7C3AED">• F1-Score: 92.0%</text>
    </g>
  </g>

  <!-- Bottom Verification Badge -->
  <rect x="70" y="245" width="660" height="26" rx="6" fill="#F1F5F9" stroke="#E2E8F0"/>
  <text x="400" y="262" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#334155" text-anchor="middle">✓ End-to-end Pipeline guarantees test data is evaluated once and remains completely unseen during training</text>
</svg>"""

SVG_LIST = [
    ("SVG_TWO_CLASS_HYPERPLANE", SVG_TWO_CLASS_HYPERPLANE),
    ("SVG_MAXIMUM_MARGIN", SVG_MAXIMUM_MARGIN),
    ("SVG_ACTUAL_SUPPORT_VECTORS", SVG_ACTUAL_SUPPORT_VECTORS),
    ("SVG_NARROW_VS_WIDE_MARGIN", SVG_NARROW_VS_WIDE_MARGIN),
    ("SVG_LINEAR_SVM_SEPARABLE", SVG_LINEAR_SVM_SEPARABLE),
    ("SVG_HARD_VS_SOFT_MARGIN", SVG_HARD_VS_SOFT_MARGIN),
    ("SVG_C_PARAMETER_COMPARISON", SVG_C_PARAMETER_COMPARISON),
    ("SVG_KERNEL_COMPARISON", SVG_KERNEL_COMPARISON),
    ("SVG_RBF_GAMMA_COMPARISON", SVG_RBF_GAMMA_COMPARISON),
    ("SVG_FEATURE_SCALING_EFFECT", SVG_FEATURE_SCALING_EFFECT),
    ("SVG_TRAIN_VAL_PERFORMANCE", SVG_TRAIN_VAL_PERFORMANCE),
    ("SVG_CLASS_DISTRIBUTION", SVG_CLASS_DISTRIBUTION),
    ("SVG_CONFUSION_MATRIX_HEATMAP", SVG_CONFUSION_MATRIX_HEATMAP),
    ("SVG_SVR_REGRESSION", SVG_SVR_REGRESSION),
    ("SVG_SVM_WORKFLOW", SVG_SVM_WORKFLOW)
]

if __name__ == "__main__":
    print(f"Validating {len(SVG_LIST)} SVGs via xml.etree.ElementTree...")
    for name, svg_str in SVG_LIST:
        try:
            elem = ET.fromstring(svg_str)
            print(f"  [PASS] {name} parsed successfully ({elem.tag})")
        except Exception as e:
            print(f"  [FAIL] {name}: {e}")
            raise e
    print("ALL 15 SVGs VALIDATED CLEANLY!")
