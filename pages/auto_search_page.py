from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

auto_title = (By.CLASS_NAME, 'ev5apm51')
sell_button = (By.CLASS_NAME, 'e1lnywgt0')
create_sale_car_button = (By.CLASS_NAME, 'ooa-1wc438x')
recommendation_price_button = (By.CLASS_NAME, 'erf630y0')
recommendation_price_button_submit = (By.CLASS_NAME, 'ooa-cnxk22')
trust_accept = (By.ID, 'onetrust-accept-btn-handler')
dropdown = (By.ID, 'onetrust-accept-btn-handler')
submit_button = (By.XPATH, '//*[@data-testid="submit-btn"]')
brand_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[2]')
model_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[3]')
generation_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[4]')
price_from_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[5]')
price_up_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[6]')
year_from_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[7]')
year_up_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[8]')
fuel_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[9]')
mileage_from_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[10]')
mileage_up_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[11]')
bmw_01_02 = 'https://www.otomoto.pl/osobowe/bmw/od-2001?search%5Bfilter_float_year%3Ato%5D=2002'
all_diesel_bmw = 'https://www.otomoto.pl/osobowe/bmw?search%5Bfilter_enum_fuel_type%5D=diesel'
all_bmw = 'https://www.otomoto.pl/osobowe/bmw'
scirocco_benzin = 'https://www.otomoto.pl/osobowe/volkswagen/scirocco?search%5Bfilter_enum_fuel_type%5D=petrol'
all_scirocco = 'https://www.otomoto.pl/osobowe/volkswagen'
sciroco_with_main = 'https://www.otomoto.pl/osobowe/volkswagen/scirocco/od-2008?search%5Bfilter_float_price%3Afrom' \
                    '%5D=2000&search%5Bfilter_float_price%3Ato%5D=200000'


class AutoSearchPage(BasePage):
    page_url = '/?category=osobowe'

    def clicking_result_button(self):
        self.find(submit_button).click()

    def trust_button_click(self):
        self.find(trust_accept).click()

    def recommendation_price_button_clicking(self):
        self.find(recommendation_price_button).click()

    @property
    def all_auto_for_sale_page_is_opened(self):
        return self.find(auto_title).is_displayed()

    @property
    def create_sale_car_button_is_displayed(self):
        return self.find(create_sale_car_button).is_displayed()

    @property
    def recommendation_price_button_submit_is_displayed(self):
        return self.find(recommendation_price_button_submit).is_displayed()

    @property
    def sell_button_clicking(self):
        return self.find(sell_button).click()

    def brand_choose(self, brand):
        self.find(brand_choose).click()
        self.click_option(brand)

    def model_choose(self, model):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(model_choose))
        self.find(model_choose).click()
        self.click_option(model)

    def petrol_choose(self, petrol):
        self.find(fuel_choose).click()
        self.click_option(petrol)

    def year_from_choose(self, year):
        self.find(year_from_choose).click()
        self.click_option(year)

    def year_up_choose(self, year):
        self.find(year_up_choose).click()
        self.click_option(year)

    def price_from(self, price):
        self.find(price_from_choose).click()
        self.click_option(price)

    def price_up(self, price):
        self.find(price_up_choose).click()
        self.click_option(price)

    def milage_from(self, km):
        self.find(mileage_from_choose).click()
        self.open_page(km)

    def milage_up(self, km):
        self.find(mileage_up_choose).click()
        self.open_page(km)

    def all_volkswagen_scirocco_on_benzyna_cars_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(scirocco_benzin))
        return True

    def all_bmw_on_diesel_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(all_diesel_bmw))
        return True

    def all_volkswagen_cars_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(all_scirocco))
        return True

    def all_volkswagen_scirocco_cars_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/osobowe/volkswagen/scirocco'))
        return True

    def all_bmw_cars_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(all_bmw))
        return True

    def all_bmw_cars_from_01_to_02(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(bmw_01_02))
        return True

    def sciroco_page_with_advanced_filters_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(sciroco_with_main))
        return True