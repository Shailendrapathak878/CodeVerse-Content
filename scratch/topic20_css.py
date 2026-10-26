# Topic 20 CSS Stylesheet - Strict Light Mode Only (Deep Emerald & Royal Teal Theme)

TOPIC20_CSS = """
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
      
      /* Topic 20 Theme: Deep Emerald & Royal Teal */
      --primary-accent: #059669;
      --primary-accent-hover: #047857;
      --primary-accent-light: #ECFDF5;
      --primary-badge-bg: #D1FAE5;
      --primary-badge-text: #065F46;
      --toc-bg: #F8FAFC;
      --toc-border: #A7F3D0;
      --toc-text: #065F46;

      /* Definition Card (Soft Emerald) */
      --def-card-bg: #ECFDF5;
      --def-card-border: #A7F3D0;
      --def-card-title: #059669;
      --def-card-text: #064E3B;

      /* Training Card (Soft Sky Blue) */
      --train-card-bg: #F0F9FF;
      --train-card-border: #BAE6FD;
      --train-card-title: #0284C7;
      --train-card-text: #0C4A6E;

      /* Test Card (Soft Purple) */
      --test-card-bg: #FAF5FF;
      --test-card-border: #E9D5FF;
      --test-card-title: #7E22CE;
      --test-card-text: #581C87;

      /* Analogy Card (Soft Amber / Honey) */
      --analogy-card-bg: #FFFBEB;
      --analogy-card-border: #FDE68A;
      --analogy-card-title: #D97706;
      --analogy-card-text: #78350F;

      /* Warning / Leakage Card (Soft Coral / Red) */
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
      background: linear-gradient(135deg, #FFFFFF 0%, #ECFDF5 50%, #F0FDF4 100%);
      border: 1px solid #A7F3D0;
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
      border-top: 1px solid #A7F3D0;
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

    .card-train {
      background: var(--train-card-bg);
      border-left: 4px solid var(--train-card-title);
      color: var(--train-card-text);
    }
    .card-train .card-title { color: var(--train-card-title); }

    .card-test {
      background: var(--test-card-bg);
      border-left: 4px solid var(--test-card-title);
      color: var(--test-card-text);
    }
    .card-test .card-title { color: var(--test-card-title); }

    .card-analogy {
      background: var(--analogy-card-bg);
      border-left: 4px solid var(--analogy-card-title);
      color: var(--analogy-card-text);
    }
    .card-analogy .card-title { color: var(--analogy-card-title); }

    .card-warn {
      background: var(--warn-card-bg);
      border-left: 4px solid var(--warn-card-title);
      color: var(--warn-card-text);
    }
    .card-warn .card-title { color: var(--warn-card-title); }

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

    /* Interactive Fold Explorer Widget */
    .kfold-widget {
      background: #F8FAFC;
      border: 1px solid #A7F3D0;
      border-radius: 12px;
      padding: 24px;
      margin: 24px 0;
      box-shadow: 0 4px 12px rgba(5, 150, 105, 0.06);
    }

    .kfold-controls {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
    }

    .kfold-btn-group {
      display: flex;
      gap: 8px;
    }

    .kfold-btn {
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      padding: 8px 16px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.9rem;
      color: #334155;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .kfold-btn.active, .kfold-btn:hover {
      background: #059669;
      border-color: #059669;
      color: #FFFFFF;
    }

    .kfold-metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
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
      border-color: #A7F3D0;
      box-shadow: 0 2px 8px rgba(5, 150, 105, 0.06);
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
      .kfold-metrics-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
"""
