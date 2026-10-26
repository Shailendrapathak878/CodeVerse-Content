# Sanitize Topic 21 SVGs
# Replaces non-XML HTML named entities with literal UTF-8 characters

import os
import sys
import re

sys.path.insert(0, os.path.abspath("."))

svg_file = os.path.join("scratch", "topic21_svgs.py")

ENTITY_MAP = {
    "&bull;": "•",
    "&rarr;": "→",
    "&larr;": "←",
    "&lambda;": "λ",
    "&alpha;": "α",
    "&sigma;": "σ",
    "&sup1;": "¹",
    "&sup2;": "²",
    "&sup3;": "³",
    "&ne;": "≠",
    "&asymp;": "≈",
    "&plusmn;": "±",
    "&check;": "✓",
    "&minus;": "−",
    "&ycirc;": "ŷ",
    "&star;": "★",
    "&deg;": "°",
    "&ndash;": "–",
    "&sum;": "∑",
    "&times;": "×",
    "&mu;": "μ",
    "&sup4;": "⁴",
}

with open(svg_file, "r", encoding="utf-8") as f:
    content = f.read()

for ent, char in ENTITY_MAP.items():
    content = content.replace(ent, char)

with open(svg_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Sanitization complete. Testing XML validity...")

import importlib
import scratch.topic21_svgs as s
importlib.reload(s)
import xml.etree.ElementTree as ET

failed = 0
for k, v in s.svgs.items():
    try:
        ET.fromstring(v)
    except Exception as e:
        print(f"FAILED {k}: {e}")
        failed += 1

if failed == 0:
    print(f"SUCCESS: All {len(s.svgs)} SVGs are 100% valid XML!")
else:
    print(f"Errors in {failed} SVGs.")
