from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

submit_button = (By.XPATH, '//*[@data-testid="submit-btn"]')
advanced_filters_button = (By.XPATH, '//*[@data-testid="advanced-search-link"]')
sign_in_button = (By.XPATH, '//*[@data-testid="sign-in-button"]')
add_to_favorite = (By.CLASS_NAME, 'e1t8pd740')
more_filters_button = (By.CLASS_NAME, 'ooa-1tn9tf5')
manual_search_bar = (By.CSS_SELECTOR, '[aria-label="Wpisz model, wersję lub inne szczegóły"]')
submit_search_bar_button = (By.CLASS_NAME, 'ooa-10ry9s3')
dropdown = (By.CSS_SELECTOR, '[data-testid="dropdown-item"]')
model_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[2]')
price_from = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[4]')
price_for = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[5]')


class MotoSearchPage(BasePage):
    page_url = '/?category=motocykle-i-quady'

    def submit_button_clicking(self):
        self.find(submit_button).click()

    def all_motorcycles_page_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/motocykle-i-quady'))
        return True

    def advanced_filter_submit_button_clicking(self):
        self.find(advanced_filters_button).click()

    def add_to_favorite_button_is_working(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(sign_in_button))
        return True

    def add_to_favorite_click(self):
        self.find(add_to_favorite).click()

    def more_filters_button_clicking(self):
        self.find(more_filters_button).click()

    def finding_moto_manualy_by_search_bar(self, phrase):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(submit_search_bar_button))
        self.find(manual_search_bar).send_keys(phrase)

    def search_bar_submit_button_clicking(self):
        self.find(submit_search_bar_button).click()

    def all_yamaha_r_125_results_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/motocykle-i-quady/q-Yamaha-R125?search%5Badvanced_search_expanded%5D=true'))
        return True

    def choosing_model_from_the_list(self):
        self.find(model_choose).click()

    def ajp_brand_choose(self):
        self.find(model_choose).click()
        self.click_option('AJP')

    def all_ajp_motos_are_presented(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/motocykle-i-quady/ajp'))
        return True

    def yamaha_brand_choose(self):
        self.find(model_choose).click()
        self.click_option('Yamaha')

    def price_from_10000_choose(self):
        self.find(price_from).click()
        self.click_option('10 000')

    def price_for_15000_choose(self):
        self.find(price_for).click()
        self.click_option('15 000')

    def yamaha_from_10000_up_to_1500_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.otomoto.pl/motocykle-i-quady/yamaha?search%5Bfilter_float_price%3Afrom%5D=10000&search%5Bfilter_float_price%3Ato%5D=15000'))
        return True


