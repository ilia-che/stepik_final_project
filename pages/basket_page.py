from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_basket_items()
        self.should_be_empty_basket_message()

    def should_not_be_basket_items(self):
        # Проверка на отсутствие товаров в корзине
        assert self.is_not_element_present(*BasketPageLocators.FIRST_ITEM_IN_BASKET), \
            "Item is in empty basket"

    def should_be_empty_basket_message(self):
        # Проверка на наличие сообщения о пустой корзине с гиперсылкой на страницу товаров
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE_HYPERLINK), \
            "Empty basket message is not presented"
