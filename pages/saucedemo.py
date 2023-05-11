from pages.base_page import BasePage
from components.components import WebElement


class SauceDemo(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'
        super().__init__(driver, self.base_url)

        self.username = WebElement(driver, '#user-name')
        self.password = WebElement(driver, '#password')
        self.btn_submit = WebElement(driver, '#login-button')
        self.btn_ruk_korz = WebElement(driver, '#add-to-cart-sauce-labs-backpack')
        self.btn_kof_korz = WebElement(driver, '#add-to-cart-sauce-labs-fleece-jacket')
        self.btn_korz = WebElement(driver, '#shopping_cart_container > a')
