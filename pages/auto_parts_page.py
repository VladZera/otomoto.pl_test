from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from pages.locators import auto_parts_page_locators as loc


class PartsPage(BasePage):
    page_url = '/?category=czesci'

    def clicking_result_button(self):
        self.find(loc.result_button).click()

    def finding_parts_manualy(self, phrase):
        self.find(loc.input_parts_info).send_keys(phrase)

    def model_choosing_parts(self, brand):
        self.find(loc.auto_model_list).click()
        self.click_option(brand)

    def abarth_parts_page_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/czesci/samochodowe/abarth/'))
        return True

    def audi_parts_page_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/czesci/samochodowe/audi/'))
        return True

    def abarth_parts_page_opened_manualy(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/czesci/samochodowe/q-Abarth/'))
        return True

    def volkswagen_parts_are_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/czesci/samochodowe/volkswagen/'))
        return True


class PartsSearchPage(BasePage):
    page_url = '/czesci/samochodowe/'

    def entering_searching_bar(self, phrase):
        self.find(loc.search_bar).send_keys(phrase)

    def clicking_submit(self):
        self.find(loc.submit_search).click()

    def entering_searching_bar_2(self, phrase):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.adv))
        self.find(loc.search_bar).send_keys(phrase)

    def abarth_parts_page_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/czesci/samochodowe/abarth/'))
        print('Abarth parts page is opened')

    def clicking_advanced_filter_button(self):
        self.find(loc.advanced_filter_button).click()
