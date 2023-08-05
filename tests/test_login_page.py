from pages.login_page import LoginPage


def test_log_in_error_when_incorrect_email(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    driver.implicitly_wait(10)
    login_page.cookies()
    login_page.enter_email('aaaaaaaa.com')
    assert login_page.email_message_error.is_displayed()


def test_log_in_error_when_short_password(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    driver.implicitly_wait(10)
    login_page.cookies()
    login_page.enter_password('12345')
    assert login_page.password_message_error.is_displayed()


def test_login_button_is_visible_when_email_and_passwd_correct(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    driver.implicitly_wait(10)
    login_page.cookies()
    login_page.enter_email('1234@gmail.com')
    login_page.enter_password('Aa12345678!')
    assert login_page.login_button.is_displayed()


def test_warning_account_not_exist(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.cookies()
    login_page.enter_email('1234@gmail.com')
    login_page.enter_password('Aa12345678!')
    driver.implicitly_wait(5)
    login_page.cookies()
    login_page.login_button_clicking()
    assert login_page.account_not_exist.is_displayed()
