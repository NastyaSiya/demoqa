from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        self.el = WebElement(driver, '#section1Content > p')
        self.el1 = WebElement(driver, '#section1Heading')
        self.el2 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.el3 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.el4 = WebElement(driver, '#section3Content > p')
        super().__init__(driver, self.base_url)
