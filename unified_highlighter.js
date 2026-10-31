// unified_highlighter.js
// Universal syntax highlighter & code block decorator for CodeVerse notes

const hljs = require('C:/Users/rp353/AppData/Roaming/npm/node_modules/firebase-tools/node_modules/highlight.js');

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function unescapeHtml(text) {
  return text
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#039;/g, "'")
    .replace(/&amp;/g, '&');
}

/**
 * Strips existing HTML tags from code text to get pure raw source code
 */
function stripTags(html) {
  return unescapeHtml(html.replace(/<[^>]*>/g, ''));
}

/**
 * Highlights a snippet for R, Kotlin, or Dart
 */
function highlightCode(rawCode, language) {
  const langKey = language.toLowerCase();
  let hlLang = langKey;
  if (langKey === 'r') hlLang = 'r';
  else if (langKey === 'kotlin') hlLang = 'kotlin';
  else if (langKey === 'dart') hlLang = 'dart';
  else if (langKey === 'bash' || langKey === 'terminal' || langKey === 'shell') hlLang = 'bash';

  try {
    const res = hljs.highlight(rawCode, { language: hlLang, ignoreIllegals: true });
    return res.value;
  } catch (e) {
    return escapeHtml(rawCode);
  }
}

/**
 * Generates the unified IDE code block HTML
 */
function buildCodeBlock({ code, language, title, langBadge }) {
  const rawCode = stripTags(code).trim();
  const highlighted = highlightCode(rawCode, language);
  const displayTitle = title || (language.toUpperCase() + ' Code');
  const badgeText = langBadge || language.toUpperCase();

  return `<div class="code-container">
  <div class="code-header">
    <div class="code-dots">
      <span class="code-dot dot-red"></span>
      <span class="code-dot dot-yellow"></span>
      <span class="code-dot dot-green"></span>
    </div>
    <span class="code-title">${escapeHtml(displayTitle)}</span>
    <div class="code-actions">
      <span class="code-badge">${escapeHtml(badgeText)}</span>
      <button class="copy-btn" onclick="copyCode(this)" title="Copy Code">
        <svg class="copy-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
        <span>Copy</span>
      </button>
    </div>
  </div>
  <pre><code>${highlighted}</code></pre>
</div>`;
}

module.exports = {
  buildCodeBlock,
  highlightCode,
  stripTags,
  escapeHtml,
  unescapeHtml
};

