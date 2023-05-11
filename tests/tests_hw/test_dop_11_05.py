from pages.saucedemo import SauceDemo
from pages.sausedemokorzina import SauseDemoKorzina
from pages.saucekatalog import SauceKatalog


def test_form(browser):
    sauce_page = SauceDemo(browser)
    sauce_page.visit()
    sauce_page.username.send_keys('standard_user')
    sauce_page.password.send_keys('secret_sauce')
    sauce_page.btn_submit.click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html'


def test_korzina(browser):
    sauce_page = SauceDemo(browser)
    sauce_katalog = SauceKatalog(browser)
    sauce_korzina = SauseDemoKorzina(browser)

    sauce_page.visit()
    sauce_page.username.send_keys('standard_user')
    sauce_page.password.send_keys('secret_sauce')
    sauce_page.btn_submit.click()
    sauce_katalog.btn_kof_korz.click()
    sauce_katalog.btn_ruk_korz.click()
    sauce_katalog.btn_korz.click()
    assert sauce_korzina.tovar1.exist()
    assert sauce_korzina.tovar2.exist()
    sauce_korzina.btn_del_tovar1.click()
    sauce_korzina.btn_del_tovar2.click()
    assert not sauce_korzina.tovar1.exist()
    assert not sauce_korzina.tovar2.exist()
    assert not sauce_korzina.marker.exist()
