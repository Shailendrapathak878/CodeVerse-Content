"""
Topic 15: Ensemble Learning - CSS Stylesheet
Strict Light Mode Only
Color Palette: Deep Ocean Cyan / Persian Teal (#0891B2)
"""

TOPIC_15_CSS = """
    :root {
      /* Base Surfaces - Strict Light Mode Only */
      --bg-page: #F8FAFC;
      --card-bg: #FFFFFF;
      --card-border: #E2E8F0;
      --card-soft-bg: #F1F5F9;
      --card-shadow: 0 4px 14px 0 rgba(15, 23, 42, 0.05), 0 1px 3px rgba(15, 23, 42, 0.03);
      
      /* Typography */
      --text-primary: #0F172A;
      --text-secondary: #334155;
      --text-muted: #64748B;
      --heading-color: #0F172A;
      
      /* Topic 15 Theme: Deep Ocean Cyan / Persian Teal & Navy */
      --primary-accent: #0891B2;
      --primary-accent-hover: #0E7490;
      --primary-accent-light: #ECFEFF;
      --primary-badge-bg: #ECFEFF;
      --primary-badge-text: #0E7490;
      --toc-bg: #F8FAFC;
      --toc-border: #A5F3FC;
      --toc-text: #0E7490;

      /* Definition Card (Soft Sky / Cyan) */
      --def-card-bg: #F0F9FF;
      --def-card-border: #BAE6FD;
      --def-card-title: #0284C7;
      --def-card-text: #0C4A6E;

      /* Analogy Card (Soft Amber / Warm Honey) */
      --analogy-card-bg: #FFFBEB;
      --analogy-card-border: #FDE68A;
      --analogy-card-title: #D97706;
      --analogy-card-text: #78350F;

      /* Success / Highlight Card (Emerald / Mint) */
      --success-card-bg: #ECFDF5;
      --success-card-border: #A7F3D0;
      --success-card-title: #059669;
      --success-card-text: #065F46;

      /* Warning / Pitfall Card (Soft Rose / Coral) */
      --warn-card-bg: #FEF2F2;
      --warn-card-border: #FECACA;
      --warn-card-title: #DC2626;
      --warn-card-text: #7F1D1D;

      /* Tables */
      --table-header-bg: #F8FAFC;
      --table-row-alt: #F8FAFC;
      --table-border: #E2E8F0;
    }

    /* Reset & Base Setup */
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-primary);
      line-height: 1.65;
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      max-width: 100vw;
      width: 100%;
    }

    .container {
      max-width: 1040px;
      margin: 0 auto;
      padding: 40px 24px 80px;
      overflow-x: hidden;
      width: 100%;
    }

    /* Hero Header */
    .hero-header {
      background: linear-gradient(135deg, #FFFFFF 0%, #F0FDFA 50%, #ECFEFF 100%);
      border: 1px solid #CFFAFE;
      border-radius: 16px;
      padding: 40px 36px;
      margin-bottom: 36px;
      box-shadow: var(--card-shadow);
      position: relative;
      overflow: hidden;
      width: 100%;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--primary-badge-bg);
      color: var(--primary-badge-text);
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 6px 14px;
      border-radius: 20px;
      margin-bottom: 16px;
      border: 1px solid #A5F3FC;
    }

    .hero-title {
      font-size: 2.35rem;
      font-weight: 800;
      color: var(--heading-color);
      line-height: 1.25;
      margin-bottom: 14px;
      letter-spacing: -0.02em;
      overflow-wrap: break-word;
    }

    .hero-desc {
      font-size: 1.15rem;
      color: var(--text-secondary);
      max-width: 860px;
      margin-bottom: 24px;
      line-height: 1.6;
      overflow-wrap: break-word;
    }

    .hero-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      padding-top: 20px;
      border-top: 1px solid #E0F2FE;
    }

    .hero-meta-item {
      display: flex;
      flex-direction: column;
    }

    .hero-meta-label {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      font-weight: 600;
    }

    .hero-meta-value {
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-primary);
    }

    /* Table of Contents */
    .toc-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 28px 32px;
      margin-bottom: 40px;
      box-shadow: var(--card-shadow);
      overflow: hidden;
      width: 100%;
    }

    .toc-title {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--heading-color);
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .toc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 10px 16px;
      list-style: none;
    }

    .toc-link {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.92rem;
      color: var(--text-secondary);
      text-decoration: none;
      padding: 6px 10px;
      border-radius: 6px;
      transition: all 0.15s ease;
      overflow-wrap: break-word;
    }

    .toc-link:hover {
      background: var(--primary-accent-light);
      color: var(--primary-accent);
      transform: translateX(3px);
    }

    .toc-number {
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--primary-accent);
      background: #E0F2FE;
      padding: 2px 7px;
      border-radius: 4px;
      min-width: 28px;
      text-align: center;
      flex-shrink: 0;
    }

    /* Content Sections */
    .content-section {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 36px 36px 40px;
      margin-bottom: 36px;
      box-shadow: var(--card-shadow);
      overflow-x: hidden;
      width: 100%;
    }

    .section-header {
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 2px solid #F1F5F9;
    }

    .section-badge {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--primary-accent);
      background: var(--primary-accent-light);
      padding: 3px 10px;
      border-radius: 12px;
      margin-bottom: 8px;
    }

    .section-title {
      font-size: 1.7rem;
      font-weight: 800;
      color: var(--heading-color);
      letter-spacing: -0.015em;
      line-height: 1.3;
      overflow-wrap: break-word;
    }

    .section-subtitle {
      font-size: 1.02rem;
      color: var(--text-muted);
      margin-top: 6px;
      overflow-wrap: break-word;
    }

    h3 {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--heading-color);
      margin: 28px 0 14px;
      line-height: 1.35;
      overflow-wrap: break-word;
    }

    h4 {
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--text-secondary);
      margin: 20px 0 10px;
      overflow-wrap: break-word;
    }

    p {
      color: var(--text-secondary);
      margin-bottom: 16px;
      line-height: 1.68;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    p:last-child {
      margin-bottom: 0;
    }

    ul, ol {
      margin: 0 0 18px 24px;
      color: var(--text-secondary);
    }

    li {
      margin-bottom: 8px;
      line-height: 1.6;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    code {
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 0.88em;
      background: #F1F5F9;
      color: #0E7490;
      padding: 2px 6px;
      border-radius: 4px;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    /* Callout & Specialized Cards */
    .callout-card {
      border-radius: 10px;
      padding: 20px 22px;
      margin: 20px 0;
      border-left: 4px solid;
      overflow: hidden;
      width: 100%;
    }

    .def-card {
      background: var(--def-card-bg);
      border: 1px solid var(--def-card-border);
      border-left: 4px solid var(--def-card-title);
    }

    .def-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--def-card-title);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .def-card p {
      color: var(--def-card-text);
      font-size: 0.95rem;
    }

    .analogy-card {
      background: var(--analogy-card-bg);
      border: 1px solid var(--analogy-card-border);
      border-left: 4px solid var(--analogy-card-title);
    }

    .analogy-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--analogy-card-title);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .analogy-card p {
      color: var(--analogy-card-text);
      font-size: 0.95rem;
    }

    .success-card {
      background: var(--success-card-bg);
      border: 1px solid var(--success-card-border);
      border-left: 4px solid var(--success-card-title);
    }

    .success-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--success-card-title);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .success-card p {
      color: var(--success-card-text);
      font-size: 0.95rem;
    }

    .warn-card {
      background: var(--warn-card-bg);
      border: 1px solid var(--warn-card-border);
      border-left: 4px solid var(--warn-card-title);
    }

    .warn-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--warn-card-title);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .warn-card p {
      color: var(--warn-card-text);
      font-size: 0.95rem;
    }

    /* Formulas & Math Blocks */
    .formula-block {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 18px 22px;
      margin: 20px 0;
      text-align: center;
      overflow-x: auto;
      width: 100%;
    }

    .formula-title {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
    }

    .formula-math {
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
      font-size: 1.15rem;
      color: #0F172A;
      font-weight: 600;
      margin: 8px 0;
      letter-spacing: 0.02em;
    }

    .formula-explanation {
      font-size: 0.88rem;
      color: var(--text-secondary);
      margin-top: 8px;
      text-align: left;
    }

    /* Step-by-Step Calculation Box */
    .calc-box {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 22px;
      margin: 22px 0;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
      overflow-x: hidden;
      width: 100%;
    }

    .calc-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-accent);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .calc-step {
      display: flex;
      gap: 14px;
      margin-bottom: 14px;
      padding-bottom: 14px;
      border-bottom: 1px dashed #E2E8F0;
    }

    .calc-step:last-child {
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }

    .calc-step-num {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #ECFEFF;
      color: #0891B2;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.82rem;
      font-weight: 700;
      flex-shrink: 0;
      margin-top: 2px;
      border: 1px solid #A5F3FC;
    }

    .calc-step-content {
      flex: 1;
      font-size: 0.95rem;
      color: var(--text-secondary);
      overflow-wrap: break-word;
      word-break: break-word;
    }

    .calc-step-content strong {
      color: var(--text-primary);
    }

    /* Code Container */
    .code-container {
      background: #0F172A;
      border-radius: 10px;
      margin: 22px 0;
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.12);
      width: 100%;
    }

    .code-header {
      background: #1E293B;
      padding: 8px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
    }

    .code-lang-badge {
      font-size: 0.75rem;
      font-weight: 700;
      color: #38BDF8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .code-body {
      padding: 18px 20px;
      color: #E2E8F0;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 0.88rem;
      line-height: 1.55;
      overflow-x: auto;
      white-space: pre;
    }

    .code-output {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      padding: 14px 18px;
      margin: 12px 0 22px;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 0.85rem;
      color: #1E293B;
      line-height: 1.5;
      overflow-x: auto;
      white-space: pre;
      width: 100%;
    }

    .code-output-title {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-muted);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Visual & SVG Container */
    .visual-container {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 24px;
      margin: 26px 0;
      box-shadow: var(--card-shadow);
      text-align: center;
      overflow: hidden;
      width: 100%;
    }

    .svg-wrapper {
      width: 100%;
      overflow-x: auto;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 10px 0;
    }

    .svg-wrapper svg {
      max-width: 100%;
      height: auto;
      display: block;
    }

    .visual-caption {
      margin-top: 14px;
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.5;
      text-align: left;
      padding: 10px 14px;
      background: #F8FAFC;
      border-radius: 6px;
      border-left: 3px solid var(--primary-accent);
      overflow-wrap: break-word;
    }

    .visual-caption strong {
      color: var(--text-primary);
    }

    /* Tables */
    .table-wrapper {
      width: 100%;
      overflow-x: auto;
      margin: 22px 0;
      border-radius: 10px;
      border: 1px solid var(--table-border);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.92rem;
    }

    th {
      background-color: var(--table-header-bg);
      color: var(--heading-color);
      font-weight: 700;
      padding: 12px 16px;
      border-bottom: 2px solid var(--table-border);
      white-space: nowrap;
    }

    td {
      padding: 12px 16px;
      border-bottom: 1px solid var(--table-border);
      color: var(--text-secondary);
      vertical-align: top;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:nth-child(even) td {
      background-color: var(--table-row-alt);
    }

    /* Mistake & Fix Cards */
    .mistake-card {
      background: #FFFFFF;
      border: 1px solid #FECACA;
      border-radius: 10px;
      margin-bottom: 18px;
      overflow: hidden;
      box-shadow: 0 1px 3px rgba(220, 38, 38, 0.05);
      width: 100%;
    }

    .mistake-header {
      background: #FEF2F2;
      padding: 12px 18px;
      font-weight: 700;
      color: #B91C1C;
      font-size: 0.95rem;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid #FEE2E2;
    }

    .mistake-body {
      padding: 16px 18px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }

    .mistake-error {
      background: #FFF1F2;
      border: 1px solid #FFE4E6;
      border-radius: 6px;
      padding: 12px 14px;
      font-size: 0.88rem;
      color: #9F1239;
      overflow-wrap: break-word;
    }

    .mistake-fix {
      background: #F0FDF4;
      border: 1px solid #DCFCE7;
      border-radius: 6px;
      padding: 12px 14px;
      font-size: 0.88rem;
      color: #166534;
      overflow-wrap: break-word;
    }

    /* Interactive Accordion / FAQ */
    .accordion-item {
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      margin-bottom: 12px;
      background: #FFFFFF;
      overflow: hidden;
      transition: all 0.2s ease;
      width: 100%;
    }

    .accordion-item[open] {
      border-color: #A5F3FC;
      box-shadow: 0 2px 8px rgba(8, 145, 178, 0.08);
    }

    .accordion-summary {
      padding: 16px 20px;
      font-weight: 700;
      color: var(--heading-color);
      font-size: 0.98rem;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #FFFFFF;
      user-select: none;
      overflow-wrap: break-word;
    }

    .accordion-summary:hover {
      background: #F8FAFC;
      color: var(--primary-accent);
    }

    .accordion-content {
      padding: 16px 20px 20px;
      color: var(--text-secondary);
      font-size: 0.92rem;
      line-height: 1.65;
      border-top: 1px solid #F1F5F9;
      background: #FAFAFA;
      overflow-wrap: break-word;
    }

    /* Footer */
    .notes-footer {
      text-align: center;
      padding: 40px 20px;
      margin-top: 40px;
      border-top: 1px solid #E2E8F0;
      color: var(--text-muted);
      font-size: 0.88rem;
      overflow-wrap: break-word;
      width: 100%;
    }

    /* Mobile Responsive Queries */
    @media (max-width: 768px) {
      .container {
        padding: 16px 12px 40px;
      }

      .hero-header {
        padding: 24px 18px;
        margin-bottom: 24px;
      }

      .hero-title {
        font-size: 1.65rem;
      }

      .hero-desc {
        font-size: 0.98rem;
      }

      .content-section {
        padding: 22px 14px;
        margin-bottom: 24px;
      }

      .section-title {
        font-size: 1.35rem;
      }

      .toc-card {
        padding: 20px 14px;
      }

      .toc-grid {
        grid-template-columns: 1fr;
      }

      .mistake-body {
        grid-template-columns: 1fr;
        gap: 10px;
      }

      .code-body {
        font-size: 0.78rem;
        padding: 14px 12px;
      }

      .table-wrapper {
        margin: 16px 0;
      }

      th, td {
        padding: 10px 12px;
        font-size: 0.84rem;
      }
    }
"""
