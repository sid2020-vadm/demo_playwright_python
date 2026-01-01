import pytest
from playwright.sync_api import expect, Playwright, Page

search_items=['laptop','Gift card','smartphone','monitor']

@pytest.mark.parametrize("item",['laptop','Gift card','smartphone','monitor'])
def test_search_items(page:Page,item):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill(item)
    page.locator("input[class='button-1 search-box-button']").click()

    # assertion
    expect(page.locator("h2 a").nth(0)).to_contain_text("laptop",ignore_case=True)



