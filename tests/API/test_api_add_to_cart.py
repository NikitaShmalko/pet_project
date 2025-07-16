import requests
import pytest
import allure

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

    with allure.step('Отправляем запрос на сервер'):
        response = session.post(cart_url, data=payload, headers=headers)


    with allure.step('Проверяем, что статус = ОК, кол-во в payload = кол-во в api_data'):
        try:
            api_data = response.json()
        except ValueError:
            pytest.fail('Ответ не JSON')

        assert response.status_code == 200
        assert api_data.get('status') == 'ok'
        assert api_data.get('data', {}).get('count') == payload['quantity']
        assert 'total' in api_data.get('data')