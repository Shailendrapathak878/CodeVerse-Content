"""
Sanitize scratch/topic11_svgs.py: replace HTML entities with UTF-8 characters.
"""

with open('scratch/topic11_svgs.py', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    '&times;': '×',
    '&ldquo;': '“',
    '&rdquo;': '”',
    '&lsquo;': '‘',
    '&rsquo;': '’',
    '&radic;': '√',
    '&Sigma;': 'Σ',
    '&sup2;': '²',
    '&Delta;': 'Δ',
    '&isin;': '∈',
    '&bull;': '•',
    '&rarr;': '→',
    '&infin;': '∞',
    '&beta;': 'β',
    '&sigma;': 'σ',
    '&sum;': 'Σ',
}

for ent, char in replacements.items():
    text = text.replace(ent, char)

with open('scratch/topic11_svgs.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Sanitization complete!')
