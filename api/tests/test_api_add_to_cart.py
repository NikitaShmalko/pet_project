import requests
import pytest
import allure

from api.models.add_to_cart_model import AddToCartResponse

cart_url = 'https://m-g-p.ru/cart/add/'

@allure.title('Тест Api добавления товара в корзину')
@pytest.mark.parametrize('quantity, product_id', [
    (1, 933), (2, 930), (3, 931), (4, 936), (5, 929)
])
def test_add_to_cart_api(quantity, product_id, api_session):
    session = api_session['session']
    headers = api_session['headers']
    payload = {
        'product_id': product_id,
        'features[2]': 5,
        'quantity': quantity,
        'html':'true'
    }

    with allure.step('Отправляем POST-запрос на сервер'):

        response = session.post(cart_url, data=payload, headers=headers)

    with allure.step('Валидация ответа через Pydantic'):

        try:
            api_obj = AddToCartResponse.model_validate(response.json())
        except Exception as e:
            pytest.fail(f'Ошибка валидации ответа API: {e}')

    with allure.step('Проверяем содержимое ответа'):

        assert response.status_code == 200
        assert api_obj.status == 'ok'
        assert api_obj.data.count == payload['quantity']
        assert api_obj.data.total is not None