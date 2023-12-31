from pages.moto_search_page import MotoSearchPage
import allure


@allure.feature('All motorcycles page is opened')
def test_all_motorcycles_page_is_opened(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.submit_button_clicking()
    assert motorcycles_page.all_motorcycles_page_is_opened()


@allure.feature('All motorcycles page is opened by advanced filter button')
def test_all_motorcycles_page_is_opened_by_advanced_filter_button(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.advanced_filter_submit_button_clicking()
    assert motorcycles_page.all_motorcycles_page_is_opened()


@allure.feature('Add to favorite art')
def test_add_to_favorite_cart(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.submit_button_clicking()
    motorcycles_page.add_to_favorite_click()
    assert motorcycles_page.add_to_favorite_button_is_working


@allure.feature('Yamaha R125 search by search bar')
def test_manual_search_for_yamaha_r_125(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.submit_button_clicking()
    motorcycles_page.more_filters_button_clicking()
    motorcycles_page.finding_moto_manualy_by_search_bar('Yamaha R125')
    motorcycles_page.search_bar_submit_button_clicking()
    assert motorcycles_page.all_yamaha_r_125_results_is_opened()


@allure.feature('All AJP motorcycles are chosen')
def test_ajp_brand_from_the_list(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.brand_choose('AJP')
    motorcycles_page.submit_button_clicking()
    assert motorcycles_page.all_ajp_motos_are_presented()


@allure.feature('Yamaha R125 chosen with price parametrize')
def test_finding_moto_by_brand_and_price(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.brand_choose('Yamaha')
    motorcycles_page.price_from_choose('10 000')
    motorcycles_page.price_for_choose('15 000')
    motorcycles_page.submit_button_clicking()
    assert motorcycles_page.yamaha_from_10000_up_to_1500_is_opened()
