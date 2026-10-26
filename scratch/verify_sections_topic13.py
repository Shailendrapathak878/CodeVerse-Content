import re

content = open('coding/machine_learning/topic_13/notes.html', encoding='utf-8').read()
sec_ids = sorted(re.findall(r'id="(sec-\d+)"', content))
print(f"Total section IDs found: {len(sec_ids)}")
print(f"IDs: {sec_ids}")
assert len(sec_ids) == 23, f"Expected 23 sections, found {len(sec_ids)}"
for i in range(1, 24):
    expected = f"sec-{i:02d}"
    assert expected in sec_ids, f"Missing section {expected}!"
print("ALL 23 SECTIONS CONFIRMED (sec-01 to sec-23)!")

# Check for unrendered SVG placeholders
unrendered = re.findall(r'__SVG_[A-Z0-9_]+__', content)
print(f"Unrendered SVG placeholders: {len(unrendered)}")
assert len(unrendered) == 0, f"Found unrendered placeholders: {unrendered}"

# Count SVGs
svg_tags = re.findall(r'<svg\b', content)
print(f"Embedded SVG count: {len(svg_tags)}")
assert len(svg_tags) == 15, f"Expected 15 SVGs, found {len(svg_tags)}"

# Check Light Mode: ensure no dark theme or media (prefers-color-scheme: dark)
assert "@media (prefers-color-scheme: dark)" not in content, "Found dark mode media query!"
assert "dark-theme" not in content, "Found dark-theme class!"

print("EVERY STRUCTURAL CHECK PASSED CLEANLY!")
