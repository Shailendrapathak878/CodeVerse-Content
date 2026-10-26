# Verification script for Topic 19 notes.html
import re

with open("coding/machine_learning/topic_19/notes.html", "r", encoding="utf-8") as f:
    html = f.read()

print("=== TOPIC 19 STRUCTURAL VERIFICATION ===")

# 1. Check sections 01 to 27
sections = [f"sec-{i:02d}" for i in range(1, 28)]
missing_sections = []
for sec in sections:
    if f'id="{sec}"' not in html:
        missing_sections.append(sec)

if missing_sections:
    print(f"FAILED: Missing sections: {missing_sections}")
else:
    print(f"PASSED: All 27 sections present (sec-01 to sec-27)!")

# 2. Check SVGs count
svg_count = html.count("<svg")
print(f"SVG tags count: {svg_count} (Expected at least 17)")
if svg_count >= 17:
    print("PASSED: SVG count check passed!")
else:
    print("FAILED: Insufficient SVGs!")

# 3. Check for lingering placeholders
placeholders = re.findall(r"__SVG_[A-Z0-9_]+__", html)
if placeholders:
    print(f"FAILED: Lingering placeholders found: {placeholders}")
else:
    print("PASSED: Zero lingering placeholders found!")

# 4. Check Strict Light Mode
if "prefers-color-scheme: dark" in html or "dark-mode" in html:
    print("FAILED: Dark mode styling found!")
else:
    print("PASSED: Strict Light Mode confirmed (No dark-mode CSS or media queries)!")

# 5. Check Mistake Cards
mistake_count = html.count("class=\"mistake-card\"")
print(f"Mistake cards count: {mistake_count} (Expected 14)")
if mistake_count >= 14:
    print("PASSED: 14 Common Mistake cards verified!")
else:
    print("FAILED: Missing mistake cards!")

# 6. Check Self-Check FAQ Accordions
faq_count = html.count("class=\"faq-item\"")
print(f"Self-check FAQ accordions count: {faq_count} (Expected 12)")
if faq_count >= 12:
    print("PASSED: 12 Self-Check FAQ accordions verified!")
else:
    print("FAILED: Missing FAQ items!")

# 7. Check Practical Section Workflows
has_clf_workflow = "CLASSIFICATION METRICS REPORT" in html
has_reg_workflow = "REGRESSION METRICS REPORT" in html
print(f"Workflow A (Classification): {'PASSED' if has_clf_workflow else 'FAILED'}")
print(f"Workflow B (Regression):     {'PASSED' if has_reg_workflow else 'FAILED'}")

# 8. Check for any non-currency dollar signs
dollar_tokens = set(re.findall(r"\S*\$\S*", html))
non_currency = [t for t in dollar_tokens if not any(c.isdigit() for c in t) and t not in ["$", "$k", "$k^2", "$k²", "($k)", "($k²)", "($k^2)", "(e.g.,", "$)", "$)</td>", "($)</text>"]]
if non_currency:
    print(f"WARNING: Suspicious non-currency dollar tokens: {non_currency}")
else:
    print("PASSED: Zero suspicious non-currency dollar tokens!")

print("=== VERIFICATION COMPLETE ===")

