from pages.webtables import Webtables


def test_webtables(browser):
    webtab_p = Webtables(browser)

    webtab_p.visit()
    assert not webtab_p.block.exist()

    while webtab_p.btn_del_all.exist():
        webtab_p.btn_del_all.click()

    assert webtab_p.block.exist()
