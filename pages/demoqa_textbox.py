from pages.base_page import BasePage
from components.components import WebElement


class DemoqaTextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.pole1 = WebElement(driver, '#userName')
        self.pole2 = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.znach1 = WebElement(driver, '#name')
        self.znach2 = WebElement(driver, '#output > div > #currentAddress')
