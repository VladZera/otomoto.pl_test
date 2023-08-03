from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

facebook_icon = (By.LINK_TEXT, 'Facebook')
facebook_cancel_log_in = (By.CLASS_NAME, 'x92rtbv')
instagram_icon = (By.LINK_TEXT, 'Instagram')
instagram_otomoto_page = ((By.XPATH, '//button[contains(@class, "x1lliihq")]'))
youtube_icon = (By.LINK_TEXT, 'YouTube')
yt_channel = (By.LINK_TEXT, 'OTOMOTO TV - Kanał Motoryzacyjny')
tik_tok_icon = (By.LINK_TEXT, 'TikTok')


class SocialPage(BasePage):
    page_url = '/'

    def opening_youtube(self):
        self.find(youtube_icon).click()

    def yt_channel_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.youtube.com/user/otomotopl'))
        print('Everything is fine')

    def opening_instagram(self):
        self.find(instagram_icon).click()

    def opening_tik_tok(self):
        self.find(tik_tok_icon).click()

    def cookies_instagram(self):
        try:
            button_cookie = self.find((By.CLASS_NAME, '_a9_0'))
            button_cookie.click()
        except NoSuchElementException:
            pass

    def cookies_youtube(self):
        try:
            you_tube_cookies = self.find((By.CSS_SELECTOR, '[aria-label="Принять все"]'))
            you_tube_cookies.click()
        except NoSuchElementException:
            pass

    def cookies_facebook(self):
        try:
            facebook_cookies = self.find((By.CSS_SELECTOR, '[aria-label="Разрешить все cookie"]'))
            facebook_cookies.click()
        except NoSuchElementException:
            pass

    def instagram_otomoto_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.instagram.com/otomotopl/'))
        return True

    def tik_tok_otomoto_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be('https://www.tiktok.com/@otomotopl'))
        return True

    def facebook_otomoto_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains('https://www.facebook.com/otomotopl/'))
        return True

    def opening_facebook(self):
        self.find(facebook_icon).click()

    def cookies_facebook_2(self):
        try:
            button_cookie = self.find((By.XPATH, "//button[contains(string(), 'Allow essential and optional cookies')]"))
            button_cookie.click()
        except NoSuchElementException:
            pass

    def facebook_log_in_cancel(self):
        self.find(facebook_cancel_log_in).click()



