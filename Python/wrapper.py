from playwright.sync_api import sync_playwright

browser = None
page = None

def start_browser():
    global browser, page
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()


def close_browser():
    global browser
    browser.close

def set_page(page_obj):
    global page
    page = page_obj

def click(text):
    global page

    page.get_by_text(text).click()
    # page.get_by_text("Add/Remove Elements").click()

def goto(url):
    global page
    page.goto(url)