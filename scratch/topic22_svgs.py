# Topic 22 SVG Visual Assets
# 20 High Quality, Valid XML, Responsive Vector Illustrations
# Strict Light Mode Colors, No HTML Named Entities

SVG_MAP = {}

# 1. Tuning Workflow (Fig 1.1)
SVG_MAP["__SVG_TUNING_WORKFLOW__"] = """<svg viewBox="0 0 900 240" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="240" fill="#F8FAFC" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <defs>
    <marker id="arr1" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#6366F1"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="450" y="30" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B" text-anchor="middle">The Hyperparameter Tuning Lifecycle</text>

  <!-- Node 1: Raw Data -->
  <rect x="25" y="70" width="95" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="25" y="70" width="95" height="28" rx="8" fill="#F1F5F9"/>
  <text x="72" y="88" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">1. DATASET</text>
  <text x="72" y="118" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Features (X)</text>
  <text x="72" y="136" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Labels (y)</text>
  <text x="72" y="158" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#6366F1" text-anchor="middle">Split Isolated</text>

  <line x1="120" y1="125" x2="148" y2="125" stroke="#6366F1" stroke-width="2" marker-end="url(#arr1)"/>

  <!-- Node 2: Candidate Space -->
  <rect x="150" y="70" width="105" height="110" rx="8" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="1.5"/>
  <rect x="150" y="70" width="105" height="28" rx="8" fill="#EEF2FF"/>
  <text x="202" y="88" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#3730A3" text-anchor="middle">2. SEARCH SPACE</text>
  <text x="202" y="118" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">k = [3, 5, 7, 9]</text>
  <text x="202" y="136" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">weights = [U, D]</text>
  <text x="202" y="158" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#4F46E5" text-anchor="middle">Candidate Grid</text>

  <line x1="255" y1="125" x2="283" y2="125" stroke="#6366F1" stroke-width="2" marker-end="url(#arr1)"/>

  <!-- Node 3: Train Models -->
  <rect x="285" y="70" width="105" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="285" y="70" width="105" height="28" rx="8" fill="#F1F5F9"/>
  <text x="337" y="88" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">3. FIT MODELS</text>
  <text x="337" y="118" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">K-Fold Splits</text>
  <text x="337" y="136" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Fit on K-1 folds</text>
  <text x="337" y="158" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#6366F1" text-anchor="middle">N_fits = N x K</text>

  <line x1="390" y1="125" x2="418" y2="125" stroke="#6366F1" stroke-width="2" marker-end="url(#arr1)"/>

  <!-- Node 4: Validate & Score -->
  <rect x="420" y="70" width="105" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="420" y="70" width="105" height="28" rx="8" fill="#F1F5F9"/>
  <text x="472" y="88" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">4. VALIDATE</text>
  <text x="472" y="118" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Predict holdout</text>
  <text x="472" y="136" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Record metric</text>
  <text x="472" y="158" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#6366F1" text-anchor="middle">Mean CV Score</text>

  <line x1="525" y1="125" x2="553" y2="125" stroke="#6366F1" stroke-width="2" marker-end="url(#arr1)"/>

  <!-- Node 5: Compare & Rank -->
  <rect x="555" y="70" width="105" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="555" y="70" width="105" height="28" rx="8" fill="#F1F5F9"/>
  <text x="607" y="88" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">5. COMPARE</text>
  <text x="607" y="118" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Rank configs</text>
  <text x="607" y="136" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Check stability</text>
  <text x="607" y="158" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#6366F1" text-anchor="middle">best_params_</text>

  <line x1="660" y1="125" x2="688" y2="125" stroke="#6366F1" stroke-width="2" marker-end="url(#arr1)"/>

  <!-- Node 6: Refit & Test -->
  <rect x="690" y="70" width="185" height="110" rx="8" fill="#FFFFFF" stroke="#86EFAC" stroke-width="2"/>
  <rect x="690" y="70" width="185" height="28" rx="8" fill="#DCFCE7"/>
  <text x="782" y="88" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#15803D" text-anchor="middle">6. REFIT &amp; FINAL TEST</text>
  <text x="782" y="115" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">1. Refit best on FULL train</text>
  <text x="782" y="135" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">2. Test once on untouched test set</text>
  <text x="782" y="160" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#16A34A" text-anchor="middle">Unbiased Generalization</text>

  <!-- Legend bottom -->
  <text x="450" y="215" font-family="-apple-system, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Cross-validation guides hyperparameter choice; the isolated test set proves true real-world generalization.</text>
</svg>"""

# 2. Parameters vs Hyperparameters (Fig 2.1)
SVG_MAP["__SVG_PARAMS_VS_HYPERPARAMS__"] = """<svg viewBox="0 0 880 260" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="260" fill="#F8FAFC" rx="12" stroke="#E2E8F0" stroke-width="1"/>

  <!-- Column 1: Model Parameters -->
  <rect x="40" y="30" width="380" height="200" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="40" y="30" width="380" height="38" rx="10" fill="#F1F5F9"/>
  <text x="230" y="54" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#1E293B" text-anchor="middle">MODEL PARAMETERS (Internal)</text>

  <text x="60" y="95" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">Who sets it?</text>
  <text x="170" y="95" font-family="-apple-system, sans-serif" font-size="12" fill="#0F172A">Learned automatically by the algorithm</text>

  <text x="60" y="125" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">When?</text>
  <text x="170" y="125" font-family="-apple-system, sans-serif" font-size="12" fill="#0F172A">During training / fitting (model.fit)</text>

  <text x="60" y="155" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">Source:</text>
  <text x="170" y="155" font-family="-apple-system, sans-serif" font-size="12" fill="#0F172A">Derived directly from training data</text>

  <text x="60" y="185" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">Examples:</text>
  <text x="170" y="185" font-family="-apple-system, sans-serif" font-size="12" fill="#0284C7">Weights (w), Biases (b), Tree split thresholds</text>

  <rect x="60" y="200" width="340" height="20" rx="4" fill="#F0F9FF"/>
  <text x="230" y="214" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#0369A1" text-anchor="middle">Saved in model attributes (e.g. coef_, intercept_)</text>

  <!-- Column 2: Hyperparameters -->
  <rect x="460" y="30" width="380" height="200" rx="10" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="2"/>
  <rect x="460" y="30" width="380" height="38" rx="10" fill="#EEF2FF"/>
  <text x="650" y="54" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#3730A3" text-anchor="middle">HYPERPARAMETERS (External Knobs)</text>

  <text x="480" y="95" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">Who sets it?</text>
  <text x="590" y="95" font-family="-apple-system, sans-serif" font-size="12" fill="#0F172A">Practitioner / Data Scientist</text>

  <text x="480" y="125" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">When?</text>
  <text x="590" y="125" font-family="-apple-system, sans-serif" font-size="12" fill="#0F172A">BEFORE training begins (instantiation)</text>

  <text x="480" y="155" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">Source:</text>
  <text x="590" y="155" font-family="-apple-system, sans-serif" font-size="12" fill="#0F172A">Experimentation, Grid/Random Search</text>

  <text x="480" y="185" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#475569">Examples:</text>
  <text x="590" y="185" font-family="-apple-system, sans-serif" font-size="12" fill="#6366F1">n_neighbors, max_depth, alpha, C, kernel</text>

  <rect x="480" y="200" width="340" height="20" rx="4" fill="#EEF2FF"/>
  <text x="650" y="214" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#4338CA" text-anchor="middle">Controls model capacity and learning mechanics</text>
</svg>"""

# 3. Settings Fit Spectrum (Fig 3.1)
SVG_MAP["__SVG_SETTINGS_FIT_SPECTRUM__"] = """<svg viewBox="0 0 900 240" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="240" fill="#F8FAFC" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="450" y="28" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B" text-anchor="middle">How Hyperparameter Settings Govern Model Generalization</text>

  <!-- Panel 1: Underfitting -->
  <rect x="30" y="50" width="260" height="170" rx="8" fill="#FFFFFF" stroke="#FCD34D" stroke-width="1.5"/>
  <rect x="30" y="50" width="260" height="30" rx="8" fill="#FEF3C7"/>
  <text x="160" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#92400E" text-anchor="middle">UNDERFITTING (High Bias)</text>
  <text x="50" y="105" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">KNN:</text>
  <text x="130" y="105" font-family="-apple-system, sans-serif" font-size="11" fill="#0F172A">k = 50 (Too smooth)</text>
  <text x="50" y="125" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">Tree:</text>
  <text x="130" y="125" font-family="-apple-system, sans-serif" font-size="11" fill="#0F172A">max_depth = 1 (Decision Stump)</text>
  <text x="50" y="145" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">Ridge:</text>
  <text x="130" y="145" font-family="-apple-system, sans-serif" font-size="11" fill="#0F172A">alpha = 1000.0 (Over-regularized)</text>
  <rect x="45" y="165" width="230" height="40" rx="6" fill="#FFFBEB"/>
  <text x="160" y="180" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">Train Error: HIGH | Val Error: HIGH</text>
  <text x="160" y="196" font-family="-apple-system, sans-serif" font-size="10" fill="#78350F" text-anchor="middle">Cannot capture underlying signal</text>

  <!-- Panel 2: Good Fit -->
  <rect x="320" y="50" width="260" height="170" rx="8" fill="#FFFFFF" stroke="#86EFAC" stroke-width="2"/>
  <rect x="320" y="50" width="260" height="30" rx="8" fill="#DCFCE7"/>
  <text x="450" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#166534" text-anchor="middle">OPTIMAL FIT (Sweet Spot)</text>
  <text x="340" y="105" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">KNN:</text>
  <text x="420" y="105" font-family="-apple-system, sans-serif" font-size="11" fill="#0F172A">k = 7 (Clean boundaries)</text>
  <text x="340" y="125" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">Tree:</text>
  <text x="420" y="125" font-family="-apple-system, sans-serif" font-size="11" fill="#0F172A">max_depth = 4 (Pruned tree)</text>
  <text x="340" y="145" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">Ridge:</text>
  <text x="420" y="145" font-family="-apple-system, sans-serif" font-size="11" fill="#0F172A">alpha = 1.0 (Balanced penalty)</text>
  <rect x="335" y="165" width="230" height="40" rx="6" fill="#F0FDF4"/>
  <text x="450" y="180" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#15803D" text-anchor="middle">Train Error: LOW | Val Error: LOW</text>
  <text x="450" y="196" font-family="-apple-system, sans-serif" font-size="10" fill="#14532D" text-anchor="middle">Discovers true pattern and generalizes</text>

  <!-- Panel 3: Overfitting -->
  <rect x="610" y="50" width="260" height="170" rx="8" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="1.5"/>
  <rect x="610" y="50" width="260" height="30" rx="8" fill="#FEE2E2"/>
  <text x="740" y="70" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#991B1B" text-anchor="middle">OVERFITTING (High Variance)</text>
  <text x="630" y="105" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">KNN:</text>
  <text x="710" y="105" font-family="-apple-system, sans-serif" font-size="11" fill="#0F172A">k = 1 (Memorizes noise)</text>
  <text x="630" y="125" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">Tree:</text>
  <text x="710" y="125" font-family="-apple-system, sans-serif" font-size="11" fill="#0F172A">max_depth = None (Unconstrained)</text>
  <text x="630" y="145" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#475569">Ridge:</text>
  <text x="710" y="145" font-family="-apple-system, sans-serif" font-size="11" fill="#0F172A">alpha = 0.0 (Unregularized OLS)</text>
  <rect x="625" y="165" width="230" height="40" rx="6" fill="#FEF2F2"/>
  <text x="740" y="180" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#B91C1C" text-anchor="middle">Train Error: ZERO | Val Error: HIGH</text>
  <text x="740" y="196" font-family="-apple-system, sans-serif" font-size="10" fill="#7F1D1D" text-anchor="middle">Fits random dataset noise</text>
</svg>"""

# 4. Data Split Roles (Fig 4.1)
SVG_MAP["__SVG_DATA_SPLIT_ROLES__"] = """<svg viewBox="0 0 880 230" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="230" fill="#F8FAFC" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="28" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B" text-anchor="middle">The Three Distinct Partitions in Hyperparameter Tuning</text>

  <!-- Complete Bar -->
  <g transform="translate(60, 50)">
    <!-- Train partition: 60% (456px) -->
    <rect x="0" y="0" width="456" height="50" rx="6" fill="#EEF2FF" stroke="#6366F1" stroke-width="2"/>
    <text x="228" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#3730A3" text-anchor="middle">TRAINING SET (60%)</text>
    <text x="228" y="42" font-family="-apple-system, sans-serif" font-size="10.5" fill="#4F46E5" text-anchor="middle">Used to learn internal model parameters (weights, splits)</text>

    <!-- Validation partition: 20% (152px) -->
    <rect x="466" y="0" width="142" height="50" rx="6" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
    <text x="537" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#92400E" text-anchor="middle">VALIDATION (20%)</text>
    <text x="537" y="42" font-family="-apple-system, sans-serif" font-size="10.5" fill="#B45309" text-anchor="middle">Compare configs</text>

    <!-- Test partition: 20% (152px) -->
    <rect x="618" y="0" width="142" height="50" rx="6" fill="#DCFCE7" stroke="#10B981" stroke-width="2"/>
    <text x="689" y="25" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#065F46" text-anchor="middle">TEST SET (20%)</text>
    <text x="689" y="42" font-family="-apple-system, sans-serif" font-size="10.5" fill="#047857" text-anchor="middle">Final verification</text>
  </g>

  <!-- Explanation cards below -->
  <g transform="translate(60, 120)">
    <!-- Card 1 -->
    <rect x="0" y="0" width="240" height="90" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="15" y="24" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#3730A3">Training Set Role</text>
    <text x="15" y="46" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">Fitted repeatedly for every</text>
    <text x="15" y="62" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">candidate setting tested.</text>
    <text x="15" y="80" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#6366F1">Algorithm sees all labels here.</text>

    <!-- Card 2 -->
    <rect x="260" y="0" width="240" height="90" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="275" y="24" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#B45309">Validation Set Role</text>
    <text x="275" y="46" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">Provides an objective score to</text>
    <text x="275" y="62" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">pick the winner (e.g. k=7 vs 9).</text>
    <text x="275" y="80" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#D97706">May be replaced by K-Fold CV.</text>

    <!-- Card 3 -->
    <rect x="520" y="0" width="240" height="90" rx="8" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.5"/>
    <text x="535" y="24" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#047857">Holdout Test Set Role</text>
    <text x="535" y="46" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">LOCKED in a vault until tuning</text>
    <text x="535" y="62" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">is 100% finished. Evaluated once.</text>
    <text x="535" y="80" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#15803D">Guarantees zero selection bias!</text>
  </g>
</svg>"""

# 5. Manual Tuning Curve (Fig 5.1)
# Uses genuine numbers from executed code:
# k=1: Train 1.0000, CV 0.9429
# k=3: Train 0.9780, CV 0.9692
# k=5: Train 0.9736, CV 0.9670
# k=7: Train 0.9758, CV 0.9714 (Best)
# k=9: Train 0.9736, CV 0.9692
# k=11: Train 0.9714, CV 0.9626
# k=15: Train 0.9692, CV 0.9626
# k=21: Train 0.9648, CV 0.9604
# k=31: Train 0.9626, CV 0.9538
SVG_MAP["__SVG_MANUAL_TUNING_CURVE__"] = """<svg viewBox="0 0 880 320" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Manual Tuning Experiment: KNN n_neighbors vs Accuracy (Breast Cancer Dataset)</text>

  <!-- Plot Area: x: 100 -> 800 (width 700), y: 50 -> 260 (height 210) -->
  <!-- Y-axis: 0.93 to 1.01 (range 0.08, height 210 -> 26.25 px per 0.01) -->
  <!-- Y mapping: y_px = 260 - (score - 0.93) / 0.08 * 210 -->
  <!-- 0.94 -> 233.75, 0.95 -> 207.5, 0.96 -> 181.25, 0.97 -> 155.0, 0.98 -> 128.75, 0.99 -> 102.5, 1.00 -> 76.25 -->

  <!-- Grid lines -->
  <line x1="100" y1="234" x2="800" y2="234" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="238" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.94</text>

  <line x1="100" y1="208" x2="800" y2="208" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="212" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.95</text>

  <line x1="100" y1="181" x2="800" y2="181" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="185" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.96</text>

  <line x1="100" y1="155" x2="800" y2="155" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="159" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.97</text>

  <line x1="100" y1="129" x2="800" y2="129" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="133" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.98</text>

  <line x1="100" y1="76" x2="800" y2="76" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="80" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">1.00</text>

  <!-- Axes -->
  <line x1="100" y1="260" x2="800" y2="260" stroke="#CBD5E1" stroke-width="1.5"/>
  <line x1="100" y1="50" x2="100" y2="260" stroke="#CBD5E1" stroke-width="1.5"/>

  <!-- X ticks: k in [1, 3, 5, 7, 9, 11, 15, 21, 31] -->
  <!-- X mapping: x = 100 + (k - 1) / 30 * 680 -->
  <!-- k=1: 100, k=3: 145, k=5: 191, k=7: 236, k=9: 281, k=11: 327, k=15: 417, k=21: 553, k=31: 780 -->

  <!-- Training Score Line: (1, 1.0000), (3, 0.9780), (5, 0.9736), (7, 0.9758), (9, 0.9736), (11, 0.9714), (15, 0.9692), (21, 0.9648), (31, 0.9626) -->
  <!-- Ys: 76.25, 134.0, 145.5, 139.8, 145.5, 151.3, 157.1, 168.6, 174.4 -->
  <polyline points="100,76 145,134 191,146 236,140 281,146 327,151 417,157 553,169 780,174" fill="none" stroke="#F43F5E" stroke-width="2.5" stroke-dasharray="4 3"/>

  <!-- 5-Fold CV Score Line: (1, 0.9429), (3, 0.9692), (5, 0.9670), (7, 0.9714), (9, 0.9692), (11, 0.9626), (15, 0.9626), (21, 0.9604), (31, 0.9538) -->
  <!-- Ys: 226.1, 157.1, 162.9, 151.3, 157.1, 174.4, 174.4, 180.2, 197.5 -->
  <polyline points="100,226 145,157 191,163 236,151 281,157 327,174 417,174 553,180 780,198" fill="none" stroke="#4F46E5" stroke-width="3"/>

  <!-- Points on CV curve -->
  <circle cx="100" cy="226" r="4.5" fill="#4F46E5"/>
  <circle cx="145" cy="157" r="4.5" fill="#4F46E5"/>
  <circle cx="191" cy="163" r="4.5" fill="#4F46E5"/>
  <circle cx="236" cy="151" r="7" fill="#10B981" stroke="#065F46" stroke-width="2"/>
  <circle cx="281" cy="157" r="4.5" fill="#4F46E5"/>
  <circle cx="327" cy="174" r="4.5" fill="#4F46E5"/>
  <circle cx="417" cy="174" r="4.5" fill="#4F46E5"/>
  <circle cx="553" cy="180" r="4.5" fill="#4F46E5"/>
  <circle cx="780" cy="198" r="4.5" fill="#4F46E5"/>

  <!-- Annotation for Best Point k=7 -->
  <rect x="245" y="105" width="160" height="38" rx="6" fill="#EEF2FF" stroke="#6366F1" stroke-width="1.5"/>
  <text x="325" y="120" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#3730A3" text-anchor="middle">PEAK: k = 7</text>
  <text x="325" y="135" font-family="-apple-system, sans-serif" font-size="10" fill="#4F46E5" text-anchor="middle">CV Accuracy = 0.9714</text>
  <line x1="245" y1="125" x2="238" y2="145" stroke="#6366F1" stroke-width="1.5"/>

  <!-- Annotation for k=1 Overfitting -->
  <rect x="110" y="65" width="130" height="30" rx="4" fill="#FFE4E6" stroke="#FDA4AF" stroke-width="1"/>
  <text x="175" y="78" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#9F1239" text-anchor="middle">k=1: Memorizes Noise</text>
  <text x="175" y="90" font-family="-apple-system, sans-serif" font-size="9" fill="#9F1239" text-anchor="middle">Train: 1.000 | Val: 0.943</text>

  <!-- X axis labels -->
  <text x="100" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">k=1</text>
  <text x="145" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">k=3</text>
  <text x="191" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">k=5</text>
  <text x="236" y="278" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#15803D" text-anchor="middle">k=7*</text>
  <text x="281" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">k=9</text>
  <text x="327" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">k=11</text>
  <text x="417" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">k=15</text>
  <text x="553" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">k=21</text>
  <text x="780" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">k=31</text>

  <text x="450" y="302" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E293B" text-anchor="middle">Candidate Values (n_neighbors)</text>

  <!-- Legend -->
  <g transform="translate(560, 48)">
    <line x1="0" y1="10" x2="25" y2="10" stroke="#F43F5E" stroke-width="2.5" stroke-dasharray="4 3"/>
    <text x="32" y="14" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Training Accuracy</text>
    <line x1="140" y1="10" x2="165" y2="10" stroke="#4F46E5" stroke-width="3"/>
    <circle cx="152.5" cy="10" r="4" fill="#4F46E5"/>
    <text x="172" y="14" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#3730A3">5-Fold CV Accuracy</text>
  </g>
</svg>"""

# 6. Search Space Types (Fig 6.1)
SVG_MAP["__SVG_SEARCH_SPACE_TYPES__"] = """<svg viewBox="0 0 880 230" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="230" fill="#F8FAFC" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="28" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#1E293B" text-anchor="middle">Anatomy of Hyperparameter Search Spaces</text>

  <!-- Box 1: Discrete / Integer -->
  <rect x="30" y="50" width="190" height="155" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="30" y="50" width="190" height="30" rx="8" fill="#F1F5F9"/>
  <text x="125" y="70" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#1E293B" text-anchor="middle">1. INTEGER / DISCRETE</text>
  <text x="45" y="100" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">Parameters taking whole numbers:</text>
  <text x="45" y="122" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#6366F1">• n_neighbors: [3, 5, 7, 9]</text>
  <text x="45" y="140" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#6366F1">• max_depth: [3, 5, 8, 12]</text>
  <text x="45" y="158" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#6366F1">• n_estimators: [50, 100, 200]</text>
  <text x="45" y="185" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">Must be strictly integer (no floats)</text>

  <!-- Box 2: Continuous -->
  <rect x="240" y="50" width="190" height="155" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="240" y="50" width="190" height="30" rx="8" fill="#F1F5F9"/>
  <text x="335" y="70" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#1E293B" text-anchor="middle">2. CONTINUOUS</text>
  <text x="255" y="100" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">Real-valued float parameters:</text>
  <text x="255" y="122" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0284C7">• learning_rate: (0.001, 0.3)</text>
  <text x="255" y="140" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0284C7">• l1_ratio: [0.0, 1.0]</text>
  <text x="255" y="158" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0284C7">• min_impurity_decrease</text>
  <text x="255" y="185" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">Infinite possible values inside range</text>

  <!-- Box 3: Categorical -->
  <rect x="450" y="50" width="190" height="155" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="450" y="50" width="190" height="30" rx="8" fill="#F1F5F9"/>
  <text x="545" y="70" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#1E293B" text-anchor="middle">3. CATEGORICAL</text>
  <text x="465" y="100" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">Discrete qualitative options:</text>
  <text x="465" y="122" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#D97706">• weights: ['uniform', 'distance']</text>
  <text x="465" y="140" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#D97706">• kernel: ['linear', 'rbf', 'poly']</text>
  <text x="465" y="158" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#D97706">• solver: ['lbfgs', 'saga']</text>
  <text x="465" y="185" font-family="-apple-system, sans-serif" font-size="9.5" fill="#64748B">Often dictates which other knobs apply</text>

  <!-- Box 4: Logarithmic Space -->
  <rect x="660" y="50" width="190" height="155" rx="8" fill="#FFFFFF" stroke="#A855F7" stroke-width="1.5"/>
  <rect x="660" y="50" width="190" height="30" rx="8" fill="#FDF4FF"/>
  <text x="755" y="70" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#7E22CE" text-anchor="middle">4. LOGARITHMIC</text>
  <text x="675" y="100" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">Spans orders of magnitude:</text>
  <text x="675" y="122" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#9333EA">• C: [0.001, 0.01, 0.1, 1, 10, 100]</text>
  <text x="675" y="140" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#9333EA">• alpha: logspace(-4, 2, 7)</text>
  <text x="675" y="158" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#9333EA">• gamma: loguniform(1e-4, 1e0)</text>
  <text x="675" y="185" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="600" fill="#7E22CE">Uniform linear steps miss small scales!</text>
</svg>"""

# 7. Grid Search Combinations (Fig 7.1)
SVG_MAP["__SVG_GRID_SEARCH_COMBINATIONS__"] = """<svg viewBox="0 0 880 260" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="260" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Grid Search: Full Cartesian Product Evaluation</text>

  <!-- Left: Formula and workload explanation -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="320" height="180" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="16" y="26" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#3730A3">Search Complexity Calculation</text>
    <text x="16" y="52" font-family="-apple-system, sans-serif" font-size="11.5" fill="#334155">• Hyperparameter 1: k ∈ {3, 5, 7, 9} (n₁ = 4)</text>
    <text x="16" y="72" font-family="-apple-system, sans-serif" font-size="11.5" fill="#334155">• Hyperparameter 2: weights ∈ {uni, dist} (n₂ = 2)</text>
    <text x="16" y="92" font-family="-apple-system, sans-serif" font-size="11.5" fill="#334155">• Hyperparameter 3: p ∈ {1, 2} (n₃ = 2)</text>
    <line x1="16" y1="105" x2="300" y2="105" stroke="#E2E8F0" stroke-width="1"/>
    <text x="16" y="125" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" fill="#0F172A">Total Configurations = 4 × 2 × 2 = 16</text>
    <text x="16" y="145" font-family="-apple-system, sans-serif" font-size="11.5" fill="#475569">With 5-Fold Cross-Validation (K = 5):</text>
    <text x="16" y="165" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#4F46E5">Total Model Fits = 16 × 5 = 80 fits</text>
  </g>

  <!-- Right: 2D Grid Visual (k vs weights) -->
  <g transform="translate(420, 45)">
    <!-- Axes -->
    <line x1="80" y1="160" x2="400" y2="160" stroke="#64748B" stroke-width="1.5"/>
    <line x1="80" y1="30" x2="80" y2="160" stroke="#64748B" stroke-width="1.5"/>
    <text x="240" y="195" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#1E293B" text-anchor="middle">n_neighbors (k)</text>
    <text x="25" y="95" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#1E293B" text-anchor="middle" transform="rotate(-90 25 95)">weights</text>

    <!-- X ticks -->
    <text x="120" y="176" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569" text-anchor="middle">3</text>
    <text x="200" y="176" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569" text-anchor="middle">5</text>
    <text x="280" y="176" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569" text-anchor="middle">7</text>
    <text x="360" y="176" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569" text-anchor="middle">9</text>

    <!-- Y ticks -->
    <text x="70" y="125" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569" text-anchor="end">'uniform'</text>
    <text x="70" y="65" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569" text-anchor="end">'distance'</text>

    <!-- Grid lines -->
    <line x1="120" y1="30" x2="120" y2="160" stroke="#EEF2FF" stroke-width="1.5" stroke-dasharray="2 2"/>
    <line x1="200" y1="30" x2="200" y2="160" stroke="#EEF2FF" stroke-width="1.5" stroke-dasharray="2 2"/>
    <line x1="280" y1="30" x2="280" y2="160" stroke="#EEF2FF" stroke-width="1.5" stroke-dasharray="2 2"/>
    <line x1="360" y1="30" x2="360" y2="160" stroke="#EEF2FF" stroke-width="1.5" stroke-dasharray="2 2"/>

    <line x1="80" y1="120" x2="400" y2="120" stroke="#EEF2FF" stroke-width="1.5" stroke-dasharray="2 2"/>
    <line x1="80" y1="60" x2="400" y2="60" stroke="#EEF2FF" stroke-width="1.5" stroke-dasharray="2 2"/>

    <!-- Grid Nodes (All 8 evaluated) -->
    <circle cx="120" cy="120" r="7" fill="#6366F1"/>
    <circle cx="200" cy="120" r="7" fill="#6366F1"/>
    <!-- Winner: (7, uniform) -->
    <circle cx="280" cy="120" r="9" fill="#10B981" stroke="#047857" stroke-width="2.5"/>
    <circle cx="360" cy="120" r="7" fill="#6366F1"/>

    <circle cx="120" cy="60" r="7" fill="#6366F1"/>
    <circle cx="200" cy="60" r="7" fill="#6366F1"/>
    <circle cx="280" cy="60" r="7" fill="#6366F1"/>
    <circle cx="360" cy="60" r="7" fill="#6366F1"/>

    <!-- Annotation on winner -->
    <text x="280" y="100" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Best: (7, uniform)</text>
  </g>
</svg>"""

# 8. Grid Search vs Random Search (Fig 9.1 / 11.1)
SVG_MAP["__SVG_GRID_VS_RANDOM_SEARCH__"] = """<svg viewBox="0 0 880 320" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Grid Search vs. Random Search in a 2D Parameter Space</text>

  <!-- Left: Grid Search (9 trials) -->
  <g transform="translate(60, 45)">
    <rect x="0" y="0" width="340" height="235" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="170" y="24" font-family="-apple-system, sans-serif" font-size="12.5" font-weight="800" fill="#3730A3" text-anchor="middle">GRID SEARCH (9 Evaluations)</text>

    <!-- Axes -->
    <line x1="50" y1="180" x2="290" y2="180" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="50" y1="40" x2="50" y2="180" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="170" y="200" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle">Important Parameter (e.g. learning_rate)</text>
    <text x="20" y="110" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle" transform="rotate(-90 20 110)">Unimportant (e.g. seed)</text>

    <!-- Grid points (3x3 = 9) -->
    <!-- X values: 90, 170, 250 (Only 3 distinct values explored!) -->
    <!-- Y values: 60, 110, 160 (Only 3 distinct values explored!) -->
    <circle cx="90" cy="60" r="6" fill="#6366F1"/>
    <circle cx="170" cy="60" r="6" fill="#6366F1"/>
    <circle cx="250" cy="60" r="6" fill="#6366F1"/>

    <circle cx="90" cy="110" r="6" fill="#6366F1"/>
    <circle cx="170" cy="110" r="6" fill="#6366F1"/>
    <circle cx="250" cy="110" r="6" fill="#6366F1"/>

    <circle cx="90" cy="160" r="6" fill="#6366F1"/>
    <circle cx="170" cy="160" r="6" fill="#6366F1"/>
    <circle cx="250" cy="160" r="6" fill="#6366F1"/>

    <text x="170" y="222" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#E11D48" text-anchor="middle">Only 3 distinct values tested along X axis!</text>
  </g>

  <!-- Right: Random Search (9 trials) -->
  <g transform="translate(480, 45)">
    <rect x="0" y="0" width="340" height="235" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="170" y="24" font-family="-apple-system, sans-serif" font-size="12.5" font-weight="800" fill="#047857" text-anchor="middle">RANDOM SEARCH (9 Evaluations)</text>

    <!-- Axes -->
    <line x1="50" y1="180" x2="290" y2="180" stroke="#94A3B8" stroke-width="1.5"/>
    <line x1="50" y1="40" x2="50" y2="180" stroke="#94A3B8" stroke-width="1.5"/>
    <text x="170" y="200" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle">Important Parameter (e.g. learning_rate)</text>
    <text x="20" y="110" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle" transform="rotate(-90 20 110)">Unimportant (e.g. seed)</text>

    <!-- 9 randomly distributed points -->
    <circle cx="75" cy="145" r="6" fill="#10B981"/>
    <circle cx="98" cy="72" r="6" fill="#10B981"/>
    <circle cx="124" cy="165" r="6" fill="#10B981"/>
    <circle cx="150" cy="95" r="6" fill="#10B981"/>
    <circle cx="182" cy="50" r="6" fill="#10B981"/>
    <circle cx="205" cy="130" r="6" fill="#10B981"/>
    <!-- Winner near optimum: -->
    <circle cx="230" cy="85" r="8" fill="#F59E0B" stroke="#B45309" stroke-width="2"/>
    <circle cx="255" cy="155" r="6" fill="#10B981"/>
    <circle cx="278" cy="115" r="6" fill="#10B981"/>

    <text x="170" y="222" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#047857" text-anchor="middle">9 DISTINCT values explored along X axis!</text>
  </g>
</svg>"""

# 9. K-Fold Cross-Validation Diagram (Fig 12.1)
SVG_MAP["__SVG_KFOLD_TUNING_DIAGRAM__"] = """<svg viewBox="0 0 880 260" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="260" fill="#F8FAFC" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">5-Fold Cross-Validation: Rotating Validation Sets</text>

  <!-- 5 Iteration Rows -->
  <!-- Width: 500px, 5 folds = 100px each -->
  <!-- Start X: 160, Start Y: 45, Row height: 26, gap: 10 -->
  <g transform="translate(140, 45)">
    <!-- Fold 1 -->
    <text x="-15" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="end">Split 1</text>
    <rect x="0" y="0" width="100" height="26" rx="4" fill="#FDE68A" stroke="#D97706" stroke-width="1.5"/>
    <text x="50" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#92400E" text-anchor="middle">Val (Fold 1)</text>
    <rect x="105" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
    <rect x="210" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
    <rect x="315" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
    <rect x="420" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
    <text x="310" y="17" font-family="-apple-system, sans-serif" font-size="10.5" fill="#4338CA" text-anchor="middle">Training Folds (80% of data)</text>
    <text x="545" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#1E293B">Score₁ = 0.967</text>

    <!-- Fold 2 -->
    <g transform="translate(0, 34)">
      <text x="-15" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="end">Split 2</text>
      <rect x="0" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="105" y="0" width="100" height="26" rx="4" fill="#FDE68A" stroke="#D97706" stroke-width="1.5"/>
      <text x="155" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#92400E" text-anchor="middle">Val (Fold 2)</text>
      <rect x="210" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="315" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="420" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <text x="545" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#1E293B">Score₂ = 0.989</text>
    </g>

    <!-- Fold 3 -->
    <g transform="translate(0, 68)">
      <text x="-15" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="end">Split 3</text>
      <rect x="0" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="105" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="210" y="0" width="100" height="26" rx="4" fill="#FDE68A" stroke="#D97706" stroke-width="1.5"/>
      <text x="260" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#92400E" text-anchor="middle">Val (Fold 3)</text>
      <rect x="315" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="420" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <text x="545" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#1E293B">Score₃ = 0.978</text>
    </g>

    <!-- Fold 4 -->
    <g transform="translate(0, 102)">
      <text x="-15" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="end">Split 4</text>
      <rect x="0" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="105" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="210" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="315" y="0" width="100" height="26" rx="4" fill="#FDE68A" stroke="#D97706" stroke-width="1.5"/>
      <text x="365" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#92400E" text-anchor="middle">Val (Fold 4)</text>
      <rect x="420" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <text x="545" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#1E293B">Score₄ = 0.945</text>
    </g>

    <!-- Fold 5 -->
    <g transform="translate(0, 136)">
      <text x="-15" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="end">Split 5</text>
      <rect x="0" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="105" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="210" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="315" y="0" width="100" height="26" rx="4" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1"/>
      <rect x="420" y="0" width="100" height="26" rx="4" fill="#FDE68A" stroke="#D97706" stroke-width="1.5"/>
      <text x="470" y="17" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#92400E" text-anchor="middle">Val (Fold 5)</text>
      <text x="545" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" fill="#1E293B">Score₅ = 0.978</text>
    </g>
  </g>

  <!-- Summary Box at Bottom -->
  <rect x="140" y="215" width="600" height="32" rx="6" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1"/>
  <text x="440" y="235" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#166534" text-anchor="middle">Aggregated CV Metric = Mean(Scores) ± Std = 0.9714 ± 0.0192</text>
</svg>"""

# 10. CV Score Variability (Fig 13.1)
SVG_MAP["__SVG_CV_SCORE_VARIABILITY__"] = """<svg viewBox="0 0 880 280" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="280" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Candidate Configurations with Cross-Validation Error Bars (Mean ± 1 SD)</text>

  <!-- Plot area: x: 120 -> 780, y: 50 -> 220 -->
  <!-- Y-axis: 0.94 to 1.00 (height 170 -> 28.3 px per 0.01) -->
  <line x1="120" y1="220" x2="780" y2="220" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="120" y1="163" x2="780" y2="163" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="120" y1="107" x2="780" y2="107" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="120" y1="50" x2="780" y2="50" stroke="#F1F5F9" stroke-width="1"/>

  <text x="110" y="224" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.94</text>
  <text x="110" y="167" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.96</text>
  <text x="110" y="111" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.98</text>
  <text x="110" y="54" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">1.00</text>

  <!-- Config 1: k=1, uni (Mean 0.9429, std 0.0213) -->
  <!-- Mean Y: 220 - (0.9429-0.94)/0.06*170 = 211.8 -->
  <!-- Top Y: 220 - (0.9642-0.94)/0.06*170 = 151.4 -->
  <!-- Bot Y: 220 - (0.9216-0.94)/0.06*170 = 220 (clipped) -->
  <g transform="translate(180, 0)">
    <line x1="0" y1="151" x2="0" y2="220" stroke="#64748B" stroke-width="2"/>
    <line x1="-8" y1="151" x2="8" y2="151" stroke="#64748B" stroke-width="2"/>
    <circle cx="0" cy="212" r="6" fill="#EF4444"/>
    <text x="0" y="240" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#475569" text-anchor="middle">k=1 (uni)</text>
    <text x="0" y="255" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">0.943 ± 0.021</text>
  </g>

  <!-- Config 2: k=3, uni (Mean 0.9692, std 0.0245) -->
  <!-- Mean Y: 220 - (0.9692-0.94)/0.06*170 = 137.3 -->
  <!-- Top: 137.3 - 69.4 = 67.9, Bot: 137.3 + 69.4 = 206.7 -->
  <g transform="translate(300, 0)">
    <line x1="0" y1="68" x2="0" y2="207" stroke="#64748B" stroke-width="2"/>
    <line x1="-8" y1="68" x2="8" y2="68" stroke="#64748B" stroke-width="2"/>
    <line x1="-8" y1="207" x2="8" y2="207" stroke="#64748B" stroke-width="2"/>
    <circle cx="0" cy="137" r="6" fill="#6366F1"/>
    <text x="0" y="240" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#475569" text-anchor="middle">k=3 (uni)</text>
    <text x="0" y="255" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">0.969 ± 0.025</text>
  </g>

  <!-- Config 3: k=7, uni (BEST) (Mean 0.9714, std 0.0192) -->
  <!-- Mean Y: 220 - (0.9714-0.94)/0.06*170 = 131.0 -->
  <!-- Top: 131.0 - 54.4 = 76.6, Bot: 131.0 + 54.4 = 185.4 -->
  <g transform="translate(420, 0)">
    <line x1="0" y1="77" x2="0" y2="185" stroke="#10B981" stroke-width="2.5"/>
    <line x1="-10" y1="77" x2="10" y2="77" stroke="#10B981" stroke-width="2.5"/>
    <line x1="-10" y1="185" x2="10" y2="185" stroke="#10B981" stroke-width="2.5"/>
    <circle cx="0" cy="131" r="8" fill="#10B981" stroke="#065F46" stroke-width="2"/>
    <text x="0" y="240" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#047857" text-anchor="middle">k=7 (uni)*</text>
    <text x="0" y="255" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">0.971 ± 0.019</text>
  </g>

  <!-- Config 4: k=9, dist (Mean 0.9692, std 0.0162) -->
  <!-- Mean Y: 137.3 -->
  <!-- Top: 137.3 - 45.9 = 91.4, Bot: 137.3 + 45.9 = 183.2 -->
  <g transform="translate(540, 0)">
    <line x1="0" y1="91" x2="0" y2="183" stroke="#64748B" stroke-width="2"/>
    <line x1="-8" y1="91" x2="8" y2="91" stroke="#64748B" stroke-width="2"/>
    <line x1="-8" y1="183" x2="8" y2="183" stroke="#64748B" stroke-width="2"/>
    <circle cx="0" cy="137" r="6" fill="#6366F1"/>
    <text x="0" y="240" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#475569" text-anchor="middle">k=9 (dist)</text>
    <text x="0" y="255" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">0.969 ± 0.016</text>
  </g>

  <!-- Config 5: k=31, uni (Mean 0.9538, std 0.0235) -->
  <!-- Mean Y: 220 - (0.9538-0.94)/0.06*170 = 180.9 -->
  <g transform="translate(660, 0)">
    <line x1="0" y1="114" x2="0" y2="247" stroke="#64748B" stroke-width="2"/>
    <line x1="-8" y1="114" x2="8" y2="114" stroke="#64748B" stroke-width="2"/>
    <line x1="-8" y1="247" x2="8" y2="247" stroke="#64748B" stroke-width="2"/>
    <circle cx="0" cy="181" r="6" fill="#F59E0B"/>
    <text x="0" y="240" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#475569" text-anchor="middle">k=31 (uni)</text>
    <text x="0" y="255" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">0.954 ± 0.024</text>
  </g>
</svg>"""

# 11. Algorithm Hyperparameters Map (Fig 14.1)
SVG_MAP["__SVG_ALGORITHM_HYPERPARAMS_MAP__"] = """<svg viewBox="0 0 900 300" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="300" fill="#F8FAFC" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="450" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Core Hyperparameter Map Across Machine Learning Algorithms</text>

  <!-- 6 algorithm cards in 2x3 grid -->
  <!-- Row 1 -->
  <!-- Card 1: KNN -->
  <g transform="translate(25, 45)">
    <rect x="0" y="0" width="270" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="270" height="26" rx="8" fill="#EEF2FF"/>
    <text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#3730A3">K-Nearest Neighbors (KNN)</text>
    <text x="12" y="46" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">n_neighbors:</tspan> Low=Overfit, High=Smooth</text>
    <text x="12" y="66" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">weights:</tspan> 'uniform' vs 'distance'</text>
    <text x="12" y="86" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">p:</tspan> 1 (Manhattan) or 2 (Euclidean)</text>
    <text x="12" y="102" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#4F46E5">Critical: Features MUST be scaled first!</text>
  </g>

  <!-- Card 2: Decision Trees -->
  <g transform="translate(315, 45)">
    <rect x="0" y="0" width="270" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="270" height="26" rx="8" fill="#FEF3C7"/>
    <text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#92400E">Decision Trees</text>
    <text x="12" y="46" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">max_depth:</tspan> Controls tree tree depth</text>
    <text x="12" y="66" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">min_samples_split:</tspan> Min data to split node</text>
    <text x="12" y="86" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">min_samples_leaf:</tspan> Min data in leaf</text>
    <text x="12" y="102" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#D97706">Higher leaf/split values prevent overfitting</text>
  </g>

  <!-- Card 3: Random Forest -->
  <g transform="translate(605, 45)">
    <rect x="0" y="0" width="270" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="270" height="26" rx="8" fill="#DCFCE7"/>
    <text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#166534">Random Forest</text>
    <text x="12" y="46" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">n_estimators:</tspan> Trees (100 to 500, higher=safer)</text>
    <text x="12" y="66" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">max_features:</tspan> 'sqrt' or 'log2' (decorrelation)</text>
    <text x="12" y="86" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">max_depth &amp; min_samples_leaf:</tspan> Tree pruning</text>
    <text x="12" y="102" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#15803D">Ensemble stabilizes variance over single trees</text>
  </g>

  <!-- Row 2 -->
  <!-- Card 4: SVM -->
  <g transform="translate(25, 170)">
    <rect x="0" y="0" width="270" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="270" height="26" rx="8" fill="#FCE7F3"/>
    <text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#9D174D">Support Vector Machine (SVM)</text>
    <text x="12" y="46" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">C:</tspan> Penalty (High C = small margin, overfit)</text>
    <text x="12" y="66" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">kernel:</tspan> 'linear', 'rbf', 'poly'</text>
    <text x="12" y="86" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">gamma:</tspan> RBF radius (High gamma = tight island)</text>
    <text x="12" y="102" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#BE185D">Tune C and gamma on log scale [1e-3, 1e2]</text>
  </g>

  <!-- Card 5: Logistic Regression / Ridge / Lasso -->
  <g transform="translate(315, 170)">
    <rect x="0" y="0" width="270" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="270" height="26" rx="8" fill="#E0F2FE"/>
    <text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#0369A1">Linear Models (Ridge / Lasso / LogReg)</text>
    <text x="12" y="46" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">alpha (Ridge/Lasso):</tspan> Penalty strength</text>
    <text x="12" y="66" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">C (LogisticRegression):</tspan> Inverse alpha (1/λ)</text>
    <text x="12" y="86" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">penalty:</tspan> 'l1', 'l2', 'elasticnet'</text>
    <text x="12" y="102" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#0284C7">Ensure solver matches penalty (e.g. 'saga' for L1)</text>
  </g>

  <!-- Card 6: Gradient Boosting -->
  <g transform="translate(605, 170)">
    <rect x="0" y="0" width="270" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="270" height="26" rx="8" fill="#FDF4FF"/>
    <text x="12" y="18" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#7E22CE">Gradient Boosting</text>
    <text x="12" y="46" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">learning_rate:</tspan> Shrinkage per tree (0.01 - 0.2)</text>
    <text x="12" y="66" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">n_estimators:</tspan> Sequential trees added</text>
    <text x="12" y="86" font-family="-apple-system, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="700">max_depth:</tspan> Shallow trees (typically 3 to 6)</text>
    <text x="12" y="102" font-family="-apple-system, sans-serif" font-size="9" font-weight="600" fill="#9333EA">Inverse relationship: Low rate requires more trees</text>
  </g>
</svg>"""

# 12. Metric Selection Guide (Fig 15.1)
SVG_MAP["__SVG_METRIC_SELECTION_GUIDE__"] = """<svg viewBox="0 0 880 250" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="250" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Scoring Metric Selector: Aligning the Optimizer with Problem Reality</text>

  <!-- Left: Classification Branch -->
  <g transform="translate(40, 45)">
    <rect x="0" y="0" width="380" height="185" rx="8" fill="#F8FAFC" stroke="#C7D2FE" stroke-width="1.5"/>
    <rect x="0" y="0" width="380" height="30" rx="8" fill="#EEF2FF"/>
    <text x="190" y="20" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#3730A3" text-anchor="middle">CLASSIFICATION METRICS</text>

    <text x="15" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E293B">Accuracy ('accuracy'):</text>
    <text x="15" y="68" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">Only suitable when classes are balanced (e.g. 50/50). Misleading on skew!</text>

    <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E293B">Precision ('precision') vs Recall ('recall'):</text>
    <text x="15" y="108" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569"><tspan font-weight="600">Recall:</tspan> Costly False Negatives (Cancer, fraud detection).</text>
    <text x="15" y="124" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569"><tspan font-weight="600">Precision:</tspan> Costly False Positives (Spam filters, customer alerts).</text>

    <text x="15" y="148" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E293B">F1 Score ('f1') &amp; ROC-AUC ('roc_auc'):</text>
    <text x="15" y="164" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569"><tspan font-weight="600">F1:</tspan> Harmonic balance. <tspan font-weight="600">ROC-AUC:</tspan> Ranking quality across all thresholds.</text>
  </g>

  <!-- Right: Regression Branch -->
  <g transform="translate(460, 45)">
    <rect x="0" y="0" width="380" height="185" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="380" height="30" rx="8" fill="#F1F5F9"/>
    <text x="190" y="20" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#334155" text-anchor="middle">REGRESSION METRICS</text>

    <text x="15" y="52" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E293B">Mean Absolute Error ('neg_mean_absolute_error'):</text>
    <text x="15" y="68" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">Linear penalty. Robust to outliers. In target units ($).</text>

    <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E293B">Root Mean Squared Error ('neg_root_mean_squared_error'):</text>
    <text x="15" y="108" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">Heavy quadratic penalty on large errors. Use when big misses are disastrous.</text>

    <text x="15" y="132" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E293B">R-Squared ('r2'):</text>
    <text x="15" y="148" font-family="-apple-system, sans-serif" font-size="10.5" fill="#475569">Variance explained relative to horizontal mean baseline.</text>

    <rect x="15" y="158" width="350" height="20" rx="4" fill="#FEF3C7"/>
    <text x="190" y="172" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#92400E" text-anchor="middle">Notice: Scikit-learn negates loss metrics ('neg_...') so greater is better!</text>
  </g>
</svg>"""

# 13. Safe vs Unsafe Model Selection (Fig 16.1)
SVG_MAP["__SVG_SAFE_MODEL_SELECTION__"] = """<svg viewBox="0 0 880 270" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="270" fill="#F8FAFC" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Safe vs Unsafe Model Selection Protocols</text>

  <!-- Left: Flawed Unsafe Workflow -->
  <g transform="translate(30, 45)">
    <rect x="0" y="0" width="395" height="205" rx="8" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="1.5"/>
    <rect x="0" y="0" width="395" height="28" rx="8" fill="#FEE2E2"/>
    <text x="197" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#991B1B" text-anchor="middle">FLAWED: TUNING ON TEST SET (Direct Leakage)</text>

    <text x="15" y="52" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">1. Train on Train Split</text>
    <text x="15" y="72" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">2. Evaluate 500 candidate models directly on <tspan font-weight="700" fill="#DC2626">TEST SET</tspan></text>
    <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">3. Pick the configuration with highest test score</text>
    <text x="15" y="112" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">4. Report that test score as "expected real-world accuracy"</text>

    <rect x="15" y="125" width="365" height="70" rx="6" fill="#FEF2F2" stroke="#FECDD3" stroke-width="1"/>
    <text x="25" y="145" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#B91C1C">Fatal Consequence: Information Leakage</text>
    <text x="25" y="165" font-family="-apple-system, sans-serif" font-size="10" fill="#991B1B">The test set is no longer independent. You have overfitted the</text>
    <text x="25" y="181" font-family="-apple-system, sans-serif" font-size="10" fill="#991B1B">hyperparameter choice to the test set quirks. Real deployment fails!</text>
  </g>

  <!-- Right: Robust Safe Protocol -->
  <g transform="translate(455, 45)">
    <rect x="0" y="0" width="395" height="205" rx="8" fill="#FFFFFF" stroke="#86EFAC" stroke-width="2"/>
    <rect x="0" y="0" width="395" height="28" rx="8" fill="#DCFCE7"/>
    <text x="197" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#15803D" text-anchor="middle">ROBUST: ISOLATED CROSS-VALIDATION + HOLDOUT</text>

    <text x="15" y="52" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">1. Lock Test Set in a vault immediately (Never seen by tuner)</text>
    <text x="15" y="72" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">2. Run GridSearchCV / RandomizedSearchCV strictly on <tspan font-weight="700" fill="#16A34A">TRAIN FOLDS</tspan></text>
    <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">3. Select best_params_ by Cross-Validation Score</text>
    <text x="15" y="112" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">4. Refit winning model on full training set, test <tspan font-weight="700">ONCE</tspan> on holdout</text>

    <rect x="15" y="125" width="365" height="70" rx="6" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1"/>
    <text x="25" y="145" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#166534">Generalization Guarantee</text>
    <text x="25" y="165" font-family="-apple-system, sans-serif" font-size="10" fill="#14532D">Test set has had ZERO influence on any hyperparameter decisions.</text>
    <text x="25" y="181" font-family="-apple-system, sans-serif" font-size="10" fill="#14532D">The final holdout score is an honest, unbiased performance estimate.</text>
  </g>
</svg>"""

# 14. Data Leakage Comparison Diagram (Fig 17.1)
SVG_MAP["__SVG_DATA_LEAKAGE_COMPARISON__"] = """<svg viewBox="0 0 880 270" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="270" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Data Leakage in Preprocessing: Naive vs Pipeline</text>

  <!-- Top: Leaky Workflow -->
  <g transform="translate(40, 45)">
    <rect x="0" y="0" width="800" height="95" rx="8" fill="#FEF2F2" stroke="#FECDD3" stroke-width="1.5"/>
    <text x="20" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#991B1B">INCORRECT: Preprocessing Entire Dataset Before Cross-Validation</text>

    <!-- Flow -->
    <rect x="20" y="38" width="160" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="100" y="56" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#334155" text-anchor="middle">All 569 Samples</text>
    <text x="100" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">(Train + Test Combined)</text>

    <text x="200" y="63" font-family="-apple-system, sans-serif" font-size="16" fill="#EF4444">→</text>

    <rect x="220" y="38" width="190" height="42" rx="6" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
    <text x="315" y="56" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#991B1B" text-anchor="middle">scaler.fit_transform(X)</text>
    <text x="315" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#B91C1C" text-anchor="middle">Uses global mean and variance!</text>

    <text x="430" y="63" font-family="-apple-system, sans-serif" font-size="16" fill="#EF4444">→</text>

    <rect x="450" y="38" width="160" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="530" y="56" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#334155" text-anchor="middle">Split into Folds</text>
    <text x="530" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Validation fold already leaked</text>

    <rect x="630" y="38" width="150" height="42" rx="6" fill="#FEF2F2" stroke="#EF4444"/>
    <text x="705" y="56" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#DC2626" text-anchor="middle">LEAKAGE!</text>
    <text x="705" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#991B1B" text-anchor="middle">Optimistic CV score</text>
  </g>

  <!-- Bottom: Leakage-Safe Pipeline -->
  <g transform="translate(40, 155)">
    <rect x="0" y="0" width="800" height="95" rx="8" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="2"/>
    <text x="20" y="24" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#166534">CORRECT: Encapsulating Preprocessing Inside sklearn Pipeline</text>

    <!-- Flow -->
    <rect x="20" y="38" width="160" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="100" y="56" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#334155" text-anchor="middle">Cross-Validation Split</text>
    <text x="100" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Train Fold vs Val Fold</text>

    <text x="200" y="63" font-family="-apple-system, sans-serif" font-size="16" fill="#10B981">→</text>

    <rect x="220" y="38" width="190" height="42" rx="6" fill="#DCFCE7" stroke="#10B981" stroke-width="1.5"/>
    <text x="315" y="56" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#15803D" text-anchor="middle">scaler.fit(Train_Fold)</text>
    <text x="315" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#166534" text-anchor="middle">Mean &amp; Var computed on TRAIN ONLY</text>

    <text x="430" y="63" font-family="-apple-system, sans-serif" font-size="16" fill="#10B981">→</text>

    <rect x="450" y="38" width="160" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
    <text x="530" y="56" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#334155" text-anchor="middle">scaler.transform(Val)</text>
    <text x="530" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Zero information leaked</text>

    <rect x="630" y="38" width="150" height="42" rx="6" fill="#DCFCE7" stroke="#16A34A"/>
    <text x="705" y="56" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#15803D" text-anchor="middle">100% SAFE</text>
    <text x="705" y="72" font-family="-apple-system, sans-serif" font-size="9" fill="#14532D" text-anchor="middle">Honest evaluation</text>
  </g>
</svg>"""

# 15. Actual Learning Curve (Fig 18.1)
# Uses genuine values from executed script:
# N=36: Train 0.8611, Val 0.9253
# N=118: Train 0.9458, Val 0.9495
# N=200: Train 0.9620, Val 0.9560
# N=282: Train 0.9681, Val 0.9648
# N=364: Train 0.9742, Val 0.9714
SVG_MAP["__SVG_ACTUAL_LEARNING_CURVE__"] = """<svg viewBox="0 0 880 320" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Learning Curve: Training Set Size vs Accuracy (Tuned KNN, k=7)</text>

  <!-- Plot Area: x: 100 -> 800 (width 700), y: 50 -> 260 (height 210) -->
  <!-- Y-axis: 0.84 to 1.00 (range 0.16, 210 px -> 13.125 px per 0.01) -->
  <!-- Y mapping: y_px = 260 - (score - 0.84) / 0.16 * 210 -->
  <!-- 0.86 -> 233.75, 0.88 -> 207.5, 0.90 -> 181.25, 0.92 -> 155.0, 0.94 -> 128.75, 0.96 -> 102.5, 0.98 -> 76.25, 1.00 -> 50.0 -->

  <line x1="100" y1="234" x2="800" y2="234" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="238" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.86</text>

  <line x1="100" y1="181" x2="800" y2="181" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="185" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.90</text>

  <line x1="100" y1="129" x2="800" y2="129" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="133" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.94</text>

  <line x1="100" y1="76" x2="800" y2="76" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="80" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.98</text>

  <line x1="100" y1="260" x2="800" y2="260" stroke="#CBD5E1" stroke-width="1.5"/>
  <line x1="100" y1="50" x2="100" y2="260" stroke="#CBD5E1" stroke-width="1.5"/>

  <!-- X ticks: 36, 118, 200, 282, 364 -->
  <!-- X mapping: x = 120 + (N - 36) / (364 - 36) * 640 -->
  <!-- N=36: 120, N=118: 280, N=200: 440, N=282: 600, N=364: 760 -->

  <!-- Training Score Line: (36, 0.8611), (118, 0.9458), (200, 0.9620), (282, 0.9681), (364, 0.9742) -->
  <!-- Ys: 232.3, 121.1, 99.9, 91.9, 83.9 -->
  <polyline points="120,232 280,121 440,100 600,92 760,84" fill="none" stroke="#F43F5E" stroke-width="2.5" stroke-dasharray="4 3"/>

  <!-- Validation Score Line: (36, 0.9253), (118, 0.9495), (200, 0.9560), (282, 0.9648), (364, 0.9714) -->
  <!-- Ys: 148.0, 116.3, 107.8, 96.2, 87.5 -->
  <polyline points="120,148 280,116 440,108 600,96 760,88" fill="none" stroke="#4F46E5" stroke-width="3"/>

  <!-- Points -->
  <circle cx="120" cy="232" r="4.5" fill="#F43F5E"/>
  <circle cx="280" cy="121" r="4.5" fill="#F43F5E"/>
  <circle cx="440" cy="100" r="4.5" fill="#F43F5E"/>
  <circle cx="600" cy="92" r="4.5" fill="#F43F5E"/>
  <circle cx="760" cy="84" r="4.5" fill="#F43F5E"/>

  <circle cx="120" cy="148" r="5" fill="#4F46E5"/>
  <circle cx="280" cy="116" r="5" fill="#4F46E5"/>
  <circle cx="440" cy="108" r="5" fill="#4F46E5"/>
  <circle cx="600" cy="96" r="5" fill="#4F46E5"/>
  <circle cx="760" cy="88" r="6" fill="#10B981" stroke="#047857" stroke-width="2"/>

  <!-- Annotation at N=364 -->
  <rect x="630" y="110" width="160" height="42" rx="6" fill="#EEF2FF" stroke="#6366F1" stroke-width="1.5"/>
  <text x="710" y="126" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#3730A3" text-anchor="middle">Convergence at N=364</text>
  <text x="710" y="142" font-family="-apple-system, sans-serif" font-size="9.5" fill="#4F46E5" text-anchor="middle">Tiny Gap: 0.0027 (Low Var)</text>

  <!-- X ticks -->
  <text x="120" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">36</text>
  <text x="280" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">118</text>
  <text x="440" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">200</text>
  <text x="600" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">282</text>
  <text x="760" y="278" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#1E293B" text-anchor="middle">364</text>

  <text x="440" y="302" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E293B" text-anchor="middle">Number of Training Examples</text>

  <!-- Legend -->
  <g transform="translate(140, 50)">
    <line x1="0" y1="10" x2="25" y2="10" stroke="#F43F5E" stroke-width="2.5" stroke-dasharray="4 3"/>
    <text x="32" y="14" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Training Score</text>
    <line x1="140" y1="10" x2="165" y2="10" stroke="#4F46E5" stroke-width="3"/>
    <circle cx="152.5" cy="10" r="4" fill="#4F46E5"/>
    <text x="172" y="14" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#3730A3">Cross-Validation Score</text>
  </g>
</svg>"""

# 16. Actual Validation Curve (Fig 18.2)
# Uses genuine values from executed script:
# Depth 1: Train 0.9258, Val 0.8967
# Depth 2: Train 0.9571, Val 0.9187
# Depth 3: Train 0.9802, Val 0.9253
# Depth 4: Train 0.9912, Val 0.9385 (PEAK VAL)
# Depth 5: Train 0.9940, Val 0.9319
# Depth 6: Train 0.9967, Val 0.9187
# Depth 8-15: Train 1.0000, Val 0.9099 (Overfitting gap 0.0901)
SVG_MAP["__SVG_ACTUAL_VALIDATION_CURVE__"] = """<svg viewBox="0 0 880 320" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="320" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Validation Curve: Decision Tree max_depth vs Accuracy (Actual Data)</text>

  <!-- Plot Area: x: 100 -> 800 (width 700), y: 50 -> 260 (height 210) -->
  <!-- Y-axis: 0.88 to 1.01 (range 0.13, 210 px -> 16.15 px per 0.01) -->
  <!-- Y mapping: y_px = 260 - (score - 0.88) / 0.13 * 210 -->
  <!-- 0.90 -> 227.7, 0.92 -> 195.4, 0.94 -> 163.1, 0.96 -> 130.8, 0.98 -> 98.5, 1.00 -> 66.2 -->

  <line x1="100" y1="228" x2="800" y2="228" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="232" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.90</text>

  <line x1="100" y1="195" x2="800" y2="195" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="199" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.92</text>

  <line x1="100" y1="163" x2="800" y2="163" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="167" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.94</text>

  <line x1="100" y1="131" x2="800" y2="131" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="135" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.96</text>

  <line x1="100" y1="66" x2="800" y2="66" stroke="#F1F5F9" stroke-width="1"/>
  <text x="90" y="70" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">1.00</text>

  <line x1="100" y1="260" x2="800" y2="260" stroke="#CBD5E1" stroke-width="1.5"/>
  <line x1="100" y1="50" x2="100" y2="260" stroke="#CBD5E1" stroke-width="1.5"/>

  <!-- X ticks: Depth 1 to 15 -->
  <!-- X mapping: x = 120 + (depth - 1) / 14 * 660 -->
  <!-- d=1: 120, d=2: 167, d=3: 214, d=4: 261, d=5: 308, d=6: 356, d=7: 403, d=8: 450, d=10: 544, d=12: 638, d=15: 780 -->

  <!-- Training Score Line: (1, 0.9258), (2, 0.9571), (3, 0.9802), (4, 0.9912), (5, 0.9940), (6, 0.9967), (7, 0.9989), (8-15, 1.0000) -->
  <!-- Ys: 186.0, 135.5, 98.1, 80.4, 75.8, 71.5, 68.0, 66.2 -->
  <polyline points="120,186 167,136 214,98 261,80 308,76 356,72 403,68 450,66 544,66 638,66 780,66" fill="none" stroke="#F43F5E" stroke-width="2.5" stroke-dasharray="4 3"/>

  <!-- Validation Score Line: (1, 0.8967), (2, 0.9187), (3, 0.9253), (4, 0.9385), (5, 0.9319), (6, 0.9187), (7, 0.9209), (8-15, 0.9099) -->
  <!-- Ys: 233.0, 197.5, 186.8, 165.5, 176.2, 197.5, 193.9, 211.7 -->
  <polyline points="120,233 167,198 214,187 261,166 308,176 356,198 403,194 450,212 544,212 638,212 780,212" fill="none" stroke="#4F46E5" stroke-width="3"/>

  <!-- Peak point at depth=4 -->
  <circle cx="261" cy="166" r="8" fill="#10B981" stroke="#047857" stroke-width="2"/>
  <rect x="220" y="115" width="130" height="38" rx="6" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1.5"/>
  <text x="285" y="130" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#15803D" text-anchor="middle">PEAK: max_depth = 4</text>
  <text x="285" y="144" font-family="-apple-system, sans-serif" font-size="9.5" fill="#166534" text-anchor="middle">Val Acc = 0.9385</text>

  <!-- Overfitting bracket on the right -->
  <rect x="580" y="85" width="180" height="42" rx="6" fill="#FEE2E2" stroke="#FCA5A5" stroke-width="1"/>
  <text x="670" y="102" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">OVERFITTING ZONE</text>
  <text x="670" y="118" font-family="-apple-system, sans-serif" font-size="9" fill="#B91C1C" text-anchor="middle">Train=1.000, Val=0.910 (Gap 0.090)</text>

  <!-- X ticks -->
  <text x="120" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">1</text>
  <text x="167" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">2</text>
  <text x="214" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">3</text>
  <text x="261" y="278" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#15803D" text-anchor="middle">4*</text>
  <text x="308" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">5</text>
  <text x="356" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">6</text>
  <text x="450" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">8</text>
  <text x="544" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">10</text>
  <text x="638" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">12</text>
  <text x="780" y="278" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">15</text>

  <text x="440" y="302" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#1E293B" text-anchor="middle">Hyperparameter Value: max_depth</text>

  <!-- Legend -->
  <g transform="translate(140, 50)">
    <line x1="0" y1="10" x2="25" y2="10" stroke="#F43F5E" stroke-width="2.5" stroke-dasharray="4 3"/>
    <text x="32" y="14" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">Training Accuracy</text>
    <line x1="140" y1="10" x2="165" y2="10" stroke="#4F46E5" stroke-width="3"/>
    <circle cx="152.5" cy="10" r="4" fill="#4F46E5"/>
    <text x="172" y="14" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#3730A3">Validation Accuracy</text>
  </g>
</svg>"""

# 17. Search Computational Cost Workload (Fig 19.1)
SVG_MAP["__SVG_COMPUTATIONAL_COST_WORKLOAD__"] = """<svg viewBox="0 0 880 240" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="240" fill="#F8FAFC" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Search Workload Formula: N_fits ≈ N_configurations × K_folds</text>

  <!-- Card 1: Small Targeted Grid -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="240" height="160" rx="8" fill="#FFFFFF" stroke="#86EFAC" stroke-width="2"/>
    <rect x="0" y="0" width="240" height="28" rx="8" fill="#DCFCE7"/>
    <text x="120" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#15803D" text-anchor="middle">PLAN A: Targeted Grid (KNN)</text>
    <text x="15" y="52" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Configs: 24 configurations</text>
    <text x="15" y="72" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Cross-Validation: 5 Folds (K=5)</text>
    <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Refit Best Estimator: +1 fit</text>
    <rect x="15" y="105" width="210" height="42" rx="6" fill="#F0FDF4"/>
    <text x="120" y="122" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#166534" text-anchor="middle">Total Fits = 121</text>
    <text x="120" y="138" font-family="-apple-system, sans-serif" font-size="10" fill="#15803D" text-anchor="middle">Time: ~0.4 seconds (Fast!)</text>
  </g>

  <!-- Card 2: Randomized Budget -->
  <g transform="translate(320, 50)">
    <rect x="0" y="0" width="240" height="160" rx="8" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="1.5"/>
    <rect x="0" y="0" width="240" height="28" rx="8" fill="#EEF2FF"/>
    <text x="120" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#3730A3" text-anchor="middle">PLAN B: Budgeted Random (RF)</text>
    <text x="15" y="52" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Search Space: 675 combinations</text>
    <text x="15" y="72" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Budget (n_iter): 20 samples</text>
    <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Cross-Validation: 5 Folds</text>
    <rect x="15" y="105" width="210" height="42" rx="6" fill="#EEF2FF"/>
    <text x="120" y="122" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#3730A3" text-anchor="middle">Total Fits = 101</text>
    <text x="120" y="138" font-family="-apple-system, sans-serif" font-size="10" fill="#4F46E5" text-anchor="middle">Time: ~2.8 seconds (Controlled!)</text>
  </g>

  <!-- Card 3: Naive Combinatorial Explosion -->
  <g transform="translate(600, 50)">
    <rect x="0" y="0" width="240" height="160" rx="8" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="1.5"/>
    <rect x="0" y="0" width="240" height="28" rx="8" fill="#FEE2E2"/>
    <text x="120" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#991B1B" text-anchor="middle">PLAN C: Naive Exhaustive Grid</text>
    <text x="15" y="52" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Full RF Grid: 675 combinations</text>
    <text x="15" y="72" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• Cross-Validation: 10 Folds</text>
    <text x="15" y="92" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">• n_jobs = 1 (Sequential)</text>
    <rect x="15" y="105" width="210" height="42" rx="6" fill="#FEF2F2"/>
    <text x="120" y="122" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#B91C1C" text-anchor="middle">Total Fits = 6,750</text>
    <text x="120" y="138" font-family="-apple-system, sans-serif" font-size="10" fill="#991B1B" text-anchor="middle">Time: ~18 minutes (Wasteful!)</text>
  </g>
</svg>"""

# 18. Nested Cross-Validation (Fig 20.1)
SVG_MAP["__SVG_NESTED_CV_LOOPS__"] = """<svg viewBox="0 0 880 280" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="280" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Nested Cross-Validation: Unbiased Generalization Estimation</text>

  <!-- Outer Loop Container -->
  <g transform="translate(30, 45)">
    <rect x="0" y="0" width="820" height="215" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="820" height="28" rx="10" fill="#F1F5F9"/>
    <text x="20" y="19" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#334155">OUTER LOOP: Evaluates the Entire Model-Selection Strategy (K_outer = 5 folds)</text>

    <!-- Outer split illustration -->
    <g transform="translate(20, 38)">
      <!-- Outer Train (80%) -->
      <rect x="0" y="0" width="560" height="150" rx="8" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="1.5"/>
      <rect x="0" y="0" width="560" height="26" rx="8" fill="#EEF2FF"/>
      <text x="280" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#3730A3" text-anchor="middle">OUTER TRAINING DATA (Passed to Inner Tuning)</text>

      <!-- Inner Loop Box -->
      <g transform="translate(20, 38)">
        <rect x="0" y="0" width="520" height="98" rx="6" fill="#FDF4FF" stroke="#F5D0FE" stroke-width="1"/>
        <text x="15" y="18" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#7E22CE">INNER LOOP: Selects Hyperparameters (K_inner = 3 folds)</text>
        <text x="15" y="38" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">1. Splits Outer Train into 3 inner train/val folds</text>
        <text x="15" y="56" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">2. Evaluates all candidate configurations (GridSearchCV)</text>
        <text x="15" y="74" font-family="-apple-system, sans-serif" font-size="10" fill="#475569">3. Picks winning params and refits on all Outer Train</text>
        <text x="15" y="90" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#9333EA">Winner handed to outer test</text>
      </g>

      <!-- Outer Test (20%) -->
      <rect x="580" y="0" width="190" height="150" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="2"/>
      <text x="675" y="24" font-family="-apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#15803D" text-anchor="middle">OUTER TEST FOLD</text>
      <text x="675" y="50" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">Evaluates the inner winner</text>
      <text x="675" y="70" font-family="-apple-system, sans-serif" font-size="10" fill="#334155" text-anchor="middle">on untouched outer fold.</text>
      <rect x="595" y="90" width="160" height="44" rx="6" fill="#FFFFFF" stroke="#86EFAC"/>
      <text x="675" y="106" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">Our Experiment Result:</text>
      <text x="675" y="122" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#15803D" text-anchor="middle">0.9604 ± 0.0149</text>
    </g>
  </g>
</svg>"""

# 19. Practical Project Search Results Plot (Fig 21.1)
SVG_MAP["__SVG_PRACTICAL_SEARCH_RESULTS__"] = """<svg viewBox="0 0 880 290" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="880" height="290" fill="#FFFFFF" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="440" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">End-to-End Practical: Top Candidate Configurations vs CV Accuracy</text>

  <!-- Plot Area: x: 100 -> 780, y: 50 -> 240 -->
  <!-- Y-axis: 0.94 to 0.98 (height 190 -> 47.5 px per 0.01) -->
  <line x1="120" y1="240" x2="780" y2="240" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="120" y1="192" x2="780" y2="192" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="120" y1="145" x2="780" y2="145" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="120" y1="97" x2="780" y2="97" stroke="#F1F5F9" stroke-width="1"/>
  <line x1="120" y1="50" x2="780" y2="50" stroke="#F1F5F9" stroke-width="1"/>

  <text x="110" y="244" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.94</text>
  <text x="110" y="196" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.95</text>
  <text x="110" y="149" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.96</text>
  <text x="110" y="101" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.97</text>
  <text x="110" y="54" font-family="-apple-system, sans-serif" font-size="10" fill="#94A3B8" text-anchor="end">0.98</text>

  <!-- Bars for 5 models -->
  <!-- 1. Baseline Default KNN (k=5, unscaled data or simple): 0.925 (below, show bar at 0.94 base) -->
  <!-- 2. Manual Best KNN: 0.9714 -->
  <!-- 3. GridSearchCV Best KNN: 0.9714 -->
  <!-- 4. RandomizedSearchCV RF: 0.9582 -->
  <!-- 5. Holdout Final Test: 0.9737 -->

  <!-- Model 1: Default Baseline -->
  <g transform="translate(160, 0)">
    <rect x="-30" y="180" width="60" height="60" rx="4" fill="#E2E8F0"/>
    <text x="0" y="172" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle">0.9429</text>
    <text x="0" y="258" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Default (k=1)</text>
    <text x="0" y="272" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">Baseline</text>
  </g>

  <!-- Model 2: Manual Tuning Best -->
  <g transform="translate(290, 0)">
    <rect x="-30" y="91" width="60" height="149" rx="4" fill="#C7D2FE"/>
    <text x="0" y="83" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#3730A3" text-anchor="middle">0.9714</text>
    <text x="0" y="258" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Manual (k=7)</text>
    <text x="0" y="272" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">CV Accuracy</text>
  </g>

  <!-- Model 3: GridSearchCV Best -->
  <g transform="translate(420, 0)">
    <rect x="-30" y="91" width="60" height="149" rx="4" fill="#6366F1"/>
    <text x="0" y="83" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#3730A3" text-anchor="middle">0.9714</text>
    <text x="0" y="258" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#3730A3" text-anchor="middle">GridSearchCV</text>
    <text x="0" y="272" font-family="-apple-system, sans-serif" font-size="9" fill="#4F46E5" text-anchor="middle">Best CV (k=7, uni)</text>
  </g>

  <!-- Model 4: RandomizedSearchCV RF -->
  <g transform="translate(550, 0)">
    <rect x="-30" y="153" width="60" height="87" rx="4" fill="#FDE68A"/>
    <text x="0" y="145" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#92400E" text-anchor="middle">0.9582</text>
    <text x="0" y="258" font-family="-apple-system, sans-serif" font-size="10" fill="#475569" text-anchor="middle">RandomSearch</text>
    <text x="0" y="272" font-family="-apple-system, sans-serif" font-size="9" fill="#D97706" text-anchor="middle">Random Forest (20 iters)</text>
  </g>

  <!-- Model 5: Final Holdout Test -->
  <g transform="translate(680, 0)">
    <rect x="-30" y="80" width="60" height="160" rx="4" fill="#10B981"/>
    <text x="0" y="72" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#065F46" text-anchor="middle">0.9737</text>
    <text x="0" y="258" font-family="-apple-system, sans-serif" font-size="10" font-weight="800" fill="#047857" text-anchor="middle">Final Test Set</text>
    <text x="0" y="272" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">Untouched Holdout</text>
  </g>
</svg>"""

# 20. End-to-End Model Selection Decision Guide (Fig 23.1)
SVG_MAP["__SVG_MODEL_SELECTION_DECISION_GUIDE__"] = """<svg viewBox="0 0 900 270" width="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="270" fill="#F8FAFC" rx="12" stroke="#E2E8F0" stroke-width="1"/>
  <text x="450" y="26" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" fill="#0F172A" text-anchor="middle">Master Decision Flowchart: How to Approach Any Hyperparameter Tuning Task</text>

  <!-- Step 1 -->
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="150" height="180" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="150" height="26" rx="8" fill="#F1F5F9"/>
    <text x="75" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#1E293B" text-anchor="middle">1. DATA SPLIT</text>
    <text x="12" y="48" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Lock 20% test set away</text>
    <text x="12" y="70" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Choose CV strategy:</text>
    <text x="20" y="90" font-family="-apple-system, sans-serif" font-size="9.5" fill="#475569">- StratifiedKFold (class)</text>
    <text x="20" y="108" font-family="-apple-system, sans-serif" font-size="9.5" fill="#475569">- TimeSeriesSplit (time)</text>
    <text x="20" y="126" font-family="-apple-system, sans-serif" font-size="9.5" fill="#475569">- GroupKFold (clusters)</text>
    <rect x="10" y="145" width="130" height="24" rx="4" fill="#EEF2FF"/>
    <text x="75" y="161" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#4338CA" text-anchor="middle">Zero Test Snooping</text>
  </g>

  <!-- Arrow -->
  <text x="195" y="145" font-family="-apple-system, sans-serif" font-size="16" fill="#94A3B8">→</text>

  <!-- Step 2 -->
  <g transform="translate(210, 50)">
    <rect x="0" y="0" width="150" height="180" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="150" height="26" rx="8" fill="#F1F5F9"/>
    <text x="75" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#1E293B" text-anchor="middle">2. SAFE PIPELINE</text>
    <text x="12" y="48" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Bundle preprocessing:</text>
    <text x="20" y="70" font-family="-apple-system, sans-serif" font-size="9.5" fill="#475569">- StandardScaler</text>
    <text x="20" y="88" font-family="-apple-system, sans-serif" font-size="9.5" fill="#475569">- SimpleImputer</text>
    <text x="20" y="106" font-family="-apple-system, sans-serif" font-size="9.5" fill="#475569">- OneHotEncoder</text>
    <text x="12" y="130" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Inside sklearn Pipeline</text>
    <rect x="10" y="145" width="130" height="24" rx="4" fill="#EEF2FF"/>
    <text x="75" y="161" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#4338CA" text-anchor="middle">Prevents Leakage</text>
  </g>

  <!-- Arrow -->
  <text x="375" y="145" font-family="-apple-system, sans-serif" font-size="16" fill="#94A3B8">→</text>

  <!-- Step 3 -->
  <g transform="translate(390, 50)">
    <rect x="0" y="0" width="150" height="180" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="150" height="26" rx="8" fill="#F1F5F9"/>
    <text x="75" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#1E293B" text-anchor="middle">3. SEARCH METHOD</text>
    <text x="12" y="48" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Small grid (&lt;50 configs):</text>
    <text x="20" y="68" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#4F46E5">GridSearchCV</text>
    <text x="12" y="94" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Large / Continuous:</text>
    <text x="20" y="114" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#D97706">RandomizedSearchCV</text>
    <text x="12" y="136" font-family="-apple-system, sans-serif" font-size="9.5" fill="#475569">• Set realistic n_iter &amp; jobs</text>
    <rect x="10" y="145" width="130" height="24" rx="4" fill="#EEF2FF"/>
    <text x="75" y="161" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#4338CA" text-anchor="middle">Fit on Train Only</text>
  </g>

  <!-- Arrow -->
  <text x="555" y="145" font-family="-apple-system, sans-serif" font-size="16" fill="#94A3B8">→</text>

  <!-- Step 4 -->
  <g transform="translate(570, 50)">
    <rect x="0" y="0" width="140" height="180" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <rect x="0" y="0" width="140" height="26" rx="8" fill="#F1F5F9"/>
    <text x="70" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#1E293B" text-anchor="middle">4. DIAGNOSE</text>
    <text x="10" y="48" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Plot validation curve</text>
    <text x="10" y="70" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Plot learning curve</text>
    <text x="10" y="92" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Inspect score std:</text>
    <text x="16" y="112" font-family="-apple-system, sans-serif" font-size="9.5" fill="#475569">Is winner reliable?</text>
    <text x="10" y="134" font-family="-apple-system, sans-serif" font-size="9.5" fill="#475569">• Check overfit gap</text>
    <rect x="10" y="145" width="120" height="24" rx="4" fill="#EEF2FF"/>
    <text x="70" y="161" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#4338CA" text-anchor="middle">Verify Stability</text>
  </g>

  <!-- Arrow -->
  <text x="725" y="145" font-family="-apple-system, sans-serif" font-size="16" fill="#10B981">→</text>

  <!-- Step 5 -->
  <g transform="translate(740, 50)">
    <rect x="0" y="0" width="135" height="180" rx="8" fill="#FFFFFF" stroke="#86EFAC" stroke-width="2"/>
    <rect x="0" y="0" width="135" height="26" rx="8" fill="#DCFCE7"/>
    <text x="67" y="18" font-family="-apple-system, sans-serif" font-size="11" font-weight="800" fill="#15803D" text-anchor="middle">5. FINAL TEST</text>
    <text x="10" y="48" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Refit winner on full</text>
    <text x="10" y="66" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">  training partition</text>
    <text x="10" y="90" font-family="-apple-system, sans-serif" font-size="10" fill="#334155">• Evaluate ONCE on</text>
    <text x="10" y="108" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#15803D">  Holdout Test Set</text>
    <text x="10" y="132" font-family="-apple-system, sans-serif" font-size="9.5" fill="#475569">• Report generalization</text>
    <rect x="8" y="145" width="118" height="24" rx="4" fill="#DCFCE7"/>
    <text x="67" y="161" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#166534" text-anchor="middle">Ready for Prod</text>
  </g>
</svg>"""
