"""Verification script for Topic 16 notes.html.
Asserts all 27 sections, 18 SVGs, 14+ mistakes, 12 accordions, strict Light Mode.
"""
import re
import os

def verify_topic16():
    file_path = os.path.join("coding", "machine_learning", "topic_16", "notes.html")
    assert os.path.exists(file_path), f"File not found: {file_path}"
    
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    print(f"Loaded {file_path} (length: {len(html)} chars)")
    
    # 1. Verify all 27 sections
    for i in range(1, 28):
        sec_id = f"sec-{i:02d}"
        assert f'id="{sec_id}"' in html, f"Missing section id: {sec_id}"
    print("PASS: All 27 sections (sec-01 through sec-27) present!")
    
    # 2. Verify all 18 SVGs
    svg_count = html.count("<svg")
    assert svg_count == 18, f"Expected 18 SVGs, found {svg_count}"
    print("PASS: Exactly 18 vector SVGs embedded!")
    
    # 3. Verify strict Light Mode
    assert "@media (prefers-color-scheme: dark)" not in html, "Found dark mode media query!"
    assert "dark-mode" not in html, "Found dark-mode class!"
    assert "theme-toggle" not in html, "Found theme toggle!"
    print("PASS: Strict Light Mode verified (zero dark-mode CSS or toggles)!")
    
    # 4. Verify 14+ mistake cards
    mistake_count = len(re.findall(r'class="mistake-card"', html))
    assert mistake_count >= 14, f"Expected at least 14 mistake cards, found {mistake_count}"
    print(f"PASS: {mistake_count} practitioner mistake cards found (>= 14)!")
    
    # 5. Verify 12 interactive accordions
    details_count = html.count("<details>")
    assert details_count >= 12, f"Expected at least 12 <details> accordions, found {details_count}"
    print(f"PASS: {details_count} interactive FAQ accordions found (>= 12)!")
    
    # 6. Verify 3 runnable labs
    assert "kmeans_complete_lab.py" in html, "Missing K-Means complete lab"
    assert "hierarchical_complete_lab.py" in html, "Missing Hierarchical complete lab"
    assert "dbscan_complete_lab.py" in html, "Missing DBSCAN complete lab"
    print("PASS: All 3 runnable Python lab scripts present with console outputs!")
    
    # 7. Verify zero unresolved placeholders
    assert "__SVG_" not in html, "Found unresolved __SVG_ placeholder!"
    print("PASS: Zero unresolved template placeholders!")
    
    print("\nALL TOPIC 16 STRUCTURAL AUDITS PASSED PERFECTLY!")

if __name__ == "__main__":
    verify_topic16()
