# Topic 21 Assembly Script
# Combines CSS, HTML parts 1-4, injects 20 verified vector SVGs, and outputs to coding/machine_learning/topic_21/notes.html

import os
import sys
import re

sys.path.insert(0, os.path.abspath("."))

from scratch.topic21_css import TOPIC21_CSS
from scratch.topic21_svgs import svgs
from scratch.topic21_part1 import TOPIC21_PART1
from scratch.topic21_part2 import TOPIC21_PART2
from scratch.topic21_part3 import TOPIC21_PART3
from scratch.topic21_part4 import TOPIC21_PART4

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 21: Overfitting, Underfitting &amp; Regularization &bull; CodeVerse ML Notes</title>
  <style>
{css}
  </style>
</head>
<body>
  <div class="page-container">
    <main class="content-wrapper">
{body}
    </main>
  </div>
</body>
</html>
"""

def assemble():
    print("=" * 60)
    print("Assembling Topic 21: Overfitting, Underfitting & Regularization...")
    print("=" * 60)
    
    body_content = TOPIC21_PART1 + "\n" + TOPIC21_PART2 + "\n" + TOPIC21_PART3 + "\n" + TOPIC21_PART4
    
    # Verify all 24 sections exist in body
    sections = re.findall(r'id="sec-([0-9]{2})"', body_content)
    print(f"Detected {len(sections)} sections in combined body: {sections}")
    expected_sections = [f"{i:02d}" for i in range(1, 25)]
    missing_sections = set(expected_sections) - set(sections)
    if missing_sections:
        raise ValueError(f"ERROR: Missing sections: {missing_sections}")
    print("  [x] All 24 required sections (01 to 24) are present!")

    # Replace all SVG placeholders
    print(f"\nInjecting {len(svgs)} SVG graphics...")
    injected_count = 0
    for placeholder, svg_code in svgs.items():
        if placeholder in body_content:
            body_content = body_content.replace(placeholder, svg_code)
            injected_count += 1
            print(f"  [x] Injected {placeholder}")
        else:
            print(f"  [!] WARNING: Placeholder {placeholder} NOT found in body!")

    if injected_count != len(svgs):
        print(f"WARNING: Expected {len(svgs)} SVGs, but only {injected_count} were injected.")
    else:
        print(f"  [x] All {len(svgs)} SVGs successfully injected!")

    # Check for any lingering placeholders
    lingering = re.findall(r'__SVG_[A-Z0-9_]+__', body_content)
    if lingering:
        raise ValueError(f"ERROR: Lingering placeholders found: {lingering}")
    print("  [x] No lingering placeholders detected.")

    final_html = HTML_TEMPLATE.format(css=TOPIC21_CSS, body=body_content)
    
    out_dir = os.path.join("coding", "machine_learning", "topic_21")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "notes.html")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"\nSuccessfully assembled and wrote {len(final_html):,} bytes ({os.path.getsize(out_path) / 1024:.1f} KB) to {out_path}!")

if __name__ == "__main__":
    assemble()
