"""
Module: topic9_css.py
Light Mode only CSS styles for Topic 9: Linear Regression.
Ensures zero horizontal overflow and 100% Flutter webview compatibility.
"""

TOPIC9_CSS = """
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

      /* Badges */
      --train-badge-bg: #EEF2FF;
      --train-badge-text: #4338CA;
      --val-badge-bg: #FEF3C7;
      --val-badge-text: #B45309;
      --test-badge-bg: #DCFCE7;
      --test-badge-text: #15803D;
      --leak-badge-bg: #FEE2E2;
      --leak-badge-text: #B91C1C;
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
      background: linear-gradient(90deg, #4F46E5, #06B6D4, #10B981);
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

    .toc-item {
      display: flex;
      align-items: baseline;
      gap: 0.6rem;
      text-decoration: none;
      color: #334155;
      font-size: 0.925rem;
      padding: 0.45rem 0.6rem;
      border-radius: 6px;
      transition: background 0.15s, color 0.15s;
    }

    .toc-item:hover {
      background: rgba(79, 70, 229, 0.08);
      color: var(--primary-accent);
    }

    .toc-num {
      font-weight: 700;
      font-size: 0.82rem;
      color: var(--primary-accent);
      min-width: 1.8rem;
    }

    /* Section Cards */
    .section-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 2.25rem;
      margin-bottom: 2.25rem;
      box-shadow: var(--card-shadow);
      overflow-x: hidden;
    }

    .section-header {
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 1px solid #F1F5F9;
    }

    .section-badge {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--primary-accent);
      background: var(--primary-accent-light);
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      margin-bottom: 0.5rem;
    }

    .section-title {
      font-size: 1.65rem;
      font-weight: 800;
      color: var(--heading-color);
      letter-spacing: -0.015em;
    }

    .section-intro {
      font-size: 1.05rem;
      line-height: 1.7;
      color: var(--text-secondary);
      margin-bottom: 1.5rem;
    }

    /* Semantic Callout Cards */
    .card {
      border-radius: 10px;
      padding: 1.35rem 1.5rem;
      margin: 1.5rem 0;
      border-left: 4px solid transparent;
    }

    .card-title {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 0.65rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .card-def {
      background: var(--def-card-bg);
      border-color: var(--def-card-border);
      border-left-color: var(--def-card-title);
      color: var(--def-card-text);
    }
    .card-def .card-title { color: var(--def-card-title); }

    .card-analogy {
      background: var(--analogy-card-bg);
      border-color: var(--analogy-card-border);
      border-left-color: var(--analogy-card-title);
      color: var(--analogy-card-text);
    }
    .card-analogy .card-title { color: var(--analogy-card-title); }

    .card-concept {
      background: var(--concept-card-bg);
      border-color: var(--concept-card-border);
      border-left-color: var(--concept-card-title);
      color: var(--concept-card-text);
    }
    .card-concept .card-title { color: var(--concept-card-title); }

    .card-warn {
      background: var(--warn-card-bg);
      border-color: var(--warn-card-border);
      border-left-color: var(--warn-card-title);
      color: var(--warn-card-text);
    }
    .card-warn .card-title { color: var(--warn-card-title); }

    .card-amber {
      background: var(--amber-card-bg);
      border-color: var(--amber-card-border);
      border-left-color: var(--amber-card-title);
      color: var(--amber-card-text);
    }
    .card-amber .card-title { color: var(--amber-card-title); }

    .card-success {
      background: var(--success-card-bg);
      border-color: var(--success-card-border);
      border-left-color: var(--success-card-title);
      color: var(--success-card-text);
    }
    .card-success .card-title { color: var(--success-card-title); }

    /* Formula Cards */
    .formula-card {
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-radius: 10px;
      padding: 1.5rem;
      margin: 1.5rem 0;
      text-align: center;
      box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }

    .formula-title {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #64748B;
      margin-bottom: 0.75rem;
    }

    .formula-box {
      font-family: "Cambria Math", "Latin Modern Math", "Times New Roman", serif;
      font-size: 1.45rem;
      font-weight: 600;
      color: #0F172A;
      padding: 0.85rem;
      background: #F8FAFC;
      border-radius: 8px;
      border: 1px solid #E2E8F0;
      display: inline-block;
      margin-bottom: 0.75rem;
      max-width: 100%;
      overflow-x: auto;
    }

    .formula-desc {
      font-size: 0.95rem;
      color: var(--text-secondary);
      max-width: 700px;
      margin: 0 auto;
      text-align: left;
    }

    /* Diagram Containers */
    .diagram-container {
      margin: 2rem 0;
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 1rem;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03);
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
      overflow-x: hidden;
    }

    .svg-diagram-wrap {
      width: 100%;
      max-width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
    }

    .svg-diagram-wrap svg {
      width: 100%;
      max-width: 100%;
      height: auto;
      display: block;
    }

    .diagram-caption {
      margin-top: 0.85rem;
      font-size: 0.875rem;
      color: #64748B;
      text-align: center;
      font-style: italic;
      padding: 0 0.5rem;
    }

    /* Tables */
    .table-wrapper {
      width: 100%;
      overflow-x: auto;
      margin: 1.5rem 0;
      border-radius: 8px;
      border: 1px solid #E2E8F0;
      -webkit-overflow-scrolling: touch;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
      background: #FFFFFF;
    }

    th {
      background-color: #F8FAFC;
      color: #0F172A;
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-bottom: 2px solid #E2E8F0;
      white-space: nowrap;
    }

    td {
      padding: 0.8rem 1rem;
      border-bottom: 1px solid #F1F5F9;
      color: #334155;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:nth-child(even) td {
      background-color: #FCFDFE;
    }

    /* Code Blocks */
    .code-block {
      background-color: var(--code-bg);
      border-radius: 10px;
      margin: 1.5rem 0;
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
      border: 1px solid #334155;
    }

    .code-header {
      background-color: var(--code-header-bg);
      padding: 0.6rem 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
    }

    .code-title {
      font-family: "SFMono-Regular", Consolas, monospace;
      font-size: 0.825rem;
      color: #94A3B8;
      font-weight: 600;
    }

    .code-lang {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #38BDF8;
      background: rgba(56, 189, 248, 0.1);
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
    }

    .code-block pre {
      padding: 1.25rem 1rem;
      overflow-x: auto;
      margin: 0;
      color: var(--code-text);
      -webkit-overflow-scrolling: touch;
    }

    /* Interactive Accordion Details */
    details {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      margin: 0.85rem 0;
      overflow: hidden;
      transition: border-color 0.15s;
    }

    details[open] {
      border-color: #CBD5E1;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }

    details summary {
      padding: 1rem 1.25rem;
      background: #F8FAFC;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      color: #0F172A;
      user-select: none;
      list-style: none;
    }

    details summary::-webkit-details-marker {
      display: none;
    }

    details summary:hover {
      background: #F1F5F9;
    }

    .details-content {
      padding: 1.25rem;
      border-top: 1px solid #E2E8F0;
      background: #FFFFFF;
      font-size: 0.95rem;
      line-height: 1.65;
      color: #334155;
    }

    /* Badges */
    .badge {
      display: inline-block;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 700;
    }
    .badge-train { background: var(--train-badge-bg); color: var(--train-badge-text); }
    .badge-val { background: var(--val-badge-bg); color: var(--val-badge-text); }
    .badge-test { background: var(--test-badge-bg); color: var(--test-badge-text); }
    .badge-leak { background: var(--leak-badge-bg); color: var(--leak-badge-text); }

    /* Footer */
    .notes-footer {
      margin-top: 3.5rem;
      padding: 2rem 0;
      border-top: 1px solid #E2E8F0;
      text-align: center;
      color: #64748B;
      font-size: 0.875rem;
    }

    /* Responsive Media Queries */
    @media (max-width: 768px) {
      .container {
        padding: 1.25rem 0.75rem;
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
    }

    @media (max-width: 480px) {
      .hero-title {
        font-size: 1.6rem;
      }
      .formula-box {
        font-size: 1.15rem;
        padding: 0.6rem;
      }
      table {
        font-size: 0.85rem;
      }
      th, td {
        padding: 0.6rem 0.6rem;
      }
    }
"""
