from playwright.async_api import async_playwright

browser = None
page = None

async def start_browser():
    global browser, page
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()

async def close_browser():
    global browser
    await browser.close()

async def click(text):
    global page
    await page.click(f"text={text}")

async def goto(url):
    global page
    await page.goto(url)

async def getTitle():
    global page
    print("1")
    title = await page.title()
    print("2")
    return title