"""Topic 17: Dimensionality Reduction - Automated Playwright QA
Captures Desktop (1280x800) and Mobile (390x844) screenshots.
Verifies 0 console errors, 0 page errors, and hasOverflow: False on mobile.
"""

import os
from playwright.sync_api import sync_playwright

EVIDENCE_DIR = os.path.abspath("qa_evidence/machine_learning")
os.makedirs(EVIDENCE_DIR, exist_ok=True)

TARGET_HTML = os.path.abspath("coding/machine_learning/topic_17/notes.html")
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
        assert "Topic 17: Dimensionality Reduction" in title, f"Unexpected page title: {title}"

        # Verify SVGs
        svg_count = page.locator("svg").count()
        print(f"Rendered SVGs: {svg_count}")
        assert svg_count == 16, f"Expected 16 SVGs, found {svg_count}"

        # Capture Full Desktop Page
        desktop_full_path = os.path.join(EVIDENCE_DIR, "ml_topic_17_light_desktop.png")
        page.screenshot(path=desktop_full_path, full_page=True)
        print(f"Captured Desktop Full Page: {desktop_full_path}")

        # Capture Selected Major Sections
        sections_to_capture = [
            ("sec-01", "ml_topic_17_sec01_intro.png"),
            ("sec-02", "ml_topic_17_sec02_curse.png"),
            ("sec-03", "ml_topic_17_sec03_selection_vs_extraction.png"),
            ("sec-04", "ml_topic_17_sec04_methods.png"),
            ("sec-05", "ml_topic_17_sec05_pca_intuition.png"),
            ("sec-06", "ml_topic_17_sec06_math_foundations.png"),
            ("sec-07", "ml_topic_17_sec07_numerical_example.png"),
            ("sec-08", "ml_topic_17_sec08_explained_variance.png"),
            ("sec-09", "ml_topic_17_sec09_2d_3d_viz.png"),
            ("sec-10", "ml_topic_17_sec10_sklearn_pipeline.png"),
            ("sec-11", "ml_topic_17_sec11_model_performance.png"),
            ("sec-12", "ml_topic_17_sec12_tsne.png"),
            ("sec-13", "ml_topic_17_sec13_umap.png"),
            ("sec-14", "ml_topic_17_sec14_lda_vs_pca.png"),
            ("sec-15", "ml_topic_17_sec15_applications.png"),
            ("sec-16", "ml_topic_17_sec16_mistakes.png"),
            ("sec-18", "ml_topic_17_sec18_decision_flowchart.png"),
            ("sec-19", "ml_topic_17_sec19_complete_lab.png"),
            ("sec-20", "ml_topic_17_sec20_accordions.png"),
        ]

        for sec_id, out_name in sections_to_capture:
            loc = page.locator(f"#{sec_id}")
            if loc.count() > 0:
                out_path = os.path.join(EVIDENCE_DIR, out_name)
                loc.screenshot(path=out_path)
                print(f"Captured #{sec_id} -> {out_name}")
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
        mobile_full_path = os.path.join(EVIDENCE_DIR, "ml_topic_17_light_mobile.png")
        page_m.screenshot(path=mobile_full_path, full_page=True)
        print(f"Captured Mobile Full Page: {mobile_full_path}")

        # Capture Mobile Hero Viewport
        mobile_hero_path = os.path.join(EVIDENCE_DIR, "ml_topic_17_mobile_hero.png")
        page_m.screenshot(path=mobile_hero_path, full_page=False)
        print(f"Captured Mobile Viewport: {mobile_hero_path}")

        # Scroll to Section 10 and capture Mobile Pipeline Lab Viewport
        page_m.locator("#sec-10").scroll_into_view_if_needed()
        page_m.wait_for_timeout(300)
        mobile_lab1_path = os.path.join(EVIDENCE_DIR, "ml_topic_17_mobile_lab1.png")
        page_m.screenshot(path=mobile_lab1_path, full_page=False)
        print(f"Captured Mobile Pipeline Lab Viewport: {mobile_lab1_path}")

        # Scroll to Section 16 and capture Mobile Mistakes Viewport
        page_m.locator("#sec-16").scroll_into_view_if_needed()
        page_m.wait_for_timeout(300)
        mobile_mistakes_path = os.path.join(EVIDENCE_DIR, "ml_topic_17_mobile_mistakes.png")
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
