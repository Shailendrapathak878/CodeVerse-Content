"""
Fixes all LaTeX backslashes in parts 1-4 with clean, beautiful HTML math representations.
"""

def fix_part1():
    with open("scratch/topic13_part1.py", "r", encoding="utf-8") as f:
        content = f.read()

    old_sec3_math = """    <div class="math-display" style="font-size: 1.1rem;">
      \\text{Distance} = \\frac{|wᵀx₀ + b|}{∥w∥}
    </div>
    <p>
      Since points on the positive margin boundary satisfy <code>wᵀx + b = +1</code>, their perpendicular distance to the decision hyperplane is:
    </p>
    <div class="math-display" style="font-size: 1.1rem;">
      d_+ = \\frac{|+1|}{∥w∥} = \\frac{1}{∥w∥}
    </div>
    <p>
      Similarly, points on the negative margin boundary satisfy <code>wᵀx + b = -1</code>, and their distance to the decision line is:
    </p>
    <div class="math-display" style="font-size: 1.1rem;">
      d_- = \\frac{|-1|}{∥w∥} = \\frac{1}{∥w∥}
    </div>
    <p>
      Adding these two symmetrical distances together yields the total margin width <code>M</code>:
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; Total Margin Width Formula</div>
      <div class="math-display">\\text{Margin Width} = d_+ + d_- = \\frac{1}{∥w∥} + \\frac{1}{∥w∥} = \\frac{2}{∥w∥}</div>"""

    # Because in memory \t was tab and \f was form feed, let's replace by targeted block
    import re
    # Match the block in Section 3
    pattern = r'<div class="math-display" style="font-size: 1\.1rem;">[\s\S]*?<div class="formula-header">&#128290; Total Margin Width Formula</div>\s*<div class="math-display">[\s\S]*?</div>'
    replacement = """<div class="math-display" style="font-size: 1.1rem;">
      Distance = |wᵀx₀ + b| / ∥w∥
    </div>
    <p>
      Since points on the positive margin boundary satisfy <code>wᵀx + b = +1</code>, their perpendicular distance to the decision hyperplane is:
    </p>
    <div class="math-display" style="font-size: 1.1rem;">
      d₊ = |+1| / ∥w∥ = 1 / ∥w∥
    </div>
    <p>
      Similarly, points on the negative margin boundary satisfy <code>wᵀx + b = -1</code>, and their distance to the decision line is:
    </p>
    <div class="math-display" style="font-size: 1.1rem;">
      d₋ = |-1| / ∥w∥ = 1 / ∥w∥
    </div>
    <p>
      Adding these two symmetrical distances together yields the total margin width <code>M</code>:
    </p>

    <div class="formula-block">
      <div class="formula-header">&#128290; Total Margin Width Formula</div>
      <div class="math-display">Total Margin Width (M) = d₊ + d₋ = (1 / ∥w∥) + (1 / ∥w∥) = 2 / ∥w∥</div>"""

    content = re.sub(pattern, replacement, content)
    with open("scratch/topic13_part1.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed part 1 math display.")

def fix_part2():
    with open("scratch/topic13_part2.py", "r", encoding="utf-8") as f:
        content = f.read()

    # In section 10:
    content = content.replace("K(x, z) = xᵀz \\quad \\text{(Linear Kernel)}", "K(x, z) = xᵀz &nbsp;&nbsp;&nbsp;&nbsp; (Linear Kernel)")
    content = content.replace("K(x, z) = (\\gamma xᵀz + r)^d \\quad \\text{(Polynomial Kernel)}", "K(x, z) = (γ xᵀz + r)ᵈ &nbsp;&nbsp;&nbsp;&nbsp; (Polynomial Kernel)")
    content = content.replace("K(x, z) = \\exp(-\\gamma ∥x - z∥²) \\quad \\text{(Radial Basis Function / RBF Kernel)}", "K(x, z) = exp( -γ ∥x - z∥² ) &nbsp;&nbsp;&nbsp;&nbsp; (RBF Kernel)")

    with open("scratch/topic13_part2.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed part 2 math display.")

def fix_part3():
    with open("scratch/topic13_part3.py", "r", encoding="utf-8") as f:
        content = f.read()

    import re
    # Section 12 formula
    pattern = r'<div class="formula-header">&#128290; The Role of Gamma in the RBF Kernel</div>\s*<div class="math-display">[\s\S]*?</div>'
    replacement = """<div class="formula-header">&#128290; The Role of Gamma in the RBF Kernel</div>
      <div class="math-display">K(x, z) = exp( -γ ∥x - z∥² ) = exp( - ∥x - z∥² / (2σ²) )</div>"""
    content = re.sub(pattern, replacement, content)

    # Section 13 standardization
    pattern_std = r'<div class="formula-header">&#128290; Z-Score Feature Standardization</div>\s*<div class="math-display">[\s\S]*?</div>'
    replacement_std = """<div class="formula-header">&#128290; Z-Score Feature Standardization</div>
      <div class="math-display">z = (x - μ) / σ</div>"""
    content = re.sub(pattern_std, replacement_std, content)

    with open("scratch/topic13_part3.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed part 3 math display.")

def fix_part4():
    with open("scratch/topic13_part4.py", "r", encoding="utf-8") as f:
        content = f.read()

    import re
    # Section 16 SVR loss
    pattern_svr = r'<div class="formula-header">&#128290; The Epsilon-Insensitive Loss Function</div>\s*<div class="math-display">[\s\S]*?</div>'
    replacement_svr = """<div class="formula-header">&#128290; The Epsilon-Insensitive Loss Function</div>
      <div class="math-display">L_ε(y, f(x)) = 0 &nbsp; if |y - f(x)| ≤ ε &nbsp;&nbsp;|&nbsp;&nbsp; |y - f(x)| - ε &nbsp; if |y - f(x)| > ε</div>"""
    content = re.sub(pattern_svr, replacement_svr, content)

    # Section 17 metrics formulas
    # Accuracy
    content = re.sub(
        r'<div class="math-display">\\text\{Acc\} = \\frac\{TP \+ TN\}\{TP \+ TN \+ FP \+ FN\} = \\frac\{23 \+ 21\}\{48\} = \\mathbf\{91\.67\%\}</div>',
        '<div class="math-display">Accuracy = (TP + TN) / (TP + TN + FP + FN) = (23 + 21) / 48 = 91.67%</div>',
        content
    )
    # Precision
    content = re.sub(
        r'<div class="math-display">\\text\{Prec\} = \\frac\{TP\}\{TP \+ FP\} = \\frac\{23\}\{23 \+ 3\} = \\frac\{23\}\{26\} = \\mathbf\{88\.46\%\}</div>',
        '<div class="math-display">Precision = TP / (TP + FP) = 23 / (23 + 3) = 23 / 26 = 88.46%</div>',
        content
    )
    # Recall
    content = re.sub(
        r'<div class="math-display">\\text\{Rec\} = \\frac\{TP\}\{TP \+ FN\} = \\frac\{23\}\{23 \+ 1\} = \\frac\{23\}\{24\} = \\mathbf\{95\.83\%\}</div>',
        '<div class="math-display">Recall = TP / (TP + FN) = 23 / (23 + 1) = 23 / 24 = 95.83%</div>',
        content
    )
    # F1-Score
    content = re.sub(
        r'<div class="math-display">F_1 = 2 \\cdot \\frac\{\\text\{Prec\} \\cdot \\text\{Rec\}\}\{\\text\{Prec\} \+ \\text\{Rec\}\} = 2 \\cdot \\frac\{0\.8846 \\cdot 0\.9583\}\{0\.8846 \+ 0\.9583\} = \\mathbf\{92\.00\%\}</div>',
        '<div class="math-display">F1-Score = 2 × (Precision × Recall) / (Precision + Recall) = 92.00%</div>',
        content
    )

    with open("scratch/topic13_part4.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed part 4 math display.")

if __name__ == "__main__":
    fix_part1()
    fix_part2()
    fix_part3()
    fix_part4()
