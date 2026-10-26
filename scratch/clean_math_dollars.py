# Script to remove stray dollar signs around non-currency text
import re
import glob

def clean_dollars(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Specific cleanups
    text = text.replace('Accuracy$.', 'Accuracy.')
    text = text.replace('MAE$).', 'MAE).')
    text = text.replace('MAE$', 'MAE')
    text = text.replace('P$)', 'P)')
    text = text.replace('K$ > 2', 'K &gt; 2')
    text = text.replace('K$', 'K')
    text = text.replace('|e|$).', '|e|).')
    text = text.replace('FP,$', 'FP,')
    text = text.replace('F<sub>&beta;</sub>$', 'F<sub>&beta;</sub>')
    text = text.replace('(SS<sub>res</sub>$)', '(SS<sub>res</sub>)')
    text = text.replace('(SS<sub>tot</sub>$),', '(SS<sub>tot</sub>),')
    text = text.replace('SS<sub>tot</sub>$', 'SS<sub>tot</sub>')
    text = text.replace('SS<sub>res</sub>$', 'SS<sub>res</sub>')
    text = text.replace('$(P', '(P')
    text = text.replace('$(TP', '(TP')
    text = text.replace('$(SS_res', '(SS_res')
    text = text.replace('$(y<sub>i</sub>', '(y<sub>i</sub>')
    text = text.replace('$(y_i', '(y_i')

    # General regex cleanup: remove $ before ( or after ) or after tags
    text = re.sub(r'\$\(([^)]+)\)', r'(\1)', text)
    text = re.sub(r'([a-zA-Z0-9_>])\$', r'\1', text)
    text = re.sub(r'\$([a-zA-Z_])', r'\1', text)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Cleaned", path)

for p in glob.glob('scratch/topic19_part*.py') + ['coding/machine_learning/topic_19/notes.html']:
    clean_dollars(p)

import sys
sys.path.append('scratch')
import topic19_assemble
topic19_assemble.assemble_notes()
clean_dollars('coding/machine_learning/topic_19/notes.html')
print("Finished cleaning math dollars!")
