from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from pages.locators import moto_search_page_locators as loc


class MotoSearchPage(BasePage):
    page_url = '/?category=motocykle-i-quady'

    def submit_button_clicking(self):
        self.find(loc.submit_button).click()

    def all_motorcycles_page_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/motocykle-i-quady'))
        return True

    def advanced_filter_submit_button_clicking(self):
        self.find(loc.advanced_filters_button).click()

    def add_to_favorite_button_is_working(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.sign_in_button))
        return True

    def add_to_favorite_click(self):
        self.find(loc.add_to_favorite).click()

    def more_filters_button_clicking(self):
        self.find(loc.more_filters_button).click()

    def finding_moto_manualy_by_search_bar(self, phrase):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.submit_search_bar_button))
        self.find(loc.manual_search_bar).send_keys(phrase)

    def search_bar_submit_button_clicking(self):
        self.find(loc.submit_search_bar_button).click()

    def all_yamaha_r_125_results_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.yamaha_r125_is_opened))
        return True

    def choosing_model_from_the_list(self):
        self.find(loc.model_choose).click()

    def brand_choose(self, brand):
        self.find(loc.model_choose).click()
        self.click_option(brand)

    def all_ajp_motos_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.ajp_moto))
        return True

    def price_from_choose(self, price):
        self.find(loc.price_from).click()
        self.click_option(price)

    def price_for_choose(self, price):
        self.find(loc.price_for).click()
        self.click_option(price)

    def yamaha_from_10000_up_to_1500_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.yamaha_with_price_filter))
        return True
