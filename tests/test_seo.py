from pages.demoqa import DemoQa
from pages.according import Accordion
from pages.alerts import Alert
from pages.browser_tab import BrowserTab
import pytest


def test_seo(browser):
    demo_qa = DemoQa(browser)

    demo_qa.visit()
    assert browser.title == 'DEMOQA'


@pytest.mark.parametrize('pages', [Accordion, Alert, DemoQa, BrowserTab])
def test_seo(browser, pages):
    page = pages(browser)

    page.visit()
    assert browser.title == page.pageData['title']
