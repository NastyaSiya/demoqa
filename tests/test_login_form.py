import time
from selenium.webdriver.common.keys import Keys

from pages.form_page import FormPage


def test_login_form(browser):
    formp = FormPage(browser)

    formp.visit()
    assert not formp.modal_dialog.exist()
    time.sleep(2)
    formp.first_name.send_keys('test')
    formp.last_name.send_keys('tester')
    formp.user_email.send_keys('bhjnk@gmail.com')
    formp.gender_radio_1.click_force()
    formp.user_number.send_keys('89999999999')
    formp.hobbies_radio_sport.click_force()
    formp.user_address.send_keys('fghjklkjhgfhjkl')
    time.sleep(2)
    formp.btn_submit.click_force()
    time.sleep(2)
    assert formp.modal_dialog.exist()
    formp.btn_close_modal.click_force()


def test_form_state(browser):
    formp = FormPage(browser)
    formp.visit()
    formp.state.send_keys('NCR')
    formp.state.send_keys(Keys.ENTER)
    time.sleep(5)


def test_form(browser):
    formp = FormPage(browser)
    formp.visit()
    formp.sel_st.click_force()
    time.sleep(5)


def test_form_s(browser):
    formp = FormPage(browser)
    formp.visit()
    formp.state.scroll_to_element()
    formp.state.click()
    formp.state.send_keys(Keys.PAGE_DOWN)
    formp.state.send_keys(Keys.ENTER)
