import re

for part in ['topic24_part1.py', 'topic24_part2.py', 'topic24_part3.py', 'topic24_part4.py']:
    with open('scratch/' + part, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = list(re.finditer(r'\"\"\"', content))
    print(f'{part}: {len(matches)} occurrences of triple quotes')
    if len(matches) > 2:
        # The first and last are the string delimiters
        # Any in-between should be replaced with single quotes or escaped
        print(f"  Fixing inner triple quotes in {part}...")
        prefix = content[:matches[0].end()]
        suffix = content[matches[-1].start():]
        middle = content[matches[0].end():matches[-1].start()]
        # Replace triple quotes in middle with escaped or hash comments
        middle_fixed = re.sub(r'\"\"\"(.*?)\"\"\"', r'# \1', middle, flags=re.DOTALL)
        # Any stray remaining \"\"\"
        middle_fixed = middle_fixed.replace('"""', "'''")
        new_content = prefix + middle_fixed + suffix
        with open('scratch/' + part, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Saved fixed {part}")
