from wrapper import * 
webSite = "https://the-internet.herokuapp.com/"
timeout = 1000

def test_add_remove_elements():
    with sync_playwright() as p:
        start_browser()
        click("Add/Remove Elements")
        page.wait_for_timeout(timeout)
        close_browser()

# def test_example_website():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://example.com")
#         assert "Example Domain" in page.title()
#         browser.close()