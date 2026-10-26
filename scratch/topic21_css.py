# Topic 21 CSS Stylesheet
# Strict Light Mode Only, Rose & Vibrant Crimson / Electric Coral & Slate Theme
# Fully responsive, accessible contrast, scoped scrollable tables and code blocks.

TOPIC21_CSS = """
    :root {
      --primary-accent: #E11D48;
      --primary-accent-hover: #BE123C;
      --primary-accent-light: #FFF1F2;
      --primary-badge-bg: #FFE4E6;
      --primary-badge-text: #9F1239;
      --border-color: #FECDD3;
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
      background: linear-gradient(135deg, #FFFFFF 0%, #FFF1F2 100%);
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
      border: 1px solid #FDA4AF;
    }

    .hero-title {
      font-size: 32px;
      font-weight: 800;
      color: #0F172A;
      line-height: 1.25;
      margin-bottom: 14px;
      letter-spacing: -0.02em;
    }

    .hero-subtitle {
      font-size: 16px;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 24px;
    }

    .hero-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      border-top: 1px solid #FFE4E6;
      padding-top: 20px;
    }

    .hero-meta-item {
      display: flex;
      flex-direction: column;
    }

    .hero-meta-label {
      font-size: 11px;
      text-transform: uppercase;
      font-weight: 700;
      color: #9F1239;
      letter-spacing: 0.04em;
    }

    .hero-meta-val {
      font-size: 14px;
      font-weight: 600;
      color: #1E293B;
      margin-top: 2px;
    }

    /* TOC */
    .toc-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      padding: 24px 28px;
      margin-bottom: 40px;
      box-shadow: var(--shadow-sm);
    }

    .toc-title {
      font-size: 16px;
      font-weight: 800;
      color: #0F172A;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .toc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 10px 16px;
      list-style: none;
    }

    .toc-link {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 13.5px;
      color: #334155;
      text-decoration: none;
      font-weight: 500;
      padding: 4px 6px;
      border-radius: var(--radius-sm);
      transition: all 0.15s ease;
    }

    .toc-link:hover {
      color: var(--primary-accent);
      background-color: var(--primary-accent-light);
    }

    .toc-num {
      display: inline-block;
      width: 20px;
      font-weight: 700;
      font-size: 11px;
      color: var(--primary-accent);
    }

    /* SECTIONS */
    .content-section {
      background: var(--bg-card);
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-lg);
      padding: 36px 32px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-sm);
      position: relative;
    }

    .section-tag {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      color: var(--primary-accent);
      background: var(--primary-accent-light);
      padding: 3px 8px;
      border-radius: 4px;
      margin-bottom: 8px;
      border: 1px solid var(--border-color);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .section-title {
      font-size: 24px;
      font-weight: 800;
      color: #0F172A;
      margin-bottom: 14px;
      letter-spacing: -0.015em;
    }

    .section-intro {
      font-size: 15.5px;
      color: var(--text-muted);
      margin-bottom: 24px;
      line-height: 1.6;
    }

    h3 {
      font-size: 18px;
      font-weight: 750;
      color: #1E293B;
      margin: 28px 0 12px 0;
    }

    p {
      margin-bottom: 16px;
      font-size: 14.5px;
      line-height: 1.65;
      color: #334155;
    }

    ul, ol {
      margin: 0 0 20px 24px;
      font-size: 14.5px;
      color: #334155;
    }

    li {
      margin-bottom: 8px;
      line-height: 1.6;
    }

    /* CARDS */
    .card {
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin: 20px 0;
      border: 1px solid #E2E8F0;
      background: #FFFFFF;
    }

    .card-def {
      background: #FFF1F2;
      border-color: #FECDD3;
      border-left: 4px solid var(--primary-accent);
    }

    .card-warn {
      background: #FFFBEB;
      border-color: #FDE68A;
      border-left: 4px solid #D97706;
    }

    .card-analogy {
      background: #F8FAFC;
      border-color: #CBD5E1;
      border-left: 4px solid #0284C7;
    }

    .card-strategy {
      background: #FDF4FF;
      border-color: #F5D0FE;
      border-left: 4px solid #A855F7;
    }

    .card-title {
      font-size: 15px;
      font-weight: 800;
      color: #0F172A;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .grid-2col {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin: 20px 0;
    }

    .grid-3col {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin: 20px 0;
    }

    /* MATH BOX */
    .math-box {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      padding: 16px 20px;
      margin: 16px 0;
      text-align: center;
      font-family: "SF Pro Text", -apple-system, sans-serif;
      font-size: 15.5px;
      font-weight: 600;
      color: #0F172A;
      box-shadow: inset 0 1px 2px rgba(0,0,0,0.02);
    }

    /* VISUAL CONTAINER */
    .visual-wrapper {
      margin: 28px 0;
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      padding: 18px;
      box-shadow: var(--shadow-sm);
    }

    .visual-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid #F1F5F9;
    }

    .visual-title {
      font-size: 13px;
      font-weight: 750;
      color: #1E293B;
      letter-spacing: -0.01em;
    }

    .visual-tag {
      font-size: 11px;
      font-weight: 600;
      color: var(--primary-accent);
      background: var(--primary-accent-light);
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid var(--border-color);
    }

    .visual-caption {
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.5;
      margin-top: 10px;
      padding-top: 8px;
      border-top: 1px dashed #E2E8F0;
      font-style: italic;
    }

    /* TABLES */
    .table-container {
      width: 100%;
      overflow-x: auto;
      margin: 20px 0;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
      text-align: left;
      background: #FFFFFF;
      min-width: 580px;
    }

    th {
      background: #FFF1F2;
      color: #881337;
      font-weight: 750;
      padding: 12px 14px;
      border-bottom: 1px solid #FECDD3;
      white-space: nowrap;
    }

    td {
      padding: 12px 14px;
      border-bottom: 1px solid #F1F5F9;
      color: #334155;
      vertical-align: top;
      line-height: 1.55;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:hover td {
      background-color: #FFF5F5;
    }

    /* CODE BLOCKS */
    .code-block-wrapper {
      margin: 20px 0;
      border: 1px solid var(--code-border);
      border-radius: var(--radius-md);
      background: var(--code-bg);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }

    .code-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 14px;
      background: #E2E8F0;
      border-bottom: 1px solid #CBD5E1;
      font-size: 12px;
      color: #475569;
      font-weight: 600;
    }

    .code-lang {
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.05em;
      color: #0F172A;
      font-weight: 700;
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
      font-family: inherit;
    }

    p code, li code, td code {
      background: #F1F5F9;
      color: #9F1239;
      padding: 2px 5px;
      border-radius: 4px;
      font-size: 0.9em;
      border: 1px solid #E2E8F0;
    }

    /* INTERACTIVE REGULARIZATION EXPLORER */
    .reg-explorer {
      background: #FFFFFF;
      border: 1px solid #FECDD3;
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin: 24px 0;
      box-shadow: var(--shadow-sm);
    }

    .reg-controls {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
    }

    .reg-btn-group {
      display: inline-flex;
      background: #F1F5F9;
      padding: 3px;
      border-radius: 8px;
      border: 1px solid #E2E8F0;
    }

    .reg-btn {
      padding: 6px 14px;
      font-size: 13px;
      font-weight: 700;
      border: none;
      background: transparent;
      color: #475569;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .reg-btn.active {
      background: #E11D48;
      color: #FFFFFF;
      box-shadow: var(--shadow-sm);
    }

    .reg-metrics {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }

    .reg-metric-box {
      background: #FFF1F2;
      border: 1px solid #FECDD3;
      padding: 12px 14px;
      border-radius: 8px;
    }

    .reg-metric-title {
      font-size: 11px;
      text-transform: uppercase;
      font-weight: 700;
      color: #9F1239;
      margin-bottom: 4px;
    }

    .reg-metric-val {
      font-size: 15px;
      font-weight: 800;
      color: #0F172A;
    }

    /* 15 MISTAKE CARDS */
    .mistake-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin: 24px 0;
    }

    .mistake-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      padding: 18px 20px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .mistake-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 10px;
    }

    .mistake-num {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 26px;
      height: 26px;
      background: #FFE4E6;
      color: #E11D48;
      font-size: 12px;
      font-weight: 800;
      border-radius: 50%;
      flex-shrink: 0;
    }

    .mistake-title {
      font-size: 14px;
      font-weight: 750;
      color: #0F172A;
    }

    .mistake-body {
      font-size: 13px;
      line-height: 1.55;
    }

    .mistake-line.bad {
      color: #991B1B;
      background: #FEF2F2;
      padding: 6px 10px;
      border-radius: 4px;
      margin-bottom: 6px;
      border-left: 3px solid #EF4444;
    }

    .mistake-line.good {
      color: #065F46;
      background: #ECFDF5;
      padding: 6px 10px;
      border-radius: 4px;
      border-left: 3px solid #10B981;
    }

    /* FAQ ACCORDIONS */
    .faq-list {
      margin: 24px 0;
    }

    .faq-item {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      margin-bottom: 12px;
      overflow: hidden;
      transition: all 0.2s ease;
    }

    .faq-item[open] {
      border-color: #FECDD3;
      box-shadow: var(--shadow-sm);
    }

    .faq-question {
      padding: 16px 20px;
      font-size: 14.5px;
      font-weight: 700;
      color: #0F172A;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #FFFFFF;
      user-select: none;
    }

    .faq-question:hover {
      background: #FFF1F2;
      color: var(--primary-accent);
    }

    .faq-answer {
      padding: 16px 20px 20px 20px;
      border-top: 1px solid #F1F5F9;
      font-size: 14px;
      color: #334155;
      line-height: 1.65;
      background: #FAFAFA;
    }

    /* FOOTER NAV */
    .chapter-nav {
      display: flex;
      justify-content: space-between;
      gap: 16px;
      margin-top: 48px;
      padding-top: 24px;
      border-top: 1px solid #E2E8F0;
    }

    .chapter-nav-btn {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 14px 20px;
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: var(--radius-md);
      text-decoration: none;
      color: #0F172A;
      font-weight: 700;
      font-size: 14px;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
      flex: 1;
    }

    .chapter-nav-btn:hover {
      border-color: var(--primary-accent);
      background: var(--primary-accent-light);
      color: var(--primary-accent);
    }

    .chapter-nav-btn.prev {
      justify-content: flex-start;
    }

    .chapter-nav-btn.next {
      justify-content: flex-end;
      text-align: right;
    }

    .chapter-nav-sub {
      font-size: 11px;
      text-transform: uppercase;
      color: var(--text-muted);
      font-weight: 600;
      letter-spacing: 0.04em;
    }

    .chapter-nav-title {
      font-size: 14px;
      font-weight: 750;
      color: #0F172A;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 640px) {
      .page-container {
        padding: 16px 12px 60px 12px;
      }
      .hero-header {
        padding: 24px 18px;
      }
      .hero-title {
        font-size: 24px;
      }
      .content-section {
        padding: 24px 16px;
      }
      .section-title {
        font-size: 20px;
      }
      .toc-card {
        padding: 18px 16px;
      }
      .toc-grid {
        grid-template-columns: 1fr;
      }
      .chapter-nav {
        flex-direction: column;
      }
      .chapter-nav-btn.next {
        text-align: left;
        justify-content: flex-start;
      }
      table {
        min-width: 500px;
      }
    }
"""
