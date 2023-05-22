from pages.demoqa import DemoQa
from pages.according import Accordion
from pages.alerts import Alert
from pages.browser_tab import BrowserTab
import pytest


@pytest.mark.parametrize('pages', [Accordion, Alert, DemoQa, BrowserTab])
def test_seo(browser, pages):
    page = pages(browser)

    page.visit()
    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == 'viewport'
    assert page.metaView.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
    