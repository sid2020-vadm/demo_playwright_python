from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.prodcuts_list_locator = "h4.card-title a"
        self.add_to_cart_button = self.page.locator(".btn.btn-success.btn-lg")
        self.cart_link = self.page.locator("a[onclick='showcart()']")

    def add_product_to_cart(self, product_name):
        products = self.page.locator(self.prodcuts_list_locator)
        count = products.count()

        for i in range(count):
            name = products.nth(i).text_content().strip()
            if name == product_name:
                products.nth(i).click()
                break

        self.page.on("dialog", lambda dialog: dialog.accept())  # handle dialog
        self.add_to_cart_button.click()

    def goto_cart(self):
        self.cart_link.click()
