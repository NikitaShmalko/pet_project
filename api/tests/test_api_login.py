import requests
import pytest
import allure
from api.models.login_model import LoginErrorResponse, LoginDataResponse

login_url = 'https://m-g-p.ru/login/'

@allure.title('Тест Api проверка неправильного Логина или Пароля')
@pytest.mark.parametrize('login, password', [
    ('fgggdb','fgfrw5')
])
def test_api_wrong_login(api_session, login, password):
    headers = api_session['headers']
    session = api_session['session']
    payload = {
        'login': login,
        'password': password,
        'wa_auth_login':1,
        'wa_json_mode':1,
        'need_redirects':1
    }

    with allure.step('Отправляем Post-запрос на сервер'):
        response = session.post(login_url, data=payload, headers=headers)

    with allure.step('Валидация ответа через Pydantic'):

        try:
            api_obj = LoginErrorResponse.model_validate(response.json())
        except Exception as e:
            pytest.fail(f'Ошибка валидации ответа API: {e}')


        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        print(api_obj)
        # assert 'Неправильное имя пользователя или пароль.' in

# @allure.title('Тест Api проверка правильного Логина и Пароля')
# @pytest.mark.parametrize('login, password', [
#     ('shmalkopress@gmail.com', 'test_password'),
# ])
# def test_api_right_login(api_session, login, password):
#     session = api_session['session']
#     headers = api_session['headers']
#     payload = {
#                 'login': login,
#                 'password': password,
#                 'wa_auth_login':1,
#                 'wa_json_mode':1,
#                 'need_redirects':1
#     }
#
#     with allure.step('Отправляем Post-запрос на сервер'):
#         response = session.post(login_url, data=payload, headers=headers)
#
#     with allure.step('Проверяем, содержимое ответа и что ответ - словарь'):
#
#         try:
#             api_data = response.json()
#         except ValueError:
#             pytest.fail('Ответ не JSON')
#         print(api_data)
#
#         assert response.status_code == 200
#         assert isinstance(api_data, dict)
#         assert 'redirect_url' in api_data.get('data', {})
