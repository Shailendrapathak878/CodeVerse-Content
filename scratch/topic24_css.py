# Topic 24 CSS Stylesheet — Modern Light Mode Design System
# Electric Blue (#2563EB) & Modern Navy (#1E40AF)
# Strictly Light Mode Only. Fully responsive, zero horizontal overflow.

TOPIC24_CSS = """
    :root {
      --primary-accent: #2563EB;
      --primary-hover: #1D4ED8;
      --primary-light: #EFF6FF;
      --secondary-accent: #0284C7;
      --navy-deep: #1E3A8A;
      --bg-page: #F8FAFC;
      --bg-card: #FFFFFF;
      --bg-subtle: #F1F5F9;
      --text-main: #0F172A;
      --text-muted: #475569;
      --text-light: #64748B;
      --border-color: #E2E8F0;
      --border-accent: #BFDBFE;
      --code-bg: #F8FAFC;
      --code-border: #E2E8F0;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
    }

    * {
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.65;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    .page-container {
      max-width: 1000px;
      margin: 0 auto;
      padding: 32px 20px 80px 20px;
      box-sizing: border-box;
      overflow-x: hidden;
    }

    /* HERO HEADER */
    .hero-header {
      background: linear-gradient(135deg, #FFFFFF 0%, #EFF6FF 100%);
      border: 1px solid var(--border-accent);
      border-radius: var(--radius-lg);
      padding: 40px 32px;
      margin-bottom: 32px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
    }

    .hero-header::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 6px;
      height: 100%;
      background: linear-gradient(180deg, var(--primary-accent), var(--secondary-accent));
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #DBEAFE;
      color: #1E40AF;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 12px;
      border-radius: 9999px;
      margin-bottom: 12px;
    }

    .hero-title {
      font-size: 32px;
      font-weight: 800;
      color: var(--navy-deep);
      line-height: 1.25;
      margin: 0 0 12px 0;
      letter-spacing: -0.02em;
    }

    .hero-subtitle {
      font-size: 16px;
      color: var(--text-muted);
      margin: 0 0 24px 0;
      line-height: 1.6;
      max-width: 800px;
    }

    .hero-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
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
      background: #EFF6FF;
      color: var(--primary-accent);
    }

    .toc-num {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 11px;
      font-weight: 700;
      color: #3B82F6;
      background: #EFF6FF;
      padding: 2px 5px;
      border-radius: 4px;
    }

    /* SECTION CARDS */
    .section-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 36px 32px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-sm);
    }

    .section-header {
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 1px solid #F1F5F9;
    }

    .section-tag {
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--primary-accent);
      margin-bottom: 4px;
      display: inline-block;
    }

    .section-title {
      font-size: 24px;
      font-weight: 800;
      color: #0F172A;
      margin: 0;
      letter-spacing: -0.015em;
    }

    .section-title a {
      color: inherit;
      text-decoration: none;
    }

    .section-title a:hover {
      color: var(--primary-accent);
    }

    h3 {
      font-size: 18px;
      font-weight: 700;
      color: #1E293B;
      margin: 28px 0 12px 0;
      letter-spacing: -0.01em;
    }

    h4 {
      font-size: 15px;
      font-weight: 700;
      color: #334155;
      margin: 20px 0 8px 0;
    }

    p {
      margin: 0 0 14px 0;
      color: #334155;
      font-size: 15px;
      line-height: 1.7;
    }

    ul, ol {
      margin: 0 0 16px 0;
      padding-left: 24px;
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
      max-width: 100%;
      overflow-x: auto;
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
    pre {
      margin: 16px 0;
      padding: 16px;
      max-width: 100%;
      overflow-x: auto;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 13px;
      line-height: 1.6;
      color: #0F172A;
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      box-sizing: border-box;
      word-break: normal;
      word-wrap: normal;
    }

    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.9em;
      background-color: #F1F5F9;
      color: #1D4ED8;
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

    /* TABLES & CONTAINERS (PREVENT MOBILE OVERFLOW) */
    .table-container,
    .table-responsive {
      width: 100%;
      max-width: 100%;
      overflow-x: auto;
      margin: 20px 0;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      -webkit-overflow-scrolling: touch;
      background: #FFFFFF;
    }

    table, .data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13.5px;
      background: #FFFFFF;
      min-width: 500px;
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
    .callout-tip .callout-title { color: #15803D; }

    .callout-important {
      background-color: #EFF6FF;
      border-color: #3B82F6;
      color: #1E3A8A;
    }
    .callout-important .callout-title { color: #1D4ED8; }

    .callout-warning {
      background-color: #FFFBEB;
      border-color: #F59E0B;
      color: #78350F;
    }
    .callout-warning .callout-title { color: #B45309; }

    .callout-danger {
      background-color: #FEF2F2;
      border-color: #EF4444;
      color: #7F1D1D;
    }
    .callout-danger .callout-title { color: #B91C1C; }

    /* BADGES */
    .badge {
      display: inline-block;
      padding: 3px 8px;
      font-size: 11px;
      font-weight: 700;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .badge-success { background: #DCFCE7; color: #166534; border: 1px solid #86EFAC; }
    .badge-warning { background: #FEF3C7; color: #92400E; border: 1px solid #FCD34D; }
    .badge-info { background: #DBEAFE; color: #1E40AF; border: 1px solid #93C5FD; }

    /* INTERACTIVE ACCORDIONS */
    .interactive-accordion {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      margin-bottom: 12px;
      overflow: hidden;
      transition: border-color 0.15s ease;
    }

    .interactive-accordion:hover {
      border-color: #93C5FD;
    }

    .interactive-accordion[open] {
      border-color: #60A5FA;
      box-shadow: var(--shadow-sm);
    }

    .accordion-header {
      padding: 14px 18px;
      font-weight: 600;
      font-size: 14.5px;
      color: #1E293B;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #F8FAFC;
      user-select: none;
    }

    .accordion-header:hover {
      background: #EFF6FF;
      color: var(--primary-accent);
    }

    .accordion-icon {
      font-size: 16px;
      font-weight: 700;
      color: #64748B;
      transition: transform 0.2s ease;
    }

    .interactive-accordion[open] .accordion-icon {
      transform: rotate(45deg);
      color: var(--primary-accent);
    }

    .accordion-body {
      padding: 16px 18px;
      border-top: 1px solid #E2E8F0;
      background: #FFFFFF;
      font-size: 14px;
      color: #334155;
      line-height: 1.65;
    }

    /* INTERACTIVE CALCULATOR */
    .calculator-card {
      background: #F0F9FF;
      border: 1.5px solid #BAE6FD;
      border-radius: var(--radius-md);
      padding: 24px;
      margin: 24px 0;
      box-shadow: var(--shadow-sm);
    }

    .calc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-bottom: 20px;
    }

    .calc-input-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .calc-label {
      font-size: 13px;
      font-weight: 600;
      color: #0F172A;
    }

    .calc-input-group input[type="range"] {
      width: 100%;
      accent-color: #2563EB;
      cursor: pointer;
    }

    .calc-val-display {
      font-size: 12px;
      font-weight: 700;
      color: #2563EB;
      font-family: ui-monospace, monospace;
    }

    .calc-results-box {
      background: #FFFFFF;
      border: 1px solid #BAE6FD;
      border-radius: var(--radius-sm);
      padding: 16px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 14px;
    }

    .calc-result-item {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .calc-result-label {
      font-size: 11px;
      font-weight: 700;
      color: #64748B;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .calc-result-num {
      font-size: 17px;
      font-weight: 800;
      color: #1D4ED8;
      font-family: ui-monospace, monospace;
    }

    /* COMPLETION & PROJECT BANNER */
    .banner-section {
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      padding: 0 !important;
      margin: 40px 0 20px 0 !important;
    }

    .completion-banner {
      background: linear-gradient(135deg, #FFFFFF 0%, #F0F9FF 50%, #E0F2FE 100%);
      border: 2px solid #38BDF8;
      border-radius: var(--radius-lg);
      padding: 36px 28px;
      box-shadow: 0 10px 25px -5px rgba(14, 165, 233, 0.15), 0 8px 10px -6px rgba(14, 165, 233, 0.1);
    }

    .banner-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #FEF3C7;
      color: #92400E;
      border: 1px solid #FCD34D;
      font-size: 11.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 6px 14px;
      border-radius: 9999px;
      margin-bottom: 16px;
    }

    .banner-title {
      font-size: 26px;
      font-weight: 900;
      color: #0F172A;
      line-height: 1.3;
      margin: 0 0 12px 0;
    }

    .banner-message {
      font-size: 15px;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 24px;
    }

    .project-challenge-card {
      background: #FFFFFF;
      border: 1px solid #BAE6FD;
      border-radius: var(--radius-md);
      padding: 24px;
      margin-top: 24px;
    }

    .challenge-title {
      font-size: 18px;
      font-weight: 800;
      color: #0369A1;
      margin: 0 0 10px 0;
    }

    .challenge-desc {
      font-size: 14px;
      color: #334155;
      line-height: 1.6;
      margin-bottom: 20px;
    }

    .roadmap-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(115px, 1fr));
      gap: 10px;
      margin-bottom: 24px;
    }

    .roadmap-step {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-sm);
      padding: 12px 8px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      transition: transform 0.15s ease, border-color 0.15s ease;
    }

    .roadmap-step:hover {
      transform: translateY(-2px);
      border-color: #38BDF8;
      background: #F0F9FF;
    }

    .step-num {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: #2563EB;
      color: #FFFFFF;
      font-size: 12px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 4px;
    }

    .step-name {
      font-size: 13px;
      font-weight: 700;
      color: #0F172A;
    }

    .step-desc {
      font-size: 11px;
      color: #64748B;
      line-height: 1.4;
    }

    .criteria-box {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-sm);
      padding: 16px 20px;
      margin-bottom: 24px;
    }

    .criteria-box h4 {
      font-size: 14px;
      font-weight: 700;
      color: #1E293B;
      margin: 0 0 12px 0;
    }

    .criteria-list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 8px 16px;
    }

    .criteria-item {
      font-size: 13px;
      color: #334155;
      display: flex;
      align-items: baseline;
      gap: 6px;
    }

    .banner-cta-container {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 10px;
    }

    .btn-primary {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: #2563EB;
      color: #FFFFFF;
      font-size: 14px;
      font-weight: 700;
      padding: 10px 20px;
      border-radius: var(--radius-sm);
      text-decoration: none;
      transition: background 0.15s ease;
    }

    .btn-primary:hover {
      background: #1D4ED8;
    }

    .btn-secondary {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: #FFFFFF;
      color: #2563EB;
      border: 1px solid #BFDBFE;
      font-size: 14px;
      font-weight: 700;
      padding: 10px 20px;
      border-radius: var(--radius-sm);
      text-decoration: none;
      transition: background 0.15s ease, border-color 0.15s ease;
    }

    .btn-secondary:hover {
      background: #EFF6FF;
      border-color: #93C5FD;
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
      .calc-grid {
        grid-template-columns: 1fr;
      }
      .calc-results-box {
        grid-template-columns: 1fr;
      }
      .completion-banner {
        padding: 24px 16px;
      }
      .banner-title {
        font-size: 21px;
      }
      .roadmap-grid {
        grid-template-columns: 1fr;
      }
      .criteria-list {
        grid-template-columns: 1fr;
      }
      .banner-cta-container {
        flex-direction: column;
      }
      .btn-primary, .btn-secondary {
        width: 100%;
        text-align: center;
      }
    }
"""
