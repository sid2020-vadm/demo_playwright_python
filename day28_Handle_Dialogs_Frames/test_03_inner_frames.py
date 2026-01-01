from playwright.sync_api import Page, expect


def test_inner_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frames =page.frames
    print(len(frames))
    frame3=page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html")
    frame3.locator("input[name='mytext3']").fill("welcome")
    child_frames=frame3.child_frames #frames inside frame3
    inner_frame=child_frames[0]
    radio_btn=inner_frame.locator("input[name='mytext3']").check()
    expect(radio_btn).to_be_checked()


