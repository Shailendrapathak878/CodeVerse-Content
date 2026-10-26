import asyncio
import os
from playwright.async_api import async_playwright

async def run_qa():
    print("Starting Playwright QA for Topic 19: Classification and Regression Metrics...")
    
    html_path = os.path.abspath(os.path.join("coding", "machine_learning", "topic_19", "notes.html"))
    file_url = f"file:///{html_path.replace(os.sep, '/')}"
    
    qa_dir = os.path.join("qa_evidence", "machine_learning")
    os.makedirs(qa_dir, exist_ok=True)
    
    console_errors = []
    page_errors = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # 1. Desktop Test (1280 x 800)
        context_desktop = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            device_scale_factor=1.0
        )
        page_desktop = await context_desktop.new_page()
        
        page_desktop.on("console", lambda msg: console_errors.append(f"CONSOLE: {msg.text}") if msg.type == "error" else None)
        page_desktop.on("pageerror", lambda err: page_errors.append(f"PAGE_ERROR: {err.message}"))
        
        print(f"Navigating to {file_url} at 1280x800...")
        await page_desktop.goto(file_url, wait_until="networkidle")
        
        # Desktop Full Page Screenshot
        desktop_full_path = os.path.join(qa_dir, "ml_topic_19_light_desktop.png")
        await page_desktop.screenshot(path=desktop_full_path, full_page=True)
        print(f"  Desktop full-page screenshot saved: {desktop_full_path} ({os.path.getsize(desktop_full_path)} bytes)")
        
        # Capture individual sections for detailed inspection
        sections_to_capture = [
            ("sec-01", "intro_cls_vs_reg"),
            ("sec-02", "prob_threshold"),
            ("sec-04", "confusion_matrix"),
            ("sec-05", "accuracy_paradox"),
            ("sec-07", "precision_vs_recall"),
            ("sec-08", "specificity_fpr_fnr"),
            ("sec-10", "threshold_sweep"),
            ("sec-11", "threshold_demo_widget"),
            ("sec-12", "roc_curve"),
            ("sec-13", "pr_curve"),
            ("sec-14", "multiclass_averaging"),
            ("sec-15", "regression_residuals"),
            ("sec-19", "mae_vs_mse_curve"),
            ("sec-20", "r2_baseline"),
            ("sec-21", "residual_plots"),
            ("sec-22", "eval_splits_pipeline"),
            ("sec-23", "decision_tree"),
            ("sec-24", "mistakes"),
            ("sec-25", "practical_dashboard"),
            ("sec-26", "revision_formulas"),
            ("sec-27", "self_check_faq")
        ]
        
        for sec_id, name in sections_to_capture:
            el = await page_desktop.query_selector(f"#{sec_id}")
            if el:
                sec_path = os.path.join(qa_dir, f"ml_topic_19_sec_{name}.png")
                await el.screenshot(path=sec_path)
                print(f"  Captured section {sec_id} -> {sec_path}")
            else:
                print(f"  WARNING: Section #{sec_id} not found!")

        # Also test adjusting the slider in Section 11 to verify interactive logic
        slider = await page_desktop.query_selector("#threshold-slider")
        if slider:
            await page_desktop.evaluate("""() => {
                const s = document.getElementById('threshold-slider');
                if (s) {
                    s.value = '0.70';
                    s.dispatchEvent(new Event('input'));
                }
            }""")
            await asyncio.sleep(0.3)
            widget_el = await page_desktop.query_selector(".threshold-widget")
            if widget_el:
                widget_path = os.path.join(qa_dir, "ml_topic_19_widget_at_070.png")
                await widget_el.screenshot(path=widget_path)
                print(f"  Captured threshold widget at threshold=0.70 -> {widget_path}")

        await context_desktop.close()
        
        # 2. Mobile Test (390 x 844 - iPhone 12/13/14 size)
        context_mobile = await browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2.0,
            is_mobile=True
        )
        page_mobile = await context_mobile.new_page()
        
        page_mobile.on("console", lambda msg: console_errors.append(f"MOBILE CONSOLE: {msg.text}") if msg.type == "error" else None)
        page_mobile.on("pageerror", lambda err: page_errors.append(f"MOBILE PAGE_ERROR: {err.message}"))
        
        print(f"Navigating to {file_url} at 390x844...")
        await page_mobile.goto(file_url, wait_until="networkidle")
        
        # Mobile Full Page Screenshot
        mobile_full_path = os.path.join(qa_dir, "ml_topic_19_light_mobile.png")
        await page_mobile.screenshot(path=mobile_full_path, full_page=True)
        print(f"  Mobile full-page screenshot saved: {mobile_full_path} ({os.path.getsize(mobile_full_path)} bytes)")
        
        # Mobile Viewports
        # 1. Hero
        hero_path = os.path.join(qa_dir, "ml_topic_19_mobile_hero.png")
        await page_mobile.screenshot(path=hero_path)
        print(f"  Mobile hero viewport saved: {hero_path}")
        
        # 2. Section 11 Widget
        await page_mobile.evaluate("document.getElementById('sec-11').scrollIntoView()")
        await asyncio.sleep(0.3)
        widget_mobile_path = os.path.join(qa_dir, "ml_topic_19_mobile_widget.png")
        await page_mobile.screenshot(path=widget_mobile_path)
        print(f"  Mobile widget viewport saved: {widget_mobile_path}")

        # 3. Section 14 Multiclass
        await page_mobile.evaluate("document.getElementById('sec-14').scrollIntoView()")
        await asyncio.sleep(0.3)
        multi_mobile_path = os.path.join(qa_dir, "ml_topic_19_mobile_multiclass.png")
        await page_mobile.screenshot(path=multi_mobile_path)
        print(f"  Mobile multiclass viewport saved: {multi_mobile_path}")

        # 4. Section 24 Mistakes
        await page_mobile.evaluate("document.getElementById('sec-24').scrollIntoView()")
        await asyncio.sleep(0.3)
        mistakes_mobile_path = os.path.join(qa_dir, "ml_topic_19_mobile_mistakes.png")
        await page_mobile.screenshot(path=mistakes_mobile_path)
        print(f"  Mobile mistakes viewport saved: {mistakes_mobile_path}")

        # 5. Section 25 Practical
        await page_mobile.evaluate("document.getElementById('sec-25').scrollIntoView()")
        await asyncio.sleep(0.3)
        practical_mobile_path = os.path.join(qa_dir, "ml_topic_19_mobile_practical.png")
        await page_mobile.screenshot(path=practical_mobile_path)
        print(f"  Mobile practical viewport saved: {practical_mobile_path}")

        # 6. Section 27 Accordions
        await page_mobile.evaluate("document.getElementById('sec-27').scrollIntoView()")
        await asyncio.sleep(0.3)
        accordions_mobile_path = os.path.join(qa_dir, "ml_topic_19_mobile_accordions.png")
        await page_mobile.screenshot(path=accordions_mobile_path)
        print(f"  Mobile accordions viewport saved: {accordions_mobile_path}")
        
        # Check for Horizontal Overflow on Mobile
        overflow_info = await page_mobile.evaluate("""() => {
            const docWidth = document.documentElement.offsetWidth;
            const scrollWidth = document.documentElement.scrollWidth;
            const clientWidth = document.documentElement.clientWidth;
            const bodyScrollWidth = document.body.scrollWidth;
            return {
                docWidth,
                scrollWidth,
                clientWidth,
                bodyScrollWidth,
                windowWidth: window.innerWidth,
                hasOverflow: scrollWidth > clientWidth || bodyScrollWidth > window.innerWidth
            };
        }""")
        
        print(f"Mobile Overflow Check: {overflow_info}")
        if overflow_info["hasOverflow"]:
            print("  WARNING: Horizontal overflow detected on mobile!")
        else:
            print("  PASSED: Zero horizontal overflow on mobile!")
            
        await context_mobile.close()
        await browser.close()
        
    print(f"\nQA Summary:")
    print(f"  Console Errors: {len(console_errors)}")
    for err in console_errors:
        print(f"    {err}")
    print(f"  Page Errors: {len(page_errors)}")
    for err in page_errors:
        print(f"    {err}")
    print("Playwright QA finished!")

if __name__ == "__main__":
    asyncio.run(run_qa())
