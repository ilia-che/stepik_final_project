from .base_page import BasePage
from .login_page import LoginPage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BTN)
        add_to_basket.click()

    def should_be_same_price(self):
        product_price = self.element_text(*ProductPageLocators.PRODUCT_PRICE)
        price_in_message = self.element_text(*ProductPageLocators.PRODUCT_ADDED_PRICE_MESSAGE)
        assert product_price == price_in_message, "Incorrect price of product in message"

    def should_be_same_name(self):
        product_name = self.element_text(*ProductPageLocators.PRODUCT_NAME)
        print(product_name)
        product_name_in_message = self.element_text(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE)
        print(product_name_in_message)
        assert product_name == product_name_in_message, "Incorrect name of product in message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"