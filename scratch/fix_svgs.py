# Script to fix SVG strong tags and text anchor
with open('scratch/topic19_svgs.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace strong tags with tspan font-weight="700"
text = text.replace('<strong>', '<tspan font-weight="700">').replace('</strong>', '</tspan>')

# Fix line 48 in figure 1.1
old_line = '<text x="597" y="166" fill="#D97706" font-family="-apple-system, sans-serif" font-size="10" font-weight="700">Error = Actual &minus; Predicted = +$10,000</text>'
new_line = '<text x="597" y="166" fill="#D97706" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" text-anchor="middle">Error = Actual &minus; Predicted = +$10,000</text>'
text = text.replace(old_line, new_line)

with open('scratch/topic19_svgs.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated topic19_svgs.py!")
