import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.title('Проверка успешного входа')
@pytest.mark.parametrize('username, password', [
('shmalkopress@gmail.com', 'test_password'),
])
def test_login_success(username, password, login_page, base_url):
    with allure.step('Открываем браузер и переходим на страницу https://m-g-p.ru/'):
        login_page.load(base_url)

    with allure.step('Вводим логин и пароль и нажимаем на кнопку "Войти", затем переходим в Профиль'):
        login_set = login_page.login(username, password)
        profile_set = login_page.go_to_profile()

    with allure.step('Проверяем, что в профиле верно отображается: телефон, почта, имя, фамилия'):

        assert 'Вход в личный кабинет' in login_set['window']
        assert 'Nikita' in profile_set['username_in_profile']
        assert 'Shmalko' in profile_set['user_lastname_in_profile']
        assert '+7 (919) 793-46-23' in profile_set['phone_number_in_profile']
        assert 'shmalkopress@gmail.com' in profile_set['email_in_profile']


@allure.title('Проверка неуспешного входа')
@pytest.mark.parametrize('username, password', [
('fgfgfgg', 'gfgfg'),
])
def test_login_failure(username,password, login_page, base_url):
    with allure.step('Открываем браузер и переходим на страницу https://m-g-p.ru/'):
        login_page.load(base_url)

    with allure.step('Вводим логин и пароль и нажимаем на кнопку "Войти"'):
        login_page.login(username, password)
        alert = login_page.get_alert()

    with allure.step('Проверяем сообщение "Неправильное имя пользователя или пароль"'):
        assert 'Неправильное имя пользователя или пароль' in alert['error_text']
