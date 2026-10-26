import os
import re
import sys

# Set standard output encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')

html_path = os.path.join("coding", "machine_learning", "topic_24", "notes.html")
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

print("=" * 60)
print(f"VERIFYING {html_path}")
print("=" * 60)

# 1. Unresolved placeholders
placeholders = re.findall(r"__[A-Z0-9_]+__", content)
print(f"1. Unresolved placeholders: {placeholders}")
assert len(placeholders) == 0, f"Found unresolved placeholders: {placeholders}"

# 2. Check for height="auto" in SVGs
bad_svg_height = re.findall(r'<svg[^>]*height=["\']auto["\']', content, re.IGNORECASE)
print(f"2. SVGs with height='auto': {len(bad_svg_height)}")
assert len(bad_svg_height) == 0, f"Found {len(bad_svg_height)} bad SVGs"

# 3. Verify all 21 section IDs
missing_secs = []
for i in range(1, 22):
    sec_id = f"sec-{i:02d}"
    if f'id="{sec_id}"' not in content:
        missing_secs.append(sec_id)
print(f"3. Missing section IDs: {missing_secs}")
assert len(missing_secs) == 0, f"Missing sections: {missing_secs}"

# 4. Check SVG count
svg_count = content.count("<svg")
print(f"4. Total <svg> tags: {svg_count}")
assert svg_count >= 20, f"Expected at least 20 SVGs, got {svg_count}"

# 5. Check interactive calculator and accordion
has_calc = "updateServingEstimates" in content
has_accordion = "<details class=\"interactive-accordion\"" in content
has_banner = "Congratulations! You've Completed Machine Learning Fundamentals" in content
print(f"5. Interactive Calculator present: {has_calc}")
print(f"   Accordion present: {has_accordion}")
print(f"   Completion Banner present: {has_banner}")

print("\nALL SANITY CHECKS PASSED!")
