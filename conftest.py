import pytest
import requests
from selenium import webdriver
from pages.login_page import LoginPage
from pages.categories_page import CategoriesPage
from pages.search_cart_page import SearchCart
from pages.main_page import MainPage
import time
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

