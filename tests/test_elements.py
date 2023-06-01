from pages.elements_page import ElementsPage

def test_count_elements(browser):
    elemp = ElementsPage(browser)
    elemp.visit()
    assert elemp.btns_first_menu.check_count_elements(9)
