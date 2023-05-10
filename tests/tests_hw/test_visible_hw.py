from pages.according import Accordion
import time


def test_visible_according(browser):
    demo_qa_according = Accordion(browser)
    demo_qa_according.visit()
    assert demo_qa_according.el.visible()
    demo_qa_according.el1.click()
    time.sleep(2)
    assert not demo_qa_according.el.visible()


def test_visible_accortian_default(browser):
    demo_qa_accordian = Accordion(browser)
    demo_qa_accordian.visit()
    assert not demo_qa_accordian.el2.visible()
    assert not demo_qa_accordian.el3.visible()
    assert not demo_qa_accordian.el4.visible()
