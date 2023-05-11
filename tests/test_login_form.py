import time

from pages.form_page import FormPage


def test_login_form(browser):
    formp = FormPage(browser)

    formp.visit()
    # assert not formp.modal_dialog.exist()
    # time.sleep(2)
    formp.first_name.send_keys('test')
    formp.last_name.send_keys('tester')
    formp.user_email.send_keys('bhjnk@mail.com')
    formp.gender_radio_1.click()
    formp.user_number.send_keys('67890')
    time.sleep(2)
    formp.btn_submit.click()
    time.sleep(2)
