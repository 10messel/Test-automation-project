from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    USERNAME_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name = "login_submit"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')


class ProductPageLocators:
    BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".item.active img")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    IN_STOCK_AVAIL = (By.CSS_SELECTOR, ".product_main .instock")
    WRITE_REVIEW_BUTTON = (By.CSS_SELECTOR, "#write_review")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > .alertinner strong")
    INFO_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
