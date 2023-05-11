from pages.base_page import BasePage
from components.components import WebElement


class SauceKatalog(BasePage):

    def __init__(self, driver):
        base_url = 'https://www.saucedemo.com/inventory.html'
        super().__init__(driver, base_url)

        self.btn_ruk_korz = WebElement(driver, '#add-to-cart-sauce-labs-backpack')
        self.btn_kof_korz = WebElement(driver, '#add-to-cart-sauce-labs-fleece-jacket')
        self.btn_korz = WebElement(driver, '#shopping_cart_container > a')

