from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        self.nadpis_tsentr = WebElement(driver, 'div.col-12.mt-4.col-md-6')
        self.header = WebElement(driver, 'div.pattern-backgound.playgound-header')
        super().__init__(driver, self.base_url)
