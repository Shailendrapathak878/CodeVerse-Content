// topic_transformer.js
// Parses, beautifies, highlights, adds copy buttons, and applies dual-theme system to a topic HTML

const fs = require('fs');
const path = require('path');
const { buildCodeBlock, stripTags } = require('./unified_highlighter.js');
const { getUnifiedHeadStyles, getUnifiedScript } = require('./unified_theme_template.js');

/**
 * Transforms an existing topic HTML file cleanly
 */
function transformTopicHtml(filePath, language, topicNum) {
  let html = fs.readFileSync(filePath, 'utf8');

  // 1. Ensure <html data-theme="light">
  html = html.replace(/<html[^>]*>/i, '<html lang="en" data-theme="light">');

  // 2. Replace or inject unified <style>
  const unifiedCss = getUnifiedHeadStyles(language);
  if (/<style>[\s\S]*?<\/style>/i.test(html)) {
    html = html.replace(/<style>[\s\S]*?<\/style>/i, `<style>${unifiedCss}</style>`);
  } else {
    html = html.replace(/<\/head>/i, `<style>${unifiedCss}</style>\n</head>`);
  }

  // 3. Inject Theme Switcher Button into the header/nav if not already present in body
  const navBarHtml = `
  <div class="topic-nav-bar">
    <div class="topic-badges">
      <span class="badge badge-brand">${language.toUpperCase()} Track</span>
      <span class="badge badge-teal">Topic ${topicNum}</span>
    </div>
    <button id="theme-toggle-btn" class="theme-toggle-btn" onclick="toggleTheme()" title="Toggle Dark/Light Mode">
      🌙 Dark Mode
    </button>
  </div>`;
  
  // Remove any stale nav-bar first to avoid duplicates
  html = html.replace(/<div class="topic-nav-bar">[\s\S]*?<\/div>\s*<\/div>/i, '');

  if (html.includes('<div class="container">')) {
    html = html.replace('<div class="container">', `<div class="container">\n${navBarHtml}`);
  } else if (html.includes('<body>')) {
    html = html.replace('<body>', `<body>\n<div class="container">\n${navBarHtml}`);
    html = html.replace('</body>', '</div>\n</body>');
  }

  // 4. Remove existing wrapper divs around pre if they are .code-card or .code-container
  html = html.replace(/<div class="(?:code-container|code-card)"[^>]*>([\s\S]*?)<\/div>/gi, (match, inner) => {
    const preMatch = inner.match(/<pre[^>]*>[\s\S]*?<\/pre>/i);
    if (preMatch) {
      let title = '';
      const headerMatch = inner.match(/<div class="code-header"[^>]*>([\s\S]*?)<\/div>/i);
      if (headerMatch) {
        title = stripTags(headerMatch[1]).replace(/copy/gi, '').trim();
      }
      return title ? `<!--title:${title}-->${preMatch[0]}` : preMatch[0];
    }
    return match;
  });

  // 5. Now transform every <pre[^>]*>...</pre> cleanly
  html = html.replace(/(?:<!--title:([^-]*)-->)?\s*<pre[^>]*>([\s\S]*?)<\/pre>/gi, (match, extractedTitle, codeInner) => {
    const rawCode = stripTags(codeInner).trim();
    if (!rawCode) return match;

    const title = (extractedTitle && extractedTitle.trim()) ? extractedTitle.trim() : `${language.toUpperCase()} Script`;
    return buildCodeBlock({
      code: rawCode,
      language: language,
      title: title,
      langBadge: language.toUpperCase()
    });
  });

  // 6. Ensure Copy script and toggleTheme script are in the page before </body>
  const unifiedScript = getUnifiedScript();
  if (html.includes('<script>')) {
    // Replace old script
    html = html.replace(/<script>[\s\S]*?<\/script>/gi, '');
  }
  html = html.replace(/<\/body>/i, `${unifiedScript}\n</body>`);

  fs.writeFileSync(filePath, html, 'utf8');
  return { success: true };
}

module.exports = {
  transformTopicHtml
};
