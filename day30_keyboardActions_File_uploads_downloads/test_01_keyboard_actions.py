from playwright.sync_api import Page

def test_keyboard_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1=page.locator("#input1")
    #1
    input1.focus()
    page.keyboard.insert_text("welcome")
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")

