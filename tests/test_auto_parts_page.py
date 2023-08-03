from pages.auto_parts_page import PartsPage
from pages.results import ResultsPage


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
    driver.implicitly_wait(10)
    auto_parts_page.abarth_parts()
    auto_parts_page.clicking_result_button()
    assert auto_parts_page.abarth_parts_page_opened()
    # Этот тест падает. Не выбирает элемент из дропдауна, хотя раньше выбирал и было все ок. В чем дело - непонятно.


def test_manual_search_parts_for_abarth(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    driver.implicitly_wait(10)
    auto_parts_page.cookies()
    auto_parts_page.finding_parts_manualy('Abarth')
    auto_parts_page.clicking_result_button()
    assert auto_parts_page.abarth_parts_page_opened_manualy()


def test_parts_for_audi(driver):
    auto_parts_page = PartsPage(driver)
    auto_parts_page.open_page()
    auto_parts_page.cookies()
    driver.implicitly_wait(10)
    auto_parts_page.audi_parts()
    auto_parts_page.clicking_result_button()
    assert auto_parts_page.audi_parts_page_opened
    # Этот тест падает. Не выбирает элемент из дропдауна, хотя раньше выбирал и было все ок. В чем дело - непонятно.
