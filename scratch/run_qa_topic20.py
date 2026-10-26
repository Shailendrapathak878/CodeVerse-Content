import asyncio
import os
from playwright.async_api import async_playwright

async def run_qa():
    print("Starting Playwright QA for Topic 20: Cross-Validation and Model Validation...")
    
    html_path = os.path.abspath(os.path.join("coding", "machine_learning", "topic_20", "notes.html"))
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
        desktop_full_path = os.path.join(qa_dir, "ml_topic_20_light_desktop.png")
        await page_desktop.screenshot(path=desktop_full_path, full_page=True)
        print(f"  Desktop full-page screenshot saved: {desktop_full_path} ({os.path.getsize(desktop_full_path)} bytes)")
        
        # Capture individual sections for detailed inspection
        sections_to_capture = [
            ("sec-01", "intro_val_workflow"),
            ("sec-02", "train_val_test_splits"),
            ("sec-03", "generalization_gap"),
            ("sec-04", "fit_spectrum"),
            ("sec-05", "kfold_architecture"),
            ("sec-06", "kfold_rotation_math"),
            ("sec-07", "kfold_explorer"),
            ("sec-08", "stratified_vs_ordinary"),
            ("sec-09", "specialized_cv_strategies"),
            ("sec-10", "timeseries_split"),
            ("sec-11", "cross_val_score_iris"),
            ("sec-12", "actual_fold_scores"),
            ("sec-13", "hyperparameter_workflow"),
            ("sec-14", "grid_search_cv"),
            ("sec-15", "random_search_cv"),
            ("sec-16", "learning_curve"),
            ("sec-17", "validation_curve"),
            ("sec-18", "data_leakage_anatomy"),
            ("sec-19", "leakage_safe_pipeline"),
            ("sec-20", "common_pitfalls_15"),
            ("sec-21", "practical_project"),
            ("sec-22", "revision_formulas_glossary"),
            ("sec-23", "self_check_faq")
        ]
        
        for sec_id, name in sections_to_capture:
            el = await page_desktop.query_selector(f"#{sec_id}")
            if el:
                sec_path = os.path.join(qa_dir, f"ml_topic_20_sec_{name}.png")
                await el.screenshot(path=sec_path)
                print(f"  Captured section {sec_id} -> {sec_path}")
            else:
                print(f"  WARNING: Section #{sec_id} not found!")

        # Interactive Test: Test clicking K=3 and K=10 on K-Fold Explorer
        k3_btn = await page_desktop.query_selector(".kfold-btn:nth-child(1)")
        if k3_btn:
            await k3_btn.click()
            await asyncio.sleep(0.2)
            widget_el = await page_desktop.query_selector("#kfoldExplorer")
            if widget_el:
                k3_path = os.path.join(qa_dir, "ml_topic_20_widget_at_k3.png")
                await widget_el.screenshot(path=k3_path)
                print(f"  Captured K-Fold explorer at K=3 -> {k3_path}")
                
        k10_btn = await page_desktop.query_selector(".kfold-btn:nth-child(3)")
        if k10_btn:
            await k10_btn.click()
            await asyncio.sleep(0.2)
            widget_el = await page_desktop.query_selector("#kfoldExplorer")
            if widget_el:
                k10_path = os.path.join(qa_dir, "ml_topic_20_widget_at_k10.png")
                await widget_el.screenshot(path=k10_path)
                print(f"  Captured K-Fold explorer at K=10 -> {k10_path}")

        # Desktop Overflow Check
        desktop_overflow = await page_desktop.evaluate("""() => {
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
        print(f"Desktop Overflow Check: {desktop_overflow}")
        assert not desktop_overflow["hasOverflow"], "Desktop horizontal overflow detected!"

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
        mobile_full_path = os.path.join(qa_dir, "ml_topic_20_light_mobile.png")
        await page_mobile.screenshot(path=mobile_full_path, full_page=True)
        print(f"  Mobile full-page screenshot saved: {mobile_full_path} ({os.path.getsize(mobile_full_path)} bytes)")
        
        # Mobile Viewports
        # 1. Hero
        hero_path = os.path.join(qa_dir, "ml_topic_20_mobile_hero.png")
        await page_mobile.screenshot(path=hero_path)
        print(f"  Mobile hero viewport saved: {hero_path}")
        
        # 2. Section 07 Widget
        await page_mobile.evaluate("document.getElementById('sec-07').scrollIntoView()")
        await asyncio.sleep(0.3)
        widget_mobile_path = os.path.join(qa_dir, "ml_topic_20_mobile_widget.png")
        await page_mobile.screenshot(path=widget_mobile_path)
        print(f"  Mobile widget viewport saved: {widget_mobile_path}")

        # 3. Section 08 Stratified vs Ordinary
        await page_mobile.evaluate("document.getElementById('sec-08').scrollIntoView()")
        await asyncio.sleep(0.3)
        strat_mobile_path = os.path.join(qa_dir, "ml_topic_20_mobile_stratified.png")
        await page_mobile.screenshot(path=strat_mobile_path)
        print(f"  Mobile stratified viewport saved: {strat_mobile_path}")

        # 4. Section 16 Learning Curve
        await page_mobile.evaluate("document.getElementById('sec-16').scrollIntoView()")
        await asyncio.sleep(0.3)
        lc_mobile_path = os.path.join(qa_dir, "ml_topic_20_mobile_learning_curve.png")
        await page_mobile.screenshot(path=lc_mobile_path)
        print(f"  Mobile learning curve viewport saved: {lc_mobile_path}")

        # 5. Section 20 Pitfalls
        await page_mobile.evaluate("document.getElementById('sec-20').scrollIntoView()")
        await asyncio.sleep(0.3)
        pitfalls_mobile_path = os.path.join(qa_dir, "ml_topic_20_mobile_pitfalls.png")
        await page_mobile.screenshot(path=pitfalls_mobile_path)
        print(f"  Mobile pitfalls viewport saved: {pitfalls_mobile_path}")

        # 6. Section 21 Practical
        await page_mobile.evaluate("document.getElementById('sec-21').scrollIntoView()")
        await asyncio.sleep(0.3)
        practical_mobile_path = os.path.join(qa_dir, "ml_topic_20_mobile_practical.png")
        await page_mobile.screenshot(path=practical_mobile_path)
        print(f"  Mobile practical viewport saved: {practical_mobile_path}")

        # 7. Section 23 Accordions
        await page_mobile.evaluate("document.getElementById('sec-23').scrollIntoView()")
        await asyncio.sleep(0.3)
        accordions_mobile_path = os.path.join(qa_dir, "ml_topic_20_mobile_accordions.png")
        await page_mobile.screenshot(path=accordions_mobile_path)
        print(f"  Mobile accordions viewport saved: {accordions_mobile_path}")
        
        # Check for Horizontal Overflow on Mobile
        mobile_overflow = await page_mobile.evaluate("""() => {
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
        
        print(f"Mobile Overflow Check: {mobile_overflow}")
        if mobile_overflow["hasOverflow"]:
            print("  WARNING: Horizontal overflow detected on mobile!")
        else:
            print("  PASSED: Zero horizontal overflow on mobile!")
        assert not mobile_overflow["hasOverflow"], "Mobile horizontal overflow detected!"
            
        await context_mobile.close()
        await browser.close()
        
    print(f"\nQA Summary:")
    print(f"  Console Errors: {len(console_errors)}")
    for err in console_errors:
        print(f"    {err}")
    print(f"  Page Errors: {len(page_errors)}")
    for err in page_errors:
        print(f"    {err}")
        
    assert len(console_errors) == 0, f"Encountered console errors: {console_errors}"
    assert len(page_errors) == 0, f"Encountered page errors: {page_errors}"
    print("Playwright QA finished successfully with 100% PASS rate!")

if __name__ == "__main__":
    asyncio.run(run_qa())
