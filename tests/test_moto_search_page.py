from pages.moto_search_page import MotoSearchPage


def test_all_motorcycles_page_is_opened(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.submit_button_clicking()
    assert motorcycles_page.all_motorcycles_page_is_opened()


def test_all_motorcycles_page_is_opened_by_advanced_filter_button(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.advanced_filter_submit_button_clicking()
    assert motorcycles_page.all_motorcycles_page_is_opened()


def test_add_to_favorite_cart(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.submit_button_clicking()
    motorcycles_page.add_to_favorite_click()
    assert motorcycles_page.add_to_favorite_button_is_working


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


def test_ajp_brand_from_the_list(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.ajp_brand_choose()
    motorcycles_page.submit_button_clicking()
    assert motorcycles_page.all_ajp_motos_are_presented()


def test_finding_moto_by_brand_and_price(driver):
    motorcycles_page = MotoSearchPage(driver)
    motorcycles_page.open_page()
    driver.implicitly_wait(10)
    motorcycles_page.cookies()
    motorcycles_page.yamaha_brand_choose()
    motorcycles_page.price_from_10000_choose()
    motorcycles_page.price_for_15000_choose()
    motorcycles_page.submit_button_clicking()
    assert motorcycles_page.yamaha_from_10000_up_to_1500_is_opened()

