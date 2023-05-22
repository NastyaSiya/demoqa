import time

from pages.alerts import Alert


def test_allert(browser):
    allert_p = Alert(browser)
    allert_p.visit()
    assert not allert_p.alert()
    allert_p.btn.click()
    time.sleep(2)
    assert allert_p.alert()
    allert_p.alert().accept()


def test_alert_text(browser):
    alert_p = Alert(browser)
    alert_p.visit()
    alert_p.btn.click()
    time.sleep(2)
    assert alert_p.alert().text == 'You clicked a button'
    alert_p.alert().accept()
    assert not alert_p.alert()


def test_alert_2(browser):
    alert_p = Alert(browser)

    alert_p.visit()
    alert_p.btn2.click()
    time.sleep(2)
    alert_p.alert().dismiss()
    assert alert_p.block.get_text() == 'You selected Cancel'


def test_prompt(browser):
    alert_p = Alert(browser)
    a = 'name'

    alert_p.visit()
    alert_p.btn3.click()
    time.sleep(2)
    alert_p.alert().send_keys(a)
    alert_p.alert().accept()
    assert alert_p.block1.get_text() == f'You entered {a}'
