from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


user_email = (By.NAME, 'username')
user_passwd = (By.NAME, 'password')
error_text_email = (By.CLASS_NAME, 'css-sf6wsj')
error_text_passwd = (By.CLASS_NAME, 'css-sf6wsj')
login_button = (By.CLASS_NAME, 'css-1m3y0q6')
email_not_registered = (By.CLASS_NAME, 'css-1kd8jyo')
login_button_click = (By.XPATH, '//*[@data-testid="login-submit-button"]')


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
        self.find(user_email).send_keys(email)

    def enter_password(self, password):
        self.find(user_passwd).send_keys(password)

    @property
    def email_message_error(self):
        return self.find(error_text_email)

    @property
    def password_message_error(self):
        return self.find(error_text_passwd)

    @property
    def login_button(self):
        return self.find(login_button)

    @property
    def account_not_exist(self):
        return self.find(email_not_registered)

    def login_button_clicking(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.find(login_button_click)))
        self.find(login_button_click).click()

    def cookies(self):
        try:
            button_cookie = self.find((By.ID, 'onetrust-accept-btn-handler'))
            button_cookie.click()
        except NoSuchElementException:
            pass




