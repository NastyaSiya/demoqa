from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn1_5 = WebElement(driver, '#item-2')
        self.icon = WebElement(driver, 'header > a > img')
