"""
Topic 14: Naive Bayes - Automated Playwright QA
Captures Desktop (1280x800) and Mobile (390x844) screenshots.
Verifies 0 console errors, 0 page errors, and hasOverflow: False on mobile.
"""

import os
from playwright.sync_api import sync_playwright

EVIDENCE_DIR = os.path.abspath("qa_evidence/machine_learning")
os.makedirs(EVIDENCE_DIR, exist_ok=True)

TARGET_HTML = os.path.abspath("coding/machine_learning/topic_14/notes.html")
TARGET_URL = f"file:///{TARGET_HTML.replace(os.sep, '/')}"

def run_qa():
    console_errors = []
    page_errors = []

    with sync_playwright() as p:
        # =========================================================
        # 1. Desktop QA (1280x800)
        # =========================================================
        print(f"=== 1. Starting Desktop QA at 1280x800 ===")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: page_errors.append(str(err)))

        print(f"Loading {TARGET_URL}...")
        page.goto(TARGET_URL, wait_until="networkidle")

        title = page.title()
        print(f"Page Title: {title}")
        assert "Topic 14: Naive Bayes" in title, f"Unexpected page title: {title}"

        # Verify SVGs
        svg_count = page.locator("svg").count()
        print(f"Rendered SVGs: {svg_count}")
        assert svg_count >= 15, f"Expected at least 15 SVGs, found {svg_count}"

        # Capture Full Desktop Page
        desktop_full_path = os.path.join(EVIDENCE_DIR, "ml_topic_14_light_desktop.png")
        page.screenshot(path=desktop_full_path, full_page=True)
        print(f"Captured Desktop Full Page: {desktop_full_path}")

        # Capture Selected Major Sections
        sections_to_capture = [
            ("sec-01", "ml_topic_14_sec01_intro.png"),
            ("sec-02", "ml_topic_14_sec02_priors.png"),
            ("sec-03", "ml_topic_14_sec03_contingency.png"),
            ("sec-04", "ml_topic_14_sec04_bayes_theorem.png"),
            ("sec-05", "ml_topic_14_sec05_likelihoods.png"),
            ("sec-07", "ml_topic_14_sec07_independence.png"),
            ("sec-08", "ml_topic_14_sec08_step_by_step.png"),
            ("sec-09", "ml_topic_14_sec09_zero_frequency.png"),
            ("sec-10", "ml_topic_14_sec10_laplace_smoothing.png"),
            ("sec-11", "ml_topic_14_sec11_variants.png"),
            ("sec-12", "ml_topic_14_sec12_visual_matrices.png"),
            ("sec-13", "ml_topic_14_sec13_spam_lab.png"),
            ("sec-14", "ml_topic_14_sec14_gaussian_lab.png"),
            ("sec-15", "ml_topic_14_sec15_probabilities.png"),
            ("sec-16", "ml_topic_14_sec16_evaluation.png"),
            ("sec-20", "ml_topic_14_sec20_mistakes.png"),
            ("sec-23", "ml_topic_14_sec23_accordions.png"),
        ]

        for sec_id, out_name in sections_to_capture:
            loc = page.locator(f"#{sec_id}")
            if loc.count() > 0:
                out_path = os.path.join(EVIDENCE_DIR, out_name)
                loc.screenshot(path=out_path)
                print(f"Captured #{sec_id} -> {out_path}")
            else:
                print(f"WARNING: #{sec_id} not found!")

        browser.close()

        # =========================================================
        # 2. Mobile QA (390x844 - iPhone 12/13/14 viewport)
        # =========================================================
        print(f"\n=== 2. Starting Mobile QA at 390x844 ===")
        browser_m = p.chromium.launch(headless=True)
        context_m = browser_m.new_context(
            viewport={"width": 390, "height": 844},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
        )
        page_m = context_m.new_page()

        page_m.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page_m.on("pageerror", lambda err: page_errors.append(str(err)))

        page_m.goto(TARGET_URL, wait_until="networkidle")

        # Check for Horizontal Overflow
        overflow_diagnostics = page_m.evaluate("""() => {
            const docWidth = document.documentElement.scrollWidth;
            const clientWidth = document.documentElement.clientWidth;
            const bodyWidth = document.body.scrollWidth;
            const winWidth = window.innerWidth;
            return {
                scrollWidth: docWidth,
                clientWidth: clientWidth,
                bodyScrollWidth: bodyWidth,
                windowWidth: winWidth,
                hasOverflow: docWidth > clientWidth || bodyWidth > winWidth
            };
        }""")
        print(f"Mobile Overflow Diagnostics: {overflow_diagnostics}")
        assert not overflow_diagnostics["hasOverflow"], f"Mobile horizontal overflow detected: {overflow_diagnostics}"

        # Capture Full Mobile Page
        mobile_full_path = os.path.join(EVIDENCE_DIR, "ml_topic_14_light_mobile.png")
        page_m.screenshot(path=mobile_full_path, full_page=True)
        print(f"Captured Mobile Full Page: {mobile_full_path}")

        # Capture Mobile Hero Viewport
        mobile_hero_path = os.path.join(EVIDENCE_DIR, "ml_topic_14_mobile_hero.png")
        page_m.screenshot(path=mobile_hero_path, full_page=False)
        print(f"Captured Mobile Viewport: {mobile_hero_path}")

        # Scroll to Section 13 and capture Mobile Lab Viewport
        page_m.locator("#sec-13").scroll_into_view_if_needed()
        page_m.wait_for_timeout(300)
        mobile_lab_path = os.path.join(EVIDENCE_DIR, "ml_topic_14_mobile_lab.png")
        page_m.screenshot(path=mobile_lab_path, full_page=False)
        print(f"Captured Mobile Lab Viewport: {mobile_lab_path}")

        # Test Interactive Accordion Expansion
        accordion_summary = page_m.locator("details summary").first
        if accordion_summary.count() > 0:
            accordion_summary.click()
            page_m.wait_for_timeout(200)
            is_open = page_m.locator("details").first.get_attribute("open") is not None
            print(f"Interactive Accordion Expanded: {is_open}")
            assert is_open, "Accordion failed to expand upon click!"

        browser_m.close()

        # =========================================================
        # 3. Console & Page Errors Verification
        # =========================================================
        print(f"\n=== 3. Error Verification ===")
        print(f"Console Errors: {len(console_errors)}")
        if console_errors:
            for err in console_errors:
                print(f"  Console Error: {err}")
        print(f"Page Errors: {len(page_errors)}")
        if page_errors:
            for err in page_errors:
                print(f"  Page Error: {err}")

        assert len(console_errors) == 0, f"Found console errors: {console_errors}"
        assert len(page_errors) == 0, f"Found page errors: {page_errors}"

        print("\nALL DESKTOP & MOBILE QA CHECKS PASSED WITH ZERO ERRORS!")

if __name__ == "__main__":
    run_qa()
