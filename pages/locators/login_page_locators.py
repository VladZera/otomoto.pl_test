from selenium.webdriver.common.by import By

user_email = (By.NAME, 'username')
user_passwd = (By.NAME, 'password')
error_text_email = (By.CLASS_NAME, 'css-sf6wsj')
error_text_passwd = (By.CLASS_NAME, 'css-sf6wsj')
login_button = (By.CLASS_NAME, 'css-1m3y0q6')
email_not_registered = (By.CLASS_NAME, 'css-1kd8jyo')
login_button_click = (By.XPATH, '//*[@data-testid="login-submit-button"]')
cookies = (By.ID, 'onetrust-accept-btn-handler')