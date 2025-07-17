import pytest
import requests
from selenium import webdriver
from pages.login_page import LoginPage
from pages.categories_page import CategoriesPage
from pages.search_cart_page import SearchCart
from pages.main_page import MainPage
import allure

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver=webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def search(driver):
    return SearchCart(driver)

@pytest.fixture
def categories(driver):
    return CategoriesPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def base_url():
    return 'https://m-g-p.ru/'

@pytest.fixture
def api_session(base_url):
    session = requests.Session()
    session.get(base_url)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://m-g-p.ru/',
    }

    return {
        'session': session,
        'headers': headers
    }

@pytest.fixture
def api_login_session(login, password):
    login_url = 'https://m-g-p.ru/login/'
    payload = {
        'login': login,
        'password': password,
        'wa_auth_login':1,
        'wa_json_mode':1,
        'need_redirects':1
    }
    return {
        'login_url': login_url,
        'payload': payload
    }

