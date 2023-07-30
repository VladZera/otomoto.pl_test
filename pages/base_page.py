from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    base_url = 'https://www.otomoto.pl/'
    page_url = None

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

    def cookies(self):
        try:
            button_cookie = self.find((By.ID, 'onetrust-accept-btn-handler'))
            button_cookie.click()
        except NoSuchElementException:
            pass

    def click_option(self, option_name):
        options = (By.CSS_SELECTOR, '[data-testid="dropdown-item"]')
        for option in options:
            if option_name in option.text:
                option.click()
                break
