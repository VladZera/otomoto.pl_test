from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


result_button = (By.XPATH, '//*[@data-testid="submit-btn"]')
search_bar = (By.ID, 'parts-search-text')
submit_search = (By.ID, 'search-button-group')


class PartsPage(BasePage):
    page_url = '/?category=czesci'

    def clicking_result_button(self):
        self.find(result_button).click()


class PartsSearchPage(BasePage):
    page_url = '/czesci/samochodowe/'

    #def entering_searching_bar(self, phrase):
        #self.find(search_bar).send_keys(phrase)

    def clicking_submit(self):
        self.find(submit_search).click()

    def entering_searching_bar(self, phrase):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(self.find(search_bar)))
        self.find(search_bar).send_keys(phrase)






