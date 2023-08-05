from selenium.webdriver.common.by import By

facebook_icon = (By.LINK_TEXT, 'Facebook')
facebook_cancel_log_in = (By.CLASS_NAME, 'x92rtbv')
instagram_icon = (By.LINK_TEXT, 'Instagram')
instagram_otomoto_page = (By.XPATH, '//button[contains(@class, "x1lliihq")]')
youtube_icon = (By.LINK_TEXT, 'YouTube')
yt_channel = (By.LINK_TEXT, 'OTOMOTO TV - Kanał Motoryzacyjny')
tik_tok_icon = (By.LINK_TEXT, 'TikTok')
cookies = (By.CLASS_NAME, '_a9_0')
cookies_youtube = (By.CSS_SELECTOR, '[aria-label="Принять все"]')
cookies_facebook = (By.CSS_SELECTOR, '[aria-label="Разрешить все cookie"]')
yt_channel_link = 'https://www.youtube.com/user/otomotopl'
ig_page_link = 'https://www.instagram.com/otomotopl/'
tik_tok_page_link = 'https://www.tiktok.com/@otomotopl'
facebook_page_link = 'https://www.facebook.com/otomotopl/'
facebook_cookie_button = (By.XPATH, "//button[contains(string(), 'Allow essential and optional cookies')]")
