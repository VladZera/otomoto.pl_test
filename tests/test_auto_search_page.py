from pages.auto_search_page import AutoSearchPage
from time import sleep


def test_submit_button(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    search_auto_page.cookies()
    driver.implicitly_wait(10)
    search_auto_page.clicking_result_button()
    assert search_auto_page.all_auto_for_sale_page_is_opened


def test_sell_button_is_work(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    search_auto_page.cookies()
    driver.implicitly_wait(10)
    search_auto_page.sell_button_clicking
    assert search_auto_page.create_sale_car_button_is_displayed


def test_recommendation_price_system(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    search_auto_page.cookies()
    driver.implicitly_wait(10)
    search_auto_page.sell_button_clicking
    search_auto_page.recommendation_price_button_clicking()
    assert search_auto_page.recommendation_price_button_submit_is_displayed


def test_all_bmw_autos_choose(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    search_auto_page.cookies()
    driver.implicitly_wait(10)
    search_auto_page.bmw_brand_choose()
    search_auto_page.clicking_result_button()
    assert driver.current_url == 'https://www.otomoto.pl/osobowe/bmw'


