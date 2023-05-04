from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_url_click_url(browser):
    demo_qa_page_1 = DemoQa(browser)
    demo_qa_page_1.visit()
    assert demo_qa_page_1.equal_url()
    demo_qa_page_1.btn_elements.click()
    demo_qa_page_2 = ElementsPage(browser)
    assert demo_qa_page_2.equal_url()
