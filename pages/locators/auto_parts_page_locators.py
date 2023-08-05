from selenium.webdriver.common.by import By

result_button = (By.XPATH, '//*[@data-testid="submit-btn"]')
search_bar = (By.CLASS_NAME, 'ds-search-input')
submit_search = (By.NAME, 'q')
adv = (By.ID, 'megaboardDiv')
advanced_filter_button = (By.XPATH, '//*[@data-testid="advanced-search-link"]')
auto_model_list = (By.CLASS_NAME, 'ooa-14l7e0q')
options = (By.CSS_SELECTOR, '[data-testid="dropdown-item"]')
trust_button = (By.ID, 'onetrust-accept-btn-handler')
dropdown = (By.CSS_SELECTOR, '[data-testid="dropdown-item"]')
model_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[2]')
input_parts_info = (By.ID, 'q')
