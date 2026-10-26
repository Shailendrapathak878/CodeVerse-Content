# Assembly script for Topic 19 notes.html
import os
import sys

# Add scratch to path
sys.path.append(os.path.join(os.path.dirname(__file__)))

from topic19_css import TOPIC19_CSS
from topic19_svgs import svgs
from topic19_part1 import TOPIC19_PART1
from topic19_part2 import TOPIC19_PART2
from topic19_part3 import TOPIC19_PART3
from topic19_part4 import TOPIC19_PART4

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 19: Classification and Regression Metrics | CodeVerse ML Notes</title>
  <style>
{css}
  </style>
</head>
<body>
  <div class="container">
{content}
  </div>
</body>
</html>
"""

def assemble_notes():
    content = TOPIC19_PART1 + "\\n" + TOPIC19_PART2 + "\\n" + TOPIC19_PART3 + "\\n" + TOPIC19_PART4

    # Replace SVG placeholders
    for placeholder, svg_code in svgs.items():
        if placeholder in content:
            content = content.replace(placeholder, svg_code)
        else:
            print(f"WARNING: Placeholder {placeholder} not found in content!")

    final_html = HTML_TEMPLATE.format(css=TOPIC19_CSS, content=content)

    output_dir = os.path.join("coding", "machine_learning", "topic_19")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "notes.html")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"SUCCESS: Assembled Topic 19 notes at {output_path}")
    print(f"Total HTML file size: {len(final_html)} characters, {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    assemble_notes()
