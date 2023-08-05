from selenium.webdriver.common.by import By

auto_title = (By.CLASS_NAME, 'ev5apm51')
sell_button = (By.CLASS_NAME, 'e1lnywgt0')
create_sale_car_button = (By.CLASS_NAME, 'ooa-1wc438x')
recommendation_price_button = (By.CLASS_NAME, 'erf630y0')
recommendation_price_button_submit = (By.CLASS_NAME, 'ooa-cnxk22')
trust_accept = (By.ID, 'onetrust-accept-btn-handler')
dropdown = (By.ID, 'onetrust-accept-btn-handler')
submit_button = (By.XPATH, '//*[@data-testid="submit-btn"]')
brand_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[2]')
model_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[3]')
generation_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[4]')
price_from_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[5]')
price_up_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[6]')
year_from_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[7]')
year_up_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[8]')
fuel_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[9]')
mileage_from_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[10]')
mileage_up_choose = (By.XPATH, '(//*[@data-testid="dropdown-expand-button"])[11]')
bmw_01_02 = 'https://www.otomoto.pl/osobowe/bmw/od-2001?search%5Bfilter_float_year%3Ato%5D=2002'
all_diesel_bmw = 'https://www.otomoto.pl/osobowe/bmw?search%5Bfilter_enum_fuel_type%5D=diesel'
all_bmw = 'https://www.otomoto.pl/osobowe/bmw'
scirocco_benzin = 'https://www.otomoto.pl/osobowe/volkswagen/scirocco?search%5Bfilter_enum_fuel_type%5D=petrol'
all_scirocco = 'https://www.otomoto.pl/osobowe/volkswagen'
sciroco_with_main = 'https://www.otomoto.pl/osobowe/volkswagen/scirocco/od-2008?search%5Bfilter_float_price%3Afrom' \
                    '%5D=2000&search%5Bfilter_float_price%3Ato%5D=200000'
all_scirocco_cars_are_presented = 'https://www.otomoto.pl/osobowe/volkswagen/scirocco'
