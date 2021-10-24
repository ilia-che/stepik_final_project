from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/" # URL английской версии страницы
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")  # кнопка добавить в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")  # название товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")  # цена товара
    PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert:first-of-type strong")  # сообщение о дабавлении товара в корзину
    PRODUCT_ADDED_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")  # сообщение о цене товаров в корзине
