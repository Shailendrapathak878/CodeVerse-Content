"""
Sanitizes scratch/topic12_svgs.py by replacing named HTML entities with UTF-8 character literals.
"""

with open("scratch/topic12_svgs.py", "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "&ge;": "≥",
    "&le;": "≤",
    "&Delta;": "Δ",
    "&sum;": "Σ",
    "&times;": "×",
    "&check;": "✓",
    "&bull;": "•",
    "&rarr;": "→",
    "&sup2;": "²",
    "&sub1;": "₁",
    "&sub2;": "₂",
    "&deg;": "°",
    "&#8321;": "₁",
    "&#8322;": "₂",
    "&#7522;": "ᵢ",
    "&#772;": "̄",
}

for entity, char in replacements.items():
    content = content.replace(entity, char)

with open("scratch/topic12_svgs.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Sanitization applied successfully!")
