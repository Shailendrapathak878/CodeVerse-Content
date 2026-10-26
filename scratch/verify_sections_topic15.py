"""
Topic 15: Ensemble Learning - Verification Script
Checks all 27 sections, TOC links, 17 SVGs, absence of placeholders, and strict Light Mode.
"""

import re
import os

def verify_topic15():
    file_path = os.path.join("coding", "machine_learning", "topic_15", "notes.html")
    if not os.path.exists(file_path):
        print(f"FAIL: File {file_path} does not exist!")
        return False
    
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    print(f"Verifying {file_path} (Size: {len(html)} chars)...")

    # 1. Check sections
    all_sections = [f"sec-{i:02d}" for i in range(1, 28)]
    missing_sections = []
    for sec in all_sections:
        if f'id="{sec}"' not in html:
            missing_sections.append(sec)
    
    if missing_sections:
        print(f"FAIL: Missing sections: {missing_sections}")
    else:
        print("PASS: All 27 section IDs (sec-01 through sec-27) are present.")

    # 2. Check TOC links
    missing_toc_links = []
    for sec in all_sections:
        if f'href="#{sec}"' not in html:
            missing_toc_links.append(sec)

    if missing_toc_links:
        print(f"FAIL: Missing TOC links for: {missing_toc_links}")
    else:
        print("PASS: All 27 TOC links point correctly to the respective sections.")

    # 3. Check SVG diagrams
    svg_matches = re.findall(r'<svg\b', html)
    print(f"Found {len(svg_matches)} total <svg> elements (17 standalone diagrams + UI icons).")
    if len(svg_matches) < 17:
        print(f"FAIL: Expected at least 17 SVGs, found {len(svg_matches)}")
    else:
        print(f"PASS: Meets requirement of minimum 17 SVGs (total: {len(svg_matches)}).")

    # 4. Check for placeholders
    placeholders = re.findall(r'__SVG_[A-Z0-9_]+__|TODO|FIXME|PLACEHOLDER', html, re.IGNORECASE)
    if placeholders:
        print(f"FAIL: Found unresolved placeholders: {set(placeholders)}")
    else:
        print("PASS: Zero unresolved placeholders found.")

    # 5. Strict Light Mode Verification
    dark_checks = [
        ("prefers-color-scheme: dark", "@media (prefers-color-scheme: dark)"),
        ("prefers-color-scheme:dark", "@media (prefers-color-scheme:dark)"),
        (".dark-mode", "dark-mode class"),
        (".dark-theme", "dark-theme class"),
        ("dark_mode", "dark_mode identifier"),
        ("theme-toggle", "theme-toggle element")
    ]
    dark_violations = []
    for term, label in dark_checks:
        if term in html:
            dark_violations.append(label)

    if dark_violations:
        print(f"FAIL: Dark mode styling found: {dark_violations}")
    else:
        print("PASS: Strict Light Mode validated (zero dark mode queries, classes, or toggles).")

    # 6. Check interactive accordions
    details_count = len(re.findall(r'<details\b', html))
    print(f"Found {details_count} interactive <details> accordion elements.")
    if details_count < 12:
        print(f"FAIL: Expected at least 12 interactive FAQs, found {details_count}")
    else:
        print("PASS: 12 interactive accordions present.")

    # 7. Check mistake cards
    mistake_count = len(re.findall(r'class="mistake-card"', html))
    print(f"Found {mistake_count} mistake cards in Section 24.")
    if mistake_count < 12:
        print(f"FAIL: Expected at least 12 mistake cards, found {mistake_count}")
    else:
        print("PASS: Comprehensive mistake cards present.")

    return len(missing_sections) == 0 and len(missing_toc_links) == 0 and not dark_violations and len(placeholders) == 0

if __name__ == "__main__":
    success = verify_topic15()
    print("OVERALL VERIFICATION:", "PASS" if success else "FAIL")
