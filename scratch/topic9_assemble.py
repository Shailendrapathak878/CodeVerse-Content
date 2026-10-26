"""
Assembly script for Topic 9: Linear Regression notes.html
"""

import os
from scratch.topic9_css import TOPIC9_CSS
from scratch.topic9_part1 import PART1_HTML
from scratch.topic9_part2 import PART2_HTML
from scratch.topic9_part3 import PART3_HTML
from scratch.topic9_part4 import PART4_HTML

OUTPUT_DIR = os.path.join("coding", "machine_learning", "topic_9")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "notes.html")

os.makedirs(OUTPUT_DIR, exist_ok=True)

HTML_DOCUMENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Comprehensive educational notes on Machine Learning Topic 9: Linear Regression. Master Ordinary Least Squares (OLS), slope and intercept, residual errors, gradient descent, multiple regression, diagnostic plots, and leak-free evaluation.">
  <title>Machine Learning &bull; Topic 9: Linear Regression</title>
  <style>
{TOPIC9_CSS}
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

# 1. Check all 19 section anchors
for sec_idx in range(1, 20):
    anchor = f'id="sec-{sec_idx:02d}"'
    assert anchor in content, f"Missing section anchor {anchor}!"
print("All 19 section anchors verified present!")

# 2. Check for placeholder tokens
for token in ['TODO', 'FIXME', 'PLACEHOLDER', 'Lorem ipsum']:
    count = content.count(token)
    assert count == 0, f"Found placeholder token {token} ({count} times)!"
print("Zero placeholder tokens found!")

# 3. Check for SVGs present
svg_count = content.count("<svg")
print(f"Total SVGs embedded: {svg_count}")
assert svg_count >= 14, f"Expected at least 14 SVGs, found {svg_count}!"

print("Topic 9 compilation & verification completed successfully!")
