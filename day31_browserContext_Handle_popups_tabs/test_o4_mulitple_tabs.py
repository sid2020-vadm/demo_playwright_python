from playwright.sync_api import Playwright, expect


def test_tabs(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context = browser.new_context()
    parent_page = context.new_page()
    parent_page.goto("https://testautomationpractice.blogspot.com/")

    #register event
    parent_page.on("page", lambda p:p.wait_for_load_state())

    parent_page.locator("button[onclick='myFunction()']").click()
    parent_page.wait_for_timeout(3000)
    all_pages = context.pages
    print("number os tabs : ",len(all_pages))

    for tab in all_pages:
        print(tab.title())
