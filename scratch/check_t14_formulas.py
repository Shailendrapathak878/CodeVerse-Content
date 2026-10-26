with open('coding/machine_learning/topic_14/notes.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div class="formula-block">(.*?)</div>', text, re.DOTALL)
print(f"Total formula-block in Topic 14: {len(matches)}")
for i, m in enumerate(matches[:5], 1):
    print(f"--- Formula {i} ---")
    print(m.strip())
