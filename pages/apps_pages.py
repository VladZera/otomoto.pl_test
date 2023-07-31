from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

app_store = (By.CLASS_NAME, 'ooa-102yvlg')
google_store_icon = (By.CLASS_NAME, 'ooa-g5lh0b')
apple_store_icon = (By.CLASS_NAME, 'we-button')
google_downloading_page = (By.CLASS_NAME, 'f0UV3d')


class AppPage(BasePage):
    page_url = '/'

    def apple_store_download_page(self):
        self.find(app_store).click()

    def google_store_download_page(self):
        self.find(google_store_icon).click()



