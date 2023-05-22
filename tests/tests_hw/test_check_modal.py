import time
from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    p_modal = ModalDialogs(browser)

    p_modal.visit()

    p_modal.small_modal.click()
    time.sleep(4)
    assert p_modal.alert()
    p_modal.alert().dismiss()
    time.sleep(2)
    assert not p_modal.alert()

    p_modal.large_modal.click()
    time.sleep(2)
    assert p_modal.alert()
    p_modal.alert().dismiss()
    time.sleep(2)
    assert not p_modal.alert()


