from selenium.webdriver.common.by import By

submit_button = (By.XPATH, '//*[@data-testid="submit-btn"]')
advanced_filters_button = (By.XPATH, '//*[@data-testid="advanced-search-link"]')
sign_in_button = (By.XPATH, '//*[@data-testid="sign-in-button"]')
add_to_favorite = (By.CLASS_NAME, 'e1t8pd740')
more_filters_button = (By.CLASS_NAME, 'ooa-1tn9tf5')
manual_search_bar = (By.CSS_SELECTOR, '[aria-label="Wpisz model, wersję lub inne szczegóły"]')
submit_search_bar_button = (By.CLASS_NAME, 'ooa-10ry9s3')
dropdown = (By.CSS_SELECTOR, '[data-testid="dropdown-item"]')
model_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[2]')
price_from = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[4]')
price_for = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[5]')
yamaha_r125_is_opened = 'https://www.otomoto.pl/motocykle-i-quady' \
                        '/q-Yamaha-R125?search%5Badvanced_search_expanded%5D=true'
ajp_moto = 'https://www.otomoto.pl/motocykle-i-quady/ajp'
yamaha_with_price_filter = 'https://www.otomoto.pl/motocykle-i-quady/yamaha?search%5Bfilter_float_price%3Afrom%5D=' \
                           '10000&search%5Bfilter_float_price%3Ato%5D=15000'
