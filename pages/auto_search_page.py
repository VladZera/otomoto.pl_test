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

    def bmw_brand_choose(self):
        self.find(dropdown).click()
        self.find(brand_choose).click()
        self.click_option('BMW')



