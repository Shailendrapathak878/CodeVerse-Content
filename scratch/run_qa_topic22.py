import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def run_qa():
    print("=" * 60)
    print("Starting Playwright QA for Topic 22: Hyperparameter Tuning...")
    print("=" * 60)
    
    html_path = os.path.abspath(os.path.join("coding", "machine_learning", "topic_22", "notes.html"))
    file_url = f"file:///{html_path.replace(os.sep, '/')}"
    
    qa_dir = os.path.join("qa_evidence", "machine_learning")
    os.makedirs(qa_dir, exist_ok=True)
    
    console_errors = []
    page_errors = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # ==========================================
        # 1. DESKTOP TEST (1280 x 800)
        # ==========================================
        context_desktop = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            device_scale_factor=1.0
        )
        page_desktop = await context_desktop.new_page()
        
        page_desktop.on("console", lambda msg: console_errors.append(f"CONSOLE: {msg.text}") if msg.type == "error" else None)
        page_desktop.on("pageerror", lambda err: page_errors.append(f"PAGE_ERROR: {err.message}"))
        
        print(f"\n[Desktop] Navigating to {file_url} at 1280x800...")
        await page_desktop.goto(file_url, wait_until="networkidle")
        
        # Desktop Full Page Screenshot
        desktop_full_path = os.path.join(qa_dir, "ml_topic_22_light_desktop.png")
        await page_desktop.screenshot(path=desktop_full_path, full_page=True)
        print(f"  [x] Desktop full-page screenshot saved: {desktop_full_path} ({os.path.getsize(desktop_full_path):,} bytes)")
        
        # Capture all 24 individual sections
        sections_to_capture = [
            ("sec-01", "01_intro_study_analogy"),
            ("sec-02", "02_params_vs_hyperparams"),
            ("sec-03", "03_why_tuning_needed"),
            ("sec-04", "04_train_val_test_sets"),
            ("sec-05", "05_manual_knn_tuning"),
            ("sec-06", "06_search_spaces_and_scales"),
            ("sec-07", "07_grid_search_theory"),
            ("sec-08", "08_gridsearchcv_practical"),
            ("sec-09", "09_random_search_theory"),
            ("sec-10", "10_randomizedsearchcv_practical"),
            ("sec-11", "11_grid_vs_random_search"),
            ("sec-12", "12_cross_validation_tuning"),
            ("sec-13", "13_interpreting_cv_scores"),
            ("sec-14", "14_algorithm_hyperparams_map"),
            ("sec-15", "15_choosing_scoring_metrics"),
            ("sec-16", "16_overfitting_selection_bias"),
            ("sec-17", "17_data_leakage_pipelines"),
            ("sec-18", "18_learning_and_validation_curves"),
            ("sec-19", "19_computational_cost_efficiency"),
            ("sec-20", "20_nested_cross_validation"),
            ("sec-21", "21_complete_practical_project"),
            ("sec-22", "22_15_common_mistakes"),
            ("sec-23", "23_revision_glossary_checklist"),
            ("sec-24", "24_self_check_questions")
        ]
        
        print(f"\n[Desktop] Capturing {len(sections_to_capture)} individual section screenshots...")
        for sec_id, name in sections_to_capture:
            el = await page_desktop.query_selector(f"#{sec_id}")
            if el:
                sec_path = os.path.join(qa_dir, f"ml_topic_22_sec_{name}.png")
                await el.screenshot(path=sec_path)
                print(f"  [x] Captured section #{sec_id} -> {sec_path}")
            else:
                print(f"  [!] WARNING: Section #{sec_id} not found!")

        # Interactive Test 1: Expanding an FAQ accordion
        first_faq = await page_desktop.query_selector("details.faq-item summary")
        if first_faq:
            await first_faq.click()
            await asyncio.sleep(0.2)
            faq_container = await page_desktop.query_selector("#sec-24")
            if faq_container:
                faq_shot = os.path.join(qa_dir, "ml_topic_22_accordion_expanded.png")
                await faq_container.screenshot(path=faq_shot)
                print(f"  [x] Captured expanded accordion in Section 24 -> {faq_shot}")

        # Interactive Test 2: Interactive Search Workload Calculator
        calc_input = await page_desktop.query_selector("#calc-params")
        if calc_input:
            await calc_input.fill("4")
            await page_desktop.evaluate("document.getElementById('calc-params').dispatchEvent(new Event('input'))")
            await asyncio.sleep(0.2)
            calc_container = await page_desktop.query_selector("#interactive-calculator")
            if calc_container:
                calc_shot = os.path.join(qa_dir, "ml_topic_22_calculator_interactive.png")
                await calc_container.screenshot(path=calc_shot)
                print(f"  [x] Captured interactive calculator -> {calc_shot}")

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
        print(f"\n[Desktop] Overflow Check: {desktop_overflow}")
        assert not desktop_overflow["hasOverflow"], "ERROR: Desktop horizontal overflow detected!"
        print("  [x] PASSED Desktop horizontal overflow check (0px overflow).")

        await context_desktop.close()
        
        # ==========================================
        # 2. MOBILE TEST (390 x 844 - iPhone Viewport)
        # ==========================================
        context_mobile = await browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2.0,
            is_mobile=True
        )
        page_mobile = await context_mobile.new_page()
        
        page_mobile.on("console", lambda msg: console_errors.append(f"MOBILE CONSOLE: {msg.text}") if msg.type == "error" else None)
        page_mobile.on("pageerror", lambda err: page_errors.append(f"MOBILE PAGE_ERROR: {err.message}"))
        
        print(f"\n[Mobile] Navigating to {file_url} at 390x844...")
        await page_mobile.goto(file_url, wait_until="networkidle")
        
        # Mobile Full Page Screenshot
        mobile_full_path = os.path.join(qa_dir, "ml_topic_22_light_mobile.png")
        await page_mobile.screenshot(path=mobile_full_path, full_page=True)
        print(f"  [x] Mobile full-page screenshot saved: {mobile_full_path} ({os.path.getsize(mobile_full_path):,} bytes)")
        
        # Mobile Viewports
        # 1. Hero
        hero_path = os.path.join(qa_dir, "ml_topic_22_mobile_hero.png")
        await page_mobile.screenshot(path=hero_path)
        print(f"  [x] Mobile hero viewport saved: {hero_path}")
        
        # 2. Section 01 Workflow
        await page_mobile.evaluate("document.getElementById('sec-01').scrollIntoView()")
        await asyncio.sleep(0.3)
        s1_path = os.path.join(qa_dir, "ml_topic_22_mobile_sec01_workflow.png")
        await page_mobile.screenshot(path=s1_path)
        print(f"  [x] Mobile Sec 01 viewport saved: {s1_path}")

        # 3. Section 05 Manual Tuning
        await page_mobile.evaluate("document.getElementById('sec-05').scrollIntoView()")
        await asyncio.sleep(0.3)
        s5_path = os.path.join(qa_dir, "ml_topic_22_mobile_sec05_manual_tuning.png")
        await page_mobile.screenshot(path=s5_path)
        print(f"  [x] Mobile Sec 05 viewport saved: {s5_path}")

        # 4. Section 08 GridSearchCV
        await page_mobile.evaluate("document.getElementById('sec-08').scrollIntoView()")
        await asyncio.sleep(0.3)
        s8_path = os.path.join(qa_dir, "ml_topic_22_mobile_sec08_gridsearchcv.png")
        await page_mobile.screenshot(path=s8_path)
        print(f"  [x] Mobile Sec 08 viewport saved: {s8_path}")

        # 5. Section 11 Grid vs Random
        await page_mobile.evaluate("document.getElementById('sec-11').scrollIntoView()")
        await asyncio.sleep(0.3)
        s11_path = os.path.join(qa_dir, "ml_topic_22_mobile_sec11_grid_vs_random.png")
        await page_mobile.screenshot(path=s11_path)
        print(f"  [x] Mobile Sec 11 viewport saved: {s11_path}")

        # 6. Section 15 Metrics
        await page_mobile.evaluate("document.getElementById('sec-15').scrollIntoView()")
        await asyncio.sleep(0.3)
        s15_path = os.path.join(qa_dir, "ml_topic_22_mobile_sec15_metrics.png")
        await page_mobile.screenshot(path=s15_path)
        print(f"  [x] Mobile Sec 15 viewport saved: {s15_path}")

        # 7. Section 18 Curves
        await page_mobile.evaluate("document.getElementById('sec-18').scrollIntoView()")
        await asyncio.sleep(0.3)
        s18_path = os.path.join(qa_dir, "ml_topic_22_mobile_sec18_curves.png")
        await page_mobile.screenshot(path=s18_path)
        print(f"  [x] Mobile Sec 18 viewport saved: {s18_path}")

        # 8. Section 21 Practical
        await page_mobile.evaluate("document.getElementById('sec-21').scrollIntoView()")
        await asyncio.sleep(0.3)
        s21_path = os.path.join(qa_dir, "ml_topic_22_mobile_sec21_practical.png")
        await page_mobile.screenshot(path=s21_path)
        print(f"  [x] Mobile Sec 21 viewport saved: {s21_path}")

        # 9. Section 24 Self-check
        await page_mobile.evaluate("document.getElementById('sec-24').scrollIntoView()")
        await asyncio.sleep(0.3)
        s24_path = os.path.join(qa_dir, "ml_topic_22_mobile_sec24_self_check.png")
        await page_mobile.screenshot(path=s24_path)
        print(f"  [x] Mobile Sec 24 viewport saved: {s24_path}")

        # Mobile Overflow Check
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
        print(f"\n[Mobile] Overflow Check: {mobile_overflow}")
        assert not mobile_overflow["hasOverflow"], "ERROR: Mobile horizontal overflow detected!"
        print("  [x] PASSED Mobile horizontal overflow check (0px overflow on 390px viewport).")

        await context_mobile.close()
        await browser.close()
        
    print(f"\nConsole Errors: {len(console_errors)}")
    if console_errors:
        for err in console_errors:
            print(f"  {err}")
    assert len(console_errors) == 0, f"Detected console errors: {console_errors}"
    
    print(f"Page Errors: {len(page_errors)}")
    if page_errors:
        for err in page_errors:
            print(f"  {err}")
    assert len(page_errors) == 0, f"Detected page errors: {page_errors}"
    
    print("\n" + "=" * 60)
    print("ALL PLAYWRIGHT QA CHECKS PASSED WITH 100% SUCCESS!")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(run_qa())
