with open('scratch/topic8_svgs.py', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '&bull;': '•',
    '&mdash;': '—',
    '&ndash;': '–',
    '&times;': '✕',
    '&radic;': '√',
    '&mu;': 'μ',
    '&sigma;': 'σ',
    '&alpha;': 'α',
    '&rarr;': '→',
    '&larr;': '←',
    '&check;': '✓',
    '&apos;': "'",
}

for ent, rep in replacements.items():
    content = content.replace(ent, rep)

with open('scratch/topic8_svgs.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete. Validating...")
import scratch.topic8_svgs as s
s.validate_all_svgs()
