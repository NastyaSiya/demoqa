from pages.base_page import BasePage
from components.components import WebElement


class Webtables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://Demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.block = WebElement(driver, 'div:nth-child(7) > div > div:nth-child(4)')
        self.btn_del_all = WebElement(driver, "span[title='Delete']")
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_sbm = WebElement(driver, '#submit')
        self.forma = WebElement(driver, '#userForm')
        self.p_fn = WebElement(driver, '#firstName')
        self.p_ln = WebElement(driver, '#lastName')
        self.p_ue = WebElement(driver, '#userEmail')
        self.p_a = WebElement(driver, '#age')
        self.p_s = WebElement(driver, '#salary')
        self.p_d = WebElement(driver, '#department')
        self.tab = WebElement(driver, 'div.ReactTable.-striped.-highlight')
        self.tab_str = WebElement(driver, 'div.rt-tbody > div:nth-child(4)')
        self.btn_edit = WebElement(driver, '#edit-record-4 > svg')
        self.btn_del = WebElement(driver, '#delete-record-4 > svg > path')

        self.rows = WebElement(driver, ' span.select-wrap.-pageSizeOptions > select')
        self.btn_previous = WebElement(driver, 'div.-previous > button')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.total_pages = WebElement(driver, 'span.-pageInfo > span')
        self.this_page = WebElement(driver, 'input[type=number]')

        self.st_fn = WebElement(driver, 'div:nth-child(1) > div.rt-resizable-header-content')
        self.st_a = WebElement(driver, 'div.rt-th.rt-resizable-header.-sort-asc.-cursor-pointer > div.rt-resizable-header-content')
        self.znach1_st_fn = WebElement(driver, 'div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)')
        self.znach1_st_a = WebElement(driver, 'div.rt-tbody > div:nth-child(1) > div > div:nth-child(3)')
