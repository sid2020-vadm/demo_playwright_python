import pytest
from playwright.sync_api import expect, Playwright, Page
import json
file_path="E:\win7_backup_25-08-2025\Pycharm_IDE\Pavan_Python\Pytest_Basics_Pavan\/testdata\login_data.json"
with open(file_path,"r") as file:
    login_data = json.load(file)
# [data["email"],data["password"],data["validity"]]
@pytest.mark.parametrize("email,password,validity", [tuple(data.values()) for data in login_data]) # Convert dictionary values to tuple (preserve order of keys)
def test_login_data_driven_json(email,password,validity,page:Page):
    page.goto("https://demowebshop.tricentis.com/login")
    # fill the form
    page.locator("#Email").fill(email)
    page.locator("#Password").fill(password)
    page.locator("input[value='Log in']").click()

    if validity =="valid":
        expect(page.locator("a[href='/logout']")).to_be_visible(timeout=3000)
    else:
        expect(page.locator(".validation-summary-errors")).to_be_visible(timeout=3000)
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")




