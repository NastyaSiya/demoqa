import time

from pages.progress_bar import ProgressBar


def test_progress_bar(browser):
    p_prog_bar = ProgressBar(browser)

    p_prog_bar.visit()
    time.sleep(2)
    # p_prog_bar.start.click()
    # while not p_prog_bar.prog_bar.get_dom_attribute('style') == 'width: 51%;':
    #     p_prog_bar.start.click()
    #
    # assert p_prog_bar.prog_bar.get_dom_attribute('style') == 'width: 51%;'

    p_prog_bar.start.click()
    while True:
        if p_prog_bar.prog_bar.get_dom_attribute('style') == 'width: 51%;':
            p_prog_bar.start.click()
            break
