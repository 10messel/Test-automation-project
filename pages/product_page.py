import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def should_be_product_page(self):
        assert self.is_element_present(*ProductPageLocators.BREADCRUMB), "Breadcrumb is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IMAGE), "Product image is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), "Product title is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        assert self.is_element_present(*ProductPageLocators.IN_STOCK_AVAIL), "In stock available is not presented"
        assert self.is_element_present(*ProductPageLocators.WRITE_REVIEW_BUTTON), "Review button is not presented"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Basket button is not presented"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
