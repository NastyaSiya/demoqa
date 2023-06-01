from pages.base_page import BasePage
from components.components import WebElement


class RadioButton(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.no = WebElement(driver, 'div.custom-control.disabled.custom-radio.custom-control-inline > label')
        self.yes = WebElement(driver, 'div:nth-child(2) > label')
        self.txt = WebElement(driver, 'p > span')
        self.imp = WebElement(driver, 'div:nth-child(3) > label')
