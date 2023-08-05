from pages.base_page import BasePage
from pages.locators import apps_pages_locators as loc


class AppPage(BasePage):
    page_url = '/'

    def apple_store_download_page(self):
        self.find(loc.app_store).click()

    def google_store_download_page(self):
        self.find(loc.google_store_icon).click()
