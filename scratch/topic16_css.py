"""Topic 16 CSS: Strict Light Mode, Electric Indigo Theme, Zero Horizontal Overflow.
"""

TOPIC16_CSS = """
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
      
      /* Topic 16 Theme: Electric Indigo & Royal Violet */
      --primary-accent: #4F46E5;
      --primary-accent-hover: #4338CA;
      --primary-accent-light: #EEF2FF;
      --primary-badge-bg: #EEF2FF;
      --primary-badge-text: #4338CA;
      --toc-bg: #F8FAFC;
      --toc-border: #C7D2FE;
      --toc-text: #4338CA;

      /* Definition Card (Soft Sky / Indigo) */
      --def-card-bg: #EEF2FF;
      --def-card-border: #C7D2FE;
      --def-card-title: #4338CA;
      --def-card-text: #1E1B4B;

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

      /* Purple Card (Algorithm highlight) */
      --purple-card-bg: #FAF5FF;
      --purple-card-border: #E9D5FF;
      --purple-card-title: #7E22CE;
      --purple-card-text: #581C87;

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
      background: linear-gradient(135deg, #FFFFFF 0%, #EEF2FF 50%, #F5F3FF 100%);
      border: 1px solid #E0E7FF;
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
      border: 1px solid #C7D2FE;
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

    .hero-subtitle {
      font-size: 1.15rem;
      color: var(--text-secondary);
      line-height: 1.6;
      max-width: 860px;
      margin-bottom: 24px;
      overflow-wrap: break-word;
    }

    .hero-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-top: 24px;
      padding-top: 20px;
      border-top: 1px solid #E0E7FF;
      width: 100%;
    }

    .meta-item {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .meta-label {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      font-weight: 600;
    }

    .meta-value {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-primary);
    }

    /* Table of Contents */
    .toc-card {
      background: var(--card-bg);
      border: 1px solid var(--toc-border);
      border-radius: 14px;
      padding: 28px 32px;
      margin-bottom: 44px;
      box-shadow: var(--card-shadow);
      width: 100%;
    }

    .toc-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 2px solid var(--primary-accent-light);
    }

    .toc-title {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--toc-text);
    }

    .toc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px 24px;
      width: 100%;
    }

    .toc-link {
      color: var(--text-secondary);
      text-decoration: none;
      font-size: 0.93rem;
      line-height: 1.5;
      padding: 4px 8px;
      border-radius: 6px;
      transition: all 0.15s ease;
      display: flex;
      align-items: flex-start;
      gap: 8px;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    .toc-link:hover {
      background: var(--primary-accent-light);
      color: var(--primary-accent);
      transform: translateX(3px);
    }

    .toc-num {
      font-weight: 700;
      color: var(--primary-accent);
      font-size: 0.85rem;
      flex-shrink: 0;
      min-width: 22px;
    }

    /* Section Cards */
    .content-section {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 36px 34px;
      margin-bottom: 40px;
      box-shadow: var(--card-shadow);
      overflow-x: hidden;
      width: 100%;
    }

    .section-badge {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--primary-accent);
      background: var(--primary-accent-light);
      padding: 4px 10px;
      border-radius: 6px;
      margin-bottom: 12px;
      border: 1px solid #C7D2FE;
    }

    .section-title {
      font-size: 1.8rem;
      font-weight: 800;
      color: var(--heading-color);
      line-height: 1.3;
      margin-bottom: 20px;
      letter-spacing: -0.01em;
      overflow-wrap: break-word;
    }

    .subsection-title {
      font-size: 1.28rem;
      font-weight: 700;
      color: var(--heading-color);
      margin: 28px 0 14px;
      overflow-wrap: break-word;
    }

    p {
      color: var(--text-secondary);
      margin-bottom: 16px;
      font-size: 1.02rem;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    strong {
      color: var(--text-primary);
      font-weight: 700;
    }

    ul, ol {
      margin: 0 0 20px 22px;
      color: var(--text-secondary);
    }

    li {
      margin-bottom: 8px;
      line-height: 1.6;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    /* Visual Diagram Container */
    .visual-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 24px;
      margin: 28px 0;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
      width: 100%;
      overflow: hidden;
    }

    .visual-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 10px;
      border-bottom: 1px solid #F1F5F9;
      flex-wrap: wrap;
      gap: 8px;
    }

    .visual-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--heading-color);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .visual-badge {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      background: #F1F5F9;
      color: #475569;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid #CBD5E1;
    }

    .visual-badge.verified {
      background: #ECFDF5;
      color: #065F46;
      border-color: #A7F3D0;
    }

    .svg-wrapper {
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 10px 0;
      overflow-x: auto;
    }

    .svg-wrapper svg {
      max-width: 100%;
      height: auto;
      display: block;
    }

    .visual-caption {
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-top: 14px;
      padding-top: 10px;
      border-top: 1px dashed #E2E8F0;
      font-style: italic;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    /* Concept & Analogy Cards */
    .callout-card {
      border-radius: 10px;
      padding: 20px 22px;
      margin: 22px 0;
      border-left: 4px solid;
      width: 100%;
    }

    .callout-def {
      background: var(--def-card-bg);
      border-color: var(--def-card-title);
      border: 1px solid var(--def-card-border);
      border-left: 5px solid var(--def-card-title);
    }
    .callout-def .callout-title { color: var(--def-card-title); }
    .callout-def p, .callout-def li { color: var(--def-card-text); }

    .callout-analogy {
      background: var(--analogy-card-bg);
      border-color: var(--analogy-card-title);
      border: 1px solid var(--analogy-card-border);
      border-left: 5px solid var(--analogy-card-title);
    }
    .callout-analogy .callout-title { color: var(--analogy-card-title); }
    .callout-analogy p, .callout-analogy li { color: var(--analogy-card-text); }

    .callout-success {
      background: var(--success-card-bg);
      border-color: var(--success-card-title);
      border: 1px solid var(--success-card-border);
      border-left: 5px solid var(--success-card-title);
    }
    .callout-success .callout-title { color: var(--success-card-title); }
    .callout-success p, .callout-success li { color: var(--success-card-text); }

    .callout-warn {
      background: var(--warn-card-bg);
      border-color: var(--warn-card-title);
      border: 1px solid var(--warn-card-border);
      border-left: 5px solid var(--warn-card-title);
    }
    .callout-warn .callout-title { color: var(--warn-card-title); }
    .callout-warn p, .callout-warn li { color: var(--warn-card-text); }

    .callout-purple {
      background: var(--purple-card-bg);
      border-color: var(--purple-card-title);
      border: 1px solid var(--purple-card-border);
      border-left: 5px solid var(--purple-card-title);
    }
    .callout-purple .callout-title { color: var(--purple-card-title); }
    .callout-purple p, .callout-purple li { color: var(--purple-card-text); }

    .callout-title {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Math Formula Block */
    .formula-block {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 18px 22px;
      margin: 22px 0;
      text-align: center;
      font-family: "Georgia", "Cambria", serif;
      font-size: 1.18rem;
      color: #0F172A;
      box-shadow: inset 0 1px 3px rgba(15, 23, 42, 0.03);
      overflow-x: auto;
      width: 100%;
    }

    .formula-breakdown {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 12px;
      margin-top: 14px;
      padding-top: 14px;
      border-top: 1px solid #E2E8F0;
      text-align: left;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 0.88rem;
      color: var(--text-secondary);
    }

    .breakdown-item strong {
      color: var(--primary-accent);
      font-family: "Georgia", serif;
    }

    /* Comparison & Data Tables */
    .table-wrapper {
      width: 100%;
      overflow-x: auto;
      margin: 24px 0;
      border-radius: 10px;
      border: 1px solid var(--table-border);
      box-shadow: 0 1px 4px rgba(15, 23, 42, 0.03);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.94rem;
      text-align: left;
    }

    thead th {
      background: var(--table-header-bg);
      color: var(--heading-color);
      font-weight: 700;
      padding: 14px 18px;
      border-bottom: 2px solid var(--table-border);
      white-space: nowrap;
    }

    tbody td {
      padding: 13px 18px;
      border-bottom: 1px solid var(--table-border);
      color: var(--text-secondary);
      vertical-align: top;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    tbody tr:nth-child(even) {
      background: var(--table-row-alt);
    }

    tbody tr:hover {
      background: #F1F5F9;
    }

    /* Code Blocks */
    .code-card {
      background: #0F172A;
      border-radius: 12px;
      margin: 24px 0;
      box-shadow: 0 6px 18px rgba(15, 23, 42, 0.12);
      border: 1px solid #1E293B;
      overflow: hidden;
      width: 100%;
    }

    .code-header {
      background: #1E293B;
      padding: 10px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
    }

    .code-title {
      font-size: 0.82rem;
      font-weight: 600;
      color: #94A3B8;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .code-tag {
      font-size: 0.72rem;
      font-weight: 700;
      background: #334155;
      color: #F8FAFC;
      padding: 2px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .code-tag.verified {
      background: #065F46;
      color: #A7F3D0;
    }

    .code-body {
      padding: 18px 20px;
      overflow-x: auto;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
      font-size: 0.88rem;
      line-height: 1.6;
      color: #E2E8F0;
      tab-size: 4;
    }

    .code-body pre {
      margin: 0;
      font-family: inherit;
    }

    /* Syntax Highlighting */
    .c-kw { color: #F43F5E; font-weight: 600; }
    .c-fn { color: #38BDF8; }
    .c-st { color: #34D399; }
    .c-cm { color: #64748B; font-style: italic; }
    .c-nb { color: #F59E0B; }
    .c-op { color: #E2E8F0; }

    /* Inline Code */
    code {
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
      font-size: 0.88em;
      background: #EEF2FF;
      color: #4338CA;
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid #C7D2FE;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    /* Output Console */
    .console-output {
      background: #1E293B;
      border-top: 1px dashed #334155;
      padding: 14px 18px;
      font-family: "SFMono-Regular", Consolas, monospace;
      font-size: 0.82rem;
      color: #38BDF8;
      line-height: 1.5;
      overflow-x: auto;
    }

    .console-label {
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #64748B;
      margin-bottom: 6px;
      font-weight: 700;
    }

    /* Mistake Card */
    .mistake-card {
      background: #FFFFFF;
      border: 1px solid #FECACA;
      border-radius: 10px;
      padding: 20px;
      margin: 16px 0;
      box-shadow: 0 2px 6px rgba(239, 68, 68, 0.05);
      width: 100%;
    }

    .mistake-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid #FEE2E2;
    }

    .mistake-icon {
      font-size: 1.2rem;
    }

    .mistake-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: #DC2626;
      overflow-wrap: break-word;
    }

    .mistake-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-top: 10px;
      width: 100%;
    }

    .mistake-bad {
      background: #FEF2F2;
      border: 1px solid #FECACA;
      border-radius: 6px;
      padding: 12px;
      font-size: 0.88rem;
      color: #7F1D1D;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    .mistake-good {
      background: #ECFDF5;
      border: 1px solid #A7F3D0;
      border-radius: 6px;
      padding: 12px;
      font-size: 0.88rem;
      color: #065F46;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    .mistake-tag {
      font-weight: 700;
      text-transform: uppercase;
      font-size: 0.72rem;
      letter-spacing: 0.05em;
      margin-bottom: 4px;
      display: block;
    }

    /* Accordion FAQ */
    details {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      margin: 12px 0;
      padding: 16px 20px;
      transition: all 0.2s ease;
      width: 100%;
    }

    details[open] {
      border-color: #C7D2FE;
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.06);
    }

    summary {
      font-weight: 700;
      color: var(--heading-color);
      cursor: pointer;
      font-size: 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      list-style: none;
      user-select: none;
      overflow-wrap: break-word;
    }

    summary::-webkit-details-marker {
      display: none;
    }

    summary::after {
      content: "+";
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--primary-accent);
      transition: transform 0.2s ease;
      flex-shrink: 0;
      margin-left: 10px;
    }

    details[open] summary::after {
      content: "−";
      transform: rotate(180deg);
    }

    .details-content {
      margin-top: 14px;
      padding-top: 14px;
      border-top: 1px solid #EEF2FF;
      color: var(--text-secondary);
      font-size: 0.95rem;
      line-height: 1.6;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    /* Step Process Flow */
    .step-flow {
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin: 22px 0;
      width: 100%;
    }

    .step-item {
      display: flex;
      gap: 16px;
      align-items: flex-start;
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 18px 20px;
      width: 100%;
    }

    .step-number {
      background: var(--primary-accent);
      color: #FFFFFF;
      font-weight: 800;
      font-size: 0.9rem;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 2px 6px rgba(79, 70, 229, 0.3);
    }

    .step-content {
      flex: 1;
      min-width: 0;
    }

    .step-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--heading-color);
      margin-bottom: 6px;
      overflow-wrap: break-word;
    }

    .step-desc {
      font-size: 0.94rem;
      color: var(--text-secondary);
      line-height: 1.55;
      margin: 0;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    /* Real-World Application Cards */
    .app-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 24px;
      margin: 20px 0;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
      width: 100%;
    }

    .app-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid #F1F5F9;
    }

    .app-icon {
      font-size: 1.6rem;
    }

    .app-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--heading-color);
    }

    .app-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
      margin-top: 12px;
      width: 100%;
    }

    .app-item {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      padding: 12px 14px;
      font-size: 0.88rem;
      overflow-wrap: break-word;
      word-break: break-word;
    }

    .app-item-label {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--primary-accent);
      margin-bottom: 4px;
      display: block;
    }

    /* Footer */
    .notes-footer {
      text-align: center;
      padding: 40px 20px 20px;
      border-top: 1px solid #E2E8F0;
      margin-top: 60px;
      color: var(--text-muted);
      font-size: 0.88rem;
    }

    .notes-footer strong {
      color: var(--text-primary);
    }

    /* Mobile Responsiveness */
    @media (max-width: 768px) {
      .container {
        padding: 20px 14px 60px;
      }

      .hero-header {
        padding: 28px 20px;
      }

      .hero-title {
        font-size: 1.75rem;
      }

      .hero-subtitle {
        font-size: 1rem;
      }

      .content-section {
        padding: 24px 18px;
        margin-bottom: 28px;
      }

      .section-title {
        font-size: 1.4rem;
      }

      .subsection-title {
        font-size: 1.15rem;
      }

      .toc-card {
        padding: 20px 18px;
      }

      .mistake-grid {
        grid-template-columns: 1fr;
      }

      .visual-card {
        padding: 16px 12px;
      }

      .code-body {
        padding: 14px 14px;
        font-size: 0.82rem;
      }

      .formula-block {
        font-size: 1.02rem;
        padding: 14px 12px;
      }
    }
"""
