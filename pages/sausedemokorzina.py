from pages.base_page import BasePage
from components.components import WebElement


class SauseDemoKorzina(BasePage):

    def __init__(self, driver):
        base_url = 'https://www.saucedemo.com/cart.html'
        super().__init__(driver, base_url)

        self.tovar1 = WebElement(driver, '#item_4_title_link > div')
        self.tovar2 = WebElement(driver, '#item_5_title_link > div')
        self.btn_del_tovar1 = WebElement(driver, '#remove-sauce-labs-backpack')
        self.btn_del_tovar2 = WebElement(driver, '#remove-sauce-labs-fleece-jacket')
        self.marker = WebElement(driver, '#shopping_cart_container > a > span')
        self.btn_menu = WebElement(driver, '#react-burger-menu-btn')
        self.btn_menu_logout = WebElement(driver, '#logout_sidebar_link')
