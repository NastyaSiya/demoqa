from pages.demoqa_textbox import DemoqaTextBox


def test_placeholder(browser):
    demoqa_t_box = DemoqaTextBox(browser)
    demoqa_t_box.visit()
    assert demoqa_t_box.pole1.get_dom_attribute('placeholder') == 'Full Name'
