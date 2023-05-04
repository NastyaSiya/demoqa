from pages.demoqa import DemoQa


def test_icon_exit(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.icon.exist()
    # assert demo_qa_page.equal_url()
