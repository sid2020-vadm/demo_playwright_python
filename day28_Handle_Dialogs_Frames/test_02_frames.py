from playwright.sync_api import Page, expect


def test_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frames =page.frames
    print(len(frames))
    #1
    frame1=page.frame_locator("frame[src='frame_1.html']")
    frame1.locator("input[name='mytext1']").fill("welcome")

    # 2
    # frame1=page.frame(url="https://ui.vision/demo/webtest/frames/frame_1.html")
    # frame1.locator("input[name='mytext1']").fill("welcome")
    # 3
    # frame1 = page.frame("mention name of the frame")
    # frame1.locator("input[name='mytext1']").fill("welcome")