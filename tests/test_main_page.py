import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.locators import ProjectLocators

@allure.title('Проверка работы кнопки прокрутки вверх')
def test_main_page_up_button(main_page, base_url):
    with allure.step('Открываем браузер и переходим на страницу https://m-g-p.ru/'):
        main_page.load(base_url)

    with allure.step('Прокручиваем страницу вниз на 2000 пикселей и нажимаем кнопку "Вверх"'):
        scroll_position = main_page.zero_scroll_position(2000)

    with allure.step('Проверяем, что кнопка вернула страницу в нулевое положение'):
        main_page.take_screenshot()
        assert scroll_position == 0

@allure.title('Проверка работы ссылок соц. сетей')
@pytest.mark.parametrize('social_network_url, locator, name',[
    ('https://t.me/mgp495', ProjectLocators.telegram_btn, 'Telegram'),
    ('https://vk.com/magazingidravliki',ProjectLocators.vk_btn, 'VK'),
    ('https://api.whatsapp.com/send/?phone=79618801466&text&type=phone_number&app_absent=0',ProjectLocators.whatsapp_btn, 'WhatsApp'),
    ('https://rutube.ru/channel/60803933/',ProjectLocators.rutube_btn, 'RUTUBE'),
])

def test_main_social_networks_links(main_page, driver, base_url,social_network_url, locator, name):
    with allure.step('Открываем браузер и переходим на страницу https://m-g-p.ru/'):
        main_page.load(base_url)

    with allure.step(f'Переход в {name}'):
        main_page.go_to_link(locator)

    with allure.step('Проверяем url'):
        assert driver.current_url == social_network_url
