from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def login_user(self):
        fields = self.browser.find_elements_by_css_selector("#login_form input[required]")
        values = ['ivan.ivanov@gmail.com', 'testpassword']
        for i, j in enumerate(fields):
            j.send_keys(values[i])
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def register_new_user(self):
        fields = self.browser.find_elements_by_css_selector("#register_form input[required]")
        values = ['ivan.ivanov@gmail.com', 'testpassword', 'testpassword']
        for i, j in enumerate(fields):
            j.send_keys(values[i])
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

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
