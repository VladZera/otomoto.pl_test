from pages.auto_parts_page import PartsPage
from pages.results import ResultsPage
from pages.auto_parts_page import PartsSearchPage
from pages.results import FelgiPage
from time import sleep


def test_all_auto_parts_without_any_filters(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    auto_parts_page.cookies()
    driver.implicitly_wait(3)
    auto_parts_page.clicking_result_button()
    driver.implicitly_wait(3)
    results_parts_page = ResultsPage(driver)
    assert results_parts_page.auto_parts_filters_is_displayed


def test_advanced_filter_button(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    auto_parts_page.cookies()
    driver.implicitly_wait(3)
    auto_parts_page.clicking_result_button()
    results_parts_page = ResultsPage(driver)
    assert results_parts_page.auto_parts_filters_is_displayed


def test_parts_for_abarth(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    auto_parts_page.cookies()
    driver.implicitly_wait(3)
    auto_parts_page.abarth_parts()



def test_search_bar(driver):
    search_page = PartsSearchPage(driver)
    search_page.open_page()
    search_page.cookies()
    driver.implicitly_wait(5)
    search_page.entering_searching_bar('Felgi')
    search_page.clicking_submit()
    driver.implicitly_wait(5)
    result_search_felgi = FelgiPage
    assert result_search_felgi




sleep(5)
