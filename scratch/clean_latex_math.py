# Script to systematically clean raw LaTeX from topic19_part1.py, part2.py, part3.py, part4.py

import os

def clean_part(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    replacements = [
        # Common LaTeX commands
        (r'\frac{TP}{TP + FN}', 'TP / (TP + FN)'),
        (r'\frac{FP}{FP + TN}', 'FP / (FP + TN)'),
        (r'\frac{FP}{TN + FP}', 'FP / (TN + FP)'),
        (r'\frac{TP}{TP + FP}', 'TP / (TP + FP)'),
        (r'\frac{TN}{TN + FP}', 'TN / (TN + FP)'),
        (r'\frac{FN}{FN + TP}', 'FN / (FN + TP)'),
        (r'\frac{P \cdot R}{P + R}', '(P &times; R) / (P + R)'),
        (r'\frac{\sum TP}{\sum TP + \sum FP}', '&sum; TP / (&sum; TP + &sum; FP)'),
        (r'\frac{SS_{\text{res}}}{SS_{\text{tot}}}', '(SS_res / SS_tot)'),
        (r'\frac{SS_{res}}{SS_{tot}}', '(SS_res / SS_tot)'),
        (r'\text{ROC-AUC} = 0.9200', 'ROC-AUC = 0.9200'),
        (r'\text{ROC-AUC}', 'ROC-AUC'),
        (r'\text{Total Cost} = c_{FP} \cdot FP + c_{FN} \cdot FN', 'Total Cost = (c_FP &times; FP) + (c_FN &times; FN)'),
        (r'\text{Total Correct}', 'Total Correct'),
        (r'\text{Total Samples}', 'Total Samples'),
        (r'\text{Accuracy}', 'Accuracy'),
        (r'SS_{\text{res}}', 'SS<sub>res</sub>'),
        (r'SS_{\text{tot}}', 'SS<sub>tot</sub>'),
        (r'\mathbf{0.9766}', '<strong>0.9766</strong>'),
        (r'\mathbf{0.9813}', '<strong>0.9813</strong>'),
        (r'\mathbf{0.9688}', '<strong>0.9688</strong>'),
        (r'\mathbf{0.9971}', '<strong>0.9971</strong>'),
        (r'\mathbf{0.9984}', '<strong>0.9984</strong>'),
        (r'\mathbf{\$11.96k}', '<strong>$11.96k</strong>'),
        (r'\mathbf{223.14}', '<strong>223.14</strong>'),
        (r'\mathbf{\$14.94k}', '<strong>$14.94k</strong>'),
        (r'\mathbf{0.9238}', '<strong>0.9238</strong>'),
        (r'\sqrt{223.14}', '&radic;(223.14)'),
        (r'R^2 = 0.90', 'R&sup2; = 0.90'),
        (r'R^2 < 0', 'R&sup2; &lt; 0'),
        (r'R^2 = 1', 'R&sup2; = 1'),
        (r'R^2 = 0', 'R&sup2; = 0'),
        (r'R^2', 'R&sup2;'),
        (r'F_\beta', 'F<sub>&beta;</sub>'),
        (r'F_1', 'F1'),
        (r'RMSE \ge MAE', 'RMSE &ge; MAE'),
        (r'P(y=1|X) = 0.82', 'P(y=1|X) = 0.82'),
        (r'P(y=1|X) \ge 0.50', 'P(y=1|X) &ge; 0.50'),
        (r'P(y=1|x) \ge 0.50', 'P(y=1|x) &ge; 0.50'),
        (r'P(y=1|X)', 'P(y=1|X)'),
        (r'P(y=1|x)', 'P(y=1|x)'),
        (r'TP, FP,', 'TP, FP,'),
        (r'FN = 0', 'FN = 0'),
        (r'FN', 'FN'),
        (r'FP', 'FP'),
        (r'TN', 'TN'),
        (r'TP', 'TP'),
        (r'P / (P + N)', 'P / (P + N)'),
        (r'K > 2', 'K &gt; 2'),
        (r'e_i = y_i - \hat{y}_i', 'e<sub>i</sub> = y<sub>i</sub> &minus; &#375;<sub>i</sub>'),
        (r'e_i = y_i - &#375;_i', 'e<sub>i</sub> = y<sub>i</sub> &minus; &#375;<sub>i</sub>'),
        (r'e_i > 0', 'e<sub>i</sub> &gt; 0'),
        (r'e_i < 0', 'e<sub>i</sub> &lt; 0'),
        (r'e_i = 0', 'e<sub>i</sub> = 0'),
        (r'e_1 = -20,000', 'e<sub>1</sub> = -$20,000'),
        (r'e_2 = +20,000', 'e<sub>2</sub> = +$20,000'),
        (r'|e|', '|e|'),
        (r'e^2', 'e&sup2;'),
        (r'y = |e|', 'y = |e|'),
        (r'y = e^2', 'y = e&sup2;'),
        (r'y_i', 'y<sub>i</sub>'),
        (r'&#375;_i', '&#375;<sub>i</sub>'),
        (r'\hat{y}_i', '&#375;<sub>i</sub>'),
        (r'\bar{y} = 300', 'y&#772; = 300'),
        (r'1 - P', '1 &minus; P'),
    ]

    for old, new in replacements:
        text = text.replace(old, new)

    # Clean leftover single-character $ wrappers like $i$, $n$, $y$, $X$
    single_var_maps = [
        ('$i$', '<em>i</em>'),
        ('$n$', '<em>n</em>'),
        ('$y$', '<em>y</em>'),
        ('$X$', '<em>X</em>'),
        ('$e$', '<em>e</em>'),
        ('$K$', '<em>K</em>'),
        ('$N$', '<em>N</em>'),
        ('$P$', '<em>P</em>'),
        ('$R$', '<em>R</em>'),
        ('$n = 5$', '<em>n</em> = 5'),
        ('$TP$', 'TP'),
        ('$FP$', 'FP'),
        ('$TN$', 'TN'),
        ('$FN$', 'FN'),
    ]
    for old, new in single_var_maps:
        text = text.replace(old, new)

    # Clean up double dollars or stray $ around math identifiers without deleting currency
    import re
    # Remove $ when wrapped around non-digits, e.g. $TPR$, $FPR$, $TP$
    text = re.sub(r'\$([a-zA-Z_\\^&;{}]+)\$', r'\1', text)
    text = re.sub(r'\$([a-zA-Z_\\^&;{}]+)', r'\1', text)
    text = text.replace('TPR = TP / (TP + FN)', 'TPR = TP / (TP + FN)')
    text = text.replace('FPR = FP / (FP + TN)', 'FPR = FP / (FP + TN)')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Cleaned {file_path}")

for part in ['scratch/topic19_part1.py', 'scratch/topic19_part2.py', 'scratch/topic19_part3.py', 'scratch/topic19_part4.py']:
    clean_part(part)

print("All parts cleaned successfully!")
