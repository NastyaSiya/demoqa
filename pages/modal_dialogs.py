from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn1_5 = WebElement(driver, '#item-2')
        self.icon = WebElement(driver, 'header > a > img')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.dom_small_modal = WebElement(driver, 'div.modal-body')
        self.cls_small_modal = WebElement(driver, '#closeSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.dom_large_modal = WebElement(driver, 'div.fade.modal.show > div > div')
        self.cls_large_modal = WebElement(driver, '#closeLargeModal')
