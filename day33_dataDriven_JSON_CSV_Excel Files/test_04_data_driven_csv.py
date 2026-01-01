import pytest
from playwright.sync_api import expect, Playwright, Page
import csv

with open("testdata/data.csv",newline='',encoding='utf-8') as file:
    csv_file =csv.DictReader(file)

@pytest.mark.parametrize("email,password,validity", [tuple(row.values()) for row in csv_file]) # Convert dictionary values to tuple (preserve order of keys)
def test_login_data_driven_csv(email,password,validity,page:Page):
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




