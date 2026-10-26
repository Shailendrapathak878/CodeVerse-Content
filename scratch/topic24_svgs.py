# Topic 24 SVGs
# 20 High-Quality, Accessible, Light Mode Vector SVG Diagrams
# Color Palette: Electric Blue (#2563EB), Navy (#1E40AF), Light Blue (#EFF6FF), Border (#BFDBFE), Slate (#0F172A), Emerald (#10B981), Amber (#F59E0B), Coral/Red (#EF4444)

SVG_MAP = {}

# 1. COMPLETE ML LIFECYCLE
SVG_MAP["__SVG_ML_LIFECYCLE__"] = """
<svg viewBox="0 0 860 210" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="lcShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Step 1: Problem Definition -->
  <g transform="translate(10, 30)" filter="url(#lcShadow)">
    <rect width="90" height="120" rx="8" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="2"/>
    <rect width="90" height="26" rx="8" fill="#EFF6FF"/>
    <text x="45" y="18" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">PHASE 1</text>
    <text x="45" y="52" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Problem</text>
    <text x="45" y="68" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Business Goal</text>
    <text x="45" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Target Metric</text>
    <text x="45" y="118" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🎯</text>
  </g>
  <path d="M 102 90 L 115 90" stroke="#2563EB" stroke-width="2" fill="none"/>

  <!-- Step 2: Data Collection & Preparation -->
  <g transform="translate(118, 30)" filter="url(#lcShadow)">
    <rect width="90" height="120" rx="8" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="2"/>
    <rect width="90" height="26" rx="8" fill="#EFF6FF"/>
    <text x="45" y="18" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">PHASE 2</text>
    <text x="45" y="52" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Data Prep</text>
    <text x="45" y="68" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">SQL, Clean</text>
    <text x="45" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Train/Test Split</text>
    <text x="45" y="118" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🧹</text>
  </g>
  <path d="M 210 90 L 223 90" stroke="#2563EB" stroke-width="2" fill="none"/>

  <!-- Step 3: Feature Engineering -->
  <g transform="translate(226, 30)" filter="url(#lcShadow)">
    <rect width="90" height="120" rx="8" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="2"/>
    <rect width="90" height="26" rx="8" fill="#EFF6FF"/>
    <text x="45" y="18" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">PHASE 3</text>
    <text x="45" y="52" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Feature Eng</text>
    <text x="45" y="68" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Ratios, Scale</text>
    <text x="45" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">ColumnTransf.</text>
    <text x="45" y="118" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">⚡</text>
  </g>
  <path d="M 318 90 L 331 90" stroke="#2563EB" stroke-width="2" fill="none"/>

  <!-- Step 4: Model Training & Tuning -->
  <g transform="translate(334, 30)" filter="url(#lcShadow)">
    <rect width="90" height="120" rx="8" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="2"/>
    <rect width="90" height="26" rx="8" fill="#EFF6FF"/>
    <text x="45" y="18" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">PHASE 4</text>
    <text x="45" y="52" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Train &amp; Tune</text>
    <text x="45" y="68" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">GridSearchCV</text>
    <text x="45" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Regularization</text>
    <text x="45" y="118" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">⚙️</text>
  </g>
  <path d="M 426 90 L 439 90" stroke="#2563EB" stroke-width="2" fill="none"/>

  <!-- Step 5: Model Evaluation -->
  <g transform="translate(442, 30)" filter="url(#lcShadow)">
    <rect width="90" height="120" rx="8" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="2"/>
    <rect width="90" height="26" rx="8" fill="#EFF6FF"/>
    <text x="45" y="18" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">PHASE 5</text>
    <text x="45" y="52" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Evaluation</text>
    <text x="45" y="68" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">ROC-AUC, F1</text>
    <text x="45" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Holdout Test</text>
    <text x="45" y="118" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">📊</text>
  </g>
  <path d="M 534 90 L 547 90" stroke="#2563EB" stroke-width="2" fill="none"/>

  <!-- Step 6: Artifact Serialization -->
  <g transform="translate(550, 30)" filter="url(#lcShadow)">
    <rect width="90" height="120" rx="8" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="2"/>
    <rect width="90" height="26" rx="8" fill="#EFF6FF"/>
    <text x="45" y="18" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">PHASE 6</text>
    <text x="45" y="52" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Serialize</text>
    <text x="45" y="68" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">joblib.dump()</text>
    <text x="45" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Freeze Pipeline</text>
    <text x="45" y="118" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">💾</text>
  </g>
  <path d="M 642 90 L 655 90" stroke="#2563EB" stroke-width="2" fill="none"/>

  <!-- Step 7: Deployment (API / Container) -->
  <g transform="translate(658, 30)" filter="url(#lcShadow)">
    <rect width="94" height="120" rx="8" fill="#FFFFFF" stroke="#2563EB" stroke-width="2.5"/>
    <rect width="94" height="26" rx="8" fill="#DBEAFE"/>
    <text x="47" y="18" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#1E40AF" text-anchor="middle">PHASE 7 • CORE</text>
    <text x="47" y="52" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#2563EB" text-anchor="middle">Deployment</text>
    <text x="47" y="68" font-family="system-ui, sans-serif" font-size="10" fill="#1E3A8A" text-anchor="middle">FastAPI, Docker</text>
    <text x="47" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#1E3A8A" text-anchor="middle">REST Endpoint</text>
    <text x="47" y="118" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🚀</text>
  </g>
  <path d="M 754 90 L 767 90" stroke="#2563EB" stroke-width="2" fill="none"/>

  <!-- Step 8: MLOps & Monitoring -->
  <g transform="translate(770, 30)" filter="url(#lcShadow)">
    <rect width="80" height="120" rx="8" fill="#F0FDF4" stroke="#10B981" stroke-width="2"/>
    <rect width="80" height="26" rx="8" fill="#10B981"/>
    <text x="40" y="18" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">PHASE 8</text>
    <text x="40" y="52" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#047857" text-anchor="middle">MLOps</text>
    <text x="40" y="68" font-family="system-ui, sans-serif" font-size="9.5" fill="#14532D" text-anchor="middle">Drift Detection</text>
    <text x="40" y="84" font-family="system-ui, sans-serif" font-size="9.5" fill="#14532D" text-anchor="middle">Retraining</text>
    <text x="40" y="118" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🛡️</text>
  </g>

  <!-- Subtitle Caption -->
  <text x="430" y="185" font-family="system-ui, sans-serif" font-size="12" fill="#64748B" text-anchor="middle">The Complete End-to-End Machine Learning Engineering Lifecycle: from business problem formulation to production MLOps.</text>
</svg>
"""

# 2. MODEL DEPLOYMENT ARCHITECTURE
SVG_MAP["__SVG_DEPLOYMENT_ARCH__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="daShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#daShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Production Model Serving Architecture: Turning a Python Pipeline into an Application</text>

    <!-- Client Layer -->
    <g transform="translate(30, 50)">
      <rect width="130" height="120" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="65" y="24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Client Layer</text>
      <text x="65" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#475569" text-anchor="middle">• Web Frontend</text>
      <text x="65" y="66" font-family="system-ui, sans-serif" font-size="10" fill="#475569" text-anchor="middle">• Mobile App</text>
      <text x="65" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#475569" text-anchor="middle">• Microservice</text>
      <text x="65" y="106" font-family="system-ui, sans-serif" font-size="18" text-anchor="middle">📱 💻</text>
    </g>

    <path d="M 165 110 L 215 110" stroke="#2563EB" stroke-width="2"/>
    <polygon points="215,106 223,110 215,114" fill="#2563EB"/>
    <text x="190" y="100" font-family="monospace" font-size="9" fill="#2563EB" text-anchor="middle">HTTP POST</text>

    <!-- API Gateway / FastAPI -->
    <g transform="translate(225, 50)">
      <rect width="180" height="120" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="90" y="24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#1E40AF" text-anchor="middle">FastAPI Layer</text>
      <text x="90" y="46" font-family="monospace" font-size="10" fill="#1D4ED8" text-anchor="middle">POST /predict</text>
      <rect x="15" y="58" width="150" height="24" rx="4" fill="#FFFFFF" stroke="#BFDBFE"/>
      <text x="90" y="74" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#1E40AF" text-anchor="middle">Pydantic Validation (422)</text>
      <text x="90" y="104" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Uvicorn ASGI Server</text>
    </g>

    <path d="M 410 110 L 460 110" stroke="#2563EB" stroke-width="2"/>
    <polygon points="460,106 468,110 460,114" fill="#2563EB"/>
    <text x="435" y="100" font-family="monospace" font-size="9" fill="#2563EB" text-anchor="middle">Valid DF</text>

    <!-- Frozen Pipeline Engine -->
    <g transform="translate(470, 50)">
      <rect width="280" height="120" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <text x="140" y="24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#047857" text-anchor="middle">Loaded Pipeline (In-Memory)</text>
      
      <rect x="15" y="38" width="250" height="30" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
      <text x="140" y="57" font-family="monospace" font-size="10" fill="#065F46" text-anchor="middle">ColumnTransformer.transform()</text>

      <rect x="15" y="74" width="250" height="30" rx="4" fill="#FFFFFF" stroke="#86EFAC"/>
      <text x="140" y="93" font-family="monospace" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">Estimator.predict_proba()</text>

      <text x="140" y="120" font-family="system-ui, sans-serif" font-size="9" fill="#15803D" text-anchor="middle">Zero File I/O during request; Sub-15ms Latency</text>
    </g>
  </g>
</svg>
"""

# 3. BATCH VS REAL-TIME INFERENCE
SVG_MAP["__SVG_BATCH_VS_REALTIME__"] = """
<svg viewBox="0 0 820 240" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="brShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#brShadow)">
    <rect width="780" height="210" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Inference Paradigms: Real-Time Request/Response vs. Scheduled Batch Scoring</text>

    <!-- Left: Real-Time -->
    <g transform="translate(40, 52)">
      <rect width="330" height="135" rx="8" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.5"/>
      <text x="165" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F766E" text-anchor="middle">1. Real-Time (Online API)</text>
      
      <text x="20" y="50" font-family="system-ui, sans-serif" font-size="11" fill="#134E4A"><strong>Latency Requirement:</strong> 10 ms – 100 ms</text>
      <text x="20" y="70" font-family="system-ui, sans-serif" font-size="11" fill="#134E4A"><strong>Trigger:</strong> User action (HTTP REST / gRPC)</text>
      <text x="20" y="90" font-family="system-ui, sans-serif" font-size="11" fill="#134E4A"><strong>Payload:</strong> Single row or small JSON object</text>
      <text x="20" y="110" font-family="system-ui, sans-serif" font-size="11" fill="#134E4A"><strong>Examples:</strong> Fraud detection, search autocomplete</text>

      <rect x="230" y="10" width="85" height="18" rx="4" fill="#CCFBF1"/>
      <text x="272" y="23" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#0F766E" text-anchor="middle">Interactive</text>
    </g>

    <!-- Right: Batch -->
    <g transform="translate(410, 52)">
      <rect width="330" height="135" rx="8" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
      <text x="165" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#334155" text-anchor="middle">2. Batch (Offline Job)</text>
      
      <text x="20" y="50" font-family="system-ui, sans-serif" font-size="11" fill="#475569"><strong>Latency Requirement:</strong> Hours / Overnight</text>
      <text x="20" y="70" font-family="system-ui, sans-serif" font-size="11" fill="#475569"><strong>Trigger:</strong> Scheduled Cron / Airflow DAG</text>
      <text x="20" y="90" font-family="system-ui, sans-serif" font-size="11" fill="#475569"><strong>Payload:</strong> Millions of DB rows (Parquet / SQL)</text>
      <text x="20" y="110" font-family="system-ui, sans-serif" font-size="11" fill="#475569"><strong>Examples:</strong> Weekly churn scores, marketing leads</text>

      <rect x="230" y="10" width="85" height="18" rx="4" fill="#E2E8F0"/>
      <text x="272" y="23" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">High-Throughput</text>
    </g>
  </g>
</svg>
"""

# 4. ARTIFACT WORKFLOW
SVG_MAP["__SVG_ARTIFACT_WORKFLOW__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="awShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#awShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Model Artifact Lifecycle: Serialization, Persistence, and Security</text>

    <!-- Training Environment Left -->
    <g transform="translate(30, 50)">
      <rect width="180" height="120" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="90" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Training Memory</text>
      <text x="90" y="45" font-family="monospace" font-size="10" fill="#475569" text-anchor="middle">pipeline.fit(X, y)</text>
      <text x="90" y="65" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">Fitted Trees &amp; Means</text>
      <rect x="20" y="80" width="140" height="26" rx="4" fill="#DBEAFE"/>
      <text x="90" y="97" font-family="monospace" font-size="10.5" font-weight="700" fill="#1E40AF" text-anchor="middle">joblib.dump()</text>
    </g>

    <!-- Arrow -->
    <path d="M 215 110 L 265 110" stroke="#2563EB" stroke-width="2"/>
    <polygon points="265,106 273,110 265,114" fill="#2563EB"/>

    <!-- Disk Artifact Center -->
    <g transform="translate(275, 50)">
      <rect width="210" height="120" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="105" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">Binary File on Disk</text>
      <text x="105" y="44" font-family="monospace" font-size="10.5" font-weight="700" fill="#0F172A" text-anchor="middle">pipeline.joblib</text>
      <text x="105" y="62" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Size: ~625 KB</text>

      <!-- Security Warning Box -->
      <rect x="10" y="74" width="190" height="38" rx="4" fill="#FEF2F2" stroke="#EF4444"/>
      <text x="105" y="89" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B91C1C" text-anchor="middle">⚠️ Security Warning</text>
      <text x="105" y="103" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">Never load untrusted .joblib files!</text>
    </g>

    <!-- Arrow -->
    <path d="M 490 110 L 540 110" stroke="#2563EB" stroke-width="2"/>
    <polygon points="540,106 548,110 540,114" fill="#2563EB"/>

    <!-- Serving Memory Right -->
    <g transform="translate(550, 50)">
      <rect width="190" height="120" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <text x="95" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">FastAPI Production RAM</text>
      <rect x="25" y="36" width="140" height="26" rx="4" fill="#D1FAE5"/>
      <text x="95" y="53" font-family="monospace" font-size="10.5" font-weight="700" fill="#065F46" text-anchor="middle">joblib.load()</text>
      <text x="95" y="80" font-family="system-ui, sans-serif" font-size="10" fill="#047857" text-anchor="middle">Loaded once at startup</text>
      <text x="95" y="100" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#047857" text-anchor="middle">Reusable for 100k+ calls</text>
    </g>
  </g>
</svg>
"""

# 5. API REQUEST/RESPONSE FLOW
SVG_MAP["__SVG_API_FLOW__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="afShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#afShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">HTTP Request &amp; Response Contract: JSON In &rarr; Schema Validated &rarr; Prediction Out</text>

    <!-- Request Side Left -->
    <g transform="translate(30, 50)">
      <rect width="220" height="120" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="110" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Incoming JSON Request</text>
      <rect x="15" y="30" width="190" height="80" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="25" y="48" font-family="monospace" font-size="9" fill="#1E40AF">POST /predict HTTP/1.1</text>
      <text x="25" y="64" font-family="monospace" font-size="8.5" fill="#334155">{"tenure_months": 3,</text>
      <text x="25" y="78" font-family="monospace" font-size="8.5" fill="#334155"> "monthly_charges": 95.0,</text>
      <text x="25" y="92" font-family="monospace" font-size="8.5" fill="#334155"> "contract_type": "M2M"}</text>
    </g>

    <!-- Router Center -->
    <g transform="translate(290, 50)">
      <path d="M -30 60 L 0 60" stroke="#2563EB" stroke-width="2"/>
      <rect width="180" height="120" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="90" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">API Processing</text>
      <text x="90" y="44" font-family="system-ui, sans-serif" font-size="9.5" fill="#1D4ED8" text-anchor="middle">1. Pydantic validation</text>
      <text x="90" y="64" font-family="system-ui, sans-serif" font-size="9.5" fill="#1D4ED8" text-anchor="middle">2. DataFrame packing</text>
      <text x="90" y="84" font-family="system-ui, sans-serif" font-size="9.5" fill="#1D4ED8" text-anchor="middle">3. pipeline.predict_proba()</text>
      <text x="90" y="104" font-family="system-ui, sans-serif" font-size="9.5" fill="#1D4ED8" text-anchor="middle">4. Latency timing (10.8ms)</text>
    </g>

    <!-- Response Side Right -->
    <g transform="translate(510, 50)">
      <path d="M -30 60 L 0 60" stroke="#2563EB" stroke-width="2"/>
      <rect width="240" height="120" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <text x="120" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">Outgoing JSON Response</text>
      <rect x="15" y="30" width="210" height="80" rx="4" fill="#FFFFFF" stroke="#A7F3D0"/>
      <text x="25" y="46" font-family="monospace" font-size="9" font-weight="700" fill="#047857">HTTP 200 OK</text>
      <text x="25" y="60" font-family="monospace" font-size="8.5" fill="#334155">{"prediction": 1,</text>
      <text x="25" y="74" font-family="monospace" font-size="8.5" fill="#334155"> "prediction_label": "Churn",</text>
      <text x="25" y="88" font-family="monospace" font-size="8.5" fill="#334155"> "churn_probability": 0.9996,</text>
      <text x="25" y="102" font-family="monospace" font-size="8.5" fill="#334155"> "risk_tier": "High"}</text>
    </g>
  </g>
</svg>
"""

# 6. FASTAPI PREDICTION ARCHITECTURE
SVG_MAP["__SVG_FASTAPI_ARCH__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="faShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#faShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">FastAPI Layer Components: ASGI Engine, Schema Enforcement, and Routing</text>

    <!-- Component 1: ASGI Uvicorn -->
    <g transform="translate(40, 55)">
      <rect width="210" height="120" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="105" y="24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Uvicorn ASGI Server</text>
      <text x="20" y="52" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569">• Asynchronous event loop</text>
      <text x="20" y="74" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569">• Port binding (8000)</text>
      <text x="20" y="96" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569">• Concurrency &amp; workers</text>
    </g>

    <!-- Component 2: Pydantic -->
    <g transform="translate(280, 55)">
      <rect width="220" height="120" rx="8" fill="#EFF6FF" stroke="#2563EB"/>
      <text x="110" y="24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#1E40AF" text-anchor="middle">Pydantic BaseModel</text>
      <text x="20" y="52" font-family="system-ui, sans-serif" font-size="10.5" fill="#1D4ED8">• Automatic type casting</text>
      <text x="20" y="74" font-family="system-ui, sans-serif" font-size="10.5" fill="#1D4ED8">• Field bounds: ge=0, le=120</text>
      <text x="20" y="96" font-family="system-ui, sans-serif" font-size="10.5" fill="#1D4ED8">• 422 error on invalid inputs</text>
    </g>

    <!-- Component 3: Scikit-learn Pipeline -->
    <g transform="translate(530, 55)">
      <rect width="210" height="120" rx="8" fill="#ECFDF5" stroke="#10B981"/>
      <text x="105" y="24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#047857" text-anchor="middle">Scikit-Learn Pipeline</text>
      <text x="20" y="52" font-family="system-ui, sans-serif" font-size="10.5" fill="#065F46">• Preprocessing enclosed</text>
      <text x="20" y="74" font-family="system-ui, sans-serif" font-size="10.5" fill="#065F46">• StandardScaler &amp; OHE</text>
      <text x="20" y="96" font-family="system-ui, sans-serif" font-size="10.5" fill="#065F46">• Probabilities via Forest</text>
    </g>
  </g>
</svg>
"""

# 7. LOCAL VS CLOUD DEPLOYMENT
SVG_MAP["__SVG_LOCAL_VS_CLOUD__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="lcCompareShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#lcCompareShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Deployment Environments: Localhost Prototype vs. Production Cloud Infrastructure</text>

    <!-- Localhost Left -->
    <g transform="translate(40, 50)">
      <rect width="330" height="125" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="165" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">Localhost (Dev Machine)</text>
      <text x="20" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#475569"><strong>URL:</strong> http://127.0.0.1:8000</text>
      <text x="20" y="68" font-family="system-ui, sans-serif" font-size="11" fill="#475569"><strong>Accessibility:</strong> Only your computer</text>
      <text x="20" y="88" font-family="system-ui, sans-serif" font-size="11" fill="#475569"><strong>Cost:</strong> $0.00 (Zero hosting bill)</text>
      <text x="20" y="108" font-family="system-ui, sans-serif" font-size="11" fill="#475569"><strong>Best for:</strong> Building, debugging, rapid tests</text>
    </g>

    <!-- Cloud Production Right -->
    <g transform="translate(410, 50)">
      <rect width="330" height="125" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="165" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#1E40AF" text-anchor="middle">Cloud Production (AWS / GCP / VPS)</text>
      <text x="20" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#1D4ED8"><strong>URL:</strong> https://api.yourcompany.com</text>
      <text x="20" y="68" font-family="system-ui, sans-serif" font-size="11" fill="#1D4ED8"><strong>Accessibility:</strong> Global internet with SSL</text>
      <text x="20" y="88" font-family="system-ui, sans-serif" font-size="11" fill="#1D4ED8"><strong>Features:</strong> Load balancers, horizontal auto-scaling</text>
      <text x="20" y="108" font-family="system-ui, sans-serif" font-size="11" fill="#1D4ED8"><strong>Best for:</strong> Real user traffic, SLAs, high availability</text>
    </g>
  </g>
</svg>
"""

# 8. DOCKER IMAGE & CONTAINER
SVG_MAP["__SVG_DOCKER_CONTAINER__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="dkShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#dkShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Containerization: Packaging Code, Dependencies, and Artifacts with Docker</text>

    <!-- Dockerfile Left -->
    <g transform="translate(30, 50)">
      <rect width="210" height="120" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="105" y="20" font-family="monospace" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Dockerfile (Blueprint)</text>
      <text x="15" y="42" font-family="monospace" font-size="9" fill="#1E40AF">FROM python:3.10-slim</text>
      <text x="15" y="58" font-family="monospace" font-size="9" fill="#475569">COPY requirements.txt .</text>
      <text x="15" y="74" font-family="monospace" font-size="9" fill="#475569">RUN pip install -r reqs.txt</text>
      <text x="15" y="90" font-family="monospace" font-size="9" fill="#475569">COPY app.py pipeline.joblib .</text>
      <text x="15" y="106" font-family="monospace" font-size="9" fill="#1E40AF">CMD ["uvicorn", "app:app"]</text>
    </g>

    <!-- Arrow Build -->
    <path d="M 250 110 L 295 110" stroke="#2563EB" stroke-width="2"/>
    <polygon points="295,106 303,110 295,114" fill="#2563EB"/>
    <text x="275" y="100" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#2563EB" text-anchor="middle">build</text>

    <!-- Container Image Center -->
    <g transform="translate(310, 50)">
      <rect width="200" height="120" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="100" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">Container Image</text>
      <text x="100" y="44" font-family="monospace" font-size="10" fill="#0F172A" text-anchor="middle">churn-api:v1.0.0</text>
      <text x="100" y="66" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">• Immutable binary snapshot</text>
      <text x="100" y="84" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">• Python + exact library versions</text>
      <text x="100" y="104" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">📦</text>
    </g>

    <!-- Arrow Run -->
    <path d="M 520 110 L 565 110" stroke="#2563EB" stroke-width="2"/>
    <polygon points="565,106 573,110 565,114" fill="#2563EB"/>
    <text x="545" y="100" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#2563EB" text-anchor="middle">run</text>

    <!-- Running Container Right -->
    <g transform="translate(575, 50)">
      <rect width="175" height="120" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
      <text x="87" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">Running Container</text>
      <text x="87" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#065F46" text-anchor="middle">Isolated Linux OS</text>
      <text x="87" y="68" font-family="system-ui, sans-serif" font-size="10" fill="#065F46" text-anchor="middle">Port 8000 exposed</text>
      <text x="87" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Zero "works on my machine" bugs!</text>
    </g>
  </g>
</svg>
"""

# 9. MLOPS LIFECYCLE
SVG_MAP["__SVG_MLOPS_LIFECYCLE__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="mlopsShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#mlopsShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">The Continuous MLOps Flywheel: DevOps Principles Applied to Machine Learning</text>

    <!-- Circular / Sequential Nodes -->
    <g transform="translate(30, 60)">
      <!-- 1. Data -->
      <circle cx="45" cy="45" r="35" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="45" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">1. Data</text>
      <text x="45" y="55" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">Versioned</text>

      <path d="M 85 45 L 115 45" stroke="#2563EB" stroke-width="2"/>

      <!-- 2. Train -->
      <circle cx="150" cy="45" r="35" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="150" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">2. Train</text>
      <text x="150" y="55" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">Pipelines</text>

      <path d="M 190 45 L 220 45" stroke="#2563EB" stroke-width="2"/>

      <!-- 3. Validate -->
      <circle cx="255" cy="45" r="35" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="255" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">3. Validate</text>
      <text x="255" y="55" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">Gates &amp; Tests</text>

      <path d="M 295 45 L 325 45" stroke="#2563EB" stroke-width="2"/>

      <!-- 4. Package -->
      <circle cx="360" cy="45" r="35" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="360" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">4. Package</text>
      <text x="360" y="55" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">Docker Image</text>

      <path d="M 400 45 L 430 45" stroke="#2563EB" stroke-width="2"/>

      <!-- 5. Deploy -->
      <circle cx="465" cy="45" r="35" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="465" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">5. Deploy</text>
      <text x="465" y="55" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">CI/CD Release</text>

      <path d="M 505 45 L 535 45" stroke="#2563EB" stroke-width="2"/>

      <!-- 6. Monitor -->
      <circle cx="570" cy="45" r="35" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="570" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E40AF" text-anchor="middle">6. Monitor</text>
      <text x="570" y="55" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">Drift &amp; Errors</text>

      <path d="M 610 45 L 640 45" stroke="#10B981" stroke-width="2"/>

      <!-- 7. Improve / Retrain -->
      <circle cx="675" cy="45" r="35" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
      <text x="675" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#047857" text-anchor="middle">7. Retrain</text>
      <text x="675" y="55" font-family="system-ui, sans-serif" font-size="8.5" fill="#065F46" text-anchor="middle">Continuous</text>
    </g>

    <!-- Feedback Loop Path Back -->
    <path d="M 705 130 C 500 170, 200 170, 65 130" stroke="#10B981" stroke-width="2" stroke-dasharray="4,4" fill="none"/>
    <text x="390" y="165" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" fill="#047857" text-anchor="middle">&larr; Feedback Loop: Production Insights Trigger Data Collection &amp; Automated Retraining &larr;</text>
  </g>
</svg>
"""

# 10. EXPERIMENT TRACKING
SVG_MAP["__SVG_EXPERIMENT_TRACKING__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="etShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#etShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Model &amp; Experiment Tracking: Reproducibility Beyond Filenames</text>

    <!-- Table of tracked experiments -->
    <g transform="translate(30, 48)">
      <rect width="720" height="26" fill="#F1F5F9" stroke="#E2E8F0"/>
      <text x="50" y="17" font-family="monospace" font-size="10" font-weight="700" fill="#0F172A">Exp ID</text>
      <text x="140" y="17" font-family="monospace" font-size="10" font-weight="700" fill="#0F172A">Git Commit</text>
      <text x="240" y="17" font-family="monospace" font-size="10" font-weight="700" fill="#0F172A">Data Hash</text>
      <text x="360" y="17" font-family="monospace" font-size="10" font-weight="700" fill="#0F172A">Key Params</text>
      <text x="520" y="17" font-family="monospace" font-size="10" font-weight="700" fill="#0F172A">Holdout ROC-AUC</text>
      <text x="650" y="17" font-family="monospace" font-size="10" font-weight="700" fill="#0F172A">Status</text>

      <!-- Row 1 -->
      <rect y="26" width="720" height="24" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="50" y="42" font-family="monospace" font-size="10" fill="#475569">exp-001</text>
      <text x="140" y="42" font-family="monospace" font-size="10" fill="#475569">a18f92c</text>
      <text x="240" y="42" font-family="monospace" font-size="10" fill="#475569">v1_raw.csv</text>
      <text x="360" y="42" font-family="monospace" font-size="9.5" fill="#475569">max_depth=3, n_est=50</text>
      <text x="520" y="42" font-family="monospace" font-size="10" fill="#475569">0.9340</text>
      <text x="650" y="42" font-family="system-ui, sans-serif" font-size="10" fill="#64748B">Archived</text>

      <!-- Row 2 -->
      <rect y="50" width="720" height="24" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="50" y="66" font-family="monospace" font-size="10" fill="#475569">exp-002</text>
      <text x="140" y="66" font-family="monospace" font-size="10" fill="#475569">f49b10a</text>
      <text x="240" y="66" font-family="monospace" font-size="10" fill="#475569">v2_fe.csv</text>
      <text x="360" y="66" font-family="monospace" font-size="9.5" fill="#475569">max_depth=6, n_est=50</text>
      <text x="520" y="66" font-family="monospace" font-size="10" fill="#475569">0.9680</text>
      <text x="650" y="66" font-family="system-ui, sans-serif" font-size="10" fill="#64748B">Staged</text>

      <!-- Row 3: Active Champion -->
      <rect y="74" width="720" height="24" fill="#ECFDF5" stroke="#86EFAC"/>
      <text x="50" y="90" font-family="monospace" font-size="10" font-weight="700" fill="#047857">exp-003</text>
      <text x="140" y="90" font-family="monospace" font-size="10" font-weight="700" fill="#047857">8c2e41d</text>
      <text x="240" y="90" font-family="monospace" font-size="10" font-weight="700" fill="#047857">v3_clean.csv</text>
      <text x="360" y="90" font-family="monospace" font-size="9.5" font-weight="700" fill="#047857">max_depth=6, n_est=100</text>
      <text x="520" y="90" font-family="monospace" font-size="10.5" font-weight="800" fill="#047857">0.9924 ✔</text>
      <text x="650" y="90" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857">Production</text>
    </g>

    <text x="390" y="172" font-family="system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">
      Experiment logs couple code commits with exact dataset snapshots and evaluation metrics, guaranteeing auditability.
    </text>
  </g>
</svg>
"""

# 11. DATA DRIFT (DISTRIBUTION SHIFT)
SVG_MAP["__SVG_DATA_DRIFT__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="ddShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#ddShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Data Drift: Input Feature Distribution P(X) Shifts Over Time</text>

    <!-- Axes -->
    <g transform="translate(60, 50)">
      <line x1="30" y1="105" x2="680" y2="105" stroke="#CBD5E1" stroke-width="2"/>
      <line x1="30" y1="105" x2="30" y2="15" stroke="#CBD5E1" stroke-width="2"/>
      <text x="680" y="122" font-family="system-ui, sans-serif" font-size="11" fill="#475569" text-anchor="end">Customer Monthly Spend ($)</text>
      <text x="20" y="25" font-family="system-ui, sans-serif" font-size="10" fill="#475569" text-anchor="end">Density</text>

      <!-- Curve 1: Training Distribution P(X) in Blue -->
      <path d="M 60 105 Q 180 15, 280 105" fill="#EFF6FF" fill-opacity="0.6" stroke="#2563EB" stroke-width="2.5"/>
      <text x="180" y="45" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1D4ED8" text-anchor="middle">Training Baseline P(X)</text>
      <text x="180" y="60" font-family="monospace" font-size="9.5" fill="#1E40AF" text-anchor="middle">Mean: $50.00</text>

      <!-- Shift Arrow -->
      <path d="M 230 70 L 330 70" stroke="#EF4444" stroke-width="2.5" stroke-dasharray="3,3"/>
      <polygon points="330,66 338,70 330,74" fill="#EF4444"/>
      <text x="280" y="62" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#B91C1C" text-anchor="middle">Data Drift</text>

      <!-- Curve 2: Production Shifted Distribution P'(X) in Red/Orange -->
      <path d="M 260 105 Q 380 20, 500 105" fill="#FEF2F2" fill-opacity="0.6" stroke="#EF4444" stroke-width="2.5"/>
      <text x="380" y="45" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#B91C1C" text-anchor="middle">Production Actual P'(X)</text>
      <text x="380" y="60" font-family="monospace" font-size="9.5" fill="#991B1B" text-anchor="middle">Mean: $85.00 (Inflation)</text>
    </g>

    <text x="390" y="180" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">
      Features drift when real-world economics, demographics, or user behavior change, causing the model to operate out of bounds.
    </text>
  </g>
</svg>
"""

# 12. CONCEPT DRIFT (RELATIONSHIP SHIFT)
SVG_MAP["__SVG_CONCEPT_DRIFT__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="cdShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#cdShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Concept Drift: Relationship P(Y|X) Changes Even if Input Features Look Familiar</text>

    <!-- Left Box: Historical Relationship -->
    <g transform="translate(50, 50)">
      <rect width="320" height="120" rx="8" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="160" y="22" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Historical Rule: 2021 Data</text>
      
      <circle cx="90" cy="65" r="14" fill="#DBEAFE" stroke="#2563EB"/>
      <text x="90" y="69" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">X</text>
      <text x="90" y="95" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">High Online Spend</text>

      <path d="M 120 65 L 180 65" stroke="#2563EB" stroke-width="2"/>
      <polygon points="180,61 188,65 180,69" fill="#2563EB"/>

      <circle cx="220" cy="65" r="14" fill="#FEE2E2" stroke="#EF4444"/>
      <text x="220" y="69" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">Y</text>
      <text x="220" y="95" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#B91C1C" text-anchor="middle">Likely Fraud (90%)</text>
    </g>

    <!-- Right Box: Post-Pandemic Shift -->
    <g transform="translate(410, 50)">
      <rect width="320" height="120" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
      <text x="160" y="22" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#B91C1C" text-anchor="middle">Post-Pandemic Shift: 2024 Data</text>
      
      <circle cx="90" cy="65" r="14" fill="#DBEAFE" stroke="#2563EB"/>
      <text x="90" y="69" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1E40AF" text-anchor="middle">X</text>
      <text x="90" y="95" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">High Online Spend</text>

      <path d="M 120 65 L 180 65" stroke="#EF4444" stroke-width="2"/>
      <polygon points="180,61 188,65 180,69" fill="#EF4444"/>

      <circle cx="220" cy="65" r="14" fill="#ECFDF5" stroke="#10B981"/>
      <text x="220" y="69" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">Y</text>
      <text x="220" y="95" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#047857" text-anchor="middle">Legitimate Shopper (95%)</text>
    </g>

    <text x="390" y="185" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">
      In concept drift, the input values look normal, but their meaning has inverted, requiring fresh training labels.
    </text>
  </g>
</svg>
"""

# 13. MONITORING DASHBOARD MOCKUP
SVG_MAP["__SVG_MONITORING_DASH__"] = """
<svg viewBox="0 0 820 240" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="mdShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#mdShadow)">
    <rect width="780" height="210" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Production Model Observability Dashboard: Live Telemetry &amp; Health Metrics</text>

    <!-- Card 1: Request Rate -->
    <g transform="translate(40, 52)">
      <rect width="160" height="95" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#64748B">REQUEST THROUGHPUT</text>
      <text x="15" y="55" font-family="monospace" font-size="20" font-weight="800" fill="#0F172A">1,450 /m</text>
      <rect x="15" y="68" width="60" height="15" rx="3" fill="#D1FAE5"/>
      <text x="45" y="79" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#065F46" text-anchor="middle">+4.2% vs avg</text>
    </g>

    <!-- Card 2: P95 Latency -->
    <g transform="translate(220, 52)">
      <rect width="160" height="95" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#64748B">P95 INFERENCE LATENCY</text>
      <text x="15" y="55" font-family="monospace" font-size="20" font-weight="800" fill="#2563EB">15.05 ms</text>
      <rect x="15" y="68" width="70" height="15" rx="3" fill="#DBEAFE"/>
      <text x="50" y="79" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#1E40AF" text-anchor="middle">SLA: &lt; 50 ms</text>
    </g>

    <!-- Card 3: Error Rate -->
    <g transform="translate(400, 52)">
      <rect width="160" height="95" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#64748B">HTTP 5XX ERRORS</text>
      <text x="15" y="55" font-family="monospace" font-size="20" font-weight="800" fill="#10B981">0.00 %</text>
      <rect x="15" y="68" width="60" height="15" rx="3" fill="#D1FAE5"/>
      <text x="45" y="79" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#065F46" text-anchor="middle">Zero Faults</text>
    </g>

    <!-- Card 4: Drift Status -->
    <g transform="translate(580, 52)">
      <rect width="160" height="95" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="15" y="24" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#64748B">DRIFT DRIFT STATUS</text>
      <text x="15" y="55" font-family="monospace" font-size="20" font-weight="800" fill="#10B981">STABLE</text>
      <rect x="15" y="68" width="70" height="15" rx="3" fill="#D1FAE5"/>
      <text x="50" y="79" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#065F46" text-anchor="middle">KS-test p &gt; .05</text>
    </g>

    <!-- Mini Telemetry Sparkline Footer -->
    <rect x="40" y="160" width="700" height="30" rx="4" fill="#F8FAFC" stroke="#E2E8F0"/>
    <text x="55" y="179" font-family="monospace" font-size="10" fill="#2563EB">Live Stream: /predict [200 OK] 10.8ms | /predict [200 OK] 12.1ms | /health [200 OK] 1.2ms | /predict [422 REJECT] 2.1ms</text>
  </g>
</svg>
"""

# 14. RETRAINING LOOP
SVG_MAP["__SVG_RETRAINING_LOOP__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="rlShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#rlShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Continuous Retraining Workflow: Champion vs. Challenger Promotion</text>

    <!-- Step 1: Detect -->
    <g transform="translate(30, 55)">
      <rect width="125" height="115" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="62" y="20" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0F172A" text-anchor="middle">1. Trigger</text>
      <text x="62" y="44" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Drift Alarm OR</text>
      <text x="62" y="60" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Scheduled Date</text>
      <text x="62" y="85" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">⏰ 🚨</text>
    </g>

    <path d="M 160 110 L 185 110" stroke="#2563EB" stroke-width="2"/>

    <!-- Step 2: Retrain -->
    <g transform="translate(190, 55)">
      <rect width="135" height="115" rx="6" fill="#EFF6FF" stroke="#2563EB"/>
      <text x="67" y="20" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1E40AF" text-anchor="middle">2. Retrain</text>
      <text x="67" y="44" font-family="system-ui, sans-serif" font-size="9.5" fill="#1D4ED8" text-anchor="middle">Fit on recent 90d</text>
      <text x="67" y="60" font-family="system-ui, sans-serif" font-size="9.5" fill="#1D4ED8" text-anchor="middle">Challenger Model</text>
      <text x="67" y="85" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">⚙️</text>
    </g>

    <path d="M 330 110 L 355 110" stroke="#2563EB" stroke-width="2"/>

    <!-- Step 3: Evaluate -->
    <g transform="translate(360, 55)">
      <rect width="135" height="115" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="67" y="20" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0F172A" text-anchor="middle">3. Evaluate</text>
      <text x="67" y="44" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Challenger vs</text>
      <text x="67" y="60" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Active Champion</text>
      <text x="67" y="85" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">⚖️</text>
    </g>

    <path d="M 500 110 L 525 110" stroke="#2563EB" stroke-width="2"/>

    <!-- Step 4: Governance Gate -->
    <g transform="translate(530, 55)">
      <rect width="105" height="115" rx="6" fill="#FFFBEB" stroke="#F59E0B"/>
      <text x="52" y="20" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#B45309" text-anchor="middle">4. Gate</text>
      <text x="52" y="44" font-family="system-ui, sans-serif" font-size="9.5" fill="#78350F" text-anchor="middle">Automated OR</text>
      <text x="52" y="60" font-family="system-ui, sans-serif" font-size="9.5" fill="#78350F" text-anchor="middle">Human Review</text>
      <text x="52" y="85" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🔒</text>
    </g>

    <path d="M 640 110 L 665 110" stroke="#10B981" stroke-width="2"/>

    <!-- Step 5: Canary Deploy -->
    <g transform="translate(670, 55)">
      <rect width="80" height="115" rx="6" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
      <text x="40" y="20" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#047857" text-anchor="middle">5. Deploy</text>
      <text x="40" y="44" font-family="system-ui, sans-serif" font-size="9" fill="#065F46" text-anchor="middle">10% Canary</text>
      <text x="40" y="60" font-family="system-ui, sans-serif" font-size="9" fill="#065F46" text-anchor="middle">100% Release</text>
      <text x="40" y="85" font-family="system-ui, sans-serif" font-size="16" text-anchor="middle">🚀</text>
    </g>
  </g>
</svg>
"""

# 15. CI/CD WORKFLOW
SVG_MAP["__SVG_CICD_WORKFLOW__"] = """
<svg viewBox="0 0 820 200" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="cicdShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#cicdShadow)">
    <rect width="780" height="170" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="30" rx="10" fill="#EFF6FF"/>
    <text x="25" y="20" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">CI/CD Pipeline: Automated Quality Gates from Git Commit to Deployment</text>

    <!-- Stage 1 -->
    <g transform="translate(30, 48)">
      <rect width="130" height="75" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
      <text x="65" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#0F172A" text-anchor="middle">1. Git Push</text>
      <text x="65" y="44" font-family="monospace" font-size="9.5" fill="#475569" text-anchor="middle">git commit</text>
      <text x="65" y="60" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Trigger GitHub Action</text>
    </g>

    <path d="M 165 85 L 185 85" stroke="#2563EB" stroke-width="2"/>

    <!-- Stage 2 -->
    <g transform="translate(190, 48)">
      <rect width="130" height="75" rx="6" fill="#EFF6FF" stroke="#2563EB"/>
      <text x="65" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1E40AF" text-anchor="middle">2. Unit Tests</text>
      <text x="65" y="44" font-family="monospace" font-size="9.5" fill="#1D4ED8" text-anchor="middle">pytest tests/</text>
      <text x="65" y="60" font-family="system-ui, sans-serif" font-size="9" fill="#1D4ED8" text-anchor="middle">FastAPI endpoint tests</text>
    </g>

    <path d="M 325 85 L 345 85" stroke="#2563EB" stroke-width="2"/>

    <!-- Stage 3 -->
    <g transform="translate(350, 48)">
      <rect width="130" height="75" rx="6" fill="#EFF6FF" stroke="#2563EB"/>
      <text x="65" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1E40AF" text-anchor="middle">3. Model Gate</text>
      <text x="65" y="44" font-family="monospace" font-size="9.5" fill="#1D4ED8" text-anchor="middle">AUC &gt;= 0.95</text>
      <text x="65" y="60" font-family="system-ui, sans-serif" font-size="9" fill="#1D4ED8" text-anchor="middle">Latency &lt; 50ms check</text>
    </g>

    <path d="M 485 85 L 505 85" stroke="#2563EB" stroke-width="2"/>

    <!-- Stage 4 -->
    <g transform="translate(510, 48)">
      <rect width="115" height="75" rx="6" fill="#EFF6FF" stroke="#2563EB"/>
      <text x="57" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1E40AF" text-anchor="middle">4. Docker</text>
      <text x="57" y="44" font-family="monospace" font-size="9.5" fill="#1D4ED8" text-anchor="middle">docker build</text>
      <text x="57" y="60" font-family="system-ui, sans-serif" font-size="9" fill="#1D4ED8" text-anchor="middle">Push to Registry</text>
    </g>

    <path d="M 630 85 L 650 85" stroke="#10B981" stroke-width="2"/>

    <!-- Stage 5 -->
    <g transform="translate(655, 48)">
      <rect width="95" height="75" rx="6" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
      <text x="47" y="22" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" fill="#047857" text-anchor="middle">5. Deploy</text>
      <text x="47" y="44" font-family="system-ui, sans-serif" font-size="9.5" fill="#065F46" text-anchor="middle">Rolling Update</text>
      <text x="47" y="60" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">Live on Cloud</text>
    </g>

    <text x="390" y="146" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">
      Automated testing prevents faulty code or degraded models from ever reaching production users.
    </text>
  </g>
</svg>
"""

# 16. SECURITY CHECKLIST
SVG_MAP["__SVG_SECURITY_CHECKLIST__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="scShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#scShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">The 6 Pillars of Production Model Security &amp; Robustness</text>

    <!-- Grid of 6 Pillars -->
    <g transform="translate(30, 48)">
      <!-- Pillar 1 -->
      <rect x="0" y="0" width="225" height="48" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="15" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">1. Schema Validation</text>
      <text x="15" y="36" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B">Enforce strict Pydantic bounds</text>

      <!-- Pillar 2 -->
      <rect x="245" y="0" width="225" height="48" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="15" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" transform="translate(245, 0)">2. Trusted Artifacts Only</text>
      <text x="15" y="36" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" transform="translate(245, 0)">Verify SHA256 checksums</text>

      <!-- Pillar 3 -->
      <rect x="490" y="0" width="230" height="48" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="15" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" transform="translate(490, 0)">3. Zero Hardcoded Secrets</text>
      <text x="15" y="36" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" transform="translate(490, 0)">Use .env and Secret Managers</text>

      <!-- Pillar 4 -->
      <rect x="0" y="60" width="225" height="48" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="15" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" transform="translate(0, 60)">4. API Rate Limiting</text>
      <text x="15" y="36" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" transform="translate(0, 60)">Protect against DoS attacks</text>

      <!-- Pillar 5 -->
      <rect x="245" y="60" width="225" height="48" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="15" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" transform="translate(245, 60)">5. Privacy Redaction</text>
      <text x="15" y="36" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" transform="translate(245, 60)">Never log raw PII or credit cards</text>

      <!-- Pillar 6 -->
      <rect x="490" y="60" width="230" height="48" rx="6" fill="#ECFDF5" stroke="#10B981"/>
      <text x="15" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#047857" transform="translate(490, 60)">6. Pin Exact Dependencies</text>
      <text x="15" y="36" font-family="system-ui, sans-serif" font-size="9.5" fill="#065F46" transform="translate(490, 60)">requirements.txt with exact hashes</text>
    </g>

    <text x="390" y="176" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">
      A model service is only as reliable as the security boundary enclosing its prediction endpoints.
    </text>
  </g>
</svg>
"""

# 17. ACTUAL MODEL EVALUATION ROC PLOT
SVG_MAP["__SVG_MODEL_EVAL_PLOT__"] = """
<svg viewBox="0 0 820 250" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="meShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#meShadow)">
    <rect width="780" height="220" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Empirical Evaluation: ROC Curve and Holdout Performance (N=200 Test)</text>

    <!-- ROC Plot Left -->
    <g transform="translate(40, 50)">
      <rect width="320" height="145" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <!-- Grid Lines -->
      <line x1="50" y1="115" x2="290" y2="115" stroke="#CBD5E1" stroke-width="1.5"/>
      <line x1="50" y1="115" x2="50" y2="25" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="290" y="132" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" text-anchor="end">False Positive Rate (FPR)</text>
      <text x="45" y="20" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B" text-anchor="end">TPR</text>

      <!-- Diagonal Random line -->
      <line x1="50" y1="115" x2="290" y2="25" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>

      <!-- Empirical ROC Curve -->
      <path d="M 50 115 L 54 32 L 68 28 L 120 26 L 290 25" fill="#EFF6FF" fill-opacity="0.5" stroke="#2563EB" stroke-width="2.5"/>
      <text x="170" y="70" font-family="monospace" font-size="12" font-weight="800" fill="#1E40AF" text-anchor="middle">ROC-AUC = 0.9924</text>
    </g>

    <!-- Metrics Breakdown Right -->
    <g transform="translate(400, 50)">
      <rect width="340" height="145" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="170" y="24" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#0F172A" text-anchor="middle">Holdout Test Set Performance</text>

      <g transform="translate(20, 42)">
        <text x="0" y="14" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569">Accuracy:</text>
        <text x="140" y="14" font-family="monospace" font-size="11.5" font-weight="700" fill="#0F172A">95.50% (191 / 200)</text>

        <text x="0" y="36" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569">Precision:</text>
        <text x="140" y="36" font-family="monospace" font-size="11.5" font-weight="700" fill="#0F172A">94.95%</text>

        <text x="0" y="58" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569">Recall:</text>
        <text x="140" y="58" font-family="monospace" font-size="11.5" font-weight="700" fill="#0F172A">95.92%</text>

        <text x="0" y="80" font-family="system-ui, sans-serif" font-size="10.5" fill="#475569">F1-Score:</text>
        <text x="140" y="80" font-family="monospace" font-size="11.5" font-weight="700" fill="#0F172A">0.9543</text>
      </g>
    </g>
  </g>
</svg>
"""

# 18. ACTUAL INFERENCE LATENCY MONITORING PLOT
SVG_MAP["__SVG_MONITORING_PLOT__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="mpShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#mpShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Empirical Inference Latency Quantiles (100 Successive Requests via TestClient)</text>

    <!-- Horizontal Quantile Bar Plot -->
    <g transform="translate(40, 55)">
      <!-- P50 -->
      <text x="80" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">P50 (Median):</text>
      <rect x="90" y="8" width="380" height="20" rx="4" fill="#2563EB"/>
      <text x="480" y="23" font-family="monospace" font-size="11" font-weight="700" fill="#1D4ED8">12.69 ms</text>

      <!-- Mean -->
      <text x="80" y="52" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">Mean Latency:</text>
      <rect x="90" y="38" width="390" height="20" rx="4" fill="#3B82F6"/>
      <text x="490" y="53" font-family="monospace" font-size="11" font-weight="700" fill="#1D4ED8">12.95 ms</text>

      <!-- P95 -->
      <text x="80" y="82" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">P95 Quantile:</text>
      <rect x="90" y="68" width="450" height="20" rx="4" fill="#60A5FA"/>
      <text x="550" y="83" font-family="monospace" font-size="11" font-weight="700" fill="#1D4ED8">15.05 ms</text>

      <!-- P99 -->
      <text x="80" y="112" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="end">P99 Quantile:</text>
      <rect x="90" y="98" width="485" height="20" rx="4" fill="#93C5FD"/>
      <text x="585" y="113" font-family="monospace" font-size="11" font-weight="700" fill="#1D4ED8">16.16 ms</text>
    </g>

    <text x="390" y="180" font-family="system-ui, sans-serif" font-size="10.5" fill="#64748B" text-anchor="middle">
      Measured locally with complete ColumnTransformer + 100-tree RandomForestClassifier inference pipeline.
    </text>
  </g>
</svg>
"""

# 19. PROJECT ARCHITECTURE
SVG_MAP["__SVG_PROJECT_ARCH__"] = """
<svg viewBox="0 0 820 220" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="paShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>
  </defs>

  <g transform="translate(20, 15)" filter="url(#paShadow)">
    <rect width="780" height="190" rx="10" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="1.5"/>
    <rect width="780" height="32" rx="10" fill="#EFF6FF"/>
    <text x="25" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#1E40AF">Production Project Structure: Standardized Layout for Deployable ML Services</text>

    <!-- File Tree Left -->
    <g transform="translate(40, 50)">
      <rect width="270" height="125" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="20" y="24" font-family="monospace" font-size="10.5" font-weight="700" fill="#1E40AF">churn-prediction-api/</text>
      <text x="35" y="44" font-family="monospace" font-size="10" fill="#334155">├── train_model.py</text>
      <text x="35" y="60" font-family="monospace" font-size="10" fill="#334155">├── app.py</text>
      <text x="35" y="76" font-family="monospace" font-size="10" fill="#334155">├── schemas.py</text>
      <text x="35" y="92" font-family="monospace" font-size="10" fill="#334155">├── customer_pipeline.joblib</text>
      <text x="35" y="108" font-family="monospace" font-size="10" fill="#334155">├── Dockerfile &amp; requirements.txt</text>
    </g>

    <!-- Component Explanations Right -->
    <g transform="translate(340, 50)">
      <rect width="400" height="125" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="20" y="25" font-family="system-ui, sans-serif" font-size="10.5" fill="#0F172A"><strong>train_model.py:</strong> Ingests raw data, builds pipeline, exports joblib.</text>
      <text x="20" y="48" font-family="system-ui, sans-serif" font-size="10.5" fill="#0F172A"><strong>app.py:</strong> FastAPI router handling /health and /predict endpoints.</text>
      <text x="20" y="71" font-family="system-ui, sans-serif" font-size="10.5" fill="#0F172A"><strong>schemas.py:</strong> Pydantic models with range checks and JSON examples.</text>
      <text x="20" y="94" font-family="system-ui, sans-serif" font-size="10.5" fill="#0F172A"><strong>Dockerfile:</strong> Multi-stage build packaging dependencies into image.</text>
      <text x="20" y="114" font-family="system-ui, sans-serif" font-size="10.5" fill="#0F172A"><strong>tests/:</strong> Automated Pytest client scripts validating status codes.</text>
    </g>
  </g>
</svg>
"""

# 20. MANDATORY COMPLETION & PROJECT ROADMAP BANNER
SVG_MAP["__SVG_COMPLETION_BANNER__"] = """
<svg viewBox="0 0 820 230" width="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="compGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF" />
      <stop offset="50%" stop-color="#DBEAFE" />
      <stop offset="100%" stop-color="#BFDBFE" />
    </linearGradient>
    <filter id="cbShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#2563EB" flood-opacity="0.12"/>
    </filter>
  </defs>

  <g transform="translate(15, 10)" filter="url(#cbShadow)">
    <rect width="790" height="210" rx="14" fill="url(#compGrad)" stroke="#3B82F6" stroke-width="2"/>

    <!-- Trophy / Graduation Icon Left -->
    <g transform="translate(35, 30)">
      <circle cx="50" cy="50" r="42" fill="#FFFFFF" stroke="#3B82F6" stroke-width="2"/>
      <text x="50" y="58" font-family="system-ui, sans-serif" font-size="42" text-anchor="middle">🎓</text>
    </g>

    <!-- Center Text Content -->
    <g transform="translate(150, 26)">
      <rect width="195" height="24" rx="12" fill="#FEF3C7" stroke="#FCD34D"/>
      <text x="97" y="16" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" fill="#92400E" text-anchor="middle">CURRICULUM COMPLETE</text>

      <text x="0" y="52" font-family="system-ui, sans-serif" font-size="20" font-weight="900" fill="#0F172A">Congratulations! You've Completed ML Fundamentals</text>
      <text x="0" y="74" font-family="system-ui, sans-serif" font-size="12" fill="#334155">
        From exploratory analysis and loss optimization to hyperparameter tuning and production MLOps:
      </text>
      <text x="0" y="90" font-family="system-ui, sans-serif" font-size="12" fill="#334155">
        you have mastered the comprehensive foundations of the modern Machine Learning Engineer.
      </text>

      <!-- 7-Stage Roadmap Steps -->
      <g transform="translate(0, 106)">
        <rect x="0" y="0" width="70" height="24" rx="4" fill="#FFFFFF" stroke="#93C5FD"/>
        <text x="35" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E3A8A" text-anchor="middle">1. Build</text>

        <text x="77" y="17" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#60A5FA">&rarr;</text>

        <rect x="90" y="0" width="75" height="24" rx="4" fill="#FFFFFF" stroke="#93C5FD"/>
        <text x="127" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E3A8A" text-anchor="middle">2. Evaluate</text>

        <text x="172" y="17" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#60A5FA">&rarr;</text>

        <rect x="185" y="0" width="75" height="24" rx="4" fill="#FFFFFF" stroke="#93C5FD"/>
        <text x="222" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E3A8A" text-anchor="middle">3. Package</text>

        <text x="267" y="17" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#60A5FA">&rarr;</text>

        <rect x="280" y="0" width="70" height="24" rx="4" fill="#FFFFFF" stroke="#93C5FD"/>
        <text x="315" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E3A8A" text-anchor="middle">4. Deploy</text>

        <text x="357" y="17" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#60A5FA">&rarr;</text>

        <rect x="370" y="0" width="65" height="24" rx="4" fill="#FFFFFF" stroke="#93C5FD"/>
        <text x="402" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E3A8A" text-anchor="middle">5. Test</text>

        <text x="442" y="17" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#60A5FA">&rarr;</text>

        <rect x="455" y="0" width="80" height="24" rx="4" fill="#FFFFFF" stroke="#93C5FD"/>
        <text x="495" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1E3A8A" text-anchor="middle">6. Document</text>

        <text x="542" y="17" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#60A5FA">&rarr;</text>

        <rect x="555" y="0" width="75" height="24" rx="4" fill="#10B981"/>
        <text x="592" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#FFFFFF" text-anchor="middle">Showcase ★</text>
      </g>

      <text x="0" y="152" font-family="system-ui, sans-serif" font-size="11.5" font-weight="700" fill="#1E40AF">
        Your Final Challenge: Build, test, containerize, and showcase an end-to-end ML application!
      </text>
    </g>
  </g>
</svg>
"""
