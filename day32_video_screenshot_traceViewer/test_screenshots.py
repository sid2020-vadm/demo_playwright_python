from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import datetime


def test_screenshot_demo(page:Page):
    page.goto("https://demoblaze.com/index.html")

    time_stamp= str(int(time.time()))
    # time_stamp=datetime.datetime.now().strftime(%Y%m%d)

    # page screenshot(partially/visible)
    # page.screenshot(path=f"screenshots/homepage_{time_stamp}.png")

    # full page screenshot
    # page.screenshot(path=f"screenshots/homepage_{time_stamp}.png",
    #                 full_page=True)

    # Element/specific section of the page screenshot
    logo= page.locator("#nava")
    logo.screenshot(path=f"screenshots/logo_{time_stamp}.png")