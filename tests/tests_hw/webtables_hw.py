import time
from pages.webtables import Webtables
from selenium.webdriver.common.keys import Keys


def test_webtable_hw(browser):
    web_t_hw = Webtables(browser)
    fn = 'Kev'
    fn_new = 'Vi'
    ln = 'Bol'
    ue = 'em@mail.com'
    a = '35'
    s = '100'
    d = 'HSE'
    n = '\n'
    expect = ''.join([fn, n, ln, n, a, n, ue, n, s, n, d])
    expect_new = ''.join([fn_new, n, ln, n, a, n, ue, n, s, n, d])
    expect_pusto = '       '

    web_t_hw.visit()
    assert web_t_hw.btn_add.exist()

    web_t_hw.btn_add.click()
    time.sleep(2)
    assert web_t_hw.forma.exist()

    web_t_hw.btn_sbm.click()
    assert web_t_hw.forma.get_dom_attribute('class') == 'was-validated'

    web_t_hw.p_fn.send_keys(fn)
    web_t_hw.p_ln.send_keys(ln)
    web_t_hw.p_ue.send_keys(ue)
    web_t_hw.p_a.send_keys(a)
    web_t_hw.p_s.send_keys(s)
    web_t_hw.p_d.send_keys(d)
    web_t_hw.btn_sbm.click()
    time.sleep(2)
    assert not web_t_hw.forma.exist()
    assert web_t_hw.tab_str.exist()
    assert web_t_hw.tab_str.get_text() == expect

    web_t_hw.btn_edit.click()
    assert web_t_hw.forma.exist()
    assert web_t_hw.p_fn.get_dom_attribute('value') == fn
    assert web_t_hw.p_ln.get_dom_attribute('value') == ln
    assert web_t_hw.p_ue.get_dom_attribute('value') == ue
    assert web_t_hw.p_a.get_dom_attribute('value') == a
    assert web_t_hw.p_s.get_dom_attribute('value') == s
    assert web_t_hw.p_d.get_dom_attribute('value') == d

    web_t_hw.p_fn.send_keys(Keys.CONTROL+'a')
    web_t_hw.p_fn.send_keys(Keys.DELETE)
    web_t_hw.p_fn.send_keys(fn_new)
    web_t_hw.btn_sbm.click()
    time.sleep(2)
    assert web_t_hw.tab_str.get_text() == expect_new

    web_t_hw.btn_del.click()
    assert web_t_hw.tab_str.get_text() == expect_pusto


def test_webtables_hw2(browser):
    web_t_hw = Webtables(browser)
    fn = 'Kev'
    ln = 'Bol'
    ue = 'em@mail.com'
    a = '35'
    s = '100'
    d = 'HSE'

    web_t_hw.visit()
    web_t_hw.rows.click()
    web_t_hw.rows.send_keys(Keys.ARROW_UP)
    web_t_hw.rows.send_keys(Keys.ENTER)

    assert web_t_hw.btn_previous.get_dom_attribute('disabled')
    assert web_t_hw.btn_next.get_dom_attribute('disabled')

    for i in range(3):
        web_t_hw.btn_add.click()
        web_t_hw.p_fn.send_keys(fn)
        web_t_hw.p_ln.send_keys(ln)
        web_t_hw.p_ue.send_keys(ue)
        web_t_hw.p_a.send_keys(a)
        web_t_hw.p_s.send_keys(s)
        web_t_hw.p_d.send_keys(d)
        web_t_hw.btn_sbm.click()

    assert not web_t_hw.btn_next.get_dom_attribute('disabled')
    assert web_t_hw.total_pages.get_text() == '2'

    web_t_hw.btn_next.click()
    assert web_t_hw.this_page.get_dom_attribute('value') == '2'

    web_t_hw.btn_previous.click()
    assert web_t_hw.this_page.get_dom_attribute('value') == '1'
