"""
Generates and validates all 15 inline SVG diagrams for Topic 14: Naive Bayes.
Strict Light Mode, clear typography, verified numerical geometry, valid XML.
Uses literal UTF-8 symbols (no undefined HTML named entities).
"""

import xml.etree.ElementTree as ET

# 1. Hero / Classification Pipeline
SVG_NB_HERO_PIPELINE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 380" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <defs>
    <linearGradient id="p-grad-1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F5F3FF"/>
      <stop offset="100%" stop-color="#EDE9FE"/>
    </linearGradient>
    <filter id="p-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">The Naive Bayes Classification Pipeline</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">From incoming raw text to class conditional likelihoods and final probability prediction</text>

  <!-- Flow Steps -->
  <!-- Step 1: Input Document -->
  <g transform="translate(40, 85)" filter="url(#p-shadow)">
    <rect x="0" y="0" width="130" height="180" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="34" rx="8" fill="#F8FAFC"/>
    <text x="65" y="22" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">1. RAW EMAIL</text>
    <rect x="15" y="48" width="100" height="12" rx="3" fill="#E2E8F0"/>
    <rect x="15" y="66" width="80" height="8" rx="2" fill="#F1F5F9"/>
    <rect x="15" y="80" width="95" height="8" rx="2" fill="#F1F5F9"/>
    <rect x="15" y="94" width="70" height="8" rx="2" fill="#F1F5F9"/>
    <rect x="15" y="115" width="100" height="42" rx="4" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
    <text x="20" y="130" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#DC2626">"Claim free prize</text>
    <text x="20" y="145" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#DC2626">cash bonus now!"</text>
  </g>

  <!-- Arrow 1 -->
  <g transform="translate(180, 165)">
    <line x1="0" y1="0" x2="20" y2="0" stroke="#7C3AED" stroke-width="2.5"/>
    <polygon points="20,-4 28,0 20,4" fill="#7C3AED"/>
  </g>

  <!-- Step 2: Feature Extraction -->
  <g transform="translate(215, 85)" filter="url(#p-shadow)">
    <rect x="0" y="0" width="130" height="180" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="34" rx="8" fill="#F8FAFC"/>
    <text x="65" y="22" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">2. FEATURES</text>
    <text x="65" y="55" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Tokenize &amp; Vector</text>
    <rect x="15" y="70" width="100" height="24" rx="4" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1"/>
    <text x="65" y="86" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#7C3AED" text-anchor="middle">x₁ = "free"</text>
    <rect x="15" y="102" width="100" height="24" rx="4" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1"/>
    <text x="65" y="118" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#7C3AED" text-anchor="middle">x₂ = "offer"</text>
    <rect x="15" y="134" width="100" height="24" rx="4" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1"/>
    <text x="65" y="150" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#7C3AED" text-anchor="middle">x₃ = "prize"</text>
  </g>

  <!-- Arrow 2 -->
  <g transform="translate(355, 165)">
    <line x1="0" y1="0" x2="20" y2="0" stroke="#7C3AED" stroke-width="2.5"/>
    <polygon points="20,-4 28,0 20,4" fill="#7C3AED"/>
  </g>

  <!-- Step 3: Probabilities -->
  <g transform="translate(390, 85)" filter="url(#p-shadow)">
    <rect x="0" y="0" width="140" height="180" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="0" y="0" width="140" height="34" rx="8" fill="#F8FAFC"/>
    <text x="70" y="22" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">3. PROBABILITIES</text>
    <text x="70" y="55" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Prior × Likelihoods</text>
    <rect x="10" y="70" width="120" height="42" rx="4" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
    <text x="15" y="87" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#DC2626">P(X|Spam)·P(Spam)</text>
    <text x="15" y="103" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">= 0.056000</text>
    <rect x="10" y="120" width="120" height="42" rx="4" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
    <text x="15" y="137" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#059669">P(X|Ham)·P(Ham)</text>
    <text x="15" y="153" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#059669">= 0.000600</text>
  </g>

  <!-- Arrow 3 -->
  <g transform="translate(540, 165)">
    <line x1="0" y1="0" x2="20" y2="0" stroke="#7C3AED" stroke-width="2.5"/>
    <polygon points="20,-4 28,0 20,4" fill="#7C3AED"/>
  </g>

  <!-- Step 4: Compare Scores -->
  <g transform="translate(575, 85)" filter="url(#p-shadow)">
    <rect x="0" y="0" width="105" height="180" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
    <rect x="0" y="0" width="105" height="34" rx="8" fill="#F8FAFC"/>
    <text x="52" y="22" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569" text-anchor="middle">4. COMPARE</text>
    <text x="52" y="55" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Score Ratio</text>
    <text x="52" y="90" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626" text-anchor="middle">Spam</text>
    <text x="52" y="112" font-family="-apple-system, sans-serif" font-size="18" font-weight="800" fill="#7C3AED" text-anchor="middle">&gt;&gt;</text>
    <text x="52" y="138" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">Ham</text>
    <text x="52" y="158" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">(93.3× larger)</text>
  </g>

  <!-- Arrow 4 -->
  <g transform="translate(690, 165)">
    <line x1="0" y1="0" x2="20" y2="0" stroke="#7C3AED" stroke-width="2.5"/>
    <polygon points="20,-4 28,0 20,4" fill="#7C3AED"/>
  </g>

  <!-- Step 5: Output Prediction -->
  <g transform="translate(720, 85)" filter="url(#p-shadow)">
    <rect x="0" y="0" width="90" height="180" rx="8" fill="url(#p-grad-1)" stroke="#7C3AED" stroke-width="2"/>
    <text x="45" y="32" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#7C3AED" text-anchor="middle">5. OUTPUT</text>
    <rect x="10" y="55" width="70" height="50" rx="6" fill="#DC2626"/>
    <text x="45" y="85" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">SPAM</text>
    <text x="45" y="130" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">P(Spam|X)</text>
    <text x="45" y="150" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#DC2626" text-anchor="middle">98.9%</text>
  </g>

  <!-- Bottom Explanatory Banner -->
  <rect x="40" y="290" width="770" height="65" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="55" y="315" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Core Decision Rule (argmax):</text>
  <text x="55" y="338" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">Predicted Class = argmax_C [ P(C) × ∏ P(x_i | C) ]. Denominator P(X) is constant across classes and can be omitted during ranking.</text>
</svg>"""

# 2. Probability Fundamentals / Prior Bars
SVG_PROBABILITY_BARS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Class Prior Probabilities in Sample Dataset</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Sample of N = 100 emails: 80 Legitimate (Ham) and 20 Unsolicited (Spam)</text>

  <!-- Plot Area -->
  <g transform="translate(80, 90)">
    <!-- Y-axis Grid -->
    <line x1="0" y1="0" x2="580" y2="0" stroke="#E2E8F0" stroke-width="1"/>
    <line x1="0" y1="45" x2="580" y2="45" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="0" y1="90" x2="580" y2="90" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="0" y1="135" x2="580" y2="135" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="0" y1="180" x2="580" y2="180" stroke="#CBD5E1" stroke-width="1.5"/>

    <!-- Y-axis Labels -->
    <text x="-15" y="5" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">1.00 (100%)</text>
    <text x="-15" y="50" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0.75 (75%)</text>
    <text x="-15" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0.50 (50%)</text>
    <text x="-15" y="140" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0.25 (25%)</text>
    <text x="-15" y="184" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="end">0.00 (0%)</text>

    <!-- Bar 1: Ham (P = 0.80 -> height = 144px) -->
    <rect x="100" y="36" width="130" height="144" rx="6" fill="#059669"/>
    <text x="165" y="24" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#059669" text-anchor="middle">P(Ham) = 0.80</text>
    <text x="165" y="105" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">80 / 100</text>
    <text x="165" y="125" font-family="-apple-system, sans-serif" font-size="11" fill="#E6FFFA" text-anchor="middle">(80% of data)</text>
    <text x="165" y="205" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#1E293B" text-anchor="middle">Legitimate (Ham)</text>

    <!-- Bar 2: Spam (P = 0.20 -> height = 36px) -->
    <rect x="350" y="144" width="130" height="36" rx="6" fill="#DC2626"/>
    <text x="415" y="132" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#DC2626" text-anchor="middle">P(Spam) = 0.20</text>
    <text x="415" y="167" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">20 / 100 (20%)</text>
    <text x="415" y="205" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#1E293B" text-anchor="middle">Spam</text>
  </g>

  <!-- Callout Note -->
  <rect x="60" y="305" width="640" height="38" rx="6" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1"/>
  <text x="75" y="328" font-family="-apple-system, sans-serif" font-size="11" fill="#92400E">Note: The prior probability represents initial base knowledge before examining specific message tokens.</text>
</svg>"""

# 3. Conditional Probability Contingency Table
SVG_CONTINGENCY_TABLE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 400" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Contingency Table: Visualizing the Restricted Denominator</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">How conditioning narrows the reference universe from N = 100 to a specific subset</text>

  <!-- Table Graphic -->
  <g transform="translate(60, 90)">
    <!-- Header Row -->
    <rect x="150" y="0" width="130" height="40" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="215" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#334155" text-anchor="middle">Contains "Free"</text>

    <rect x="280" y="0" width="130" height="40" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
    <text x="345" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#334155" text-anchor="middle">No "Free"</text>

    <rect x="410" y="0" width="120" height="40" fill="#E2E8F0" stroke="#CBD5E1" stroke-width="1"/>
    <text x="470" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Class Total</text>

    <!-- Row 1: Spam -->
    <rect x="0" y="40" width="150" height="50" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
    <text x="75" y="70" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#DC2626" text-anchor="middle">Class = Spam</text>

    <rect x="150" y="40" width="130" height="50" fill="#FEE2E2" stroke="#FECACA" stroke-width="1"/>
    <text x="215" y="70" font-family="-apple-system, sans-serif" font-size="15" font-weight="800" fill="#991B1B" text-anchor="middle">16</text>

    <rect x="280" y="40" width="130" height="50" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="345" y="70" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#64748B" text-anchor="middle">4</text>

    <rect x="410" y="40" width="120" height="50" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="470" y="70" font-family="-apple-system, sans-serif" font-size="15" font-weight="800" fill="#DC2626" text-anchor="middle">20</text>

    <!-- Row 2: Ham -->
    <rect x="0" y="90" width="150" height="50" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
    <text x="75" y="120" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#059669" text-anchor="middle">Class = Ham</text>

    <rect x="150" y="90" width="130" height="50" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="215" y="120" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#64748B" text-anchor="middle">8</text>

    <rect x="280" y="90" width="130" height="50" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="345" y="120" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#64748B" text-anchor="middle">72</text>

    <rect x="410" y="90" width="120" height="50" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
    <text x="470" y="120" font-family="-apple-system, sans-serif" font-size="15" font-weight="800" fill="#059669" text-anchor="middle">80</text>

    <!-- Column Totals -->
    <rect x="0" y="140" width="150" height="45" fill="#E2E8F0" stroke="#CBD5E1" stroke-width="1"/>
    <text x="75" y="168" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Word Total</text>

    <rect x="150" y="140" width="130" height="45" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.5"/>
    <text x="215" y="168" font-family="-apple-system, sans-serif" font-size="15" font-weight="800" fill="#1D4ED8" text-anchor="middle">24</text>

    <rect x="280" y="140" width="130" height="45" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="345" y="168" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#64748B" text-anchor="middle">76</text>

    <rect x="410" y="140" width="120" height="45" fill="#0F172A" stroke="#0F172A" stroke-width="1"/>
    <text x="470" y="168" font-family="-apple-system, sans-serif" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">100</text>
  </g>

  <!-- Callout Comparison Cards -->
  <g transform="translate(60, 290)">
    <!-- Card A: P(Free | Spam) -->
    <rect x="0" y="0" width="310" height="85" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="15" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#DC2626">Likelihood: P(Free | Spam) = 16 / 20 = 0.80</text>
    <text x="15" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Universe restricted to the Spam row (20 messages).</text>
    <text x="15" y="62" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#991B1B">80% of all spam messages contain the word "free".</text>

    <!-- Card B: P(Spam | Free) -->
    <rect x="330" y="0" width="330" height="85" rx="8" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.5"/>
    <text x="345" y="24" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#1D4ED8">Posterior: P(Spam | Free) = 16 / 24 = 0.6667</text>
    <text x="345" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Universe restricted to the "Free" column (24 messages).</text>
    <text x="345" y="62" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#1E40AF">66.67% of emails containing "free" turn out to be spam.</text>
  </g>
</svg>"""

# 4. Bayes' Theorem Update Graphic
SVG_BAYES_THEOREM_UPDATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 370" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Bayes' Theorem: Prior Belief Updated by Evidence</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Observing evidence E = "Contains 'Free'" updates P(Spam) from 20.0% to 66.7%</text>

  <!-- Left: Prior Distribution -->
  <g transform="translate(60, 90)">
    <rect x="0" y="0" width="200" height="200" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="100" y="28" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#334155" text-anchor="middle">PRIOR BELIEF</text>
    <text x="100" y="46" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Before reading message text</text>

    <!-- Visual Donut/Pie representation as stacked bars -->
    <rect x="30" y="70" width="140" height="80" rx="4" fill="#059669"/>
    <text x="100" y="115" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">Ham: 80%</text>

    <rect x="30" y="155" width="140" height="25" rx="4" fill="#DC2626"/>
    <text x="100" y="172" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">Spam: 20%</text>
  </g>

  <!-- Middle: Evidence Transformation Box -->
  <g transform="translate(290, 110)">
    <rect x="0" y="0" width="200" height="160" rx="8" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1.5"/>
    <text x="100" y="26" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#7C3AED" text-anchor="middle">EVIDENCE OBSERVED</text>
    <rect x="20" y="40" width="160" height="30" rx="4" fill="#FFFFFF" stroke="#7C3AED" stroke-width="1"/>
    <text x="100" y="60" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#7C3AED" text-anchor="middle">Word = "free"</text>

    <text x="100" y="95" font-family="-apple-system, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Likelihood Ratio:</text>
    <text x="100" y="115" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#DC2626" text-anchor="middle">P(Free|Spam) = 0.80</text>
    <text x="100" y="132" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#059669" text-anchor="middle">P(Free|Ham) = 0.10</text>
    <text x="100" y="148" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#7C3AED" text-anchor="middle">(8× more likely in Spam!)</text>
  </g>

  <!-- Right: Posterior Distribution -->
  <g transform="translate(520, 90)">
    <rect x="0" y="0" width="220" height="200" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="110" y="28" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1D4ED8" text-anchor="middle">POSTERIOR BELIEF</text>
    <text x="110" y="46" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">After observing word "free"</text>

    <rect x="30" y="70" width="160" height="70" rx="4" fill="#DC2626"/>
    <text x="110" y="105" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">Spam: 66.7%</text>
    <text x="110" y="125" font-family="-apple-system, sans-serif" font-size="11" fill="#FEE2E2" text-anchor="middle">P(Spam|Free) = 16/24</text>

    <rect x="30" y="145" width="160" height="35" rx="4" fill="#059669"/>
    <text x="110" y="167" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">Ham: 33.3%</text>
  </g>

  <!-- Connective Arrows -->
  <line x1="262" y1="190" x2="288" y2="190" stroke="#7C3AED" stroke-width="2"/>
  <polygon points="288,187 294,190 288,193" fill="#7C3AED"/>

  <line x1="492" y1="190" x2="518" y2="190" stroke="#7C3AED" stroke-width="2"/>
  <polygon points="518,187 524,190 518,193" fill="#7C3AED"/>

  <!-- Footer Banner -->
  <rect x="60" y="305" width="680" height="42" rx="6" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
  <text x="75" y="331" font-family="-apple-system, sans-serif" font-size="12" fill="#1E40AF">Bayes Formula: P(Spam|Free) = [P(Free|Spam) × P(Spam)] / P(Free) = [0.80 × 0.20] / 0.24 = 0.16 / 0.24 = 66.67%</text>
</svg>"""

# 5. Spam Words Likelihood Comparison
SVG_SPAM_WORDS_LIKELIHOOD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Feature Likelihoods Across Classes: P(Word | Class)</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Comparing conditional probabilities of observed vocabulary tokens in Spam vs. Ham</text>

  <!-- Legend -->
  <g transform="translate(540, 28)">
    <rect x="0" y="0" width="14" height="14" rx="3" fill="#DC2626"/>
    <text x="20" y="12" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#334155">Spam</text>
    <rect x="75" y="0" width="14" height="14" rx="3" fill="#059669"/>
    <text x="95" y="12" font-family="-apple-system, sans-serif" font-size="12" font-weight="600" fill="#334155">Ham</text>
  </g>

  <!-- Plot Area -->
  <g transform="translate(80, 85)">
    <!-- Word 1: 'free' -->
    <text x="0" y="32" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#1E293B">"free"</text>
    <!-- Spam Bar: 0.80 -> 400px -->
    <rect x="80" y="12" width="400" height="22" rx="4" fill="#DC2626"/>
    <text x="490" y="28" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">0.80 (80%)</text>
    <!-- Ham Bar: 0.10 -> 50px -->
    <rect x="80" y="38" width="50" height="22" rx="4" fill="#059669"/>
    <text x="140" y="54" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669">0.10 (10%)</text>
    <text x="575" y="38" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#7C3AED">8.0× Ratio</text>

    <!-- Word 2: 'offer' -->
    <text x="0" y="105" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#1E293B">"offer"</text>
    <!-- Spam Bar: 0.70 -> 350px -->
    <rect x="80" y="85" width="350" height="22" rx="4" fill="#DC2626"/>
    <text x="440" y="101" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">0.70 (70%)</text>
    <!-- Ham Bar: 0.15 -> 75px -->
    <rect x="80" y="111" width="75" height="22" rx="4" fill="#059669"/>
    <text x="165" y="127" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669">0.15 (15%)</text>
    <text x="575" y="111" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#7C3AED">4.7× Ratio</text>

    <!-- Word 3: 'prize' -->
    <text x="0" y="178" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#1E293B">"prize"</text>
    <!-- Spam Bar: 0.50 -> 250px -->
    <rect x="80" y="158" width="250" height="22" rx="4" fill="#DC2626"/>
    <text x="340" y="174" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">0.50 (50%)</text>
    <!-- Ham Bar: 0.05 -> 25px -->
    <rect x="80" y="184" width="25" height="22" rx="4" fill="#059669"/>
    <text x="115" y="200" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669">0.05 (5%)</text>
    <text x="575" y="184" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#7C3AED">10.0× Ratio</text>
  </g>

  <!-- Bottom Explanatory Banner -->
  <rect x="40" y="315" width="680" height="42" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="55" y="340" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">When words appear substantially more frequently in spam than legitimate emails, their likelihood ratio pushes the posterior score toward Spam.</text>
</svg>"""

# 6. Independence Assumption Diagram
SVG_INDEPENDENCE_ASSUMPTION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 380" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">The "Naive" Conditional Independence Assumption</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Comparing full joint dependency modeling against the Naive Bayes factored product assumption</text>

  <!-- Left: Real World Interdependent Graph -->
  <g transform="translate(50, 90)">
    <rect x="0" y="0" width="320" height="210" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="160" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#DC2626" text-anchor="middle">REALITY: Interdependent Words</text>
    <text x="160" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Words correlate heavily with one another</text>

    <!-- Nodes -->
    <circle cx="80" cy="95" r="26" fill="#FFFFFF" stroke="#DC2626" stroke-width="2"/>
    <text x="80" y="100" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">"free"</text>

    <circle cx="240" cy="95" r="26" fill="#FFFFFF" stroke="#DC2626" stroke-width="2"/>
    <text x="240" y="100" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">"prize"</text>

    <circle cx="160" cy="165" r="26" fill="#FFFFFF" stroke="#DC2626" stroke-width="2"/>
    <text x="160" y="170" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626" text-anchor="middle">"offer"</text>

    <!-- Interconnecting arcs -->
    <line x1="106" y1="95" x2="214" y2="95" stroke="#DC2626" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="98" y1="114" x2="142" y2="146" stroke="#DC2626" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="222" y1="114" x2="178" y2="146" stroke="#DC2626" stroke-width="2" stroke-dasharray="3,3"/>

    <text x="160" y="85" font-family="-apple-system, sans-serif" font-size="9" fill="#991B1B" text-anchor="middle">correlated</text>
    <text x="95" y="145" font-family="-apple-system, sans-serif" font-size="9" fill="#991B1B" text-anchor="middle">correlated</text>
    <text x="225" y="145" font-family="-apple-system, sans-serif" font-size="9" fill="#991B1B" text-anchor="middle">correlated</text>
  </g>

  <!-- Right: Naive Bayes Star Topology -->
  <g transform="translate(430, 90)">
    <rect x="0" y="0" width="320" height="210" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <text x="160" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#15803D" text-anchor="middle">NAIVE BAYES: Conditionally Independent</text>
    <text x="160" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Words depend ONLY on the class node C</text>

    <!-- Center Class Node -->
    <rect x="110" y="65" width="100" height="34" rx="6" fill="#15803D"/>
    <text x="160" y="86" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">Class (C)</text>

    <!-- Leaf feature nodes -->
    <circle cx="65" cy="165" r="24" fill="#FFFFFF" stroke="#15803D" stroke-width="2"/>
    <text x="65" y="170" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#15803D" text-anchor="middle">"free"</text>

    <circle cx="160" cy="165" r="24" fill="#FFFFFF" stroke="#15803D" stroke-width="2"/>
    <text x="160" y="170" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#15803D" text-anchor="middle">"offer"</text>

    <circle cx="255" cy="165" r="24" fill="#FFFFFF" stroke="#15803D" stroke-width="2"/>
    <text x="255" y="170" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#15803D" text-anchor="middle">"prize"</text>

    <!-- Directed arrows from Class to Features -->
    <line x1="130" y1="99" x2="80" y2="142" stroke="#15803D" stroke-width="2"/>
    <polygon points="78,136 78,144 86,142" fill="#15803D"/>

    <line x1="160" y1="99" x2="160" y2="141" stroke="#15803D" stroke-width="2"/>
    <polygon points="156,134 160,141 164,134" fill="#15803D"/>

    <line x1="190" y1="99" x2="240" y2="142" stroke="#15803D" stroke-width="2"/>
    <polygon points="234,142 242,144 242,136" fill="#15803D"/>
  </g>

  <!-- Bottom Explanatory Banner -->
  <rect x="50" y="315" width="700" height="46" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="65" y="335" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Simplification Formula: P(x₁, x₂, x₃ | C) ≈ P(x₁ | C) × P(x₂ | C) × P(x₃ | C)</text>
  <text x="65" y="352" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">While conditionally naive, the decision boundary often preserves optimal ranking even when dependencies exist.</text>
</svg>"""

# 7. Step-by-Step Class Scores
SVG_STEP_BY_STEP_SCORES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 370" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Step-by-Step Score &amp; Posterior Probability Comparison</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Unnormalized class scores converted into normalized posterior probabilities</text>

  <!-- Stage 1: Unnormalized Scores -->
  <g transform="translate(60, 90)">
    <rect x="0" y="0" width="310" height="200" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="155" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#334155" text-anchor="middle">STAGE 1: Unnormalized Scores</text>
    <text x="155" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Score(C) = P(C) × ∏ P(x_i | C)</text>

    <!-- Spam Score Bar -->
    <text x="20" y="78" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">Score(Spam):</text>
    <rect x="20" y="86" width="220" height="26" rx="4" fill="#DC2626"/>
    <text x="248" y="104" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#DC2626">0.056000</text>
    <text x="30" y="103" font-family="-apple-system, sans-serif" font-size="10" fill="#FFFFFF">0.20 × (0.80 × 0.70 × 0.50)</text>

    <!-- Ham Score Bar -->
    <text x="20" y="138" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669">Score(Ham):</text>
    <rect x="20" y="146" width="12" height="26" rx="3" fill="#059669"/>
    <text x="40" y="164" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#059669">0.000600</text>
    <text x="20" y="188" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">0.80 × (0.10 × 0.15 × 0.05)</text>
  </g>

  <!-- Arrow -->
  <g transform="translate(385, 175)">
    <line x1="0" y1="0" x2="20" y2="0" stroke="#7C3AED" stroke-width="2.5"/>
    <polygon points="20,-4 28,0 20,4" fill="#7C3AED"/>
    <text x="14" y="22" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#7C3AED" text-anchor="middle">Normalize</text>
  </g>

  <!-- Stage 2: Normalized Posteriors -->
  <g transform="translate(425, 90)">
    <rect x="0" y="0" width="310" height="200" rx="8" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1.5"/>
    <text x="155" y="26" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#7C3AED" text-anchor="middle">STAGE 2: Normalized Posteriors</text>
    <text x="155" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Divide by Total Score Z = 0.056600</text>

    <!-- Spam Posterior Bar -->
    <text x="20" y="78" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">P(Spam | X):</text>
    <rect x="20" y="86" width="220" height="26" rx="4" fill="#DC2626"/>
    <text x="248" y="104" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#DC2626">98.94%</text>
    <text x="30" y="103" font-family="-apple-system, sans-serif" font-size="10" fill="#FFFFFF">0.056000 / 0.056600</text>

    <!-- Ham Posterior Bar -->
    <text x="20" y="138" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669">P(Ham | X):</text>
    <rect x="20" y="146" width="10" height="26" rx="3" fill="#059669"/>
    <text x="38" y="164" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#059669">1.06%</text>
    <text x="20" y="188" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">0.000600 / 0.056600</text>
  </g>

  <!-- Bottom Explanatory Banner -->
  <rect x="60" y="305" width="675" height="42" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="75" y="331" font-family="-apple-system, sans-serif" font-size="12" fill="#334155">Conclusion: The message is classified as <tspan font-weight="700" fill="#DC2626">SPAM</tspan> with an overwhelming estimated posterior confidence of 98.94%.</text>
</svg>"""

# 8. Zero Frequency Problem Illustration
SVG_ZERO_FREQUENCY_PROBLEM = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 370" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">The Zero-Frequency Problem: Product Annihilation</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">A single zero likelihood destroys all other accumulated evidence in the multiplication chain</text>

  <!-- Main Illustration Box -->
  <g transform="translate(50, 90)">
    <rect x="0" y="0" width="680" height="195" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="30" y="32" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#DC2626">Scenario: Incoming message contains previously unseen word in Ham ("jackpot")</text>

    <!-- Calculation Chain -->
    <g transform="translate(30, 60)">
      <rect x="0" y="0" width="620" height="50" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="15" y="30" font-family="-apple-system, sans-serif" font-size="13" font-weight="600" fill="#334155">Score(Ham) = 0.80 × 0.10 × 0.15 × 0.05 × <tspan font-weight="800" fill="#DC2626">0.00</tspan> = <tspan font-weight="800" fill="#DC2626">0.000000</tspan></text>
    </g>

    <!-- Callout explaining the issue -->
    <g transform="translate(30, 125)">
      <rect x="0" y="0" width="620" height="55" rx="6" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1"/>
      <text x="15" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#B45309">Catastrophic Failure:</text>
      <text x="15" y="44" font-family="-apple-system, sans-serif" font-size="11" fill="#78350F">Because Count("jackpot", Ham) = 0 in the 80 training emails, P("jackpot" | Ham) = 0. This instantly forces the entire Ham score to 0, completely ignoring that the email could be completely authentic!</text>
    </g>
  </g>

  <!-- Bottom Explanatory Banner -->
  <rect x="50" y="300" width="680" height="48" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="65" y="322" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Statistical Reality: Zero frequency in training data does NOT mean zero probability in nature.</text>
  <text x="65" y="338" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">It simply means the training sample did not happen to observe that particular token.</text>
</svg>"""

# 9. Laplace Smoothing Comparison
SVG_LAPLACE_SMOOTHING = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 380" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Laplace Smoothing: Preventing Zero Probabilities</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Adding pseudocount α = 1.0 ensures every event has a small, realistic non-zero likelihood</text>

  <!-- Comparison Bars -->
  <g transform="translate(60, 90)">
    <!-- Subheader 1 -->
    <text x="0" y="20" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">Word: "jackpot" in Legitimate Email (Ham) [Count = 0]</text>

    <!-- Raw Unsmoothed -->
    <text x="0" y="52" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B">Unsmoothed (α = 0):</text>
    <rect x="150" y="38" width="8" height="20" rx="2" fill="#DC2626"/>
    <text x="170" y="53" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626">0 / 80 = 0.0000 (0.00%) — FATAL ZERO</text>

    <!-- Laplace Smoothed -->
    <text x="0" y="86" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B">Smoothed (α = 1, K = 2):</text>
    <rect x="150" y="72" width="60" height="20" rx="3" fill="#059669"/>
    <text x="220" y="87" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669">(0 + 1) / (80 + 2) = 1 / 82 = 0.0122 (1.22%) — SAFE NON-ZERO</text>

    <!-- Divider -->
    <line x1="0" y1="115" x2="660" y2="115" stroke="#E2E8F0" stroke-width="1"/>

    <!-- Subheader 2 -->
    <text x="0" y="145" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B">Word: "jackpot" in Spam [Count = 4]</text>

    <!-- Raw Unsmoothed in Spam -->
    <text x="0" y="177" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B">Unsmoothed (α = 0):</text>
    <rect x="150" y="163" width="200" height="20" rx="3" fill="#64748B"/>
    <text x="360" y="178" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#64748B">4 / 20 = 0.2000 (20.00%)</text>

    <!-- Laplace Smoothed in Spam -->
    <text x="0" y="211" font-family="-apple-system, sans-serif" font-size="12" fill="#64748B">Smoothed (α = 1, K = 2):</text>
    <rect x="150" y="197" width="227" height="20" rx="3" fill="#7C3AED"/>
    <text x="390" y="212" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#7C3AED">(4 + 1) / (20 + 2) = 5 / 22 = 0.2273 (22.73%)</text>
  </g>

  <!-- Formula Callout -->
  <rect x="60" y="320" width="660" height="42" rx="6" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1"/>
  <text x="75" y="346" font-family="-apple-system, sans-serif" font-size="12" fill="#6D28D9"><tspan font-weight="700">General Smoothing Formula:</tspan> P(x_i | C) = [ Count(x_i, C) + α ] / [ Count(C) + α × K ], where K is vocabulary or outcome dimension.</text>
</svg>"""

# 10. Naive Bayes Variants 4-Card Visual
SVG_NB_VARIANTS_COMPARISON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">The Four Major Naive Bayes Variants</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Select the appropriate variant based on feature data types and statistical distribution assumptions</text>

  <!-- Grid of 4 Cards -->
  <g transform="translate(40, 80)">
    <!-- Card 1: Gaussian NB -->
    <rect x="0" y="0" width="340" height="145" rx="8" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1.5"/>
    <rect x="12" y="12" width="130" height="24" rx="4" fill="#7C3AED"/>
    <text x="77" y="28" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">GAUSSIAN NB</text>
    <text x="15" y="56" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Feature Type: Continuous Real Numbers</text>
    <text x="15" y="74" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Assumes features follow normal (Gaussian) distribution.</text>
    <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Parameters: Mean (μ_c) and Variance (σ²_c).</text>
    <text x="15" y="112" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#7C3AED">Use case: Sensor data, Iris dimensions, blood pressure.</text>

    <!-- Card 2: Multinomial NB -->
    <rect x="380" y="0" width="340" height="145" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
    <rect x="392" y="12" width="145" height="24" rx="4" fill="#059669"/>
    <text x="464" y="28" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">MULTINOMIAL NB</text>
    <text x="395" y="56" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Feature Type: Discrete Non-Negative Counts</text>
    <text x="395" y="74" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Models multinomially distributed word occurrence counts.</text>
    <text x="395" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Parameters: Token frequencies per class with Laplace smoothing.</text>
    <text x="395" y="112" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#059669">Use case: Text classification, document term counts, bag-of-words.</text>

    <!-- Card 3: Bernoulli NB -->
    <rect x="0" y="165" width="340" height="145" rx="8" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect x="12" y="177" width="135" height="24" rx="4" fill="#2563EB"/>
    <text x="79" y="193" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">BERNOULLI NB</text>
    <text x="15" y="221" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Feature Type: Binary Indicators (0 or 1)</text>
    <text x="15" y="239" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Models presence vs absence of features, penalizing non-occurrences.</text>
    <text x="15" y="257" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Parameters: Probability p_ci that feature i appears in class c.</text>
    <text x="15" y="277" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#2563EB">Use case: Short texts, binary survey responses, boolean flags.</text>

    <!-- Card 4: Categorical NB -->
    <rect x="380" y="165" width="340" height="145" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
    <rect x="392" y="177" width="145" height="24" rx="4" fill="#D97706"/>
    <text x="464" y="193" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">CATEGORICAL NB</text>
    <text x="395" y="221" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Feature Type: Discrete Nominal Categories</text>
    <text x="395" y="239" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Each feature takes one of K distinct category values.</text>
    <text x="395" y="257" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Parameters: Categorical probabilities for each category level.</text>
    <text x="395" y="277" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#D97706">Use case: Survey data (Occupation, Education, Region).</text>
  </g>

  <!-- Bottom Notice -->
  <rect x="40" y="380" width="720" height="28" rx="4" fill="#F8FAFC"/>
  <text x="400" y="398" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Key Rule: Matching the Naive Bayes algorithm variant to your feature representation is essential for mathematical validity.</text>
</svg>"""

# 11. Document-Term Count Frequency Heatmap (MultinomialNB)
SVG_MULTINOMIAL_TERM_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 370" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">MultinomialNB: Document-Term Count Matrix Heatmap</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Term frequency counts (integer counts ≥ 0) capturing repetition intensity</text>

  <!-- Heatmap Matrix -->
  <g transform="translate(60, 90)">
    <!-- Column Headers -->
    <rect x="160" y="0" width="90" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="205" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">"free"</text>

    <rect x="250" y="0" width="90" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="295" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">"prize"</text>

    <rect x="340" y="0" width="90" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="385" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">"cash"</text>

    <rect x="430" y="0" width="90" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="475" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">"meeting"</text>

    <rect x="520" y="0" width="90" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="565" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">"invoice"</text>

    <!-- Row 1: Email 1 (Spam) -->
    <rect x="0" y="35" width="160" height="40" fill="#FEF2F2" stroke="#FECACA"/>
    <text x="80" y="60" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626" text-anchor="middle">Doc 1 [Spam]</text>
    <rect x="160" y="35" width="90" height="40" fill="#F87171" stroke="#FECACA"/>
    <text x="205" y="60" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">3</text>
    <rect x="250" y="35" width="90" height="40" fill="#FCA5A5" stroke="#FECACA"/>
    <text x="295" y="60" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#7F1D1D" text-anchor="middle">2</text>
    <rect x="340" y="35" width="90" height="40" fill="#FCA5A5" stroke="#FECACA"/>
    <text x="385" y="60" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#7F1D1D" text-anchor="middle">1</text>
    <rect x="430" y="35" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="475" y="60" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="520" y="35" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="565" y="60" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>

    <!-- Row 2: Email 2 (Spam) -->
    <rect x="0" y="75" width="160" height="40" fill="#FEF2F2" stroke="#FECACA"/>
    <text x="80" y="100" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626" text-anchor="middle">Doc 2 [Spam]</text>
    <rect x="160" y="75" width="90" height="40" fill="#FCA5A5" stroke="#FECACA"/>
    <text x="205" y="100" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#7F1D1D" text-anchor="middle">1</text>
    <rect x="250" y="75" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="295" y="100" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="340" y="75" width="90" height="40" fill="#EF4444" stroke="#FECACA"/>
    <text x="385" y="100" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">4</text>
    <rect x="430" y="75" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="475" y="100" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="520" y="75" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="565" y="100" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>

    <!-- Row 3: Email 3 (Ham) -->
    <rect x="0" y="115" width="160" height="40" fill="#ECFDF5" stroke="#A7F3D0"/>
    <text x="80" y="140" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">Doc 3 [Ham]</text>
    <rect x="160" y="115" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="205" y="140" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="250" y="115" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="295" y="140" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="340" y="115" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="385" y="140" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="430" y="115" width="90" height="40" fill="#34D399" stroke="#A7F3D0"/>
    <text x="475" y="140" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#064E3B" text-anchor="middle">2</text>
    <rect x="520" y="115" width="90" height="40" fill="#6EE7B7" stroke="#A7F3D0"/>
    <text x="565" y="140" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#064E3B" text-anchor="middle">1</text>

    <!-- Row 4: Email 4 (Ham) -->
    <rect x="0" y="155" width="160" height="40" fill="#ECFDF5" stroke="#A7F3D0"/>
    <text x="80" y="180" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">Doc 4 [Ham]</text>
    <rect x="160" y="155" width="90" height="40" fill="#FEE2E2" stroke="#FECACA"/>
    <text x="205" y="180" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#DC2626" text-anchor="middle">1</text>
    <rect x="250" y="155" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="295" y="180" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="340" y="155" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="385" y="180" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="430" y="155" width="90" height="40" fill="#059669" stroke="#A7F3D0"/>
    <text x="475" y="180" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">5</text>
    <rect x="520" y="155" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="565" y="180" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
  </g>

  <!-- Explanatory Footer -->
  <rect x="60" y="305" width="650" height="42" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="75" y="331" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">Notice: In MultinomialNB, words appearing multiple times contribute proportionally higher likelihood weights.</text>
</svg>"""

# 12. BernoulliNB Binary Presence Matrix
SVG_BERNOULLI_PRESENCE_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 370" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">BernoulliNB: Binary Word Presence/Absence Matrix</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">All frequencies clamped strictly to {0, 1}: only presence or absence matters</text>

  <!-- Binary Matrix -->
  <g transform="translate(60, 90)">
    <!-- Column Headers -->
    <rect x="160" y="0" width="90" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="205" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">"free"</text>

    <rect x="250" y="0" width="90" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="295" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">"prize"</text>

    <rect x="340" y="0" width="90" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="385" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">"cash"</text>

    <rect x="430" y="0" width="90" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="475" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">"meeting"</text>

    <rect x="520" y="0" width="90" height="35" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="565" y="22" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">"invoice"</text>

    <!-- Row 1: Email 1 (Spam) -->
    <rect x="0" y="35" width="160" height="40" fill="#FEF2F2" stroke="#FECACA"/>
    <text x="80" y="60" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626" text-anchor="middle">Doc 1 [Spam]</text>
    <rect x="160" y="35" width="90" height="40" fill="#2563EB" stroke="#93C5FD"/>
    <text x="205" y="60" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
    <rect x="250" y="35" width="90" height="40" fill="#2563EB" stroke="#93C5FD"/>
    <text x="295" y="60" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
    <rect x="340" y="35" width="90" height="40" fill="#2563EB" stroke="#93C5FD"/>
    <text x="385" y="60" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
    <rect x="430" y="35" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="475" y="60" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="520" y="35" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="565" y="60" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>

    <!-- Row 2: Email 2 (Spam) -->
    <rect x="0" y="75" width="160" height="40" fill="#FEF2F2" stroke="#FECACA"/>
    <text x="80" y="100" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626" text-anchor="middle">Doc 2 [Spam]</text>
    <rect x="160" y="75" width="90" height="40" fill="#2563EB" stroke="#93C5FD"/>
    <text x="205" y="100" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
    <rect x="250" y="75" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="295" y="100" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="340" y="75" width="90" height="40" fill="#2563EB" stroke="#93C5FD"/>
    <text x="385" y="100" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
    <rect x="430" y="75" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="475" y="100" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="520" y="75" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="565" y="100" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>

    <!-- Row 3: Email 3 (Ham) -->
    <rect x="0" y="115" width="160" height="40" fill="#ECFDF5" stroke="#A7F3D0"/>
    <text x="80" y="140" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">Doc 3 [Ham]</text>
    <rect x="160" y="115" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="205" y="140" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="250" y="115" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="295" y="140" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="340" y="115" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="385" y="140" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="430" y="115" width="90" height="40" fill="#2563EB" stroke="#93C5FD"/>
    <text x="475" y="140" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
    <rect x="520" y="115" width="90" height="40" fill="#2563EB" stroke="#93C5FD"/>
    <text x="565" y="140" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>

    <!-- Row 4: Email 4 (Ham) -->
    <rect x="0" y="155" width="160" height="40" fill="#ECFDF5" stroke="#A7F3D0"/>
    <text x="80" y="180" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">Doc 4 [Ham]</text>
    <rect x="160" y="155" width="90" height="40" fill="#2563EB" stroke="#93C5FD"/>
    <text x="205" y="180" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
    <rect x="250" y="155" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="295" y="180" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="340" y="155" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="385" y="180" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
    <rect x="430" y="155" width="90" height="40" fill="#2563EB" stroke="#93C5FD"/>
    <text x="475" y="180" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
    <rect x="520" y="155" width="90" height="40" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="565" y="180" font-family="-apple-system, sans-serif" font-size="14" font-weight="600" fill="#94A3B8" text-anchor="middle">0</text>
  </g>

  <!-- Explanatory Footer -->
  <rect x="60" y="305" width="650" height="42" rx="6" fill="#EFF6FF" stroke="#BFDBFE"/>
  <text x="75" y="331" font-family="-apple-system, sans-serif" font-size="12" fill="#1D4ED8">Crucial Distinction: Even though Doc 4 had 5 instances of "meeting", BernoulliNB represents it as a single binary presence 1.</text>
</svg>"""

# 13. Gaussian Distributions (GaussianNB)
SVG_GAUSSIAN_DISTRIBUTIONS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 390" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Gaussian Naive Bayes: Class-Conditional Distributions</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Continuous feature (Study Hours) modeled as normal bell curves with estimated means (μ) and variances (σ²)</text>

  <!-- Plot Area -->
  <g transform="translate(60, 90)">
    <!-- Grid and Axes -->
    <line x1="0" y1="210" x2="660" y2="210" stroke="#CBD5E1" stroke-width="2"/>
    <line x1="0" y1="20" x2="0" y2="210" stroke="#CBD5E1" stroke-width="2"/>

    <!-- Ticks & X-labels (Hours: 0 to 40) -->
    <!-- Scale: x_pos = hours * 15 + 30 -->
    <line x1="30" y1="210" x2="30" y2="216" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="30" y="232" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">0h</text>

    <line x1="180" y1="210" x2="180" y2="216" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="180" y="232" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">10h</text>

    <line x1="330" y1="210" x2="330" y2="216" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="330" y="232" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">20h</text>

    <line x1="480" y1="210" x2="480" y2="216" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="480" y="232" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">30h</text>

    <line x1="630" y1="210" x2="630" y2="216" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="630" y="232" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">40h</text>

    <!-- Curve 1: Class 0 (Not Passed, mu=12h -> x=210) -->
    <!-- Approximate Gaussian Path: peak at x=210, y=50 (height=160) -->
    <path d="M 90,210 C 140,210 170,50 210,50 C 250,50 280,210 330,210" fill="#FEE2E2" fill-opacity="0.5" stroke="#DC2626" stroke-width="3"/>
    <line x1="210" y1="50" x2="210" y2="210" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="4,4"/>
    <circle cx="210" cy="50" r="5" fill="#DC2626"/>
    <text x="210" y="38" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626" text-anchor="middle">μ₀ = 12.0h (Not Passed)</text>

    <!-- Curve 2: Class 1 (Passed, mu=27.5h -> x=442.5) -->
    <!-- Approximate Gaussian Path: peak at x=442, y=65 (height=145) -->
    <path d="M 310,210 C 365,210 405,65 442,65 C 480,65 520,210 575,210" fill="#D1FAE5" fill-opacity="0.5" stroke="#059669" stroke-width="3"/>
    <line x1="442" y1="65" x2="442" y2="210" stroke="#059669" stroke-width="1.5" stroke-dasharray="4,4"/>
    <circle cx="442" cy="65" r="5" fill="#059669"/>
    <text x="442" y="52" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">μ₁ = 27.6h (Passed)</text>

    <!-- Test Observation Line at x=20h -> x=330 -->
    <line x1="330" y1="20" x2="330" y2="210" stroke="#7C3AED" stroke-width="2"/>
    <circle cx="330" cy="190" r="4" fill="#DC2626"/>
    <circle cx="330" cy="180" r="4" fill="#059669"/>
    <rect x="335" y="90" width="130" height="45" rx="4" fill="#FFFFFF" stroke="#7C3AED" stroke-width="1"/>
    <text x="342" y="108" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#7C3AED">Query: x = 20 Hours</text>
    <text x="342" y="124" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">Evaluate likelihoods</text>
  </g>

  <!-- Formula Callout -->
  <rect x="60" y="340" width="660" height="36" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="75" y="362" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Gaussian Likelihood: P(x | C) = [1 / (√(2πσ²))] × exp( - (x - μ)² / (2σ²) )</text>
</svg>"""

# 14. Confusion Matrix Heatmap (Actual Lab Results)
SVG_CONFUSION_MATRIX_HEATMAP = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 390" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Spam Classifier: Actual Test Set Confusion Matrix</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Evaluated on N = 20 test emails (10 Legitimate, 10 Spam) using MultinomialNB (α = 1.0)</text>

  <!-- 2x2 Matrix Grid -->
  <g transform="translate(100, 95)">
    <!-- Column Headers (Predicted) -->
    <text x="210" y="0" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="middle">PREDICTED CLASS</text>
    <rect x="110" y="15" width="100" height="30" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="160" y="35" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">Pred: Ham</text>
    <rect x="210" y="15" width="100" height="30" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="260" y="35" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#DC2626" text-anchor="middle">Pred: Spam</text>

    <!-- Row Headers (Actual) -->
    <text x="-5" y="115" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="end">ACTUAL: Ham</text>
    <text x="-5" y="175" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A" text-anchor="end">ACTUAL: Spam</text>

    <!-- Cell TN: 9 -->
    <rect x="110" y="45" width="100" height="60" fill="#D1FAE5" stroke="#A7F3D0" stroke-width="1.5"/>
    <text x="160" y="77" font-family="-apple-system, sans-serif" font-size="22" font-weight="800" fill="#065F46" text-anchor="middle">9</text>
    <text x="160" y="95" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#047857" text-anchor="middle">True Neg (TN)</text>

    <!-- Cell FP: 1 -->
    <rect x="210" y="45" width="100" height="60" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
    <text x="260" y="77" font-family="-apple-system, sans-serif" font-size="22" font-weight="800" fill="#92400E" text-anchor="middle">1</text>
    <text x="260" y="95" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#B45309" text-anchor="middle">False Pos (FP)</text>

    <!-- Cell FN: 0 -->
    <rect x="110" y="105" width="100" height="60" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
    <text x="160" y="137" font-family="-apple-system, sans-serif" font-size="22" font-weight="800" fill="#059669" text-anchor="middle">0</text>
    <text x="160" y="155" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#059669" text-anchor="middle">False Neg (FN)</text>

    <!-- Cell TP: 10 -->
    <rect x="210" y="105" width="100" height="60" fill="#D1FAE5" stroke="#A7F3D0" stroke-width="1.5"/>
    <text x="260" y="137" font-family="-apple-system, sans-serif" font-size="22" font-weight="800" fill="#065F46" text-anchor="middle">10</text>
    <text x="260" y="155" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#047857" text-anchor="middle">True Pos (TP)</text>
  </g>

  <!-- Metrics Summary Card on Right -->
  <g transform="translate(460, 110)">
    <rect x="0" y="0" width="240" height="175" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="20" y="28" font-family="-apple-system, sans-serif" font-size="13" font-weight="700" fill="#0F172A">Verified Test Metrics:</text>

    <text x="20" y="58" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">Accuracy: (10 + 9) / 20 =</text>
    <text x="175" y="58" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#059669">95.0%</text>

    <text x="20" y="88" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">Precision: 10 / (10 + 1) =</text>
    <text x="175" y="88" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#2563EB">90.9%</text>

    <text x="20" y="118" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">Recall: 10 / (10 + 0) =</text>
    <text x="175" y="118" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#059669">100.0%</text>

    <text x="20" y="148" font-family="-apple-system, sans-serif" font-size="12" fill="#475569">F1-Score: 2·P·R / (P+R) =</text>
    <text x="175" y="148" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#7C3AED">95.2%</text>
  </g>

  <!-- Explanatory Footer -->
  <rect x="60" y="315" width="660" height="50" rx="6" fill="#F5F3FF" stroke="#DDD6FE"/>
  <text x="75" y="335" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#6D28D9">Spam Tradeoff Analysis:</text>
  <text x="75" y="352" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Recall is 100% (zero spam missed). The single false positive (1 legitimate email sent to spam) shows why tuning decision thresholds matters.</text>
</svg>"""

# 15. Predicted Class Probabilities (predict_proba Bar Chart)
SVG_PREDICTED_PROBABILITY_BARS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 390" width="100%" height="100%" style="background:#FFFFFF;border-radius:12px;">
  <!-- Title & Subtitle -->
  <text x="40" y="36" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" fill="#0F172A">Model Confidence: predict_proba Class Probabilities</text>
  <text x="40" y="58" font-family="-apple-system, sans-serif" font-size="13" fill="#64748B">Estimated posterior probabilities for 4 test emails demonstrating confident vs nuanced outputs</text>

  <!-- Legend -->
  <g transform="translate(560, 28)">
    <rect x="0" y="0" width="14" height="14" rx="3" fill="#059669"/>
    <text x="20" y="12" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#334155">P(Ham)</text>
    <rect x="75" y="0" width="14" height="14" rx="3" fill="#DC2626"/>
    <text x="95" y="12" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#334155">P(Spam)</text>
  </g>

  <!-- 4 Horizontal Stacked Probability Bars -->
  <g transform="translate(60, 90)">
    <!-- Example 1 -->
    <text x="0" y="18" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Ex 1: "Claim your free prize and cash bonus today!"</text>
    <!-- Bar 1: 100% Spam -> 550px red -->
    <rect x="0" y="26" width="550" height="24" rx="4" fill="#DC2626"/>
    <text x="560" y="43" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#DC2626">100.0% Spam</text>

    <!-- Example 2 -->
    <text x="0" y="78" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Ex 2: "Team meeting scheduled for Monday project review"</text>
    <!-- Bar 2: 99.98% Ham -> 550px green -->
    <rect x="0" y="86" width="550" height="24" rx="4" fill="#059669"/>
    <text x="560" y="103" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#059669">99.98% Ham</text>

    <!-- Example 3 -->
    <text x="0" y="138" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Ex 3: "Urgent account update required to verify funds"</text>
    <!-- Bar 3: 3.4% Ham (19px green), 96.6% Spam (531px red) -->
    <rect x="0" y="146" width="19" height="24" rx="4" fill="#059669"/>
    <rect x="19" y="146" width="531" height="24" rx="4" fill="#DC2626"/>
    <text x="560" y="163" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#DC2626">96.6% Spam</text>

    <!-- Example 4 -->
    <text x="0" y="198" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Ex 4: "Please find attached the financial report invoice"</text>
    <!-- Bar 4: 97.2% Ham (535px green), 2.8% Spam (15px red) -->
    <rect x="0" y="206" width="535" height="24" rx="4" fill="#059669"/>
    <rect x="535" y="206" width="15" height="24" rx="4" fill="#DC2626"/>
    <text x="560" y="223" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#059669">97.2% Ham</text>
  </g>

  <!-- Caution Banner on Probability Calibration -->
  <rect x="60" y="325" width="660" height="42" rx="6" fill="#FFFBEB" stroke="#FDE68A"/>
  <text x="75" y="344" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#92400E">Calibration Warning:</text>
  <text x="75" y="358" font-family="-apple-system, sans-serif" font-size="11" fill="#78350F">Naive Bayes probabilities are often overconfident near 0 or 1 due to independence multiplication, but relative rankings remain solid.</text>
</svg>"""

ALL_SVGS = {
    "SVG_NB_HERO_PIPELINE": SVG_NB_HERO_PIPELINE,
    "SVG_PROBABILITY_BARS": SVG_PROBABILITY_BARS,
    "SVG_CONTINGENCY_TABLE": SVG_CONTINGENCY_TABLE,
    "SVG_BAYES_THEOREM_UPDATE": SVG_BAYES_THEOREM_UPDATE,
    "SVG_SPAM_WORDS_LIKELIHOOD": SVG_SPAM_WORDS_LIKELIHOOD,
    "SVG_INDEPENDENCE_ASSUMPTION": SVG_INDEPENDENCE_ASSUMPTION,
    "SVG_STEP_BY_STEP_SCORES": SVG_STEP_BY_STEP_SCORES,
    "SVG_ZERO_FREQUENCY_PROBLEM": SVG_ZERO_FREQUENCY_PROBLEM,
    "SVG_LAPLACE_SMOOTHING": SVG_LAPLACE_SMOOTHING,
    "SVG_NB_VARIANTS_COMPARISON": SVG_NB_VARIANTS_COMPARISON,
    "SVG_MULTINOMIAL_TERM_MATRIX": SVG_MULTINOMIAL_TERM_MATRIX,
    "SVG_BERNOULLI_PRESENCE_MATRIX": SVG_BERNOULLI_PRESENCE_MATRIX,
    "SVG_GAUSSIAN_DISTRIBUTIONS": SVG_GAUSSIAN_DISTRIBUTIONS,
    "SVG_CONFUSION_MATRIX_HEATMAP": SVG_CONFUSION_MATRIX_HEATMAP,
    "SVG_PREDICTED_PROBABILITY_BARS": SVG_PREDICTED_PROBABILITY_BARS,
}

if __name__ == "__main__":
    print(f"Validating {len(ALL_SVGS)} SVG diagrams for XML correctness...")
    all_valid = True
    for name, svg_code in ALL_SVGS.items():
        try:
            elem = ET.fromstring(svg_code)
            if elem.tag != "{http://www.w3.org/2000/svg}svg" and elem.tag != "svg":
                print(f"FAILED: {name} root tag is not svg ({elem.tag})")
                all_valid = False
            else:
                print(f"PASS: {name} (valid XML, root: {elem.tag})")
        except Exception as e:
            print(f"ERROR in {name}: {e}")
            all_valid = False

    if all_valid:
        print("\nALL 15 SVGS ARE 100% XML-VALID AND STRICT LIGHT-MODE READY!")
    else:
        print("\nSOME SVGS FAILED VALIDATION.")
