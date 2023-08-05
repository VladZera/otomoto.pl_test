from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from pages.locators import socials_pages_locators as loc


class SocialPage(BasePage):
    page_url = '/'

    def opening_youtube(self):
        self.find(loc.youtube_icon).click()

    def yt_channel_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.yt_channel_link))
        print('Everything is fine')

    def opening_instagram(self):
        self.find(loc.instagram_icon).click()

    def opening_tik_tok(self):
        self.find(loc.tik_tok_icon).click()

    def cookies_instagram(self):
        try:
            button_cookie = self.find(loc.cookies)
            button_cookie.click()
        except NoSuchElementException:
            pass

    def cookies_youtube(self):
        try:
            you_tube_cookies = self.find(loc.cookies_youtube)
            you_tube_cookies.click()
        except NoSuchElementException:
            pass

    def cookies_facebook(self):
        try:
            facebook_cookies = self.find(loc.cookies_facebook)
            facebook_cookies.click()
        except NoSuchElementException:
            pass

    def instagram_otomoto_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.ig_page_link))
        return True

    def tik_tok_otomoto_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(loc.tik_tok_page_link))
        return True

    def facebook_otomoto_is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains(loc.facebook_page_link))
        return True

    def opening_facebook(self):
        self.find(loc.facebook_icon).click()

    def cookies_facebook_2(self):
        try:
            button_cookie = self.find(loc.facebook_cookie_button)
            button_cookie.click()
        except NoSuchElementException:
            pass

    def facebook_log_in_cancel(self):
        self.find(loc.facebook_cancel_log_in).click()
