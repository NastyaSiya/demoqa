import time
from pages.demoqa_textbox import DemoqaTextBox


def test_clear(browser):
    demoqa_t_box = DemoqaTextBox(browser)
    demoqa_t_box.visit()
    demoqa_t_box.pole1.send_keys('hgjklbgjhk')
    time.sleep(2)
    demoqa_t_box.pole1.clear()
    time.sleep(2)
    assert demoqa_t_box.pole1.get_text() == ''
