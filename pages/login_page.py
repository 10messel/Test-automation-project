from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.USERNAME_FIELD), "Username field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), "Password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), "Email field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD1_FIELD), "Password1 field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD2_FIELD), "Password2 field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"
