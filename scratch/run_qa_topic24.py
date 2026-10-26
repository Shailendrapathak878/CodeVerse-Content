import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def run_qa():
    print("=" * 60)
    print("Starting Playwright QA for Topic 24: Model Deployment & MLOps Fundamentals...")
    print("=" * 60)
    
    html_path = os.path.abspath(os.path.join("coding", "machine_learning", "topic_24", "notes.html"))
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
        desktop_full_path = os.path.join(qa_dir, "ml_topic_24_light_desktop.png")
        await page_desktop.screenshot(path=desktop_full_path, full_page=True)
        print(f"  [x] Desktop full-page screenshot saved: {desktop_full_path} ({os.path.getsize(desktop_full_path):,} bytes)")
        
        # Capture all 21 individual sections
        sections_to_capture = [
            ("sec-01", "01_ml_lifecycle"),
            ("sec-02", "02_deployment_architecture"),
            ("sec-03", "03_artifact_serialization"),
            ("sec-04", "04_api_receptionist_flow"),
            ("sec-05", "05_fastapi_service"),
            ("sec-06", "06_batch_vs_realtime"),
            ("sec-07", "07_local_vs_cloud"),
            ("sec-08", "08_docker_containers"),
            ("sec-09", "09_mlops_flywheel"),
            ("sec-10", "10_experiment_versioning"),
            ("sec-11", "11_data_concept_drift"),
            ("sec-12", "12_monitoring_dashboard"),
            ("sec-13", "13_retraining_champion_challenger"),
            ("sec-14", "14_cicd_testing_pipeline"),
            ("sec-15", "15_security_checklist"),
            ("sec-16", "16_troubleshooting_challenges"),
            ("sec-17", "17_capstone_churn_project"),
            ("sec-18", "18_visuals_diagnostic_guide"),
            ("sec-19", "19_revision_checklist"),
            ("sec-20", "20_self_check_workload_calc"),
            ("sec-21", "21_final_completion_banner")
        ]
        
        for sec_id, name in sections_to_capture:
            elem = await page_desktop.query_selector(f"#{sec_id}")
            if elem:
                sec_path = os.path.join(qa_dir, f"ml_topic_24_sec_{name}.png")
                await elem.screenshot(path=sec_path)
                print(f"  [x] Captured Section {sec_id}: {name}")
            else:
                print(f"  [!] WARNING: Element #{sec_id} not found!")

        # Test Interactive Self-Check Accordion
        accordion = await page_desktop.query_selector("details.interactive-accordion")
        if accordion:
            await accordion.click()
            await page_desktop.wait_for_timeout(300)
            acc_shot = os.path.join(qa_dir, "ml_topic_24_accordion_expanded.png")
            await accordion.screenshot(path=acc_shot)
            print(f"  [x] Captured expanded accordion screenshot: {acc_shot}")

        # Test Interactive Serving Workload Calculator
        calc_elem = await page_desktop.query_selector(".calculator-card")
        if calc_elem:
            # Adjust slider values
            await page_desktop.evaluate("""
                () => {
                    document.getElementById('calc-users').value = 50000;
                    document.getElementById('calc-queries').value = 10;
                    document.getElementById('calc-latency').value = 25;
                    document.getElementById('calc-instance-cost').value = 40;
                    updateServingEstimates();
                }
            """)
            await page_desktop.wait_for_timeout(300)
            calc_shot = os.path.join(qa_dir, "ml_topic_24_calculator_interactive.png")
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
        mobile_full_path = os.path.join(qa_dir, "ml_topic_24_light_mobile.png")
        await page_mobile.screenshot(path=mobile_full_path, full_page=True)
        print(f"  [x] Mobile full-page screenshot saved: {mobile_full_path} ({os.path.getsize(mobile_full_path):,} bytes)")

        # Capture key viewports on mobile
        # 1. Hero
        hero_path = os.path.join(qa_dir, "ml_topic_24_mobile_hero.png")
        await page_mobile.screenshot(path=hero_path)
        print(f"  [x] Captured mobile hero viewport")

        # 2. Section 01
        s1 = await page_mobile.query_selector("#sec-01")
        if s1:
            await s1.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s1_path = os.path.join(qa_dir, "ml_topic_24_mobile_sec01_workflow.png")
            await page_mobile.screenshot(path=s1_path)
            print(f"  [x] Captured mobile section 01 viewport")

        # 3. Section 17 (Capstone project)
        s17 = await page_mobile.query_selector("#sec-17")
        if s17:
            await s17.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s17_path = os.path.join(qa_dir, "ml_topic_24_mobile_sec17_capstone.png")
            await page_mobile.screenshot(path=s17_path)
            print(f"  [x] Captured mobile section 17 capstone viewport")

        # 4. Section 21 (Completion Banner)
        s21 = await page_mobile.query_selector("#sec-21")
        if s21:
            await s21.scroll_into_view_if_needed()
            await page_mobile.wait_for_timeout(200)
            s21_path = os.path.join(qa_dir, "ml_topic_24_mobile_completion_banner.png")
            await page_mobile.screenshot(path=s21_path)
            print(f"  [x] Captured mobile completion banner viewport")

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
    print("QA TEST REPORT SUMMARY")
    print("=" * 60)
    print(f"Console Errors: {len(console_errors)}")
    for err in console_errors:
        print(f"  {err}")
    print(f"Page Errors: {len(page_errors)}")
    for err in page_errors:
        print(f"  {err}")

    assert len(console_errors) == 0, f"Found console errors: {console_errors}"
    assert len(page_errors) == 0, f"Found page errors: {page_errors}"
    print("\nALL QA CHECKS PASSED WITH 0 ERRORS AND 0 OVERFLOW!")

if __name__ == "__main__":
    asyncio.run(run_qa())
