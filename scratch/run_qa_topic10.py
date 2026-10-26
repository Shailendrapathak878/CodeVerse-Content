"""
Playwright QA automation script for Topic 10: Logistic Regression.
Captures full-page and section-specific screenshots in Desktop (1280x800) and Mobile (390x844).
Validates zero console errors, zero horizontal overflow, and interactive accordion behavior.
"""

import os
import asyncio
from playwright.async_api import async_playwright

NOTES_FILE = os.path.abspath("coding/machine_learning/topic_10/notes.html")
FILE_URL = f"file:///{NOTES_FILE.replace(os.sep, '/')}"
OUTPUT_DIR = os.path.abspath("qa_evidence/machine_learning")
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def run_qa():
    console_errors = []
    page_errors = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # ---------------------------------------------------------
        # 1. DESKTOP TEST: 1280 x 800
        # ---------------------------------------------------------
        print(f"=== 1. Starting Desktop QA at 1280x800 ===")
        context_desktop = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            device_scale_factor=1.0
        )
        page_desktop = await context_desktop.new_page()

        page_desktop.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page_desktop.on("pageerror", lambda exc: page_errors.append(str(exc)))

        print(f"Loading {FILE_URL}...")
        await page_desktop.goto(FILE_URL, wait_until="networkidle")
        await asyncio.sleep(1)

        # Verify page title
        title = await page_desktop.title()
        print(f"Page Title: {title}")
        assert "Topic 10: Logistic Regression" in title, f"Unexpected title: {title}"

        # Verify all 14 SVGs are present and rendered
        svg_count = await page_desktop.locator("svg").count()
        print(f"Rendered SVGs: {svg_count}")
        assert svg_count >= 14, f"Expected at least 14 SVGs, found {svg_count}"

        # Capture Desktop Full Page Screenshot
        desktop_full_path = os.path.join(OUTPUT_DIR, "ml_topic_10_light_desktop.png")
        await page_desktop.screenshot(path=desktop_full_path, full_page=True)
        print(f"Captured Desktop Full Page: {desktop_full_path}")

        # Capture Section-Specific Desktop Screenshots for all 21 sections
        sections_to_capture = [
            ("#sec-01", "ml_topic_10_sec01_intro.png"),
            ("#sec-02", "ml_topic_10_sec02_whatis.png"),
            ("#sec-03", "ml_topic_10_sec03_why_not_linear.png"),
            ("#sec-04", "ml_topic_10_sec04_sigmoid.png"),
            ("#sec-05", "ml_topic_10_sec05_equation.png"),
            ("#sec-06", "ml_topic_10_sec06_odds_logits.png"),
            ("#sec-07", "ml_topic_10_sec07_thresholds.png"),
            ("#sec-08", "ml_topic_10_sec08_decision_boundary.png"),
            ("#sec-09", "ml_topic_10_sec09_mle_learning.png"),
            ("#sec-10", "ml_topic_10_sec10_log_loss.png"),
            ("#sec-11", "ml_topic_10_sec11_multiple_logreg.png"),
            ("#sec-12", "ml_topic_10_sec12_regularization.png"),
            ("#sec-13", "ml_topic_10_sec13_metrics_confusion.png"),
            ("#sec-14", "ml_topic_10_sec14_roc_auc.png"),
            ("#sec-15", "ml_topic_10_sec15_class_imbalance.png"),
            ("#sec-16", "ml_topic_10_sec16_calibration.png"),
            ("#sec-17", "ml_topic_10_sec17_python_lab.png"),
            ("#sec-18", "ml_topic_10_sec18_case_studies.png"),
            ("#sec-19", "ml_topic_10_sec19_visual_gallery.png"),
            ("#sec-20", "ml_topic_10_sec20_mistakes.png"),
            ("#sec-21", "ml_topic_10_sec21_glossary_revision.png"),
        ]

        for selector, filename in sections_to_capture:
            elem = page_desktop.locator(selector)
            if await elem.count() > 0:
                await elem.scroll_into_view_if_needed()
                await asyncio.sleep(0.3)
                dest = os.path.join(OUTPUT_DIR, filename)
                await elem.screenshot(path=dest)
                print(f"Captured {selector} -> {dest}")

        await context_desktop.close()

        # ---------------------------------------------------------
        # 2. MOBILE TEST: 390 x 844
        # ---------------------------------------------------------
        print(f"\n=== 2. Starting Mobile QA at 390x844 ===")
        context_mobile = await browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2.0,
            is_mobile=True,
            has_touch=True
        )
        page_mobile = await context_mobile.new_page()

        page_mobile.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page_mobile.on("pageerror", lambda exc: page_errors.append(str(exc)))

        await page_mobile.goto(FILE_URL, wait_until="networkidle")
        await asyncio.sleep(1)

        # Check for Horizontal Overflow on Mobile
        overflow_info = await page_mobile.evaluate("""() => {
            return {
                scrollWidth: document.documentElement.scrollWidth,
                clientWidth: document.documentElement.clientWidth,
                bodyScrollWidth: document.body.scrollWidth,
                windowWidth: window.innerWidth,
                hasOverflow: document.documentElement.scrollWidth > window.innerWidth
            };
        }""")
        print(f"Mobile Overflow Diagnostics: {overflow_info}")
        assert not overflow_info["hasOverflow"], f"CRITICAL: Horizontal overflow detected on mobile: {overflow_info}"

        # Capture Mobile Full Page Screenshot
        mobile_full_path = os.path.join(OUTPUT_DIR, "ml_topic_10_light_mobile.png")
        await page_mobile.screenshot(path=mobile_full_path, full_page=True)
        print(f"Captured Mobile Full Page: {mobile_full_path}")

        # Capture Mobile Hero Viewport Screenshot
        mobile_sec1_path = os.path.join(OUTPUT_DIR, "ml_topic_10_mobile_sec01.png")
        await page_mobile.screenshot(path=mobile_sec1_path, full_page=False)
        print(f"Captured Mobile Viewport: {mobile_sec1_path}")

        # Capture Mobile Section 17 (Lab) Viewport Screenshot
        mobile_lab = page_mobile.locator("#sec-17")
        if await mobile_lab.count() > 0:
            await mobile_lab.scroll_into_view_if_needed()
            await asyncio.sleep(0.3)
            mobile_lab_path = os.path.join(OUTPUT_DIR, "ml_topic_10_mobile_lab.png")
            await page_mobile.screenshot(path=mobile_lab_path, full_page=False)
            print(f"Captured Mobile Lab Viewport: {mobile_lab_path}")

        # Test Interactive Accordion Expansion
        first_details = page_mobile.locator("details").first
        await first_details.scroll_into_view_if_needed()
        summary = first_details.locator("summary")
        await summary.click()
        await asyncio.sleep(0.3)
        is_open = await first_details.evaluate("el => el.hasAttribute('open')")
        print(f"Interactive Accordion Expanded: {is_open}")
        assert is_open, "Accordion failed to open on click!"

        await context_mobile.close()
        await browser.close()

        # ---------------------------------------------------------
        # 3. CONSOLE & PAGE ERROR ASSERTIONS
        # ---------------------------------------------------------
        print("\n=== 3. Error Verification ===")
        print(f"Console Errors: {len(console_errors)}")
        for err in console_errors:
            print(f"  [CONSOLE ERROR] {err}")
        print(f"Page Errors: {len(page_errors)}")
        for err in page_errors:
            print(f"  [PAGE ERROR] {err}")

        assert len(console_errors) == 0, f"Found {len(console_errors)} console errors!"
        assert len(page_errors) == 0, f"Found {len(page_errors)} page errors!"
        print("\nALL DESKTOP & MOBILE QA CHECKS PASSED WITH ZERO ERRORS!")

if __name__ == "__main__":
    asyncio.run(run_qa())
