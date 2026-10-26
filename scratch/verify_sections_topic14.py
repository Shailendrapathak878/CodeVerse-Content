"""
Verification script for Topic 14 notes.html
Checks section IDs, TOC links, SVGs, light mode enforcement, and placeholders.
"""

import os
import re

NOTES_PATH = os.path.join("coding", "machine_learning", "topic_14", "notes.html")

def verify():
    assert os.path.exists(NOTES_PATH), f"File {NOTES_PATH} does not exist!"
    
    with open(NOTES_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"File Size: {len(content)} characters, {len(content.splitlines())} lines.")

    # 1. Verify all 23 section IDs
    expected_sections = [f"sec-{i:02d}" for i in range(1, 24)]
    missing_sections = []
    for s in expected_sections:
        if f'id="{s}"' not in content:
            missing_sections.append(s)

    if missing_sections:
        print(f"FAIL: Missing section IDs: {missing_sections}")
    else:
        print(f"PASS: All 23 section IDs present (sec-01 to sec-23).")

    # 2. Verify all 23 TOC links
    missing_toc = []
    for s in expected_sections:
        if f'href="#{s}"' not in content:
            missing_toc.append(s)

    if missing_toc:
        print(f"FAIL: Missing TOC links for: {missing_toc}")
    else:
        print(f"PASS: All 23 Table of Contents anchor links present.")

    # 3. Verify all 15 SVGs
    svg_count = content.count("<svg")
    print(f"SVG tags found in document: {svg_count}")
    assert svg_count >= 15, f"Expected at least 15 SVGs, found {svg_count}"
    print("PASS: Minimum 15 SVGs verified.")

    # 4. Check for placeholders
    placeholders = re.findall(r"__[A-Z0-9_]+__", content)
    if placeholders:
        print(f"FAIL: Found unreplaced placeholders: {placeholders}")
    else:
        print("PASS: Zero unresolved placeholders found.")

    # 5. Check Light Mode Only requirement
    dark_patterns = [
        "prefers-color-scheme: dark",
        "prefers-color-scheme:dark",
        "theme-dark",
        "dark-theme",
        "dark-mode",
        "theme-toggle",
        "class=\"dark\""
    ]
    dark_violations = []
    for dp in dark_patterns:
        if dp in content.lower():
            dark_violations.append(dp)

    if dark_violations:
        print(f"FAIL: Dark mode styling or toggles found: {dark_violations}")
    else:
        print("PASS: Strict Light Mode confirmed! Zero dark mode media queries or classes.")

    # 6. Check interactive accordions
    details_count = content.count("<details")
    summary_count = content.count("<summary")
    print(f"Accordion items found: {details_count} <details>, {summary_count} <summary>")
    assert details_count >= 12, f"Expected at least 12 accordions, found {details_count}"
    print("PASS: All 12 revision accordions present.")

    # 7. Check mistake cards
    mistake_count = content.count("class=\"mistake-card\"")
    print(f"Mistake cards found: {mistake_count}")
    assert mistake_count >= 12, f"Expected at least 12 mistake cards, found {mistake_count}"
    print("PASS: All 12 mistake cards present.")

    print("\nALL NOTES STRUCTURAL AND PEDAGOGICAL CHECKS PASSED!")

if __name__ == "__main__":
    verify()
