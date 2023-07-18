from pages.base_page import BasePage
from selenium.webdriver.common.by import By

user_email = (By.NAME, 'username')
user_passwd = (By.NAME, 'password')
email_error = (By.CLASS_NAME, 'css-sf6wsj')


class LoginPage(BasePage):
    login_url = 'login.'
    page_url = '/'

    def enter_email(self, email):
        self.find(user_email).send_keys(email)

    def enter_password(self, password):
        self.find(user_passwd).send_keys(password)


