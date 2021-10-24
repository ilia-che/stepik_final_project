from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                        # открываем страницу
    page.add_product_to_basket()       # добавляем товар в корзину
    page.solve_quiz_and_get_code()     # решаем новогодний квиз
    page.should_be_same_price()        # проверяем правильность цены товара в сообщении
    page.should_be_same_name()         # проверяем правильность названия товара в сообщении
