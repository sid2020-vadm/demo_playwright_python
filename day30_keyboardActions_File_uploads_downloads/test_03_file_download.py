import os.path

from playwright.sync_api import Page

def test_file_download(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#inputText").fill("welcome")
    page.locator("#generateTxt").click()

    page.on("download",lambda d:d.save_as("downloads/testfile.txt"))
    page.locator("#txtDownloadLink").click()

    if os.path.exists("downloads/testfile.txt"):
        print("file exist")
    else:
        print("file not exist")

