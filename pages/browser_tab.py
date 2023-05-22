from pages.base_page import BasePage
from components.components import WebElement


class BrowserTab(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/browser-windows'
        self.new_tab = WebElement(driver, '#tabButton')
        self.tab_tab = WebElement(driver, '#tabButton')

        super().__init__(driver, self.base_url)
