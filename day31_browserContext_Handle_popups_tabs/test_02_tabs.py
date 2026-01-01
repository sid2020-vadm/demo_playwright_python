from playwright.sync_api import Playwright, expect


def test_tabs(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    # event listener
    page.on("popup", lambda p:p.wait_for_load_state())
    page.locator("#PopUp").click()
    page.wait_for_timeout(3000)

    all_popups = context.pages

    print("total : ",len(all_popups))

    for popup in all_popups:
        print("page url:",popup.url)
        if "Playwright" in (popup.title()):
            popup.locator(".getStarted_Sjon").click()
            popup.wait_for_timeout(3000)
            expect(popup).to_have_title("Installation | Playwright Python")
            popup.close()
