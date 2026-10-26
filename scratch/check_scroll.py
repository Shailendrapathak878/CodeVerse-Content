import asyncio
import os
from playwright.async_api import async_playwright

async def check():
    html_path = os.path.abspath(os.path.join('coding', 'machine_learning', 'topic_24', 'notes.html'))
    file_url = f"file:///{html_path.replace(os.sep, '/')}"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 390, 'height': 844}, is_mobile=True)
        await page.goto(file_url, wait_until='networkidle')
        res = await page.evaluate('''() => {
            return {
                docScroll: document.documentElement.scrollWidth,
                docClient: document.documentElement.clientWidth,
                bodyScroll: document.body.scrollWidth,
                bodyClient: document.body.clientWidth,
            }
        }''')
        print("Page dimensions:", res)

        # Find which direct children of body or page-container exceed 390px
        offenders = await page.evaluate('''() => {
            const pageContainer = document.querySelector('.page-container');
            const bad = [];
            for (const child of pageContainer.children) {
                if (child.scrollWidth > 390 || child.clientWidth > 390 || child.getBoundingClientRect().width > 390) {
                    bad.push({
                        tag: child.tagName,
                        id: child.id,
                        className: child.className,
                        scrollWidth: child.scrollWidth,
                        clientWidth: child.clientWidth,
                        rectWidth: child.getBoundingClientRect().width
                    });
                }
            }
            return bad;
        }''')
        print("Offenders in page-container:", offenders)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(check())
