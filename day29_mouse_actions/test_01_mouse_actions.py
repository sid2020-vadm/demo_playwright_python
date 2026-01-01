from playwright.sync_api import Page

def test_mouse_action(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    point_me_btn=page.locator(".dropbtn")
    point_me_btn.hover()

    laptop= page.locator(".dropdown-content a").nth(1)
    laptop.hover()

    page.wait_for_timeout(5000)

def test_mouse_right_click(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    right_click_btn=page.locator("locator")
    right_click_btn.click(button="right")

def test_mouse_double_click(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    btn= page.locator("button[ondblclick='myFunction1()']")
    btn.dblclick()

def test_mouse_drag_drop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    source = page.locator("#draggable")
    target= page.locator("#droppable")
    #1
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    #2
    source.drag_to(target)
    page.drag_and_drop(source,target)



