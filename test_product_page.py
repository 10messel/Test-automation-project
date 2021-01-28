import time
import pytest
from .pages.product_page import ProductPage


@pytest.mark.smoke
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(3)
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3)
