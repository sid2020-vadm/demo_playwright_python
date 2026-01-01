
from playwright.sync_api import Playwright,sync_playwright,expect

def test_tracing(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context =browser.new_context()

    # start trace
    context.tracing.start(screenshots=True,snapshots=True)

    page= context.new_page()
    page.goto("https://demoblaze.com/index.html")
    page.locator("#login2").click()
    page.locator("#loginusername").fill("sid2025")
    page.locator("#loginpassword").fill("Siddu@2025")
    page.locator("button[onclick='logIn()']").click()
    page.wait_for_timeout(3000)
    expect(page.locator("#logout2")).to_be_visible()

    # stop trace
    context.tracing.stop(path="trace.zip")
    # command to view trace --> playwright show-trace trace.zip

    context.close()
    browser.close()