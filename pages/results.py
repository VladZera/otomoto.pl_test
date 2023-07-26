from pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


filters_title = (By.CLASS_NAME, 'ds-facets-filter-results-header')


class ResultsPage(BasePage):
    page_url = None

    @property
    def auto_parts_filters_is_displayed(self):
        return self.find(filters_title).is_displayed()


class FelgiPage(BasePage):
    page_url = '/czesci/samochodowe/q-felgi/'

