from playwright.sync_api import sync_playwright

webSite = "https://the-internet.herokuapp.com/"
timeout = 1000
locator_add_element = page.locator("//button[contains(text(),'Add Element')]") 

def test_add_remove_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(webSite)

        page.get_by_text("Add/Remove Elements").click()

        element_exists = page.is_visible("text=Add Element")
        
        page.wait_for_timeout(timeout)

        browser.close()

# def test_example_website():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://example.com")
#         assert "Example Domain" in page.title()
#         browser.close()