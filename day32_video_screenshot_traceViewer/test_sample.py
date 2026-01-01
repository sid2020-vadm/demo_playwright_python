from playwright.sync_api import Page ,expect

def test_url(page:Page):
    page.goto("https://demoblaze.com/index.html")
    expect(page).to_have_url("https://demoblaze.com/index.html")

def test_title(page:Page):
    page.goto("https://demoblaze.com/index.html")
    expect(page.title()).to_have_text("STORE")

def test_login(page:Page):
    page.goto("https://demoblaze.com/index.html")
    page.locator("#login2").click()
    page.locator("#loginusername").fill("sid2025")
    page.locator("#loginpassword").fill("Siddu@2025")
    page.locator("button[onclick='logIn()']").click()
    page.wait_for_timeout(3000)
    expect(page.locator("#logout2")).to_be_visible()