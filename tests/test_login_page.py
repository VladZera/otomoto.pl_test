from pages.login_page import LoginPage


def test_log_in(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_email('aaaaaaaa.com')
    driver.implicitly_wait(5)
    assert login_page.email_error.is_displayed()
