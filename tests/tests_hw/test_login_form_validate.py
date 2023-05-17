from pages.form_page import FormPage


def test_login_form_vaildate(browser):
    login_form_p = FormPage(browser)
    login_form_p.visit()
    assert login_form_p.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert login_form_p.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert login_form_p.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert login_form_p.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    login_form_p.btn_submit.click()
    assert login_form_p.form.get_dom_attribute('class') == 'was-validated'


