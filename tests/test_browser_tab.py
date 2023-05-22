import time

from pages.browser_tab import BrowserTab


def test_browser_tab(browser):
    browser_p = BrowserTab(browser)
    browser_p.visit()
    assert len(browser.window_handles) == 1

    browser_p.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
