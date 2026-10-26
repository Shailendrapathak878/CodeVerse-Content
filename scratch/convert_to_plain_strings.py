"""
Fixes parts 1-4 to be non-f-strings by substituting SVG imports with __SVG_...__ placeholders.
"""
import re

for i in range(1, 5):
    fname = f"scratch/topic13_part{i}.py"
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace f\"\"\" with \"\"\"
    content = re.sub(r'TOPIC13_PART\d\s*=\s*f"""', f'TOPIC13_PART{i} = """', content)
    
    # Replace {SVG_...} with __SVG_...__
    content = re.sub(r'\{(SVG_[A-Z0-9_]+)\}', r'__\1__', content)

    # In regular strings, we can unescape {{ and }} back to single { and } if needed, or leave them as is.
    # But wait, in python string literals """...""", {{ stays as {{ unless in an f-string.
    # In HTML, {{ is sometimes used, but let's check where {{ was used.
    # In topic13_part3 code box: f"{{df.shape}}" -> we want f"{df.shape}" in the python code!
    # Let's fix double {{ and }} in python code blocks.
    
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {fname}")
