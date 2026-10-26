# Topic 20 Structural and Quality Verification Script
import os
import re

html_path = os.path.join("coding", "machine_learning", "topic_20", "notes.html")

def verify():
    assert os.path.exists(html_path), f"File {html_path} does not exist!"
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    print(f"File Size: {len(content)} bytes ({len(content)/1024:.1f} KB)")
    
    # 1. Section IDs
    section_ids = re.findall(r'<section\s+id=[\'"](sec-\d+)[\'"]', content)
    print(f"Sections Found ({len(section_ids)}/23): {section_ids}")
    expected_ids = [f"sec-{i:02d}" for i in range(1, 24)]
    missing = set(expected_ids) - set(section_ids)
    assert not missing, f"Missing sections: {missing}"
    print("  [x] All 23 sections (sec-01 to sec-23) present!")

    # 2. TOC links
    toc_links = re.findall(r'href=[\'"]#(sec-\d+)[\'"]', content)
    print(f"TOC Links Found ({len(toc_links)}/23): {toc_links}")
    assert len(toc_links) >= 23, f"Expected 23 TOC links, found {len(toc_links)}"
    print("  [x] All 23 TOC links present!")

    # 3. SVG placeholders
    lingering_svg = re.findall(r'__SVG_[A-Z0-9_]+__', content)
    assert not lingering_svg, f"Found lingering SVG placeholders: {lingering_svg}"
    svg_tags = re.findall(r'<svg\b', content)
    print(f"Total SVG tags: {len(svg_tags)} (18 vector diagrams + UI icons)")
    assert len(svg_tags) >= 18, f"Expected at least 18 SVGs, found {len(svg_tags)}"
    print("  [x] SVG graphics verified!")

    # 4. Mistake cards
    mistake_cards = re.findall(r'class=[\'"]mistake-card[\'"]', content)
    print(f"Mistake Cards: {len(mistake_cards)} (Expected: 15)")
    assert len(mistake_cards) == 15, f"Expected 15 mistake cards, found {len(mistake_cards)}"
    print("  [x] 15 common pitfall cards verified!")

    # 5. FAQ accordions
    faq_items = re.findall(r'<details\s+class=[\'"]faq-item[\'"]', content)
    print(f"FAQ / Self-check Accordions: {len(faq_items)} (Expected: 12)")
    assert len(faq_items) == 12, f"Expected 12 FAQ items, found {len(faq_items)}"
    print("  [x] 12 FAQ accordions verified!")

    # 6. Tables and code blocks
    tables = re.findall(r'<table\b', content)
    code_blocks = re.findall(r'<pre><code\b', content)
    print(f"Data Tables: {len(tables)}, Code Blocks: {len(code_blocks)}")
    assert len(tables) >= 6, f"Expected >= 6 tables, found {len(tables)}"
    assert len(code_blocks) >= 6, f"Expected >= 6 code blocks, found {len(code_blocks)}"
    print("  [x] Tables and code blocks verified!")

    # 7. Strict Light Mode Check
    dark_media = re.findall(r'prefers-color-scheme\s*:\s*dark', content, re.IGNORECASE)
    assert not dark_media, "Found dark mode media query! Strict Light Mode required."
    print("  [x] Strict Light Mode verified (no dark media queries)!")

    # 8. Check for raw unrendered LaTeX syntax
    latex_patterns = [
        r'\\frac\{',
        r'\$\$.*?\$\$',
        r'\\sum_',
        r'\\sigma\b',
        r'\\le\b',
        r'\\ge\b',
        r'\\hat\{'
    ]
    latex_matches = []
    for pat in latex_patterns:
        m = re.findall(pat, content)
        if m:
            latex_matches.append((pat, len(m)))
    if latex_matches:
        print(f"WARNING: Potential raw LaTeX patterns found: {latex_matches}")
    else:
        print("  [x] Zero unrendered raw LaTeX patterns found!")

    print("\\nALL STRUCTURAL TESTS PASSED!")

if __name__ == "__main__":
    verify()
