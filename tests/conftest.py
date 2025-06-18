import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from curl import MainUrl
from data import Credentials
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.set_window_size(1920, 1080)
        driver.get(MainUrl.main_site)
    elif request.param == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.set_window_size(1280, 720)
        driver.get(MainUrl.main_site)
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):
    """
    Фикстура для авторизации пользователя.
    """
    auth_page = AuthPage(driver)
    auth_page.auth(Credentials.email,Credentials.password)

    return driver
