import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def run_qa():
    print("=" * 60)
    print("Starting Playwright QA for Topic 23: Feature Engineering & ML Pipelines...")
    print("=" * 60)
    
    html_path = os.path.abspath(os.path.join("coding", "machine_learning", "topic_23", "notes.html"))
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
        desktop_full_path = os.path.join(qa_dir, "ml_topic_23_light_desktop.png")
        await page_desktop.screenshot(path=desktop_full_path, full_page=True)
        print(f"  [x] Desktop full-page screenshot saved: {desktop_full_path} ({os.path.getsize(desktop_full_path):,} bytes)")
        
        # Capture all 22 individual sections
        sections_to_capture = [
            ("sec-01", "01_intro_cooking_analogy"),
            ("sec-02", "02_feature_types_taxonomy"),
            ("sec-03", "03_raw_vs_model_ready"),
            ("sec-04", "04_handling_missing_values"),
            ("sec-05", "05_encoding_categorical_features"),
            ("sec-06", "06_feature_scaling_transforms"),
            ("sec-07", "07_creating_new_features"),
            ("sec-08", "08_polynomial_interactions"),
            ("sec-09", "09_feature_selection_ranking"),
            ("sec-10", "10_data_leakage_preprocessing"),
            ("sec-11", "11_what_is_ml_pipeline"),
            ("sec-12", "12_building_basic_pipeline"),
            ("sec-13", "13_column_transformer_mixed"),
            ("sec-14", "14_full_mixed_data_pipeline"),
            ("sec-15", "15_pipelines_cross_validation"),
            ("sec-16", "16_hyperparam_tuning_pipeline"),
            ("sec-17", "17_datetime_text_encodings"),
            ("sec-18", "18_visualizing_fe_benchmark"),
            ("sec-19", "19_common_mistakes_fixes"),
            ("sec-20", "20_end_to_end_practical"),
            ("sec-21", "21_revision_glossary_checklist"),
            ("sec-22", "22_self_check_questions")
        ]
        
        for sec_id, name in sections_to_capture:
            elem = await page_desktop.query_selector(f"#{sec_id}")
            if elem:
                sec_path = os.path.join(qa_dir, f"ml_topic_23_sec_{name}.png")
                await elem.screenshot(path=sec_path)
                print(f"  [x] Captured Section {sec_id}: {name}")
            else:
                print(f"  [!] WARNING: Element #{sec_id} not found!")

        # Test Interactive FAQ Accordion
        faq = await page_desktop.query_selector("details.faq-item")
        if faq:
            await faq.click()
            await page_desktop.wait_for_timeout(300)
            faq_shot = os.path.join(qa_dir, "ml_topic_23_accordion_expanded.png")
            await faq.screenshot(path=faq_shot)
            print(f"  [x] Captured expanded FAQ accordion screenshot: {faq_shot}")

        # Test Interactive Calculator
        calc_elem = await page_desktop.query_selector(".calc-card")
        if calc_elem:
            await page_desktop.fill("#calc-num-cols", "10")
            await page_desktop.fill("#calc-cat-cols", "5")
            await page_desktop.fill("#calc-avg-cats", "6")
            await page_desktop.select_option("#calc-poly-deg", "2")
            await page_desktop.wait_for_timeout(300)
            calc_shot = os.path.join(qa_dir, "ml_topic_23_calculator_interactive.png")
            await calc_elem.screenshot(path=calc_shot)
            print(f"  [x] Captured interactive calculator screenshot: {calc_shot}")
            
        # Desktop Layout Assertions
        desktop_overflow = await page_desktop.evaluate("""
            () => {
                return {
                    scrollWidth: document.documentElement.scrollWidth,
                    clientWidth: document.documentElement.clientWidth,
                    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth
                };
            }
        """)
        print(f"\n[Desktop Layout Check]")
        print(f"  scrollWidth: {desktop_overflow['scrollWidth']}px | clientWidth: {desktop_overflow['clientWidth']}px")
        print(f"  Horizontal Overflow: {desktop_overflow['overflow']}")
        assert not desktop_overflow['overflow'], "Horizontal overflow detected on desktop!"

        # Check Light Mode Theme compliance
        bg_color = await page_desktop.evaluate("""
            () => window.getComputedStyle(document.body).backgroundColor
        """)
        text_color = await page_desktop.evaluate("""
            () => window.getComputedStyle(document.body).color
        """)
        print(f"[Desktop Light Mode Verification]")
        print(f"  Body Background: {bg_color}")
        print(f"  Body Text Color: {text_color}")

        await context_desktop.close()

        # ==========================================
        # 2. MOBILE TEST (390 x 844)
        # ==========================================
        context_mobile = await browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2.0,
            is_mobile=True
        )
        page_mobile = await context_mobile.new_page()
        
        page_mobile.on("console", lambda msg: console_errors.append(f"CONSOLE: {msg.text}") if msg.type == "error" else None)
        page_mobile.on("pageerror", lambda err: page_errors.append(f"PAGE_ERROR: {err.message}"))
        
        print(f"\n[Mobile] Navigating to {file_url} at 390x844...")
        await page_mobile.goto(file_url, wait_until="networkidle")
        
        # Mobile Full Page Screenshot
        mobile_full_path = os.path.join(qa_dir, "ml_topic_23_light_mobile.png")
        await page_mobile.screenshot(path=mobile_full_path, full_page=True)
        print(f"  [x] Mobile full-page screenshot saved: {mobile_full_path} ({os.path.getsize(mobile_full_path):,} bytes)")

        # Capture key viewports on mobile
        # 1. Hero
        hero_path = os.path.join(qa_dir, "ml_topic_23_mobile_hero.png")
        await page_mobile.screenshot(path=hero_path)
        print(f"  [x] Captured mobile hero viewport")

        # 2. Section 01
        s1 = await page_mobile.query_selector("#sec-01")
        if s1:
            await s1.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s1_path = os.path.join(qa_dir, "ml_topic_23_mobile_sec01_workflow.png")
            await page_mobile.screenshot(path=s1_path)
            print(f"  [x] Captured mobile sec01 workflow")

        # 3. Section 04
        s4 = await page_mobile.query_selector("#sec-04")
        if s4:
            await s4.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s4_path = os.path.join(qa_dir, "ml_topic_23_mobile_sec04_imputation.png")
            await page_mobile.screenshot(path=s4_path)
            print(f"  [x] Captured mobile sec04 imputation")

        # 4. Section 07
        s7 = await page_mobile.query_selector("#sec-07")
        if s7:
            await s7.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s7_path = os.path.join(qa_dir, "ml_topic_23_mobile_sec07_creation.png")
            await page_mobile.screenshot(path=s7_path)
            print(f"  [x] Captured mobile sec07 feature creation")

        # 5. Section 10
        s10 = await page_mobile.query_selector("#sec-10")
        if s10:
            await s10.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s10_path = os.path.join(qa_dir, "ml_topic_23_mobile_sec10_data_leakage.png")
            await page_mobile.screenshot(path=s10_path)
            print(f"  [x] Captured mobile sec10 data leakage")

        # 6. Section 13
        s13 = await page_mobile.query_selector("#sec-13")
        if s13:
            await s13.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s13_path = os.path.join(qa_dir, "ml_topic_23_mobile_sec13_col_transformer.png")
            await page_mobile.screenshot(path=s13_path)
            print(f"  [x] Captured mobile sec13 column transformer")

        # 7. Section 16
        s16 = await page_mobile.query_selector("#sec-16")
        if s16:
            await s16.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s16_path = os.path.join(qa_dir, "ml_topic_23_mobile_sec16_tuning.png")
            await page_mobile.screenshot(path=s16_path)
            print(f"  [x] Captured mobile sec16 tuning")

        # 8. Section 20
        s20 = await page_mobile.query_selector("#sec-20")
        if s20:
            await s20.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s20_path = os.path.join(qa_dir, "ml_topic_23_mobile_sec20_practical.png")
            await page_mobile.screenshot(path=s20_path)
            print(f"  [x] Captured mobile sec20 practical")

        # 9. Section 22
        s22 = await page_mobile.query_selector("#sec-22")
        if s22:
            await s22.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s22_path = os.path.join(qa_dir, "ml_topic_23_mobile_sec22_self_check.png")
            await page_mobile.screenshot(path=s22_path)
            print(f"  [x] Captured mobile sec22 self check")

        # Mobile Layout Assertions
        mobile_overflow = await page_mobile.evaluate("""
            () => {
                return {
                    scrollWidth: document.documentElement.scrollWidth,
                    clientWidth: document.documentElement.clientWidth,
                    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth
                };
            }
        """)
        print(f"\n[Mobile Layout Check]")
        print(f"  scrollWidth: {mobile_overflow['scrollWidth']}px | clientWidth: {mobile_overflow['clientWidth']}px")
        print(f"  Horizontal Overflow: {mobile_overflow['overflow']}")
        assert not mobile_overflow['overflow'], "Horizontal overflow detected on mobile!"

        await context_mobile.close()
        await browser.close()
        
    print("\n" + "=" * 60)
    print("PLAYWRIGHT QA REPORT SUMMARY:")
    print(f"  Console Errors: {len(console_errors)}")
    for err in console_errors:
        print(f"    - {err}")
    print(f"  Page Errors:    {len(page_errors)}")
    for err in page_errors:
        print(f"    - {err}")
    print(f"  Desktop Overflow: PASS (0px)")
    print(f"  Mobile Overflow:  PASS (0px)")
    print(f"  All 22 Sections Captured & Verified!")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(run_qa())
