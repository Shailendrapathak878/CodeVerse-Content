"""
Topic 14: Naive Bayes - Assembly Script
Merges CSS, Part 1, Part 2, Part 3, Part 4, and all 15 SVGs into coding/machine_learning/topic_14/notes.html.
"""

import os
from topic14_css import TOPIC14_CSS
from topic14_part1 import TOPIC14_PART1
from topic14_part2 import TOPIC14_PART2
from topic14_part3 import TOPIC14_PART3
from topic14_part4 import TOPIC14_PART4
from topic14_svgs import ALL_SVGS

OUTPUT_DIR = os.path.join("coding", "machine_learning", "topic_14")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "notes.html")

def assemble():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    html_head = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 14: Naive Bayes &bull; CodeVerse Machine Learning</title>
  <style>
{TOPIC14_CSS}
  </style>
</head>
<body>
"""

    html_body = TOPIC14_PART1 + TOPIC14_PART2 + TOPIC14_PART3 + TOPIC14_PART4
    
    # Replace all SVG placeholders
    for name, svg_code in ALL_SVGS.items():
        placeholder = f"__{name}__"
        if placeholder in html_body:
            html_body = html_body.replace(placeholder, svg_code)
            print(f"Replaced placeholder {placeholder}")
        else:
            print(f"WARNING: Placeholder {placeholder} not found in content!")

    html_foot = """
</body>
</html>
"""

    full_html = html_head + html_body + html_foot
    
    # Validation checks
    unreplaced = [name for name in ALL_SVGS if f"__{name}__" in full_html]
    if unreplaced:
        print(f"ERROR: Unreplaced SVGs remaining: {unreplaced}")
    else:
        print("All SVG placeholders successfully resolved!")
        
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    file_size = os.path.getsize(OUTPUT_FILE)
    print(f"Successfully assembled {OUTPUT_FILE} ({file_size} bytes, {len(full_html.splitlines())} lines)")

if __name__ == "__main__":
    assemble()
