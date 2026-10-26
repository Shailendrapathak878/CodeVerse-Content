"""
Cleans double braces {{ and }} in plain strings across parts 1-4.
"""
for i in range(1, 5):
    fname = f"scratch/topic13_part{i}.py"
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace {{ with { and }} with }
    content = content.replace("{{", "{").replace("}}", "}")

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cleaned braces in {fname}")
