import re

with open('coding/machine_learning/topic_21/notes.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix non-standard entities
text = text.replace('&sup9;', '<sup>9</sup>')
text = text.replace('&sup1;&deg;', '<sup>10</sup>')
text = text.replace('&sup4;', '<sup>4</sup>')
text = text.replace('&ycirc;', '&#375;')
text = text.replace('&check;', '&#10003;')

# Fix common mojibake characters
replacements = {
    'âœ“': '&#10003;',
    'â€“': '&ndash;',
    'â€”': '&mdash;',
    'â€¢': '&bull;',
    'â‰ˆ': '&asymp;',
    'â‰ ': '&ne;',
    'âˆ’': '&minus;',
    'âˆ‘': '&sum;',
    'Ã—': '&times;',
    'â ´': '<sup>4</sup>',
    'Â¹': '<sup>1</sup>',
    'Â²': '&sup2;',
    'Â³': '&sup3;',
    'Â±': '&plusmn;',
    'Â°': '&deg;',
    'Î»': '&lambda;',
    'Î±': '&alpha;',
    'Ïƒ': '&sigma;',
    'Î¼': '&mu;',
    'Å·': '&#375;',
    'â˜…': '&#9733;'
}

for bad, good in replacements.items():
    text = text.replace(bad, good)

with open('coding/machine_learning/topic_21/notes.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cleaned entities and mojibake in coding/machine_learning/topic_21/notes.html successfully!")
