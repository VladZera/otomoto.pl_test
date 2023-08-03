from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

filters_title = (By.CLASS_NAME, 'ds-facets-filter-results-header')
abarth_page_url = 'https://www.otomoto.pl/czesci/samochodowe/abarth/'
google_downloading_page = (By.CLASS_NAME, 'f0UV3d')
apple_downloading_page = (By.CLASS_NAME, 'we-localnav__title__product')


class ResultsPage(BasePage):
    page_url = None

    @property
    def auto_parts_filters_is_displayed(self):
        return self.find(filters_title).is_displayed()


class FelgiPage(BasePage):
    page_url = '/czesci/samochodowe/q-felgi/'


class AbarthPartsPage(BasePage):
    page_url = '/czesci/samochodowe/abarth/'


class GoogleResultPage(BasePage):
    base_url = 'https://play.google.com/store/apps/details?id=pl.otomoto'
    page_url = '/'

    @property
    def google_downloading_page_is_opened(self):
        return self.find(google_downloading_page).is_displayed()


class AppleResultPage(BasePage):
    base_url = 'https://apps.apple.com/us/app/id444086109?ign-mpt=uo%3D4'
    page_url = '/'

    @property
    def apple_downloading_page_is_opened(self):
        return self.find(apple_downloading_page).is_displayed()




