from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        self.nadpis_tsentr = WebElement(driver, 'div.col-12.mt-4.col-md-6')
        self.header = WebElement(driver, 'div.pattern-backgound.playgound-header')
        self.icon_head = WebElement(driver, 'header > a > img')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div > div.header-right > div.icon > svg')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1)>div>ul>#item-0>span')
        self.btn_sidebar_first_checkbox = WebElement(driver, 'div > div > div:nth-child(1) > div > ul > #item-1')
        super().__init__(driver, self.base_url)
