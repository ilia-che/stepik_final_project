from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        expected_url = LoginPageLocators.LOGIN_URL # работает с языком en-gb
        print(current_url)
        print(expected_url)
        # Проверка, что URL страницы соответствует ожиданию
        assert current_url == expected_url, "Login URL is not correct"

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email.send_keys(email)
        register_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        register_password.send_keys(password)
        register_confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        register_confirm_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
