import pytest
from playwright.sync_api import expect, Playwright, Page

login_test_data=[("abcd@gmail.com","test123","valid"),
                 ("fsgsj@gmail.com","test2345","invalid"),
                 ("","","invalid")
                 ]
@pytest.mark.parametrize("username,password,validity",login_test_data)
def test_login_data_driven(username,password,validity,page:Page):
    page.goto("https://demowebshop.tricentis.com/login")
    # fill the form
    page.locator("#Email").fill(username)
    page.locator("#Password").fill(password)
    page.locator("input[value='Log in']").click()

    if validity =="valid":
        expect(page.locator("a[href='/logout']")).to_be_visible(timeout=3000)
    else:
        expect(page.locator(".validation-summary-errors")).to_be_visible(timeout=3000)
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")




