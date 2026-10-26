"""
Module: topic12_assemble.py
Assembly script for Topic 12: Decision Trees notes.html
"""

import os
from scratch.topic12_css import TOPIC12_CSS
from scratch.topic12_part1 import PART1_HTML
from scratch.topic12_part2 import PART2_HTML
from scratch.topic12_part3 import PART3_HTML
from scratch.topic12_part4 import PART4_HTML

OUTPUT_DIR = os.path.join("coding", "machine_learning", "topic_12")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "notes.html")

os.makedirs(OUTPUT_DIR, exist_ok=True)

HTML_DOCUMENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Comprehensive educational notes on Machine Learning Topic 12: Decision Trees. Master hierarchical binary recursive splitting, Gini Impurity, Shannon Entropy, Information Gain, orthogonal decision boundaries, tree pruning, feature importance, scikit-learn classification and regression pipelines.">
  <title>Machine Learning &bull; Topic 12: Decision Trees</title>
  <style>
{TOPIC12_CSS}
  </style>
</head>
<body>
  <div class="container">
{PART1_HTML}
{PART2_HTML}
{PART3_HTML}
{PART4_HTML}
  </div>
</body>
</html>
"""

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(HTML_DOCUMENT)

file_size_kb = os.path.getsize(OUTPUT_PATH) / 1024
print(f"Successfully assembled {OUTPUT_PATH}")
print(f"File Size: {file_size_kb:.2f} KB")

# Verification checks
with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Check all 23 section anchors
for sec_idx in range(1, 24):
    anchor = f'id="sec-{sec_idx:02d}"'
    assert anchor in content, f"Missing section anchor {anchor}!"
print("All 23 section anchors verified present!")

# 2. Check for placeholder tokens
for token in ['TODO', 'FIXME', 'PLACEHOLDER', 'Lorem ipsum', 'NOT IMPLEMENTED']:
    count = content.count(token)
    assert count == 0, f"Found placeholder token {token} ({count} times)!"
print("Zero placeholder tokens found!")

# 3. Verify strict light mode requirement
assert "@media (prefers-color-scheme: dark)" not in content, "Dark mode media query detected!"
assert "dark-mode" not in content, "Dark mode class detected!"
print("Strict Light Mode styling verified!")

# 4. Verify all 15 SVG diagrams are present
svg_count = content.count("<svg")
print(f"Total embedded SVG diagrams: {svg_count}")
assert svg_count >= 15, f"Expected at least 15 SVGs, found {svg_count}!"

# 5. Verify file size is substantial and thorough
assert file_size_kb > 80.0, f"File size too small ({file_size_kb:.2f} KB)!"
print("[SUCCESS] All assembly verifications passed!")
