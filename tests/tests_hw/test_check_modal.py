import time
from pages.modal_dialogs import ModalDialogs
from pages.alerts import Alert
from pages.webtables import Webtables
from pages.links import Links


def test_check_modal(browser, dostup):
    p_modal = ModalDialogs(browser)

    p_modal.visit()

    p_modal.small_modal.click()
    time.sleep(4)
    assert p_modal.dom_small_modal.exist()
    p_modal.cls_small_modal.click()
    # p_modal.alert().dismiss()
    time.sleep(2)
    assert not p_modal.dom_small_modal.exist()

    p_modal.large_modal.click()
    time.sleep(2)
    assert p_modal.dom_large_modal.exist()
    p_modal.cls_large_modal.click()
    # p_modal.alert().dismiss()
    time.sleep(2)
    assert not p_modal.dom_large_modal.exist()


def test_5_sek(browser):
    p_alert = Alert(browser)

    p_alert.visit()
    p_alert.btn_time_alert.click()
    time.sleep(7)
    assert p_alert.alert()


def test_sortirovka(browser):
    p_webtable = Webtables(browser)

    p_webtable.visit()
    p_webtable.st_fn.click()
    assert p_webtable.znach1_st_fn.get_dom_attribute('class') == 'rt-td'

    p_webtable.st_a.click()
    assert p_webtable.znach1_st_a.get_dom_attribute('class') == 'rt-td'


def test_window_tab(browser):
    p_links = Links(browser)

    p_links.visit()
    assert p_links.link_home.exist()
    assert p_links.link_home.get_text() == 'Home'
    assert p_links.link_home.get_dom_attribute('href') == 'https://demoqa.com'
    p_links.link_home.click()
    assert len(browser.windiw_handles) == 2
