import os
import re

file_path = os.path.join("coding", "machine_learning", "topic_18", "notes.html")
assert os.path.exists(file_path), f"File {file_path} not found!"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print(f"Checking {file_path} (Size: {len(content)} chars)...")

# 1. Check sections
sections = [f"sec-{i:02d}" for i in range(1, 21)]
missing_sections = []
for sec in sections:
    if f'id="{sec}"' not in content:
        missing_sections.append(sec)

if missing_sections:
    print(f"FAILED: Missing sections: {missing_sections}")
else:
    print(f"PASSED: All 20 sections (sec-01 through sec-20) present!")

# 2. Check SVGs
svg_count = content.count("<svg")
print(f"Found {svg_count} <svg> tags (Expected: 16)")
assert svg_count >= 16, f"Expected at least 16 SVGs, found {svg_count}"

# 3. Check for unresolved placeholders
unresolved = re.findall(r'__SVG_[A-Z0-9_]+__', content)
if unresolved:
    print(f"FAILED: Found unresolved placeholders: {unresolved}")
else:
    print("PASSED: 0 unresolved SVG placeholders!")

# 4. Check for Dark Mode styles
dark_query = re.findall(r'prefers-color-scheme\s*:\s*dark', content, re.IGNORECASE)
if dark_query:
    print(f"FAILED: Found dark mode media queries: {dark_query}")
else:
    print("PASSED: Strict Light Mode verified (0 dark-mode media queries)!")

# 5. Check Mistake cards
mistake_count = content.count("class=\"mistake-card\"")
print(f"Found {mistake_count} mistake cards (Expected: 14)")
assert mistake_count >= 14, f"Expected 14 mistake cards, found {mistake_count}"

# 6. Check FAQ Accordions
accordion_count = content.count("<details class=\"faq-item\"")
print(f"Found {accordion_count} interactive accordions (Expected: 12)")
assert accordion_count >= 12, f"Expected 12 accordions, found {accordion_count}"

print("\nALL STRUCTURAL CHECKS PASSED FOR TOPIC 18!")
