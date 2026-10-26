import re

with open('scratch/topic23_svgs.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace height="auto" with empty string
fixed_text = text.replace(' height="auto"', '')

with open('scratch/topic23_svgs.py', 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print("Updated topic23_svgs.py: removed height='auto'.")
