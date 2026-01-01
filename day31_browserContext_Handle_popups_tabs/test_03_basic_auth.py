# https://the-internet.herokuapp.com/basic_auth

from playwright.sync_api import Playwright, expect


def test_auth_popup(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context = browser.new_context(
        http_credentials={"username":"admin","password":"admin"}
    )
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    expect(page.locator("text=Congratulations")).to_be_visible()
    page.wait_for_timeout(3000)