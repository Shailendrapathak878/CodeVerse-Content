"""
Module: topic8_css.py
Light Mode only CSS styles for Topic 8: Train, Validation & Test Sets.
Ensures zero horizontal overflow and 100% Flutter webview compatibility.
"""

TOPIC8_CSS = """
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

      /* Subset Badge Colors */
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

    /* Container */
    .container {
      max-width: 900px;
      margin: 0 auto;
      padding: 2rem 1.25rem 4rem 1.25rem;
      width: 100%;
    }

    @media (max-width: 640px) {
      .container {
        padding: 1.25rem 0.85rem 3rem 0.85rem;
      }
    }

    /* Hero Card */
    .hero-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 2.5rem 2rem;
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
      height: 6px;
      background: linear-gradient(90deg, #4F46E5, #F59E0B, #10B981, #06B6D4);
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--primary-badge-bg);
      color: var(--primary-badge-text);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .hero-title {
      font-size: 2.25rem;
      font-weight: 800;
      color: var(--heading-color);
      line-height: 1.2;
      margin-bottom: 0.85rem;
      letter-spacing: -0.02em;
    }

    @media (max-width: 640px) {
      .hero-title {
        font-size: 1.75rem;
      }
    }

    .hero-subtitle {
      font-size: 1.12rem;
      color: var(--text-secondary);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }

    .hero-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      border-top: 1px solid var(--card-border);
      padding-top: 1.25rem;
    }

    .meta-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      font-size: 0.82rem;
      color: var(--text-muted);
      background: var(--card-soft-bg);
      padding: 0.3rem 0.65rem;
      border-radius: 6px;
      font-weight: 500;
    }

    /* Table of Contents */
    .toc-container {
      background: var(--toc-bg);
      border: 1px solid var(--toc-border);
      border-radius: 14px;
      padding: 1.75rem;
      margin-bottom: 2.5rem;
    }

    .toc-title {
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--toc-text);
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .toc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem;
    }

    .toc-list {
      list-style: none;
    }

    .toc-item {
      margin-bottom: 0.5rem;
      font-size: 0.92rem;
      line-height: 1.4;
    }

    .toc-item a {
      color: var(--text-secondary);
      text-decoration: none;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
      transition: color 0.15s ease;
    }

    .toc-item a:hover {
      color: var(--primary-accent);
      font-weight: 600;
    }

    .toc-number {
      font-weight: 700;
      font-size: 0.8rem;
      color: var(--primary-accent);
      min-width: 1.8rem;
    }

    /* Section Containers */
    .section-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 2.25rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--card-shadow);
      overflow-x: hidden;
    }

    @media (max-width: 640px) {
      .section-card {
        padding: 1.5rem 1rem;
      }
    }

    .section-header {
      margin-bottom: 1.5rem;
      border-bottom: 2px solid var(--card-soft-bg);
      padding-bottom: 1rem;
    }

    .section-badge {
      display: inline-block;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--primary-accent);
      background: var(--primary-accent-light);
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      margin-bottom: 0.5rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .section-title {
      font-size: 1.65rem;
      font-weight: 700;
      color: var(--heading-color);
      line-height: 1.3;
    }

    .section-intro {
      font-size: 1.05rem;
      color: var(--text-secondary);
      margin-bottom: 1.5rem;
      line-height: 1.65;
    }

    h3 {
      font-size: 1.25rem;
      font-weight: 700;
      color: #1E293B;
      margin: 1.75rem 0 0.85rem 0;
    }

    h4 {
      font-size: 1.05rem;
      font-weight: 600;
      color: #334155;
      margin: 1.25rem 0 0.5rem 0;
    }

    p {
      margin-bottom: 1rem;
      color: var(--text-secondary);
    }

    /* Educational Cards */
    .card {
      border-radius: 10px;
      padding: 1.25rem 1.5rem;
      margin: 1.25rem 0;
      border-left: 4px solid;
    }

    .card-title {
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .card-def {
      background: var(--def-card-bg);
      border-color: var(--def-card-title);
      color: var(--def-card-text);
    }
    .card-def .card-title { color: var(--def-card-title); }

    .card-analogy {
      background: var(--analogy-card-bg);
      border-color: var(--analogy-card-title);
      color: var(--analogy-card-text);
    }
    .card-analogy .card-title { color: var(--analogy-card-title); }

    .card-concept {
      background: var(--concept-card-bg);
      border-color: var(--concept-card-title);
      color: var(--concept-card-text);
    }
    .card-concept .card-title { color: var(--concept-card-title); }

    .card-warn {
      background: var(--warn-card-bg);
      border-color: var(--warn-card-title);
      color: var(--warn-card-text);
    }
    .card-warn .card-title { color: var(--warn-card-title); }

    .card-amber {
      background: var(--amber-card-bg);
      border-color: var(--amber-card-title);
      color: var(--amber-card-text);
    }
    .card-amber .card-title { color: var(--amber-card-title); }

    .card-success {
      background: var(--success-card-bg);
      border-color: var(--success-card-title);
      color: var(--success-card-text);
    }
    .card-success .card-title { color: var(--success-card-title); }

    /* Lists */
    ul, ol {
      margin-left: 1.5rem;
      margin-bottom: 1.25rem;
      color: var(--text-secondary);
    }

    li {
      margin-bottom: 0.5rem;
      line-height: 1.6;
    }

    /* Inline Code and Badges */
    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      font-size: 0.88em;
      background: var(--card-soft-bg);
      color: #D946EF;
      padding: 0.15rem 0.35rem;
      border-radius: 4px;
      border: 1px solid #E2E8F0;
    }

    .key-badge {
      display: inline-block;
      font-family: monospace;
      font-size: 0.82rem;
      font-weight: 600;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      margin: 0.1rem 0;
    }
    .badge-train { background: var(--train-badge-bg); color: var(--train-badge-text); border: 1px solid #C7D2FE; }
    .badge-val { background: var(--val-badge-bg); color: var(--val-badge-text); border: 1px solid #FDE68A; }
    .badge-test { background: var(--test-badge-bg); color: var(--test-badge-text); border: 1px solid #BBF7D0; }
    .badge-leak { background: var(--leak-badge-bg); color: var(--leak-badge-text); border: 1px solid #FECACA; }

    /* Tables */
    .table-wrapper {
      width: 100%;
      overflow-x: auto;
      margin: 1.5rem 0;
      border: 1px solid var(--card-border);
      border-radius: 10px;
      background: #FFFFFF;
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
      text-align: left;
    }

    th {
      background: #F8FAFC;
      color: #334155;
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-bottom: 2px solid var(--card-border);
      white-space: nowrap;
    }

    td {
      padding: 0.8rem 1rem;
      border-bottom: 1px solid #F1F5F9;
      color: var(--text-secondary);
      vertical-align: top;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:nth-child(even) td {
      background-color: #FAFAFA;
    }

    /* Diagram Containers */
    .diagram-container {
      margin: 2rem 0;
      background: #FFFFFF;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 1.25rem;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    .svg-diagram-wrap {
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow-x: auto;
      padding: 0.5rem 0;
    }

    .svg-diagram-wrap svg {
      max-width: 100%;
      height: auto;
      display: block;
    }

    .diagram-caption {
      font-size: 0.85rem;
      color: var(--text-muted);
      text-align: center;
      margin-top: 0.75rem;
      font-style: italic;
    }

    .how-to-read {
      background: #F8FAFC;
      border-left: 3px solid var(--primary-accent);
      padding: 0.85rem 1.15rem;
      margin-top: 1rem;
      border-radius: 0 8px 8px 0;
      font-size: 0.88rem;
      color: #334155;
    }

    .how-to-read-title {
      font-weight: 700;
      color: var(--primary-accent);
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }

    .diagram-takeaway {
      background: #F0FDF4;
      border-left: 3px solid #16A34A;
      padding: 0.85rem 1.15rem;
      margin-top: 0.75rem;
      border-radius: 0 8px 8px 0;
      font-size: 0.88rem;
      color: #166534;
    }

    /* Formula Cards */
    .formula-card {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-radius: 10px;
      padding: 1.25rem 1.5rem;
      margin: 1.5rem 0;
      text-align: center;
    }

    .formula-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: #475569;
      margin-bottom: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .formula-box {
      font-size: 1.35rem;
      font-family: "Cambria Math", "Times New Roman", serif;
      font-weight: 600;
      color: #1E293B;
      padding: 0.85rem 1.5rem;
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      display: inline-block;
      margin: 0.5rem 0;
    }

    .formula-desc {
      font-size: 0.88rem;
      color: #64748B;
      margin-top: 0.75rem;
      text-align: left;
    }

    /* Code Blocks */
    .code-block {
      background: var(--code-bg);
      border-radius: 10px;
      margin: 1.5rem 0;
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.12);
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
      color: #94A3B8;
      font-size: 0.8rem;
      font-family: monospace;
      font-weight: 600;
    }

    .code-lang {
      background: #334155;
      color: #38BDF8;
      font-size: 0.72rem;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      font-weight: 700;
      text-transform: uppercase;
    }

    pre {
      padding: 1.25rem 1rem;
      overflow-x: auto;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      font-size: 0.88rem;
      line-height: 1.6;
      color: var(--code-text);
    }

    pre code {
      background: transparent;
      color: inherit;
      padding: 0;
      border: none;
      font-size: 1em;
    }

    /* Accordions (<details>) */
    details {
      background: #FFFFFF;
      border: 1px solid var(--card-border);
      border-radius: 8px;
      margin-bottom: 0.85rem;
      overflow: hidden;
      transition: all 0.2s ease;
    }

    details[open] {
      border-color: #CBD5E1;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    summary {
      padding: 1rem 1.25rem;
      font-weight: 600;
      color: #1E293B;
      cursor: pointer;
      user-select: none;
      background: #F8FAFC;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: background 0.15s ease;
    }

    summary:hover {
      background: #F1F5F9;
      color: var(--primary-accent);
    }

    .details-content {
      padding: 1.25rem;
      border-top: 1px solid var(--card-border);
      background: #FFFFFF;
      font-size: 0.95rem;
      color: var(--text-secondary);
      line-height: 1.65;
    }

    /* Footer */
    .notes-footer {
      text-align: center;
      padding: 2.5rem 0 1rem 0;
      border-top: 1px solid var(--card-border);
      color: var(--text-muted);
      font-size: 0.85rem;
    }
"""
