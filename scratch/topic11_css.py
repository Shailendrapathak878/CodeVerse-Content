"""
Module: topic11_css.py
Light Mode only CSS styles for Topic 11: K-Nearest Neighbors (KNN).
Ensures zero horizontal overflow and 100% Flutter webview compatibility.
"""

TOPIC11_CSS = """
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
      
      /* Primary ML Theme: Indigo & Blue */
      --primary-accent: #4F46E5;
      --primary-accent-hover: #4338CA;
      --primary-accent-light: #EEF2FF;
      --primary-badge-bg: #EEF2FF;
      --primary-badge-text: #4338CA;
      --toc-bg: #F5F3FF;
      --toc-border: #DDD6FE;
      --toc-text: #4338CA;

      /* Definition Card (Soft Sky Blue) */
      --def-card-bg: #F0F9FF;
      --def-card-border: #BAE6FD;
      --def-card-title: #0284C7;
      --def-card-text: #0C4A6E;

      /* Analogy Card (Soft Teal / Mint) */
      --analogy-card-bg: #ECFEFF;
      --analogy-card-border: #A5F3FC;
      --analogy-card-title: #0891B2;
      --analogy-card-text: #164E63;

      /* Concept / Architecture Card (Soft Lavender) */
      --concept-card-bg: #FAF5FF;
      --concept-card-border: #E9D5FF;
      --concept-card-title: #7C3AED;
      --concept-card-text: #581C87;

      /* Warning / Pitfall Card (Soft Coral) */
      --warn-card-bg: #FEF2F2;
      --warn-card-border: #FECACA;
      --warn-card-title: #DC2626;
      --warn-card-text: #991B1B;

      /* Amber / Highlight Card */
      --amber-card-bg: #FFFBEB;
      --amber-card-border: #FDE68A;
      --amber-card-title: #D97706;
      --amber-card-text: #92400E;

      /* Success Card (Emerald) */
      --success-card-bg: #F0FDF4;
      --success-card-border: #BBF7D0;
      --success-card-title: #16A34A;
      --success-card-text: #166534;

      /* Code Block Colors */
      --code-bg: #0F172A;
      --code-text: #E2E8F0;
      --code-header-bg: #1E293B;

      /* Classification Badges */
      --tp-badge-bg: #DCFCE7;
      --tp-badge-text: #15803D;
      --fn-badge-bg: #FEE2E2;
      --fn-badge-text: #B91C1C;
      --fp-badge-bg: #FEF3C7;
      --fp-badge-text: #B45309;
      --tn-badge-bg: #F0FDF4;
      --tn-badge-text: #166534;
    }

    /* Reset & Containment */
    *, *::before, *::after {
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
      font-size: 0.9em;
      background-color: #F1F5F9;
      color: #0F172A;
      padding: 0.2em 0.4em;
      border-radius: 4px;
      border: 1px solid #E2E8F0;
    }

    pre code {
      background-color: transparent;
      color: inherit;
      padding: 0;
      border: none;
      font-size: 0.92rem;
      line-height: 1.55;
    }

    ul, ol {
      margin-bottom: 1.25rem;
      padding-left: 1.5rem;
      color: var(--text-secondary);
    }

    li {
      margin-bottom: 0.5rem;
    }

    /* Hero Header */
    .hero-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 2.25rem;
      margin-bottom: 2rem;
      box-shadow: var(--card-shadow);
      position: relative;
      overflow: hidden;
    }

    .hero-card::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 5px;
      background: linear-gradient(90deg, #4F46E5, #0284C7, #10B981, #F59E0B);
    }

    .hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 0.9rem;
      background: var(--primary-badge-bg);
      color: var(--primary-badge-text);
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
      color: #4338CA;
      font-size: 0.92rem;
      font-weight: 500;
      padding: 0.45rem 0.65rem;
      border-radius: 6px;
      background: #FFFFFF;
      border: 1px solid #E0E7FF;
      transition: all 0.15s ease-in-out;
    }

    .toc-link:hover {
      background: #EEF2FF;
      border-color: #C7D2FE;
      color: #312E81;
      transform: translateX(2px);
    }

    .toc-num {
      display: inline-block;
      width: 24px;
      height: 24px;
      line-height: 24px;
      text-align: center;
      background: #E0E7FF;
      color: #3730A3;
      border-radius: 4px;
      font-size: 0.78rem;
      font-weight: 700;
      flex-shrink: 0;
    }

    /* Section Styling */
    .section-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 2.25rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--card-shadow);
      scroll-margin-top: 2rem;
    }

    .section-badge {
      display: inline-block;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--primary-accent);
      background: var(--primary-accent-light);
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 0.75rem;
    }

    .section-title {
      font-size: 1.75rem;
      margin-bottom: 0.6rem;
      color: var(--heading-color);
      letter-spacing: -0.015em;
    }

    .section-lead {
      font-size: 1.1rem;
      color: var(--text-secondary);
      line-height: 1.6;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #F1F5F9;
    }

    h3.sub-title {
      font-size: 1.3rem;
      margin-top: 1.85rem;
      margin-bottom: 0.85rem;
      color: var(--heading-color);
    }

    h4.sub-sub-title {
      font-size: 1.1rem;
      margin-top: 1.35rem;
      margin-bottom: 0.65rem;
      color: #1E293B;
    }

    /* Specialized Callout Cards */
    .callout {
      border-radius: 10px;
      padding: 1.35rem 1.5rem;
      margin: 1.5rem 0;
      border: 1px solid transparent;
      position: relative;
    }

    .callout-title {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .card-definition {
      background: var(--def-card-bg);
      border-color: var(--def-card-border);
      color: var(--def-card-text);
    }
    .card-definition .callout-title { color: var(--def-card-title); }

    .card-analogy {
      background: var(--analogy-card-bg);
      border-color: var(--analogy-card-border);
      color: var(--analogy-card-text);
    }
    .card-analogy .callout-title { color: var(--analogy-card-title); }

    .card-concept {
      background: var(--concept-card-bg);
      border-color: var(--concept-card-border);
      color: var(--concept-card-text);
    }
    .card-concept .callout-title { color: var(--concept-card-title); }

    .card-warning {
      background: var(--warn-card-bg);
      border-color: var(--warn-card-border);
      color: var(--warn-card-text);
    }
    .card-warning .callout-title { color: var(--warn-card-title); }

    .card-amber {
      background: var(--amber-card-bg);
      border-color: var(--amber-card-border);
      color: var(--amber-card-text);
    }
    .card-amber .callout-title { color: var(--amber-card-title); }

    .card-success {
      background: var(--success-card-bg);
      border-color: var(--success-card-border);
      color: var(--success-card-text);
    }
    .card-success .callout-title { color: var(--success-card-title); }

    /* Formula Cards */
    .formula-card {
      background: #FFFFFF;
      border: 1.5px solid #CBD5E1;
      border-radius: 12px;
      padding: 1.5rem;
      margin: 1.5rem 0;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    .formula-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: #334155;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .formula-math {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      padding: 1rem 1.25rem;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 1.15rem;
      font-weight: 700;
      color: #1E293B;
      text-align: center;
      margin-bottom: 1rem;
      overflow-x: auto;
    }

    .formula-legend {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 0.5rem 1rem;
      font-size: 0.9rem;
      color: #475569;
      padding-top: 0.75rem;
      border-top: 1px dashed #CBD5E1;
    }

    .formula-legend-item {
      display: flex;
      align-items: baseline;
      gap: 0.4rem;
    }

    .formula-legend-item code {
      font-weight: 700;
      color: var(--primary-accent);
      background: #EEF2FF;
      border-color: #C7D2FE;
    }

    /* Responsive Tables */
    .table-wrapper {
      width: 100%;
      overflow-x: auto;
      margin: 1.5rem 0;
      border-radius: 10px;
      border: 1px solid var(--card-border);
      background: #FFFFFF;
      -webkit-overflow-scrolling: touch;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.95rem;
      text-align: left;
    }

    th {
      background: #F1F5F9;
      color: #0F172A;
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-bottom: 2px solid #CBD5E1;
      white-space: nowrap;
    }

    td {
      padding: 0.85rem 1rem;
      border-bottom: 1px solid #E2E8F0;
      color: var(--text-secondary);
      vertical-align: middle;
    }

    tr:nth-child(even) td {
      background: #F8FAFC;
    }

    tr:hover td {
      background: #F1F5F9;
    }

    /* SVG Containers */
    .svg-card {
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-radius: 12px;
      padding: 1.5rem;
      margin: 1.75rem 0;
      box-shadow: 0 3px 10px rgba(15, 23, 42, 0.04);
    }

    .svg-container {
      width: 100%;
      max-width: 100%;
      overflow: hidden;
      display: flex;
      justify-content: center;
      margin-bottom: 1rem;
    }

    .svg-container svg {
      width: 100%;
      max-width: 100%;
      height: auto;
      display: block;
    }

    .svg-caption {
      font-size: 0.92rem;
      color: #475569;
      text-align: center;
      padding: 0.5rem 0.75rem;
      background: #F8FAFC;
      border-radius: 6px;
      border: 1px solid #E2E8F0;
    }

    .svg-takeaway {
      margin-top: 0.75rem;
      font-size: 0.88rem;
      color: #1E293B;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    /* Code Blocks */
    .code-block {
      background: var(--code-bg);
      border-radius: 10px;
      margin: 1.5rem 0;
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
    }

    .code-header {
      background: var(--code-header-bg);
      padding: 0.6rem 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
    }

    .code-title {
      font-size: 0.85rem;
      font-weight: 600;
      color: #94A3B8;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .code-lang {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      color: #38BDF8;
      background: rgba(56, 189, 248, 0.1);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }

    pre {
      padding: 1.25rem 1rem;
      overflow-x: auto;
      color: var(--code-text);
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 0.9rem;
      line-height: 1.55;
      -webkit-overflow-scrolling: touch;
    }

    /* Accordions / Details */
    details.accordion {
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-radius: 10px;
      margin: 1rem 0;
      overflow: hidden;
      transition: all 0.2s ease;
    }

    details.accordion[open] {
      border-color: #94A3B8;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
    }

    summary.accordion-summary {
      padding: 1rem 1.25rem;
      font-weight: 700;
      font-size: 1.05rem;
      color: #0F172A;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #F8FAFC;
      user-select: none;
      list-style: none;
    }

    summary.accordion-summary::-webkit-details-marker {
      display: none;
    }

    summary.accordion-summary::after {
      content: "▼";
      font-size: 0.8rem;
      color: #64748B;
      transition: transform 0.2s ease;
    }

    details.accordion[open] summary.accordion-summary::after {
      transform: rotate(180deg);
      color: var(--primary-accent);
    }

    .accordion-content {
      padding: 1.25rem;
      background: #FFFFFF;
      border-top: 1px solid #E2E8F0;
    }

    /* Badges */
    .badge {
      display: inline-block;
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .badge-tp { background: var(--tp-badge-bg); color: var(--tp-badge-text); }
    .badge-fn { background: var(--fn-badge-bg); color: var(--fn-badge-text); }
    .badge-fp { background: var(--fp-badge-bg); color: var(--fp-badge-text); }
    .badge-tn { background: var(--tn-badge-bg); color: var(--tn-badge-text); }

    /* Step lists */
    .step-list {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin: 1.5rem 0;
    }

    .step-card {
      display: flex;
      gap: 1rem;
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-radius: 10px;
      padding: 1.25rem;
      align-items: flex-start;
    }

    .step-number {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--primary-accent);
      color: #FFFFFF;
      font-weight: 700;
      font-size: 0.95rem;
      flex-shrink: 0;
    }

    .step-body h4 {
      font-size: 1.05rem;
      color: #0F172A;
      margin-bottom: 0.35rem;
    }

    .step-body p {
      font-size: 0.95rem;
      color: #475569;
      margin-bottom: 0;
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
