"""
Module: topic10_assemble.py
Assembly script for Topic 10: Logistic Regression notes.html
"""

import os
from scratch.topic10_css import TOPIC10_CSS
from scratch.topic10_part1 import PART1_HTML
from scratch.topic10_part2 import PART2_HTML
from scratch.topic10_part3 import PART3_HTML
from scratch.topic10_part4 import PART4_HTML

OUTPUT_DIR = os.path.join("coding", "machine_learning", "topic_10")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "notes.html")

os.makedirs(OUTPUT_DIR, exist_ok=True)

HTML_DOCUMENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Comprehensive educational notes on Machine Learning Topic 10: Logistic Regression. Master binary classification, the sigmoid activation function, log-odds and logits, decision boundaries, maximum likelihood estimation, log loss, confusion matrices, ROC AUC, and leak-free scikit-learn pipelines.">
  <title>Machine Learning &bull; Topic 10: Logistic Regression</title>
  <style>
{TOPIC10_CSS}
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

# 1. Check all 21 section anchors
for sec_idx in range(1, 22):
    anchor = f'id="sec-{sec_idx:02d}"'
    assert anchor in content, f"Missing section anchor {anchor}!"
print("All 21 section anchors verified present!")

# 2. Check for placeholder tokens
for token in ['TODO', 'FIXME', 'PLACEHOLDER', 'Lorem ipsum']:
    count = content.count(token)
    assert count == 0, f"Found placeholder token {token} ({count} times)!"
print("Zero placeholder tokens found!")
