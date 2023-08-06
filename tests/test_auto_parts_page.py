from pages.auto_parts_page import PartsPage
from pages.results import ResultsPage
import allure


@allure.feature('All parts without any filters')
def test_all_auto_parts_without_any_filters(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    driver.implicitly_wait(10)
    auto_parts_page.cookies()
    auto_parts_page.clicking_result_button()
    results_parts_page = ResultsPage(driver)
    assert results_parts_page.auto_parts_filters_is_displayed


@allure.feature('All parts without any filters by advanced button')
def test_advanced_filter_button(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    driver.implicitly_wait(10)
    auto_parts_page.cookies()
    auto_parts_page.clicking_result_button()
    results_parts_page = ResultsPage(driver)
    assert results_parts_page.auto_parts_filters_is_displayed


@allure.feature('Parts for Abarth')
def test_parts_for_abarth(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    auto_parts_page.cookies()
    driver.implicitly_wait(10)
    auto_parts_page.model_choosing_parts('Abarth')
    auto_parts_page.clicking_result_button()
    assert auto_parts_page.abarth_parts_page_opened()


@allure.feature('Parts for Abarth by advanced search bar')
def test_manual_search_parts_for_abarth(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    driver.implicitly_wait(10)
    auto_parts_page.cookies()
    auto_parts_page.finding_parts_manualy('Abarth')
    auto_parts_page.clicking_result_button()
    assert auto_parts_page.abarth_parts_page_opened_manualy()


@allure.feature('Parts for Audi')
def test_parts_for_audi(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    auto_parts_page.cookies()
    driver.implicitly_wait(10)
    auto_parts_page.model_choosing_parts('Audi')
    auto_parts_page.clicking_result_button()
    assert auto_parts_page.audi_parts_page_opened


@allure.feature('Parts for Volkswagen')
def test_parts_for_volkswagen(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    auto_parts_page.cookies()
    driver.implicitly_wait(10)
    auto_parts_page.model_choosing_parts('Volkswagen')
    auto_parts_page.clicking_result_button()
    assert auto_parts_page.volkswagen_parts_are_displayed()
