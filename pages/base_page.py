from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    base_url = 'https://www.otomoto.pl/'
    page_url = None
    login_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        if self.login_url:
            self.driver.get(f'{self.login_url}{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened by URL')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)
