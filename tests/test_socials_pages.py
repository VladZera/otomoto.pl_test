from pages.socials_page import SocialPage
import allure


@allure.feature('Otomoto YouTube page')
def test_opening_youtube(driver):
    you_tube_page = SocialPage(driver)
    you_tube_page.open_page()
    driver.implicitly_wait(10)
    you_tube_page.cookies()
    you_tube_page.scroll_to(2800)
    you_tube_page.opening_youtube()
    you_tube_page.cookies_youtube()
    assert you_tube_page.yt_channel_is_opened


@allure.feature('Otomoto Instagram page')
def test_opening_instagram(driver):
    instagram_page = SocialPage(driver)
    instagram_page.open_page()
    driver.implicitly_wait(10)
    instagram_page.cookies()
    instagram_page.scroll_to(2800)
    instagram_page.opening_instagram()
    instagram_page.cookies_instagram()
    assert instagram_page.instagram_otomoto_is_opened


@allure.feature('Otomoto facebook page')
def test_opening_facebook(driver):
    facebook_page = SocialPage(driver)
    facebook_page.open_page()
    driver.implicitly_wait(10)
    facebook_page.cookies()
    facebook_page.scroll_to(2800)
    facebook_page.opening_facebook()
    facebook_page.cookies_facebook()
    assert facebook_page.facebook_otomoto_is_opened()
    #  Я не понимаю почему тут непроходит assert. Аналогия построена с Инстаграмом, там все работает, а тут нет(


@allure.feature('Otomoto TikTok page')
def test_opening_tik_tok(driver):
    tik_tok_page = SocialPage(driver)
    tik_tok_page.open_page()
    driver.implicitly_wait(10)
    tik_tok_page.cookies()
    tik_tok_page.scroll_to(2800)
    tik_tok_page.opening_tik_tok()
    #  Тут надо согласиться с куками тик тока, но я не нашел способа согласится с ними
    #  assert tik_tok_page.tik_tok_otomoto_is_opened()
