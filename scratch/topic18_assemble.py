import os
import sys

sys.path.append('scratch')

from topic18_css import TOPIC18_CSS
from topic18_svgs import svgs
from topic18_part1 import PART1_HTML
from topic18_part2 import PART2_HTML
from topic18_part3 import PART3_HTML
from topic18_part4 import PART4_HTML

print("Assembling Topic 18 notes...")

# Combine parts
full_body = PART1_HTML + "\\n" + PART2_HTML + "\\n" + PART3_HTML + "\\n" + PART4_HTML

# Replace all SVG placeholders
for k, v in svgs.items():
    if k in full_body:
        full_body = full_body.replace(k, v)
        print(f"  Replaced {k}")
    else:
        print(f"  WARNING: Placeholder {k} not found in body!")

# Build complete HTML
html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 18: Anomaly Detection &bull; CodeVerse Machine Learning</title>
  <style>
{TOPIC18_CSS}
  </style>
</head>
<body>
{full_body}
</body>
</html>
"""

out_dir = os.path.join("coding", "machine_learning", "topic_18")
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "notes.html")

with open(out_file, "w", encoding="utf-8") as f:
    f.write(html_doc)

file_size_kb = os.path.getsize(out_file) / 1024
print(f"Topic 18 notes assembled successfully at: {out_file}")
print(f"File size: {file_size_kb:.2f} KB ({os.path.getsize(out_file)} bytes)")
