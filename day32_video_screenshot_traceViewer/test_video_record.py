
from playwright.sync_api import Playwright,sync_playwright,expect

def test_video_record(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context =browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width":1024,"height":768}
    )
    page= context.new_page()
    page.goto("https://demoblaze.com/index.html")
    page.locator("#login2").click()
    page.locator("#loginusername").fill("sid2025")
    page.locator("#loginpassword").fill("Siddu@2025")
    page.locator("button[onclick='logIn()']").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#logout2")).to_be_visible()
    context.close()
    browser.close()