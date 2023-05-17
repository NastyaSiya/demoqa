from pages.base_page import BasePage
from components.components import WebElement


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(2) > label')
        self.hobbies_radio_sport = WebElement(driver, '#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label')
        self.user_number = WebElement(driver, '#userNumber')
        self.user_address = WebElement(driver, '#currentAddress')
        self.select_state = WebElement(driver, '#state')
        self.sel_st = WebElement(driver, '#state > div')
        self.state = WebElement(driver, '#state > div > div.css-1hwfws3 > div.css-1wa3eu0-placeholder')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.form = WebElement(driver, '#userForm')
