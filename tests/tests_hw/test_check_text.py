from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_text(browser):
    demo_qa_hw = DemoQa(browser)
    demo_qa_hw.visit()
    assert demo_qa_hw.podval.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_btn_text(browser):
    demo_qa_hw1 = DemoQa(browser)
    demo_qa_hw2 = ElementsPage(browser)
    demo_qa_hw1.visit()
    demo_qa_hw1.btn_hw.click()
    assert demo_qa_hw2.nadpis_tsentr.get_text() == 'Please select an item from left to start practice.'


def test_page_elements(browser):
    demo_qa_elements = ElementsPage(browser)
    demo_qa_elements.visit()
    assert demo_qa_elements.header.get_text() == 'Elements'
    assert demo_qa_elements.icon_head.exist()
    assert demo_qa_elements.btn_sidebar_first.exist()
    assert demo_qa_elements.btn_sidebar_first_textbox.exist()

