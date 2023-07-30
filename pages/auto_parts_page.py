from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


result_button = (By.XPATH, '//*[@data-testid="submit-btn"]')
search_bar = (By.ID, 'parts-search-text')
submit_search = (By.NAME, 'q')
adv = (By.ID, 'megaboardDiv')
advanced_filter_button = (By.XPATH, '//*[@data-testid="advanced-search-link"]')
auto_model_list = (By.CLASS_NAME, 'ooa-14l7e0q')
options = (By.CSS_SELECTOR, '[data-testid="dropdown-item"]')
trust_button = (By.ID, 'onetrust-accept-btn-handler')
dropdown = (By.ID, 'onetrust-accept-btn-handler')
model_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[2]')


class PartsPage(BasePage):
    page_url = '/?category=czesci'

    def clicking_result_button(self):
        self.find(result_button).click()

    def abarth_parts(self):
        self.find(dropdown).click()
        self.find(model_choose).click()
        self.click_option('Abarth')







class PartsSearchPage(BasePage):
    page_url = '/czesci/samochodowe/'

    #def entering_searching_bar(self, phrase):
        #self.find(search_bar).send_keys(phrase)

    def clicking_submit(self):
        self.find(submit_search).click()

    def entering_searching_bar(self, phrase):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(adv))
        self.find(search_bar).send_keys(phrase)

    def clicking_advanced_filter_button(self):
        self.find(advanced_filter_button).click()








