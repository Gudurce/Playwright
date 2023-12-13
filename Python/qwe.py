from playwright.sync_api import sync_playwright

def test1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Google" in page.title()
        browser.close()

def test_example_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        assert "Example Domain" in page.title()
        browser.close()