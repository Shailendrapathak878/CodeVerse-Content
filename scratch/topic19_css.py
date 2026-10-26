# Topic 19 CSS Stylesheet - Strict Light Mode Only

TOPIC19_CSS = """
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
      
      /* Topic 19 Theme: Vibrant Indigo & Deep Violet */
      --primary-accent: #4F46E5;
      --primary-accent-hover: #4338CA;
      --primary-accent-light: #EEF2FF;
      --primary-badge-bg: #E0E7FF;
      --primary-badge-text: #4338CA;
      --toc-bg: #F8FAFC;
      --toc-border: #C7D2FE;
      --toc-text: #4338CA;

      /* Definition Card (Soft Indigo) */
      --def-card-bg: #EEF2FF;
      --def-card-border: #C7D2FE;
      --def-card-title: #4338CA;
      --def-card-text: #312E81;

      /* Analogy Card (Soft Amber / Warm Honey) */
      --analogy-card-bg: #FFFBEB;
      --analogy-card-border: #FDE68A;
      --analogy-card-title: #D97706;
      --analogy-card-text: #78350F;

      /* Success / Precision Card (Soft Emerald) */
      --success-card-bg: #F0FDF4;
      --success-card-border: #BBF7D0;
      --success-card-title: #15803D;
      --success-card-text: #14532D;

      /* Info Card (Soft Sky Blue) */
      --info-card-bg: #F0F9FF;
      --info-card-border: #BAE6FD;
      --info-card-title: #0284C7;
      --info-card-text: #0C4A6E;

      /* Warning / Pitfall Card (Soft Coral / Red) */
      --warn-card-bg: #FEF2F2;
      --warn-card-border: #FECACA;
      --warn-card-title: #DC2626;
      --warn-card-text: #7F1D1D;

      /* Purple Card (Regression / Highlight) */
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
      border: 1px solid #C7D2FE;
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
      margin-bottom: 18px;
    }

    .hero-title {
      font-size: 2.5rem;
      font-weight: 800;
      color: var(--heading-color);
      letter-spacing: -0.03em;
      line-height: 1.15;
      margin-bottom: 16px;
    }

    .hero-subtitle {
      font-size: 1.125rem;
      color: var(--text-secondary);
      line-height: 1.6;
      max-width: 820px;
      margin-bottom: 24px;
    }

    .hero-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      border-top: 1px solid #C7D2FE;
      padding-top: 20px;
    }

    .hero-meta-item {
      display: flex;
      flex-direction: column;
    }

    .hero-meta-label {
      font-size: 0.75rem;
      text-transform: uppercase;
      color: var(--text-muted);
      font-weight: 600;
      letter-spacing: 0.05em;
    }

    .hero-meta-val {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-primary);
      margin-top: 2px;
    }

    /* Table of Contents */
    .toc-card {
      background: var(--card-bg);
      border: 1px solid var(--toc-border);
      border-radius: 14px;
      padding: 24px 28px;
      margin-bottom: 40px;
      box-shadow: var(--card-shadow);
      width: 100%;
    }

    .toc-title {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--toc-text);
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
    }

    .toc-link {
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--text-secondary);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 500;
      padding: 6px 8px;
      border-radius: 6px;
      transition: all 0.15s ease;
    }

    .toc-link:hover {
      background: var(--primary-accent-light);
      color: var(--primary-accent);
      transform: translateX(4px);
    }

    .toc-num {
      display: inline-block;
      width: 24px;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--primary-accent);
    }

    /* Sections */
    .content-section {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 36px 32px;
      margin-bottom: 36px;
      box-shadow: var(--card-shadow);
      width: 100%;
      overflow-x: hidden;
    }

    .section-tag {
      display: inline-block;
      background: var(--primary-badge-bg);
      color: var(--primary-badge-text);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 12px;
      margin-bottom: 12px;
    }

    .section-title {
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--heading-color);
      letter-spacing: -0.02em;
      line-height: 1.25;
      margin-bottom: 16px;
    }

    .section-intro {
      font-size: 1.05rem;
      color: var(--text-secondary);
      line-height: 1.7;
      margin-bottom: 24px;
    }

    h3 {
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--heading-color);
      margin: 28px 0 14px;
      letter-spacing: -0.01em;
    }

    h4 {
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--text-primary);
      margin: 20px 0 10px;
    }

    p {
      margin-bottom: 16px;
      color: var(--text-secondary);
      line-height: 1.7;
    }

    ul, ol {
      margin: 12px 0 20px 24px;
      color: var(--text-secondary);
    }

    li {
      margin-bottom: 8px;
      line-height: 1.6;
    }

    strong {
      color: var(--text-primary);
      font-weight: 700;
    }

    /* Cards */
    .card {
      border-radius: 10px;
      padding: 20px 24px;
      margin: 20px 0;
      line-height: 1.65;
      width: 100%;
    }

    .card-title {
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .card-def {
      background: var(--def-card-bg);
      border-left: 4px solid var(--def-card-title);
      color: var(--def-card-text);
    }
    .card-def .card-title { color: var(--def-card-title); }

    .card-analogy {
      background: var(--analogy-card-bg);
      border-left: 4px solid var(--analogy-card-title);
      color: var(--analogy-card-text);
    }
    .card-analogy .card-title { color: var(--analogy-card-title); }

    .card-success {
      background: var(--success-card-bg);
      border-left: 4px solid var(--success-card-title);
      color: var(--success-card-text);
    }
    .card-success .card-title { color: var(--success-card-title); }

    .card-info {
      background: var(--info-card-bg);
      border-left: 4px solid var(--info-card-title);
      color: var(--info-card-text);
    }
    .card-info .card-title { color: var(--info-card-title); }

    .card-warn {
      background: var(--warn-card-bg);
      border-left: 4px solid var(--warn-card-title);
      color: var(--warn-card-text);
    }
    .card-warn .card-title { color: var(--warn-card-title); }

    .card-purple {
      background: var(--purple-card-bg);
      border-left: 4px solid var(--purple-card-title);
      color: var(--purple-card-text);
    }
    .card-purple .card-title { color: var(--purple-card-title); }

    /* SVG Graphics Container */
    .visual-wrapper {
      background: #FFFFFF;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 20px;
      margin: 24px 0;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
      width: 100%;
      overflow-x: hidden;
    }

    .visual-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 1px solid #F1F5F9;
    }

    .visual-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-primary);
    }

    .visual-tag {
      font-size: 0.75rem;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 4px;
      background: #F1F5F9;
      color: #475569;
    }

    .visual-caption {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 12px;
      line-height: 1.5;
      font-style: italic;
      border-top: 1px dashed #E2E8F0;
      padding-top: 10px;
    }

    /* Math Formula Box */
    .math-box {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-left: 4px solid var(--primary-accent);
      border-radius: 8px;
      padding: 16px 20px;
      margin: 18px 0;
      text-align: center;
      font-family: "Georgia", "Cambria", serif;
      font-size: 1.15rem;
      color: #0F172A;
      box-shadow: inset 0 1px 3px rgba(15, 23, 42, 0.03);
      overflow-x: auto;
    }

    .math-legend {
      font-family: -apple-system, sans-serif;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 8px;
      text-align: left;
      line-height: 1.5;
    }

    /* Tables */
    .table-container {
      width: 100%;
      overflow-x: auto;
      margin: 20px 0;
      border-radius: 8px;
      border: 1px solid var(--table-border);
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02);
      -webkit-overflow-scrolling: touch;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }

    th {
      background: var(--table-header-bg);
      color: var(--text-primary);
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

    /* Code Blocks */
    .code-container {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      margin: 20px 0;
      overflow-x: auto;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
      width: 100%;
    }

    .code-header {
      background: #F1F5F9;
      padding: 8px 16px;
      border-bottom: 1px solid #E2E8F0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--text-muted);
    }

    pre {
      padding: 16px;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 0.88rem;
      line-height: 1.6;
      color: #0F172A;
      overflow-x: auto;
      background: #FFFFFF;
    }

    code {
      font-family: inherit;
    }

    p code, li code, td code {
      background: #F1F5F9;
      color: var(--primary-accent);
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.85em;
      font-weight: 600;
      font-family: "SFMono-Regular", Consolas, monospace;
    }

    /* Interactive Threshold Widget */
    .threshold-widget {
      background: #F8FAFC;
      border: 1px solid #C7D2FE;
      border-radius: 12px;
      padding: 24px;
      margin: 24px 0;
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.06);
    }

    .widget-controls {
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 20px;
    }

    .slider-row {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .slider-row input[type="range"] {
      flex: 1;
      height: 8px;
      border-radius: 4px;
      background: #E2E8F0;
      outline: none;
      -webkit-appearance: none;
    }

    .slider-row input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: #4F46E5;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(79, 70, 229, 0.4);
    }

    .threshold-val-badge {
      font-size: 1.15rem;
      font-weight: 800;
      color: #4F46E5;
      background: #EEF2FF;
      border: 1px solid #C7D2FE;
      padding: 6px 14px;
      border-radius: 8px;
      min-width: 72px;
      text-align: center;
    }

    .widget-metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 12px;
      margin-bottom: 20px;
    }

    .metric-pill {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      padding: 12px;
      text-align: center;
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
    }

    .metric-pill-label {
      font-size: 0.72rem;
      text-transform: uppercase;
      color: #64748B;
      font-weight: 700;
      letter-spacing: 0.05em;
    }

    .metric-pill-val {
      font-size: 1.35rem;
      font-weight: 800;
      color: #0F172A;
      margin-top: 4px;
    }

    /* Accordion FAQ */
    .faq-item {
      background: #FFFFFF;
      border: 1px solid var(--card-border);
      border-radius: 8px;
      margin-bottom: 12px;
      overflow: hidden;
      transition: all 0.15s ease;
    }

    .faq-item[open] {
      border-color: #C7D2FE;
      box-shadow: 0 2px 8px rgba(79, 70, 229, 0.06);
    }

    .faq-summary {
      padding: 16px 20px;
      font-weight: 700;
      color: var(--text-primary);
      cursor: pointer;
      list-style: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #F8FAFC;
    }

    .faq-summary::-webkit-details-marker {
      display: none;
    }

    .faq-summary::after {
      content: "+";
      font-size: 1.2rem;
      color: var(--primary-accent);
      font-weight: bold;
    }

    .faq-item[open] .faq-summary::after {
      content: "−";
    }

    .faq-content {
      padding: 18px 20px;
      border-top: 1px solid #F1F5F9;
      color: var(--text-secondary);
      line-height: 1.65;
    }

    /* Mistakes Grid */
    .mistake-card {
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 20px;
      margin-bottom: 18px;
      background: #FFFFFF;
      width: 100%;
    }

    .mistake-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: #DC2626;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .mistake-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-top: 12px;
    }

    .mistake-bad {
      background: #FEF2F2;
      border: 1px solid #FECACA;
      border-radius: 6px;
      padding: 12px 14px;
      font-size: 0.88rem;
    }

    .mistake-good {
      background: #F0FDF4;
      border: 1px solid #BBF7D0;
      border-radius: 6px;
      padding: 12px 14px;
      font-size: 0.88rem;
    }

    .mistake-bad-title {
      font-weight: 700;
      color: #991B1B;
      margin-bottom: 4px;
    }

    .mistake-good-title {
      font-weight: 700;
      color: #166534;
      margin-bottom: 4px;
    }

    /* Footer Nav */
    .chapter-nav {
      display: flex;
      justify-content: space-between;
      gap: 16px;
      margin-top: 48px;
      padding-top: 24px;
      border-top: 1px solid var(--card-border);
      width: 100%;
    }

    .nav-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #FFFFFF;
      border: 1px solid var(--card-border);
      padding: 12px 20px;
      border-radius: 8px;
      text-decoration: none;
      color: var(--text-primary);
      font-weight: 600;
      font-size: 0.9rem;
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);
      transition: all 0.15s ease;
    }

    .nav-btn:hover {
      border-color: var(--primary-accent);
      color: var(--primary-accent);
      background: var(--primary-accent-light);
    }

    /* Responsive */
    @media (max-width: 768px) {
      .container {
        padding: 20px 14px 60px;
      }
      .hero-header {
        padding: 28px 20px;
      }
      .hero-title {
        font-size: 1.85rem;
      }
      .content-section {
        padding: 24px 18px;
      }
      .section-title {
        font-size: 1.45rem;
      }
      .mistake-grid {
        grid-template-columns: 1fr;
      }
      .chapter-nav {
        flex-direction: column;
      }
      .widget-metrics-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
"""
