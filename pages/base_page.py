from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import allure
import time

from pages.locators import ProjectLocators

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("""
            arguments[0].scrollIntoView({ 
                behavior: 'instant',  // или 'smooth'
                block: 'center'
            });
        """, element)

    def take_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    def click(self, locator):
        self.scroll_to_element(locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        self.scroll_to_element(locator)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        self.scroll_to_element(locator)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
        return element

    def get_value(self, locator):
        self.scroll_to_element(locator)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).get_attribute('value')
        return element

    def load(self, url):
        self.driver.get(url)

    def element_located(self, locator):
        self.scroll_to_element(locator)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def scroll(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0,{pixels});")
        # скролл вниз на n пикселей

    def zero_scroll_position(self, pixels):
        self.scroll(pixels)
        self.click(ProjectLocators.btn_up)
        time.sleep(1)
        scroll_position = self.screen_position()
        return scroll_position

    def screen_position(self):
        return self.driver.execute_script("return window.pageYOffset;")

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def switch_window(self):
        time.sleep(0.3)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def switch_window_back(self):
        windows = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    def assert_text_in_element(self, text, element):
        assert text in element
