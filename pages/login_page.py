from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from pages.locators import login_page_locators as loc


class LoginPage:
    base_url = 'https://login.otomoto.pl/?client_id=1l7s2rtc114dc9uqu87n8fm27&code_challenge=x35cB60U3xDXw9A6l' \
               'XFRtTlozIuH4Jtq58eNksBK_A4&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fwww.otomoto.' \
               'pl%2Fauthentication%2Foauthverify&state=I4Ek7M8u828o9lzBDMEGOygFR7pFOyBS'
    page_url = '/'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened by URL')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def enter_email(self, email):
        self.find(loc.user_email).send_keys(email)

    def enter_password(self, password):
        self.find(loc.user_passwd).send_keys(password)

    @property
    def email_message_error(self):
        return self.find(loc.error_text_email)

    @property
    def password_message_error(self):
        return self.find(loc.error_text_passwd)

    @property
    def login_button(self):
        return self.find(loc.login_button)

    @property
    def account_not_exist(self):
        return self.find(loc.email_not_registered)

    def login_button_clicking(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.find(loc.login_button_click)))
        self.find(loc.login_button_click).click()

    def cookies(self):
        try:
            button_cookie = self.find(loc.cookies)
            button_cookie.click()
        except NoSuchElementException:
            pass
