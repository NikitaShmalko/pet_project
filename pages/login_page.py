from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

from pages.base_page import BasePage
from pages.locators import ProjectLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self,username, password):
        self.click(ProjectLocators.login_btn)
        self.send_keys(ProjectLocators.username_input, username)
        self.send_keys(ProjectLocators.password_input, password)
        window =  self.get_text(ProjectLocators.enter_login_window)
        self.take_screenshot()
        time.sleep(0.3)
        self.click(ProjectLocators.submit_btn)

        return {
            'window': window,
        }

    def go_to_profile(self):
        self.click_my_profile_btn()
        username_in_profile = self.get_username()
        user_lastname_in_profile = self.get_user_lastname()
        phone_number_in_profile = self.get_phone()
        email_in_profile = self.get_email()
        self.take_screenshot()

        return {
            'username_in_profile': username_in_profile,
            'user_lastname_in_profile': user_lastname_in_profile,
            'phone_number_in_profile': phone_number_in_profile,
            'email_in_profile': email_in_profile,
        }

    def click_my_profile_btn(self):
        self.click(ProjectLocators.my_profile_link)

    def get_alert(self):
        error_text = self.get_text(ProjectLocators.alert)
        self.take_screenshot()
        return {
            'error_text': error_text,
        }

    def profile_link_click(self):
        self.click(ProjectLocators.my_profile_link)

    def get_username(self):
        return self.get_text(ProjectLocators.username_in_profile)

    def get_user_lastname(self):
        return self.get_text(ProjectLocators.user_lastname_in_profile)

    def get_phone(self):
        return self.get_text(ProjectLocators.phone_number)

    def get_email(self):
        return self.get_text(ProjectLocators.email)




