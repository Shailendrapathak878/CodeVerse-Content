"""
Assembles Topic 13 notes.html from modular parts into coding/machine_learning/topic_13/notes.html.
Replaces __SVG_...__ placeholders with actual validated vector SVGs.
"""

import os
from scratch.topic13_css import TOPIC13_CSS
from scratch.topic13_part1 import TOPIC13_PART1
from scratch.topic13_part2 import TOPIC13_PART2
from scratch.topic13_part3 import TOPIC13_PART3
from scratch.topic13_part4 import TOPIC13_PART4
import scratch.topic13_svgs as svgs

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Comprehensive educational notes on Machine Learning Topic 13: Support Vector Machine (SVM). Master maximum-margin hyperplanes, canonical margins, support vectors, hard vs. soft margin with slack variables, C regularization, kernel trick (Linear, Polynomial, RBF), gamma tuning, feature scaling, scikit-learn classification and SVR regression pipelines.">
  <title>Machine Learning &bull; Topic 13: Support Vector Machine (SVM)</title>
  <style>
""" + TOPIC13_CSS + """
  </style>
</head>
<body>
  <div class="container">
""" + TOPIC13_PART1 + TOPIC13_PART2 + TOPIC13_PART3 + TOPIC13_PART4 + """
  </div>
</body>
</html>
"""

def assemble():
    target_dir = os.path.join("coding", "machine_learning", "topic_13")
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, "notes.html")

    html = HTML_TEMPLATE

    # Replace SVG placeholders
    for name, svg_str in svgs.SVG_LIST:
        placeholder = f"__{name}__"
        if placeholder in html:
            html = html.replace(placeholder, svg_str)
            print(f"Replaced {placeholder}")
        else:
            print(f"WARNING: {placeholder} not found in template!")

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(html)

    file_size_kb = os.path.getsize(target_file) / 1024
    print(f"Successfully generated {target_file} ({file_size_kb:.2f} KB)")

if __name__ == "__main__":
    assemble()
