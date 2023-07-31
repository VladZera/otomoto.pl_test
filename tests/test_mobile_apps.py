from pages.apps_pages import AppPage
from pages.results import GoogleResultPage
from pages.results import AppleResultPage


def test_apple_store_link_works(driver):
    apple_store = AppPage(driver)
    apple_store.open_page()
    apple_store.scroll_to(50000)
    apple_store.cookies()
    driver.implicitly_wait(10)
    apple_store.apple_store_download_page()
    apple_download_page = AppleResultPage
    assert apple_download_page.apple_downloading_page_is_opened


def test_google_store_link_works(driver):
    google_store = AppPage(driver)
    google_store.open_page()
    google_store.scroll_to(50000)
    google_store.cookies()
    driver.implicitly_wait(10)
    google_store.google_store_download_page()
    google_download_page = GoogleResultPage
    assert google_download_page.google_downloading_page_is_opened
