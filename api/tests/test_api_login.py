import requests
import pytest
import allure
from api.models.login_model import LoginErrorResponse, LoginDataResponse

@allure.title('Тест Api проверка неправильного Логина или Пароля')
@pytest.mark.parametrize('login, password', [
    ('fgggdb','fgfrw5')
])
def test_api_wrong_login(api_session, login, password, api_login_session):
    headers = api_session['headers']
    session = api_session['session']
    payload = api_login_session['payload']
    login_url = api_login_session['login_url']

    with allure.step('Отправляем Post-запрос на сервер'):
        response = session.post(login_url, data=payload, headers=headers)

    with allure.step('Валидация ответа через Pydantic'):

        try:
            api_obj = LoginErrorResponse.model_validate(response.json())
        except Exception as e:
            pytest.fail(f'Ошибка валидации ответа API: {e}')

    with allure.step('Проверяем содержимое ответа'):

        assert response.status_code == 200
        assert api_obj.status == 'fail'
        assert 'Неправильное имя пользователя или пароль.' in api_obj.errors.auth

@allure.title('Тест Api проверка правильного Логина и Пароля')
@pytest.mark.parametrize('login, password', [
    ('shmalkopress@gmail.com', 'test_password'),
])
def test_api_right_login(api_session, login, password, api_login_session):
    session = api_session['session']
    headers = api_session['headers']
    payload = api_login_session['payload']
    login_url = api_login_session['login_url']

    with allure.step('Отправляем Post-запрос на сервер'):
        response = session.post(login_url, data=payload, headers=headers)

    with allure.step('Валидация ответа через Pydantic'):
        try:
            api_obj = LoginDataResponse.model_validate(response.json())
        except Exception as e:
             pytest.fail(f'Ошибка валидации ответа API: {e}')

    with allure.step('Проверяем содержимое ответа'):

        assert api_obj.status == 'ok'
        assert response.status_code == 200
        assert api_obj.data.redirect_url is not None
