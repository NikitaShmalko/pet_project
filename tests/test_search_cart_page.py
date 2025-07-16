import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.title('Проверка добавления товаров в Корзины')

@pytest.mark.parametrize('product, quantity', [
    ('ВЕ 6.34', '2'),
    ('ВЕ 6.574', '3'),
    ('ВЕ 6.134', '5'),
    ('ВЕ 10.574', '6'),
])

def test_search(search, product, quantity, base_url):
    with allure.step('Открываем браузер и переходим на страницу https://m-g-p.ru/'):
        search.load(base_url)

    with allure.step('Ищем и добавляем Товар в Козину, переходим в Корзину и удаляем Товар'):
        add_to_cart = search.add_product_to_cart(product, quantity)
        remove_from_cart = search.remove_from_cart()

    with allure.step('Проверяем, что наименование Товара, кол-во, итоговая цена отображается правильно, а также появляется сообщение после удаления Товара из корзины'):

        assert 'Товар добавлен в корзину' in add_to_cart['product_added_to_cart_message']
        assert add_to_cart['total_price'] == add_to_cart['total_price_in_cart']
        assert add_to_cart['quantity_in_cart'] == quantity
        assert product in add_to_cart['product_name_in_cart']
        assert 'Ваша корзина пуста' in remove_from_cart['the_cart_is_empty_message']