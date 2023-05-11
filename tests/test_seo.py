from pages.demoqa import DemoQa


def test_seo(browser):
    demo_qa = DemoQa(browser)

    demo_qa.visit()
    assert browser.title == demo_qa.pageData['title']
