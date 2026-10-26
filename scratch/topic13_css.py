"""
Topic 13: Support Vector Machine (SVM) - CSS Stylesheet
Strict Light Mode only. Highly responsive, high contrast, beautiful modern card-based UI.
"""

TOPIC13_CSS = """
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
      
      /* Topic 13 Theme: Royal Sapphire Blue, Indigo & Emerald */
      --primary-accent: #2563EB;
      --primary-accent-hover: #1D4ED8;
      --primary-accent-light: #EFF6FF;
      --primary-badge-bg: #EFF6FF;
      --primary-badge-text: #1E40AF;
      --toc-bg: #F8FAFC;
      --toc-border: #BFDBFE;
      --toc-text: #1D4ED8;

      /* Definition Card (Soft Sky/Sapphire Blue) */
      --def-card-bg: #F0F9FF;
      --def-card-border: #BAE6FD;
      --def-card-title: #0284C7;
      --def-card-text: #0C4A6E;

      /* Analogy Card (Soft Amber) */
      --analogy-card-bg: #FFFBEB;
      --analogy-card-border: #FDE68A;
      --analogy-card-title: #D97706;
      --analogy-card-text: #78350F;

      /* Success / Highlight Card (Emerald) */
      --success-card-bg: #ECFDF5;
      --success-card-border: #A7F3D0;
      --success-card-title: #059669;
      --success-card-text: #065F46;

      /* Warning / Pitfall Card */
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
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-primary);
      line-height: 1.65;
      font-size: 16px;
      overflow-x: hidden;
      max-width: 100vw;
      -webkit-font-smoothing: antialiased;
    }

    .container {
      max-width: 980px;
      margin: 0 auto;
      padding: 2.5rem 1.25rem;
      width: 100%;
      overflow-x: hidden;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
      color: var(--heading-color);
      font-weight: 700;
      line-height: 1.3;
    }

    p {
      margin-bottom: 1.15rem;
      color: var(--text-secondary);
      font-size: 1.025rem;
    }

    p:last-child {
      margin-bottom: 0;
    }

    strong {
      color: var(--text-primary);
      font-weight: 600;
    }

    code {
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 0.88em;
      background-color: #F1F5F9;
      color: #1D4ED8;
      padding: 0.2em 0.45em;
      border-radius: 4px;
      border: 1px solid #E2E8F0;
      font-weight: 600;
    }

    /* Cards & Containers */
    .hero-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-top: 5px solid var(--primary-accent);
      border-radius: 14px;
      padding: 2.25rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--card-shadow);
    }

    .section-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 2.25rem;
      margin-bottom: 2.25rem;
      box-shadow: var(--card-shadow);
      scroll-margin-top: 2rem;
    }

    .section-badge {
      display: inline-block;
      padding: 0.25rem 0.75rem;
      background: var(--primary-badge-bg);
      color: var(--primary-badge-text);
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.75rem;
    }

    .section-title {
      font-size: 1.65rem;
      margin-bottom: 1rem;
      color: var(--heading-color);
      letter-spacing: -0.015em;
    }

    .section-lead {
      font-size: 1.1rem;
      color: var(--text-secondary);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .sub-title {
      font-size: 1.25rem;
      margin: 1.75rem 0 0.85rem 0;
      color: var(--heading-color);
      font-weight: 700;
      border-bottom: 1px solid #F1F5F9;
      padding-bottom: 0.4rem;
    }

    /* Hero Header Elements */
    .hero-topic-badge {
      display: inline-block;
      padding: 0.35rem 0.85rem;
      background: #EFF6FF;
      color: #1E40AF;
      border: 1px solid #BFDBFE;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 1rem;
    }

    .hero-title {
      font-size: 2.35rem;
      font-weight: 800;
      margin-bottom: 0.85rem;
      letter-spacing: -0.025em;
      color: var(--heading-color);
    }

    .hero-subtitle {
      font-size: 1.15rem;
      color: var(--text-secondary);
      line-height: 1.6;
      margin-bottom: 1.5rem;
      max-width: 900px;
    }

    .meta-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      padding-top: 1.25rem;
      border-top: 1px solid #F1F5F9;
    }

    .meta-pill {
      font-size: 0.85rem;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      background: var(--card-soft-bg);
      color: var(--text-secondary);
      font-weight: 500;
    }

    /* Table of Contents */
    .toc-card {
      background: var(--toc-bg);
      border: 1px solid var(--toc-border);
      border-radius: 14px;
      padding: 1.75rem;
      margin-bottom: 2.5rem;
    }

    .toc-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--toc-text);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .toc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 0.6rem;
    }

    .toc-link {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 0.65rem;
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      color: #334155;
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 500;
      transition: all 0.15s ease;
    }

    .toc-link:hover {
      background: var(--primary-accent-light);
      border-color: var(--primary-accent);
      color: var(--primary-accent);
      transform: translateX(2px);
    }

    .toc-num {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: #EFF6FF;
      color: #1D4ED8;
      font-size: 0.75rem;
      font-weight: 700;
      flex-shrink: 0;
    }

    /* Callout & Analogy Boxes */
    .analogy-box {
      background: var(--analogy-card-bg);
      border: 1px solid var(--analogy-card-border);
      border-left: 4px solid var(--analogy-card-title);
      border-radius: 10px;
      padding: 1.25rem 1.4rem;
      margin: 1.5rem 0;
    }

    .analogy-title {
      font-size: 1rem;
      font-weight: 700;
      color: var(--analogy-card-title);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }

    .def-box {
      background: var(--def-card-bg);
      border: 1px solid var(--def-card-border);
      border-left: 4px solid var(--def-card-title);
      border-radius: 10px;
      padding: 1.25rem 1.4rem;
      margin: 1.5rem 0;
    }

    .def-title {
      font-size: 1rem;
      font-weight: 700;
      color: var(--def-card-title);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }

    .warn-box {
      background: var(--warn-card-bg);
      border: 1px solid var(--warn-card-border);
      border-left: 4px solid var(--warn-card-title);
      border-radius: 10px;
      padding: 1.25rem 1.4rem;
      margin: 1.5rem 0;
    }

    .warn-title {
      font-size: 1rem;
      font-weight: 700;
      color: var(--warn-card-title);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }

    .success-box {
      background: var(--success-card-bg);
      border: 1px solid var(--success-card-border);
      border-left: 4px solid var(--success-card-title);
      border-radius: 10px;
      padding: 1.25rem 1.4rem;
      margin: 1.5rem 0;
    }

    .success-title {
      font-size: 1rem;
      font-weight: 700;
      color: var(--success-card-title);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }

    /* Math Formulas */
    .formula-block {
      background: #FFFFFF;
      border: 1px solid var(--card-border);
      border-left: 4px solid var(--primary-accent);
      border-radius: 10px;
      padding: 1.25rem 1.5rem;
      margin: 1.5rem 0;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }

    .formula-header {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--primary-accent);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .math-display {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--heading-color);
      text-align: center;
      margin: 1rem 0;
      padding: 0.85rem;
      background: #F8FAFC;
      border-radius: 6px;
      border: 1px solid #E2E8F0;
      overflow-x: auto;
    }

    .formula-legend {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 0.6rem;
      font-size: 0.9rem;
      color: var(--text-secondary);
      margin-top: 0.85rem;
      border-top: 1px solid #F1F5F9;
      padding-top: 0.85rem;
    }

    .legend-item {
      display: flex;
      gap: 0.4rem;
      align-items: baseline;
    }

    .legend-symbol {
      font-weight: 700;
      color: var(--primary-accent);
      font-family: monospace;
    }

    /* Worked Calculations */
    .calc-box {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 1.25rem;
      margin: 1.25rem 0;
    }

    .calc-step {
      margin-bottom: 0.85rem;
      padding-left: 1rem;
      border-left: 2px solid #CBD5E1;
    }

    .calc-step:last-child {
      margin-bottom: 0;
    }

    .step-title {
      font-weight: 700;
      color: var(--heading-color);
      font-size: 0.95rem;
      margin-bottom: 0.25rem;
    }

    /* Tables */
    .table-wrapper {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin: 1.5rem 0;
      border: 1px solid var(--table-border);
      border-radius: 10px;
      background: #FFFFFF;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.95rem;
      text-align: left;
    }

    th {
      background-color: var(--table-header-bg);
      color: var(--heading-color);
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-bottom: 2px solid var(--table-border);
    }

    td {
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--table-border);
      color: var(--text-secondary);
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:nth-child(even) td {
      background-color: var(--table-row-alt);
    }

    /* Figure & SVG Containers */
    .figure-container {
      margin: 2rem 0;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 1.25rem;
      background: #FFFFFF;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    .figure-caption {
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-top: 0.85rem;
      padding-left: 0.75rem;
      border-left: 3px solid var(--primary-accent);
      line-height: 1.5;
    }

    .figure-caption strong {
      color: var(--text-secondary);
    }

    /* Code Blocks */
    .code-container {
      margin: 1.5rem 0;
      border-radius: 10px;
      overflow: hidden;
      border: 1px solid #CBD5E1;
      background: #FFFFFF;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .code-header {
      background: #F1F5F9;
      padding: 0.5rem 1rem;
      font-size: 0.8rem;
      font-weight: 700;
      color: #334155;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid #CBD5E1;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .code-container pre {
      margin: 0;
      padding: 1.25rem;
      background: #FFFFFF !important;
      color: #0F172A !important;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 0.9rem;
      line-height: 1.55;
      overflow-x: auto;
      tab-size: 4;
    }

    .code-container code {
      background: transparent !important;
      color: #0F172A !important;
      border: none !important;
      padding: 0 !important;
      font-size: inherit;
    }

    /* Grid Layouts */
    .grid-2col {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.25rem;
      margin: 1.5rem 0;
    }

    /* Mistake Cards */
    .mistake-card {
      background: #FFFFFF;
      border: 1px solid #FECACA;
      border-left: 4px solid #DC2626;
      border-radius: 10px;
      padding: 1.25rem;
      margin-bottom: 1rem;
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }

    .mistake-header {
      font-size: 1.05rem;
      font-weight: 700;
      color: #991B1B;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .mistake-body {
      color: var(--text-secondary);
      font-size: 0.95rem;
      margin-bottom: 0.75rem;
    }

    .fix-box {
      background: #F0FDF4;
      border: 1px solid #BBF7D0;
      border-left: 3px solid #16A34A;
      border-radius: 6px;
      padding: 0.75rem 1rem;
      font-size: 0.92rem;
      color: #14532D;
    }

    .fix-box strong {
      color: #166534;
    }

    /* Accordion Revision Questions */
    .accordion-item {
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      margin-bottom: 0.75rem;
      background: #FFFFFF;
      overflow: hidden;
    }

    .accordion-header {
      padding: 1rem 1.25rem;
      font-weight: 700;
      color: var(--heading-color);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #F8FAFC;
      transition: background 0.15s ease;
      font-size: 1rem;
    }

    .accordion-header:hover {
      background: #EFF6FF;
      color: #1D4ED8;
    }

    .accordion-content {
      padding: 1.25rem;
      border-top: 1px solid #E2E8F0;
      color: var(--text-secondary);
      font-size: 0.95rem;
      line-height: 1.6;
      background: #FFFFFF;
    }

    details summary {
      list-style: none;
    }

    details summary::-webkit-details-marker {
      display: none;
    }

    details summary::after {
      content: "+";
      font-size: 1.2rem;
      font-weight: 700;
      color: #2563EB;
      float: right;
    }

    details[open] summary::after {
      content: "−";
    }

    /* Responsive Queries */
    @media (max-width: 768px) {
      .container {
        padding: 1.25rem 0.85rem;
      }
      .hero-card, .section-card {
        padding: 1.5rem 1rem;
      }
      .hero-title {
        font-size: 1.85rem;
      }
      .section-title {
        font-size: 1.4rem;
      }
      .toc-grid {
        grid-template-columns: 1fr;
      }
      .grid-2col {
        grid-template-columns: 1fr;
      }
      .math-display {
        font-size: 1.05rem;
      }
    }

    @media (max-width: 480px) {
      .hero-title {
        font-size: 1.6rem;
      }
      .hero-subtitle {
        font-size: 1rem;
      }
      .code-container pre {
        font-size: 0.82rem;
        padding: 0.85rem;
      }
    }
"""
