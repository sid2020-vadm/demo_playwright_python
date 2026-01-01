from playwright.sync_api import Page, expect


def test_upload_singlefile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#singleFileInput").set_input_files("testdata\/newfile.txt")

    page.locator("button:has-text('Upload Single File')").click()

    msg=page.locator("#singleFileInput")
    expect(msg).to_contain_text("newfile")


def test_upload_multiple_file(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    files =["testdata\/newfile1.txt","testdata\/newfile.txt"]
    page.locator("#multipleFilesInput").set_input_files(files)

    page.locator("button:has-text('Upload Multiple Files')").click()

    msg = page.locator("#multipleFilesStatus")
    expect(msg).to_contain_text("newfile.txt")
    expect(msg).to_contain_text("newfile1.txt")