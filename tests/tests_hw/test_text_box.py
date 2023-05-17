import time

from pages.demoqa_textbox import DemoqaTextBox


def test_check(browser):
    demoqa_t_box = DemoqaTextBox(browser)

    pole1_znach1 = 'vvvvvyyyyy'
    pole2_znach2 = 'bbbbbbsssss'

    demoqa_t_box.visit()
    demoqa_t_box.pole1.send_keys(pole1_znach1)
    demoqa_t_box.pole2.send_keys(pole2_znach2)
    demoqa_t_box.btn_submit.click_force()
    time.sleep(2)
    assert demoqa_t_box.znach1.get_text() == ('Name:' + pole1_znach1)
    assert demoqa_t_box.znach2.get_text() == ('Current Address :' + pole2_znach2)
