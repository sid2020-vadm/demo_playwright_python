
from playwright.sync_api import Playwright, sync_playwright, expect, Page
# need to install pytest-rerunfailures
# pip install rerunfailures
# pytest .\test_flaky.py --headed --reruns 2 --reruns-delay 2
def test_login(page:Page):
    page.goto("https://demoblaze.com/index.html")
    page.locator("#login2").click()
    page.locator("#loginusername").fill("sid2025")
    page.locator("#loginpassword").fill("Siddu@2025")
    page.locator("button[onclick='logIn()']").click()
    page.wait_for_timeout(5000)
    expect(page.locator("#logout2")).to_be_visible()
