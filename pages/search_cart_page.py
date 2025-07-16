from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pages.locators import ProjectLocators
from pages.base_page import BasePage

class SearchCart(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self, product, quantity):
        self.send_keys(ProjectLocators.search_bar, product)
        self.click(ProjectLocators.search_btn)
        self.click(ProjectLocators.search_select)
        self.send_keys(ProjectLocators.quantity_to_cart, Keys.BACKSPACE)
        self.send_keys(ProjectLocators.quantity_to_cart, quantity)
        self.click(ProjectLocators.add_to_cart)

        product_added_to_cart_message = self.get_product_added_to_cart_message()

        self.take_screenshot()
        self.go_to_cart_click()

        quantity_in_cart = self.get_quantity_value_in_cart()
        product_name_in_cart = self.get_product_name_in_cart()
        product_price = self.get_product_price_in_cart()
        total_price = product_price * int(quantity)
        total_price_in_cart = self.get_total_price()

        self.take_screenshot()

        return {
            'product_added_to_cart_message':product_added_to_cart_message,
            'quantity_in_cart': quantity_in_cart,
            'product_name_in_cart': product_name_in_cart,
            'total_price':total_price,
            'total_price_in_cart':total_price_in_cart,
        }

    def remove_from_cart(self):
        self.remove_from_cart_click()
        the_cart_is_empty_message = self.get_the_cart_is_empty_message()
        self.take_screenshot()

        return {
            'the_cart_is_empty_message': the_cart_is_empty_message,
        }

    def get_product_added_to_cart_message(self):
        return self.get_text(ProjectLocators.product_added_to_cart_message)

    def go_to_cart_click(self):
        self.click(ProjectLocators.go_to_cart)

    def get_quantity_value_in_cart(self):
        return self.get_value(ProjectLocators.quantity_value_in_cart)

    def get_total_price(self):
        element =  self.get_text(ProjectLocators.total_price)
        s_clean = ''.join(c for c in element if c.isdigit())
        price_clean = int(s_clean)
        return price_clean

    def remove_from_cart_click(self):
        self.click(ProjectLocators.remove_from_cart)
        self.click(ProjectLocators.remove_from_cart_btn)

    def get_the_cart_is_empty_message(self):
        return self.get_text(ProjectLocators.the_cart_is_empty_message)

    def get_product_name_in_cart(self):
        return self.get_text(ProjectLocators.product_name_in_cart)

    def get_product_price_in_cart(self):
        element = self.get_text(ProjectLocators.product_price)
        s_clean = ''.join(c for c in element if c.isdigit())
        element_clean = int(s_clean)
        return element_clean



