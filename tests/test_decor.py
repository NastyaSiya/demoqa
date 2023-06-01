from pages.demoqa import DemoQa
from pages.radio_button import RadioButton
import pytest


@pytest.mark.skip
def test_decor(browser):
    p_demoqa = DemoQa(browser)
    p_demoqa.visit()
    assert p_demoqa.zag.check_count_elements(6)

    for element in p_demoqa.zag.find_elements():
        assert element.text != ''


#@pytest.mark.skipif(False, reason='prosto propusk')
def test_r_b(browser):
    p_rad_b = RadioButton(browser)

    if not p_rad_b.code_status():
        pytest.skip(reason=f'Stranitsa {p_rad_b.base_url} nedostupna')

    p_rad_b.visit()
    p_rad_b.yes.click()
    assert p_rad_b.txt.exist()
    assert p_rad_b.txt.get_text() == 'Yes'

    p_rad_b.imp.click()
    assert p_rad_b.txt.exist()
    assert p_rad_b.txt.get_text() == 'Impressive'

    assert "disabled" in p_rad_b.no.get_dom_attribute('class')


