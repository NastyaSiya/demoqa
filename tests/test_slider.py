from pages.slider import Slider
from selenium.webdriver.common.keys import Keys


def test_slider(browser):
    p_slider = Slider(browser)

    p_slider.visit()
    assert p_slider.slider.exist()
    assert p_slider.pole.exist()
    assert p_slider.slider.get_dom_attribute('value') == '25'
    for i in range(25):
        p_slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert p_slider.pole.get_dom_attribute('value') == '50'


def test_slider_new(browser):
    p_slider = Slider(browser)

    p_slider.visit()
    assert p_slider.slider.exist()
    assert p_slider.pole.exist()
    assert p_slider.slider.get_dom_attribute('value') == '25'
    while not p_slider.slider.get_dom_attribute('value') == '50':
        p_slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert p_slider.pole.get_dom_attribute('value') == '50'
