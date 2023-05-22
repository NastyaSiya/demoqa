import time

from pages.droppable import Droppable
from selenium.webdriver import ActionChains


def test_drop(browser):
    drop_p = Droppable(browser)
    action_chains = ActionChains(browser)

    drop_p.visit()
    assert drop_p.drop.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(
        drop_p.drag.find_element(),
        drop_p.drop.find_element()
    ).perform()

    time.sleep(2)

    assert drop_p.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')

    action_chains.drag_and_drop_by_offset(drop_p.drag.find_element(), -200, 0).perform()

    assert drop_p.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
