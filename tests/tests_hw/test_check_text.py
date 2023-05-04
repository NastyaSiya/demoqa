from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_text(browser):
    demo_qa_hw = DemoQa(browser)
    demo_qa_hw.visit()
    if demo_qa_hw.podval.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
        return True
    else:
        return False


def test_btn_text(browser):
    demo_qa_hw1 = DemoQa(browser)
    demo_qa_hw2 = ElementsPage(browser)
    demo_qa_hw1.visit()
    demo_qa_hw1.btn_hw.click()
    if demo_qa_hw2.nadpis_tsentr.get_text() == 'Please select an item from left to start practice.':
        return True
    else:
        return False
