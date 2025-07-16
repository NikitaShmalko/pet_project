from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import random
import time

from pages.base_page import BasePage
from pages.locators import ProjectLocators

class CategoriesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_catalog_btn(self):
        self.click(ProjectLocators.catalog_btn)

    def click_catalog_item_title(self):
        self.click(ProjectLocators.catalog_item_title)

    def get_catalog_item_title(self):
        return self.get_text(ProjectLocators.catalog_item_title)

    def get_item_title(self):
        return self.get_text(ProjectLocators.item_title)

    def catalog_window_is_located(self):
        return self.element_located(ProjectLocators.catalog_window)

    def choose_catalog(self):
        self.click_catalog_btn()
        time.sleep(0.2)
        self.take_screenshot()
        catalog_item_title = self.get_catalog_item_title()
        self.click_catalog_item_title()
        time.sleep(0.2)
        self.take_screenshot()
        item_title = self.get_item_title()

        return {
            'catalog_item_title':catalog_item_title,
            'item_title': item_title,
        }