from pages.apps_pages import AppPage
from pages.results import GoogleResultPage
from pages.results import AppleResultPage
import allure


@allure.feature('Apple store')
@allure.story('Positive case')
def test_apple_store_link_works(driver):
    with allure.step('Open start page'):
        apple_store = AppPage(driver)
        apple_store.open_page()
    with allure.step('Scroll to apple store icon'):
        apple_store.scroll_to(50000)
    with allure.step('Accepting cookies'):
        apple_store.cookies()
    driver.implicitly_wait(10)
    with allure.step('Opening download apple store page'):
        apple_store.apple_store_download_page()
    apple_download_page = AppleResultPage
    with allure.step('Check if right page is opened'):
        assert apple_download_page.apple_downloading_page_is_opened


@allure.feature('Google store')
@allure.story('Positive case')
def test_google_store_link_works(driver):
    with allure.step('Open start page'):
        google_store = AppPage(driver)
        google_store.open_page()
    with allure.step('Scroll to google market store icon'):
        google_store.scroll_to(50000)
    with allure.step('Accepting cookies'):
        google_store.cookies()
    driver.implicitly_wait(10)
    with allure.step('Opening download apple store page'):
        google_store.google_store_download_page()
    google_download_page = GoogleResultPage
    with allure.step('Check if right page is opened'):
        assert google_download_page.google_downloading_page_is_opened
