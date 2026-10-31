// unified_theme_template.js
// Universal responsive, dual-theme (Light/Dark) styling & interactive scripts for CodeVerse

function getUnifiedHeadStyles(lang) {
  let brandColor = '#2563EB'; // default
  let brandDark = '#1D4ED8';
  let brandLight = '#EFF6FF';
  let brandBorder = '#BFDBFE';

  if (lang === 'r') {
    brandColor = '#276DC3';
    brandDark = '#19355E';
    brandLight = '#F0F4F8';
    brandBorder = '#C8D7E8';
  } else if (lang === 'kotlin') {
    brandColor = '#7F52FF';
    brandDark = '#6336DF';
    brandLight = '#F5F3FF';
    brandBorder = '#DDD6FE';
  } else if (lang === 'dart') {
    brandColor = '#0175C2';
    brandDark = '#02569B';
    brandLight = '#F0F9FF';
    brandBorder = '#BAE6FD';
  }

  return `
    :root {
      /* Shared Brand Accents */
      --brand: ${brandColor};
      --brand-dark: ${brandDark};
      --brand-light: ${brandLight};
      --brand-border: ${brandBorder};
      
      --blue: #0284C7;
      --blue-light: #F0F9FF;
      --green: #10B981;
      --green-light: #ECFDF5;
      --amber: #F59E0B;
      --amber-light: #FFFBEB;
      --red: #EF4444;
      --red-light: #FEF2F2;
      --purple: #8B5CF6;
      --purple-light: #F5F3FF;
      --primary: var(--brand);
      --secondary: var(--blue);
      --accent: var(--green);
      --warning: var(--amber);
      --danger: var(--red);

      /* Light Theme (Default) */
      --bg: #F8FAFC;
      --bg-page: #F8FAFC;
      --bg-dark: #0B0F19;
      --bg-card: #FFFFFF;
      --card-bg: #FFFFFF;
      --card-soft: #F1F5F9;
      --card-border: #E2E8F0;
      --border: #E2E8F0;
      --border-color: #E2E8F0;
      --border-subtle: #EDF2F7;
      --text: #0F172A;
      --text-main: #0F172A;
      --text-primary: #0F172A;
      --text-secondary: #334155;
      --text-muted: #64748B;
      
      /* IDE Code Block Styling */
      --code-bg: #0F172A;
      --code-header: #1E293B;
      --code-border: #334155;
      --code-text: #E2E8F0;

      /* UI Radii & Shadows */
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 14px;
      --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.06);
      --shadow-md: 0 4px 6px -1px rgba(15, 23, 42, 0.08);
      --max-w: 1100px;
    }

    /* Dark Theme Overrides */
    [data-theme="dark"] {
      --bg: #0B0F19;
      --bg-page: #0B0F19;
      --bg-card: #151D2E;
      --card-bg: #151D2E;
      --card-soft: #1B253B;
      --card-border: #232F48;
      --border: #232F48;
      --border-color: #232F48;
      --border-subtle: #1C263A;
      --text: #F8FAFC;
      --text-main: #F8FAFC;
      --text-primary: #F8FAFC;
      --text-secondary: #CBD5E1;
      --text-muted: #94A3B8;

      --code-bg: #070A11;
      --code-header: #0F172A;
      --code-border: #1E293B;
      --code-text: #F1F5F9;

      --blue-light: rgba(2, 132, 199, 0.15);
      --green-light: rgba(16, 185, 129, 0.15);
      --amber-light: rgba(245, 158, 11, 0.15);
      --red-light: rgba(239, 68, 68, 0.15);
      --purple-light: rgba(139, 92, 246, 0.15);
      --brand-light: rgba(39, 109, 195, 0.18);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.45;
      color: var(--text-primary);
      background-color: var(--bg-page);
      padding: 8px;
      display: flex;
      justify-content: center;
      transition: background-color 0.2s ease, color 0.2s ease;
      font-size: 13px;
    }

    .container {
      width: 100%;
      max-width: var(--max-w);
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      padding: clamp(10px, 1.8vw, 20px);
      min-width: 0;
      overflow-x: hidden;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }

    /* Header Bar & Theme Switcher */
    .topic-nav-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border-color);
      flex-wrap: wrap;
      gap: 8px;
    }

    .topic-badges {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 8px;
      border-radius: 999px;
      font-size: 10.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .badge-brand { background: var(--brand-light); color: var(--brand); border: 1px solid var(--brand-border); }
    .badge-teal, .badge-primary { background: var(--blue-light); color: var(--blue); }
    .badge-green, .badge-success { background: var(--green-light); color: var(--green); }
    .badge-warning { background: var(--amber-light); color: var(--amber); }
    .badge-danger { background: var(--red-light); color: var(--red); }

    .theme-toggle-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--card-soft);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      user-select: none;
      transition: all 0.2s ease;
    }
    .theme-toggle-btn:hover {
      background: var(--border-color);
      color: var(--text-primary);
    }

    /* Headings */
    h1 {
      font-size: clamp(18px, 2.8vw, 24px);
      font-weight: 800;
      color: var(--text-primary);
      line-height: 1.25;
      margin-bottom: 6px;
      letter-spacing: -0.02em;
    }

    .lead-p, .subtitle {
      font-size: 13px;
      color: var(--text-secondary);
      margin-bottom: 14px;
      line-height: 1.5;
    }

    h2 {
      font-size: clamp(15px, 2vw, 18px);
      font-weight: 700;
      color: var(--text-primary);
      margin: 18px 0 8px;
      padding-bottom: 5px;
      border-bottom: 2px solid var(--border-color);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    h3 {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--text-primary);
      margin: 12px 0 5px;
    }

    p {
      color: var(--text-secondary);
      margin-bottom: 8px;
      line-height: 1.5;
    }

    /* Cards, Grids & Callouts */
    .card {
      background: var(--card-soft);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 10px 12px;
      margin-bottom: 10px;
      transition: background-color 0.2s ease, border-color 0.2s ease;
      min-width: 0;
    }
    .card-title {
      font-weight: 700;
      font-size: 13px;
      color: var(--brand);
      margin-bottom: 4px;
    }

    .grid-2, .grid-3 {
      display: grid;
      gap: 10px;
      margin-bottom: 10px;
    }
    .grid-2 { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
    .grid-3 { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
    .grid-2 > *, .grid-3 > * { min-width: 0; }

    .callout {
      border-left: 4px solid var(--brand);
      background: var(--brand-light);
      padding: 8px 12px;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      margin-bottom: 10px;
    }
    .callout-title {
      font-weight: 700;
      font-size: 12px;
      color: var(--brand);
      text-transform: uppercase;
      margin-bottom: 3px;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .warning-box {
      border-left: 4px solid var(--amber);
      background: var(--amber-light);
      padding: 8px 12px;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      margin-bottom: 10px;
    }
    .warning-box .callout-title {
      color: var(--amber);
    }

    .danger-box {
      border-left: 4px solid var(--red);
      background: var(--red-light);
      padding: 8px 12px;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      margin-bottom: 10px;
    }
    .danger-box .callout-title {
      color: var(--red);
    }

    /* Table styling */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 8px 0 12px;
      font-size: 12px;
      display: table;
      overflow-x: auto;
    }
    @media (max-width: 600px) {
      table {
        display: block;
        overflow-x: auto;
        white-space: nowrap;
      }
    }
    th, td {
      padding: 6px 9px;
      text-align: left;
      border-bottom: 1px solid var(--border-color);
    }
    th {
      background: var(--card-soft);
      color: var(--text-primary);
      font-weight: 700;
    }
    td {
      color: var(--text-secondary);
    }

    /* Visual Containers & SVGs */
    .svg-container {
      display: flex;
      justify-content: center;
      align-items: center;
      background: var(--card-soft);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 8px;
      margin: 10px 0;
      overflow: hidden;
      max-width: 100%;
    }
    .svg-container svg {
      max-width: 100%;
      height: auto;
      display: block;
    }

    /* IDE Code Container & Highlight.js Tokens */
    .code-container {
      background: var(--code-bg);
      border: 1px solid var(--code-border);
      border-radius: var(--radius-md);
      overflow: hidden;
      margin: 8px 0 12px;
      box-shadow: var(--shadow-sm);
      min-width: 0;
      max-width: 100%;
    }

    .code-header {
      background: var(--code-header);
      padding: 5px 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--code-border);
      gap: 6px;
    }

    .code-dots {
      display: flex;
      gap: 4px;
      align-items: center;
    }

    .code-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      display: inline-block;
    }
    .dot-red { background: #EF4444; }
    .dot-yellow { background: #F59E0B; }
    .dot-green { background: #10B981; }

    .code-title {
      color: #94A3B8;
      font-size: 11px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-weight: 500;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      flex: 1;
      margin-left: 4px;
    }

    .code-actions {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .code-badge {
      background: rgba(255, 255, 255, 0.08);
      color: #38BDF8;
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      padding: 2px 5px;
      border-radius: 3px;
      letter-spacing: 0.5px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }

    .copy-btn {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #E2E8F0;
      padding: 2px 7px;
      border-radius: 3px;
      font-size: 10px;
      font-weight: 600;
      cursor: pointer;
      user-select: none;
      transition: all 0.15s ease;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .copy-btn:hover {
      background: rgba(255, 255, 255, 0.2);
      color: #FFFFFF;
    }
    .copy-btn.copied {
      background: #10B981;
      border-color: #059669;
      color: #FFFFFF;
    }

    pre {
      padding: 10px 12px;
      overflow-x: auto;
      font-family: "JetBrains Mono", Consolas, "Courier New", monospace;
      font-size: 12px;
      line-height: 1.5;
      color: var(--code-text);
      background: transparent;
      margin: 0;
      white-space: pre;
      word-break: normal;
    }

    code {
      font-family: inherit;
    }

    p code, li code, td code {
      background: var(--card-soft);
      color: var(--brand);
      padding: 1px 4px;
      border-radius: 3px;
      font-size: 11px;
      font-family: "JetBrains Mono", Consolas, monospace;
      border: 1px solid var(--border-color);
    }

    /* Output Container */
    .output-box, .output-card {
      background: #060911;
      border-left: 3px solid var(--green);
      padding: 7px 10px;
      border-radius: 0 0 var(--radius-md) var(--radius-md);
      font-family: "JetBrains Mono", Consolas, monospace;
      font-size: 11px;
      color: #A7F3D0;
      margin-top: -12px;
      margin-bottom: 12px;
      overflow-x: auto;
      white-space: pre-wrap;
    }
    .output-label, .output-title {
      font-size: 9px;
      font-weight: 700;
      color: #6EE7B7;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: block;
      margin-bottom: 2px;
    }

    /* Highlight.js Colors (VS Code Dark Modern Theme) */
    .hljs-keyword { color: #F472B6; font-weight: 700; }
    .hljs-built_in { color: #38BDF8; font-weight: 600; }
    .hljs-type { color: #A78BFA; font-weight: 600; }
    .hljs-function { color: #60A5FA; }
    .hljs-title { color: #60A5FA; font-weight: 600; }
    .hljs-params { color: #E2E8F0; }
    .hljs-string { color: #34D399; }
    .hljs-number { color: #FBBF24; }
    .hljs-comment { color: #64748B; font-style: italic; }
    .hljs-operator { color: #F472B6; }
    .hljs-meta { color: #94A3B8; }
    .hljs-variable { color: #F8FAFC; }

    /* Interactive Details / Solution Box */
    details {
      background: var(--card-soft);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      margin: 6px 0;
      padding: 6px 10px;
    }
    summary {
      font-weight: 600;
      cursor: pointer;
      color: var(--brand);
      user-select: none;
    }
  `;
}

function getUnifiedScript() {
  return `
    <script>
      function toggleTheme() {
        var current = document.documentElement.getAttribute('data-theme') || 'light';
        var next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        updateToggleBtn(next);
      }

      function updateToggleBtn(theme) {
        var btn = document.getElementById('theme-toggle-btn');
        if (!btn) return;
        if (theme === 'dark') {
          btn.innerHTML = '☀️ Light Mode';
        } else {
          btn.innerHTML = '🌙 Dark Mode';
        }
      }

      function copyCode(btn) {
        var container = btn.closest('.code-container') || btn.closest('.code-card') || btn.parentElement.parentElement;
        var pre = container.querySelector('pre');
        if (!pre) return;
        var code = (pre.innerText || pre.textContent).trim();

        function showSuccess() {
          var origHTML = btn.innerHTML;
          btn.innerHTML = '✓ Copied!';
          btn.classList.add('copied');
          setTimeout(function() {
            btn.innerHTML = origHTML;
            btn.classList.remove('copied');
          }, 2000);
        }

        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(code).then(showSuccess).catch(function() {
            fallbackCopy(code, showSuccess);
          });
        } else {
          fallbackCopy(code, showSuccess);
        }
      }

      function fallbackCopy(text, cb) {
        var ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.focus();
        ta.select();
        try {
          document.execCommand('copy');
          if (cb) cb();
        } catch (e) {
          console.error('Fallback copy failed', e);
        }
        document.body.removeChild(ta);
      }

      // Initial theme check
      (function() {
        var initialTheme = document.documentElement.getAttribute('data-theme') || 'light';
        updateToggleBtn(initialTheme);
      })();
    </script>
  `;
}

module.exports = {
  getUnifiedHeadStyles,
  getUnifiedScript
};
