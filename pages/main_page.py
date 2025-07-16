from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from pages.base_page import BasePage
from pages.locators import ProjectLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def catalog_link(self, index):
        return self.driver.find_element(By.XPATH, f'(//a[@class="catalog-list__link"])[{index}]')

    def get_all_catalog_links(self):
        return self.driver.find_elements(ProjectLocators.catalog_link_list)

    def call_us_btn_check(self):
        self.click(ProjectLocators.call_us_btn)

    def go_to_link(self, locator):
        self.click(locator)
        self.switch_window()
        self.take_screenshot()
