from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    USERNAME_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name = "login_submit"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')
