import asyncio
import os
from playwright.async_api import async_playwright

async def find_overflow():
    html_path = os.path.abspath(os.path.join("coding", "machine_learning", "topic_24", "notes.html"))
    file_url = f"file:///{html_path.replace(os.sep, '/')}"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 390, "height": 844},
            is_mobile=True
        )
        page = await context.new_page()
        await page.goto(file_url, wait_until="networkidle")

        overflowing_elements = await page.evaluate("""
            () => {
                const elements = document.querySelectorAll('*');
                const overflowing = [];
                for (const el of elements) {
                    const rect = el.getBoundingClientRect();
                    if (rect.width > 390 || rect.right > 395) {
                        overflowing.push({
                            tag: el.tagName,
                            id: el.id,
                            className: el.className,
                            width: Math.round(rect.width),
                            right: Math.round(rect.right),
                            htmlPreview: el.outerHTML.substring(0, 100)
                        });
                    }
                }
                return overflowing;
            }
        """)

        print(f"Total overflowing elements on mobile: {len(overflowing_elements)}")
        for el in overflowing_elements[:15]:
            print(f"Tag: {el['tag']} | class: {el['className']} | width: {el['width']}px | right: {el['right']}px | preview: {el['htmlPreview']}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(find_overflow())
