# Fix remaining latex fragments in all topic19 files
import glob
import re

def clean_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    text = re.sub(r'\\mathbf\{([^}]+)\}', r'<strong>\1</strong>', text)
    text = text.replace(r'\mathbf', '')
    text = text.replace(r'\cdot', '&times;')
    text = text.replace(r'\le', '&le;')
    text = text.replace(r'\ge', '&ge;')
    text = text.replace(r'\sqrt', '&radic;')
    text = text.replace(r'\%', '%')
    text = text.replace(r'\k', 'k')
    text = text.replace(r'\tau', '&tau;')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Cleaned {path}")

for p in glob.glob('scratch/topic19_part*.py') + ['coding/machine_learning/topic_19/notes.html']:
    clean_file(p)

# Re-assemble notes.html to be completely sure
import topic19_assemble
topic19_assemble.assemble_notes()
clean_file('coding/machine_learning/topic_19/notes.html')
print("Complete cleaning finished!")
