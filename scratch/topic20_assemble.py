# Topic 20 Assembly Script
# Combines CSS, HTML parts, injects 18 verified vector SVGs, and outputs to topic_20/notes.html

import os
import sys
import re

sys.path.insert(0, os.path.abspath("."))

from scratch.topic20_css import TOPIC20_CSS
from scratch.topic20_svgs import svgs
from scratch.topic20_part1 import TOPIC20_PART1
from scratch.topic20_part2 import TOPIC20_PART2
from scratch.topic20_part3 import TOPIC20_PART3
from scratch.topic20_part4 import TOPIC20_PART4

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 20: Cross-Validation and Model Validation &bull; CodeVerse ML Notes</title>
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
    print("Assembling Topic 20 notes...")
    body_content = TOPIC20_PART1 + "\\n" + TOPIC20_PART2 + "\\n" + TOPIC20_PART3 + "\\n" + TOPIC20_PART4
    
    # Replace all SVG placeholders
    print(f"Injecting {len(svgs)} SVG graphics...")
    for placeholder, svg_code in svgs.items():
        if placeholder in body_content:
            body_content = body_content.replace(placeholder, svg_code)
            print(f"  [x] Injected {placeholder}")
        else:
            print(f"  [!] Placeholder {placeholder} NOT found in body!")

    # Check for any lingering placeholders
    lingering = re.findall(r'__SVG_[A-Z0-9_]+__', body_content)
    if lingering:
        print(f"WARNING: Lingering placeholders found: {lingering}")
    else:
        print("  [x] All SVG placeholders successfully replaced!")

    final_html = HTML_TEMPLATE.format(css=TOPIC20_CSS, body=body_content)
    
    out_dir = os.path.join("coding", "machine_learning", "topic_20")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "notes.html")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"Successfully assembled and wrote {len(final_html)} bytes to {out_path}!")

if __name__ == "__main__":
    assemble()
