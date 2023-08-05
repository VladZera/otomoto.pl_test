from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from pages.locators import auto_search_page_locators as loc


class AutoSearchPage(BasePage):
    page_url = '/?category=osobowe'

    def clicking_result_button(self):
        self.find(loc.submit_button).click()

    def trust_button_click(self):
        self.find(loc.trust_accept).click()

    def recommendation_price_button_clicking(self):
        self.find(loc.recommendation_price_button).click()

    @property
    def all_auto_for_sale_page_is_opened(self):
        return self.find(loc.auto_title).is_displayed()

    @property
    def create_sale_car_button_is_displayed(self):
        return self.find(loc.create_sale_car_button).is_displayed()

    @property
    def recommendation_price_button_submit_is_displayed(self):
        return self.find(loc.recommendation_price_button_submit).is_displayed()

    @property
    def sell_button_clicking(self):
        return self.find(loc.sell_button).click()

    def brand_choose(self, brand):
        self.find(loc.brand_choose).click()
        self.click_option(brand)

    def model_choose(self, model):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.model_choose))
        self.find(loc.model_choose).click()
        self.click_option(model)

    def petrol_choose(self, petrol):
        self.find(loc.fuel_choose).click()
        self.click_option(petrol)

    def year_from_choose(self, year):
        self.find(loc.year_from_choose).click()
        self.click_option(year)

    def year_up_choose(self, year):
        self.find(loc.year_up_choose).click()
        self.click_option(year)

    def price_from(self, price):
        self.find(loc.price_from_choose).click()
        self.click_option(price)

    def price_up(self, price):
        self.find(loc.price_up_choose).click()
        self.click_option(price)

    def milage_from(self, km):
        self.find(loc.mileage_from_choose).click()
        self.click_option(km)

    def milage_up(self, km):
        self.find(loc.mileage_up_choose).click()
        self.click_option(km)

    def all_volkswagen_scirocco_on_benzyna_cars_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.scirocco_benzin))
        return True

    def all_bmw_on_diesel_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.all_diesel_bmw))
        return True

    def all_volkswagen_cars_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.all_scirocco))
        return True

    def all_volkswagen_scirocco_cars_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.all_scirocco_cars_are_presented))
        return True

    def all_bmw_cars_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.all_bmw))
        return True

    def all_bmw_cars_from_01_to_02(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.bmw_01_02))
        return True

    def sciroco_page_with_advanced_filters_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.sciroco_with_main))
        return True
