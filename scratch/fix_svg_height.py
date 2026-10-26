import re

def fix():
    for path in ['scratch/topic16_svgs.py', 'coding/machine_learning/topic_16/notes.html']:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = re.sub(r'\s*height=[\"\']auto[\"\']', '', content)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Fixed {path}: before len {len(content)}, after len {len(new_content)}")

if __name__ == '__main__':
    fix()
