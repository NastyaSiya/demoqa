from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage



def test_navigation(browser):
    demo_qa = DemoQa(browser)
    elem = ElementsPage(browser)

    demo_qa.visit()
    demo_qa.btn_elements.click()

    elem.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert elem.equal_url()
