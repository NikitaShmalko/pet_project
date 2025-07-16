import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.title('Проверка каталога товаров')
def test_categories(categories, base_url):
    with allure.step('Открываем браузер и переходим на страницу https://m-g-p.ru/'):
        categories.load(base_url)

    with allure.step('Нажимаем на кнопку "Каталог Товаров", выбираем случайный раздел из Каталога и переходим на его страницу'):
        result = categories.choose_catalog()
        item_title = result['item_title']
        catalog_item_title = result['catalog_item_title']

    with allure.step('Проверяем, что названия категории в Каталоге соответствует названию на странице Категории'):
        assert catalog_item_title == item_title
