from pages.base_page import BasePage
from components.components import WebElement


class KoupAdd(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://http://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.btn_add_elem = WebElement(driver, '#content > div > button')
        self.btn_add_del = WebElement(driver, '//*[@id="elements"]/button', 'xpath')
