from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("the-internet.herokuapp.com")
    
    # Provera da li postoje dugmad
    page.wait_for_selector("text=Google претрага", timeout=5000)
    assert page.is_visible("text=Google претрага")
    
    browser.close()

# with sync_playwright() as playwright:
#     run(playwright)