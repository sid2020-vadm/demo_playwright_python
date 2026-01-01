import pytest
from playwright.sync_api import expect, Playwright, Page
import openpyxl
login_data =[]
file_path="testdat/login.xlsx"
workbook = openpyxl.load_workbook(file_path)
# sheet = workbook[sheet_name] if sheet_name else workbook.active
sheet = workbook.active
for row in sheet.iter_rows(min_row=2, values_only=True):
    email,password,validity= row
    login_data.append((str(email or ""),str(password or ""),str(validity or "")))

@pytest.mark.parametrize("email,password,validity",login_data) # Convert dictionary values to tuple (preserve order of keys)
def test_login_data_driven_excel(email,password,validity,page:Page):
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




