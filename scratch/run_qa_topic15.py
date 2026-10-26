"""
Topic 15: Ensemble Learning - Automated Playwright QA
Captures Desktop (1280x800) and Mobile (390x844) screenshots.
Verifies 0 console errors, 0 page errors, and hasOverflow: False on mobile.
"""

import os
from playwright.sync_api import sync_playwright

EVIDENCE_DIR = os.path.abspath("qa_evidence/machine_learning")
os.makedirs(EVIDENCE_DIR, exist_ok=True)

TARGET_HTML = os.path.abspath("coding/machine_learning/topic_15/notes.html")
TARGET_URL = f"file:///{TARGET_HTML.replace(os.sep, '/')}"

def run_qa():
    console_errors = []
    page_errors = []

    with sync_playwright() as p:
        # =========================================================
        # 1. Desktop QA (1280x800)
        # =========================================================
        print("=== 1. Starting Desktop QA at 1280x800 ===")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: page_errors.append(str(err)))

        print(f"Loading {TARGET_URL}...")
        page.goto(TARGET_URL, wait_until="networkidle")

        title = page.title()
        print(f"Page Title: {title}")
        assert "Topic 15: Ensemble Learning" in title, f"Unexpected page title: {title}"

        # Verify SVGs
        svg_count = page.locator("svg").count()
        print(f"Rendered SVGs: {svg_count}")
        assert svg_count >= 17, f"Expected at least 17 SVGs, found {svg_count}"

        # Capture Full Desktop Page
        desktop_full_path = os.path.join(EVIDENCE_DIR, "ml_topic_15_light_desktop.png")
        page.screenshot(path=desktop_full_path, full_page=True)
        print(f"Captured Desktop Full Page: {desktop_full_path}")

        # Capture Selected Major Sections
        sections_to_capture = [
            ("sec-01", "ml_topic_15_sec01_intro.png"),
            ("sec-03", "ml_topic_15_sec03_single_vs_ensemble.png"),
            ("sec-04", "ml_topic_15_sec04_voting.png"),
            ("sec-06", "ml_topic_15_sec06_bagging_bootstrap.png"),
            ("sec-07", "ml_topic_15_sec07_bagging_classifier.png"),
            ("sec-08", "ml_topic_15_sec08_random_forest.png"),
            ("sec-09", "ml_topic_15_sec09_rf_visualizations.png"),
            ("sec-11", "ml_topic_15_sec11_boosting_core.png"),
            ("sec-12", "ml_topic_15_sec12_adaboost.png"),
            ("sec-13", "ml_topic_15_sec13_gradient_boosting.png"),
            ("sec-14", "ml_topic_15_sec14_learning_rate.png"),
            ("sec-15", "ml_topic_15_sec15_xgboost.png"),
            ("sec-16", "ml_topic_15_sec16_stacking.png"),
            ("sec-17", "ml_topic_15_sec17_master_comparison.png"),
            ("sec-18", "ml_topic_15_sec18_classification_lab.png"),
            ("sec-19", "ml_topic_15_sec19_regression_lab.png"),
            ("sec-21", "ml_topic_15_sec21_overfitting.png"),
            ("sec-22", "ml_topic_15_sec22_feature_importance.png"),
            ("sec-24", "ml_topic_15_sec24_mistakes.png"),
            ("sec-27", "ml_topic_15_sec27_accordions.png"),
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
        print("\n=== 2. Starting Mobile QA at 390x844 ===")
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
        mobile_full_path = os.path.join(EVIDENCE_DIR, "ml_topic_15_light_mobile.png")
        page_m.screenshot(path=mobile_full_path, full_page=True)
        print(f"Captured Mobile Full Page: {mobile_full_path}")

        # Capture Mobile Hero Viewport
        mobile_hero_path = os.path.join(EVIDENCE_DIR, "ml_topic_15_mobile_hero.png")
        page_m.screenshot(path=mobile_hero_path, full_page=False)
        print(f"Captured Mobile Viewport: {mobile_hero_path}")

        # Scroll to Section 18 and capture Mobile Classification Lab Viewport
        page_m.locator("#sec-18").scroll_into_view_if_needed()
        page_m.wait_for_timeout(300)
        mobile_lab_path = os.path.join(EVIDENCE_DIR, "ml_topic_15_mobile_lab.png")
        page_m.screenshot(path=mobile_lab_path, full_page=False)
        print(f"Captured Mobile Lab Viewport: {mobile_lab_path}")

        # Scroll to Section 24 and capture Mobile Mistakes Viewport
        page_m.locator("#sec-24").scroll_into_view_if_needed()
        page_m.wait_for_timeout(300)
        mobile_mistakes_path = os.path.join(EVIDENCE_DIR, "ml_topic_15_mobile_mistakes.png")
        page_m.screenshot(path=mobile_mistakes_path, full_page=False)
        print(f"Captured Mobile Mistakes Viewport: {mobile_mistakes_path}")

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
        print("\n=== 3. Error Verification ===")
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
