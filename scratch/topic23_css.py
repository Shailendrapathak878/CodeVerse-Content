# Topic 23 CSS Stylesheet
# Strict Light Mode Only, Teal & Cyan / Deep Emerald Theme
# Fully responsive, accessible contrast, scoped scrollable tables, and code blocks.

TOPIC23_CSS = """
    :root {
      --primary-accent: #0D9488;
      --primary-accent-hover: #0F766E;
      --primary-accent-light: #F0FDFA;
      --primary-badge-bg: #CCFBF1;
      --primary-badge-text: #115E59;
      --border-color: #99F6E4;
      --text-main: #0F172A;
      --text-muted: #475569;
      --bg-card: #FFFFFF;
      --bg-page: #F8FAFC;
      --code-bg: #F1F5F9;
      --code-border: #E2E8F0;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.65;
      color: var(--text-main);
      background-color: var(--bg-page);
      -webkit-font-smoothing: antialiased;
      padding: 0;
      margin: 0;
    }

    .page-container {
      max-width: 980px;
      margin: 0 auto;
      padding: 32px 20px 80px 20px;
    }

    /* HERO HEADER */
    .hero-header {
      background: linear-gradient(135deg, #FFFFFF 0%, #F0FDFA 100%);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 36px 32px;
      margin-bottom: 32px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: var(--primary-badge-bg);
      color: var(--primary-badge-text);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      padding: 5px 12px;
      border-radius: 9999px;
      margin-bottom: 16px;
    }

    .hero-title {
      font-size: 32px;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.25;
      margin-bottom: 12px;
    }

    .hero-subtitle {
      font-size: 16px;
      color: var(--text-muted);
      max-width: 820px;
      line-height: 1.6;
      margin-bottom: 24px;
    }

    .hero-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-top: 16px;
      padding-top: 20px;
      border-top: 1px solid #E2E8F0;
    }

    .hero-meta-item {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .hero-meta-label {
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      color: #64748B;
      letter-spacing: 0.04em;
    }

    .hero-meta-val {
      font-size: 14px;
      font-weight: 600;
      color: var(--text-main);
    }

    /* TABLE OF CONTENTS */
    .toc-card {
      background: var(--bg-card);
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      padding: 24px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-sm);
    }

    .toc-title {
      font-size: 17px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .toc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 8px 16px;
      list-style: none;
      padding: 0;
      margin: 0;
    }

    .toc-link {
      color: #334155;
      text-decoration: none;
      font-size: 13.5px;
      display: flex;
      align-items: baseline;
      gap: 8px;
      padding: 4px 6px;
      border-radius: var(--radius-sm);
      transition: background 0.15s ease, color 0.15s ease;
    }

    .toc-link:hover {
      background: var(--primary-accent-light);
      color: var(--primary-accent-hover);
    }

    .toc-num {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 11px;
      font-weight: 700;
      color: var(--primary-accent);
      min-width: 22px;
    }

    /* SECTION CONTAINERS */
    .section-card {
      background: var(--bg-card);
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-lg);
      padding: 32px;
      margin-bottom: 32px;
      box-shadow: var(--shadow-sm);
    }

    .section-header {
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid #F1F5F9;
    }

    .section-tag {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--primary-accent);
      margin-bottom: 6px;
      display: block;
    }

    .section-title {
      font-size: 22px;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.35;
    }

    .section-title a {
      color: inherit;
      text-decoration: none;
    }

    .section-title a:hover {
      color: var(--primary-accent);
    }

    h3 {
      font-size: 17px;
      font-weight: 700;
      color: var(--text-main);
      margin: 24px 0 10px 0;
    }

    h4 {
      font-size: 15px;
      font-weight: 600;
      color: #1E293B;
      margin: 18px 0 8px 0;
    }

    p {
      margin-bottom: 14px;
      color: #334155;
      font-size: 14.5px;
      line-height: 1.7;
    }

    ul, ol {
      margin: 0 0 16px 24px;
      color: #334155;
      font-size: 14.5px;
      line-height: 1.7;
    }

    li {
      margin-bottom: 6px;
    }

    /* SVG DIAGRAMS */
    .diagram-container {
      margin: 24px 0;
      padding: 16px;
      background: #FAFAFA;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      text-align: center;
      overflow: hidden;
    }

    .diagram-container svg {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    .diagram-caption {
      font-size: 12.5px;
      color: #64748B;
      margin-top: 10px;
      text-align: center;
      line-height: 1.5;
    }

    /* CODE BLOCKS */
    .code-container {
      margin: 20px 0;
      border: 1px solid var(--code-border);
      border-radius: var(--radius-md);
      overflow: hidden;
      background: var(--code-bg);
    }

    .code-header {
      background: #E2E8F0;
      padding: 8px 16px;
      font-size: 12px;
      font-weight: 600;
      color: #475569;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #CBD5E1;
    }

    .code-lang {
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-size: 10.5px;
      color: #0F766E;
    }

    pre {
      margin: 0;
      padding: 16px;
      overflow-x: auto;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 13px;
      line-height: 1.6;
      color: #0F172A;
      background: #F8FAFC;
    }

    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.9em;
      background-color: #F1F5F9;
      color: #0F766E;
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid #E2E8F0;
    }

    pre code {
      background: transparent;
      padding: 0;
      border: none;
      color: inherit;
    }

    /* TABLES */
    .table-responsive {
      overflow-x: auto;
      margin: 20px 0;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13.5px;
      background: #FFFFFF;
    }

    th {
      background: #F1F5F9;
      color: #0F172A;
      font-weight: 700;
      padding: 12px 14px;
      border-bottom: 2px solid #CBD5E1;
      white-space: nowrap;
    }

    td {
      padding: 10px 14px;
      border-bottom: 1px solid #E2E8F0;
      color: #334155;
      vertical-align: top;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:nth-child(even) td {
      background-color: #F8FAFC;
    }

    /* CALLOUT BOXES */
    .callout {
      padding: 16px 20px;
      border-radius: var(--radius-md);
      margin: 20px 0;
      border-left: 4px solid;
      font-size: 14px;
      line-height: 1.6;
    }

    .callout-title {
      font-weight: 700;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 14px;
    }

    .callout-tip {
      background-color: #F0FDF4;
      border-color: #22C55E;
      color: #14532D;
    }

    .callout-tip .callout-title {
      color: #15803D;
    }

    .callout-important {
      background-color: #F0FDFA;
      border-color: var(--primary-accent);
      color: #115E59;
    }

    .callout-important .callout-title {
      color: #0F766E;
    }

    .callout-warning {
      background-color: #FFFBEB;
      border-color: #F59E0B;
      color: #78350F;
    }

    .callout-warning .callout-title {
      color: #B45309;
    }

    .callout-caution {
      background-color: #FEF2F2;
      border-color: #EF4444;
      color: #7F1D1D;
    }

    .callout-caution .callout-title {
      color: #B91C1C;
    }

    .callout-note {
      background-color: #F8FAFC;
      border-color: #64748B;
      color: #1E293B;
    }

    .callout-note .callout-title {
      color: #334155;
    }

    /* FORMULA DISPLAY */
    .formula-card {
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      margin: 18px 0;
      text-align: center;
      box-shadow: var(--shadow-sm);
    }

    .formula-math {
      font-size: 16px;
      font-weight: 600;
      color: #0F766E;
      margin-bottom: 6px;
      font-family: "Cambria Math", "Times New Roman", serif;
    }

    .formula-desc {
      font-size: 12.5px;
      color: #64748B;
    }

    /* METRIC CARDS GRID */
    .metric-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 14px;
      margin: 20px 0;
    }

    .metric-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      padding: 16px;
      box-shadow: var(--shadow-sm);
      border-top: 3px solid var(--primary-accent);
    }

    .metric-label {
      font-size: 12px;
      font-weight: 600;
      color: #64748B;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .metric-val {
      font-size: 24px;
      font-weight: 800;
      color: var(--text-main);
      margin: 6px 0;
      font-family: ui-monospace, monospace;
    }

    .metric-sub {
      font-size: 12px;
      color: #0F766E;
    }

    /* ACCORDION (DETAILS) */
    details.faq-item {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      margin-bottom: 12px;
      overflow: hidden;
      transition: border-color 0.15s ease;
    }

    details.faq-item:hover {
      border-color: var(--border-color);
    }

    details.faq-item[open] {
      border-color: var(--primary-accent);
      box-shadow: var(--shadow-sm);
    }

    summary.faq-summary {
      padding: 14px 18px;
      font-weight: 700;
      font-size: 14.5px;
      color: var(--text-main);
      cursor: pointer;
      list-style: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
      background: #F8FAFC;
    }

    summary.faq-summary::-webkit-details-marker {
      display: none;
    }

    summary.faq-summary::after {
      content: "+";
      font-size: 18px;
      font-weight: 600;
      color: var(--primary-accent);
      transition: transform 0.2s ease;
    }

    details.faq-item[open] summary.faq-summary::after {
      content: "−";
      transform: rotate(180deg);
    }

    .faq-answer {
      padding: 16px 18px;
      border-top: 1px solid #E2E8F0;
      font-size: 14px;
      line-height: 1.65;
      color: #334155;
      background: #FFFFFF;
    }

    /* INTERACTIVE CALCULATOR */
    .calc-card {
      background: #F0FDFA;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin: 24px 0;
    }

    .calc-title {
      font-size: 18px;
      font-weight: 800;
      color: #115E59;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .calc-desc {
      font-size: 13.5px;
      color: #334155;
      margin-bottom: 18px;
    }

    .calc-form-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 18px;
    }

    .calc-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .calc-label {
      font-size: 12px;
      font-weight: 600;
      color: #1E293B;
    }

    .calc-input {
      padding: 8px 12px;
      border: 1px solid #CBD5E1;
      border-radius: var(--radius-sm);
      font-size: 14px;
      background: #FFFFFF;
      color: var(--text-main);
    }

    .calc-input:focus {
      outline: 2px solid var(--primary-accent);
      border-color: transparent;
    }

    .calc-results-box {
      background: #FFFFFF;
      border: 1px solid #CCFBF1;
      border-radius: var(--radius-md);
      padding: 18px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
    }

    .calc-res-item {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .calc-res-label {
      font-size: 11.5px;
      font-weight: 600;
      color: #64748B;
      text-transform: uppercase;
    }

    .calc-res-val {
      font-size: 20px;
      font-weight: 800;
      color: #0F766E;
      font-family: ui-monospace, monospace;
    }

    /* FOOTER */
    .page-footer {
      text-align: center;
      padding: 40px 0 20px 0;
      border-top: 1px solid #E2E8F0;
      color: #64748B;
      font-size: 13px;
    }

    .page-footer a {
      color: var(--primary-accent);
      text-decoration: none;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 768px) {
      .page-container {
        padding: 16px 12px 60px 12px;
      }
      .hero-header {
        padding: 24px 18px;
      }
      .hero-title {
        font-size: 24px;
      }
      .hero-subtitle {
        font-size: 14px;
      }
      .section-card {
        padding: 20px 14px;
        margin-bottom: 24px;
      }
      .section-title {
        font-size: 19px;
      }
      .toc-grid {
        grid-template-columns: 1fr;
      }
      pre {
        padding: 12px;
        font-size: 12px;
      }
      .calc-card {
        padding: 16px 12px;
      }
    }
"""
