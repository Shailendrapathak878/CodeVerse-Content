"""
Topic 14: Naive Bayes - CSS Stylesheet
Strict Light Mode only. Highly responsive, high contrast, beautiful modern card-based UI.
Color Theme: Royal Violet / Amethyst & Indigo (#7C3AED)
"""

TOPIC14_CSS = """
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
      
      /* Topic 14 Theme: Royal Violet / Deep Amethyst & Indigo */
      --primary-accent: #7C3AED;
      --primary-accent-hover: #6D28D9;
      --primary-accent-light: #F5F3FF;
      --primary-badge-bg: #F5F3FF;
      --primary-badge-text: #6D28D9;
      --toc-bg: #F8FAFC;
      --toc-border: #DDD6FE;
      --toc-text: #6D28D9;

      /* Definition Card (Soft Sky/Amethyst) */
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
      padding: 24px 20px 80px 20px;
      overflow-x: hidden;
      width: 100%;
    }

    /* Hero Section */
    .hero-header {
      background: #FFFFFF;
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 36px 32px;
      margin-bottom: 32px;
      box-shadow: var(--card-shadow);
      position: relative;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: var(--primary-badge-bg);
      color: var(--primary-badge-text);
      font-size: 12px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 16px;
      border: 1px solid var(--toc-border);
    }

    .hero-title {
      font-size: 32px;
      font-weight: 800;
      color: var(--heading-color);
      line-height: 1.25;
      margin-bottom: 12px;
      letter-spacing: -0.02em;
    }

    .hero-desc {
      font-size: 17px;
      color: var(--text-secondary);
      line-height: 1.6;
      margin-bottom: 20px;
    }

    .hero-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      padding-top: 16px;
      border-top: 1px solid var(--card-border);
    }

    .hero-meta-item {
      display: flex;
      flex-direction: column;
    }

    .hero-meta-label {
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .hero-meta-value {
      font-size: 14px;
      font-weight: 700;
      color: var(--text-primary);
    }

    /* Table of Contents */
    .toc-card {
      background: var(--card-bg);
      border: 1px solid var(--toc-border);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 36px;
      box-shadow: var(--card-shadow);
    }

    .toc-title {
      font-size: 18px;
      font-weight: 700;
      color: var(--toc-text);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .toc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 10px 18px;
      list-style: none;
    }

    .toc-link {
      display: flex;
      align-items: baseline;
      gap: 8px;
      color: var(--text-secondary);
      text-decoration: none;
      font-size: 14px;
      padding: 4px 6px;
      border-radius: 6px;
      transition: background-color 0.15s ease, color 0.15s ease;
    }

    .toc-link:hover {
      background-color: var(--primary-accent-light);
      color: var(--primary-accent);
    }

    .toc-number {
      font-size: 11px;
      font-weight: 700;
      color: var(--primary-accent);
      min-width: 20px;
    }

    /* Section Cards */
    .content-section {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 32px;
      margin-bottom: 32px;
      box-shadow: var(--card-shadow);
      overflow-x: hidden;
      width: 100%;
    }

    .section-header {
      margin-bottom: 24px;
      padding-bottom: 14px;
      border-bottom: 2px solid var(--primary-accent-light);
    }

    .section-badge {
      font-size: 12px;
      font-weight: 700;
      color: var(--primary-accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
      display: block;
    }

    .section-title {
      font-size: 24px;
      font-weight: 800;
      color: var(--heading-color);
      letter-spacing: -0.01em;
    }

    .section-subtitle {
      font-size: 14px;
      color: var(--text-muted);
      margin-top: 4px;
    }

    h3 {
      font-size: 18px;
      font-weight: 700;
      color: var(--heading-color);
      margin: 24px 0 12px 0;
    }

    h4 {
      font-size: 15px;
      font-weight: 700;
      color: var(--text-secondary);
      margin: 18px 0 8px 0;
    }

    p {
      margin-bottom: 16px;
      color: var(--text-secondary);
      font-size: 15px;
      line-height: 1.7;
    }

    p:last-child {
      margin-bottom: 0;
    }

    ul, ol {
      margin-left: 20px;
      margin-bottom: 16px;
      color: var(--text-secondary);
    }

    li {
      margin-bottom: 8px;
      line-height: 1.6;
      font-size: 15px;
    }

    /* Specialized Callout Cards */
    .callout-card {
      border-radius: 10px;
      padding: 18px 20px;
      margin: 20px 0;
      border: 1px solid;
    }

    .def-card {
      background-color: var(--def-card-bg);
      border-color: var(--def-card-border);
    }

    .def-title {
      color: var(--def-card-title);
      font-size: 14px;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .def-card p {
      color: var(--def-card-text);
      font-size: 14px;
    }

    .analogy-card {
      background-color: var(--analogy-card-bg);
      border-color: var(--analogy-card-border);
    }

    .analogy-title {
      color: var(--analogy-card-title);
      font-size: 14px;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .analogy-card p {
      color: var(--analogy-card-text);
      font-size: 14px;
    }

    .success-card {
      background-color: var(--success-card-bg);
      border-color: var(--success-card-border);
    }

    .success-title {
      color: var(--success-card-title);
      font-size: 14px;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .success-card p {
      color: var(--success-card-text);
      font-size: 14px;
    }

    .warn-card {
      background-color: var(--warn-card-bg);
      border-color: var(--warn-card-border);
    }

    .warn-title {
      color: var(--warn-card-title);
      font-size: 14px;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .warn-card p {
      color: var(--warn-card-text);
      font-size: 14px;
    }

    /* Math Formulas and Calculation Boxes */
    .formula-block {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-left: 4px solid var(--primary-accent);
      border-radius: 8px;
      padding: 16px 20px;
      margin: 18px 0;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 14px;
      color: var(--text-primary);
      overflow-x: auto;
      line-height: 1.6;
    }

    .formula-title {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 12px;
      font-weight: 700;
      color: var(--primary-accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
    }

    .calc-box {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-radius: 8px;
      padding: 16px 20px;
      margin: 18px 0;
      font-size: 14px;
    }

    .calc-title {
      font-weight: 700;
      color: var(--heading-color);
      margin-bottom: 10px;
      font-size: 14px;
    }

    .calc-step {
      display: flex;
      gap: 10px;
      margin-bottom: 8px;
      align-items: baseline;
    }

    .calc-step-num {
      font-weight: 700;
      color: var(--primary-accent);
      font-size: 12px;
      min-width: 24px;
    }

    /* Code Blocks */
    .code-container {
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-radius: 10px;
      margin: 20px 0;
      overflow: hidden;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
    }

    .code-header {
      background: #F1F5F9;
      border-bottom: 1px solid #CBD5E1;
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      font-weight: 600;
      color: #475569;
    }

    .code-lang-badge {
      background: #E2E8F0;
      color: #334155;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
    }

    .code-body {
      padding: 16px;
      background: #FAFAFA;
      color: #1E293B;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 13px;
      line-height: 1.6;
      overflow-x: auto;
      white-space: pre;
    }

    .code-output {
      background: #F8FAFC;
      border-top: 1px dashed #CBD5E1;
      padding: 14px 16px;
      font-family: "SFMono-Regular", Consolas, monospace;
      font-size: 12px;
      color: #0F172A;
      overflow-x: auto;
      white-space: pre-wrap;
      line-height: 1.5;
    }

    .code-output-title {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: #64748B;
      margin-bottom: 6px;
      letter-spacing: 0.05em;
    }

    /* Visual Containers / SVG */
    .visual-container {
      margin: 26px 0;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      overflow: hidden;
      background: #FFFFFF;
      box-shadow: var(--card-shadow);
      width: 100%;
    }

    .svg-wrapper {
      width: 100%;
      overflow-x: auto;
      display: flex;
      justify-content: center;
      background: #FFFFFF;
      padding: 12px;
    }

    .svg-wrapper svg {
      max-width: 100%;
      height: auto;
      display: block;
    }

    .visual-caption {
      background: #F8FAFC;
      border-top: 1px solid var(--card-border);
      padding: 10px 16px;
      font-size: 13px;
      color: var(--text-secondary);
      font-weight: 500;
      display: flex;
      align-items: baseline;
      gap: 6px;
    }

    .visual-caption strong {
      color: var(--primary-accent);
      font-weight: 700;
    }

    /* Tables */
    .table-wrapper {
      width: 100%;
      overflow-x: auto;
      margin: 20px 0;
      border: 1px solid var(--table-border);
      border-radius: 10px;
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
      text-align: left;
    }

    th {
      background: var(--table-header-bg);
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
      line-height: 1.5;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:nth-child(even) td {
      background-color: var(--table-row-alt);
    }

    /* Mistake Cards (Error & Fix) */
    .mistake-card {
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      margin: 20px 0;
      overflow: hidden;
      background: #FFFFFF;
      box-shadow: var(--card-shadow);
    }

    .mistake-header {
      background: #FEF2F2;
      border-bottom: 1px solid #FECACA;
      padding: 12px 18px;
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 700;
      color: #DC2626;
      font-size: 14px;
    }

    .mistake-body {
      padding: 16px 18px;
    }

    .mistake-error {
      background: #FFF1F2;
      border-left: 3px solid #E11D48;
      padding: 10px 14px;
      margin-bottom: 12px;
      border-radius: 0 6px 6px 0;
      font-size: 13px;
      color: #9F1239;
    }

    .mistake-fix {
      background: #F0FDF4;
      border-left: 3px solid #16A34A;
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      font-size: 13px;
      color: #14532D;
    }

    /* Interactive Accordions */
    .accordion-item {
      border: 1px solid var(--card-border);
      border-radius: 8px;
      margin-bottom: 12px;
      background: #FFFFFF;
      overflow: hidden;
      transition: border-color 0.15s ease;
    }

    .accordion-item[open] {
      border-color: var(--toc-border);
    }

    .accordion-summary {
      padding: 14px 18px;
      font-size: 15px;
      font-weight: 700;
      color: var(--heading-color);
      cursor: pointer;
      background: #FAFAFA;
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
    }

    .accordion-summary:hover {
      background: var(--primary-accent-light);
      color: var(--primary-accent);
    }

    .accordion-content {
      padding: 16px 18px;
      font-size: 14px;
      color: var(--text-secondary);
      line-height: 1.6;
      border-top: 1px solid var(--card-border);
      background: #FFFFFF;
    }

    /* Footer */
    .notes-footer {
      text-align: center;
      padding: 30px 20px;
      margin-top: 40px;
      border-top: 1px solid var(--card-border);
      font-size: 13px;
      color: var(--text-muted);
    }

    /* Responsive Queries */
    @media (max-width: 768px) {
      .container {
        padding: 16px 12px 60px 12px;
      }

      .hero-header {
        padding: 24px 18px;
      }

      .hero-title {
        font-size: 24px;
      }

      .hero-desc {
        font-size: 15px;
      }

      .content-section {
        padding: 20px 16px;
        margin-bottom: 24px;
        border-radius: 10px;
      }

      .section-title {
        font-size: 20px;
      }

      .toc-card {
        padding: 18px 14px;
      }

      .toc-grid {
        grid-template-columns: 1fr;
      }

      .code-body {
        font-size: 12px;
        padding: 12px;
      }

      .table-wrapper {
        margin: 14px 0;
      }

      th, td {
        padding: 9px 11px;
        font-size: 12px;
      }
    }
"""
