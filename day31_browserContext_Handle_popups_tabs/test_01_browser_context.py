from playwright.sync_api import Playwright

def test_browser_context(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page1 = context.new_page()
    # page2 = context.new_page()
    # page1.goto("https://testautomationpractice.blogspot.com/")
    # page1.wait_for_timeout(3000)
    # page2.goto("https://tutorialsninja.com/demo/")
    # page2.wait_for_timeout(3000)

    page1.goto("https://testautomationpractice.blogspot.com/")
    page1.wait_for_timeout(3000)
    page1.goto("https://tutorialsninja.com/demo/")
    page1.wait_for_timeout(3000)


