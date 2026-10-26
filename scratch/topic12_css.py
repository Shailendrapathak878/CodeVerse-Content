"""
Module: topic12_css.py
Contains complete, production-grade, accessible CSS for Topic 12: Decision Trees.
STRICT REQUIREMENT: Light Mode Only (Zero dark mode media queries or toggles).
"""

TOPIC12_CSS = """
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
      
      /* Primary Topic 12 Theme: Emerald, Forest Teal & Indigo */
      --primary-accent: #059669;
      --primary-accent-hover: #047857;
      --primary-accent-light: #ECFDF5;
      --primary-badge-bg: #ECFDF5;
      --primary-badge-text: #065F46;
      --toc-bg: #F0FDF4;
      --toc-border: #BBF7D0;
      --toc-text: #047857;

      /* Definition Card (Soft Sky Blue) */
      --def-card-bg: #F0F9FF;
      --def-card-border: #BAE6FD;
      --def-card-title: #0284C7;
      --def-card-text: #0C4A6E;

      /* Analogy Card (Soft Amber) */
      --analogy-card-bg: #FFFBEB;
      --analogy-card-border: #FDE68A;
      --analogy-card-title: #D97706;
      --analogy-card-text: #78350F;

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
      color: #0369A1;
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
      background: #ECFDF5;
      color: #047857;
      border: 1px solid #A7F3D0;
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
      text-decoration: none;
      color: var(--text-secondary);
      font-size: 0.92rem;
      padding: 0.4rem 0.65rem;
      border-radius: 6px;
      transition: all 0.15s ease-in-out;
      background: rgba(255, 255, 255, 0.6);
      border: 1px solid rgba(226, 232, 240, 0.7);
    }

    .toc-link:hover {
      background: #FFFFFF;
      color: var(--primary-accent);
      border-color: var(--primary-accent);
      transform: translateX(2px);
    }

    .toc-num {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 22px;
      height: 22px;
      border-radius: 4px;
      background: #E2E8F0;
      color: #334155;
      font-size: 0.75rem;
      font-weight: 700;
      font-family: monospace;
      flex-shrink: 0;
    }

    /* Pedagogical Callout Cards */
    .callout {
      border-radius: 10px;
      padding: 1.25rem 1.4rem;
      margin: 1.5rem 0;
      border-left: 4px solid;
    }

    .callout-title {
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .callout-def {
      background-color: var(--def-card-bg);
      border-color: var(--def-card-title);
      border: 1px solid var(--def-card-border);
      border-left-width: 4px;
    }
    .callout-def .callout-title { color: var(--def-card-title); }
    .callout-def p { color: var(--def-card-text); }

    .callout-analogy {
      background-color: var(--analogy-card-bg);
      border-color: var(--analogy-card-title);
      border: 1px solid var(--analogy-card-border);
      border-left-width: 4px;
    }
    .callout-analogy .callout-title { color: var(--analogy-card-title); }
    .callout-analogy p { color: var(--analogy-card-text); }

    .callout-warning {
      background-color: var(--warn-card-bg);
      border-color: var(--warn-card-title);
      border: 1px solid var(--warn-card-border);
      border-left-width: 4px;
    }
    .callout-warning .callout-title { color: var(--warn-card-title); }
    .callout-warning p { color: var(--warn-card-text); }

    .callout-info {
      background-color: #ECFDF5;
      border-color: #059669;
      border: 1px solid #A7F3D0;
      border-left-width: 4px;
    }
    .callout-info .callout-title { color: #047857; }
    .callout-info p { color: #065F46; }

    /* Tables */
    .table-wrapper {
      width: 100%;
      overflow-x: auto;
      margin: 1.5rem 0;
      border: 1px solid var(--table-border);
      border-radius: 10px;
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02);
      -webkit-overflow-scrolling: touch;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
      min-width: 580px;
    }

    th {
      background: var(--table-header-bg);
      color: var(--heading-color);
      font-weight: 700;
      padding: 0.85rem 1.1rem;
      border-bottom: 2px solid var(--table-border);
    }

    td {
      padding: 0.85rem 1.1rem;
      border-bottom: 1px solid var(--table-border);
      color: var(--text-secondary);
      vertical-align: top;
    }

    tr:nth-child(even) td {
      background-color: var(--table-row-alt);
    }

    tr:last-child td {
      border-bottom: none;
    }

    /* Math & Formula Boxes */
    .formula-card {
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-left: 4px solid var(--primary-accent);
      border-radius: 8px;
      padding: 1.25rem 1.5rem;
      margin: 1.5rem 0;
      box-shadow: 0 2px 4px rgba(15, 23, 42, 0.03);
    }

    .formula-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.65rem;
    }

    .formula-math {
      font-size: 1.25rem;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      color: var(--heading-color);
      text-align: center;
      padding: 1rem;
      background: #F8FAFC;
      border-radius: 6px;
      margin: 0.75rem 0;
      border: 1px solid #E2E8F0;
      overflow-x: auto;
    }

    .formula-legend {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 0.5rem;
      margin-top: 0.85rem;
      font-size: 0.88rem;
      color: var(--text-secondary);
    }

    .legend-item {
      display: flex;
      gap: 0.4rem;
    }

    .legend-sym {
      font-family: monospace;
      font-weight: 700;
      color: var(--primary-accent);
      min-width: 25px;
    }

    /* SVG Presentation Cards */
    .svg-card {
      background: #FFFFFF;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 1.5rem;
      margin: 1.75rem 0;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03);
    }

    .svg-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      padding-bottom: 0.75rem;
      border-bottom: 1px solid #F1F5F9;
    }

    .svg-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--heading-color);
    }

    .svg-badge {
      font-size: 0.78rem;
      font-weight: 700;
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      background: var(--card-soft-bg);
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .svg-wrapper {
      width: 100%;
      overflow-x: auto;
      display: flex;
      justify-content: center;
      background: #FFFFFF;
      border-radius: 8px;
      padding: 0.5rem 0;
      -webkit-overflow-scrolling: touch;
    }

    .svg-wrapper svg {
      max-width: 100%;
      height: auto;
      display: block;
    }

    .svg-caption {
      margin-top: 1rem;
      font-size: 0.92rem;
      color: var(--text-secondary);
      line-height: 1.55;
      padding: 0.75rem 1rem;
      background: #F8FAFC;
      border-radius: 6px;
      border-left: 3px solid var(--primary-accent);
    }

    /* Accordion / Revision Component */
    .accordion {
      border: 1px solid var(--card-border);
      border-radius: 8px;
      margin-bottom: 0.85rem;
      overflow: hidden;
      background: #FFFFFF;
    }

    .accordion-summary {
      padding: 1rem 1.25rem;
      font-weight: 600;
      color: var(--heading-color);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #FFFFFF;
      transition: background 0.15s ease;
      user-select: none;
      list-style: none;
    }

    .accordion-summary::-webkit-details-marker {
      display: none;
    }

    .accordion-summary:hover {
      background: #F8FAFC;
      color: var(--primary-accent);
    }

    .accordion-icon {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text-muted);
      transition: transform 0.2s ease;
    }

    details[open] .accordion-icon {
      transform: rotate(45deg);
      color: var(--primary-accent);
    }

    .accordion-content {
      padding: 1.15rem 1.25rem;
      border-top: 1px solid var(--card-border);
      background: #F8FAFC;
      color: var(--text-secondary);
      font-size: 0.95rem;
      line-height: 1.65;
    }

    /* Code Containers & Syntax Presentation (Light Mode Premium) */
    .code-container {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-radius: 12px;
      margin: 1.5rem 0 2rem 0;
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
    }

    .code-header {
      background: #F1F5F9;
      border-bottom: 1px solid #E2E8F0;
      padding: 0.65rem 1.25rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .code-lang {
      color: #0284C7;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .code-tag {
      color: #64748B;
      font-weight: 600;
      font-size: 0.8rem;
      text-transform: none;
    }

    .code-container pre {
      margin: 0;
      padding: 1.25rem 1.5rem;
      overflow-x: auto;
      background: #FFFFFF;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 0.92rem;
      line-height: 1.7;
      color: #0F172A !important;
      tab-size: 4;
      -webkit-font-smoothing: antialiased;
    }

    .code-container pre code {
      background: transparent !important;
      color: #0F172A !important;
      padding: 0 !important;
      border: none !important;
      font-size: inherit !important;
      display: block;
      white-space: pre;
    }

    /* Calculation & Step Containers */
    .calc-box {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 1.35rem 1.5rem;
      margin-bottom: 1.25rem;
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02);
    }

    .formula-block {
      background: #F1F5F9;
      border-left: 4px solid var(--primary-accent);
      padding: 0.85rem 1.25rem;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 1.02rem;
      font-weight: 700;
      color: #1E293B;
      border-radius: 0 8px 8px 0;
      margin: 0.75rem 0;
    }

    .grid-2col {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.25rem;
      margin-top: 1.25rem;
    }

    /* 15 Common Mistakes Cards */
    .mistake-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-left: 4px solid #EF4444;
      border-radius: 8px;
      padding: 1.25rem 1.5rem;
      margin-bottom: 1.25rem;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .mistake-card:hover {
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.06);
    }

    .mistake-header {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      margin-bottom: 0.75rem;
    }

    .mistake-icon {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 26px;
      height: 26px;
      background: #FEE2E2;
      color: #B91C1C;
      font-size: 1.1rem;
      font-weight: 800;
      border-radius: 50%;
      flex-shrink: 0;
    }

    .mistake-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: #0F172A;
    }

    .mistake-text {
      color: #475569;
      font-size: 0.95rem;
      line-height: 1.6;
      margin-bottom: 0.65rem;
    }

    .mistake-fix {
      color: #065F46;
      background: #ECFDF5;
      border: 1px solid #A7F3D0;
      border-radius: 6px;
      padding: 0.65rem 0.95rem;
      font-size: 0.93rem;
      line-height: 1.6;
      margin: 0;
    }

    /* Responsive Queries */
    @media (max-width: 768px) {
      .container {
        padding: 1.5rem 0.85rem;
      }
      .hero-card {
        padding: 1.5rem 1.25rem;
      }
      .hero-title {
        font-size: 1.85rem;
      }
      .hero-subtitle {
        font-size: 1.025rem;
      }
      .section-card {
        padding: 1.5rem 1.15rem;
      }
      .section-title {
        font-size: 1.45rem;
      }
      .toc-grid {
        grid-template-columns: 1fr;
      }
      .formula-legend {
        grid-template-columns: 1fr;
      }
      .grid-2col {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 480px) {
      html, body {
        font-size: 15px;
      }
      .container {
        padding: 1rem 0.65rem;
      }
      .hero-card {
        padding: 1.25rem 0.85rem;
      }
      .hero-title {
        font-size: 1.6rem;
      }
      .section-card {
        padding: 1.25rem 0.85rem;
      }
      .section-title {
        font-size: 1.3rem;
      }
      .table-wrapper {
        margin: 1rem 0;
      }
      th, td {
        padding: 0.65rem 0.75rem;
        font-size: 0.88rem;
      }
      pre {
        padding: 1rem 0.75rem;
        font-size: 0.82rem;
      }
      .svg-card {
        padding: 1rem 0.75rem;
      }
    }
"""
