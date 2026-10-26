import asyncio
import os
from playwright.async_api import async_playwright

async def run_qa():
    print("Starting Playwright QA for Topic 18: Anomaly Detection...")
    
    html_path = os.path.abspath(os.path.join("coding", "machine_learning", "topic_18", "notes.html"))
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
        desktop_full_path = os.path.join(qa_dir, "ml_topic_18_light_desktop.png")
        await page_desktop.screenshot(path=desktop_full_path, full_page=True)
        print(f"  Desktop full-page screenshot saved: {desktop_full_path} ({os.path.getsize(desktop_full_path)} bytes)")
        
        # Capture individual sections for detailed inspection
        sections_to_capture = [
            ("sec-01", "intro"),
            ("sec-03", "anomaly_outlier_noise"),
            ("sec-05", "class_cluster_anomaly"),
            ("sec-06", "univariate_multivariate"),
            ("sec-07", "zscore"),
            ("sec-08", "iqr"),
            ("sec-10", "isolation_forest"),
            ("sec-11", "lof"),
            ("sec-12", "one_class_svm"),
            ("sec-13", "algorithm_comparison"),
            ("sec-15", "confusion_matrix"),
            ("sec-16", "threshold_sweep"),
            ("sec-17", "mistakes"),
            ("sec-18", "project"),
            ("sec-19", "revision_flowchart"),
            ("sec-20", "accordions")
        ]
        
        for sec_id, name in sections_to_capture:
            el = await page_desktop.query_selector(f"#{sec_id}")
            if el:
                sec_path = os.path.join(qa_dir, f"ml_topic_18_sec_{name}.png")
                await el.screenshot(path=sec_path)
                print(f"  Captured section {sec_id} -> {sec_path}")
            else:
                print(f"  WARNING: Section #{sec_id} not found!")

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
        mobile_full_path = os.path.join(qa_dir, "ml_topic_18_light_mobile.png")
        await page_mobile.screenshot(path=mobile_full_path, full_page=True)
        print(f"  Mobile full-page screenshot saved: {mobile_full_path} ({os.path.getsize(mobile_full_path)} bytes)")
        
        # Mobile Viewports
        # Hero
        hero_path = os.path.join(qa_dir, "ml_topic_18_mobile_hero.png")
        await page_mobile.screenshot(path=hero_path)
        print(f"  Mobile hero viewport saved: {hero_path}")
        
        # Scroll to project
        await page_mobile.evaluate("document.getElementById('sec-18').scrollIntoView()")
        await asyncio.sleep(0.3)
        proj_mobile_path = os.path.join(qa_dir, "ml_topic_18_mobile_project.png")
        await page_mobile.screenshot(path=proj_mobile_path)
        print(f"  Mobile project viewport saved: {proj_mobile_path}")

        # Scroll to mistakes
        await page_mobile.evaluate("document.getElementById('sec-17').scrollIntoView()")
        await asyncio.sleep(0.3)
        mistakes_mobile_path = os.path.join(qa_dir, "ml_topic_18_mobile_mistakes.png")
        await page_mobile.screenshot(path=mistakes_mobile_path)
        print(f"  Mobile mistakes viewport saved: {mistakes_mobile_path}")
        
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
