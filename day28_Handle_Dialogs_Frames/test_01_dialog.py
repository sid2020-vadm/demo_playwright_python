from playwright.sync_api import Page, expect


def test_simpl_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    #register event
    # approach 1
    # def handle_dialog(d):
    #     d.accept()
    #
    # page.on("dialog",handle_dialog)
    #approach 2
    page.on("dialog",lambda d:d.accept())
    page.locator("#alertBtn").click()
    page.wait_for_timeout(3000)


def test_confirmation_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.on("dialog",lambda d:d.accept())
    page.on("dialog", lambda d: d.dismiss())
    page.locator("#confirmBtn").click()
    page.wait_for_timeout(3000)

    # expect(page.locator("#demo")).to_have_text("You pressed OK!")
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")



def test_prompt_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.on("dialog",lambda d:d.accept())
    page.on("dialog", lambda d: d.accept('john'))
    # page.on("dialog", lambda d: d.dismiss())
    page.locator("#promptBtn").click()
    page.wait_for_timeout(3000)


    expect(page.locator("#demo")).to_contain_text('john')