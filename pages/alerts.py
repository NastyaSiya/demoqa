from pages.base_page import BasePage
from components.components import WebElement


class Alert(BasePage):

    def __init__(self, driver):
        base_url = 'https://demoqa.com/allert.py'
        self.btn = WebElement(driver, '#alertButton')
        self.btn2 = WebElement(driver, '#confirmButton')
        self.btn3 = WebElement(driver, '#promtButton')
        self.block = WebElement(driver, '#confirmResult')
        self.block1 = WebElement(driver, '#promptResult')

        super().__init__(driver, base_url)
