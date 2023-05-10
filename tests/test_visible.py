import time

from pages.elements_page import ElementsPage


def test_visible_btn_sidebar(browser):
    demo_qa_elem = ElementsPage(browser)
    demo_qa_elem.visit()
    # demo_qa_elem.btn_sidebar_first.click()
    # time.sleep(3)
    # assert demo_qa_elem.btn_sidebar_first_textbox.exist()
    assert demo_qa_elem.btn_sidebar_first_textbox.visible()


def test_not_visiable_btn_sidebar(browser):
    demo_qa_elem = ElementsPage(browser)
    demo_qa_elem.visit()
    assert demo_qa_elem.btn_sidebar_first_checkbox.visible()
    demo_qa_elem.btn_sidebar_first.click()
    time.sleep(2)
    assert not demo_qa_elem.btn_sidebar_first_checkbox.visible()

