from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()
    assert modal_page.btn1_5.check_count_elements(5)



def test_navigation_modal(browser):
    modal_page = ModalDialogs(browser)
    demo_qa = DemoQa(browser)

    modal_page.visit()
    modal_page.refresh()
    modal_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo_qa.equal_url()
    assert browser.title == demo_qa.pageData['title']
    browser.set_window_size(1000, 1000)
