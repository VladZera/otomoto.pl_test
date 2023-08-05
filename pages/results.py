from pages.base_page import BasePage
from pages.locators import results_page_locators as loc


class ResultsPage(BasePage):
    page_url = None

    @property
    def auto_parts_filters_is_displayed(self):
        return self.find(loc.filters_title).is_displayed()


class GoogleResultPage(BasePage):
    base_url = 'https://play.google.com/store/apps/details?id=pl.otomoto'
    page_url = '/'

    @property
    def google_downloading_page_is_opened(self):
        return self.find(loc.google_downloading_page).is_displayed()


class AppleResultPage(BasePage):
    base_url = 'https://apps.apple.com/us/app/id444086109?ign-mpt=uo%3D4'
    page_url = '/'

    @property
    def apple_downloading_page_is_opened(self):
        return self.find(loc.apple_downloading_page).is_displayed()
