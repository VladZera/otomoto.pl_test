import allure
from pages.auto_search_page import AutoSearchPage


@allure.feature('All cars without any filters by submit button')
def test_submit_button(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    search_auto_page.cookies()
    driver.implicitly_wait(10)
    search_auto_page.clicking_result_button()
    assert search_auto_page.all_auto_for_sale_page_is_opened


@allure.feature('Sell button')
def test_sell_button_is_work(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    search_auto_page.cookies()
    driver.implicitly_wait(10)
    search_auto_page.sell_button_clicking
    assert search_auto_page.create_sale_car_button_is_displayed


@allure.feature('Recommendation price page ')
def test_recommendation_price_system(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    search_auto_page.cookies()
    driver.implicitly_wait(10)
    search_auto_page.sell_button_clicking
    search_auto_page.recommendation_price_button_clicking()
    assert search_auto_page.recommendation_price_button_submit_is_displayed


@allure.feature('All BMW autos are chosen')
def test_all_bmw_autos_chosen(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    driver.implicitly_wait(10)
    search_auto_page.cookies()
    search_auto_page.brand_choose('BMW')
    search_auto_page.clicking_result_button()
    assert search_auto_page.all_bmw_cars_are_presented()


@allure.feature('All Volkswagen autos are chosen')
def test_all_volkswagen_autos_chosen(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    driver.implicitly_wait(10)
    search_auto_page.cookies()
    search_auto_page.brand_choose('Volkswagen')
    search_auto_page.clicking_result_button()
    assert search_auto_page.all_volkswagen_cars_are_presented()


@allure.feature('All VW Scirocco are chosen')
def test_all_volkswagen_scirocco_autos_chosen(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    driver.implicitly_wait(10)
    search_auto_page.cookies()
    search_auto_page.brand_choose('Volkswagen')
    search_auto_page.model_choose('Scirocco')
    search_auto_page.clicking_result_button()
    assert search_auto_page.all_volkswagen_scirocco_cars_are_presented()


@allure.feature('All VW Scirocco on benzin are chosen')
def test_all_vw_sciroco_on_benzina(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    driver.implicitly_wait(10)
    search_auto_page.cookies()
    search_auto_page.brand_choose('Volkswagen')
    search_auto_page.model_choose('Scirocco')
    search_auto_page.petrol_choose('Benzyna')
    search_auto_page.clicking_result_button()
    assert search_auto_page.all_volkswagen_scirocco_on_benzyna_cars_are_presented()


@allure.feature('All BMW on diesel are chosen')
def test_all_bmw_on_diesel(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    driver.implicitly_wait(10)
    search_auto_page.cookies()
    search_auto_page.brand_choose('BMW')
    search_auto_page.petrol_choose('Diesel')
    search_auto_page.clicking_result_button()
    assert search_auto_page.all_bmw_on_diesel_are_presented()


@allure.feature('All BMW 2001 - 2002 are chosen')
def test_all_bmw_from_01_to_02_year(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    driver.implicitly_wait(10)
    search_auto_page.cookies()
    search_auto_page.brand_choose('BMW')
    search_auto_page.year_from_choose('2001')
    search_auto_page.year_up_choose('2002')
    search_auto_page.clicking_result_button()
    assert search_auto_page.all_bmw_cars_from_01_to_02()


@allure.feature('Used the most popular parameres')
def test_all_the_main_paramethres(driver):
    search_auto_page = AutoSearchPage(driver)
    search_auto_page.open_page()
    driver.implicitly_wait(10)
    search_auto_page.cookies()
    search_auto_page.brand_choose('Volkswagen')
    search_auto_page.model_choose('Scirocco')
    search_auto_page.price_from('2 000')
    search_auto_page.price_up('200 000')
    search_auto_page.year_from_choose('2008')
    search_auto_page.year_up_choose('2016')
    search_auto_page.clicking_result_button()
    assert search_auto_page.sciroco_page_with_advanced_filters_is_opened()
