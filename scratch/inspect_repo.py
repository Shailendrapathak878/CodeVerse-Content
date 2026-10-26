import re
import os

with open('coding/machine_learning/topic_16/notes.html', 'r', encoding='utf-8') as f:
    text = f.read()

secs = re.findall(r'id="(sec-[0-9]+)"', text)
print('Topic 16 section IDs:', secs)
print('Total sections:', len(secs))
