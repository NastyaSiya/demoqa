from test_koup.page.koup import Koup
from test_koup.page.koup_add import KoupAdd


def test_btn_add(browser):
    koup = Koup(browser)
    koup_add = KoupAdd(browser)

    koup.visit()
    assert koup.btn_add.exist()
    koup.btn_add.click()
    assert koup_add.btn_add_elem.exist()
    assert koup_add.btn_add_elem.get_text() == 'Add Element'

    for i in range(4):
        koup_add.btn_add_elem.click()

    assert koup_add.btn_add_del.check_count_elements(4)

    for element in koup_add.btn_add_del.find_elements():
        assert element.text == 'Delete'

    # for i in [0, 1, 2, 3]:
    #     koup_add.btn_add_del.click()

    while koup_add.btn_add_del.exist():
        koup_add.btn_add_del.click()

    assert not koup_add.btn_add_del.exist()
